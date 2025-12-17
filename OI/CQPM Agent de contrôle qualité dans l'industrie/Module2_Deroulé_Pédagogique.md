# Module 2 : Statistiques et Capabilité

## Déroulé Pédagogique Détaillé

**Durée totale** : 28 heures (4 jours de 7 heures)  
**Niveau** : BAC/BTS  
**Formateur** : Voir Guide_Formateur.md pour notes pédagogiques

---

## 🎯 Objectifs Pédagogiques du Module

À l'issue de ce module, les stagiaires seront capables de :

1. **Calculer** et **interpréter** les statistiques descriptives (moyenne, écart-type, médiane, etc.)
2. **Créer** et **exploiter** des cartes de contrôle aux mesures (X̄-R, X-MR)
3. **Calculer** la capabilité machine (Cm, Cmk) et processus (Cp, Cpk)
4. **Interpréter** les indices de capabilité et prendre des décisions
5. **Réaliser** une étude MSA (R&R) pour valider un moyen de mesure
6. **Utiliser** Excel, Ellistat et R pour les analyses statistiques qualité
7. **Construire** des histogrammes et identifier les lois de distribution

---

## 📅 JOUR 1 - Statistiques Descriptives Appliquées au Contrôle Qualité

### 🌅 MATIN (3h30) - 09h00-12h30

#### Séquence 1.1 : Accueil et Introduction au Module 2 (30 min) - 09h00-09h30

**Objectif** : Lancer le module et faire le lien avec le Module 1

**Contenu** :
- Accueil des stagiaires
- Rappel du Module 1 (plans de contrôle, gammes, AMDEC)
- Présentation du Module 2 : pourquoi les statistiques en qualité ?
- Programme des 4 jours
- Présentation des logiciels : Excel, Ellistat, R

**Activité ice-breaker** :
- "Citez un indicateur chiffré que vous utilisez dans votre travail"
- Discussion sur l'importance des chiffres en qualité

**Méthode pédagogique** : Exposé interactif

---

#### Séquence 1.2 : Les Fondamentaux des Statistiques (1h30) - 09h30-11h00

**Objectif** : Comprendre les concepts statistiques de base appliqués à la qualité

**Contenu théorique** :

1. **Pourquoi les statistiques en contrôle qualité ?**
   - Passer de l'intuition à la mesure
   - Variation naturelle vs variation anormale
   - Prendre des décisions basées sur les données

2. **Population vs Échantillon**
   - Population : Ensemble complet (ex: toute la production)
   - Échantillon : Sous-ensemble représentatif
   - Inférence statistique : du particulier au général

3. **Les mesures de tendance centrale**
   - **Moyenne (x̄)** : Somme / Nombre
     - Formule : x̄ = (Σxi) / n
     - Sensible aux valeurs extrêmes
   - **Médiane** : Valeur centrale
     - Plus robuste que la moyenne
   - **Mode** : Valeur la plus fréquente
   - Quand utiliser l'une ou l'autre?

4. **Les mesures de dispersion**
   - **Étendue (R)** : Max - Min
     - Simple mais peu robuste
   - **Écart-type (σ ou s)** : Mesure moyenne de l'écart à la moyenne
     - Formule (échantillon) : s = √[Σ(xi - x̄)² / (n-1)]
     - Plus l'écart-type est grand, plus les données sont dispersées
   - **Variance** : Carré de l'écart-type
   - **Coefficient de variation** : CV = (s / x̄) × 100%

5. **La loi Normale (Gaussienne)**
   - En forme de cloche
   - Caractérisée par μ (moyenne) et σ (écart-type)
   - **Règle des 68-95-99,7** :
     * ≈68% des données dans [μ-σ ; μ+σ]
     * ≈95% dans [μ-2σ ; μ+2σ]
     * ≈99,7% dans [μ-3σ ; μ+3σ]
   - Importance en qualité : la plupart des processus suivent une loi normale

**Activité** :
- Calcul manuel des statistiques sur un petit jeu de données (10 valeurs)
- Chacun calcule moyenne et écart-type, puis comparaison

**Méthode pédagogique** : Exposé + exercice pratique

**Support** : Module2_Support_Stagiaire.md (Section 1)

---

#### ☕ PAUSE (15 min) - 11h00-11h15

---

#### Séquence 1.3 : Visualisation des Données (1h15) - 11h15-12h30

**Objectif** : Savoir représenter graphiquement des données qualité

**Contenu** :

1. **L'histogramme**
   - Définition : Graphique en barres des fréquences
   - Construction :
     * Déterminer le nombre de classes (formule de Sturges : k ≈ 1 + 3,3 log(n))
     * Calculer la largeur des classes
     * Compter les effectifs par classe
   - Interprétation : forme, centrage, dispersion
   - Lien avec la loi normale

2. **Le diagramme en boîte (box plot)**
   - Visualise quartiles, médiane, valeurs extrêmes
   - Détection rapide des outliers

3. **Le nuage de points (scatter plot)**
   - Visualiser la relation entre 2 variables
   - Corrélation

4. **Applications en contrôle qualité**
   - Comparer les données aux spécifications
   - Identifier les tendances
   - Détecter les anomalies

**Démonstration Excel** :
- Le formateur crée un histogramme pas à pas dans Excel
- Utilisation des fonctions : MOYENNE(), ECARTYPE.STANDARD(), etc.

**Méthode pédagogique** : Exposé + démonstration

**Support** : Module2_Support_Stagiaire.md (Section 2)

---

### 🌆 APRÈS-MIDI (3h30) - 13h30-17h00

#### Séquence 1.4 : TP4 - Statistiques Descriptives avec Excel (2h30) - 13h30-16h00

**Objectif** : Maîtriser l'analyse statistique de données de production avec Excel

**Contexte du TP** :
Vous disposez d'un fichier de données de production : 100 mesures de diamètres de pièces usinées. La spécification est : Ø 25,00 ± 0,10 mm.

**Travail demandé** :

1. **Statistiques descriptives**
   - Calculer: moyenne, médiane, mode, écart-type, min, max, étendue
   - Utiliser les fonctions Excel appropriées

2. **Visualisation**
   - Créer un histogramme
   - Créer un box plot
   - Tracer les limites de spécification sur l'histogramme

3. **Interprétation**
   - Le processus est-il centré ?
   - La dispersion est-elle acceptable ?
   - Y a-t-il des valeurs aberrantes ?
   - Estimation du % de non-conformes

4. **Rapport d'analyse**
   - Synthétiser les résultats
   - Proposer des actions si nécessaire

**Déroulement** :
- 15 min : Lecture énoncé (TP4_Stats_Descriptives_Excel.md)
- 1h45 : Travail individuel
- 30 min : Correction collective + discussion

**Livrables** :
- Fichier Excel avec calculs et graphiques
- Mini-rapport d'analyse (1 page)

**Support** :
- TP4_Stats_Descriptives_Excel.md
- TP4_Donnees.xlsx (100 mesures)

**Compétences travaillées** :
✅ Calculer les statistiques descriptives  
✅ Créer des graphiques pertinents  
✅ Interpréter les résultats  
✅ Prendre des décisions basées sur les données  

---

#### ☕ PAUSE (15 min) - 16h00-16h15

---

#### Séquence 1.5 : Introduction au SPC (Maîtrise Statistique des Procédés) (45 min) - 16h15-17h00

**Objectif** : Comprendre les principes du SPC et l'utilité des cartes de contrôle

**Contenu théorique** :

1. **Qu'est-ce que le SPC ?**
   - Statistical Process Control / Maîtrise Statistique des Procédés (MSP)
   - Objectif : Surveiller et maîtriser la variabilité du processus
   - Approche préventive (pas réactive)

2. **Variation commune vs variation spéciale**
   - **Variation commune** : Inhérente au processus, aléatoire, stable
   - **Variation spéciale** : Cause assignable, à éliminer
   - Processus sous contrôle vs hors contrôle

3. **Le concept de carte de contrôle**
   - Inventée par Walter Shewhart (1924)
   - Graphique temporel avec limites de contrôle
   - Structure :
     * Ligne centrale (LC)
     * Limite de contrôle supérieure (LCS)
     * Limite de contrôle inférieure (LCI)

4. **Types de cartes de contrôle**
   - **Aux mesures** : X̄-R, X̄-S, X-MR (données continues)
   - **Aux attributs** : p, np, c, u (données discrètes)

5. **Preview du Jour 2**
   - Demain : Construction et interprétation des cartes X̄-R

**Méthode pédagogique** : Exposé + vidéo courte (5 min) sur le SPC

**Support** : Module2_Support_Stagiaire.md (Section 3)

---

## 📅 JOUR 2 - Cartes de Contrôle

### 🌅 MATIN (3h30) - 09h00-12h30

#### Séquence 2.1 : Rappel J1 et Introduction Cartes de Contrôle (15 min) - 09h00-09h15

**Objectif** : Réactiver les connaissances et introduire les cartes X̄-R

**Contenu** :
- Quiz rapide sur les statistiques descriptives
- Lien avec les cartes de contrôle
- Programme du jour

---

#### Séquence 2.2 : Cartes de Contrôle X̄-R - Théorie (1h45) - 09h15-11h00

**Objectif** : Comprendre la construction et l'utilisation des cartes X̄-R

**Contenu théorique** :

1. **Carte X̄-R : Principe**
   - **Carte X̄** (X-barre) : Surveille la moyenne (centrage du processus)
   - **Carte R** (Range/Étendue) : Surveille la dispersion (stabilité)
   - Toujours utiliser les deux ensemble

2. **Données nécessaires**
   - Sous-groupes (échantillons) de taille n (typiquement n = 4 ou 5)
   - Fréquence régulière (ex: 1 échantillon toutes les heures)
   - Minimum 20-25 sous-groupes pour calculer les limites

3. **Construction de la Carte R**
   - Pour chaque sous-groupe i :
     * Ri = Maxi - Mini
   - Calcul de R̄ (moyenne des étendues) :
     * R̄ = ΣRi / k (k = nombre de sous-groupes)
   - Limites de contrôle :
     * LCR = R̄
     * LCSR = D4 × R̄
     * LCIR = D3 × R̄
   - D3 et D4 : constantes tabulées (dépendent de n)

4. **Construction de la Carte X̄**
   - Pour chaque sous-groupe i :
     * X̄i = moyenne du sous-groupe
   - Calcul de X̿ (moyenne des moyennes) :
     * X̿ = ΣX̄i / k
   - Limites de contrôle :
     * LCX̄ = X̿
     * LCSX̄ = X̿ + A2 × R̄
     * LCIX̄ = X̿ - A2 × R̄
   - A2 : constante tabulée (dépend de n)

5. **Table des constantes**
   
   | n | A2 | D3 | D4 |
   |---|----|----|-----|
   | 2 | 1,880 | 0 | 3,267 |
   | 3 | 1,023 | 0 | 2,575 |
   | 4 | 0,729 | 0 | 2,282 |
   | 5 | 0,577 | 0 | 2,115 |
   | 6 | 0,483 | 0 | 2,004 |

6. **Interprétation : Processus sous contrôle**
   - Tous les points entre LCS et LCI
   - Pas de tendance
   - Répartition aléatoire autour de LC
   - → Seule variation commune présente

7. **Règles de détection (Western Electric Rules)**
   - **Règle 1** : 1 point hors limites → OUT
   - **Règle 2** : 2 points consécutifs sur 3 dans zone A (2-3σ) → OUT
   - **Règle 3** : 4 points consécutifs sur 5 dans zone B (1-2σ) → OUT
   - **Règle 4** : 8 points consécutifs du même côté de LC → Dérive
   - **Règle 5** : 6 points en tendance continue (montante ou descendante) → Trend

**Activité** :
- Calcul manuel sur 5 sous-groupes de taille n=4
- Tracer les cartes sur papier millimétré

**Méthode pédagogique** : Exposé + exercice guidé

**Support** : Module2_Support_Stagiaire.md (Section 4)

---

#### ☕ PAUSE (15 min) - 11h00-11h15

---

#### Séquence 2.3 : Démonstration Excel - Cartes X̄-R (1h15) - 11h15-12h30

**Objectif** : Voir comment automatiser les cartes de contrôle dans Excel

**Contenu** :
- Le formateur construit une carte X̄-R complète dans Excel
- Étapes :
  1. Organiser les données (sous-groupes en colonnes)
  2. Calculer X̄i et Ri pour chaque sous-groupe
  3. Calculer X̿ et R̄
  4. Appliquer les formules pour LCS et LCI
  5. Créer les graphiques
  6. Ajouter les limites de contrôle
  7. Interpréter

**Astuces Excel** :
- Utilisation de références absolues ($) pour R̄, X̿
- Mise en forme conditionnelle pour les points hors limites
- Création de modèles réutilisables

**Méthode pédagogique** : Démonstration interactive

**Note** : Les stagiaires suivent sur leur ordinateur (phase "mirror")

---

### 🌆 APRÈS-MIDI (3h30) - 13h30-17h00

#### Séquence 2.4 : TP5 - Cartes de Contrôle X̄-R avec Excel (2h15) - 13h30-15h45

**Objectif** : Construire et interpréter des cartes de contrôle en autonomie

**Contexte du TP** :
Vous supervisez une ligne de conditionnement. Le poids net des produits est critique. Vous prélevez des échantillons de n=5 produits toutes les heures pendant 25 heures.

**Spécification** : Poids net = 500 g ± 10 g

**Travail demandé** :

1. **Construction des cartes**
   - Calculer X̄i et Ri pour les 25 sous-groupes
   - Calculer les limites de contrôle
   - Tracer carte R
   - Tracer carte X̄

2. **Interprétation**
   - Le processus est-il sous contrôle ?
   - Identifier les points hors contrôle ou tendances
   - Appliquer les Western Electric Rules

3. **Analyse**
   - Si hors contrôle : hypothèses sur les causes spéciales
   - Proposer des actions correctives

4. **Comparaison limites de contrôle vs spécifications**
   - Les limites naturelles du processus (± 3σ) vs spécifications
   - Le processus peut-il respecter les spécifications ?

**Déroulement** :
- 15 min : Lecture énoncé (TP5_Cartes_Controle_Excel.md)
- 1h30 : Travail en binômes
- 30 min : Correction + analyse des cas particuliers rencontrés

**Livrables** :
- Fichier Excel avec cartes X̄-R
- Rapport d'interprétation

**Support** :
- TP5_Cartes_Controle_Excel.md
- TP5_Cartes_Xbarre_R.xlsx (données)

**Compétences travaillées** :
✅ Calculer les limites de contrôle  
✅ Construire des cartes X̄-R  
✅ Interpréter l'état de maîtrise du processus  
✅ Distinguer contrôle statistique vs conformité spécifications  

---

#### ☕ PAUSE (15 min) - 15h45-16h00

---

#### Séquence 2.5 : Autres Types de Cartes de Contrôle (1h00) - 16h00-17h00

**Objectif** : Découvrir les autres cartes de contrôle et leurs usages

**Contenu théorique** :

1. **Carte X-MR (Individus - Étendue Mobile)**
   - Quand : Mesures individuelles (pas de sous-groupes)
   - Exemples : Production lente, mesures destructives, analyses chimiques
   - Calcul de MR (Moving Range) : |Xi - Xi-1|

2. **Carte X̄-S (Moyenne - Écart-type)**
   - Quand : Sous-groupes de grande taille (n > 10)
   - Plus précise que X̄-R pour grandes tailles

3. **Cartes aux attributs**
   - **Carte p** : Proportion de défectueux (n variable possible)
   - **Carte np** : Nombre de défectueux (n constant)
   - **Carte c** : Nombre de défauts par unité (n constant)
   - **Carte u** : Nombre de défauts par unité (n variable)

4. **Comment choisir la bonne carte ?**
   
   | Type de données | Taille échantillon | Carte recommandée |
   |-----------------|-------------------|-------------------|
   | Mesures | n = 1 | X-MR |
   | Mesures | 2 ≤ n ≤ 10 | X̄-R |
   | Mesures | n > 10 | X̄-S |
   | Attributs (bon/mauvais) | Constant | np ou c |
   | Attributs (bon/mauvais) | Variable | p ou u |

**Activité** :
- Exercices de choix de carte (6 situations différentes)

**Méthode pédagogique** : Exposé + quiz interactif

**Support** : Module2_Support_Stagiaire.md (Section 5)

---

## 📅 JOUR 3 - Capabilité et MSA

### 🌅 MATIN (3h30) - 09h00-12h30

#### Séquence 3.1 : Rappel J2 et Introduction Capabilité (15 min) - 09h00-09h15

**Objectif** : Transition vers la capabilité

**Contenu** :
- Synthèse des cartes de contrôle
- Différence entre "sous contrôle" et "capable"
- Introduction à la capabilité

---

#### Séquence 3.2 : Capabilité Machine et Processus - Théorie (2h00) - 09h15-11h15

**Objectif** : Comprendre, calculer et interpréter les indices de capabilité

**Contenu théorique** :

1. **Définitions**
   - **Capabilité** : Aptitude d'un processus/machine à produire dans les spécifications
   - Mesure du rapport entre tolérance et variation
   - Indicateurs : Cm, Cmk, Cp, Cpk, Pp, Ppk

2. **Conditions préalables**
   - ✅ Processus sous contrôle statistique (vérifié par cartes de contrôle)
   - ✅ Distribution normale (vérifiée par test de normalité)
   - ⚠️ Ne jamais calculer la capabilité d'un processus hors contrôle !

3. **Capabilité Machine (Court terme)**
   
   - **Cm** (Capability Machine) : Capabilité intrinsèque
     * Cm = Tolérance / (6 × σm)
     * Cm = (TS - TI) / (6 × σm)
     * σm = écart-type machine (court terme, conditions stables)
   
   - **Cmk** : Capabilité machine décentrée
     * Cmk = min[(TS - μ) / (3σm) ; (μ - TI) / (3σm)]
     * Tient compte du centrage
   
   - **Interprétation Cm et Cmk**
     * < 1,00 : Machine non capable
     * 1,00 - 1,33 : Acceptable (surveiller)
     * 1,33 - 1,67 : Capable
     * ≥ 1,67 : Très capable
   
   - **Étude de capabilité machine** :
     * Machine en conditions optimales
     * Courte durée (50-100 pièces)
     * Opérateur expérimenté
     * Matière homogène

4. **Capabilité Processus (Long terme)**
   
   - **Cp** : Capabilité processus
     * Cp = (TS - TI) / (6σ)
     * σ = écart-type processus (long terme, toutes variations)
   
   - **Cpk** : Capabilité processus décentré
     * Cpk = min[(TS - μ) / (3σ) ; (μ - TI) / (3σ)]
   
   - **Étude de capabilité processus** :
     * Conditions normales de production
     * Longue durée (plusieurs jours, changements d'équipe, etc.)
     * Tous les opérateurs
     * Variation des matières
   
5. **Performance Processus : Pp et Ppk**
   - Calculés comme Cp et Cpk mais σ estimé différemment
   - Pp : Performance potentielle
   - Ppk : Performance réelle
   - Utilisés quand le processus n'est pas encore stable

6. **Lecture des indices**
   - Cmk < Cm : Processus décentré
   - Cpk < Cp : Processus décentré
   - Cm > Cp : Dérive sur le long terme
   - Si Cpk < 1,33 :
     * Recentrer si Cpk < Cp (décentrage)
     * Réduire la dispersion si Cpk ≈ Cp (dispersion excessive)

7. **Pourcentage de non-conformes**
   - Lien entre Cpk et % NC (si loi normale)
   - Cpk = 1,00 → ≈0,27% NC
   - Cpk = 1,33 → ≈63 ppm (parties par million)
   - Cpk = 1,67 → ≈0,6 ppm
   - Cpk = 2,00 → ≈0,002 ppm

**Activité** :
- Exercice de calcul : données fournies, calculer Cm, Cmk, Cp, Cpk
- Interprétation de plusieurs cas

**Méthode pédagogique** : Exposé + exercices d'application

**Support** : Module2_Support_Stagiaire.md (Section 6)

---

#### ☕ PAUSE (15 min) - 11:15-11:30

---

#### Séquence 3.3 : Démonstration Excel - Étude de Capabilité (1h00) - 11h30-12h30

**Objectif** : Automatiser le calcul de capabilité dans Excel

**Contenu de la démonstration** :
1. Import et organisation des données
2. Test de normalité (graphique + test de Shapiro-Wilk si possible)
3. Calcul de μ et σ
4. Calcul de Cm, Cmk (ou Cp, Cpk)
5. Création d'un histogramme avec limites de spécification
6. Visualisation de la courbe normale superposée
7. Calcul du % théorique de non-conformes
8. Rapport de capabilité synthétique

**Méthode pédagogique** : Démonstration pas à pas

---

### 🌆 APRÈS-MIDI (3h30) - 13h30-17h00

#### Séquence 3.4 : TP6 - Étude de Capabilité avec Excel (1h45) - 13h30-15h15

**Objectif** : Réaliser une étude de capabilité complète

**Contexte du TP** :
Vous devez valider la capabilité d'un tour de décolletage pour la production d'axes. Caractéristique critique : Ø 20,00 ± 0,05 mm.

**Données** :
- Étude machine : 100 mesures en conditions optimales
- Étude processus : 200 mesures sur 1 semaine de production

**Travail demandé** :

1. **Étude Machine**
   - Vérifier la normalité
   - Calculer Cm et Cmk
   - Interpréter (machine capable ?)

2. **Étude Processus**
   - Vérifier la normalité
   - Calculer Cp et Cpk
   - Interpréter (processus capable ?)

3. **Comparaison et Analyse**
   - Comparer Cm vs Cp : Dérive ?
   - Comparer Cmk vs Cpk : Problème de centrage ?
   - Estimation du % de non-conformes

4. **Recommandations**
   - Actions pour améliorer la capabilité si nécessaire
   - Priorités (recentrage vs réduction dispersion)

**Déroulement** :
- 15 min : Lecture énoncé (TP6_Capabilite_Excel.md)
- 1h00 : Travail en binômes
- 30 min : Correction et discussion

**Livrables** :
- Fichier Excel avec calculs et graphiques
- Rapport de capabilité (modèle fourni)

**Support** :
- TP6_Capabilite_Excel.md
- TP6_Capabilite.xlsx

**Compétences travaillées** :
✅ Distinguer capabilité machine vs processus  
✅ Calculer Cm, Cmk, Cp, Cpk  
✅ Interpréter les indices  
✅ Proposer des actions d'amélioration  

---

#### ☕ PAUSE (15 min) - 15h15-15h30

---

#### Séquence 3.5 : MSA - Measurement System Analysis (1h30) - 15h30-17h00

**Objectif** : Comprendre l'importance de valider le système de mesure

**Contenu théorique** :

1. **Pourquoi la MSA ?**
   - "Mesurer, c'est comparer à un étalon"
   - Toute mesure comporte des erreurs
   - Question : Mon moyen de mesure est-il fiable ?
   - MSA : Valider le système de mesure AVANT d'étudier le processus

2. **Composantes de la variabilité totale**
   - Variabilité Totale = Variabilité Pièce + Variabilité Mesure
   - Variabilité Mesure = Répétabilité + Reproductibilité + ...
   - **Répétabilité** : Même opérateur, même pièce → variabilité de l'instrument
   - **Reproductibilité** : Opérateurs différents, même pièce → variabilité opérateur

3. **Étude R&R (Repeatability & Reproducibility)**
   
   - **Protocole standard** :
     * 10 pièces
     * 3 opérateurs
     * 2 ou 3 répétitions
     * Total : 60 ou 90 mesures
   
   - **Plan de mesure** :
     * Pièces codées aléatoirement
     * Chaque opérateur mesure toutes les pièces
     * Plusieurs fois sans connaître le résultat précédent
   
4. **Calculs et Interprétation**
   
   - **%R&R** = (Variation R&R / Variation Totale) × 100
   
   - **Critères d'acceptation** :
     * %R&R < 10% : Système de mesure excellent
     * 10% < %R&R < 30% : Acceptable (selon criticité)
     * %R&R > 30% : Système non acceptable
   
   - **ndc** (number of distinct categories) :
     * ndc ≥ 5 : Bon système
     * ndc < 5 : Système insuffisant

5. **Actions si MSA non satisfaisante**
   - Vérifier l'étalonnage
   - Former les opérateurs
   - Changer de moyen de mesure plus précis
   - Réviser le mode opératoire

6. **Autres méthodes MSA**
   - Biais (Bias)
   - Linéarité
   - Stabilité
   - Focus aujourd'hui : R&R

**Activité** :
- Analyse d'un rapport R&R (exemple fourni)
- Discussion : Accepteriez-vous ce système de mesure ?

**Méthode pédagogique** : Exposé + étude de cas

**Support** : Module2_Support_Stagiaire.md (Section 7)

---

## 📅 JOUR 4 - Ellistat, R et Intégration

### 🌅 MATIN (3h30) - 09h00-12h30

#### Séquence 4.1 : Rappel J3 et Présentation Ellistat (15 min) - 09h00-09h15

**Objectif** : Transition vers les outils professionnels

**Contenu** :
- Synthèse capabilité et MSA
- Limites d'Excel pour les analyses avancées
- Introduction à Ellistat (logiciel SPC professionnel)

---

#### Séquence 4.2 : TP7 - MSA avec Ellistat (1h30) - 09h15-10h45

**Objectif** : Réaliser une étude R&R avec un logiciel professionnel

**Contexte du TP** :
Vous devez valider un nouveau pied à coulisse numérique pour mesurer des épaisseurs. Vous réalisez une étude R&R selon le protocole standard.

**Données fournies** :
- Fichier CSV avec les mesures (10 pièces × 3 opérateurs × 3 répétitions)

**Travail avec Ellistat** :

1. **Import des données**
   - Charger le fichier CSV
   - Structurer les données (pièce, opérateur, mesure)

2. **Lancer l'analyse R&R**
   - Menu MSA → R&R
   - Paramétrer l'étude
   - Lancer le calcul

3. **Interpréter les résultats**
   - %R&R total
   - %Répétabilité
   - %Reproductibilité
   - ndc
   - Graphiques ANOVA

4. **Report**
   - Exporter le rapport R&R
   - Conclure sur l'acceptabilité du système

**Déroulement** :
- 15 min : Découverte de l'interface Ellistat (formateur)
- 45 min : Réalisation du TP guidé
- 30 min : Analyse des résultats

**Livrables** :
- Rapport R&R généré par Ellistat
- Conclusion écrite

**Support** :
- TP7_MSA_Ellistat.md
- TP7_Donnees_MSA.csv

**Compétences travaillées** :
✅ Utiliser Ellistat  
✅ Réaliser une étude R&R  
✅ Interpréter un rapport MSA  

---

#### ☕ PAUSE (15 min) - 10h45-11h00

---

#### Séquence 4.3 : TP8 - Capabilité Complète avec Ellistat (1h30) - 11h00-12h30

**Objectif** : Maîtriser l'étude de capabilité avec Ellistat

**Contexte du TP** :
Données de production d'une semaine (n=250 mesures). Réaliser l'étude de capabilité complète avec Ellistat.

**Travail demandé** :

1. **Import et visualisation**
   - Charger les données
   - Créer un histogramme
   - Créer une carte de contrôle X-MR

2. **Vérifications préalables**
   - Vérifier la normalité (test d'Anderson-Darling)
   - Vérifier le contrôle statistique

3. **Calcul de capabilité**
   - Lancer l'analyse de capabilité
   - Spécifier les tolérances
   - Obtenir Cp, Cpk, Pp, Ppk

4. **Rapport**
   - Générer le rapport de capabilité
   - Interprétation complète
   - Recommandations

**Déroulement** :
- 10 min : Présentation du TP
- 1h00 : Travail individuel
- 20 min : Mise en commun

**Livrables** :
- Rapport Ellistat
- Synthèse écrite

**Support** :
- TP8_Capabilite_Ellistat.md
- TP8_Donnees_Production.csv

**Compétences travaillées** :
✅ Maîtriser Ellistat pour analyses complètes  
✅ Enchaîner les étapes (normalité → contrôle → capabilité)  
✅ Interpréter des rapports professionnels  

---

### 🌆 APRÈS-MIDI (3h30) - 13h30-17h00

#### Séquence 4.4 : Introduction à R pour le Contrôle Qualité (45 min) - 13h30-14h15

**Objectif** : Découvrir R comme outil d'analyse statistique (niveau débutant adapté BAC/BTS)

**Contenu** :

1. **Qu'est-ce que R ?**
   - Langage de programmation statistique
   - Gratuit et open-source
   - Très utilisé en data science et qualité

2. **Pourquoi R en contrôle qualité ?**
   - Automatisation des analyses
   - Graphiques de haute qualité
   - Reproductibilité (scripts réutilisables)
   - Librairies spécialisées (qcc, SixSigma, etc.)

3. **Installation et Interface**
   - R + RStudio
   - Console, script, environnement
   - Packages (install.packages(), library())

4. **Syntaxe de base**
   - Affectation : `x <- 10`
   - Vecteurs : `mesures <- c(10.2, 10.5, 10.1)`
   - Fonctions : `mean(mesures)`, `sd(mesures)`
   - Import CSV : `data <- read.csv("fichier.csv")`

5. **Package qcc (Quality Control Charts)**
   - Installation : `install.packages("qcc")`
   - Fonctions principales :
     * `qcc()` : Cartes de contrôle
     * `process.capability()` : Capabilité

**Démonstration live** :
- Le formateur montre un script simple :
  * Import de données
  * Calcul de statistiques
  * Création d'une carte de contrôle
  * Graphique de capabilité

**Approche pédagogique** :
- Pas de programmation complexe pour niveau BAC/BTS
- Scripts prêts à l'emploi à personnaliser
- Focus sur la compréhension, pas le codage

**Support** : Module2_Support_Stagiaire.md (Section 8)

---

#### Séquence 4.5 : TP9 - Analyse Statistique avec R (1h00) - 14h15-15h15

**Objectif** : Utiliser un script R pour analyser des données qualité

**Contexte du TP** :
Vous disposez d'un script R pré-écrit et de données de production. Vous allez exécuter le script et interpréter les résultats.

**Travail demandé** :

1. **Exécuter le script**
   - Ouvrir RStudio
   - Charger le script TP9_Script.R
   - Modifier les paramètres (nom fichier, spécifications)
   - Exécuter ligne par ligne (Ctrl+Enter)

2. **Analyser les sorties**
   - Statistiques descriptives
   - Histogramme avec courbe normale
   - Test de normalité
   - Calcul de capabilité

3. **Personnalisation simple**
   - Modifier les spécifications
   - Changer le titre du graphique
   - Exporter le graphique en image

**Script fourni (commenté en français)** :
```R
# TP9 - Analyse de Capabilité avec R
# Chargement des packages
library(qcc)

# Import des données
donnees <- read.csv("TP9_Donnees.csv")
mesures <- donnees$Valeur

# Statistiques descriptives
moyenne <- mean(mesures)
ecart_type <- sd(mesures)
print(paste("Moyenne:", round(moyenne, 3)))
print(paste("Écart-type:", round(ecart_type, 3)))

# Graphique
hist(mesures, main="Distribution des mesures", 
     xlab="Valeur", ylab="Fréquence", col="lightblue")

# Test de normalité
shapiro.test(mesures)

# Capabilité (modifier les spécifications)
spec_inf <- 19.95
spec_sup <- 20.05
process.capability(qcc(mesures, type="xbar.one"), 
                   spec.limits=c(spec_inf, spec_sup))
```

**Déroulement** :
- 15 min : Installation R/RStudio si besoin + découverte
- 30 min : Exécution et analyse du TP9
- 15 min : Discussion et questions

**Livrables** :
- Script exécuté avec résultats
- Interprétation écrite

**Support** :
- TP9_Analyse_R.md
- TP9_Script.R
- TP9_Donnees.csv

**Compétences travaillées** :
✅ Utiliser RStudio  
✅ Exécuter un script statistique  
✅ Interpréter les sorties R  

---

#### ☕ PAUSE (15 min) - 15h15-15h30

---

#### Séquence 4.6 : TP10 - Cartes de Contrôle avec R (45 min) - 15h30-16h15

**Objectif** : Créer des cartes de contrôle professionnelles avec R

**Contexte du TP** :
Utiliser le package `qcc` pour créer des cartes X̄-R automatiquement.

**Travail demandé** :
- Charger des données (25 sous-groupes de n=5)
- Créer la carte R avec qcc()
- Créer la carte X̄ avec qcc()
- Interpréter les violations de règles (détectées automatiquement par R)
- Exporter les graphiques

**Script fourni** (à compléter partiellement)

**Déroulement** :
- 30 min : Travail sur le TP
- 15 min : Correction et comparaison avec Excel

**Livrables** :
- Cartes de contrôle générées
- Interprétation

**Support** :
- TP10_Cartes_Controle_R.md
- TP10_Script.R

**Compétences travaillées** :
✅ Utiliser le package qcc  
✅ Automatiser les cartes de contrôle  
✅ Comparer Excel vs R  

---

#### Séquence 4.7 : Cas Pratique Final et Évaluation (1h30) - 16h15-17h45

**Objectif** : Intégrer toutes les compétences du module sur un cas industriel complet

**Format** : 
- CasPratique5_Projet_Final.md
- Travail en groupes de 3-4 personnes

**Contexte** :
Vous êtes une équipe qualité d'une PME sous-traitante automobile. Vous devez qualifier un nouveau processus pour un client exigeant.

**Mission complète** :
1. Valider le système de mesure (MSA R&R)
2. Vérifier le contrôle statistique (cartes de contrôle)
3. Calculer la capabilité processus
4. Conclure : Processus validé ou non ?
5. Présenter les résultats au "client" (formateur)

**Outils au choix** : Excel, Ellistat, ou R (selon préférence du groupe)

**Déroulement** :
- 1h00 : Travail en groupes
- 30 min : Présentations (5 min/groupe) + questions formateur

**Évaluation** : Ce cas pratique constitue l'évaluation sommative du Module 2

**Livrables** :
- Rapport d'analyse complet
- Graphiques et tableaux
- Présentation orale
- Conclusion go/no-go

**Critères d'évaluation** : Voir Evaluations.md

---

#### Séquence 4.8 : Clôture Module 2 et Formation CQPM (15 min) - 17h45-18h00

**Objectif** : Conclure la formation

**Contenu** :
- Synthèse du Module 2
- Liens avec le Module 1 (boucle complète : Plan de contrôle → Mesures → SPC → Capabilité → Amélioration)
- Bilan des compétences acquises
- Tour de table : retours des stagiaires
- Modalités d'évaluation CQPM si applicable
- Remise des attestations de formation

**Méthode** : Échange interactif

---

## 📊 Récapitulatif des Activités Pédagogiques

| Type d'activité | Durée totale | % du module |
|-----------------|--------------|-------------|
| Apports théoriques | 9h00 | 32% |
| Démonstrations | 4h00 | 14% |
| Travaux Pratiques | 10h30 | 38% |
| Cas pratiques | 3h00 | 11% |
| Évaluations incluses | 0h30 | 2% |
| Pauses et transitions | 1h00 | 4% |
| **TOTAL** | **28h00** | **100%** |

---

## 🎯 Compétences Validées

À l'issue du Module 2, les stagiaires maîtrisent :

✅ Calcul et interprétation des statistiques descriptives  
✅ Construction et lecture de cartes de contrôle X̄-R, X-MR  
✅ Calcul de Cm, Cmk, Cp, Cpk  
✅ Interprétation des indices de capabilité  
✅ Réalisation d'études MSA (R&R)  
✅ Utilisation d'Excel pour analyses statistiques qualité  
✅ Utilisation d'Ellistat pour SPC et capabilité  
✅ Utilisation basique de R pour analyses statistiques  
✅ Prise de décision basée sur les données  
✅ Présentation de résultats statistiques  

---

## 📚 Supports Associés

- **Module2_Guide_Formateur.md** : Notes et conseils pédagogiques
- **Module2_Support_Stagiaire.md** : Cours théorique complet
- **TP4 à TP10** : Travaux pratiques avec énoncés et corrigés
- **Cas Pratiques 3, 4, 5** : Mises en situation industrielles
- **Evaluations.md** : Grilles d'évaluation
- **Fichiers de données** : CSV et Excel pour tous les TP

---

## ✏️ Notes pour le Formateur

- **Niveau BAC/BTS** : Simplifier les formules mathématiques, privilégier l'interprétation
- **R** : Rester sur des scripts prêts à l'emploi, ne pas enseigner la programmation
- **Ellistat** : Version d'évaluation possible si licence non disponible
- **Adapter** : Utiliser des exemples du secteur d'activité des stagiaires
- **Rythme** : Prévoir du temps supplémentaire pour les stagiaires moins à l'aise avec les statistiques

---

**Fin du Module 2** ✅
