# Travaux Pratiques VSM - Value Stream Mapping

## Formation Complète avec Exemples Pratiques

---

## 📋 Table des Matières

1. [Introduction à la VSM](#1-introduction-à-la-vsm)
2. [TP 1 : Cartographie de l'État Actuel](#tp-1--cartographie-de-létat-actuel)
3. [TP 2 : Calcul du Takt Time et Dimensionnement](#tp-2--calcul-du-takt-time-et-dimensionnement)
4. [TP 3 : Identification des Gaspillages (Mudas)](#tp-3--identification-des-gaspillages-mudas)
5. [TP 4 : Conception de l'État Futur](#tp-4--conception-de-létat-futur)
6. [TP 5 : Mise en Place du Management Visuel Kanban](#tp-5--mise-en-place-du-management-visuel-kanban)
7. [Cas Pratique Intégral : Usine ABC](#cas-pratique-intégral--usine-abc)
8. [Annexes : Symboles et Formules](#annexes--symboles-et-formules)

---

## 1. Introduction à la VSM

### Qu'est-ce que la VSM ?

La **Value Stream Mapping** (Cartographie de la Chaîne de Valeur) est un outil visuel "papier-crayon" qui permet de :

- Visualiser les flux de matières et d'informations
- Identifier les gaspillages (Mudas)
- Concevoir un état futur optimisé
- Créer un plan d'action concret

### Concepts Fondamentaux

#### Valeur Ajoutée vs Non-Valeur Ajoutée

> **Définition** : La valeur est ce pour quoi le client est prêt à payer.

**Exemples :**

- ✅ **Valeur Ajoutée** : Souder deux pièces, peindre, assembler
- ❌ **Non-Valeur Ajoutée** : Attendre, transporter, stocker, retoucher

#### Le Ratio de Tension

C'est l'indicateur qui révèle l'efficacité réelle d'un processus :

```
Ratio de Tension = Temps de Traversée (Lead Time) / Temps de Valeur Ajoutée
```

**Exemple choc :**

- Lead Time : 23,6 jours = 2 038 080 secondes
- Temps de VA : 188 secondes
- **Ratio : 10 841** (seulement 0,009% du temps est à valeur ajoutée !)

---

## TP 1 : Cartographie de l'État Actuel

### 🎯 Objectif

Apprendre à dessiner une VSM de l'état actuel en utilisant les symboles standards.

### 📝 Cas d'Étude : "Flash-Metal"

**Contexte :**
Flash-Metal fabrique des supports métalliques pour l'industrie automobile. Le processus comprend 4 étapes principales.

**Données de base :**

- **Client** : Renault (demande quotidienne : 480 pièces/jour)
- **Temps de travail** : 1 équipe de 8h (480 min de temps disponible)
- **Pauses** : 2 x 15 min = 30 min
- **Temps disponible réel** : 450 min = 27 000 secondes

#### Processus de Production

| Étape | Temps de Cycle (sec) | Changement de série | Taux de rebut |
|-------|---------------------|---------------------|---------------|
| 1. Découpe | 30 s | 10 min | 2% |
| 2. Pliage | 45 s | 5 min | 1% |
| 3. Soudure | 60 s | 15 min | 3% |
| 4. Peinture | 40 s | 20 min | 1% |

#### Stocks Intermédiaires

- Entre Découpe et Pliage : 1200 pièces
- Entre Pliage et Soudure : 800 pièces
- Entre Soudure et Peinture : 600 pièces
- Stock de produits finis : 400 pièces

#### Flux d'Information

- Le client envoie une prévision mensuelle (par email)
- Le planning de production envoie un ordre hebdomadaire à chaque poste (par papier)

### 🛠️ Exercice Pratique

**Matériel nécessaire :**

- Feuille A3
- Crayon à papier
- Gomme
- Règle

**Instructions (À faire en 30 minutes) :**

1. **Commencez par le client** (en haut à droite)
   - Dessinez l'icône client
   - Notez la demande : 480 pcs/jour

2. **Dessinez le flux de matière** (de droite à gauche)
   - Ajoutez les 4 boîtes de processus avec leurs données
   - Indiquez les stocks avec le symbole triangle

3. **Ajoutez le flux d'information** (en haut)
   - Fournisseur → Planning → Postes de travail
   - Utilisez les flèches appropriées (email = éclair, papier = flèche droite)

4. **Tracez la ligne de temps** (en bas)
   - Calculez les jours de stock : Stock / Demande quotidienne
   - Exemple : 1200 pcs / 480 pcs/jour = 2,5 jours
   - VA (Valeur Ajoutée) = somme des temps de cycle

### ✅ Corrigé

**Calculs de la ligne de temps :**

```
Stock 1 : 1200 / 480 = 2,5 jours
Stock 2 : 800 / 480 = 1,67 jours  
Stock 3 : 600 / 480 = 1,25 jours
Stock 4 : 400 / 480 = 0,83 jours

Total Lead Time = 2,5 + 1,67 + 1,25 + 0,83 = 6,25 jours
Total VA = 30 + 45 + 60 + 40 = 175 secondes
```

**Ratio de Tension :**

```
6,25 jours × 27 000 s/jour = 168 750 secondes de Lead Time
Ratio = 168 750 / 175 = 964

Seulement 0,1% du temps est à valeur ajoutée !
```

---

## TP 2 : Calcul du Takt Time et Dimensionnement

### 🎯 Objectif

Maîtriser le calcul du Takt Time et dimensionner les ressources en conséquence.

### 📐 Formule du Takt Time

```
Takt Time = Temps Disponible / Demande Client
```

> **⚠️ Règle d'Or** : Le Takt Time est la voix du client, il ne se négocie JAMAIS !

### 📝 Exercice 1 : Calculs de Base

**Situation A - Usine ABC**

- Demande client : 450 pièces/jour
- Temps de travail : 2 équipes × 8h (16h total)
- Pauses : 2 × 30 min par équipe
- Temps disponible : 16h - 1h = 15h = 54 000 secondes

**Question :** Quel est le Takt Time ?

<details>
<summary>💡 Réponse</summary>

```
Takt Time = 54 000 s / 450 pcs = 120 secondes
```

**Interprétation** : Il faut sortir une pièce toutes les 2 minutes pour satisfaire la demande.

</details>

---

**Situation B - Changement de Demande**

- Même usine qu'avant
- Nouvelle demande : 600 pièces/jour (nouveau contrat)

**Question :** Quel est le nouveau Takt Time ?

<details>
<summary>💡 Réponse</summary>

```
Takt Time = 54 000 s / 600 pcs = 90 secondes
```

**Impact** : La cadence a augmenté de 25% ! Il faut produire plus vite ou ajouter des ressources.

</details>

---

### 📝 Exercice 2 : Dimensionnement des Ressources

**Contexte :** Vous créez une cellule de montage en flux continu.

**Données :**

- Takt Time : 60 secondes
- Temps de cycle total : 187 secondes (somme de 4 opérations)

**Question :** Combien d'opérateurs sont nécessaires ?

### 🧮 Formule de Dimensionnement

```
Nombre d'Opérateurs = Temps de Cycle Total / Takt Time
```

<details>
<summary>💡 Réponse Détaillée</summary>

```
Nombre d'opérateurs = 187 s / 60 s = 3,11

⚠️ On arrondit TOUJOURS à l'entier supérieur

Résultat : 4 opérateurs nécessaires
```

**Vérification :**

- Avec 4 opérateurs : 187 / 4 = 46,75 s par opérateur ✅ (< 60s)
- Avec 3 opérateurs : 187 / 3 = 62,3 s par opérateur ❌ (> 60s → goulot !)

</details>

---

### 📝 Exercice 3 : Résoudre un Goulot d'Étranglement

**Situation Critique :**

- Takt Time : 60 secondes
- Temps de cycle de la machine de peinture : 75 secondes

**❌ Problème** : TC > TT → Vous ne pouvez pas satisfaire la demande !

**Question :** Quelles sont les 4 solutions possibles, classées par priorité Lean ?

<details>
<summary>💡 Solutions</summary>

### 1. **Kaizen (Amélioration Continue)** - PRIORITÉ 1

- **Action** : Analyser le poste pour éliminer les gaspillages
- **Objectif** : Réduire les 75s à moins de 60s
- **Exemples** :
  - Réduire les mouvements inutiles
  - Rapprocher les outils
  - Éliminer les attentes

### 2. **Balancement de Ligne** - PRIORITÉ 2

- **Action** : Redistribuer les tâches entre postes
- **Exemple** : Si l'emballage ne prend que 40s, l'emballeur peut aider le peintre

### 3. **Parallélisme** - PRIORITÉ 3

- **Action** : Installer 2 machines de peinture
- **Calcul** : 2 machines à 75s → une pièce toutes les 37,5s en sortie combinée

### 4. **Heures Supplémentaires** - SOLUTION TEMPORAIRE

- **Action** : Augmenter le temps disponible
- **⚠️ Attention** : Coûteux et ne résout pas le problème de fond

</details>

---

## TP 3 : Identification des Gaspillages (Mudas)

### 🎯 Objectif

Apprendre à identifier les 7+1 gaspillages dans un processus réel.

### 📚 Les 8 Gaspillages (Mudas)

| Muda | Description | Impact |
|------|-------------|---------|
| **1. Surproduction** | Produire plus ou plus tôt que nécessaire | 👑 Le PIRE des gaspillages |
| **2. Stocks** | Matières premières, en-cours, produits finis excessifs | Immobilise du cash |
| **3. Attentes** | Opérateur ou machine inactifs | Gaspille du temps |
| **4. Transports** | Déplacements inutiles de matières | Risque de dommages |
| **5. Mouvements** | Gestes inutiles de l'opérateur | Fatigue, perte de temps |
| **6. Surtraitement** | Opérations non demandées par le client | Coût sans valeur |
| **7. Défauts** | Rebuts, retouches, contrôles | Coût de non-qualité |
| **8. Potentiel humain** | Compétences non utilisées | Démotivation |

### 📝 Exercice : Chasse aux Mudas

**Contexte :** Atelier de fabrication de châssis métalliques

**Observations sur le terrain :**

1. L'opérateur marche 15 mètres pour chercher ses outils au début du poste
2. Les pièces attendent en moyenne 2 heures entre la découpe et le pliage
3. La machine produit des lots de 500 pièces alors que le client en demande 100/jour
4. 5% des pièces sont refusées au contrôle qualité
5. Les opérateurs ont proposé une amélioration il y a 6 mois, jamais mise en œuvre
6. Les pièces finies sont transportées 3 fois avant expédition
7. On polit les pièces alors que cette zone n'est pas visible une fois montée
8. Le soudeur attend 20 minutes par jour à cause de pannes récurrentes

**Question :** Identifiez le type de Muda pour chaque observation.

<details>
<summary>💡 Réponses</summary>

1. ➡️ **Mouvements** inutiles
2. ⏱️ **Attentes** (stock en-cours)
3. 📦 **Surproduction** (et génère du stock)
4. ✘ **Défauts** (rebuts)
5. 🧠 **Potentiel humain** inexploité
6. 🚚 **Transports** inutiles
7. ⚙️ **Surtraitement**
8. ⏱️ **Attentes** (panne machine)

</details>

---

### 📝 Exercice : Calculez l'Impact Financier

**Données :**

- Surproduction : 400 pièces/jour en excès
- Coût de stockage : 0,50 €/pièce/mois
- Défauts : 5% de 480 pcs/jour, coût matière : 8 €/pièce
- Temps d'attente : 20 min/jour, coût horaire opérateur : 42 €/h

**Question :** Quel est le coût mensuel de ces gaspillages (20 jours ouvrés) ?

<details>
<summary>💡 Calcul</summary>

**Surproduction :**

```
400 pcs × 20 jours = 8000 pièces stockées
8000 × 0,50 € = 4000 € de stockage
```

**Défauts :**

```
480 × 5% × 20 jours = 480 pièces rebutées
480 × 8 € = 3840 € de pertes matière
```

**Attentes :**

```
20 min/jour × 20 jours = 400 min = 6,67 heures
6,67 h × 42 € = 280 €
```

**Total : 4000 + 3840 + 280 = 8120 € / mois**

**Sur un an : 97 440 € gaspillés !**

</details>

---

## TP 4 : Conception de l'État Futur

### 🎯 Objectif

Transformer un flux "poussé" en flux "tiré" optimisé.

### 📋 Les 8 Questions Structurantes

Pour concevoir l'état futur, répondez systématiquement à ces questions :

1. **Quel est le Takt Time ?**
2. **Produisons-nous pour un supermarché ou directement à la commande ?**
3. **Où peut-on mettre du flux continu ?**
4. **Où a-t-on besoin d'un supermarché ?**
5. **Quel est le processus régulateur (Pacemaker) ?**
6. **Comment va-t-on niveler la production (Heijunka) ?**
7. **Quel incrément de travail libérera-t-on au Pacemaker ?**
8. **Quelles améliorations Kaizen sont nécessaires ?**

---

### 📝 Exercice : Transformation de Flash-Metal

**Reprenez le cas Flash-Metal du TP 1**

#### Étape 1 : Répondez aux 8 Questions

**Données complémentaires :**

- Mix produit : 60% Modèle A, 40% Modèle B
- Distance entre postes : 50 mètres
- Les opérations de Soudure et Peinture peuvent être regroupées

<details>
<summary>💡 Réponses Guidées</summary>

**1. Takt Time :**

```
27 000 s / 480 pcs = 56,25 secondes
```

**2. Production :**
Petit supermarché de produits finis (2 heures de stock) pour lisser les enlèvements

**3. Flux continu :**
Créer une cellule Soudure-Peinture (temps total : 60 + 40 = 100s, besoin de 2 opérateurs)

**4. Supermarché :**
Entre Pliage et Cellule Soudure-Peinture (machines éloignées)

**5. Pacemaker :**
La cellule Soudure-Peinture reçoit le planning

**6. Heijunka :**
Alterner A-A-B-A-A-B... pour refléter le mix 60/40

**7. Incrément :**
Pitch de 20 minutes (= environ 20 pièces)

**8. Kaizen :**

- Réduire les changements de série sur la Découpe
- Rapprocher les postes physiquement

</details>

---

#### Étape 2 : Dessinez l'État Futur

**Changements à représenter :**

✅ **Ajouts :**

- Symbole de flux continu entre Soudure et Peinture
- Symbole de supermarché après Pliage
- Boîte de lissage (Heijunka) au Pacemaker
- Éclairs "Kaizen" sur les améliorations

❌ **Suppressions :**

- 2 des 3 stocks (remplacés par flux continu)
- Les ordres de fabrication multiples (un seul au Pacemaker)

**Résultat attendu :**

```
Nouveau Lead Time : 0,83 jour (stock PF seulement) vs 6,25 jours
Réduction de 87% !
```

---

### 📝 Exercice : Comparaison Avant/Après

| Indicateur | État Actuel | État Futur | Gain |
|------------|-------------|------------|------|
| Lead Time | 6,25 jours | 0,83 jour | **-87%** |
| Stock total | 3000 pcs | 400 pcs | **-87%** |
| Distance parcourue | 200 m | 10 m | **-95%** |
| Points de planification | 4 | 1 | **-75%** |

---

## TP 5 : Mise en Place du Management Visuel Kanban

### 🎯 Objectif

Concevoir et organiser physiquement un système Kanban efficace.

### 📚 Les 3 Types de Kanban

#### 1. Le Supermarché de Pièces

**Objectif :** Contrôler les stocks intermédiaires entre deux processus

**Organisation Physique :**

```
┌─────────────────────────────────────┐
│     SUPERMARCHÉ EMBOUTISSAGE        │
│                                     │
│  [Bac A] [Bac B] [Bac C]           │
│  🏷️     🏷️     🏷️                │
│                                     │
│  [Bac D] [Bac E] [Bac F]           │
│  🏷️     🏷️     🏷️                │
│                                     │
│  📮 Boîte aux Lettres Kanban        │
└─────────────────────────────────────┘
```

**Contenu de la Carte Kanban :**

- 📸 Photo de la pièce
- 🔢 Référence : REF-12345
- 📦 Quantité par bac : 50 pièces
- 🏭 Fournisseur : Emboutissage
- 🎯 Client : Soudure
- 📍 Adresse : Allée B - Étagère 3

**Fonctionnement :**

1. L'opérateur soudure prend un bac
2. Il retire la carte Kanban et la met dans la boîte aux lettres
3. Le manutentionnaire ramasse les cartes toutes les heures
4. Il apporte les cartes à l'emboutissage = ordre de fabrication

---

#### 2. La Boîte de Lissage (Heijunka Box)

**Objectif :** Niveler la production au processus régulateur (Pacemaker)

**Calcul du Pitch (Pas de Gestion) :**

```
Pitch = Takt Time × Quantité par conteneur

Exemple :
Takt Time = 60 secondes
Conteneur = 20 pièces
Pitch = 60 × 20 = 1200 secondes = 20 minutes
```

**Organisation Physique :**

```
BOÎTE DE LISSAGE - ASSEMBLAGE FINAL
┌───────┬──────┬──────┬──────┬──────┬──────┐
│Produit│ 8h00 │ 8h20 │ 8h40 │ 9h00 │ 9h20 │
├───────┼──────┼──────┼──────┼──────┼──────┤
│Bras G │ 🟢   │ 🟢   │      │ 🟢   │      │
├───────┼──────┼──────┼──────┼──────┼──────┤
│Bras D │      │ 🔴   │ 🔴   │      │ 🔴   │
└───────┴──────┴──────┴──────┴──────┴──────┘

🟢 = Carte Kanban Bras Gauche
🔴 = Carte Kanban Bras Droit
```

**Avantage Visuel :**

- À 8h25, si des cartes restent dans la colonne 8h00 → RETARD VISIBLE
- Le mix produit (60% vert, 40% rouge) est visible d'un coup d'œil

---

#### 3. Le Kanban de Signalisation (Pour les Lots)

**Utilisation :** Machines nécessitant des changements de série longs (presses, fours)

**Organisation :**

```
STOCK PRESSE - PIÈCE A
┌────────────────────┐
│ ███████████████    │
│ ███████████████    │  ← Stock actuel
│ ███████████████    │
│ ███████████████    │
│ 🚩 POINT DE        │  ← Triangle de signalisation
│    COMMANDE        │
│                    │
└────────────────────┘

Quand le stock descend au triangle :
1. Retirer le triangle
2. L'accrocher sur le tableau de la presse
3. La presse lancera cette référence selon l'ordre des triangles
```

**Tableau Goulot Presse :**

```
┌─────────────────────────────────┐
│  PLANNING PRESSE - ORDRE PROD   │
├─────────────────────────────────┤
│  1. 🚩 Pièce C (prioritaire)    │
│  2. 🚩 Pièce A                  │
│  3. 🚩 Pièce F                  │
└─────────────────────────────────┘
```

---

### 📝 Exercice Pratique : Dimensionner un Système Kanban

**Contexte :** Supermarché entre Emboutissage et Soudure

**Données :**

- Demande quotidienne : 480 pièces
- Lead Time de réapprovisionnement : 2 heures
- Stock de sécurité : 10% de la consommation
- Capacité d'un conteneur : 60 pièces

**Questions :**

**1. Quelle est la consommation pendant le Lead Time ?**

<details>
<summary>💡 Réponse</summary>

```
Consommation horaire = 480 pcs / 8h = 60 pcs/h
Consommation pendant LT = 60 × 2h = 120 pièces
```

</details>

**2. Quel est le stock de sécurité ?**

<details>
<summary>💡 Réponse</summary>

```
Stock de sécurité = 120 × 10% = 12 pièces
```

</details>

**3. Combien de cartes Kanban sont nécessaires ?**

<details>
<summary>💡 Réponse</summary>

**Formule :**

```
Nombre de Kanban = (Consommation pendant LT + Stock sécurité) / Capacité conteneur
                 = (120 + 12) / 60
                 = 132 / 60
                 = 2,2
                 
Arrondi supérieur : 3 cartes Kanban
```

**Vérification :**

- 3 cartes × 60 pcs = 180 pièces en circulation
- Stock nominal : 120 pcs
- Marge : 60 pcs (50% de sécurité) ✅

</details>

---

### 📝 Exercice : Concevoir un Tableau Heijunka

**Situation :**

- Takt Time : 45 secondes
- Conteneur : 20 pièces
- Mix produit : 50% A, 30% B, 20% C
- Production : 8h (480 min)

**Questions :**

**1. Quel est le Pitch ?**

<details>
<summary>💡 Réponse</summary>

```
Pitch = 45s × 20 pcs = 900 secondes = 15 minutes
```

</details>

**2. Combien de colonnes (intervalles) dans la journée ?**

<details>
<summary>💡 Réponse</summary>

```
Nombre d'intervalles = 480 min / 15 min = 32 colonnes
```

</details>

**3. Répartition des produits sur 10 intervalles consécutifs :**

<details>
<summary>💡 Réponse</summary>

**Calcul :**

- Sur 10 intervalles : 50% A = 5, 30% B = 3, 20% C = 2

**Séquence nivelée (éviter les lots) :**

```
A - B - A - C - A - B - A - A - B - C
```

**Comparaison :**

- ❌ **Mauvais** : A-A-A-A-A-B-B-B-C-C (lots = stock)
- ✅ **Bon** : A-B-A-C-A-B-A-A-B-C (lissé)

</details>

---

## Cas Pratique Intégral : Usine ABC

### 📋 Présentation de l'Entreprise

**ABC Emboutissage** fabrique des supports de suspension pour l'industrie automobile.

**Processus complet :**

1. **Emboutissage** (presse)
2. **Usinage** (perçage)
3. **Soudure**
4. **Assemblage final**
5. **Expédition**

### 📊 Données Complètes

#### Demande Client

- **Client principal** : Peugeot-Citroën
- **Prévisions mensuelles** : envoyées par email le 20 du mois précédent
- **Commandes fermes** : envoyées par EDI chaque semaine
- **Livraisons** : 2 fois par jour (matin et après-midi)
- **Demande quotidienne** :
  - Bras gauche : 270 pièces
  - Bras droit : 270 pièces
  - **Total : 540 pièces/jour**

#### Organisation du Travail

- **Horaires** : 2 équipes × 8 heures
- **Pauses** : 2 × 15 min par équipe
- **Temps disponible** : 16h - 1h = **15h = 54 000 secondes/jour**

#### Processus Détaillés

| Poste | TC (sec) | Changement série | Disponibilité | Taux rebut |
|-------|----------|------------------|---------------|------------|
| Emboutissage | 20s | 60 min | 85% | 2% |
| Usinage | 35s | 15 min | 95% | 1% |
| Soudure | 45s | 10 min | 90% | 3% |
| Assemblage | 55s | 5 min | 100% | 0,5% |

#### Stocks Actuels

- Entre Emboutissage et Usinage : 3500 pièces
- Entre Usinage et Soudure : 2100 pièces
- Entre Soudure et Assemblage : 1800 pièces
- Produits finis : 1100 pièces

#### Flux d'Information Actuel

- Planning central envoie un ordre de fabrication hebdomadaire à chaque poste (par papier)
- Chaque chef de poste décide de l'ordre de lancement
- Aucune synchronisation entre postes

### 🎯 Missions du TP Intégral

#### Mission 1 : Analyser l'État Actuel

**À réaliser :**

1. Dessiner la VSM complète de l'état actuel
2. Calculer le Takt Time
3. Calculer le Lead Time total
4. Calculer le ratio de tension
5. Identifier les 8 gaspillages présents

<details>
<summary>💡 Corrigé Mission 1</summary>

**1. Takt Time :**

```
TT = 54 000 s / 540 pcs = 100 secondes
```

**2. Lead Time (ligne de temps) :**

```
Stock 1 : 3500 / 540 = 6,48 jours
Stock 2 : 2100 / 540 = 3,89 jours
Stock 3 : 1800 / 540 = 3,33 jours
Stock 4 : 1100 / 540 = 2,04 jours

Total Lead Time = 15,74 jours
```

**3. Temps de VA :**

```
VA = 20 + 35 + 45 + 55 = 155 secondes
```

**4. Ratio de tension :**

```
15,74 jours × 54 000 s/jour = 850 000 secondes
Ratio = 850 000 / 155 = 5 484

0,018% seulement de VA !
```

**5. Gaspillages identifiés :**

- **Surproduction** : Production par lots hebdomadaires
- **Stocks** : 8500 pièces immobilisées
- **Attentes** : Pièces qui attendent entre postes
- **Transports** : Multiples allers-retours
- **Défauts** : 2% + 1% + 3% + 0,5% = perte de matière
- **Surtraitement** : Production sans lien avec commandes fermes
- **Potentiel humain** : Chaque poste optimise localement (pas de vue globale)

</details>

---

#### Mission 2 : Concevoir l'État Futur

**Contraintes à respecter :**

- L'emboutissage doit rester en lots (changement de série long)
- Soudure et Assemblage peuvent être rapprochés physiquement
- Budget pour une seule machine supplémentaire si nécessaire

**Questions guidées :**

**Q1 : Quel processus doit être le Pacemaker ?**

<details>
<summary>💡 Réponse</summary>

**L'Assemblage final** doit être le Pacemaker car :

- C'est le processus le plus proche du client
- C'est là que les 2 variantes (G et D) sont différenciées
- TC de 55s < TT de 100s → capacité suffisante

</details>

**Q2 : Où peut-on créer du flux continu ?**

<details>
<summary>💡 Réponse</summary>

**Entre Soudure et Assemblage :**

- Temps total : 45 + 55 = 100 secondes
- Exactement égal au Takt Time !
- **Besoin : 1 soudeur + 1 assembleur**

**Avantage :** Supprime 1800 pièces de stock (3,33 jours)

</details>

**Q3 : Où placer des supermarchés ?**

<details>
<summary>💡 Réponse</summary>

**Supermarché 1 :** Après Emboutissage

- Stock de 4 heures de consommation
- 540 pcs/jour × (4h/15h) = 144 pièces

**Supermarché 2 :** Après Usinage  

- Stock de 2 heures
- 540 × (2/15) = 72 pièces

**Total stock = 216 pièces vs 8500 actuellement (-97% !)**

</details>

**Q4 : L'Usinage est-il un goulot ?**

<details>
<summary>💡 Réponse</summary>

**Calcul :**

- TC = 35s (< TT de 100s) : OK en théorie
- Mais disponibilité = 95% et rebut = 1%
- TC réel = 35 / (0,95 × 0,99) = 37,2s

**Toujours < 100s → Pas de goulot avec 1 machine**

</details>

**Q5 : Comment niveler la production ?**

<details>
<summary>💡 Réponse</summary>

**Heijunka Box à l'Assemblage :**

- Mix : 50% Gauche, 50% Droite
- Pitch : 100s × 20 pcs = 2000s = 33 min
- Séquence : G-D-G-D-G-D...

**Nombre d'intervalles par jour :**

```
15h × 60 min / 33 min = 27 Pitch par jour
```

</details>

---

#### Mission 3 : Quantifier les Gains

**Calculez les gains de l'état futur :**

<details>
<summary>💡 Réponse Mission 3</summary>

| Indicateur | Avant | Après | Gain | Impact € |
|------------|-------|-------|------|----------|
| **Lead Time** | 15,74 j | 0,5 j | **-97%** | Réactivité client |
| **Stock** | 8500 pcs | 216 pcs | **-97%** | 82 840 €* |
| **Surface** | 400 m² | 120 m² | **-70%** | 70 000 €/an |
| **Distance** | 300 m | 20 m | **-93%** | Productivité |
| **Planification** | 4 points | 1 point | **-75%** | Simplification |

*Calcul stock : (8500-216) × 10 € de coût matière moyen = 82 840 € libérés*

**Retour sur investissement :**

- Coût du projet : ~50 000 € (rapprochement machines, racks)
- Économies annuelles : ~150 000 €
- **ROI : 4 mois**

</details>

---

#### Mission 4 : Créer le Plan d'Action

**Découpez en boucles Kaizen :**

<details>
<summary>💡 Réponse Mission 4</summary>

**Boucle 1 : Pacemaker (Semaines 1-4)**

- Créer la cellule Soudure-Assemblage
- Installer la Heijunka Box
- Former les opérateurs au nivelage
- **Responsable :** Chef d'atelier assemblage

**Boucle 2 : Supermarchés (Semaines 5-8)**

- Installer les racks Kanban
- Créer les cartes (avec photos)
- Former les manutentionnaires
- **Responsable :** Responsable logistique

**Boucle 3 : Emboutissage (Semaines 9-12)**

- Chantier SMED (réduction changement série)
- Objectif : passer de 60 min à 20 min
- **Responsable :** Responsable production

**Boucle 4 : Usinage (Semaines 13-16)**

- Améliorer la disponibilité (maintenance préventive)
- Objectif : passer de 95% à 98%
- **Responsable :** Maintenance

</details>

---

## Annexes : Symboles et Formules

### 🔣 Symboles VSM Essentiels

| Symbole | Nom | Utilisation |
|---------|-----|-------------|
| 🏭 | Usine/Client | Fournisseur externe ou client |
| 📦 | Processus | Étape de transformation |
| ▽ | Stock | Stock physique (en jours ou pièces) |
| 🚚 | Transport | Camion, livraison |
| ➡️ | Flux poussé | Production sans signal du client |
| ⚡ | Flux électronique | Email, EDI, système informatique |
| → | Flux manuel | Information papier |
| OXOX | Flux continu | Production pièce à pièce |
| 🏪 | Supermarché | Stock contrôlé avec Kanban |
| ⚡KAIZEN | Éclair Kaizen | Amélioration nécessaire |
| ⏱️ | Boîte données | TC, Taux disponibilité, rebuts... |

### 📐 Formules Clés

#### 1. Takt Time

```
Takt Time = Temps Disponible (secondes) / Demande Client (pièces)
```

#### 2. Temps Disponible

```
Temps Disponible = (Heures de travail - Pauses - Réunions) × 3600
```

#### 3. Dimensionnement

```
Nb Opérateurs = ⌈ Temps Cycle Total / Takt Time ⌉
(⌈ ⌉ = arrondi supérieur)
```

#### 4. Lead Time (Stock)

```
Jours de Stock = Quantité en Stock / Demande Quotidienne
```

#### 5. Ratio de Tension

```
Ratio = Lead Time Total / Temps de Valeur Ajoutée Total
```

#### 6. Nombre de Kanban

```
Nb Kanban = ⌈ (Consommation pendant LT + Stock Sécurité) / Capacité Conteneur ⌉
```

#### 7. Pitch

```
Pitch (secondes) = Takt Time × Quantité par Conteneur
```

#### 8. Efficacité Globale (TRS/OEE)

```
TRS = Disponibilité × Performance × Qualité

Exemple :
TRS = 85% × 90% × 97% = 74,2%
```

---

### 📚 Glossaire

| Terme | Définition |
|-------|------------|
| **Gemba** | Le terrain, là où la valeur est créée |
| **Heijunka** | Lissage/nivellement de la production |
| **Jidoka** | Autonomation, qualité à la source |
| **Kaizen** | Amélioration continue |
| **Kanban** | Carte ou signal visuel de réapprovisionnement |
| **Muda** | Gaspillage, activité sans valeur ajoutée |
| **Pacemaker** | Processus régulateur qui reçoit le planning |
| **Pitch** | Pas de gestion = Takt Time × Qté conteneur |
| **SMED** | Réduction des temps de changement de série |
| **Takt Time** | Rythme de production imposé par le client |
| **VSM** | Value Stream Mapping, cartographie du flux |

---

### 📋 Checklist Finale

Avant de considérer votre VSM comme terminée, vérifiez :

**État Actuel :**

- [ ] Le client est dessiné en haut à droite
- [ ] Les flux sont tracés de droite à gauche
- [ ] Tous les stocks sont représentés (triangles)
- [ ] Les flux d'information sont différenciés (manuel/électronique)
- [ ] La ligne de temps (Lead Time) est calculée
- [ ] Le ratio de tension est choquant (sinon, revérifiez vos calculs)

**État Futur :**

- [ ] Le Takt Time est calculé et affiché
- [ ] Le Pacemaker est identifié
- [ ] Au moins une zone de flux continu est créée
- [ ] Les supermarchés nécessaires sont placés
- [ ] La Heijunka Box est représentée
- [ ] Les éclairs Kaizen indiquent les améliorations
- [ ] Le nouveau Lead Time est calculé (réduction > 50%)

**Plan d'Action :**

- [ ] Les boucles Kaizen sont définies
- [ ] Chaque boucle a un responsable nommé
- [ ] Un calendrier (semaines) est établi
- [ ] Les indicateurs de succès sont définis
- [ ] Le cycle PDCA est prévu pour chaque boucle

---

## 🎓 Pour Aller Plus Loin

### Exercices Complémentaires

1. **Votre Propre Flux :**
   - Cartographiez un processus de votre entreprise
   - Calculez votre ratio de tension
   - Proposez 3 améliorations concrètes

2. **Simulation Heijunka :**
   - Avec des LEGO ou des cartes à jouer
   - Comparez production par lots vs production lissée
   - Mesurez les temps de traversée

3. **Chantier SMED :**
   - Filmez un changement de série
   - Identifiez les opérations internes/externes
   - Proposez un nouveau standard

### Ressources Recommandées

**Livres :**

- "Learning to See" - Mike Rother & John Shook
- "Système Lean" - James P. Womack
- "Le système de production Toyota" - Taiichi Ohno

**Outils :**

- Feuilles A3 et crayons (indispensables !)
- Chronomètres
- Post-it de couleurs
- Appareil photo (pour documenter l'état actuel)

---

**📌 Version du document :** 1.0  
**📅 Date de création :** 24 janvier 2026  
**✍️ Formateur :** Formation VSM - Pôle UIMM CVDL

---

**Bonne formation ! 🚀**
