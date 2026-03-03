# Guide de Référence Rapide VSM

## Symboles et Formules Essentiels

---

## Symboles VSM

### Flux de Matières

```
┌─────────────────────────────────────────────────┐
│ CLIENT / FOURNISSEUR                            │
│                                                 │
│     ┌──────┐                                    │
│     │      │  Usine ou Entreprise               │
│     │    │                                    │
│     └──────┘                                    │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│ PROCESSUS DE FABRICATION                        │
│                                                 │
│     ┌──────────┐                                │
│     │ SOUDURE  │  Boîte de processus            │
│     │ TC: 45s  │  (avec données)                │
│     └──────────┘                                │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│ STOCK                                           │
│                                                 │
│       ▽                                         │
│      2,5j      Triangle de stock               │
│               (quantité en jours)               │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│ TRANSPORT                                       │
│                                                 │
│       ─────▶  Camion avec flèche              │
│                                                 │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│ FLUX POUSSÉ                                     │
│                                                 │
│     ═══════▶    Flèche rayée                    │
│                (production sans signal client)  │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│ FLUX CONTINU                                    │
│                                                 │
│     OXOXOX     Production pièce à pièce         │
│                                                 │
└─────────────────────────────────────────────────┘
```

### Flux d'Information

```
┌─────────────────────────────────────────────────┐
│ INFORMATION ÉLECTRONIQUE                        │
│                                                 │
│     ─────▶    Éclair (EDI, Email, ERP)        │
│                                                 │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│ INFORMATION MANUELLE                            │
│                                                 │
│     ──────▶     Flèche simple (papier, oral)    │
│                                                 │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│ PLANNING DE PRODUCTION                          │
│                                                 │
│     ┌────┐                                      │
│     │MRP │      Système de planification         │
│     └────┘                                      │
└─────────────────────────────────────────────────┘
```

### Systèmes Lean

```
┌─────────────────────────────────────────────────┐
│ SUPERMARCHÉ KANBAN                              │
│                                                 │
│     ┌─┬─┬─┐                                     │
│     │ │ │ │    Stock contrôlé                   │
│     └─┴─┴─┘    avec cartes Kanban              │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│ BOÎTE DE LISSAGE (HEIJUNKA)                     │
│                                                 │
│     ╔═╦═╦═╗                                     │
│     ║ ║ ║ ║    Tableau de nivellement          │
│     ╚═╩═╩═╝    de la production                │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│ RETRAIT KANBAN                                  │
│                                                 │
│     ───┐                                        │
│        └─▶     Signal de prélèvement           │
│                                                 │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│ SIGNAL KANBAN                                   │
│                                                 │
│     ─••─▶      Signal de production             │
│                                                 │
└─────────────────────────────────────────────────┘
```

### Symboles d'Amélioration

```
┌─────────────────────────────────────────────────┐
│ ÉCLAIR KAIZEN                                   │
│                                                 │
│                                                │
│     KAIZEN     Marque une amélioration          │
│               nécessaire                        │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│ OPÉRATEUR                                       │
│                                                 │
│              Icône d'opérateur                │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

<div style="page-break-after: always;"></div>

## Formules Essentielles

### 1. Takt Time (Le Métronome de l'Usine)

```
        Temps Disponible (secondes)
TT = ────────────────────────────────
        Demande Client (pièces)
```

**Exemple :**

- Temps disponible : 27 000 s
- Demande : 480 pcs
- **TT = 27 000 / 480 = 56,25 secondes**

**Interprétation :** Il faut sortir 1 pièce toutes les 56 secondes.

---

### 2. Temps Disponible

```
Temps Disponible = (Heures de travail - Pauses - Réunions - Maintenance) × 3600
```

**Exemple :**

- 8h de travail
- 2 pauses de 15 min
- 10 min de briefing
- **TD = (8h - 0,5h - 0,17h) × 3600 = 26 400 secondes**

---

### 3. Dimensionnement des Ressources

```
                    Temps de Cycle Total
Nb Opérateurs = ⌈ ──────────────────────── ⌉
                        Takt Time

⌈ ⌉ = arrondi à l'entier SUPÉRIEUR
```

**Exemple :**

- TC Total : 187 s
- Takt Time : 60 s
- **Nb = ⌈187 / 60⌉ = ⌈3,11⌉ = 4 opérateurs**

---

### 4. Jours de Stock

```
              Quantité en Stock (pièces)
Jours = ─────────────────────────────────
        Demande Quotidienne (pièces/jour)
```

**Exemple :**

- Stock : 1200 pièces
- Demande : 480 pcs/jour
- **Jours = 1200 / 480 = 2,5 jours**

---

### 5. Lead Time Total

```
Lead Time (jours) = Σ (Jours de chaque stock)
```

**Exemple :**

- Stock 1 : 2,5 j
- Stock 2 : 1,8 j
- Stock 3 : 0,3 j
- **LT = 2,5 + 1,8 + 0,3 = 4,6 jours**

---

### 6. Temps de Valeur Ajoutée

```
VA Total = Σ (Temps de cycle de chaque processus)
```

**Exemple :**

- Découpe : 30 s
- Pliage : 45 s
- Soudure : 60 s
- **VA = 30 + 45 + 60 = 135 secondes**

---

### 7. Ratio de Tension

```
              Lead Time (secondes)
Ratio = ──────────────────────────────
        Temps de VA Total (secondes)
```

**Exemple :**

- LT : 4,6 jours × 27 000 s/jour = 124 200 s
- VA : 135 s
- **Ratio = 124 200 / 135 = 920**

**Interprétation :** Seulement 0,11% du temps est à valeur ajoutée !

---

### 8. Nombre de Cartes Kanban

```
              (Consommation pendant Lead Time) + Stock de Sécurité
Nb Kanban = ⌈ ────────────────────────────────────────────────── ⌉
                        Capacité du Conteneur
```

**Exemple :**

- Consommation : 60 pcs/h × 2h = 120 pcs
- Sécurité : 10% = 12 pcs
- Conteneur : 60 pcs
- **Nb = ⌈(120 + 12) / 60⌉ = ⌈2,2⌉ = 3 cartes**

---

### 9. Pitch (Pas de Gestion)

```
Pitch (secondes) = Takt Time × Quantité par Conteneur
```

**Exemple :**

- TT : 60 s
- Conteneur : 20 pcs
- **Pitch = 60 × 20 = 1200 s = 20 minutes**

---

### 10. TRS (Taux de Rendement Synthétique)

```
TRS = Disponibilité × Performance × Qualité
```

**Exemple :**

- Disponibilité : 85%
- Performance : 90%
- Qualité : 97%
- **TRS = 0,85 × 0,90 × 0,97 = 74,2%**

---

<div style="page-break-after: always;"></div>

## ️ Règles d'Or VSM

### À FAIRE

1. **Toujours dessiner à la main** (crayon + papier)
2. **Commencer par le client** (en haut à droite)
3. **Remonter le flux** (de droite à gauche)
4. **Aller sur le terrain** (Gemba) pour observer
5. **Mesurer avec un chronomètre** (ne pas estimer)
6. **Calculer le Takt Time en premier**
7. **Créer un plan d'action** après la VSM

### À NE PAS FAIRE

1. Utiliser un ordinateur pour dessiner l'état actuel
2. Modifier le Takt Time pour l'adapter aux machines
3. Dessiner sans aller voir le processus réel
4. Oublier les flux d'information
5. Négliger la ligne de temps
6. Créer une VSM sans plan d'action
7. Tout vouloir améliorer en même temps

---

## Les 8 Questions de l'État Futur

1. Quel est le Takt Time ?
2. Produisons-nous sur stock ou à la commande ?
3. Où peut-on créer du flux continu ?
4. Où placer des supermarchés ?
5. Quel est le processus régulateur (Pacemaker) ?
6. Comment niveler la production ?
7. Quel incrément de travail au Pacemaker ?
8. Quels chantiers Kaizen sont nécessaires ?

---

## Boîte de Données Type

```
┌─────────────────────┐
│     SOUDURE         │  ← Nom du processus
├─────────────────────┤
│ TC = 45 s           │  ← Temps de cycle
│ TR = 90 %           │  ← Taux de rendement
│ CS = 15 min         │  ← Changement de série
│ Équipe = 1          │  ← Nombre d'opérateurs
│ Rebut = 3 %         │  ← Taux de rebut
│ Shift = 2 × 8h      │  ← Organisation
└─────────────────────┘
```

---

## Seuils d'Alerte

| Indicateur |  Bon |  Attention |  Critique |
|------------|--------|--------------|-------------|
| Ratio de tension | < 10 | 10 - 100 | > 100 |
| Lead Time | < 1 jour | 1 - 5 jours | > 5 jours |
| TRS | > 85% | 70 - 85% | < 70% |
| Taux de rebut | < 1% | 1 - 3% | > 3% |
| Stock (jours) | < 0,5 j | 0,5 - 2 j | > 2 j |

---

<div style="page-break-after: always;"></div>

## Checklist VSM

### État Actuel

- [ ] Client dessiné (haut droite)
- [ ] Fournisseur dessiné (haut gauche)
- [ ] Tous les processus représentés
- [ ] Boîtes de données complètes
- [ ] Stocks mesurés et dessinés
- [ ] Flux d'information tracés
- [ ] Ligne de temps calculée
- [ ] Ratio de tension calculé

### État Futur

- [ ] Takt Time calculé
- [ ] Pacemaker identifié
- [ ] Flux continu créé
- [ ] Supermarchés placés
- [ ] Heijunka Box dessinée
- [ ] Kaizen identifiés
- [ ] Nouveau Lead Time calculé
- [ ] Gains quantifiés

### Plan d'Action

- [ ] Boucles Kaizen définies
- [ ] Responsables nommés
- [ ] Calendrier établi
- [ ] Indicateurs définis
- [ ] PDCA prévu

---

**Imprimez ce guide et gardez-le avec vous lors de vos cartographies VSM !**
