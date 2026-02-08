![Logo UIMM](../logo_uimm.jpg)

# Pole Formation UIMM-CVDL

---

# LE BEER GAME - GUIDE FORMATEUR

## Simulation de Chaine d'Approvisionnement

**Duree totale** : 4 heures
**Nombre de participants** : 8 a 16 personnes (equipes de 4)
**Materiel necessaire** : Jetons ou pieces, fiches de commande, tableaux de suivi, calculatrices

---

## TABLE DES MATIERES

1. [Objectifs pedagogiques](#objectifs-pedagogiques)
2. [Contexte et histoire](#contexte-et-histoire)
3. [Preparation de la salle](#preparation-de-la-salle)
4. [Regles du jeu](#regles-du-jeu)
5. [Deroulement detaille](#deroulement-detaille)
6. [Animation et observation](#animation-et-observation)
7. [Debriefing et analyse](#debriefing-et-analyse)
8. [Transfert vers l&#39;entreprise](#transfert-vers-lentreprise)

---

## 1. OBJECTIFS PEDAGOGIQUES

A l'issue de cette simulation, les participants seront capables de :

- **Comprendre** l'effet coup de fouet (Bullwhip Effect) et ses causes
- **Identifier** l'impact des delais d'information sur la chaine d'approvisionnement
- **Analyser** les comportements systemiques dans une organisation complexe
- **Mesurer** les couts de stockage et de rupture
- **Proposer** des solutions pour ameliorer la coordination (VMI, EDI, CPFR)
- **Distinguer** les decisions locales des decisions systemiques

---

## 2. CONTEXTE ET HISTOIRE

### 2.1 Origine du jeu

Le Beer Game (Jeu de la Biere) a ete cree au MIT Sloan School of Management dans les annees 1960 par Jay Forrester. Il illustre les concepts de la dynamique des systemes et a ete popularise par Peter Senge dans "La Cinquieme Discipline".

### 2.2 Scenario du jeu

Une brasserie fabrique et distribue de la biere a travers une chaine logistique a 4 niveaux :

- **Usine** : Produit la biere
- **Distributeur** : Stocke et distribue à grande echelle
- **Grossiste** : Approvisionne les détaillants regionaux
- **Detaillant** : Vend au consommateur final

Un phenomene mysterieux va perturber la demande du consommateur final (publicite, evenement sportif, meteo...) et les joueurs devront reagir.

---

## 3. PREPARATION DE LA SALLE

### 3.1 Disposition des postes

```
+============================================+
|                                            |
|   [USINE]                                  |
|     |                                      |
|     | (Delai 2 semaines)                   |
|     v                                      |
|   [DISTRIBUTEUR]                           |
|     |                                      |
|     | (Delai 2 semaines)                   |
|     v                                      |
|   [GROSSISTE]                              |
|     |                                      |
|     | (Delai 2 semaines)                   |
|     v                                      |
|   [DETAILLANT]                             |
|     |                                      |
|     v                                      |
|   [CONSOMMATEUR] (jeu par le formateur)    |
|                                            |
+============================================+
```

### 3.2 Materiel par poste

| Element                        | Quantite par poste | Total (4 postes) |
| ------------------------------ | ------------------ | ---------------- |
| Jetons (caisses de biere)      | 50                 | 200              |
| Fiche de decisions             | 1                  | 4                |
| Tableau de suivi (40 semaines) | 1                  | 4                |
| Stylo                          | 1                  | 4                |
| Calculatrice                   | 1                  | 4                |
| Bons de commande (pile)        | 40                 | 160              |
| Bons de livraison (pile)       | 40                 | 160              |

### 3.3 Configuration initiale

**Pour CHAQUE poste :**

- Stock initial : 12 caisses
- Commandes en transit : 4 caisses (2 dans chaque zone de delai)
- Arrieres de commandes : 0

### 3.4 Zones de delai

Entre chaque poste, prevoir 2 zones physiques :

- Zone "Semaine 1" (commande passee, en attente)
- Zone "Semaine 2" (commande recue, en livraison)

```
[POSTE A] --> [DELAI S1] --> [DELAI S2] --> [POSTE B]
              (commande)     (livraison)
```

---

## 4. REGLES DU JEU

### 4.1 Objectif

**Minimiser les couts totaux de la chaine d'approvisionnement** sur 40 semaines.

### 4.2 Couts

| Type de cout | Montant                               | Explication                                 |
| ------------ | ------------------------------------- | ------------------------------------------- |
| Stockage     | 0,50 EUR / caisse / semaine           | Chaque caisse en stock coute                |
| Rupture      | 1,00 EUR / caisse manquante / semaine | Chaque commande non honoree coute le double |

### 4.3 Sequence d'un tour (1 semaine)

**Chaque semaine, chaque joueur effectue dans l'ordre :**

1. **Recevoir les livraisons** : Prendre les caisses de la zone "Delai S2" et les ajouter au stock
2. **Recevoir les commandes** : Lire la commande client (bon de commande) sans la montrer aux autres
3. **Livrer** : Expedier les caisses demandees (ou ce qui est disponible) vers la zone "Delai S1" du client
4. **Enregistrer les arrieres** : Noter les commandes non satisfaites
5. **Passer commande** : Decider et ecrire la quantite commandee au fournisseur
6. **Avancer les delais** : Deplacer les jetons/bons d'une zone de delai a la suivante
7. **Calculer les couts** : (Stock x 0,50) + (Arrieres x 1,00)

### 4.4 Regles strictes

- **PAS DE COMMUNICATION** entre les postes (sauf bons de commande officiels)
- Le consommateur est joue par le formateur (demande predeterminee)
- On ne peut pas annuler une commande passee
- Les arrieres s'accumulent d'une semaine a l'autre
- L'usine n'a pas de limite de production (mais delai de 2 semaines)

---

## 5. DEROULEMENT DETAILLE

### 5.1 Planning de la session

| Horaire | Phase                   | Duree  | Contenu                             |
| ------- | ----------------------- | ------ | ----------------------------------- |
| 0:00    | Introduction            | 30 min | Contexte, regles, attribution roles |
| 0:30    | Phase de jeu (S1-S20)   | 60 min | Premieres 20 semaines               |
| 1:30    | Pause/Premiers constats | 15 min | Reactions a chaud                   |
| 1:45    | Phase de jeu (S21-S40)  | 45 min | 20 dernieres semaines               |
| 2:30    | Compilation resultats   | 20 min | Graphiques, calcul couts            |
| 2:50    | **PAUSE**         | 15 min | -                                   |
| 3:05    | Debriefing              | 40 min | Analyse effet coup de fouet         |
| 3:45    | Transfert               | 15 min | Solutions industrielles             |
| 4:00    | **FIN**           | -      | -                                   |

### 5.2 Demande du consommateur (a lire par le formateur)

**CONFIDENTIEL - NE PAS MONTRER AUX PARTICIPANTS**

| Semaine | Demande (caisses) | Observation                 |
| ------- | ----------------- | --------------------------- |
| 1-4     | 4                 | Demande stable              |
| 5       | 8                 | Doublement soudain          |
| 6-40    | 8                 | Demande stable mais doublee |

**Explication cachee** : Une publicite televisee a double la demande a partir de la semaine 5. La demande se stabilise ensuite a 8 caisses par semaine.

### 5.3 Script formateur - Introduction

> "Bienvenue dans la simulation Beer Game. Vous dirigez une chaine d'approvisionnement de biere. Chacun de vous va gerer un niveau de cette chaine : le detaillant, le grossiste, le distributeur ou l'usine.
>
> Votre objectif commun est de minimiser les couts totaux. Attention, vous ne pouvez PAS communiquer entre vous, sauf par les bons de commande officiels. Vous allez jouer 40 semaines de simulation.
>
> Le consommateur final, que je joue, va vous envoyer ses commandes. A vous de gerer vos stocks et vos approvisionnements au mieux."

### 5.4 Script formateur - A la semaine 5

> "(Ne rien annoncer de special. Simplement envoyer une commande de 8 caisses au detaillant au lieu de 4. Observer les reactions.)"

---

## 6. ANIMATION ET OBSERVATION

### 6.1 Points a observer

- [ ] Premiere reaction du detaillant a la semaine 5-6
- [ ] Propagation de la "panique" vers l'amont
- [ ] Pic de commandes vers l'usine (quand ? amplitude ?)
- [ ] Apparition massive de stocks a partir de la semaine 20-25
- [ ] Frustration des joueurs face au systeme
- [ ] Accusations mutuelles ("c'est de leur faute")

### 6.2 Pieges typiques des joueurs

| Piege              | Description                                 | Semaine typique |
| ------------------ | ------------------------------------------- | --------------- |
| Surreaction        | Commander beaucoup plus que necessaire      | S6-S10          |
| Effet de panique   | Doubler les commandes car "ca n'arrive pas" | S8-S15          |
| Annulation mentale | Vouloir annuler les commandes passees       | S15-S25         |
| Blame des autres   | "L'usine ne livre pas assez vite"           | S10-S20         |
| Resignation        | "De toute facon, on ne peut rien faire"     | S25-S40         |

### 6.3 Interventions du formateur

**A NE PAS FAIRE :**

- Donner des conseils pendant le jeu
- Reveler la demande future
- Permettre la communication entre postes

**A FAIRE :**

- Rappeler les regles si necessaire
- Noter les comportements observes
- Chronometrer les decisions
- Preparer les graphiques en temps reel si possible

---

## 7. DEBRIEFING ET ANALYSE

### 7.1 Phase emotionnelle (10 min)

**Questions a poser :**

1. Comment vous etes-vous senti pendant le jeu ?
2. A quel moment avez-vous ete le plus frustre ?
3. De qui pensiez-vous que c'etait la faute ?
4. Avez-vous eu l'impression de bien gerer votre poste ?

**Reponses typiques attendues :**

- "J'etais noye sous les commandes"
- "L'usine ne produisait pas assez vite"
- "Le grossiste commandait n'importe quoi"
- "On aurait du pouvoir communiquer"

### 7.2 Phase factuelle - L'effet coup de fouet (15 min)

**Afficher les graphiques de commandes :**

```
Commandes par semaine

     |
 100 |                    *
     |                   * *
  80 |                  *   *
     |                 *     *
  60 |                *       *
     |               *         *
  40 |              *           *
     |             *             *
  20 |   * * * * *                 * * * *
     |  
   0 +---------------------------------> Semaines
       1  5  10  15  20  25  30  35  40

Legende:
--- Detaillant (demande reelle : 4 puis 8)
... Grossiste (amplification)
-.- Distributeur (amplification++)
*** Usine (amplification maximale)
```

**Points cles a faire ressortir :**

1. La demande reelle n'a augmente que de 4 a 8 (+100%)
2. Les commandes a l'usine ont pu atteindre 50-100 (+500% a +1000%)
3. C'est la STRUCTURE du systeme qui cree l'amplification, pas les individus

### 7.3 Phase analytique - Causes du Bullwhip Effect (10 min)

| Cause                | Explication                            | Solution               |
| -------------------- | -------------------------------------- | ---------------------- |
| Delais d'information | 2 semaines entre commande et livraison | Reduire les lead times |
| Batching             | Tendance a commander par gros lots     | Flux continu           |
| Anticipation         | "Je commande plus car ca va manquer"   | Partage d'information  |
| Promotions           | Variation artificielle de demande      | EDLP (prix stable)     |
| Isolement            | Chaque maillon ne voit que son voisin  | VMI, CPFR              |

### 7.4 Revele final

> "La demande du consommateur final n'a fait que doubler une seule fois, de 4 a 8 caisses, a la semaine 5. Depuis, elle est STABLE a 8 caisses. Pourtant, vous avez tous vecu un chaos incroyable. Pourquoi ?"

---

## 8. TRANSFERT VERS L'ENTREPRISE

### 8.1 Solutions industrielles

| Solution                                    | Description                            | Exemple                       |
| ------------------------------------------- | -------------------------------------- | ----------------------------- |
| **VMI** (Vendor Managed Inventory)    | Le fournisseur gere le stock du client | Procter & Gamble avec Walmart |
| **EDI** (Echange Donnees Informatise) | Partage electronique des donnees       | Commandes automatiques        |
| **CPFR** (Collaborative Planning)     | Planification collaborative            | Previsions partagees          |
| **Reduction des delais**              | Lead times plus courts                 | Livraison J+1                 |
| **Cross-docking**                     | Pas de stockage intermediaire          | Flux direct usine-magasin     |

### 8.2 Questions de transfert

1. Dans votre entreprise, combien de niveaux a la chaine d'approvisionnement ?
2. Quel est le delai entre une commande et sa livraison ?
3. Partagez-vous vos previsions avec vos fournisseurs ?
4. Avez-vous deja observe des "coups de fouet" sur certains produits ?

### 8.3 Synthese des apprentissages

> "Le Beer Game nous apprend que dans un systeme complexe, les problemes ne viennent pas des individus mais de la STRUCTURE. Meme des personnes intelligentes et bien intentionnees peuvent creer un chaos total si le systeme dans lequel elles operent n'est pas concu pour la collaboration et la transparence."

---

## ANNEXES

### Annexe A : Fiche de decisions vierge

A photocopier pour chaque joueur (voir Livret Stagiaire).

### Annexe B : Tableau recapitulatif des couts

| Poste                  | Stock total (cumule) | Arrieres total (cumule) | Cout stockage | Cout rupture | TOTAL |
| ---------------------- | -------------------- | ----------------------- | ------------- | ------------ | ----- |
| Detaillant             |                      |                         |               |              |       |
| Grossiste              |                      |                         |               |              |       |
| Distributeur           |                      |                         |               |              |       |
| Usine                  |                      |                         |               |              |       |
| **TOTAL CHAINE** |                      |                         |               |              |       |

### Annexe C : Resultats types

**Parties typiques (40 semaines) :**

- Cout total chaine sans strategie : 2000-4000 EUR
- Cout optimal theorique : ~800 EUR
- Pic de commandes usine : 40-100 caisses (vs demande reelle de 8)
- Pic de stock : 60-150 caisses par poste

---

**Document cree par Pole Formation UIMM-CVDL**
**Version 1.0 - Fevrier 2026**
