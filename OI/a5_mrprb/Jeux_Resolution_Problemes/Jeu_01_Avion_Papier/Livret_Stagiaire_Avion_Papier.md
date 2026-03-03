![Logo UIMM](../logo_uimm.jpg)

# Pole Formation UIMM-CVDL

---

# JEU DE L'AVION EN PAPIER - LIVRET STAGIAIRE

## Simulation Lean Manufacturing

**Duree** : 4 heures  
**Votre role** : Membre de l'equipe de production

---

## PRESENTATION

Bienvenue dans cette simulation de production industrielle. Vous allez integrer une usine de fabrication d'avions en papier et vivre concretement les principes du Lean Manufacturing.

Au cours de 4 rounds successifs, vous allez experimenter differentes organisations de production et observer leurs impacts sur la performance de l'entreprise.

**L'objectif** : Satisfaire le client en livrant des avions conformes, dans les meilleurs delais et au moindre cout.

---

## VOTRE POSTE

### Nom : _________________________________

### Role attribue : _________________________________

Cochez votre role :

- [ ] Operateur Poste 1 - Pliage de base
- [ ] Operateur Poste 2 - Pliage des ailes
- [ ] Operateur Poste 3 - Pliage final
- [ ] Operateur Poste 4 - Finition
- [ ] Controleur Qualite
- [ ] Manutentionnaire
- [ ] Chronometreur
- [ ] Observateur
- [ ] Manager de Production
- [ ] Client

---

## FICHE DE POSTE - OPERATEUR

### Instructions de pliage

**Poste 1 - Pliage de base**

1. Prendre une feuille A4
2. Plier la feuille en deux dans le sens de la longueur
3. Bien marquer le pli central
4. Deposer la piece dans la zone "Sortie"

**Poste 2 - Pliage des ailes**

1. Prendre une piece du poste 1
2. Plier les deux coins superieurs vers le pli central
3. Bien marquer les plis
4. Deposer la piece dans la zone "Sortie"

**Poste 3 - Pliage final**

1. Prendre une piece du poste 2
2. Plier les bords exterieurs vers le pli central
3. Former la pointe de l'avion
4. Deposer la piece dans la zone "Sortie"

**Poste 4 - Finition**

1. Prendre une piece du poste 3
2. Plier les ailes vers le bas symetriquement
3. Ajuster la symetrie de l'avion
4. Deposer la piece dans la zone "Sortie"

---

## FICHE DE POSTE - CONTROLEUR QUALITE

### Criteres de conformite

Un avion est **CONFORME** si TOUS les criteres sont respectes :

| Critere | Verification |
|---------|--------------|
| Pli central | Bien marque, symetrique |
| Ailes | Longueur egale (tolerance 5mm) |
| Nez | Pointu, non ecrase |
| Vol | Plane sur minimum 3 metres |
| Aspect | Aucune dechirure visible |

### Actions

- **Avion CONFORME** : Passer au Client
- **Avion NON CONFORME** : Placer dans la zone "Rebuts"

### Tableau de suivi qualite

| Round | Avions controles | Conformes | Rebuts | Taux (%) |
|-------|------------------|-----------|--------|----------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |

---

## FICHE DE POSTE - MANUTENTIONNAIRE

### Regles de transfert

**Round 1** : Transferer les pieces par lots de 5

**Round 2** : Transferer uniquement sur presentation d'une carte Kanban

**Round 3** : Transferer piece par piece

**Round 4** : Poste supprime (flux direct)

### Schema de circulation

```
Poste 1 --> Poste 2 --> Poste 3 --> Poste 4 --> Controle --> Client
```

---

## FICHE DE POSTE - CHRONOMETREUR

### Mesures a effectuer

**Lead Time** (temps de traversee)

- Demarrer le chrono quand la feuille entre au Poste 1
- Arreter quand l'avion est livre au Client
- Noter le temps

**Temps de cycle par poste**

- Temps entre deux pieces terminees au meme poste

### Tableau de mesures

| Round | 1er avion livre (Lead Time) | Temps cycle P1 | Temps cycle P2 | Temps cycle P3 | Temps cycle P4 |
|-------|------------------------------|----------------|----------------|----------------|----------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |

---

## FICHE DE POSTE - OBSERVATEUR MUDA

### Les 7 gaspillages a identifier

| Muda | Definition | Round 1 | Round 2 | Round 3 | Round 4 |
|------|------------|---------|---------|---------|---------|
| Surproduction | Produire plus que la demande | | | | |
| Attentes | Temps mort sans travail | | | | |
| Transports | Deplacements inutiles | | | | |
| Surprocessing | Operations superflues | | | | |
| Stocks | En-cours excessifs | | | | |
| Mouvements | Gestes inutiles | | | | |
| Defauts | Pieces non conformes | | | | |

### Notez vos observations

_______________________________________________
_______________________________________________
_______________________________________________

---

## TABLEAU DE BORD - RESULTATS

### Indicateurs de performance (KPI)

| Indicateur | Round 1 | Round 2 | Round 3 | Round 4 |
|------------|---------|---------|---------|---------|
| Lead Time (temps 1er avion) | | | | |
| WIP (en-cours en fin de round) | | | | |
| Avions livres au client | | | | |
| Avions rejetes (rebuts) | | | | |
| Taux de qualite (%) | | | | |

### Formules de calcul

**Taux de qualite** = (Avions conformes / Total produit) x 100

**Evolution Lead Time** = ((LT Round 4 - LT Round 1) / LT Round 1) x 100

---

## REGLES PAR ROUND

### ROUND 1 - FLUX POUSSE

**Regles :**

- Production par lots de 5 pieces
- Pas de communication entre postes
- Chaque operateur est evalue sur SA production personnelle
- Stocks illimites entre les postes

**Votre objectif** : Produire le maximum de pieces

---

### ROUND 2 - SYSTEME KANBAN

**Nouvelles regles :**

- Systeme de cartes Kanban
- Production uniquement sur reception d'une carte du poste aval
- Maximum 2 pieces en stock entre chaque poste
- Communication visuelle autorisee

**Votre objectif** : Respecter les cartes Kanban

---

### ROUND 3 - EQUILIBRAGE

**Nouvelles regles :**

- Analyse des temps de cycle
- Redistribution des taches si necessaire
- Utilisation des gabarits de pliage
- Travail d'equipe encourage

**Votre objectif** : Equilibrer la ligne

---

### ROUND 4 - FLUX PIECE A PIECE

**Nouvelles regles :**

- Cellule en U
- Transfert immediat apres chaque operation
- Polyvalence entre operateurs
- Plus de manutentionnaire

**Votre objectif** : Maximiser le flux

---

## SYNTHESE PERSONNELLE

### Ce que j'ai appris aujourd'hui

1. _______________________________________________

2. _______________________________________________

3. _______________________________________________

### Liens avec mon entreprise/stage

**Un gaspillage que j'ai identifie :**
_______________________________________________

**Une action d'amelioration que je peux proposer :**
_______________________________________________

**L'indicateur que je vais suivre :**
_______________________________________________

---

## LEXIQUE

| Terme | Definition |
|-------|------------|
| **Lead Time** | Temps de traversee, du debut a la fin du processus |
| **WIP** | Work In Process, pieces en cours de fabrication |
| **Kanban** | Systeme de cartes pour tirer la production |
| **Muda** | Gaspillage en japonais |
| **Takt Time** | Rythme de production aligne sur la demande client |
| **Kaizen** | Amelioration continue par petits pas |
| **Flux pousse** | Production basee sur des previsions |
| **Flux tire** | Production declenchee par la demande reelle |

---

**Document Pole Formation UIMM-CVDL**
