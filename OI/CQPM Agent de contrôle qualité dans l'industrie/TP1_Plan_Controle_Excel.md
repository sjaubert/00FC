# TP1 : Création d'un Plan de Contrôle avec Excel

## 📋 Informations Générales

- **Module** : Module 1 - Plans de Contrôle et Gammes de Contrôle
- **Durée** : 2h15 (incluant correction)
- **Modalité** : Individuel ou binômes
- **Niveau** : BAC/BTS
- **Logiciel** : Microsoft Excel

---

## 🎯 Objectifs Pédagogiques

À l'issue de ce TP, vous serez capable de :
- ✅ Analyser un processus de fabrication
- ✅ Identifier les caractéristiques à contrôler
- ✅ Créer un plan de contrôle APQP structuré
- ✅ Définir des méthodes de contrôle appropriées
- ✅ Établir des plans de réaction

---

## 📝 Contexte Industriel

### Entreprise
Vous travaillez pour **PRÉCIMECA**, un équipementier automobile de rang 2 spécialisé dans la fabrication de pièces métalliques de fixation.

### Client
Votre client est un constructeur automobile exigeant qui impose le référentiel **IATF 16949** (qualité automobile).

### Produit
**Support de fixation métallique** référence **SF-2024-A**

**Usage** : Fixation de composants électroniques sous le tableau de bord

**Quantité** : 50 000 pièces/an (série moyenne)

**Exigences particulières** :
- Pièce d'aspect (visible par le client final lors de maintenance)
- Fonction critique : Tenue mécanique
- Traçabilité par lot obligatoire

---

## 🏭 Processus de Fabrication

Le support est fabriqué selon le processus suivant :

### Étape 1 : Réception Matière Première
- **Entrant** : Tôle acier S235JR (ép. 2 mm) en bobine
- **Fournisseur** : ARCELORMITTAL
- **Documents associés** : Certificat matière 3.1

### Étape 2 : Découpe Laser
- **Moyen** : Découpe laser fibre TRUMPF 3000 W
- **Opération** : Découpe du contour et des 3 perçages Ø6,5 mm
- **Paramètres critiques** : Puissance, vitesse, gaz assist

### Étape 3 : Pliage
- **Moyen** : Presse plieuse AMADA 80 tonnes
- **Opération** : Pliage à 90° sur deux zones
- **Paramètres critiques** : Force, position matrice, angle

### Étape 4 : Taraudage
- **Moyen** : Taraudeuse automatique
- **Opération** : Création filetage M6 sur 2 trous
- **Paramètres critiques** : Profondeur, couple

### Étape 5 : Traitement de Surface
- **Moyen** : Ligne de cataphorèse
- **Opération** : Dégraissage → Phosphatation → Cataphorèse noire
- **Paramètres critiques** : Temps immersion, température bains, pH

### Étape 6 : Contrôle Final
- **Opération** : Contrôle dimensionnel, visuel, fonctionnel
- **Décision** : Acceptation ou�� rebut

### Étape 7 : Conditionnement
- **Opération** : Emballage par lots de 100 en carton
- **Traçabilité** : Étiquette N° lot + date

---

## 📐 Spécifications Critiques

### Dimensions (extrait du plan)

| N° | Caractéristique | Spécification | Tolérance | Criticité |
|----|-----------------|---------------|-----------|-----------|
| 1 | Longueur totale | 120 mm | ± 0,5 mm | ▲ |
| 2 | Largeur | 40 mm | ± 0,3 mm | ● |
| 3 | Épaisseur tôle | 2 mm | ± 0,1 mm | ◆ |
| 4 | Ø perçages (x3) | Ø 6,5 mm | +0,2 / 0 mm | ◆ |
| 5 | Entraxe perçages | 60 mm | ± 0,15 mm | ◆ |
| 6 | Angle de pliage zone A | 90° | ± 2° | ◆ |
| 7 | Angle de pliage zone B | 90° | ± 2° | ◆ |
| 8 | Filetage M6 (x2) | M6 - 6H | ISO | ◆ |
| 9 | Couple de serrage filetage | ≥ 8 N.m | Mini | ◆ |
| 10 | Épaisseur cataphorèse | 15-25 μm | - | ▲ |
| 11 | Aspect peinture | Visuel | 0 défaut | ▲ |

**Légende criticité** :
- ◆ : Caractéristique critique (sécurité ou fonction principale)
- ▲ : Caractéristique significative (impact client)
- ● : Caractéristique standard

### Caractéristiques issues de l'AMDEC

Une AMDEC processus a été réalisée (voir Module 1 - Séquence 2.2). Les modes de défaillance avec **IPR > 100** sont :

1. **Découpe** : Dimension perçage hors tolérance (IPR = 144)
2. **Pliage** : Angle non-conforme (IPR = 120)
3. **Taraudage** : Filetage arraché / incomplet (IPR = 180)
4. **Cataphorèse** : Manque de peinture (zones non couvertes) (IPR = 108)

Ces caractéristiques doivent impérativement apparaître comme **critiques (◆)** dans le plan de contrôle.

---

## 🎯 Travail Demandé

### Partie 1 : Analyse Préparatoire (20 min)

Avant d'ouvrir Excel, répondez aux questions suivantes sur papier :

1. **Identification des caractéristiques à contrôler**
   - Listez toutes les caractéristiques qui doivent être contrôlées (minimum 10)
   - Classez-les par criticité

2. **Positionnement des contrôles**
   - À quelle(s) étape(s) du processus faut-il contrôler chaque caractéristique ?
   - Y a-t-il des caractéristiques à contrôler plusieurs fois ?

3. **Méthodes de contrôle**
   - Quel moyen de mesure pour les dimensions ?
   - Comment vérifier les filetages ?
   - Comment contrôler l'aspect peinture ?

4. **Échantillonnage**
   - Contrôle à 100% ou par échantillonnage ? Justifier pour 3 caractéristiques différentes

### Partie 2 : Création du Plan de Contrôle sur Excel (1h30)

Utilisez le template fourni **TP1_Template.xlsx**

Le template contient les colonnes suivantes (respecter cette structure) :

| Colonne | Description |
|---------|-------------|
| **N°** | Numéro séquentiel |
| **Processus / Étape** | Nom de l'étape de fabrication |
| **Caractéristique à contrôler** | Nom précis de la caractéristique |
| **Spécification / Tolérance** | Valeur nominale ± tolérance |
| **Technique de mesure** | Méthode et moyen (ex: Pied à coulisse) |
| **Taille échantillon** | Nombre de pièces à contrôler |
| **Fréquence** | À quelle fréquence ? (ex: 1/heure) |
| **Type de contrôle** | Réception / En-cours / Final |
| **Responsable** | Fonction (ex: Opérateur, Contrôleur) |
| **Plan de réaction** | Que faire si non-conforme ? |
| **Enregistrement** | Nom du document d'enregistrement |
| **Criticité** | ◆ / ▲ / ● |

**Consignes** :

1. **Compléter au minimum 15 lignes** (couvrant l'ensemble du processus)

2. **Identifier au moins 4 caractéristiques critiques (◆)**
   - Les 4 issues de l'AMDEC sont obligatoires
   - Possibilité d'en ajouter d'autres

3. **Diversifier les types de contrôle**
   - Au moins 1 contrôle réception
   - Au moins 8 contrôles en-cours
   - Au moins 3 contrôles finaux

4. **Définir des fréquences réalistes**
   - Tenir compte de la production (≈200 pièces/jour)
   - Adapter selon la criticité

5. **Plans de réaction précis**
   - Ne pas écrire "Corriger" ou "Voir responsable"
   - Spécifier : Qui fait quoi ? Isolation ? Tri ? Lot complet ou pièce ?

6. **Moyens de mesure**
   - Spécifier précisément (pas seulement "règle" mais "Pied à coulisse digital ±0,01mm")

### Partie 3 : Cas Particuliers à Traiter (20 min)

Après avoir complété le plan de contrôle de base, traitez les 3 cas suivants :

#### Cas A : Nouveau Fournisseur de Tôle
Le fournisseur d'acier habituel est en rupture. Vous devez utiliser temporairement un nouveau fournisseur non qualifié.

**Question** : Quels contrôles renforcés ajouteriez-vous ? Modifiez votre plan de contrôle en conséquence.

#### Cas B : Dérive Détectée sur le Pliage
Les cartes de contrôle montrent une dérive sur l'angle de pliage depuis 2 jours.

**Question** : Proposez une modification temporaire du plan de contrôle pendant la période de surveillance renforcée.

#### Cas C : Demande Client d'Audit
Le client automobile demande à auditer votre processus la semaine prochaine.

**Question** : Votre plan de contrôle est-il complet ? Qu'est-ce qui pourrait manquer selon vous ?

---

## 📤 Livrables Attendus

À remettre au formateur :

1. **Fichier Excel** : `TP1_VotreNom.xlsx`
   - Plan de contrôle complété (minimum 15 lignes)
   - Mise en forme soignée
   - Formules si pertinent (ex: calcul automatique de fréquence horaire en pièces/lot)

2. **Document d'analyse** (fichier Word ou dans l'onglet "Analyse" du fichier Excel) :
   - Réponses à la Partie 1 (analyse préparatoire)
   - Réponses aux 3 cas particuliers (Partie 3)
   - Justification de vos choix principaux (200-300 mots)

3. **Présentation orale** (si demandé par le formateur) :
   - 5 minutes
   - Expliquer votre logique
   - Mettre en avant les points clés

---

## ✅ Critères d'Évaluation

| Critère | Points | Détails |
|---------|--------|---------|
| **Complétude** | /4 | Au moins 15 lignes, toutes les étapes couvertes |
| **Criticité** | /3 | Les 4 caractéristiques AMDEC identifiées comme critiques |
| **Moyens de mesure** | /3 | Précis et adaptés (pas de moyens inadaptés) |
| **Fréquences** | /2 | Réalistes et justifiées |
| **Plans de réaction** | /4 | Précis, actionnables, responsabilités claires |
| **Traçabilité** | /2 | Enregistrements spécifiés |
| **Cas particuliers** | /3 | 3 cas traités de manière pertinente |
| **Forme et clarté** | /2 | Présentation professionnelle |
| **Justifications** | /2 | Argumentation cohérente |
| **TOTAL** | **/25** | |

**Seuil de validation** : 15/25 (60%)

---

## 📚 Ressources Disponibles

### Documents Fournis
- `TP1_Template.xlsx` : Template Excel avec colonnes pré-formatées
- `TP1_Plan_Piece.pdf` : Plan technique de la pièce (dimensions détaillées)
- `TP1_AMDEC_Extrait.pdf` : Extrait de l'AMDEC Processus

### Documents de Référence
- Module1_Support_Stagiaire.md (Sections 2 et 3)
- Norme IATF 16949:2016 (extrait fourni)
- AIAG APQP Manual (extrait)

### Aide Formateur
- Le formateur est disponible pour questions de compréhension
- Pas d'aide sur le contenu du plan (travail en autonomie)

---

## 💡 Conseils et Astuces

### Pour Réussir le TP

1. **Lisez tout l'énoncé avant de commencer** 📖
   - Comprenez le processus global
   - Identifiez les informations clés

2. **Pensez "risque"** ⚠️
   - Les caractéristiques critiques sont celles où l'échec a le plus d'impact
   - Référez-vous à l'AMDEC

3. **Soyez précis** 🎯
   - "Contrôler la dimension" → ❌ Trop vague
   - "Contrôler le Ø des 3 perçages avec pied à coulisse digital Mitutoyo (résolution 0,01mm)" → ✅ Précis

4. **Plans de réaction actionnables** 🚨
   - ❌ "Prévenir le responsable"
   - ✅ "Arrêt production + isolation lot + tri 100% par contrôleur qualité + information chef d'équipe"

5. **Cohérence des fréquences** 📅
   - Production : ≈200 pièces/jour soit ≈25 pièces/heure (ligne en 8h)
   - "Contrôle toutes les heures" = 8 contrôles/jour OK
   - "Contrôle toutes les 10 minutes" = 48 contrôles/jour → Irréaliste pour pièce standard

6. **Distinguez contrôle/surveillance** 👁️
   - Contrôle : Mesure précise avec enregistrement
   - Surveillance : Monitoring visuel/sensoriel (ex: écoute bruit machine)

### Pièges à Éviter

❌ Oublier le contrôle réception matière  
❌ Ne contrôler qu'au final (trop tard !)  
❌ Mettre la même fréquence partout  
❌ Prévoir des moyens de mesure inexistants ou inadaptés  
❌ Confondre limites de spécification et limites de contrôle SPC  
❌ Ne pas différencier les criticités  

---

## 🔗 Liens avec les Autres TP

- **TP2 (AMDEC)** : L'AMDEC alimente le plan de contrôle
- **TP3 (Gamme de contrôle)** : La gamme détaille les instructions du plan de contrôle
- **Module 2 (TP5, TP6)** : Les données collectées selon ce plan alimenteront les cartes de contrôle et études de capabilité

---

## ⏱️ Planning Conseillé

| Activité | Durée | Timing |
|----------|-------|--------|
| Lecture énoncé + questions | 15 min | 0:00 - 0:15 |
| Analyse préparatoire (Partie 1) | 20 min | 0:15 - 0:35 |
| Création plan de contrôle Excel (Partie 2) | 1h30 | 0:35 - 2:05 |
| Cas particuliers (Partie 3) | 20 min | 2:05 - 2:25 |
| Relecture et finalisation | 10 min | 2:25 - 2:35 |
| **TOTAL TRAVAIL** | **2h35** | (dont 20min marge) |
| Correction collective | 30 min | Après remise |

---

## 📊 Corrigé Type (Formateur Uniquement)

📁 Voir fichier **TP1_Corrige.xlsx** pour un exemple de plan de contrôle complet.

**Points clés du corrigé** :

1. **Contrôle réception tôle** : Épaisseur, certificat matière 3.1, aspect
2. **Contrôle post-découpe** : Dimensions perçages (critique), contour
3. **Contrôle post-pliage** : Angles (critique), cotes après formage
4. **Contrôle post-taraudage** : Fonctionnalité filetage avec calibre GO/NO-GO (critique), couple
5. **Contrôle post-cataphorèse** : Épaisseur peinture, aspect, adhérence
6. **Contrôle final** : Vérification dimensionnelle récapitulative, fonctionnelle (vissage), aspect global

---

## ❓ FAQ

**Q1 : Faut-il tout contrôler à 100% ?**  
R : Non. Réfléchissez au rapport coût/bénéfice. Les caractéristiques critiques (◆) peuvent justifier un contrôle 100% ou très fréquent. Les autres peuvent être par échantillonnage.

**Q2 : Les fréquences doivent-elles être en temps (1/h) ou en quantité (1/50 pièces) ?**  
R : Les deux sont acceptables. Privilégiez le temps pour les processus continus, la quantité pour les lots.

**Q3 : Que mettre dans "Enregistrement" si pas d'enregistrement ?**  
R : En qualité automobile (IATF 16949), tout contrôle doit être enregistré. Indiquez le nom du support : "Fiche contrôle réception FR-Q-01", "Carte de contrôle Ø perçages", etc.

**Q4 : Peut-on avoir plusieurs lignes pour une même étape ?**  
R : Oui, absolument. Une étape peut avoir multiples caractéristiques à contrôler. Exemple : "Pliage" peut avoir 5 lignes (angle zone A, angle zone B, cote hauteur, etc.).

**Q5 : Combien de temps pour ce TP en réel ?**  
R : Travail efficace : 1h45-2h00. Avec analyse et cas : 2h15-2h30. Correction : +30min.

---

## 📞 Contact

En cas de difficulté technique (fichier Excel, etc.), contacter le formateur.

Pour questions de compréhension de l'énoncé : relire attentivement puis formateur si persistance.

---

**Bon travail ! 💪**
