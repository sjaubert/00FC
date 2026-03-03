![Logo UIMM](logo_uimm.jpg)

# Pole Formation UIMM-CVDL

---

# JEU DE L'AVION EN PAPIER - GUIDE FORMATEUR

## Simulation Lean Manufacturing - Flux Pousse vs Flux Tire

**Duree totale** : 4 heures  
**Nombre de participants** : 8 a 12 personnes  
**Niveau** : BTS / Bachelor  
**Materiel necessaire** : Feuilles A4 (100 minimum), chronometre, tableau blanc, marqueurs

---

## TABLE DES MATIERES

1. [Objectifs pedagogiques](#objectifs-pedagogiques)
2. [Preparation de la salle](#preparation-de-la-salle)
3. [Attribution des roles](#attribution-des-roles)
4. [Deroulement detaille](#deroulement-detaille)
5. [Regles et consignes par round](#regles-et-consignes-par-round)
6. [Fiches de debriefing](#fiches-de-debriefing)
7. [Solutions et reponses attendues](#solutions-et-reponses-attendues)
8. [Transfert vers l'entreprise](#transfert-vers-lentreprise)

---

## 1. OBJECTIFS PEDAGOGIQUES

A l'issue de cette simulation, les participants seront capables de :

- **Distinguer** le flux pousse (Push) du flux tire (Pull)
- **Identifier** les 7 gaspillages (Muda) dans un processus de production
- **Mesurer** l'impact du systeme Kanban sur le Lead Time et les en-cours (WIP)
- **Appliquer** la demarche Kaizen pour ameliorer un processus entre deux iterations
- **Calculer** les indicateurs de performance (Lead Time, WIP, Taux de qualite, Productivite)
- **Equilibrer** une ligne de production en utilisant le concept de Takt Time

---

## 2. PREPARATION DE LA SALLE

### 2.1 Disposition initiale (Round 1 - Flux Pousse)

```
+------------------+     +------------------+     +------------------+
|   POSTE 1        | --> |   POSTE 2        | --> |   POSTE 3        |
|   Pliage base    |     |   Pliage ailes   |     |   Pliage final   |
+------------------+     +------------------+     +------------------+
        |                        |                        |
        v                        v                        v
   [Stock MP]              [En-cours]               [En-cours]
                                                          |
                                                          v
                                              +------------------+
                                              |   POSTE 4        |
                                              |   Finition       |
                                              +------------------+
                                                          |
                                                          v
                                              +------------------+
                                              |   CONTROLE       |
                                              |   QUALITE        |
                                              +------------------+
                                                          |
                                                          v
                                              +------------------+
                                              |   CLIENT         |
                                              |   (Livraison)    |
                                              +------------------+
```

### 2.2 Materiel a preparer

| Element | Quantite | Observations |
|---------|----------|--------------|
| Feuilles A4 blanches | 100 | Matiere premiere |
| Feuilles A4 couleur (3 couleurs) | 30 de chaque | Pour differencier les commandes |
| Chronometre | 2 | Un pour le Lead Time, un pour les cycles |
| Tableau blanc | 1 | Pour noter les KPIs |
| Marqueurs | 4 | Couleurs differentes |
| Fiches de poste plastifiees | 4 | Une par operateur |
| Gabarits de pliage | 4 | Pour le Round 3 |
| Cartes Kanban | 20 | Pour le Round 2 |
| Tableau de suivi KPI | 1 | Version grand format |

### 2.3 Preparation des postes

**Avant l'arrivee des participants :**

1. Disposer les tables en ligne droite (configuration initiale)
2. Placer 30 feuilles A4 au poste 1 (stock matiere premiere)
3. Preparer les fiches de poste (face cachee)
4. Afficher le tableau de suivi KPI vierge
5. Preparer les cartes Kanban (ne pas les montrer avant le Round 2)
6. Verifier que les gabarits de pliage sont prets (pour le Round 3)

---

## 3. ATTRIBUTION DES ROLES

### 3.1 Roles des participants

| Role | Nombre | Responsabilites |
|------|--------|-----------------|
| Operateur Poste 1 | 1 | Pliage de base selon fiche d'instruction |
| Operateur Poste 2 | 1 | Pliage des ailes selon fiche d'instruction |
| Operateur Poste 3 | 1 | Pliage final selon fiche d'instruction |
| Operateur Poste 4 | 1 | Finition et ajustements |
| Controleur Qualite | 1 | Verification selon criteres, comptage rebuts |
| Manutentionnaire | 1 | Transfer des pieces entre postes |
| Chronometreur | 1 | Mesure Lead Time et temps de cycle |
| Observateur Muda | 1 | Identification des gaspillages |
| Manager de Production | 1 | Pilotage, analyse, animation debriefing |
| Client | 1 | Reception, verification satisfaction |

### 3.2 Script d'attribution (a lire aux participants)

> "Vous allez constituer une usine de fabrication d'avions en papier. Chacun d'entre vous va occuper un poste specifique. L'objectif de l'entreprise est de satisfaire le client en livrant des avions conformes, dans les meilleurs delais et au moindre cout. Vous serez evalues sur plusieurs indicateurs : le temps de traversee, la quantite produite, le niveau de qualite et le niveau d'en-cours. Vos decisions et votre organisation vont directement impacter ces resultats."

---

## 4. DEROULEMENT DETAILLE

### 4.1 Planning de la journee

| Horaire | Phase | Duree | Contenu |
|---------|-------|-------|---------|
| 0:00 | Introduction | 20 min | Presentation, attribution roles |
| 0:20 | Round 1 | 30 min | Production flux pousse |
| 0:50 | Debriefing 1 | 20 min | Analyse KPIs, identification Muda |
| 1:10 | Round 2 | 30 min | Introduction Kanban |
| 1:40 | Debriefing 2 | 20 min | Comparaison resultats |
| 2:00 | **PAUSE** | 15 min | - |
| 2:15 | Round 3 | 30 min | Equilibrage ligne + gabarits |
| 2:45 | Debriefing 3 | 20 min | Analyse amelioration |
| 3:05 | Round 4 | 30 min | Flux piece a piece + cellule en U |
| 3:35 | Debriefing final | 25 min | Synthese, transfert entreprise |
| 4:00 | **FIN** | - | - |

---

## 5. REGLES ET CONSIGNES PAR ROUND

### 5.1 ROUND 1 : LE CHAOS DU FLUX POUSSE

#### Objectif cache (ne pas reveler aux participants)

Creer volontairement un systeme inefficace pour que les participants vivent les problemes du flux pousse.

#### Regles a annoncer

1. **Production par lots** : Chaque operateur doit terminer un lot de 5 avions avant de les passer au poste suivant
2. **Pas de communication** : Les operateurs ne doivent pas parler entre eux pendant la production
3. **Prime individuelle** : Chaque operateur est evalue sur SA production personnelle (nombre de pieces traitees)
4. **Stockage libre** : Les en-cours peuvent s'accumuler sans limite entre les postes
5. **Duree** : 10 minutes de production effective

#### Script formateur (Round 1)

> "Nous allons demarrer la production. Chaque operateur doit produire le maximum de pieces possible. Vous travaillez par lots de 5 : vous ne passez vos pieces au poste suivant que lorsque vous avez termine 5 avions. Votre performance individuelle sera evaluee. C'est parti !"

#### Observations a noter (pour le formateur)

- [ ] Accumulation d'en-cours entre les postes ?
- [ ] Quel poste devient le goulot d'etranglement ?
- [ ] Combien de temps avant la premiere livraison client ?
- [ ] Reactions des operateurs (stress, frustration) ?
- [ ] Defauts qualite observes ?
- [ ] Gaspillages identifies (attentes, mouvements, stocks) ?

#### Resultats attendus (Round 1)

| KPI | Resultat typique | Explication |
|-----|------------------|-------------|
| Lead Time | 8-15 minutes | Tres long a cause des lots |
| WIP (en-cours) | 15-25 pieces | Accumulation massive |
| Taux qualite | 60-80% | Defauts detectes tard |
| Livraisons client | 3-6 avions | Faible productivite reelle |

---

### 5.2 ROUND 2 : INTRODUCTION DU FLUX TIRE (KANBAN)

#### Changements a introduire

1. **Systeme Kanban** : Une carte Kanban accompagne chaque avion
2. **Regle du Kanban** : On ne produit que si on recoit une carte du poste aval
3. **Limite des en-cours** : Maximum 2 pieces entre chaque poste
4. **Communication autorisee** : Signaux visuels permis

#### Script formateur (Round 2)

> "Nous avons observe des problemes lors du premier round. Nous allons maintenant introduire le systeme Kanban. Voici les nouvelles regles : vous ne pouvez produire une piece QUE si vous recevez une carte Kanban du poste suivant. Cette carte signifie que le poste aval a besoin d'une piece. Le stock maximum entre chaque poste est de 2 pieces. Si vous avez deja 2 pieces en attente, vous devez ARRETER de produire et attendre."

#### Mecanisme Kanban a mettre en place

```
[Client demande] --> Carte au Poste 4 --> Carte au Poste 3 --> Carte au Poste 2 --> Carte au Poste 1

Flux des cartes Kanban (remonte vers l'amont)
<----------------------------------------------------

Flux des avions (descend vers l'aval)
---------------------------------------------------->
```

#### Resultats attendus (Round 2)

| KPI | Resultat typique | Evolution |
|-----|------------------|-----------|
| Lead Time | 4-7 minutes | Reduction 40-50% |
| WIP (en-cours) | 6-10 pieces | Reduction 50-60% |
| Taux qualite | 75-90% | Amelioration |
| Livraisons client | 6-10 avions | Amelioration |

---

### 5.3 ROUND 3 : EQUILIBRAGE ET STANDARDISATION

#### Changements a introduire

1. **Analyse Yamazumi** : Mesure du temps de cycle par poste
2. **Redistribution des taches** : Equilibrer la charge de travail
3. **Gabarits de pliage** : Introduction d'outils d'aide au travail
4. **Instructions visuelles** : Affichage des modes operatoires

#### Activite d'analyse (15 minutes avant le round)

Demander aux participants de :

1. Chronometrer le temps de cycle de chaque poste (3 mesures)
2. Identifier le poste goulot (temps de cycle le plus long)
3. Proposer une redistribution des taches
4. Calculer le Takt Time cible

#### Calcul du Takt Time

```
Takt Time = Temps disponible / Demande client

Exemple :
- Temps disponible : 10 minutes = 600 secondes
- Demande client : 15 avions
- Takt Time = 600 / 15 = 40 secondes par avion
```

#### Resultats attendus (Round 3)

| KPI | Resultat typique | Evolution |
|-----|------------------|-----------|
| Lead Time | 2-4 minutes | Reduction supplementaire |
| WIP (en-cours) | 4-6 pieces | Reduction |
| Taux qualite | 90-95% | Grace aux gabarits |
| Livraisons client | 12-18 avions | Nette amelioration |

---

### 5.4 ROUND 4 : FLUX PIECE A PIECE ET CELLULE EN U

#### Changements a introduire

1. **Cellule en U** : Reorganisation physique des postes
2. **Flux piece a piece** : Transfert immediat apres chaque operation
3. **Polyvalence** : Les operateurs peuvent s'entraider
4. **Suppression du manutentionnaire** : Postes suffisamment proches

#### Nouvelle disposition

```
        +------------------+
        |   POSTE 4        |
        |   Finition       |
        +------------------+
              ^     |
              |     v
+----------+  |  +----------+
| POSTE 1  |  |  | CONTROLE |
| Base     |--+  | QUALITE  |
+----------+     +----------+
    |                 |
    v                 v
+----------+     +----------+
| POSTE 2  |     | CLIENT   |
| Ailes    |     | Livraison|
+----------+     +----------+
    |
    v
+----------+
| POSTE 3  |
| Final    |
+----------+
```

#### Resultats attendus (Round 4)

| KPI | Resultat typique | Evolution globale |
|-----|------------------|-------------------|
| Lead Time | 1-2 minutes | -80% vs Round 1 |
| WIP (en-cours) | 2-3 pieces | -85% vs Round 1 |
| Taux qualite | 95-100% | Detection immediate |
| Livraisons client | 20-30 avions | +400% vs Round 1 |

---

## 6. FICHES DE DEBRIEFING

### 6.1 Questions pour le debriefing Round 1

**Phase emotionnelle** (5 min)

1. Comment vous etes-vous senti pendant ce round ?
2. Qu'est-ce qui vous a frustre ?
3. Avez-vous eu l'impression de bien travailler ?

**Phase factuelle** (10 min)

1. Combien d'avions avez-vous livre au client ?
2. Combien d'avions sont restes en-cours a la fin ?
3. Quel etait le temps de traversee du premier avion ?
4. Quel etait le taux de qualite ?

**Phase analytique** (5 min)

1. Ou se trouvait le goulot d'etranglement ?
2. Quels gaspillages avez-vous observes ?
3. Pourquoi le lead time etait-il si long ?

### 6.2 Grille d'identification des 7 Muda

| Muda | Definition | Observation Round 1 |
|------|------------|---------------------|
| Surproduction | Produire plus que necessaire | Poste 1 qui continue alors que stocks pleins |
| Attentes | Temps mort sans valeur ajoutee | Poste 3 attend les pieces du poste 2 |
| Transports | Deplacements inutiles de pieces | Manutentionnaire fait des allers-retours |
| Surprocessing | Operations inutiles | Reprise de pliage mal fait |
| Stocks | En-cours excessifs | Piles de pieces entre postes |
| Mouvements | Gestes inutiles des operateurs | Recherche des pieces dans le tas |
| Defauts | Pieces non conformes | Avions rejetes par le controleur |

### 6.3 Tableau comparatif des rounds (a completer)

| Indicateur | Round 1 | Round 2 | Round 3 | Round 4 |
|------------|---------|---------|---------|---------|
| Lead Time (min) | | | | |
| WIP (pieces) | | | | |
| Taux qualite (%) | | | | |
| Avions livres | | | | |
| Goulot | | | | |

---

## 7. SOLUTIONS ET REPONSES ATTENDUES

### 7.1 Pourquoi le flux pousse est inefficace ?

**Reponse attendue :**

- La production par lots cree des files d'attente entre les postes
- Chaque poste optimise SA performance sans voir le systeme global
- Les defauts sont detectes tard (en fin de ligne)
- Le lead time est long car les pieces attendent dans les stocks intermediaires
- La variabilite d'un poste impacte toute la chaine

### 7.2 Comment le Kanban resout ces problemes ?

**Reponse attendue :**

- Le Kanban limite les en-cours (WIP) a un maximum defini
- La production est declenchee par la demande reelle du poste aval
- Les problemes deviennent visibles immediatement (pas de stock pour les masquer)
- Le lead time diminue car les pieces ne stagnent plus
- L'equilibrage devient necessaire (et visible)

### 7.3 Lien avec les concepts industriels

| Concept jeu | Equivalent industriel |
|-------------|----------------------|
| Lots de 5 | Ordres de fabrication par grandes series |
| Cartes Kanban | Systeme Kanban physique ou electronique |
| Cellule en U | Ilot de production autonome |
| Gabarits de pliage | Outillage, Poka-Yoke |
| Equilibrage | Yamazumi, Takt Time |
| Prime individuelle | Systeme de remuneration a la piece |

---

## 8. TRANSFERT VERS L'ENTREPRISE

### 8.1 Questions de transfert (debriefing final)

1. Dans votre entreprise/stage, identifiez-vous des situations de flux pousse ?
2. Ou sont les stocks intermediaires dans votre atelier ?
3. Quels gaspillages avez-vous observes recemment ?
4. Comment pourriez-vous appliquer le Kanban dans votre contexte ?
5. Quels indicateurs mesurez-vous actuellement ?

### 8.2 Plan d'action individuel

Demander a chaque participant de completer :

| Question | Reponse |
|----------|---------|
| Un gaspillage que j'ai identifie dans mon entreprise | |
| Une action d'amelioration que je peux proposer | |
| L'indicateur que je vais suivre | |
| La date a laquelle je vais agir | |

### 8.3 Ressources complementaires

- Livres : "Le But" de Eliyahu Goldratt, "Lean Thinking" de Womack et Jones
- Videos : Chaine YouTube "Gemba Academy"
- Outils : Application "Kanban Tool", logiciel de simulation FlexSim

---

## ANNEXES

### Annexe A : Modele d'avion recommande

Utiliser le modele "Dart" classique :

1. Pli central longitudinal
2. Plis des coins superieurs vers le centre
3. Plis des bords vers le centre (ailes)
4. Pli des ailes vers le bas
5. Ajustement final des ailes

### Annexe B : Criteres de qualite (pour le controleur)

Un avion est conforme si :

- [ ] Le pli central est bien marque et symetrique
- [ ] Les deux ailes sont de longueur egale (tolerance 5mm)
- [ ] Le nez est pointu et non ecrase
- [ ] L'avion peut planer sur au moins 3 metres
- [ ] Aucune dechirure visible

### Annexe C : Codes couleur des commandes

| Couleur | Type de commande | Priorite |
|---------|------------------|----------|
| Blanc | Commande standard | Normale |
| Jaune | Commande urgente | Haute |
| Bleu | Commande export | Speciale |

---

**Document cree par Pole Formation UIMM-CVDL**  
**Version 1.0 - Fevrier 2026**
