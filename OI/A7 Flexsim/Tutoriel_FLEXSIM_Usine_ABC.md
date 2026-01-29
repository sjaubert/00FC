# Tutoriel FLEXSIM - Modélisation Usine ABC Emboutissage Ltée

**Pôle Formation UIMM CVDL - Organisation Industrielle**

*Reproduire l'État Initial depuis l'Étude VSM*

---

## 📑 Table des Matières

1. [Introduction et Objectifs](#1-introduction-et-objectifs)
2. [Données de l'Usine ABC](#2-données-de-lusine-abc)
3. [Préparation du Modèle FLEXSIM](#3-préparation-du-modèle-flexsim)
4. [Modélisation des Processus](#4-modélisation-des-processus)
5. [Configuration des Paramètres](#5-configuration-des-paramètres)
6. [Connexions et Flux](#6-connexions-et-flux)
7. [Exécution et Analyse](#7-exécution-et-analyse)
8. [Exercices de Validation](#8-exercices-de-validation)
9. [FAQ et Dépannage](#9-faq-et-dépannage)

---

## 1. Introduction et Objectifs

### 🎯 Objectif du Tutoriel

Ce tutoriel vous guide **pas à pas** dans la création d'un modèle FLEXSIM de l'usine **ABC Emboutissage Ltée**, basé sur les données de l'étude VSM (Value Stream Mapping).

### Ce que vous allez apprendre

- Créer un modèle de simulation de production avec FLEXSIM
- Configurer des processus avec temps de cycle, changements de format et pannes
- Modéliser des stocks intermédiaires entre processus
- Analyser les goulots d'étranglement et le Lead Time
- Valider les résultats par rapport aux calculs VSM

### 📋 Prérequis

- **Logiciel :** FLEXSIM 24.0 ou version ultérieure installé
- **Connaissances :** Notions de base en simulation (interface FLEXSIM)
- **Temps estimé :** 2-3 heures pour la modélisation complète
- **Documents :** Étude VSM ABC Emboutissage (pour référence)

> **💡 Note Pédagogique :** Ce tutoriel se concentre sur la modélisation de l'**état initial** de l'usine (avant améliorations Lean). Cela permet de visualiser les problèmes identifiés dans la VSM et de tester ensuite des scénarios d'amélioration.

---

## 2. Données de l'Usine ABC

### 🏭 Contexte de Production

ABC Emboutissage Ltée fabrique des **supports de tableaux de bord en acier** pour l'industrie automobile. L'usine produit deux variantes :

- **Version Gauche (LH)** : 12 000 pièces/mois (65%)
- **Version Droite (RH)** : 6 400 pièces/mois (35%)

### 📊 Paramètres Globaux

| Paramètre | Valeur |
|-----------|--------|
| **Demande Totale Mensuelle** | 18 400 pièces |
| **Demande Quotidienne** | 920 pièces/jour |
| **Takt Time** | 60 secondes/pièce |
| **Régime de Travail** | 2 × 8h = 16h/jour |
| **Temps Net par Jour** | 920 minutes |
| **Jours Travaillés/Mois** | 20 jours |

### ⚙️ Processus de Production

| Processus | Machine | TC (s) | TCF | Fiabilité | Stock Sortie |
|-----------|---------|--------|-----|-----------|--------------|
| **1. Emboutissage** | Presse 200t automatique | 1 | 1 heure | 85% | 7 000 pièces (4 600 LH + 2 400 RH) |
| **2. Soudage I** | Manuel (1 opérateur) | 39 | 10 min | 100% | 1 700 pièces (1 100 LH + 600 RH) |
| **3. Soudage II** | Manuel (1 opérateur) | 46 | 10 min | 80% | 2 450 pièces (1 600 LH + 850 RH) |
| **4. Montage I** ⚠️ | Manuel (1 opérateur) | **62 (GOULOT)** | - | 100% | 1 840 pièces (1 200 LH + 640 RH) |
| **5. Montage II** | Manuel (1 opérateur) | 40 | - | 100% | 4 140 pièces (2 700 LH + 1 440 RH) |

> **⚠️ Point Critique :** Le **Montage I** a un temps de cycle de **62 secondes**, ce qui est supérieur au Takt Time de **60 secondes**. C'est le **goulot d'étranglement** qui limite la capacité de toute la chaîne de production !

### 📦 Approvisionnement

- **Fournisseur :** Aciers Ultra Ltée
- **Livraisons :** Mardis et Jeudis (2×/semaine)
- **Stock matière première :** 5 jours de rouleaux d'acier

---

## 3. Préparation du Modèle FLEXSIM

### Étape 1 : Créer un Nouveau Modèle

1. Lancez **FLEXSIM 24.0**
2. Cliquez sur **File → New Model**
3. Enregistrez immédiatement : **File → Save As...**
   - Nom : `ABC_Emboutissage_Etat_Initial.fsm`
   - Emplacement : dans votre dossier de travail

### Étape 2 : Configurer les Paramètres Globaux

1. Allez dans **Tools → Global Preferences**
2. Onglet **Units** :
   - Time Units : **Seconds**
   - Distance Units : **Meters**
3. Configurez les paramètres de simulation :
   - Menu : **Model → Properties**
   - Warmup Time : **0** secondes
   - Run Time : **1728000** secondes (20 jours × 16h × 3600)

> **💡 Pourquoi 20 jours × 16h ?** Nous simulons **un mois de production** (20 jours ouvrés) avec **2 quarts de 8 heures chacun** (16h/jour), ce qui correspond au régime de travail d'ABC Emboutissage.

### Étape 3 : Préparer l'Espace de Travail

1. Dans la **Library** (panneau de gauche), repérez les objets dont vous aurez besoin :
   - **Source** (arrivée des matières premières)
   - **Processor** (machines de transformation)
   - **Queue** (files d'attente / stocks)
   - **Sink** (expédition client)
2. Configurez la vue : utilisez la molette de la souris pour zoomer/dézoomer
3. Activez la grille : **View → Show Grid**

---

## 4. Modélisation des Processus

### Étape 4 : Créer la Source (Matières Premières)

1. Glissez-déposez un objet **Source** depuis la Library vers le modèle
2. Positionnez-le à gauche de l'espace de travail
3. Double-cliquez sur la Source pour ouvrir ses propriétés
4. Renommez-la : **"MP_Acier"** (Matière Première Acier)
5. Configuration de l'arrivée :
   - Onglet **Flow**
   - Arrival Style : **Arrival at time 0**
   - Max Arrivals : **Unlimited**

> **💡 Pourquoi "Arrival at time 0" ?** Nous supposons que les **5 jours de stock de matière première** sont déjà présents en début de simulation. Les pièces seront "tirées" par les processus selon leurs besoins.

### Étape 5 : Créer le Processus Emboutissage

1. Glissez-déposez un **Processor** à droite de la Source
2. Renommez-le : **"Emboutissage"**
3. Changez sa couleur (clic droit → Edit Visual) pour le distinguer (ex: bleu foncé)

### Étape 6 : Créer le Stock après Emboutissage

1. Glissez-déposez une **Queue** à droite de l'Emboutissage
2. Renommez-la : **"Stock_Emboutissage"**
3. Changez son apparence : clic droit → **Edit Visual**
   - Augmentez la taille de la zone de stockage pour visualiser 7000 pièces

### Étape 7 : Créer les Autres Processus

Répétez les étapes 5 et 6 pour créer la chaîne complète :

| Ordre | Objet FLEXSIM | Nom | Notes |
|-------|---------------|-----|-------|
| 1 | Processor | Soudage_I | Couleur verte |
| 2 | Queue | Stock_Soudage_I | Capacité 1 700 pièces |
| 3 | Processor | Soudage_II | Couleur verte claire |
| 4 | Queue | Stock_Soudage_II | Capacité 2 450 pièces |
| 5 | Processor | Montage_I | Couleur rouge (GOULOT !) |
| 6 | Queue | Stock_Montage_I | Capacité 1 840 pièces |
| 7 | Processor | Montage_II | Couleur orange |
| 8 | Queue | Stock_PF | Produits Finis - 4 140 pièces |

### Étape 8 : Créer le Sink (Expédition Client)

1. Glissez-déposez un **Sink** à l'extrémité droite
2. Renommez-le : **"Client_Carbec"**

**✅ Vérification Visuelle :** Vous devriez maintenant avoir une ligne horizontale :

```
MP_Acier → Emboutissage → Stock_Emboutissage → Soudage_I → Stock_Soudage_I → 
Soudage_II → Stock_Soudage_II → Montage_I → Stock_Montage_I → Montage_II → 
Stock_PF → Client_Carbec
```

---

## 5. Configuration des Paramètres

> **⚠️ Attention aux Unités :** FLEXSIM utilise les **secondes** comme unité de temps par défaut. Tous les temps de cycle doivent être en secondes !

### Étape 9 : Configurer Emboutissage

1. Double-cliquez sur le processeur **Emboutissage**
2. Onglet **Process Time** :
   - Distribution : **Constant**
   - Value : **1** (seconde)
3. Onglet **Setup Time** (Temps de Changement de Format) :
   - Activez le Setup Time
   - Distribution : **Constant**
   - Value : **3600** (1 heure = 3600 secondes)
4. Onglet **State** (Pannes / Fiabilité 85%) :
   - Cliquez sur **Add State Profile**
   - Type : **Time Based**
   - MTBF = 10000 s, MTTR = 1765 s (pour obtenir ~85% de disponibilité)

### Étape 10 : Configurer Soudage I

1. Double-cliquez sur **Soudage_I**
2. Process Time : **39** secondes (Constant)
3. Setup Time : **600** secondes (10 min)
4. State : Pas de pannes (Fiabilité 100%)

### Étape 11 : Configurer Soudage II

1. Process Time : **46** secondes
2. Setup Time : **600** secondes
3. State : Pannes pour 80% de fiabilité
   - MTBF = 8000 s, MTTR = 2000 s (pour obtenir ~80%)

### Étape 12 : Configurer Montage I (GOULOT)

1. Process Time : **62** secondes ⚠️
2. Setup Time : Aucun (pas de TCF)
3. State : Pas de pannes (100%)

> **🔴 Goulot d'Étranglement :** Avec un temps de cycle de **62 secondes** supérieur au Takt Time de **60 secondes**, ce processus ne pourra jamais suivre la demande client sans amélioration !

### Étape 13 : Configurer Montage II

1. Process Time : **40** secondes
2. Setup Time : Aucun
3. State : Pas de pannes (100%)

### Étape 14 : Configurer les Stocks Initiaux

Pour chaque **Queue**, configurez le stock initial :

1. Double-cliquez sur la Queue
2. Onglet **Initial Content**
3. Ajoutez le nombre de pièces initiales :
   - Stock_Emboutissage : **7000**
   - Stock_Soudage_I : **1700**
   - Stock_Soudage_II : **2450**
   - Stock_Montage_I : **1840**
   - Stock_PF : **4140**

> **💡 Stocks Initiaux :** Ces stocks représentent l'état observé lors de l'étude VSM. Ils permettent de démarrer la simulation dans les conditions réelles de l'usine.

---

## 6. Connexions et Flux

### Étape 15 : Créer les Connexions

1. Sélectionnez l'icône **Connect Objects (A)** dans la barre d'outils
2. Créez les connexions dans l'ordre :
   a. MP_Acier → Emboutissage
   b. Emboutissage → Stock_Emboutissage
   c. Stock_Emboutissage → Soudage_I
   d. Soudage_I → Stock_Soudage_I
   e. Stock_Soudage_I → Soudage_II
   f. Soudage_II → Stock_Soudage_II
   g. Stock_Soudage_II → Montage_I
   h. Montage_I → Stock_Montage_I
   i. Stock_Montage_I → Montage_II
   j. Montage_II → Stock_PF
   k. Stock_PF → Client_Carbec

### Étape 16 : Configurer la Demande Client

1. Double-cliquez sur **Client_Carbec** (Sink)
2. Configuration de la demande :
   - Nous devons simuler une demande de **920 pièces par jour**
   - Avec 2 quarts de 8h, cela donne un rythme constant
3. Pour simplifier, le Sink accepte toutes les pièces qui arrivent

> **💡 Modélisation Simplifiée :** Pour ce modèle initial, nous simulons un **flux poussé** où chaque processus produit en continu. Dans un modèle avancé, on pourrait ajouter un système de contrôle de production (MRP) et des commandes quotidiennes.

---

## 7. Exécution et Analyse

### Étape 17 : Préparer les Statistiques

1. Ajoutez un **Dashboard** pour visualiser les résultats
2. Créez des graphiques pour :
   - **État des processus** (occupé, en panne, idle)
   - **Niveaux de stocks** dans chaque Queue
   - **Throughput** (nombre de pièces produites)
   - **Cycle Time** moyen

### Étape 18 : Lancer la Simulation

1. Vérifiez que tous les objets sont bien connectés
2. Cliquez sur le bouton **Reset** (icône de rafraîchissement) pour réinitialiser
3. Cliquez sur **Run** (icône de lecture)
4. Observez la simulation :
   - Les pièces se déplacent entre les processus
   - Les stocks évoluent
   - Le goulot **Montage_I** devrait créer une accumulation en amont
5. Laissez la simulation tourner jusqu'à la fin (1 728 000 secondes = 20 jours)

> **⏱️ Temps de Simulation :** La simulation peut prendre plusieurs minutes selon votre ordinateur. Vous pouvez augmenter la vitesse avec le curseur **Speed**.

### Étape 19 : Analyser les Résultats

Après la simulation, consultez les statistiques :

#### 📊 Indicateurs Clés à Vérifier

| Indicateur | Comment le Trouver | Valeur Attendue |
|------------|-------------------|-----------------|
| **Throughput Total** | Sink → Statistics → Output | ~18 400 pièces (ou moins à cause du goulot) |
| **Utilisation Montage_I** ⚠️ | Processor → State Bar | ~100% (SATURÉ) |
| **Niveau Stock_Emboutissage** | Queue → Content Graph | Augmente continuellement |
| **Lead Time Moyen** | Dashboard → Average Staytime | ~23,6 jours (correspondance VSM) |

**✅ Validation VSM :** Si vos résultats correspondent approximativement aux calculs VSM (goulot à Montage I, stocks élevés, Lead Time ~23-24 jours), votre modèle est **validé** ! 🎉

---

## 8. Exercices de Validation

### 📝 Exercice 1 : Vérifier le Goulot

**Question :** Confirmez que Montage_I est bien le goulot en observant :

1. Son taux d'utilisation (doit être proche de 100%)
2. L'accumulation de stock en amont (Stock_Montage_I doit augmenter)
3. La famine en aval (Stock_PF devrait diminuer si le goulot ne suit pas)

### 📝 Exercice 2 : Calculer le Taux de Production Réel

**Consigne :** Avec un temps de cycle de 62s à Montage_I, calculez :

- Combien de pièces peuvent être produites par jour ?
- Quelle est la capacité mensuelle (20 jours) ?
- Quel est le déficit par rapport à la demande de 18 400 pièces/mois ?

**Réponse attendue :**

- Pièces/jour = 55 200 s ÷ 62 s = **890 pièces/jour**
- Capacité mensuelle = 890 × 20 = **17 800 pièces/mois**
- Déficit = 18 400 - 17 800 = **600 pièces/mois** ⚠️

### 📝 Exercice 3 : Tester une Amélioration

**Scénario :** Proposez et testez une amélioration pour éliminer le goulot.

**Suggestions :**

- **Option A :** Ajouter un 2ème opérateur à Montage_I (dupliquer le processeur)
- **Option B :** Réduire le temps de cycle de Montage_I à 58s (amélioration méthode)
- **Option C :** Accepter les heures supplémentaires (augmenter temps disponible)

**Défi :** Créez une nouvelle version du modèle avec votre amélioration et comparez les résultats !

### 📝 Exercice 4 : Analyser l'Impact des Pannes

**Question :** Les processus Emboutissage (85%) et Soudage II (80%) ont des pannes.

1. Observez l'évolution des stocks en amont et en aval de ces processus
2. Les pannes créent-elles des goulots temporaires ?
3. Quel serait l'impact d'améliorer la fiabilité à 95% ?

---

## 9. FAQ et Dépannage

### ❓ Les pièces ne se déplacent pas dans la simulation

**Solution :**

- Vérifiez que tous les objets sont correctement connectés (flèches visibles)
- Vérifiez que la Source génère bien des pièces (clic droit → Quick Properties)
- Réinitialisez et relancez : bouton **Reset** puis **Run**

### ❓ La simulation est très lente

**Solution :**

- Augmentez le curseur **Speed** en haut de l'écran
- Désactivez les animations 3D : **View → Disable 3D**
- Réduisez la durée de simulation pour les tests (ex: 5 jours au lieu de 20)

### ❓ Les résultats ne correspondent pas aux calculs VSM

**Vérifications :**

- Les temps de cycle sont-ils en **secondes** ?
- Les stocks initiaux sont-ils correctement configurés ?
- La durée de simulation est-elle de 1 728 000 secondes (20 jours × 16h) ?
- Les pannes (MTBF/MTTR) sont-elles configurées pour Emboutissage et Soudage II ?

### ❓ Quel niveau de détail pour un modèle réaliste ?

**Réponse :**

Ce tutoriel présente un modèle **de niveau intermédiaire**. Pour aller plus loin :

- **Niveau avancé :** Ajouter les 2 variantes (LH/RH), les changements de format, les opérateurs, les convoyeurs
- **Niveau expert :** Modéliser le contrôle de production (MRP), les commandes quotidiennes, les livraisons fournisseur, les calendriers de pause

### ❓ Comment sauvegarder et exporter les résultats ?

**Méthodes :**

- **Statistiques :** Clic droit sur un graphique → **Export Data** (Excel)
- **Captures d'écran :** **File → Export View → Image**
- **Rapport :** **Tools → Experimenter** pour générer des rapports automatiques

### 🎓 Ressources Complémentaires

Pour approfondir FLEXSIM, consultez :

- **FlexSim Primer 2020** (dans le dossier Supports_Enseignement)
- **Formation FlexSim 24.0.pdf** (tutoriels officiels)
- **FlexSim User Manual** : Help → User Manual dans FLEXSIM
- **FlexSim Community** : forum.flexsim.com

---

## 🎯 Conclusion

### Félicitations ! 🎉

Vous avez créé votre premier modèle FLEXSIM de l'usine ABC Emboutissage et reproduit l'état initial de l'étude VSM.

#### Ce que vous avez appris

- ✅ Structurer un flux de production dans FLEXSIM
- ✅ Configurer des processus avec temps de cycle, changements de format et pannes
- ✅ Modéliser des stocks intermédiaires
- ✅ Identifier les goulots d'étranglement par simulation
- ✅ Valider un modèle par comparaison avec les calculs VSM

### 🚀 Prochaines Étapes

Pour continuer votre apprentissage :

1. **Expérimentez** avec différents scénarios d'amélioration
2. **Créez l'état futur** en appliquant les principes Lean (flux tiré, kanban, nivellement)
3. **Comparez** l'état initial et l'état futur (Lead Time, stocks, throughput)
4. **Présentez** vos résultats avec des graphiques et dashboards

### 💡 Point Clé

La simulation FLEXSIM permet de **tester des améliorations sans risque** avant de les implémenter dans la réalité. C'est un outil puissant pour le Lean Manufacturing et l'amélioration continue !

---

**Tutoriel FLEXSIM - Modélisation Usine ABC Emboutissage**  
Pôle Formation UIMM CVDL - Organisation Industrielle

*"Simuler pour mieux comprendre, comprendre pour mieux améliorer"*
