# TP4 : Statistiques Descriptives avec Excel

## 📋 Informations Générales

- **Module** : Module 2 - Statistiques et Capabilité  
- **Durée** : 2h30 (including correction)  
- **Modalité** : Travail individuel  
- **Niveau** : BAC/BTS  
- **Logiciel** : Microsoft Excel

---

## 🎯 Objectifs Pédagogiques

À l'issue de ce TP, vous serez capable de :
- ✅ Calculer les statistiques descriptives avec Excel (moyenne, écart-type, etc.)  
- ✅ Créer un histogramme avec Excel  
- ✅ Interpréter la distribution des données  
- ✅ Comparer les données aux spécifications  
- ✅ Estimer le pourcentage de non-conformes  
- ✅ Prendre des décisions basées sur l'analyse statistique

---

## 📝 Contexte Industriel

### Entreprise
**PRÉCIMECA** - Sous-traitant en usinage de précision (déjà rencontré en TP1 !)

### Situation
Vous êtes technicien(ne) qualité. La production d'axes de précision pour l'aéronautique démarre depuis 2 semaines. Le responsable production vous demande une **analyse statistique** pour vérifier que le processus est maîtrisé.

### Produit
**Axe de précision** en acier inoxydable 316L  
Référence : **AXE-AERO-2024**

### Caractéristique Critique
**Diamètre nominal : Ø 25,00 mm**  
**Tolérance : ± 0,10 mm**  
Donc : **Spécification = 24,90 à 25,10 mm**

> Cette dimension est **critique** car elle garantit l'assemblage avec d'autres composants. Un diamètre hors tolérance rend la pièce inutilisable.

### Données Disponibles
Vous disposez des **100 dernières mesures** de diamètre prises lors du contrôle final (1 mesure par pièce) sur les 5 derniers jours de production.

**Moyen de mesure** : Micromètre digital Mitutoyo, résolution 0,001 mm (système de mesure validé par MSA).

---

## 🎯 Travail Demandé

### Partie 1 : Import et Organisation des Données (10 min)

1. **Ouvrez le fichier `TP4_Donnees.xlsx`**
   - Onglet "Données_Brutes" : Les 100 mesures (colonne A : N° mesure, colonne B : Diamètre)

2. **Vérifiez les données**
   - Pas de cellule vide ?
   - Toutes les valeurs sont numériques ?
   - Valeurs cohérentes (pas de 0, pas de valeurs aberrantes évidentes) ?

3. **Créez un nouvel onglet "Analyse"**
   - C'est ici que vous ferez tous vos calculs

---

### Partie 2 : Statistiques Descriptives (30 min)

Dans l'onglet "Analyse", créez un tableau propre avec les calculs suivants :

#### 2.1 - Mesures de Tendance Centrale

Calculez (utilisez les fonctions Excel appropriées) :

| Statistique | Formule Excel | Votre résultat |
|-------------|---------------|----------------|
| **Nombre de données (n)** | `=NB(...)` | |
| **Minimum** | `=MIN(...)` | |
| **Maximum** | `=MAX(...)` | |
| **Étendue (R)** | `=MAX(...) - MIN(...)` | |
| **Moyenne (x̄)** | `=MOYENNE(...)` | |
| **Médiane** | `=MEDIANE(...)` | |
| **Mode** | `=MODE.SN(...)` | |

#### 2.2 - Mesures de Dispersion

| Statistique | Formule Excel | Votre résultat |
|-------------|---------------|----------------|
| **Variance (s²)** | `=VAR.S(...)` | |
| **Écart-type (s)** | `=ECARTYPE.STANDARD(...)` | |
| **Coefficient de variation (CV%)** | `=(Écart-type/Moyenne)*100` | |

#### 2.3 - Quartiles et Analyse de Distribution

| Statistique | Formule Excel | Votre résultat |
|-------------|---------------|----------------|
| **Q1 (1er quartile)** | `=QUARTILE.INCLUS(...; 1)` | |
| **Q3 (3ème quartile)** | `=QUARTILE.INCLUS(...; 3)` | |
| **Écart interquartile (IQR)** | `=Q3-Q1` | |

#### 2.4 - Mise en Forme

- Ajoutez des **titres clairs** à votre tableau
- Utilisez **2 à 3 décimales** pour les résultats (format nombre)
- Ajoutez les **unités** (mm) là où pertinent
- **Mettez en couleur** les valeurs clés (moyenne, écart-type)

---

### Partie 3 : Visualisation - Histogramme (40 min)

Objectif : Créer un histogramme professionnel de la distribution des diamètres.

#### 3.1 - Préparation : Déterminer les Classes

Pour un histogramme, il faut regrouper les données par "classes" (intervalles).

**Nombre de classes optimal** : Utilisez la formule de Sturges :
```
k = 1 + 3,3 × log₁₀(n)
```

Pour n = 100 : k ≈ 7 ou 8 classes

**Calcul de la largeur de classe** :
```
Largeur = (Max - Min) / k
```

Arrondissez à une valeur pratique (ex: 0,02 mm ou 0,03 mm).

➡️ **Dans Excel**, créez un tableau avec :
- Colonne "Classe" : Les intervalles (ex: 24,88-24,91 / 24,91-24,94 / etc.)
- Colonne "Borne inférieure"
- Colonne "Borne supérieure"
- Colonne "Effectif" (nombre de valeurs dans la classe)

**Astuce Excel** : Utilisez la fonction `NB.SI.ENS()` pour compter les valeurs entre deux bornes.

Exemple :
```excel
=NB.SI.ENS(Données_Brutes!B:B; ">="&Borne_inf; Données_Brutes!B:B; "<"&Borne_sup)
```

#### 3.2 - Création du Graphique Histogramme

**Méthode 1 : Graphique en barres manuel**
1. Sélectionnez vos colonnes "Classe" et "Effectif"
2. Insertion → Graphique → Histogramme (barres verticales)
3. Formatez :
   - Réduire l'espace entre les barres à 0% (histogramme = barres collées)
   - Couleur : Bleu ou vert professionnel
   - Bordures noires fines

**Méthode 2 : Outil d'analyse Excel (plus simple)**
1. Onglet "Données" → "Analyse de données"
   - Si non disponible : Fichier → Options → Compléments → Utilitaire d'analyse → Activer
2. Choisir "Histogramme"
3. Sélectionner plage de données et classes
4. Générer le graphique

#### 3.3 - Ajouter les Spécifications à l'Histogramme

**Très important** : Visualiser les limites de spécification !

1. Ajoutez deux **lignes verticales** sur le graphique :
   - **LIS** (Limite Inférieure Spécification) = 24,90 mm → Ligne rouge pointillée
   - **LSS** (Limite Supérieure Spécification) = 25,10 mm → Ligne rouge pointillée

2. Optionnel : Ajouter une **courbe normale théorique**
   - Créez une colonne avec les valeurs de la loi normale : `=LOI.NORMALE(...)`
   - Superposez cette courbe à l'histogramme

#### 3.4 - Finalisation du Graphique

Votre histogramme doit comporter :
✅ **Titre** : "Distribution des Diamètres - Axe Aéro-2024 (n=100)"  
✅ **Axe X** : "Diamètre (mm)" avec échelle visible  
✅ **Axe Y** : "Effectif (nombre de pièces)"  
✅ **Limites de spécification** en lignes rouges avec légende  
✅ **Légende** claire  
✅ **Gridlines** (quadrillage) léger pour faciliter la lecture

---

### Partie 4 : Interprétation et Analyse (40 min)

Dans un nouvel onglet "**Rapport d'Analyse**" (ou sous forme de zone de texte dans Excel), répondez aux questions suivantes de manière structurée :

#### 4.1 - Analyse de la Tendance Centrale

**Q1 : Le processus est-il centré sur la valeur nominale (25,00 mm) ?**
- Comparez la moyenne calculée à 25,00
- Écart = Moyenne - 25,00 = ?
- Conclusion : Centré / Légèrement décentré / Fortement décentré ?

**Q2 : La médiane est-elle proche de la moyenne ?**
- Si oui → distribution symétrique (proche de la normale)
- Si non → distribution asymétrique

#### 4.2 - Analyse de la Dispersion

**Q3 : Quelle est l'amplitude de variation du processus ?**
- Étendue (R) = ?
- Comparez à la tolérance totale (0,20 mm)
- La variation naturelle est-elle petite ou grande par rapport à la tolérance ?

**Q4 : L'écart-type est-il acceptable ?**
- Règle empirique : Pour un processus capable, l'écart-type devrait être tel que 6σ < Tolérance
- Calculez : 6 × s = ?
- Comparez à la tolérance (0,20 mm)
- Si 6σ < tolérance → Bon signe  
- Si 6σ > tolérance → Problème !

#### 4.3 - Analyse de la Distribution (Histogramme)

**Q5 : La distribution ressemble-t-elle à une courbe en cloche (loi normale) ?**
- Observez votre histogramme
- Forme symétrique ou asymétrique ?
- Un seul pic (unimodal) ou plusieurs pics (bimodal = alerte !) ?

**Q6 : Y a-t-il des valeurs aberrantes (outliers) ?**
- Regardez les extrêmes (min/max)
- Y a-t-il des valeurs isolées très loin du reste ?

#### 4.4 - Conformité aux Spécifications

**Q7 : Combien de pièces sont non-conformes ?**
Comptez (fonction NB.SI d'Excel) :
- Nombre de pièces < 24,90 mm (sous-dimension) = ?
- Nombre de pièces > 25,10 mm (sur-dimension) = ?
- **Total non-conformes** = ?
- **Pourcentage de rebut** = (NC / 100) × 100 = ?%

**Q8 : Le taux de non-conformes est-il acceptable ?**
- Objectif qualité en aéronautique : < 1% de rebut (idéalement < 0,5%)
- Votre résultat : ?
- Conclusion : Acceptable / Limite / Inacceptable ?

#### 4.5 - Estimation du Taux de Non-Conformes Théorique

**Q9 : Si le processus suit une loi normale, quel serait le %NC théorique ?**

Utilisez la loi normale avec votre moyenne et écart-type calculés :

**Probabilité d'être < LIS** (24,90) :
```excel
=LOI.NORMALE.STANDARD.N((24,90 - Moyenne) / Ecart_type; VRAI)
```

**Probabilité d'être > LSS** (25,10) :
```excel
=1 - LOI.NORMALE.STANDARD.N((25,10 - Moyenne) / Ecart_type; VRAI)
```

**Pourcentage total théorique de NC** = Somme des deux × 100

Comparez ce résultat théorique au % réel observé.

#### 4.6 - Recommandations

**Q10 : Quelles actions recommandez-vous ?**

En fonction de vos résultats, proposez **2 à 3 actions concrètes** parmi :

**Si décentrage** :
- ☐ Recentrer le processus (réglage outil / paramètre machine)
- ☐ Identifier la cause du décentrage (usure outil ? dérive thermique ?)

**Si dispersion excessive** :
- ☐ Réduire la variabilité (stabiliser paramètres, améliorer maintenance)
- ☐ Changer de machine / d'outil
- ☐ Formation opérateurs

**Si % NC > seuil** :
- ☐ Augmenter la fréquence de contrôle (SPC - cartes de contrôle)
- ☐ Tri des pièces produites
- ☐ Analyse de capabilité machine avant relance prod

**Si tout est OK** :
- ☐ Maintenir la surveillance
- ☐ Documenter les paramètres optimaux
- ☐ Passer en contrôle par échantillonnage

---

### Partie 5 : Synthèse - Rapport Visuel (30 min)

**Créez une "Dashboard" (Tableau de bord) visuel sur une nouvelle feuille Excel.**

Ce dashboard doit tenir sur **1 page A4 imprimable** et contenir :

1. **Titre** : "Analyse Statistique - Production Axes Aéro-2024"
2. **Indicateurs clés** (KPI) :
   - Moyenne, Écart-type ⟶ Encadrés colorés
   - % de non-conformes ⟶ **Gros chiffre visible** (conditionnel : vert si <1%, orange si 1-3%, rouge si >3%)
3. **Histogramme** avec spécifications (copié depuis Partie 3)
4. **Box Plot** (facultatif mais valorisé) :
   - Montre Min, Q1, Médiane, Q3, Max
   - Outil : Graphique → Boîte à moustaches
5. **Conclusions et recommandations** (3 points maximum, bullet points)

**Mise en forme** :
- Utilisez des couleurs cohérentes (palette professionnelle : bleu/gris/vert)
- Icônes si possible (✅ ❌ ⚠️)
- Alignement soigné

---

## 📤 Livrables Attendus

**Fichier Excel unique** : `TP4_Analyse_VotreNom.xlsx`

Avec les onglets suivants :
1. **Données_Brutes** (fourni, non modifié)
2. **Analyse** : Calculs statistiques
3. **Histogramme** : Graphique principal
4. **Rapport d'Analyse** : Réponses aux 10 questions
5. **Dashboard** : Synthèse visuelle 1 page

---

## ✅ Critères d'Évaluation

| Critère | Points | Détails |
|---------|--------|---------|
| **Calculs statistiques** | /5 | Toutes les formules correctes, résultats cohérents |
| **Histogramme** | /5 | Classes correctes, spécifications visibles, mise en forme pro |
| **Interprétation** | /6 | Réponses Q1-Q10 pertinentes et argumentées |
| **Calcul %NC** | /3 | Réel ET théorique calculés |
| **Recommandations** | /3 | Actions concrètes et adaptées aux résultats |
| **Dashboard** | /2 | Clarté, professionnalisme, synthèse efficace |
| **Rigueur et forme** | /1 | Organisation, propreté, formules Excel (pas de valeurs en dur) |
| **TOTAL** | **/25** | |

**Seuil de validation** : 15/25

---

## 💡 Conseils et Astuces Excel

### Fonctions Utiles

```excel
=MOYENNE(A2:A101)           ' Moyenne
=ECARTYPE.STANDARD(A2:A101) ' Écart-type échantillon
=VAR.S(A2:A101)             ' Variance échantillon
=MIN(A2:A101)               ' Minimum
=MAX(A2:A101)               ' Maximum
=MEDIANE(A2:A101)           ' Médiane
=QUARTILE.INCLUS(A2:A101;1) ' 1er quartile (25%)
=NB.SI(A2:A101;"<24.9")     ' Compter valeurs < 24,9
=NB.SI.ENS(A2:A101;">=24.9";A2:A101;"<25.1") ' Compter entre deux bornes
```

### Astuce : Nommer des Plages

Au lieu d'écrire `A2:A101` partout :
1. Sélectionnez A2:A101
2. Zone "Nom" (à gauche de la barre de formule) → Tapez **"Diametres"**
3. Utilisez : `=MOYENNE(Diametres)` ➡️ Plus lisible !

### Mise en Forme Conditionnelle

Pour le %NC dans le dashboard :
1. Sélectionnez la cellule du %NC
2. Accueil → Mise en forme conditionnelle → Nouvelle règle → Formule
3. Vert si <1%, Orange si 1-3%, Rouge si >3%

### Création de Graphiques Professionnels

- ❌ Évitez les couleurs criardes (rose fluo, vert pomme)
- ✅ Utilisez bleu, gris, vert foncé
- ❌ Pas d'effets 3D (illisibles)
- ✅ Graphiques 2D plats, nets
- ✅ Ajoutez des étiquettes de données si pertinent

---

## 🎯 Points Clés à Retenir

> **Concepts Fondamentaux**

1. **Moyenne** ≠ **Médiane** si distribution asymétrique
2. **Écart-type** mesure la dispersion : petit = données homogènes, grand = données dispersées
3. **6σ** représente ≈99,7% des données (si loi normale)
4. **Spécifications** (client) ≠ **Limites naturelles du processus** (6σ)
5. Un processus peut être **centré** mais **non capable** (trop de dispersion)
6. Un processus peut être **capable** mais **décentré** (décalage systématique)

> **Règle d'Or**

**Pour être "capable" :**
- ✅ Centré sur la valeur nominale (moyenne ≈ cible)
- ✅ Faible dispersion (6σ < Tolérance, idéalement 6σ < Tol/2)
- ✅ Distribution normale
- ✅ Processus stable (pas de dérive)

---

## ⏱️ Planning Conseillé

| Activité | Durée conseillée |
|----------|------------------|
| Lecture énoncé + import données | 10 min |
| Partie 2 : Calculs statistiques | 30 min |
| Partie 3 : Histogramme | 40 min |
| Partie 4 : Interprétation (Q1-Q10) | 40 min |
| Partie 5 : Dashboard | 30 min |
| Relecture et finition | 10 min |
| **TOTAL** | **2h40** (dont 10min marge) |
| Correction collective | 30 min |

---

## 📚 Ressources

### Documents Fournis
- `TP4_Donnees.xlsx` : 100 mesures de diamètres
- `TP4_Aide_Formules.pdf` : Récapitulatif formules Excel

### Références Théoriques
- Module2_Support_Stagiaire.md (Sections 1 et 2)
- Aide Excel (F1) pour syntaxe des fonctions

### Vidéos (si temps disponible)
- YouTube : "Créer un histogramme Excel" (nombreux tutos 5-10 min)
- Recherche : "Excel distribution normale"

---

## ❓ FAQ

**Q : Puis-je utiliser l'outil "Analyse de données" d'Excel ?**  
R : Oui, mais assurez-vous de comprendre ce qu'il fait. Ne pas utiliser en "boîte noire".

**Q : Mon histogramme ne ressemble pas à une courbe en cloche, est-ce grave ?**  
R : Pas forcément. Certains processus ne suivent pas une loi normale. Mentionnez-le dans votre analyse.

**Q : J'ai un %NC de 0%. Est-ce réaliste ?**  
R : Sur 100 pièces, c'est possible ! Mais attention : 0% sur 100 pièces ≠ garantie 0% sur 10 000 pièces. D'où l'intérêt du calcul théorique.

**Q : Mes calculs réels et théoriques ne correspondent pas, pourquoi ?**  
R : Normal si :
  - L'échantillon est petit (100 pièces)
  - La distribution n'est pas parfaitement normale
  - Précision de calcul

**Q : Combien de décimales afficher ?**  
R : 2-3 décimales pour les statistiques (écart-type, moyenne), 1 décimale pour les % (ex: 2,5%).

---

## 🔗 Suite Pédagogique

Ce TP est **fondamental** pour la suite du module :

- **TP5** : Vous utiliserez ces compétences pour créer des cartes de contrôle
- **TP6** : Calcul de capabilité (Cp, Cpk) basé sur moyenne et écart-type
- **Module 1** : Les données non-conformes identifiées ici pourraient déclencher des actions dans le Plan de Contrôle ou l'AMDEC

---

**Bonne analyse ! 📊**
