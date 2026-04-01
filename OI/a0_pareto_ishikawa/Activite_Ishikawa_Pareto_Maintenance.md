![Logo UIMM](../../logo_uimm_placeholder.jpg)

# Activité Pratique : Méthodes de Résolution de Problèmes en Maintenance Industrielle

## Objectifs Pédagogiques
- Mettre en œuvre le diagramme d'Ishikawa (5M) pour analyser les causes d'un problème technique.
- S'appuyer sur l'expérience terrain pour identifier et structurer les causes racines.
- Utiliser un tableur (Excel) pour construire un diagramme de Pareto et prioriser les actions de maintenance.
- Proposer un plan d'action pertinent basé sur l'analyse des données.

## Contexte Industriel
Vous faites partie de l'équipe de maintenance d'un site de production. Depuis plusieurs semaines, la ligne de conditionnement automatique (Ligne 4) subit des micros-arrêts fréquents et des pannes récurrentes. Ces dysfonctionnements font chuter le TRS (Taux de Rendement Synthétique) de manière inquiétante et la production prend du retard.

Plutôt que d'intervenir "à l'aveuglette" ou dans l'urgence, le responsable technique vous demande de réunir vos expériences respectives pour identifier l'origine de ces problèmes, puis d'analyser les données de la GMAO pour prioriser vos prochaines interventions.

---

## PARTIE 1 : Brainstorming et Diagramme d'Ishikawa (En groupe)

*Durée conseillée : 45 minutes*

### 1. Dégager les pistes (Tempête de cerveaux)
L'effet constaté (le problème) est : **« Pannes et arrêts fréquents de la ligne de conditionnement 4 »**.

En vous basant sur votre **expérience terrain de technicien de maintenance**, listez sur un brouillon (ou post-it) toutes les causes possibles pouvant conduire à ce type de problème sur une installation industrielle continue.
*Exemples : usure prématurée d'un composant, capteur sale, mauvais réglage, pièce de rechange défectueuse, etc.*

### 2. Construction de l'Ishikawa (5M)
Classez ensuite ces causes dans un diagramme d'Ishikawa (arêtes de poisson) selon les 5 familles (5M) :
- **Matériel** (Machines, outils, équipements...)
- **Méthode** (Modes opératoires, gammes de maintenance, procédures de changement de format...)
- **Main d'Œuvre** (Compétences, formation, fatigue, communication...)
- **Milieu** (Environnement de travail : poussière, température, vibrations, espace...)
- **Matière** (Pièces de rechange, consommables, qualité du produit conditionné...)

### 3. Restitution et Échange
Chaque groupe présente son diagramme. 
- Discutez des causes trouvées. Avez-vous déjà rencontré ces situations dans vos entreprises respectives ?
- Lesquelles vous semblent, au feeling, les plus probables pour notre ligne 4 ?

---

## PARTIE 2 : Analyse de Pareto et Priorisation (Individuel ou Binôme)

*Durée conseillée : 45 minutes*

Votre brainstorming a permis d'isoler de nombreuses pistes. Entre-temps, vous récupérez un export de la GMAO détaillant la durée totale des arrêts de maintenance (en minutes) constatés sur le dernier mois, classés par famille de pannes (issues de votre réflexion 5M).

### Données de la GMAO (le mois dernier) :

| ID | Description de la cause (Type de panne) | Temps d'arrêt cumulé (min) |
|:--:|:---|:---:|
| A | Encrassement des capteurs optiques de présence | 195 |
| B | Paramètres de chauffe mal réglés au changement de format | 145 |
| C | Usure et rupture de la courroie d'entraînement principal | 80 |
| D | Mauvaise qualité du film d'emballage (déchirures) | 45 |
| E | Composant pneumatique grippé par manque de lubrification | 25 |
| F | Fausse manipulation opérateur sur le pupitre IHM | 20 |
| G | Micro-coupures électriques de l'armoire de commande | 15 |
| H | Desserrage mécanique à cause des vibrations | 10 |

### Travail à réaliser sous Excel :
1. **Saisie des données :** Entrez ce tableau dans un tableur Excel.
2. **Tri :** Triez les données par temps d'arrêt décroissant.
3. **Calculs :** 
   - Calculez le temps d'arrêt total.
   - Ajoutez une colonne pour calculer le pourcentage de chaque cause (%).
   - Ajoutez une colonne pour calculer le pourcentage cumulé.
4. **Graphique :** 
   - Tracez le diagramme de Pareto : un histogramme pour les temps d'arrêt (axe principal) et une courbe pour le pourcentage cumulé (axe secondaire).
5. **Analyse (Loi des 20/80) :** 
   - Quelles sont les causes qui représentent environ 80% du temps d'arrêt total ?
   - Correspondent-elles à votre "feeling" de la Partie 1 ?

---

## PARTIE 3 : Synthèse et Plan d'Action

*Durée conseillée : 30 minutes*

À partir de l'analyse de Pareto, définissez les **3 actions de maintenance prioritaires** à mettre en place rapidement pour faire remonter le TRS de la Ligne 4.

Pour chaque action, précisez :
- De quel ordre est-elle ? (Préventif systématique ? Préventif conditionnel ? Amélioratif ? Formation ?)
- Comment la rattacher au diagramme d'Ishikawa pour montrer que la cause racine est définitivement traitée ?

*Exemple de réflexion : "Si la cause principale est l'encrassement des capteurs (Milieu/Matériel), faut-il modifier le capteur (Amélioratif), changer la fréquence de nettoyage (Méthode/Préventif), ou isoler la zone (Milieu) ?"*
