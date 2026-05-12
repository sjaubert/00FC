# Simulation Flux Poussé / Flux Tiré (Kanban)

**Formation BTS ATI — Organisation Industrielle & Lean**
Pôle Formation UIMM CVDL | Formateur : S. Jaubert | Mai 2026

---

## Objectif pédagogique

Illustrer de manière interactive la différence fondamentale entre :

- **Flux poussé (MRP/planning)** : chaque poste produit selon un plan prédéfini, sans attendre le besoin aval → accumulation de stocks, mauvaise réactivité, effet "coup de fouet"
- **Flux tiré (Kanban)** : la production n'est déclenchée que par la consommation réelle du client → stocks maîtrisés, meilleure qualité de service, gaspillages réduits

---

## Deux versions disponibles

| Version | Fichier | Usage | Prérequis |
|---|---|---|---|
| Navigateur (en ligne) | `simulation_kanban.html` | Apprenants à distance, présentiel sur tablette/PC | Aucun |
| Application locale | `simulation_kanban.py` | Formateur, usage hors connexion | Python + dépendances |

**Lien direct (GitHub Pages) :**
`https://sjaubert.github.io/00FC/OI/jeu_du_kanban/simulation_kanban.html`

---

## Architecture de la simulation

```
Fournisseur → [M.P.] → P1 Usinage → [EC1] → P2 Assemblage → [EC2] → P3 Contrôle → [PF] → Client
                                 ←── Kanban ───┘          ←── Kanban ───┘         ←── Kanban ───┘
                                              (flux tiré uniquement)
```

- **3 postes** : Usinage, Assemblage, Contrôle
- **4 zones de stock** : Matières premières, En-cours 1, En-cours 2, Stock Produits Finis
- **Fournisseur** : réapprovisionne le stock MP chaque période (livraison continue planifiée)
- **Client** : demande variable selon une loi normale (moyenne + coefficient de variation)

### Logique flux poussé
Chaque poste produit à sa cadence nominale maximale, indépendamment de la demande aval.
Les stocks intermédiaires grossissent sans limite car la production n'est pas régulée par le besoin réel.

### Logique flux tiré (Kanban)
Un **ticket kanban** est nécessaire pour autoriser toute production.
Les tickets circulent de l'aval vers l'amont au rythme de la consommation réelle.
Le nombre de tickets fixe le plafond de WIP (Work In Progress) dans chaque boucle.

---

## Paramètres ajustables

| Paramètre | Description | Valeur par défaut |
|---|---|---|
| Demande moyenne (u/p) | Demande client moyenne par période | 8 |
| Variabilité (CV) | Coefficient de variation de la demande | 30 % |
| Cadence Usinage | Production max du poste 1 (u/p) | 10 |
| Cadence Assemblage | Production max du poste 2 (u/p) — goulot | 9 |
| Cadence Contrôle | Production max du poste 3 (u/p) | 10 |
| Tickets kanban | Nombre de tickets par boucle (3 boucles) | 6 |
| Taille de lot | Nombre de pièces par ticket kanban | 3 |
| Probabilité d'incident | Risque de panne par poste et par période | 12 % |

### Interprétation des paramètres clés

**`t` (période)** : unité de temps discrète de la simulation, assimilable à une heure de production dans le jeu physique.

**u/p (unités par période)** : cadence de production. Assemblage à 9 u/p crée un goulot visible sur la VSM.

**Variabilité (CV)** : écart-type / moyenne. À 30 %, une demande moyenne de 8 oscille typiquement entre 3 et 13 u/p.

**Barre d'efficience** (sur chaque poste) : ratio quantité produite / cadence nominale.
- Vert > 60 % | Orange 30-60 % | Rouge < 30 %
- En flux tiré, un poste qui attend un ticket (efficience basse) est normal : c'est le principe du Juste-à-Temps.

---

## Indicateurs affichés

| Indicateur | Calcul | Seuil "bon" |
|---|---|---|
| Taux de service | Livré cumulé / Demande cumulée | ≥ 85 % |
| Stock total | Somme des 4 zones de stock | ≤ 60 u |
| Efficience moyenne | Moyenne des efficiences des 3 postes | ≥ 65 % |
| Incidents | Nombre total de pannes survenues | ≤ 5 |

---

## Scénarios pédagogiques conseillés

### Scénario 1 — Flux poussé (point de départ)

| Paramètre | Valeur |
|---|---|
| Mode | Flux poussé |
| Demande moyenne | 8 u/p |
| Variabilité | 30 % |
| Cadences | 10 / 9 / 10 |
| Tickets kanban | 6 (sans effet en mode poussé) |
| Incidents | 12 % |

**Observation attendue :** Les stocks EC1 et EC2 gonflent indéfiniment. Le taux de service est instable malgré une efficience proche de 100 %. Le goulot (Assemblage à 9 u/p) est visible sur la VSM.

### Scénario 2 — Flux tiré, flux peu tendu

Mêmes paramètres, passer en mode **Flux tiré** avec **8 tickets/boucle**.

**Observation attendue :** Les stocks plafonnent. Le taux de service s'améliore. L'efficience baisse légèrement (postes qui attendent parfois un ticket) — occasion de débat pédagogique.

### Scénario 3 — Flux tiré, flux tendu

| Paramètre | Valeur |
|---|---|
| Variabilité | 50 % |
| Tickets kanban | 4 par boucle |
| Taille de lot | 2 |
| Incidents | 20 % |

**Observation attendue :** Le système devient fragile. Un incident peut provoquer une rupture. Introduction naturelle des leviers d'amélioration : SMED, maintenance préventive, qualité.

### Séquence conseillée en formation (45-60 min)

1. Lancer Scénario 1 (~20 périodes) — laisser les apprenants constater le problème
2. Réinitialiser → Scénario 2 — comparer les graphiques côte à côte
3. Réduire progressivement les tickets → Scénario 3 — débat sur les conditions du flux tendu

**Message clé à faire émerger :** *Le Kanban n'est pas magique — il révèle les problèmes que le stock cachait.*

---

## Installation (version Python)

```bash
# Cloner le dépôt
git clone https://github.com/sjaubert/00FC.git
cd 00FC/OI/jeu_du_kanban

# Installer les dépendances
pip install -r requirements.txt

# Lancer
python simulation_kanban.py
```

---

## Pistes d'évolution

- Variante financière : coût de stock, pénalité de retard, coût d'incident
- Goulot paramétrable (un poste intentionnellement sous-capacitaire)
- Export CSV des résultats pour comparaison entre groupes
- Mode "compétition" multi-équipes

---

## Licence

Usage pédagogique — Pôle Formation UIMM CVDL.
Réutilisation bienvenue dans un cadre de formation avec mention de la source.
