# Guide de Construction des Fichiers Excel TP1

## 📋 Objectif

Ce guide explique comment créer les fichiers Excel **TP1_Template.xlsx** et **TP1_Corrige.xlsx** à partir des fichiers CSV fournis.

---

## 🔧 Étape 1 : Créer TP1_Template.xlsx

### 1.1 - Ouvrir le CSV dans Excel

1. Ouvrez **TP1_Template.csv** avec Excel
2. Les colonnes doivent s'afficher correctement (séparateur = virgule)

### 1.2 - Mise en Forme de l'En-tête

**Ligne 1 (En-têtes de colonnes)** :
- Police : **Arial 11, Gras**
- Couleur de fond : **Bleu foncé (RGB: 31, 78, 120)**
- Couleur texte : **Blanc**
- Alignement : **Centré horizontal et vertical**
- Bordures : **Toutes les bordures noires épaisses**
- Hauteur de ligne : **30**

### 1.3 - Ajuster les Largeurs de Colonnes

| Colonne | Largeur |
|---------|---------|
| A (N°) | 5 |
| B (Processus/Étape) | 20 |
| C (Caractéristique) | 30 |
| D (Spécification) | 20 |
| E (Technique mesure) | 35 |
| F (Taille échantillon) | 12 |
| G (Fréquence) | 15 |
| H (Type contrôle) | 12 |
| I (Responsable) | 18 |
| J (Plan réaction) | 40 |
| K (Enregistrement) | 25 |
| L (Criticité) | 10 |

### 1.4 - Mise en Forme des Lignes de Données

**Lignes 2 à 16** :
- Police : **Arial 10**
- Alignement : **Gauche pour texte, Centré pour N° et Criticité**
- Bordures : **Grilledéfinie (toutes cellules)**
- Couleur alternée (facultatif) :
  - Lignes paires : Blanc
  - Lignes impaires : Gris très clair (RGB: 242, 242, 242)

### 1.5 - Validation des Données (Listes Déroulantes)

**Colonne H (Type de contrôle)** - Cellules H2:H16 :
- Données → Validation des données
- Liste : `Réception,En-cours,Final`

**Colonne L (Criticité)** - Cellules L2:L16 :
- Données → Validation des données
- Liste : `◆,▲,●`
- Police : **16 pt** pour cette colonne (symboles plus visibles)

### 1.6 - Protection (Optionnel)

Si vous voulez guider les stagiaires :
1. Sélectionner toute la feuille → Clic droit → Format de cellule → Protection → Décocher "Verrouillée"
2. Sélectionner uniquement ligne 1 (en-têtes) → Cocher "Verrouillée"
3. Révision → Protéger la feuille (sans mot de passe)

### 1.7 - Ajouter un Onglet "Instructions"

Créer un 2ème onglet nommé **"Instructions"** avec :

```
INSTRUCTIONS TP1 - Plan de Contrôle

1. Complétez le plan de contrôle dans l'onglet "Plan_Controle"
2. Remplissez TOUTES les colonnes pour chaque ligne
3. Identifiez au minimum 4 caractéristiques critiques (◆)
4. Utilisez les listes déroulantes pour Type de contrôle et Criticité

Légende Criticité :
◆ = Critique (sécurité/fonction principale)
▲ = Significative (impact client)
● = Standard

Conseils :
- Soyez précis sur les techniques de mesure (avec références/résolutions)
- Plans de réaction = actions concrètes (qui fait quoi ?)
- Adaptez les fréquences à la production (≈200 pièces/jour)
```

Mise en forme : Texte simple, lisible, police 11.

### 1.8 - Enregistrer

**Fichier → Enregistrer sous → TP1_Template.xlsx** (format Excel)

---

## ✅ Étape 2 : Créer TP1_Corrige.xlsx

### 2.1 - Ouvrir le CSV Corrigé

1. Ouvrez **TP1_Corrige.csv** avec Excel
2. Les 23 lignes de données remplies doivent apparaître

### 2.2 - Appliquer la Même Mise en Forme que le Template

Reproduisez exactement les étapes 1.2 à 1.5 de la section précédente :
- En-tête bleu
- Largeurs de colonnes identiques
- Bordures et alternance de couleurs

### 2.3 - Mise en Évidence des Caractéristiques Critiques

**Pour toutes les lignes où Criticité = ◆** :
- Couleur de fond de la ligne : **Jaune clair (RGB: 255, 242, 204)**
- OU Bordure gauche épaisse rouge (3 pt)

Cela permet de repérer visuellement les points critiques.

### 2.4 - Ajouter Onglet "Notes Formateur"

Créer un 3ème onglet **"Notes_Formateur"** avec :

```
CORRIGÉ TP1 - Notes pour le Formateur

Ce plan de contrôle contient 23 points de contrôle répartis sur les 7 étapes :
- 3 contrôles réception (matière première)
- 16 contrôles en-cours (processus)
- 4 contrôles finaux

CARACTÉRISTIQUES CRITIQUES (◆) : 11 au total
Issues de l'AMDEC avec IPR > 100 :
- Diamètre perçages (découpe laser)
- Angles de pliage zones A et B
- Filetage M6 (profondeur + fonctionnalité + couple)
- Couverture peinture

Autres critiques ajoutées :
- Épaisseur tôle (réception)
- Entraxe perçages
- Vérification dimensions critiques (final)
- Essai fonctionnel

POINTS DE VIGILANCE CORRECTION :
✓ Les moyens de mesure sont précis (modèle, résolution)
✓ Les fréquences sont réalistes (production 200 pcs/jour)
✓ Les plans de réaction sont actionnables
✓ La traçabilité est assurée (enregistrements nommés)
✓ Les 3 types de contrôle sont représentés

VARIANTES ACCEPTABLES :
- Fréquences légèrement différentes (si justifiées)
- Moyens de mesure équivalents
- Plans de réaction formulés différemment (mais complets)
- Ajout de contrôles supplémentaires pertinents

À SANCTIONNER :
❌ Caractéristiques AMDEC (IPR > 100) non identifiées comme critiques
❌ Moyens de mesure inadaptés (règle pour Ø avec tolérance ±0.2mm)
❌ Plans de réaction vagues ("corriger", "voir responsable")
❌ Absence de contrôle réception
❌ Fréquences incohérentes (ex: 1/minute pour production 25 pcs/h)
```

### 2.5 - Formules Automatiques (Optionnel Avancé)

Si vous voulez rendre le fichier plus "intelligent" :

**Colonne M** : "Nb contrôles/jour (estimation)"
- Formule exemple pour ligne 2 :
```excel
=SI(G2="Par bobine";"Variable";SI(G2="Toutes les heures";8;SI(G2="Continu";"100%";"À calculer")))
```

Adaptez selon les fréquences.

### 2.6 - Enregistrer

**Fichier → Enregistrer sous → TP1_Corrige.xlsx**

---

## 📊 Résultat Final

Vous devez avoir **3 fichiers** :

1. **TP1_Template.csv** → Base de travail (fourni)
2. **TP1_Template.xlsx** → Pour les stagiaires (vierge, formaté)
3. **TP1_Corrige.xlsx** → Pour le formateur (complété, annoté)

---

## 🎨 Captures d'Écran Recommandées (si possible)

Pour enrichir le guide :
- Screenshot de l'en-tête formaté
- Screenshot d'une ligne complète avec validation
- Screenshot des caractéristiques critiques surlignées

---

## ⚡ Raccourcis Gain de Temps

### Copier la Mise en Forme
1. Formater parfaitement la première ligne de données (ligne 2)
2. Sélectionner ligne 2 → Copier (Ctrl+C)
3. Sélectionner lignes 3 à 16 → Clic droit → Collage spécial → Formats

### Validation en Masse
1. Sélectionner toute la colonne H (H2:H100 par exemple)
2. Créer la validation une seule fois
3. Elle s'appliquera à toutes les cellules sélectionnées

---

## 🔍 Vérification Qualité

Avant de distribuer les fichiers, vérifiez :

**TP1_Template.xlsx** :
- [ ] En-têtes bien formatés
- [ ] Colonnes à la bonne largeur
- [ ] Listes déroulantes fonctionnelles
- [ ] Onglet Instructions présent et clair
- [ ] Pas de données pré-remplies (sauf noms étapes)

**TP1_Corrige.xlsx** :
- [ ] Toutes les 23 lignes complètes
- [ ] 11 caractéristiques critiques (◆) identifiées
- [ ] Mise en évidence visuelle des critiques
- [ ] Onglet Notes Formateur complet
- [ ] Cohérence globale (fréquences, moyens, criticités)

---

## ❓ Questions Fréquentes

**Q : Pourquoi CSV puis Excel ?**  
R : Le CSV permet de versionner facilement (Git) et de partager la structure. L'Excel apporte la mise en forme professionnelle.

**Q : Puis-je modifier la structure (colonnes) ?**  
R : Oui, mais mettez à jour le TP1_Plan_Controle_Excel.md en conséquence (descriptions colonnes).

**Q : Les stagiaires peuvent-ils utiliser le CSV directement ?**  
R : Déconseillé, le formatage Excel guide mieux et évite les erreurs de saisie (listes déroulantes).

---

**Temps de création estimé** :
- TP1_Template.xlsx : 15-20 minutes
- TP1_Corrige.xlsx : 20-25 minutes
- **Total : 40-45 minutes**

Bon travail ! 📝
