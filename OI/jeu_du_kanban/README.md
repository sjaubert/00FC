# Simulation Flux Poussé / Flux Tiré (Kanban)

**Formation BTS ATI — Organisation Industrielle & Lean**  
Pôle Formation UIMM CVDL | Formateur : S. Jaubert

---

## Objectif pédagogique

Cette simulation Python illustre, de manière interactive et visuelle, la différence fondamentale entre :

- **Flux poussé (MRP/planning)** : chaque poste produit selon un plan prédéfini, sans attendre le besoin aval → accumulation de stocks, mauvaise réactivité, effet « coup de fouet »
- **Flux tiré (Kanban)** : la production n'est déclenchée que par la consommation réelle du client → stocks maîtrisés, meilleure qualité de service, gaspillages réduits

La simulation reprend le principe d'une **carte de flux de valeur (VSM)** avec 3 postes de transformation, des stocks intermédiaires et un client final.

---

## Fonctionnalités

| Fonctionnalité | Description |
|---|---|
| VSM animée | Diagramme flux temps réel (postes, stocks, tickets kanban) |
| Bascule mode | Passage instantané FLUX POUSSÉ ↔ FLUX TIRÉ |
| Paramètres ajustables | Demande, cadences, nb tickets, taille lot, incidents |
| Incidents aléatoires | Pannes simulées avec durée variable |
| Graphiques temps réel | Taux de service, niveaux de stocks, efficience postes |
| Indicateurs KPI | Taux de service, stock total, efficience, nb incidents |
| Pas à pas | Avancement période par période pour l'analyse |
| Journal événements | Trace de chaque période (production, incidents, livraisons) |

---

## Architecture de la simulation

```
Fournisseur → [P1 Usinage] → Stock EC1 → [P2 Assemblage] → Stock EC2 → [P3 Contrôle] → Stock PF → Client
                                ↑                              ↑                            ↑
                         ← Kanban boucle 1 ←         ← Kanban boucle 2 ←        ← Kanban boucle 3 ←
                                              (flux tiré uniquement)
```

### Logique flux poussé
Chaque poste produit à la limite de sa capacité nominale, indépendamment de la demande aval.  
→ Les stocks grossissent en amont des goulots ; le client peut être en rupture en aval.

### Logique flux tiré (Kanban)
Un ticket kanban est requis pour autoriser toute production.  
Les tickets circulent de l'aval vers l'amont au rythme de la consommation réelle.  
→ Le nombre de tickets limite le nombre de pièces en circulation (encours maîtrisé).

---

## Installation

```bash
# Cloner le dépôt
git clone https://github.com/sjaubert/00FC.git
cd 00FC/OI/jeu_du_kanban

# Installer les dépendances
pip install -r requirements.txt

# Lancer la simulation
python simulation_kanban.py
```

**Dépendances :** `matplotlib` · `numpy` · `pillow` (optionnel, pour le logo)

---

## Guide d'utilisation rapide

1. **Lancer** → `python simulation_kanban.py`
2. **Observer en flux poussé** (mode par défaut) : cliquer **DÉMARRER** et observer l'accumulation des stocks
3. **Basculer en flux tiré** : cliquer **MODE : FLUX POUSSÉ** pour passer en Kanban
4. **Réinitialiser** puis relancer pour comparer les deux modes à paramètres identiques
5. **Ajuster les paramètres** : réduire le nombre de tickets kanban pour « tendre les flux »

### Paramètres clés à expérimenter

| Paramètre | Effet pédagogique |
|---|---|
| Nombre de tickets kanban ↓ | Flux plus tendu, moins d'encours, risque de rupture |
| Variabilité demande ↑ | Met en évidence la résilience du Kanban vs. le poussé |
| Probabilité d'incident ↑ | Montre l'impact des aléas sur les deux modes |
| Cadence P2 < P1 et P3 | Crée un goulot visible sur la VSM |

---

## Contenu du répertoire

```
jeu_du_kanban/
├── simulation_kanban.py   ← simulation principale (ce fichier)
├── requirements.txt
├── README.md
└── Kanban/                ← ressources pédagogiques (PDF, documents)
```

---

## Licence

Usage pédagogique — Pôle Formation UIMM CVDL.  
Toute réutilisation dans un cadre de formation est bienvenue avec mention de la source.
