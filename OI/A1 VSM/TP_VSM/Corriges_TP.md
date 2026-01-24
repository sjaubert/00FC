# Corrigés des Travaux Pratiques VSM

---

## TP 1 : Flash-Metal - État Actuel

### VSM Complète

```
================================================================================
                        FORMATION VSM - CAS FLASH-METAL
                              ÉTAT ACTUEL
================================================================================

                           RENAULT
                        480 pcs/jour
                     ┌──────────────┐
                     │   CLIENT     │
                     │      🏭      │
                     └──────┬───────┘
                            │
                    Prév. mensuelle
                         (email)
                            ⚡
                            ↓
                     ┌──────────────┐      Ordre hebdo
                     │   PLANNING   │──────────────────┐
                     │     MRP      │    (papier)      │
                     └──────────────┘     ────▶        │
                            │                          │
                 ┌──────────┼──────────┬───────────────┼──────────┐
                 │          │          │               │          │
              ───▶       ───▶       ───▶            ───▶          │
                 │          │          │               │          │
FOURNISSEUR  ┌───────┐  ┌───────┐  ┌────────┐  ┌──────────┐  ┌────────┐
  ACIER      │DÉCOUPE│  │PLIAGE │  │SOUDURE │  │ PEINTURE │  │ CLIENT │
    🏭  ───▶ │ TC:30s│─▶│ TC:45s│─▶│ TC:60s │─▶│  TC:40s  │─▶│   🏭   │
             │ CS:10'│  │ CS: 5'│  │ CS:15' │  │  CS:20'  │  │        │
             │ R: 2% │  │ R: 1% │  │ R: 3%  │  │  R: 1%   │  │        │
             └───┬───┘  └───┬───┘  └────┬───┘  └────┬─────┘  └────────┘
                 │          │           │            │
                 ▽          ▽           ▽            ▽
               1200pcs    800pcs      600pcs       400pcs
               2,5 j      1,67 j      1,25 j       0,83 j

================================================================================
LIGNE DE TEMPS
================================================================================

    30s         45s         60s          40s
    ├──┤        ├──┤       ├───┤        ├──┤
    VA          VA          VA           VA

    └──2,5j──┘ └─1,67j─┘ └─1,25j─┘ └─0,83j─┘
       NVA        NVA        NVA        NVA

Total Lead Time = 2,5 + 1,67 + 1,25 + 0,83 = 6,25 jours
Total VA        = 30 + 45 + 60 + 40 = 175 secondes

TAKT TIME = 27 000 s / 480 pcs = 56,25 secondes

RATIO DE TENSION = (6,25 × 27 000) / 175 = 964
→ Seulement 0,104% de valeur ajoutée !
```

---

## TP 2 : Exercices Takt Time

### Exercice 1 - Situation A

```
Takt Time = 54 000 s / 450 pcs = 120 secondes

Interprétation : Une pièce doit sortir toutes les 2 minutes.
```

### Exercice 1 - Situation B

```
Takt Time = 54 000 s / 600 pcs = 90 secondes

Impact : Augmentation de 33% de la cadence !
Conséquences :
- Certains postes deviennent des goulots
- Besoin de rééquilibrage ou de ressources supplémentaires
```

### Exercice 2 : Dimensionnement

```
Nombre d'opérateurs = 187 s / 60 s = 3,11 → arrondi à 4

Vérification :
- Avec 4 opérateurs : 187 / 4 = 46,75 s/opérateur ✅
- Chaque opérateur cycle en moins de 60s → OK !

Si on n'avait mis que 3 opérateurs :
- 187 / 3 = 62,3 s/opérateur ❌
- Goulot ! Retard de 2,3 s par pièce
- Sur une journée : (62,3 - 60) × (54000/60) = 2070 secondes de retard
  → 34,5 minutes de production perdues
```

### Exercice 3 : Résoudre le Goulot

**Analyse du problème :**

```
TC Machine = 75 s
Takt Time  = 60 s
Écart      = 15 s (25% trop lent)
```

**Solutions priorisées :**

**1. Kaizen (Priorité 1) :**

```
Objectif : Gagner 15 secondes

Actions possibles :
- Réduire les mouvements inutiles : gain estimé 5-8 s
- Optimiser le poste de travail (5S) : gain estimé 3-5 s
- Changer de méthode : gain estimé 4-7 s

Total potentiel : 12-20 secondes → OBJECTIF ATTEIGNABLE
```

**2. Balancement (Priorité 2) :**

```
Exemple de redistribution :

Avant :
Peinture : 75 s (GOULOT)
Emballage : 40 s (sous-charge)

Après :
Peinture : 58 s (enlever 17s de tâches)
Emballage : 57 s (récupérer les 17s)

Les deux postes < 60s → PROBLÈME RÉSOLU
```

**3. Parallélisme (Priorité 3) :**

```
Coût : ~50 000 € pour une 2ème machine

Résultat :
2 machines à 75s → 1 pièce toutes les 37,5s en sortie

Mais… avant d'investir, TOUJOURS essayer Kaizen !
```

**4. Heures Supplémentaires (Temporaire) :**

```
Déficit par jour :
(75 - 60) × (54000 / 60) = 13 500 secondes = 3,75 heures

Besoin : +3,75h de production
Coût : 3,75h × 42 €/h × 20 jours = 3150 €/mois

→ NON DURABLE (épuisement + coût élevé)
```

---

## TP 3 : Identification des Mudas

### Exercice : Chasse aux Mudas

| Observation | Type de Muda | Explication |
|-------------|--------------|-------------|
| 1. Marche 15m pour outils | **Mouvements** | Geste sans VA, fatigue l'opérateur |
| 2. Attente 2h entre postes | **Attentes** (Stock) | Temps mort = perte de réactivité |
| 3. Lots de 500 vs 100/jour | **Surproduction** | Produit 5 jours d'avance ! |
| 4. 5% de rebuts | **Défauts** | Perte matière + temps de retouche |
| 5. Idée non mise en œuvre | **Potentiel humain** | Compétence gaspillée |
| 6. 3 transports PF | **Transports** | Risque de dommage + temps perdu |
| 7. Polissage non visible | **Surtraitement** | Travail sans valeur client |
| 8. Panne 20 min/jour | **Attentes** | Machine arrêtée = perte |

### Calcul Impact Financier

**Surproduction :**

```
Stock excessif : 400 pcs/jour × 20 jours = 8000 pièces
Coût de stockage : 8000 × 0,50 € = 4000 €/mois
```

**Défauts :**

```
Rebuts : 480 × 5% × 20 jours = 480 pièces
Perte matière : 480 × 8 € = 3840 €/mois
```

**Attentes :**

```
Temps perdu : 20 min/j × 20 j = 400 min = 6,67 h
Coût main d'œuvre : 6,67 × 42 € = 280 €/mois
```

**TOTAL MENSUEL : 8120 €**
**TOTAL ANNUEL : 97 440 €**

**Analyse :**
Pour une usine de 20 personnes, c'est l'équivalent de :

- 2,3 salaires complets gaspillés
- Ou 15% de la masse salariale perdue !

---

## TP 4 : Flash-Metal - État Futur

### Réponses aux 8 Questions

**1. Takt Time :**

```
TT = 27 000 s / 480 pcs = 56,25 secondes
```

**2. Production :**

```
Supermarché de produits finis = 2 heures de stock
= 480 pcs / 8h × 2h = 120 pièces
```

**3. Flux continu :**

```
Cellule Soudure-Peinture :
TC total = 60 + 40 = 100 secondes
Nb opérateurs = 100 / 56,25 = 1,78 → 2 opérateurs

Avantage : Supprime 600 pcs de stock (1,25 jours)
```

**4. Supermarchés :**

```
Supermarché 1 : Après Pliage
Stock tampon = 1 heure = 60 pièces

Raison : Éloignement physique entre Pliage et Cellule
```

**5. Pacemaker :**

```
La Cellule Soudure-Peinture reçoit le planning unique

C'est le point le plus proche du client où se fait
l'assemblage final de la valeur.
```

**6. Heijunka (Nivellement) :**

```
Mix : 60% Modèle A, 40% Modèle B

Séquence sur 10 pièces :
A - A - B - A - B - A - A - B - A - B

Évite les lots et lisse la charge.
```

**7. Pitch (Incrément) :**

```
Conteneur = 20 pièces
Pitch = 56,25 × 20 = 1125 s ≈ 19 minutes

Colonnes Heijunka : 8h00, 8h19, 8h38, 8h57...
Nombre d'intervalles/jour = 8h × 60 / 19 = 25 Pitch
```

**8. Kaizen nécessaires :**

```
KAIZEN 1 : Réduction CS Découpe
- Objectif : passer de 10 min à 5 min
- Méthode : SMED (changement rapide)

KAIZEN 2 : Rapprochement Pliage-Cellule
- Objectif : réduire la distance de 50m à 10m
- Gain : moins de transport

KAIZEN 3 : Amélioration qualité
- Objectif : réduire les rebuts de 2% à 0,5%
- Méthode : Poka-Yoke (détrompeur)
```

### VSM État Futur

```
================================================================================
                        FORMATION VSM - CAS FLASH-METAL
                              ÉTAT FUTUR
================================================================================

                           RENAULT
                        480 pcs/jour
                     ┌──────────────┐
                     │   CLIENT     │
                     │      🏭      │
                     └──────┬───────┘
                            │
                    Commande ferme
                        (quotidienne)
                            ⚡
                            ↓
FOURNISSEUR          ┌──────────────┐
  ACIER              │ HEIJUNKA BOX │ ← Planning unique
    🏭  ════════╗    │  CELLULE S-P │
                ║    └──────┬───────┘
                ║           │ Pitch = 19 min
                ║        ─••▶         
                ║           │
             ┌──▼───┐  ┌───▼────────────────────┐  ┌────────┐
             │DÉCOUPE  │🏪│  CELLULE SOUDURE-    │  │ CLIENT │
             │ TC:30s│  │  PEINTURE (flux continu)│  │   🏭   │
             │ ⚡CS:5'│  │  TC: 100s (2 opérateurs)│  │        │
             └───┬───┘  │  Takt Time: 56s        │  │        │
                 │      └───────────┬────────────┘  └────────┘
                 ▽                  │
               60pcs                ▽
               0,13 j             120pcs (PF)
                                  0,25 j

================================================================================
LIGNE DE TEMPS - ÉTAT FUTUR
================================================================================

    30s              100s
    ├──┤            ├────┤
    VA               VA

    └─0,13j─┘    └─0,25j─┘
       NVA          NVA

Total Lead Time = 0,13 + 0,25 = 0,38 jours (3 heures)
Total VA        = 30 + 100 = 130 secondes

NOUVEAU RATIO = (0,38 × 27 000) / 130 = 79

================================================================================
COMPARAISON AVANT / APRÈS
================================================================================

| Indicateur           | État Actuel | État Futur | Gain       |
|----------------------|-------------|------------|------------|
| Lead Time            | 6,25 jours  | 0,38 jour  | **-94%**   |
| Stock total          | 3000 pcs    | 180 pcs    | **-94%**   |
| Ratio de tension     | 964         | 79         | **-92%**   |
| Points planification | 4           | 1          | **-75%**   |
| Distance parcourue   | 200 m       | 15 m       | **-93%**   |
| Réactivité client    | 6,25 jours  | 3 heures   | **50× plus rapide** |
```

---

## TP 5 : Dimensionnement Kanban

### Exercice : Supermarché Emboutissage-Soudure

**Données :**

- Demande : 480 pcs/jour
- Lead Time : 2 heures
- Sécurité : 10%
- Conteneur : 60 pcs

**Calculs :**

**1. Consommation horaire :**

```
480 pcs / 8h = 60 pcs/heure
```

**2. Consommation pendant le Lead Time :**

```
60 pcs/h × 2h = 120 pièces
```

**3. Stock de sécurité :**

```
120 × 10% = 12 pièces
```

**4. Nombre de Kanban :**

```
Nb = ⌈(120 + 12) / 60⌉ = ⌈132 / 60⌉ = ⌈2,2⌉ = 3 cartes

Stock en circulation = 3 × 60 = 180 pièces
```

**5. Vérification :**

```
Stock théorique nécessaire : 132 pcs
Stock réel : 180 pcs
Marge : 180 - 132 = 48 pcs (36% de sécurité)

✅ Suffisant pour absorber les variations
```

---

### Exercice : Tableau Heijunka

**Données :**

- Takt : 45s
- Conteneur : 20 pcs
- Mix : 50% A, 30% B, 20% C
- Journée : 8h

**Calculs :**

**1. Pitch :**

```
Pitch = 45s × 20 pcs = 900 s = 15 minutes
```

**2. Nombre de colonnes :**

```
480 min / 15 min = 32 intervalles
```

**3. Répartition sur 10 intervalles :**

```
A : 50% de 10 = 5 cartes
B : 30% de 10 = 3 cartes
C : 20% de 10 = 2 cartes
```

**4. Séquence nivelée recommandée :**

```
Position : 1   2   3   4   5   6   7   8   9   10
Produit  : A - B - A - C - A - B - A - A - B - C

Justification :
- Pas de lots consécutifs (évite surproduction)
- Distribution homogène des modèles
- Facilite le lissage de charge amont
```

**Tableau Heijunka visuel :**

```
╔═══════╦══════╦══════╦══════╦══════╦══════╦══════╦══════╦══════╦══════╦══════╗
║Produit║ 8h00 ║ 8h15 ║ 8h30 ║ 8h45 ║ 9h00 ║ 9h15 ║ 9h30 ║ 9h45 ║10h00 ║10h15 ║
╠═══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╣
║   A   ║  🟢  ║      ║  🟢  ║      ║  🟢  ║      ║  🟢  ║  🟢  ║      ║      ║
╠═══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╣
║   B   ║      ║  🔵  ║      ║      ║      ║  🔵  ║      ║      ║  🔵  ║      ║
╠═══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╣
║   C   ║      ║      ║      ║  🔴  ║      ║      ║      ║      ║      ║  🔴  ║
╚═══════╩══════╩══════╩══════╩══════╩══════╩══════╩══════╩══════╩══════╩══════╝
```

---

## Cas Intégral : Usine ABC - Corrigés Complets

### Mission 1 : État Actuel

**Takt Time :**

```
TT = 54 000 s / 540 pcs = 100 secondes
```

**Lead Time (détaillé) :**

```
Stock 1 (après Emboutissage) : 3500 / 540 = 6,48 jours
Stock 2 (après Usinage)       : 2100 / 540 = 3,89 jours
Stock 3 (après Soudure)        : 1800 / 540 = 3,33 jours
Stock 4 (Produits Finis)       : 1100 / 540 = 2,04 jours

Lead Time Total = 6,48 + 3,89 + 3,33 + 2,04 = 15,74 jours
```

**Temps de VA :**

```
VA = 20 + 35 + 45 + 55 = 155 secondes
```

**Ratio :**

```
15,74 jours × 54 000 s/jour = 849 960 secondes
Ratio = 849 960 / 155 = 5484

Seulement 0,018% de VA → DRAMATIQUE !
```

---

### Mission 2 : État Futur - Conception Détaillée

**Décisions de conception :**

**1. Pacemaker = Assemblage**

```
Raison : Plus proche du client + différenciation G/D
```

**2. Cellule Soudure-Assemblage**

```
TC combiné = 45 + 55 = 100s = TT !
Nb opérateurs = 100 / 100 = 1... mais arrondi à 2
(1 soudeur + 1 assembleur, chacun à 50s)

Gain : Suppression de 1800 pcs de stock
```

**3. Supermarchés dimensionnés**

```
Supermarché 1 (après Emboutissage) :
- Lead Time réappro : 4h
- Consommation : 540 / 15h × 4h = 144 pcs
- Sécurité 10% : 14 pcs
- Total : 158 pcs → 3 conteneurs de 60 pcs = 180 pcs

Supermarché 2 (après Usinage) :
- Lead Time : 2h
- Consommation : 540 / 15h × 2h = 72 pcs
- Sécurité : 7 pcs
- Total : 79 pcs → 2 conteneurs de 50 pcs = 100 pcs
```

**4. Goulots analysés**

```
Emboutissage :
TC = 20s, TT = 100s → OK (capacité × 5)
Mais CS = 60 min → doit produire par lots
→ Chantier SMED pour réduire à 20 min

Usinage :
TC = 35s × 1/0,95 × 1/0,99 = 37,2s effectif
37,2s << 100s → Pas de goulot

Cellule :
100s = 100s → Parfaitement dimensionnée !
```

**5. Heijunka - Assemblage**

```
Mix : 50% Bras G, 50% Bras D
Conteneur : 20 pcs
Pitch : 100s × 20 = 2000s = 33 min

Séquence : G-D-G-D-G-D...
Nb colonnes/jour : 15h × 60 / 33 = 27 pitch
```

---

### Mission 3 : Quantification des Gains

**Tableau comparatif détaillé :**

| Indicateur | État Actuel | État Futur | Formule Gain | Impact |
|------------|-------------|------------|--------------|--------|
| **Lead Time** | 15,74 j | 0,42 j | (15,74-0,42)/15,74 | **-97,3%** |
| **Stock (pcs)** | 8500 | 280 | (8500-280)/8500 | **-96,7%** |
| **Stock (€)** | 85 000 € | 2800 € | 8220 pcs × 10€ | **82 200 € libérés** |
| **Surface** | 450 m² | 120 m² | (450-120)/450 | **-73%** |
| **Loyer évité** | - | - | 330 m² × 15€/m²/mois | **59 400 €/an** |
| **Main d'œuvre** | 4 postes | 2 postes | Réduction planif | **-50%** |
| **Manutention** | 8 trajets/j | 2 trajets/j | Distance × temps | **-75%** |
| **Ratio tension** | 5484 | 147 | (5484-147)/5484 | **-97,3%** |

**ROI Calculé :**

```
INVESTISSEMENTS :
- Rapprochement machines (manutention) : 15 000 €
- Racks supermarchés (2 zones)          : 12 000 €
- Formation opérateurs                  :  8 000 €
- Heijunka Box + cartes Kanban          :  5 000 €
                                        ──────────
TOTAL INVESTISSEMENT                    : 40 000 €

ÉCONOMIES ANNUELLES :
- Loyer (330 m² × 15€ × 12)             : 59 400 €
- Réduction stock (intérêt 5%)          :  4 110 €
- Planification (0,5 ETP × 35k€)        : 17 500 €
- Manutention (gain productivité)       : 12 000 €
- Réduction rebuts (meilleure qualité)  :  8 000 €
                                        ──────────
TOTAL ÉCONOMIES                         : 101 010 €/an

ROI = 40 000 / 101 010 = 0,396 an = 4,8 mois
```

---

### Mission 4 : Plan d'Action Détaillé

**BOUCLE 1 : PACEMAKER (Semaines 1-4)**

**Responsable :** Chef d'atelier assemblage  
**Objectif :** Créer la cellule Soudure-Assemblage

| Semaine | Action | Livrable |
|---------|--------|----------|
| S1 | Rapprocher physiquement les machines | Layout validé |
| S2 | Former les 2 opérateurs au flux continu | Certification |
| S3 | Installer Heijunka Box + créer cartes | Système opérationnel |
| S4 | Démarrage + ajustements | Prod à 100% |

**Indicateurs de succès :**

- Lead Time cellule < 2 min
- Pas de stock entre Soudure et Assemblage
- Respect Pitch ≥ 95%

---

**BOUCLE 2 : SUPERMARCHÉS (Semaines 5-8)**

**Responsable :** Responsable logistique  
**Objectif :** Mettre en place les 2 supermarchés Kanban

| Semaine | Action | Livrable |
|---------|--------|----------|
| S5 | Installer racks Zone 1 (Emboutissage) | 3 cartes Kanban actives |
| S6 | Installer racks Zone 2 (Usinage) | 2 cartes Kanban actives |
| S7 | Former manutentionnaires au système | Procédure écrite |
| S8 | Optimisation tournées | Planning optimisé |

**Indicateurs de succès :**

- Stock ≤ 280 pièces total
- Taux de service ≥ 99%
- Rupture = 0

---

**BOUCLE 3 : EMBOUTISSAGE (Semaines 9-12)**

**Responsable :** Responsable production  
**Objectif :** Réduire CS de 60 min à 20 min (SMED)

| Semaine | Action | Livrable |
|---------|--------|----------|
| S9 | Filmer CS actuel + analyse | Vidéo annotée |
| S10 | Séparer interne/externe | Nouveau standard |
| S11 | Tester amélioration | CS à 30 min |
| S12 | Optimisation finale | CS à 20 min |

**Indicateurs de succès :**

- CS ≤ 20 min
- Fréquence changements × 3
- Taille lots / 3

---

**BOUCLE 4 : USINAGE (Semaines 13-16)**

**Responsable :** Maintenance  
**Objectif :** Améliorer disponibilité de 95% à 98%

| Semaine | Action | Livrable |
|---------|--------|----------|
| S13 | Analyse pannes récurrentes (Pareto) | Top 3 causes |
| S14 | Plan maintenance préventive | Planning annuel |
| S15 | Remplacement pièces critiques | Stock sécurisé |
| S16 | Formation opérateurs maintenance autonome | Check-list quotidienne |

**Indicateurs de succès :**

- Disponibilité ≥ 98%
- MTBF (temps entre pannes) × 2
- Pannes imprévues / 2

---

**Suivi Global (PDCA)**

**Comité de pilotage mensuel :**

- Responsable VSM (Manager Chaîne de Valeur)
- Tous les responsables de boucle
- Direction

**Indicateurs tableau de bord :**

1. Lead Time global
2. Stock total (pièces et €)
3. Taux de service client
4. Productivité (pcs/opérateur/jour)
5. Qualité (taux de rebut)

---

**🎉 Félicitations ! Vous avez terminé tous les exercices !**

**📊 Résumé des Gains Usine ABC :**

- **Lead Time : -97% (15,74j → 0,42j)**
- **Stock : -97% (8500 → 280 pcs)**
- **Cash libéré : 82 200 €**
- **Surface : -73% (450 → 120 m²)**
- **ROI : 4,8 mois**

**Prochaine étape :** Appliquez ces méthodes dans votre propre entreprise !
