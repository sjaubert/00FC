---
output:
  word_document: default
  html_document: default
---
![Logo UIMM](../logo_uimm.jpg)

# Pole Formation UIMM-CVDL

---

# TPM / MAINTENANCE - GUIDE FORMATEUR

## Le Dilemme de Production : Simulation de Maintenance Industrielle

**Duree totale** : 4 heures  
**Nombre de participants** : 6 a 12 personnes (equipes de 3-4)  
**Niveau** : BTS Maintenance / Bachelor  
**Materiel necessaire** : Des, fiches machine, tableaux de calcul, cartes evenements

---

## TABLE DES MATIERES

1. [Objectifs pedagogiques](#objectifs-pedagogiques)
2. [Presentation de la TPM](#presentation-de-la-tpm)
3. [Scenario et regles du jeu](#scenario-et-regles-du-jeu)
4. [Deroulement detaille](#deroulement-detaille)
5. [Cartes evenements et pannes](#cartes-evenements-et-pannes)
6. [Calculs et indicateurs](#calculs-et-indicateurs)
7. [Debriefing](#debriefing)

---

## 1. OBJECTIFS PEDAGOGIQUES

A l'issue de cette simulation, les participants seront capables de :

- **Calculer** les indicateurs MTBF, MTTR et TRG
- **Comparer** les strategies de maintenance (curative vs preventive)
- **Arbitrer** entre production immediate et fiabilite a long terme
- **Identifier** les leviers d'amelioration du TRG
- **Comprendre** les principes de la TPM (Total Productive Maintenance)
- **Chiffrer** le cout des differentes strategies

---

## 2. PRESENTATION DE LA TPM

### 2.1 Definition

La TPM (Total Productive Maintenance ou Maintenance Productive Totale) est une demarche d'amelioration continue visant a maximiser la disponibilite des equipements en impliquant tous les acteurs.

### 2.2 Les 8 piliers de la TPM

| Pilier | Description |
|--------|-------------|
| 1. Amelioration au cas par cas | Eliminer les pertes |
| 2. Maintenance autonome | Operateurs formes a la maintenance 1er niveau |
| 3. Maintenance planifiee | Prevision et planification des interventions |
| 4. Amelioration des competences | Formation continue |
| 5. Conception maintenance | Integrer la maintenabilite des la conception |
| 6. Maintenance qualite | Lien entre qualite et maintenance |
| 7. TPM dans les bureaux | Appliquer aux fonctions support |
| 8. Securite et environnement | Zero accident |

### 2.3 Les 6 pertes majeures

| Perte | Type | Impact |
|-------|------|--------|
| Pannes | Disponibilite | Arrets non planifies |
| Changements de serie | Disponibilite | Temps de reglage |
| Micro-arrets | Performance | Petits blocages |
| Ralentissements | Performance | Vitesse reduite |
| Rebuts au demarrage | Qualite | Pieces non conformes |
| Defauts en production | Qualite | Non-qualite |

---

## 3. SCENARIO ET REGLES DU JEU

### 3.1 Contexte

Les participants dirigent l'atelier de production d'une usine fictive **PRODMAX Industries**. L'atelier comprend 4 machines en serie. L'objectif est de maximiser la production sur 10 semaines tout en minimisant les couts.

### 3.2 Configuration de l'atelier

```
[Machine A] --> [Machine B] --> [Machine C] --> [Machine D] --> [Expedition]
  (Decoupe)     (Pliage)        (Soudure)       (Peinture)
```

### 3.3 Caracteristiques des machines

| Machine | Age | MTBF theorique | MTTR moyen | Cout panne |
|---------|-----|----------------|------------|------------|
| A - Decoupe | 8 ans | 40h | 4h | 2000 EUR |
| B - Pliage | 5 ans | 60h | 2h | 1500 EUR |
| C - Soudure | 12 ans | 25h | 6h | 3000 EUR |
| D - Peinture | 3 ans | 80h | 3h | 2500 EUR |

### 3.4 Parametres economiques

| Element | Valeur |
|---------|--------|
| Prix de vente unitaire | 50 EUR |
| Cout production unitaire | 30 EUR |
| Marge unitaire | 20 EUR |
| Cadence theorique | 10 pieces/heure |
| Temps disponible | 40h/semaine |
| Cout maintenance preventive | 500 EUR/machine/semaine |
| Cout intervention curative | Variable (voir tableau) |
| Cout horaire arret | 500 EUR/heure |

### 3.5 Regles de probabilite des pannes

Les pannes sont determinees par un lancer de des en debut de chaque semaine.

**Sans maintenance preventive :**

| Machine | De | Panne si... |
|---------|----|----|
| A (8 ans) | D6 | 1 ou 2 |
| B (5 ans) | D6 | 1 |
| C (12 ans) | D6 | 1, 2 ou 3 |
| D (3 ans) | D6 | 1 seulement avec D20 < 5 |

**Avec maintenance preventive :**

La probabilite de panne est divisee par 2 (ex: Machine C panne si 1 seulement).

---

## 4. DEROULEMENT DETAILLE

### 4.1 Planning de la session

| Horaire | Phase | Duree | Contenu |
|---------|-------|-------|---------|
| 0:00 | Introduction | 25 min | Presentation TPM, regles du jeu |
| 0:25 | Tour 1 (S1-S4) | 40 min | Strategie reactive (curatif) |
| 1:05 | Debriefing 1 | 20 min | Calcul TRG, analyse |
| 1:25 | Formation | 30 min | Maintenance preventive, MTBF/MTTR |
| 1:55 | **PAUSE** | 15 min | - |
| 2:10 | Tour 2 (S5-S7) | 35 min | Introduction maintenance preventive |
| 2:45 | Debriefing 2 | 20 min | Comparaison resultats |
| 3:05 | Tour 3 (S8-S10) | 35 min | Strategie TPM optimisee |
| 3:40 | Debriefing final | 20 min | Synthese, gains, transfert |
| 4:00 | **FIN** | - | - |

### 4.2 Deroulement d'une semaine

Chaque semaine se deroule ainsi :

1. **Tirage des pannes** : Lancer les des pour chaque machine
2. **Gestion des pannes** : Decider de la priorite de reparation
3. **Options de maintenance** : Decider si maintenance preventive (cout 500 EUR)
4. **Calcul production** : Pieces produites = Heures disponibles x Cadence
5. **Calcul financier** : Marge - Couts pannes - Couts maintenance
6. **Report au tableau** : Noter les resultats

### 4.3 Contraintes

- **Une seule equipe de maintenance** : On ne peut reparer qu'une machine a la fois
- **Priorite de ligne** : Si plusieurs machines tombent en panne, la ligne est arretee
- **Maintenance preventive** : Doit etre decidee EN DEBUT de semaine (avant tirage)
- **Pas de stockage** : Les machines sont en serie, pas de buffer

---

## 5. CARTES EVENEMENTS ET PANNES

### 5.1 Cartes evenements speciaux (a tirer 1 fois par tour)

| N. | Evenement | Effet |
|----|-----------|-------|
| 1 | Urgence client | Production x 1.5 demandee cette semaine |
| 2 | Piece de rechange manquante | MTTR double pour prochaine panne |
| 3 | Operateur experimente | Micro-arrets reduits de 50% |
| 4 | Maintenance externe | Une reparation gratuite |
| 5 | Audit client | Malus 5000 EUR si TRG < 80% |
| 6 | Innovation | Cout preventif reduit a 300 EUR |
| 7 | Penurie energie | Production limitee a 30h |
| 8 | Formation operateur | Machine au choix MTBF +20h |
| 9 | Defaillance fournisseur | 1 semaine sans production machine C |
| 10 | Investissement autorise | Remplacement 1 machine (reset MTBF) |

### 5.2 Types de pannes

| Type | Duree reparation | Cout |
|------|------------------|------|
| Mineure | MTTR / 2 | Cout base / 2 |
| Standard | MTTR | Cout base |
| Majeure | MTTR x 2 | Cout base x 2 |
| Catastrophique | MTTR x 3 | Cout base x 3 + pieces |

Pour determiner le type : lancer D6 apres une panne

- 1-3 : Mineure
- 4-5 : Standard
- 6 : Majeure (relancer, 6 = Catastrophique)

---

## 6. CALCULS ET INDICATEURS

### 6.1 MTBF (Mean Time Between Failures)

```
MTBF = Temps de fonctionnement total / Nombre de pannes

Exemple :
- Temps total : 40h
- 2 pannes
- MTBF = 40 / 2 = 20h
```

### 6.2 MTTR (Mean Time To Repair)

```
MTTR = Temps total de reparation / Nombre de pannes

Exemple :
- Reparations : 4h + 6h = 10h
- 2 pannes
- MTTR = 10 / 2 = 5h
```

### 6.3 TRG (Taux de Rendement Global)

```
TRG = Disponibilite x Performance x Qualite

Ou :
- Disponibilite = (Temps requis - Arrets) / Temps requis
- Performance = (Temps net - Micro-arrets) / (Temps requis - Arrets)
- Qualite = Pieces bonnes / Pieces totales
```

### 6.4 Exemple de calcul semaine

| Element | Valeur |
|---------|--------|
| Temps disponible | 40h |
| Panne machine C | 6h |
| Temps reel | 34h |
| Cadence theorique | 10 p/h |
| Production theorique | 340 pieces |
| Micro-arrets | 10% |
| Production reelle | 306 pieces |
| Rebuts | 3% |
| Production bonne | 297 pieces |

**TRG = (34/40) x 0.90 x 0.97 = 74.2%**

---

## 7. DEBRIEFING

### 7.1 Questions de debriefing

**Apres Tour 1 (strategie reactive) :**

1. Quel a ete votre TRG moyen ?
2. Quelle machine a pose le plus de problemes ?
3. Quel a ete le cout total des pannes ?
4. Auriez-vous pu eviter certaines pannes ?

**Apres Tour 2 (maintenance preventive) :**

1. La maintenance preventive a-t-elle ete rentable ?
2. Sur quelles machines l'avez-vous appliquee ?
3. Comment a evolue votre TRG ?

**Apres Tour 3 (strategie optimisee) :**

1. Quelle est votre strategie finale ?
2. Quel est le gain par rapport au debut ?
3. Comment transposer ces enseignements dans votre entreprise ?

### 7.2 Resultats types

| Strategie | TRG moyen | Cout pannes | Marge nette |
|-----------|-----------|-------------|-------------|
| Full curatif | 65-75% | Eleve | Faible |
| Preventif partiel | 75-85% | Moyen | Moyenne |
| TPM optimisee | 85-95% | Faible | Elevee |

### 7.3 Tableaux comparatifs a completer

| Indicateur | Tour 1 | Tour 2 | Tour 3 |
|------------|--------|--------|--------|
| TRG moyen | | | |
| Nb pannes | | | |
| Cout pannes | | | |
| Cout preventif | | | |
| Production | | | |
| Marge totale | | | |

### 7.4 Lecons cles

1. **La maintenance preventive coute moins cher que les pannes** quand les equipements sont critiques
2. **Le TRG est un indicateur global** qui revele les vrais problemes
3. **L'age des machines** impacte fortement la fiabilite
4. **L'arbitrage production/maintenance** est au coeur de la performance industrielle
5. **La TPM implique tout le monde** : production, maintenance, qualite

---

## ANNEXES

### Annexe A : Tableau de suivi par semaine

A photocopier et distribuer aux equipes.

### Annexe B : Solutions optimales

**Strategie recommandee :**

- Maintenance preventive systematique sur Machine C (la plus ancienne)
- Maintenance preventive sur Machine A (8 ans, critique en tete de ligne)
- Surveillance renforcee sur Machine B
- Machine D en curatif (fiable, jeune)

**Budget optimal :**

- Preventif : 1000 EUR/semaine (2 machines)
- Gain estime : 3000 EUR/semaine en pannes evitees
- ROI : 200%

---

**Document cree par Pole Formation UIMM-CVDL**  
**Version 1.0 - Fevrier 2026**
