#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simulation Flux Poussé vs Flux Tiré (Kanban)
============================================
Formation BTS ATI - Organisation Industrielle & Lean
Pôle Formation UIMM CVDL | Formateur : S. Jaubert

Dépendances : pip install matplotlib numpy pillow
"""

import tkinter as tk
from tkinter import ttk, font as tkfont
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import random
import os
import sys
from dataclasses import dataclass, field
from typing import List

# ---------------------------------------------------------------------------
# PALETTE COULEURS UIMM
# ---------------------------------------------------------------------------
C = {
    "bleu_uimm":   "#1a3a5c",
    "rouge_uimm":  "#c8102e",
    "blanc":       "#ffffff",
    "fond":        "#f4f6f8",
    "panneau":     "#ffffff",
    "push":        "#e74c3c",
    "pull":        "#27ae60",
    "stock_haut":  "#e74c3c",
    "stock_moyen": "#f39c12",
    "stock_bas":   "#27ae60",
    "incident":    "#c0392b",
    "gris_clair":  "#ecf0f1",
    "gris":        "#95a5a6",
    "texte":       "#2c3e50",
}

STATION_NAMES  = ["Usinage", "Assemblage", "Contrôle"]
STOCK_LABELS   = ["M.P.", "En-cours 1", "En-cours 2", "Stock P.F."]

# ---------------------------------------------------------------------------
# MOTEUR DE SIMULATION
# ---------------------------------------------------------------------------

@dataclass
class SimParams:
    """Tous les paramètres ajustables de la simulation."""
    demand_mean:          float = 8.0
    demand_cv:            float = 0.30   # coefficient de variation
    capacities:           List[float] = field(default_factory=lambda: [10.0, 9.0, 9.0])
    initial_stocks:       List[int]   = field(default_factory=lambda: [40, 25, 20, 20])
    kanban_counts:        List[int]   = field(default_factory=lambda: [6, 6, 6])
    kanban_lot_size:      int   = 3
    incident_prob:        float = 0.12
    incident_max_dur:     int   = 3
    mode:                 str   = "push"   # "push" | "pull"
    speed_ms:             int   = 800      # ms entre deux périodes


class SimulationEngine:
    """
    Moteur discret période par période.

    Flux poussé : chaque poste produit à sa capacité nominale sans attendre
    la demande aval (logique MRP/planning).

    Flux tiré   : la production n'est autorisée que si un ticket kanban est
    disponible ; les tickets circulent du client vers les postes amont.
    """

    def __init__(self, params: SimParams):
        self.p = params
        self.reset()

    def reset(self):
        p = self.p
        self.t = 0

        # Stocks  [MP, EC1, EC2, PF]
        self.stocks = list(p.initial_stocks)

        # Etat des postes (0 = libre, >0 = en incident, nb périodes restantes)
        self.busy = [0, 0, 0]

        # Capacité réellement utilisée cette période
        self.cap_used = [0.0, 0.0, 0.0]

        # Tickets kanban disponibles par boucle [boucle1, boucle2, boucle3]
        # Boucle i relie poste i+1 au stock i+1
        self.kanbans = list(p.kanban_counts)

        # Backlog client (commandes non honorées reportées)
        self.backlog = 0

        # Historiques
        self.time_hist      = []
        self.stock_hist     = [[], [], [], []]
        self.demand_hist    = []
        self.delivered_hist = []
        self.service_hist   = []
        self.eff_hist       = [[], [], []]
        self.incident_hist  = []   # liste de (t, station_idx)
        self.events_log     = []   # messages texte

        self.total_demand    = 0
        self.total_delivered = 0
        self.total_incidents = 0

    # ------------------------------------------------------------------
    def step(self) -> dict:
        """Avance d'une période et retourne les événements."""
        p = self.p
        self.t += 1
        ev = {
            "t":        self.t,
            "incidents": [],
            "produced": [0, 0, 0],
            "demand":   0,
            "delivered": 0,
            "backlog":  0,
        }

        # 1. Réapprovisionnement fournisseur (livraison continue selon cadence P1)
        self.stocks[0] += int(p.capacities[0])

        # 2. Incidents aléatoires
        for i in range(3):
            if self.busy[i] > 0:
                self.busy[i] -= 1
            elif random.random() < p.incident_prob:
                dur = random.randint(1, p.incident_max_dur)
                self.busy[i] = dur
                self.total_incidents += 1
                ev["incidents"].append({"station": i, "duration": dur})
                self.incident_hist.append((self.t, i))

        # 3. Production
        if p.mode == "push":
            self._produce_push(ev)
        else:
            self._produce_pull(ev)

        # 4. Demande client et livraison depuis stock PF
        demand = self._generate_demand()
        self.total_demand += demand
        ev["demand"] = demand

        to_fulfill = demand + self.backlog
        delivered  = min(to_fulfill, self.stocks[3])
        self.stocks[3] -= delivered
        self.backlog    = max(0, to_fulfill - delivered)
        self.total_delivered += delivered
        ev["delivered"] = delivered
        ev["backlog"]   = self.backlog

        # 4. En flux tiré : la consommation du PF libère des tickets vers P3
        if p.mode == "pull":
            released = delivered // p.kanban_lot_size
            self.kanbans[2] = min(self.kanbans[2] + released, p.kanban_counts[2])

        # 5. Enregistrement
        self.time_hist.append(self.t)
        self.demand_hist.append(demand)
        self.delivered_hist.append(delivered)
        for i, s in enumerate(self.stocks):
            self.stock_hist[i].append(s)
        svc = self.total_delivered / max(self.total_demand, 1)
        self.service_hist.append(svc)
        for i in range(3):
            eff = self.cap_used[i] / max(p.capacities[i], 1)
            self.eff_hist[i].append(min(eff, 1.0))

        ev["stocks"]  = list(self.stocks)
        ev["kanbans"] = list(self.kanbans)
        ev["service"] = svc
        return ev

    # ------------------------------------------------------------------
    def _generate_demand(self) -> int:
        p = self.p
        val = int(np.random.normal(p.demand_mean, p.demand_mean * p.demand_cv))
        return max(0, val)

    def _produce_push(self, ev):
        """Chaque poste produit au max de sa capacité sans attendre l'aval.
        Snapshot des stocks en début de période : production simultanée réaliste
        (une pièce ne peut pas traverser deux postes dans la même période)."""
        p = self.p
        snapshot = list(self.stocks)   # lecture avant toute production
        for i in range(3):
            if self.busy[i] > 0:
                self.cap_used[i] = 0
                continue
            produced = max(0, int(min(p.capacities[i], snapshot[i])))
            self.stocks[i]     -= produced
            self.stocks[i + 1] += produced
            self.cap_used[i]    = produced
            ev["produced"][i]   = produced

    def _produce_pull(self, ev):
        """
        Production déclenchée de l'aval vers l'amont.
        Poste i produit seulement si un ticket kanban de la boucle i est dispo.
        """
        p = self.p
        order = [2, 1, 0]   # traitement aval -> amont pour propager les tickets
        for i in order:
            if self.busy[i] > 0:
                self.cap_used[i] = 0
                continue
            if self.kanbans[i] <= 0:
                self.cap_used[i] = 0
                continue

            lot       = p.kanban_lot_size
            max_prod  = min(p.capacities[i], self.stocks[i], self.kanbans[i] * lot)
            produced  = max(0, int(max_prod))
            if produced == 0:
                self.cap_used[i] = 0
                continue

            lots_used         = max(1, produced // lot)
            self.kanbans[i]  -= lots_used
            self.stocks[i]   -= produced
            self.stocks[i+1] += produced
            self.cap_used[i]  = produced
            ev["produced"][i] = produced

            # La consommation du stock amont libère les tickets de la boucle en amont
            if i > 0:
                self.kanbans[i-1] = min(
                    self.kanbans[i-1] + lots_used,
                    p.kanban_counts[i-1]
                )

    # ------------------------------------------------------------------
    @property
    def taux_service(self) -> float:
        return self.total_delivered / max(self.total_demand, 1)

    @property
    def stock_total(self) -> int:
        return sum(self.stocks)

    @property
    def efficience_moyenne(self) -> float:
        n = len(self.eff_hist[0])
        if n == 0:
            return 0.0
        return float(np.mean([np.mean(self.eff_hist[i]) for i in range(3)]))


# ---------------------------------------------------------------------------
# INTERFACE GRAPHIQUE
# ---------------------------------------------------------------------------

class KanbanApp:
    """Application principale Tkinter."""

    # Dimensions VSM
    VSM_W, VSM_H = 960, 240

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Simulation Flux Poussé / Flux Tiré (Kanban)")
        self.root.configure(bg=C["fond"])
        self.root.resizable(True, True)

        self.params = SimParams()
        self.engine = SimulationEngine(self.params)
        self.running = False
        self._after_id = None

        # Variables Tkinter pour les paramètres
        self._init_tk_vars()

        # Construction de l'interface
        self._build_header()
        self._build_main()

        # Premier dessin
        self.update_vsm()
        self.update_charts()
        self.update_kpis()

    # ---------------------------------------------------------------
    # Variables Tkinter
    # ---------------------------------------------------------------
    def _init_tk_vars(self):
        p = self.params
        self.var_mode    = tk.StringVar(value=p.mode)
        self.var_demand  = tk.DoubleVar(value=p.demand_mean)
        self.var_cv      = tk.DoubleVar(value=p.demand_cv)
        self.var_cap     = [tk.DoubleVar(value=c) for c in p.capacities]
        self.var_kanban  = [tk.IntVar(value=k) for k in p.kanban_counts]
        self.var_lot     = tk.IntVar(value=p.kanban_lot_size)
        self.var_inc     = tk.DoubleVar(value=p.incident_prob)
        self.var_speed   = tk.IntVar(value=p.speed_ms)

    # ---------------------------------------------------------------
    # HEADER
    # ---------------------------------------------------------------
    def _build_header(self):
        hdr = tk.Frame(self.root, bg=C["bleu_uimm"], pady=6)
        hdr.pack(fill=tk.X)

        # Logo (optionnel)
        logo_paths = [
            os.path.join(os.path.dirname(__file__), "logo_uimm.png"),
            os.path.join(os.path.dirname(__file__), "logo_uimm.jpg"),
            os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "..", "..", "..", "BTS ATI", "Administratif ATI",
                         ".claude", "logo_uimm_placeholder.jpg"),
        ]
        self._logo_img = None
        for lp in logo_paths:
            try:
                from PIL import Image, ImageTk
                img = Image.open(lp).convert("RGBA")
                h = 52
                w = int(img.width * h / img.height)
                img = img.resize((w, h), Image.LANCZOS)
                self._logo_img = ImageTk.PhotoImage(img)
                tk.Label(hdr, image=self._logo_img, bg=C["bleu_uimm"]).pack(
                    side=tk.LEFT, padx=12)
                break
            except Exception:
                pass

        # Titre central
        center = tk.Frame(hdr, bg=C["bleu_uimm"])
        center.pack(side=tk.LEFT, expand=True)
        tk.Label(center,
                 text="SIMULATION FLUX POUSSÉ  /  FLUX TIRÉ (KANBAN)",
                 bg=C["bleu_uimm"], fg=C["blanc"],
                 font=("Helvetica", 15, "bold")).pack()
        tk.Label(center,
                 text="Organisation Industrielle — BTS ATI",
                 bg=C["bleu_uimm"], fg="#adc6e0",
                 font=("Helvetica", 10)).pack()

        # Formateur (droite)
        right = tk.Frame(hdr, bg=C["bleu_uimm"])
        right.pack(side=tk.RIGHT, padx=16)
        tk.Label(right, text="Pôle Formation - UIMM CVDL",
                 bg=C["bleu_uimm"], fg=C["blanc"],
                 font=("Helvetica", 9, "bold")).pack(anchor=tk.E)
        tk.Label(right, text="Formateur : S. Jaubert",
                 bg=C["bleu_uimm"], fg="#adc6e0",
                 font=("Helvetica", 9)).pack(anchor=tk.E)

        # Barre rouge sous le header
        tk.Frame(self.root, bg=C["rouge_uimm"], height=4).pack(fill=tk.X)

    # ---------------------------------------------------------------
    # LAYOUT PRINCIPAL
    # ---------------------------------------------------------------
    def _build_main(self):
        main = tk.Frame(self.root, bg=C["fond"])
        main.pack(fill=tk.BOTH, expand=True, padx=8, pady=6)

        # Colonne gauche : paramètres
        left = tk.Frame(main, bg=C["panneau"], bd=1, relief=tk.GROOVE, width=220)
        left.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 6))
        left.pack_propagate(False)
        self._build_params(left)

        # Colonne centrale : VSM + contrôles + log
        center = tk.Frame(main, bg=C["fond"])
        center.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self._build_controls(center)
        self._build_vsm(center)
        self._build_log(center)

        # Colonne droite : KPI + graphiques
        right = tk.Frame(main, bg=C["panneau"], bd=1, relief=tk.GROOVE, width=300)
        right.pack(side=tk.RIGHT, fill=tk.Y, padx=(6, 0))
        right.pack_propagate(False)
        self._build_kpis(right)
        self._build_charts(right)

    # ---------------------------------------------------------------
    # PANNEAU PARAMÈTRES
    # ---------------------------------------------------------------
    def _build_params(self, parent):
        tk.Label(parent, text="PARAMÈTRES", bg=C["bleu_uimm"], fg=C["blanc"],
                 font=("Helvetica", 10, "bold"), pady=4).pack(fill=tk.X)

        scroll = tk.Frame(parent, bg=C["panneau"])
        scroll.pack(fill=tk.BOTH, expand=True, padx=6, pady=4)

        def section(txt):
            tk.Label(scroll, text=txt, bg=C["gris_clair"], fg=C["bleu_uimm"],
                     font=("Helvetica", 9, "bold"), anchor=tk.W, padx=4).pack(
                fill=tk.X, pady=(8, 2))

        def row(parent, label, var, frm, to, step, fmt="{:.1f}", is_int=False):
            f = tk.Frame(parent, bg=C["panneau"])
            f.pack(fill=tk.X, pady=1)
            tk.Label(f, text=label, bg=C["panneau"], fg=C["texte"],
                     font=("Helvetica", 8), width=14, anchor=tk.W).pack(side=tk.LEFT)
            val_lbl = tk.Label(f, text=fmt.format(var.get()),
                               bg=C["panneau"], fg=C["bleu_uimm"],
                               font=("Helvetica", 8, "bold"), width=4)
            val_lbl.pack(side=tk.RIGHT)

            def on_change(v, lbl=val_lbl, variable=var, f=fmt):
                try:
                    lbl.config(text=f.format(variable.get()))
                    self._apply_params()
                except Exception:
                    pass

            sl = ttk.Scale(f, from_=frm, to=to, variable=var,
                           orient=tk.HORIZONTAL, length=80,
                           command=on_change)
            sl.pack(side=tk.RIGHT, padx=2)

        # --- Demande client ---
        section("Demande client")
        row(scroll, "Moyenne (u/p)", self.var_demand, 2, 20, 0.5)
        row(scroll, "Variabilité", self.var_cv, 0.0, 0.8, 0.05,
            fmt="{:.0%}")

        # --- Cadences ---
        section("Cadence postes (u/p)")
        for i, name in enumerate(STATION_NAMES):
            row(scroll, name, self.var_cap[i], 2, 20, 0.5)

        # --- Kanban ---
        section("Tickets Kanban")
        for i, name in enumerate(STATION_NAMES):
            row(scroll, f"Boucle {name[:5]}", self.var_kanban[i], 1, 20, 1,
                fmt="{:.0f}", is_int=True)
        row(scroll, "Taille lot", self.var_lot, 1, 10, 1,
            fmt="{:.0f}", is_int=True)

        # --- Incidents ---
        section("Incidents")
        row(scroll, "Probabilité", self.var_inc, 0.0, 0.5, 0.01,
            fmt="{:.0%}")

        # --- Vitesse ---
        section("Vitesse simulation")
        f = tk.Frame(scroll, bg=C["panneau"])
        f.pack(fill=tk.X, pady=2)
        tk.Label(f, text="Délai (ms)", bg=C["panneau"], fg=C["texte"],
                 font=("Helvetica", 8), width=14, anchor=tk.W).pack(side=tk.LEFT)
        spd_lbl = tk.Label(f, text=str(self.var_speed.get()),
                           bg=C["panneau"], fg=C["bleu_uimm"],
                           font=("Helvetica", 8, "bold"), width=4)
        spd_lbl.pack(side=tk.RIGHT)

        def on_speed(v):
            spd_lbl.config(text=str(self.var_speed.get()))
            self._apply_params()

        ttk.Scale(f, from_=100, to=2000, variable=self.var_speed,
                  orient=tk.HORIZONTAL, length=80,
                  command=on_speed).pack(side=tk.RIGHT, padx=2)

    def _apply_params(self):
        """Reporte les variables Tkinter dans SimParams."""
        p = self.params
        p.demand_mean      = self.var_demand.get()
        p.demand_cv        = self.var_cv.get()
        p.capacities       = [v.get() for v in self.var_cap]
        p.kanban_counts    = [v.get() for v in self.var_kanban]
        p.kanban_lot_size  = self.var_lot.get()
        p.incident_prob    = self.var_inc.get()
        p.speed_ms         = self.var_speed.get()
        p.mode             = self.var_mode.get()
        # Met aussi à jour les kanbans courants si on n'a pas encore démarré
        if self.engine.t == 0:
            self.engine.kanbans = list(p.kanban_counts)

    # ---------------------------------------------------------------
    # CONTRÔLES
    # ---------------------------------------------------------------
    def _build_controls(self, parent):
        bar = tk.Frame(parent, bg=C["fond"], pady=4)
        bar.pack(fill=tk.X)

        # Bouton mode
        self.btn_mode = tk.Button(
            bar, text="MODE : FLUX POUSSÉ",
            bg=C["push"], fg=C["blanc"],
            font=("Helvetica", 10, "bold"),
            relief=tk.FLAT, padx=12, pady=4,
            command=self._toggle_mode)
        self.btn_mode.pack(side=tk.LEFT, padx=4)

        ttk.Separator(bar, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y,
                                                     padx=6, pady=2)

        self.btn_start = tk.Button(
            bar, text="DÉMARRER", bg=C["bleu_uimm"], fg=C["blanc"],
            font=("Helvetica", 9, "bold"), relief=tk.FLAT, padx=10, pady=4,
            command=self._toggle_run)
        self.btn_start.pack(side=tk.LEFT, padx=2)

        tk.Button(bar, text="Pas à pas", bg=C["gris_clair"], fg=C["texte"],
                  font=("Helvetica", 9), relief=tk.FLAT, padx=8, pady=4,
                  command=self._step_once).pack(side=tk.LEFT, padx=2)

        tk.Button(bar, text="Réinitialiser", bg=C["gris_clair"], fg=C["texte"],
                  font=("Helvetica", 9), relief=tk.FLAT, padx=8, pady=4,
                  command=self._reset).pack(side=tk.LEFT, padx=2)

        # Période et taux de service en cours
        self.lbl_period = tk.Label(bar, text="Période : 0",
                                   bg=C["fond"], fg=C["texte"],
                                   font=("Helvetica", 9))
        self.lbl_period.pack(side=tk.RIGHT, padx=10)

    def _toggle_mode(self):
        current = self.var_mode.get()
        new = "pull" if current == "push" else "push"
        self.var_mode.set(new)
        self._apply_params()
        self.engine.p.mode = new
        color  = C["pull"] if new == "pull" else C["push"]
        label  = "MODE : FLUX TIRÉ (KANBAN)" if new == "pull" else "MODE : FLUX POUSSÉ"
        self.btn_mode.config(bg=color, text=label)
        self.update_vsm()

    def _toggle_run(self):
        self.running = not self.running
        if self.running:
            self.btn_start.config(text="PAUSE", bg=C["rouge_uimm"])
            self._run_loop()
        else:
            self.btn_start.config(text="DÉMARRER", bg=C["bleu_uimm"])
            if self._after_id:
                self.root.after_cancel(self._after_id)

    def _run_loop(self):
        if not self.running:
            return
        self._step_once()
        self._after_id = self.root.after(self.params.speed_ms, self._run_loop)

    def _step_once(self):
        self._apply_params()
        ev = self.engine.step()
        self._log_event(ev)
        self.update_vsm()
        self.update_charts()
        self.update_kpis()
        self.lbl_period.config(text=f"Période : {self.engine.t}")

    def _reset(self):
        if self.running:
            self._toggle_run()
        self._apply_params()
        self.engine.reset()
        self.log_text.config(state=tk.NORMAL)
        self.log_text.delete("1.0", tk.END)
        self.log_text.config(state=tk.DISABLED)
        self.update_vsm()
        self.update_charts()
        self.update_kpis()
        self.lbl_period.config(text="Période : 0")

    # ---------------------------------------------------------------
    # DIAGRAMME VSM
    # ---------------------------------------------------------------
    def _build_vsm(self, parent):
        frame = tk.Frame(parent, bg=C["panneau"], bd=1, relief=tk.GROOVE)
        frame.pack(fill=tk.X, padx=0, pady=(0, 4))
        tk.Label(frame, text="CARTE DE FLUX DE VALEUR (VSM)",
                 bg=C["bleu_uimm"], fg=C["blanc"],
                 font=("Helvetica", 9, "bold"), pady=2).pack(fill=tk.X)
        self.vsm_canvas = tk.Canvas(frame, width=self.VSM_W, height=self.VSM_H,
                                    bg=C["panneau"], highlightthickness=0)
        self.vsm_canvas.pack(fill=tk.X)

    def update_vsm(self):
        c  = self.vsm_canvas
        W, H = self.VSM_W, self.VSM_H
        c.delete("all")
        e  = self.engine
        p  = self.params
        is_pull = p.mode == "pull"

        # Positions horizontales
        xs_fournisseur = 30
        xs_stations    = [130, 380, 630]
        xs_stocks      = [240, 490, 740]
        xs_client      = 860
        y_mid          = H // 2 + 10
        box_w, box_h   = 90, 54
        stk_w, stk_h   = 64, 54

        # ---- Fournisseur ----
        self._vsm_actor(c, xs_fournisseur, y_mid, "Fournisseur", C["bleu_uimm"])

        # ---- Flèche fournisseur -> P1 ----
        arrow_color = C["push"] if not is_pull else C["bleu_uimm"]
        c.create_line(xs_fournisseur + 30, y_mid,
                      xs_stations[0] - box_w // 2, y_mid,
                      arrow=tk.LAST, fill=arrow_color, width=2)
        # Stock MP au-dessus de la flèche
        mp_x = (xs_fournisseur + 30 + xs_stations[0] - box_w // 2) // 2
        self._vsm_stock_badge(c, mp_x, y_mid - 22, e.stocks[0],
                              STOCK_LABELS[0], stk_high=30)

        # ---- 3 postes + 3 stocks intermédiaires ----
        for i in range(3):
            sx = xs_stations[i]
            incident = e.busy[i] > 0

            # Boîte poste
            self._vsm_station(c, sx, y_mid, STATION_NAMES[i],
                              e.cap_used[i], p.capacities[i], incident)

            # Flèche poste -> stock aval
            stk_x = xs_stocks[i]
            c.create_line(sx + box_w // 2, y_mid,
                          stk_x - stk_w // 2, y_mid,
                          arrow=tk.LAST, fill=arrow_color, width=2)

            # Badge stock
            stock_val = e.stocks[i + 1]
            self._vsm_stock_badge(c, stk_x, y_mid, stock_val,
                                  STOCK_LABELS[i + 1], stk_high=20)

            # Flèche stock -> poste suivant ou client
            next_x = xs_stations[i + 1] if i < 2 else xs_client
            next_offset = -box_w // 2 if i < 2 else -28
            c.create_line(stk_x + stk_w // 2, y_mid,
                          next_x + next_offset, y_mid,
                          arrow=tk.LAST, fill=arrow_color, width=2)

            # Tickets kanban (flux tiré)
            if is_pull:
                self._vsm_kanban_loop(c, sx, stk_x, y_mid, i,
                                      e.kanbans[i], p.kanban_counts[i])

        # ---- Client ----
        self._vsm_actor(c, xs_client, y_mid, "Client", C["rouge_uimm"])

        # ---- Demande client (flèche vers le bas depuis le client) ----
        c.create_line(xs_client, y_mid + 28, xs_client, y_mid + 55,
                      arrow=tk.LAST, fill=C["rouge_uimm"], width=2,
                      dash=(4, 2))
        c.create_text(xs_client + 14, y_mid + 45,
                      text=f"≈{p.demand_mean:.0f} u/p",
                      fill=C["rouge_uimm"], font=("Helvetica", 8), anchor=tk.W)

        # ---- Légende mode ----
        mode_txt = "FLUX TIRÉ — KANBAN" if is_pull else "FLUX POUSSÉ — MRP"
        mode_col = C["pull"] if is_pull else C["push"]
        c.create_rectangle(W - 190, 8, W - 10, 30, fill=mode_col, outline="")
        c.create_text(W - 100, 19, text=mode_txt,
                      fill=C["blanc"], font=("Helvetica", 9, "bold"))

        # ---- Période ----
        c.create_text(12, 12, text=f"t = {e.t}",
                      fill=C["texte"], font=("Helvetica", 9), anchor=tk.W)

    def _vsm_actor(self, c, x, y, label, color):
        """Dessine une icône 'acteur' (fournisseur / client)."""
        r = 26
        c.create_oval(x - r, y - r, x + r, y + r, fill=color, outline="")
        c.create_text(x, y, text=label, fill=C["blanc"],
                      font=("Helvetica", 8, "bold"), justify=tk.CENTER,
                      width=52)

    def _vsm_station(self, c, x, y, name, used, cap, incident):
        """Dessine la boîte d'un poste de travail."""
        bw, bh = 90, 54
        color = C["incident"] if incident else C["bleu_uimm"]
        c.create_rectangle(x - bw // 2, y - bh // 2,
                            x + bw // 2, y + bh // 2,
                            fill=color, outline="", width=0)
        c.create_text(x, y - 10, text=name,
                      fill=C["blanc"], font=("Helvetica", 8, "bold"))

        # Barre d'efficience
        eff = min(used / max(cap, 1), 1.0)
        bar_w = int(70 * eff)
        c.create_rectangle(x - 35, y + 8, x + 35, y + 20,
                            fill="#2980b9", outline="")
        eff_col = "#2ecc71" if eff > 0.6 else "#e67e22" if eff > 0.3 else "#e74c3c"
        c.create_rectangle(x - 35, y + 8, x - 35 + bar_w, y + 20,
                            fill=eff_col, outline="")
        c.create_text(x, y + 14, text=f"{eff:.0%}",
                      fill=C["blanc"], font=("Helvetica", 7, "bold"))

        if incident:
            c.create_text(x, y + 28, text="⚠ INCIDENT",
                          fill="#ffcc00", font=("Helvetica", 7, "bold"))

    def _vsm_stock_badge(self, c, x, y, value, label, stk_high=20):
        """Dessine le badge de stock triangulaire."""
        pts = [x, y - 26, x - 22, y + 4, x + 22, y + 4]
        # Couleur selon niveau
        if value > stk_high * 1.5:
            col = C["stock_haut"]
        elif value > stk_high * 0.5:
            col = C["stock_moyen"]
        else:
            col = C["stock_bas"]
        c.create_polygon(pts, fill=col, outline=C["blanc"], width=1)
        c.create_text(x, y - 10, text=str(value),
                      fill=C["blanc"], font=("Helvetica", 9, "bold"))
        c.create_text(x, y + 18, text=label,
                      fill=C["texte"], font=("Helvetica", 7))

    def _vsm_kanban_loop(self, c, station_x, stock_x, y, loop_idx,
                         available, total):
        """Dessine la boucle kanban sous le flux principal."""
        y2 = y + 70 + loop_idx * 4
        x1 = station_x
        x2 = stock_x
        # Ligne retour kanban
        c.create_line(x2, y + 30, x2, y2, fill="#8e44ad", width=1, dash=(3, 2))
        c.create_line(x2, y2, x1, y2, fill="#8e44ad", width=1, dash=(3, 2),
                      arrow=tk.LAST)
        c.create_line(x1, y2, x1, y + 30, fill="#8e44ad", width=1, dash=(3, 2))

        # Etiquette tickets
        mid_x = (x1 + x2) // 2
        c.create_rectangle(mid_x - 28, y2 - 8, mid_x + 28, y2 + 8,
                            fill="#8e44ad", outline="")
        c.create_text(mid_x, y2, text=f"K: {available}/{total}",
                      fill=C["blanc"], font=("Helvetica", 7, "bold"))

    # ---------------------------------------------------------------
    # LOG ÉVÉNEMENTS
    # ---------------------------------------------------------------
    def _build_log(self, parent):
        frame = tk.Frame(parent, bg=C["panneau"], bd=1, relief=tk.GROOVE)
        frame.pack(fill=tk.X)
        tk.Label(frame, text="JOURNAL DES ÉVÉNEMENTS",
                 bg=C["bleu_uimm"], fg=C["blanc"],
                 font=("Helvetica", 8, "bold"), pady=2).pack(fill=tk.X)
        self.log_text = tk.Text(frame, height=4, font=("Courier", 8),
                                bg="#1e2a3a", fg="#7fdbff",
                                state=tk.DISABLED, wrap=tk.WORD)
        self.log_text.pack(fill=tk.X, padx=4, pady=2)

    def _log_event(self, ev):
        t  = ev["t"]
        msgs = []
        for inc in ev.get("incidents", []):
            msgs.append(
                f"[t={t}] INCIDENT Poste {STATION_NAMES[inc['station']]} "
                f"({inc['duration']} période(s))"
            )
        prod = ev.get("produced", [0, 0, 0])
        if any(p > 0 for p in prod):
            msgs.append(
                f"[t={t}] Production : "
                + " | ".join(f"{STATION_NAMES[i]}={prod[i]}" for i in range(3))
            )
        msgs.append(
            f"[t={t}] Demande={ev['demand']}  Livré={ev['delivered']}  "
            f"Retard={ev['backlog']}  Service={ev.get('service', 0):.1%}"
        )
        self.log_text.config(state=tk.NORMAL)
        for m in msgs:
            self.log_text.insert("1.0", m + "\n")
        # Limite à 200 lignes
        lines = int(self.log_text.index("end-1c").split(".")[0])
        if lines > 200:
            self.log_text.delete("201.0", tk.END)
        self.log_text.config(state=tk.DISABLED)

    # ---------------------------------------------------------------
    # KPI
    # ---------------------------------------------------------------
    def _build_kpis(self, parent):
        tk.Label(parent, text="INDICATEURS CLÉS", bg=C["bleu_uimm"],
                 fg=C["blanc"], font=("Helvetica", 10, "bold"), pady=4).pack(
            fill=tk.X)
        grid = tk.Frame(parent, bg=C["panneau"])
        grid.pack(fill=tk.X, padx=6, pady=4)
        grid.columnconfigure(0, weight=1)
        grid.columnconfigure(1, weight=1)

        def kpi_cell(row, col, label, attr, fmt="{:.1%}", good_thresh=0.9,
                     reverse=False):
            f = tk.Frame(grid, bg=C["gris_clair"], bd=1, relief=tk.GROOVE)
            f.grid(row=row, column=col, padx=3, pady=3, sticky=tk.NSEW)
            tk.Label(f, text=label, bg=C["gris_clair"], fg=C["texte"],
                     font=("Helvetica", 8)).pack()
            lbl = tk.Label(f, text="—", bg=C["gris_clair"],
                           font=("Helvetica", 14, "bold"))
            lbl.pack()
            return lbl, attr, fmt, good_thresh, reverse

        self.kpi_cells = [
            kpi_cell(0, 0, "Taux de service", "taux_service",
                     fmt="{:.1%}", good_thresh=0.85),
            kpi_cell(0, 1, "Stock total (u)", "stock_total",
                     fmt="{:d}", good_thresh=50, reverse=True),
            kpi_cell(1, 0, "Efficience moy.", "efficience_moyenne",
                     fmt="{:.1%}", good_thresh=0.70),
            kpi_cell(1, 1, "Incidents", "total_incidents",
                     fmt="{:d}", good_thresh=5, reverse=True),
        ]

    def update_kpis(self):
        e = self.engine
        for lbl, attr, fmt, thresh, reverse in self.kpi_cells:
            val = getattr(e, attr)
            txt = fmt.format(val)
            if isinstance(val, float):
                good = val >= thresh if not reverse else val <= thresh
            else:
                good = val <= thresh if reverse else val >= thresh
            color = C["pull"] if good else C["push"]
            lbl.config(text=txt, fg=color)

    # ---------------------------------------------------------------
    # GRAPHIQUES
    # ---------------------------------------------------------------
    def _build_charts(self, parent):
        self.fig = Figure(figsize=(3.2, 5.5), dpi=90,
                          facecolor=C["panneau"])
        self.fig.subplots_adjust(hspace=0.55, left=0.18, right=0.97,
                                 top=0.95, bottom=0.06)

        self.ax_svc   = self.fig.add_subplot(3, 1, 1)
        self.ax_stk   = self.fig.add_subplot(3, 1, 2)
        self.ax_eff   = self.fig.add_subplot(3, 1, 3)

        for ax, title in [
            (self.ax_svc, "Taux de service"),
            (self.ax_stk, "Stocks par zone"),
            (self.ax_eff, "Efficience postes"),
        ]:
            ax.set_title(title, fontsize=8, color=C["bleu_uimm"], pad=3)
            ax.tick_params(labelsize=7)
            ax.set_facecolor(C["fond"])

        self.canvas_fig = FigureCanvasTkAgg(self.fig, master=parent)
        self.canvas_fig.get_tk_widget().pack(fill=tk.BOTH, expand=True,
                                             padx=4, pady=4)

    def update_charts(self):
        e = self.engine
        t = e.time_hist
        if not t:
            self.canvas_fig.draw()
            return

        mode_col = C["pull"] if self.params.mode == "pull" else C["push"]

        # Taux de service
        ax = self.ax_svc
        ax.clear()
        ax.plot(t, e.service_hist, color=mode_col, lw=1.5)
        ax.axhline(1.0, color=C["gris"], lw=0.8, ls="--")
        ax.set_ylim(0, 1.05)
        ax.set_ylabel("%", fontsize=7)
        ax.set_title("Taux de service", fontsize=8,
                     color=C["bleu_uimm"], pad=3)
        ax.set_facecolor(C["fond"])
        ax.tick_params(labelsize=7)

        # Stocks
        ax = self.ax_stk
        ax.clear()
        colors_stk = [C["bleu_uimm"], C["stock_moyen"], C["stock_haut"], C["pull"]]
        for i, (hist, lbl, col) in enumerate(
                zip(e.stock_hist, STOCK_LABELS, colors_stk)):
            ax.plot(t, hist, label=lbl[:6], color=col, lw=1.2)
        ax.set_ylabel("unités", fontsize=7)
        ax.set_title("Stocks par zone", fontsize=8,
                     color=C["bleu_uimm"], pad=3)
        ax.legend(fontsize=6, loc="upper right", ncol=2, framealpha=0.5)
        ax.set_facecolor(C["fond"])
        ax.tick_params(labelsize=7)

        # Efficience
        ax = self.ax_eff
        ax.clear()
        eff_cols = [C["bleu_uimm"], C["stock_moyen"], C["pull"]]
        for i, (name, col) in enumerate(zip(STATION_NAMES, eff_cols)):
            ax.plot(t, e.eff_hist[i], label=name[:5], color=col, lw=1.2)
        ax.set_ylim(0, 1.05)
        ax.set_ylabel("%", fontsize=7)
        ax.set_title("Efficience postes", fontsize=8,
                     color=C["bleu_uimm"], pad=3)
        ax.legend(fontsize=6, loc="lower left", framealpha=0.5)
        ax.set_facecolor(C["fond"])
        ax.tick_params(labelsize=7)

        # Marques incidents
        for ax_ in [self.ax_svc, self.ax_stk, self.ax_eff]:
            for it, _ in e.incident_hist:
                ax_.axvline(it, color=C["incident"], lw=0.6,
                            alpha=0.4, ls=":")

        self.canvas_fig.draw()


# ---------------------------------------------------------------------------
# POINT D'ENTRÉE
# ---------------------------------------------------------------------------
def main():
    root = tk.Tk()
    root.minsize(1100, 700)

    # Tenter d'agrandir selon l'écran
    try:
        root.state("zoomed")
    except Exception:
        root.geometry("1200x780")

    app = KanbanApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
