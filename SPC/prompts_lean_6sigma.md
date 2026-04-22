# Focus LEAN / 6 Sigma : Résolution de Problèmes assistée par l'IA (Spécial Maintenance)

Ce document présente 6 approches méthodologiques phares de la qualité et de l'amélioration continue, appliquées aux métiers de la maintenance industrielle. Pour chaque méthode, vous trouverez un "prompt" (requête) prêt à être copié-collé dans une IA générative (comme ChatGPT, Claude ou Gemini) ainsi qu'un cas d'usage concret tiré de problématiques d'exploitation et de fiabilité.

---

## 1. Méthode QQOQCP (Qui, Quoi, Où, Quand, Comment, Combien, Pourquoi)

**Objectif :** Poser le problème, clarifier la situation initiale (contexte équipement, fréquence, impact) et délimiter le périmètre avant de chercher des solutions.

### 📋 Prompt générique à copier-coller

```text
Tu es un consultant en maintenance et ingénierie de fiabilité, spécialisé en diagnostic, animé par le besoin de clarifier les zones d'ombre pour cibler précisément l'investigation technique.
Voici une situation à analyser : [décris la situation]. Réponds aux 7 questions QQOQCP (Qui, Quoi, Où, Quand, Comment, Combien, Pourquoi) de façon structurée pour m'aider à poser un diagnostic clair et proposer un plan d'action d'inspection.
```

### 🏭 Exemple d'application : Maintenance

* **L'anomalie (à insérer) :**  Dérives thermiques inexpliquées sur un four de traitement.
* **Le prompt prêt à l'emploi :**

```text
Tu es un consultant en maintenance et ingénierie de fiabilité, spécialisé en diagnostic, animé par le besoin de clarifier les zones d'ombre pour cibler précisément l'investigation technique.
Voici une situation à analyser : Depuis le début du trimestre, nous constatons des dérives de température inexpliquées (+/- 5°C par rapport à la consigne) sur le four de traitement thermique n°2, ce qui déclenche régulièrement de fausses alarmes de sécurité pendant les week-ends sans supervision.
Réponds aux 7 questions QQOQCP (Qui, Quoi, Où, Quand, Comment, Combien, Pourquoi) de façon structurée pour m'aider à poser un diagnostic clair et proposer un plan d'action d'inspection.
```

---

## 2. Les 5 Pourquoi

**Objectif :** Dépasser les symptômes (la simple panne) et remonter l'enchaînement logique jusqu'à trouver la cause racine technique, humaine ou organisationnelle.

### 📋 Prompt générique à copier-coller

```text
Tu es un expert en maintenance industrielle et résolution de problèmes racine, passionné par la compréhension profonde des pannes pour éviter le simple changement de pièce ("re-panne").
Voici un problème technique sur mon parc machine : [décris le problème ou la panne].
Pose-moi cinq fois la question "Pourquoi ?", de manière logique (arbre des défaillances), pour m'aider à remonter jusqu'à la cause fondamentale. 
Propose une synthèse finale de la cause identifiée.
```

### 🏭 Exemple d'application : Maintenance

* **L'anomalie (à insérer) :** Rupture prématurée d'un roulement sur une pompe.
* **Le prompt prêt à l'emploi :**

```text
Tu es un expert en maintenance industrielle et résolution de problèmes racine, passionné par la compréhension profonde des pannes pour éviter le simple changement de pièce ("re-panne").
Voici un problème technique sur mon parc machine : Lors de l'inspection vibratoire mensuelle, le technicien a diagnostiqué une usure sévère d'un roulement côté accouplement sur la pompe de circulation d'eau glacée, alors que celui-ci avait été remplacé en préventif il y a seulement 3 mois (sa durée de vie moyenne théorique est de 5 ans).
Pose-moi cinq fois la question "Pourquoi ?", de manière logique (arbre des défaillances), pour m'aider à remonter jusqu'à la cause fondamentale. 
Propose une synthèse finale de la cause identifiée.
```

---

## 3. Arbre des causes

**Objectif :** Modéliser graphiquement tous les faits contributifs ayant amené à une défaillance grave afin d'agir sur l'ensemble de la combinaison d'événements.

### 📋 Prompt générique à copier-coller

```text
Tu es un ingénieur méthode maintenance et spécialiste en sûreté de fonctionnement utilisant l'approche Arbre des causes.
Problème ou incident : [décrivez la panne ou l'événement redouté].
1. Reformule les faits de façon factuelle (pas d'hypothèse).
2. Construit l'arbre en remontant des faits probants vers les causes initiales.
3. Pour chaque branche, identifie les conditions contributives (organisation, technique, erreur de manipulation).
4. Présente le tout sous forme d'arbre textuel utilisant des puces hiérarchisées.
5. Conclus par 2 ou 3 pistes d'actions correctives durables à ajouter au plan de maintenance.
```

### 🏭 Exemple d'application : Maintenance

* **L'anomalie (à insérer) :** Incendie mineur dans une armoire basse tension.
* **Le prompt prêt à l'emploi :**

```text
Tu es un ingénieur méthode maintenance et spécialiste en sûreté de fonctionnement utilisant l'approche Arbre des causes.
Problème ou incident : Cette nuit, un départ d'incendie a eu lieu dans l'armoire électrique TGBT du local compresseurs. Cela a provoqué le déclenchement des extincteurs automatiques et causé l'arrêt complet des installations d'air comprimé de l'usine.
1. Reformule les faits de façon factuelle (pas d'hypothèse).
2. Construit l'arbre en remontant des faits probants vers les causes initiales.
3. Pour chaque branche, identifie les conditions contributives (organisation, technique, erreur de manipulation).
4. Présente le tout sous forme d'arbre textuel utilisant des puces hiérarchisées.
5. Conclus par 2 ou 3 pistes d'actions correctives durables à ajouter au plan de maintenance.
```

---

## 4. Diagramme d'Ishikawa (ou 5M)

**Objectif :** Structurer un brainstorming technique lorsqu'une dérive de performance maintenance est observée (qualité de réparation, délai de remise en état, fréquence de panne).

### 📋 Prompt générique à copier-coller

```text
Tu es un manager méthode/fiabilité, expert en analyse de performance opérationnelle et adepte des diagrammes d'Ishikawa.
Voici la problématique ou la dérive constatée en maintenance : [décrivez la problématique]. 
Classe les causes potentielles en catégories 5M (Méthodes, Matériel, Main-d'œuvre, Milieu, Matière/Pièces de rechange) et dresse un schéma textuel Ishikawa de ce problème.
Termine en m'indiquant sur laquelle de ces familles il serait le plus pertinent d'axer le diagnostic initial prioritaires.
```

### 🏭 Exemple d'application : Maintenance

* **L'anomalie (à insérer) :** Allongement du MTTR (Temps Moyen de Réparation).
* **Le prompt prêt à l'emploi :**

```text
Tu es un manager méthode/fiabilité, expert en analyse de performance opérationnelle et adepte des diagrammes d'Ishikawa.
Voici la problématique ou la dérive constatée en maintenance : Lors du bilan GMAO du dernier trimestre, nous avons observé une dégradation (augmentation) de notre indicateur MTTR (Temps Moyen de Réparation) de 25 % spécifiquement sur les interventions curatives du parc de convoyeurs de la zone d'expédition.
Classe les causes potentielles en catégories 5M (Méthodes, Matériel, Main-d'œuvre, Milieu, Matière/Pièces de rechange) et dresse un schéma textuel Ishikawa de ce problème.
Termine en m'indiquant sur laquelle de ces familles il serait le plus pertinent d'axer le diagnostic initial prioritaires.
```

---

## 5. AMDEC (Moyen de Production)

**Objectif :** Outil central de la maintenance, il permet de baser son plan de maintenance préventive et conditionnelle sur une véritable analyse des risques technologiques (AMDEC Machine).

### 📋 Prompt générique à copier-coller

```text
Tu es un ingénieur Méthodes Maintenance spécialisé en AMDEC Moyen de Production.
Je dois bâtir ou optimiser le plan de maintenance pour ce système : [décris l'équipement].
Identifie ses 5 principaux sous-ensembles, liste pour chacun les modes de défaillance pertinents, leurs effets et causes probables.
Puis propose-moi un plan d'actions basé sur l'Inspection (Visuel, Vibratoire, Thermographie, etc.), le Préventif Systématique (lubrification, échange standard) ou la modification de design, en fonction de la criticité supposée de la défaillance.
```

### 🏭 Exemple d'application : Maintenance

* **L'équipement (à insérer) :** Nouvelle centrale de cogénération biomasse.
* **Le prompt prêt à l'emploi :**

```text
Tu es un  technicien Méthodes Maintenance spécialisé en AMDEC Moyen de Production.
Je dois bâtir ou optimiser le plan de maintenance pour ce système : Une nouvelle centrale de cogénération biomasse intégrant un silo d'alimentation, une chaudière à grille mobile, un traitement de fumées et une turbine vapeur couplée à un alternateur.
Identifie ses 5 principaux sous-ensembles, liste pour chacun les modes de défaillance pertinents, leurs effets et causes probables.
Puis propose-moi un plan d'actions basé sur l'Inspection (Visuel, Vibratoire, Thermographie, etc.), le Préventif Systématique (lubrification, échange standard) ou la modification de design, en fonction de la criticité supposée de la défaillance.
```

---

## 6. Méthode 8D (8 Do)

**Objectif :** Résoudre un incident technique majeur, engageant souvent la sécurité ou arrêtant très longuement de la production, à travers un suivi collaboratif en 8 étapes pour sécuriser les installations.

### 📋 Prompt générique à copier-coller

```text
Tu es un référent technique LEAN Maintenance expert en animation de la démarche 8D pour des pannes critiques.
Voici l'incident majeur que nous devons sécuriser et résoudre : [décris la panne critique].
Guide-moi de manière pratique à travers les 8 étapes du 8D orienté maintenance. Assure-toi de mettre en évidence l'étape des actions de sécurisation immédiates (D3) et la définition d'actions préventives durables (intégration dans la GMAO en D6/D7).
Donne pour chaque étape ce que nous devons livrer et formaliser concrètement.
```

### 🏭 Exemple d'application : Maintenance

* **L'incident (à insérer) :** Casse critique de capteurs arrêtant des centres d'usinage grande vitesse.
* **Le prompt prêt à l'emploi :**

```text
Tu es un référent technique LEAN Maintenance expert en animation de la démarche 8D pour des pannes critiques.
Voici l'incident majeur que nous devons sécuriser et résoudre : Sur nos centres d'usinage grande vitesse (UGV), nous subissons depuis le début de l'année une série de défaillances inattendues des capteurs de vibration intégrés aux broches (pertes de signal ou câbles sectionnés), ce qui a provoqué ce mois-ci trois crashs machine car la sécurité anti-collision n'a pas pu s'activer à temps.
Guide-moi de manière pratique à travers les 8 étapes du 8D orienté maintenance. Assure-toi de mettre en évidence l'étape des actions de sécurisation immédiates (D3) et la définition d'actions préventives durables (intégration dans la GMAO en D6/D7).
Donne pour chaque étape ce que nous devons livrer et formaliser concrètement.
```
