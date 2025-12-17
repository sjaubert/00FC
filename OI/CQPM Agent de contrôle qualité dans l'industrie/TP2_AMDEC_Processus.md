# TP2 : Réaliser une AMDEC Processus

## 📋 Informations Générales

- **Module** : Module 1 - Plans de Contrôle et Gammes de Contrôle  
- **Durée** : 2h00 (incluant correction)  
- **Modalité** : Binômes  
- **Niveau** : BAC/BTS  
- **Logiciel** : Microsoft Excel

---

## 🎯 Objectifs Pédagogiques

À l'issue de ce TP, vous serez capable de :
- ✅ Conduire une AMDEC Processus méthodiquement  
- ✅ Identifier les modes de défaillance potentiels  
- ✅ Coter objectivement G, O, D  
- ✅ Calculer l'IPR (Indice de Priorité de Risque)  
- ✅ Proposer un plan d'action priorisé  
- ✅ Mettre à jour le Plan de Contrôle en conséquence

---

## 📝 Contexte Industriel

### Entreprise
Vous travaillez pour **PLASTINNOV**, PME spécialisée dans l'injection plastique pour l'industrie automobile et électroménager.

###Client  
Client historique : **WHIRLPOOL** (électroménager)  
Nouveau produit : Façade de lave-linge (pièce d'aspect visible)

### Enjeu
- Premier contrat avec ce client prestigieux → Image de marque critique  
- Volume : 20 000 pièces/mois  
- Exigence : **0 défaut aspect** (pièce visible par le consommateur final)  
- Pénalités contractuelles si taux de rebut > 2%

### Situation
Vous êtes l'équipe qualité. Le directeur vous demande de réaliser une **AMDEC processus** AVANT le lancement en série prévu dans 1 mois.

> **Objectif** : Identifier et prévenir les risques qualité pour réussir le lancement !

---

## 🏭 Processus d'Injection Plastique - Description

### Vue d'Ensemble

```
[Matière première] → [Préparation] → [Injection] → [Refroidissement] → 
[Éjection] → [Ébavurage] → [Contrôle] → [Conditionnement]
```

### Étape 1 : Préparation Matière Première

**Opération** : Séchage des granulés de plastique (ABS)

**Description** :
- Les granulés d'ABS arrivent en sacs de 25 kg
- Ils doivent être séchés dans une étuve à 80°C pendant 4 heures minimum
- L'humidité résiduelle doit être < 0,05%
- Si pas assez séchés → risque de bulles, aspect mat

**Paramètres process** :
- Température étuve : 80°C ± 5°C
- Durée séchage : 4h minimum
- Contrôle humidité : Testeur Karl Fischer

**Moyens** :
- Étuve PIOVAN (2 étuves disponibles)
- Contrôleur d'hygrométrie

---

### Étape 2 : Réglage Presse à Injecter

**Opération** : Paramétrage de la presse injection

**Description** :
- Presse ENGEL 250 tonnes
- Moule 2 empreintes (2 pièces par cycle)
- Temps de cycle nominal : 45 secondes/pièce
- Réglages multiples : températures, pressions, vitesses, temps

**Paramètres critiques** :
- Température matière : 220-240°C (4 zones)
- Pression injection : 800-1200 bars
- Vitesse injection : 50-80 mm/s
- Temps de maintien : 3-5 s

**Moyens** :
- Automate presse (écran tactile)
- Protocole de réglage validé
- Gamme de réglage référence : GR-FAC-001

**Risques connus** :
- Mauvais réglages → pièces courtes, bavures, gauchissement, retassures

---

### Étape 3 : Injection

**Opération** : Injection de la matière dans le moule

**Description** :
- Fermeture moule (force 250 T)
- Injection ABS fondu dans l'empreinte
- Compactage
- Début refroidissement

**Durée** : ≈10-15 secondes

**Paramètres surveillés** :
- Pression injection réelle
- Matière injectée (volume)
- Temps de remplissage

**Risques spécifiques** :
- Injection incomplète → pièce courte
- Surpression → bavures
- Injection décentrée → dissymétrie

---

### Étape 4 : Refroidissement

**Opération** : Solidification de la pièce dans le moule

**Description** :
- Le moule est refroidi par circulation d'eau (15°C)
- Durée : 25-30 secondes
- La pièce se solidifie et se rétracte

**Paramètres critiques** :
- Température eau refroidissement : 15°C ± 2°C
- Débit d'eau
- Homogénéité refroidissement (canaux dans le moule)

**Risques** :
- Refroidissement trop rapide → tensions internes, criques
- Refroidissement trop lent → temps cycle augmenté, déformation
- Refroidissement non homogène → gauchissement, retrait différentiel

---

### Étape 5 : Éjection

**Opération** : Extraction de la pièce du moule

**Description** :
- Ouverture moule
- Éjecteurs poussent la pièce hors empreinte
- La pièce tombe sur tapis convoyeur

**Paramètres** :
- Force d'éjection (réglable)
- Vitesse d'éjection
- Nombre de coups d'éjecteurs

**Risques** :
- Éjection difficile (pièce collée) → traces d'éjecteurs, déformation
- Éjection trop brutale → pièce cassée
- Pièce tombe mal → rayures

---

### Étape 6 : Ébavurage

**Opération** : Retrait de la carotte et des bavures

**Description** :
- Opérateur coupe manuellement la carotte (reste de matière du canal d'injection)
- Retrait des micro-bavures au niveau du plan de joint si nécessaire
- Outillage : pince coupante, cutter

**Paramètres** :
- Dextérité opérateur
- Qualité de l'outillage

**Risques** :
- Coupe mal faite → cicatrice visible, aspect dégradé
- Oubli bavure → non-conformité
- Marquage pièce avec outil → rayure

---

### Étape 7 : Contrôle Visuel

**Opération** : Inspection aspect

**Description** :
- Contrôle visuel 100% par opérateur qualité
- Vérification : brillance, couleur, bulles, rayures, bavures, traces
- Éclairage normalisé (2000 lux, lumière du jour)

**Critères d'acceptation** :
- 0 bulle visible
- 0 rayure > 2 mm
- 0 différence de teinte
- 0 trace d'éjecteur visible à 50 cm

**Risques** :
- Contrôle subjectif (fatigue, variation inter-opérateurs)
- Éclairage inadapté → défauts non détectés
- Cadence élevée → contrôle bâclé

---

### Étape 8 : Conditionnement

**Opération** : Emballage et stockage

**Description** :
- Pièces OK placées dans cartons avec intercalaires mousse (protection rayures)
- 50 pièces/carton
- Étiquetage : N° lot, date, quantité

**Risques** :
- Pièces mal protégées → rayures transport
- Cartons mal empilés → écrasement
- Erreur étiquetage → traçabilité perdue

---

## 🎯 Travail Demandé

### Partie 1 : Préparation - Identification des Défaillances (20 min)

En binôme, sur papier ou tableau, faire un brainstorming :

**Pour chacune des 8 étapes, listez :**
1. Au moins **2 modes de défaillance potentiels** différents
2. Pour chacun, l'**effet** sur le produit/client
3. La ou les **causes racines** possibles

**Exemple pour l'étape "Séchage" :**

| Mode de défaillance | Effet | Cause(s) |
|---------------------|-------|----------|
| Granulés insuffisamment séchés | Bulles dans la pièce → rebut aspect | Durée séchage < 4h / Température trop basse / Étuve défaillante |

➡️ À reproduire pour les 7 autres étapes (complétez votre propre tableau)

---

### Partie 2 : AMDEC Processus sur Excel (1h15)

Utilisez le fichier **TP2_AMDEC.xlsx** fourni.

#### Structure du fichier Excel

Le template contient les colonnes suivantes :

| Colonne | Description | Détails |
|---------|-------------|---------|
| **Étape processus** | Nom de l'étape | Ex: "3. Injection" |
| **Fonction** | Que doit faire l'étape ? | Ex: "Remplir l'empreinte avec ABS" |
| **Mode de défaillance** | Comment peut-elle échouer ? | Ex: "Injection incomplète" |
| **Effet(s)** | Conséquence sur produit/client | Ex: "Pièce courte → rebut" |
| **Gravité (G)** | Cotation 1-10 | 10 = critique client |
| **Cause(s)** | Pourquoi la défaillance ? | Ex: "Pression injection trop faible" |
| **Occurrence (O)** | Cotation 1-10 | 10 = très fréquent |
| **Détection actuelle** | Moyen de détection en place | Ex: "Contrôle visuel 100%" |
| **Détection (D)** | Cotation 1-10 | 10 = indétectable |
| **IPR** | G × O × D | Calculé automatiquement |
| **Action recommandée** | Que faire pour réduire IPR ? | Précis et actionnable |
| **Responsable** | Qui mène l'action ? | Fonction |
| **Échéance** | Délai | Date ou durée |

#### Grilles de Cotation

**Gravité (G)** :

| Note | Critère | Description |
|------|---------|-------------|
| 9-10 | Critique | Danger sécurité OU non-conformité majeure client OU rebut certain |
| 7-8 | Majeure | Impact fonctionnel important, client mécontent |
| 4-6 | Modérée | Défaut mineur, impact limité |
| 1-3 | Mineure | Défaut sans impact client |

**Occurrence (O)** :

| Note | Probabilité | Indice |
|------|-------------|--------|
| 9-10 | Très élevée | Défaut quasi systématique (> 1/10 pièces) |
| 7-8 | Élevée | Défaut fréquent (1/100 à 1/10) |
| 4-6 | Modérée | Défaut occasionnel (1/1000 à 1/100) |
| 1-3 | Faible | Défaut rare (< 1/1000) |

**Détection (D)** :

| Note | Capacité | Description |
|------|----------|-------------|
| 9-10 | Très faible | Indétectable ou détection tardive (chez client) |
| 7-8 | Faible | Détection difficile, contrôle non systématique |
| 4-6 | Moyenne | Détection possible par contrôle dédié |
| 1-3 | Élevée | Détection automatique ou évidente |

#### Consignes de Remplissage

1. **Complétez minimum 15 lignes** (modes de défaillance) réparties sur les 8 étapes
   - Certaines étapes peuvent avoir 1 ligne, d'autres 3-4 (selon les risques)

2. **Cotez G, O, D** de manière cohérente
   - Justifiez vos choix (utilisez la colonne "Commentaire" si disponible dans le template)

3. **Calculez l'IPR** (normalement automatique via formule Excel)

4. **Identifiez les priorités** :
   - IPR > 125 : Action OBLIGATOIRE
   - 75 < IPR < 125 : Action recommandée
   - IPR < 75 : Surveillance

5. **Proposez des actions** pour tous les IPR > 75
   - ❌ Mauvais : "Améliorer le processus"
   - ✅ Bon : "Installer alarme température étuve + check visuel opérateur chaque 2h + instruction IT-003"

---

### Partie 3 : Plan d'Action Priorisé (15 min)

Dans un nouvel onglet Excel nommé "**Plan Action**", créez un tableau récapitulatif :

**Colonnes** :
- N° action
- Mode de défaillance concerné
- IPR initial
- Action corrective/préventive
- Responsable
- Échéance
- IPR cible (après action)

**Classez par IPR décroissant**

**Identifiez les 3 actions prioritaires** les plus critiques.

---

### Partie 4 : Lien avec le Plan de Contrôle (10 min)

**Question** : Parmi les modes de défaillance avec IPR > 100, lesquels doivent impérativement figurer comme caractéristiques **critiques (◆)** dans le plan de contrôle ?

**Travail** :
- Listez-les (minimum 4)
- Pour chacun, indiquez :
  * À quelle étape du processus le contrôler ?
  * Quel moyen de contrôle ?
  * Quelle fréquence ?

➡️ Vous pouvez compléter ceci dans un onglet "**Lien Plan Contrôle**"

---

## 📤 Livrables Attendus

1. **Fichier Excel** : `TP2_AMDEC_VotreNom.xlsx`
   - Onglet "AMDEC" : Tableau complété (min 15 lignes)
   - Onglet "Plan Action" : Actions priorisées
   - Onglet "Lien Plan Contrôle" : Caractéristiques critiques identifiées

2. **Présentation orale** (1 groupe tiré au sort) :
   - 5-7 minutes
   - Présenter les 3 risques majeurs identifiés
   - Justifier les cotations
   - Expliquer les actions prioritaires

---

## ✅ Critères d'Évaluation

| Critère | Points | Détails |
|---------|--------|---------|
| **Identification défaillances** | /4 | Pertinence et exhaustivité (15 lignes min, réparties sur toutes les étapes) |
| **Cotation G** | /3 | Cohérence avec impact client |
| **Cotation O** | /3 | Réalisme (basé sur données ou expérience du processus) |
| **Cotation D** | /3 | Cohérence avec moyens de détection décrits |
| **Calcul IPR** | /1 | Formules correctes |
| **Actions proposées** | /5 | Pertinence, précision, actionnables, priorisées |
| **Plan action structuré** | /2 | Tableau clair et priorisé |
| **Lien plan de contrôle** | /3 | Caractéristiques critiques bien identifiées |
| **Forme et rigueur** | /1 | Professionnalisme du document |
| **TOTAL** | **/25** | |

**Seuil de validation** : 15/25

---

## 💡 Conseils pour Réussir

### Méthodologie

1. **Travailler étape par étape** 🔄
   - Ne sautez pas d'étapes du processus
   - Chaque étape a ses risques spécifiques

2. **Mettre le "chapeau client"** 👤
   - Pour coter la Gravité, pensez : "Si je suis le client final (consommateur), quel impact ?"
   - Une bulle sur façade visible = G très élevée (9-10)

3. **Différencier Effet et Cause** ⚠️
   - Effet = Conséquence sur le PRODUIT/CLIENT
   - Cause = Raison RACINE du mode de défaillance
   - Ne pas confondre !

4. **Privilégier les actions préventives** 🛡️
   - Mieux vaut empêcher la défaillance (↓ Occurrence) que mieux la détecter
   - Détecter ne réduit pas l'occurrence, seulement le risque client

5. **Penser "poka-yoke"** 🔒
   - Détrompeurs, alarmes, contrôles automatiques
   - Exemple : Capteur humidité dans étuve avec alarme si > 0,05%

### Pièges à Éviter

❌ Coter toutes les Gravités à 10 (manque de discernement)  
❌ Confondre Occurrence et urgence  
❌ Proposer "Formation opérateur" pour tout (action générique)  
❌ Ne pas calculer l'IPR cible après action  
❌ Oublier des étapes du processus  
❌ Durée excessive de remplissage (si > 1h30 sur Partie 2, vous êtes trop lents !)

---

## 📊 Exemple de Ligne AMDEC (Référence)

| Étape | Fonction | Mode défaillance | Effet | G | Cause | O | Détection | D | IPR | Action |
|-------|----------|------------------|-------|---|-------|---|-----------|---|-----|--------|
| 1. Préparation | Sécher granulés ABS | Séchage insuffisant (humidité > 0,05%) | Bulles dans pièce → Rebut (aspect) | 9 | Durée < 4h OU T° étuve basse | 6 | Test humidimètre (1 fois/jour) | 7 | **378** | ⚠️ Installer alarme temps + Contrôle auto humidité toutes les 2h avec enregistrement |

➡️ IPR de 378 = **CRITIQUE** → Action immédiate obligatoire !

---

## 🔗 Liens avec les Autres Activités

- **TP1** : Le plan de contrôle créé en TP1 doit intégrer les caractéristiques critiques issues de cette AMDEC
- **Module 2 (Capabilité)** : Les caractéristiques critiques identifiées ici feront l'objet d'études de capabilité
- **Amélioration continue** : L'AMDEC est un document vivant, à mettre à jour régulièrement

---

## ⏱️ Planning Conseillé

| Activité | Durée | Timing Cumulé |
|----------|-------|---------------|
| Lecture énoncé + compréhension processus | 15 min | 0:15 |
| Partie 1 : Brainstorming défaillances | 20 min | 0:35 |
| Partie 2 : Remplissage AMDEC Excel | 1h15 | 1:50 |
| Partie 3 : Plan d'action | 15 min | 2:05 |
| Partie 4 : Lien plan de contrôle | 10 min | 2:15 |
| Relecture et finalisation | 10 min | 2:25 |
| **Correction collective** | 30 min | Après rendu |

---

## 📚 Ressources

### Documents Fournis
- `TP2_AMDEC.xlsx` : Template Excel AMDEC
- `TP2_Processus_Schema.pdf` : Schéma synoptique du processus
- `TP2_Grilles_Cotation.pdf` : Grilles G-O-D détaillées

### Références
- Module1_Support_Stagiaire.md (Section 4 : AMDEC)
- Norme NF EN 60812 (AMDEC)
- AIAG FMEA Manual 4th edition (automotive)

---

## ❓ FAQ

**Q : Faut-il remplir TOUTES les colonnes du template ?**  
R : Oui, toutes les colonnes obligatoires (étape, mode, effet, G, cause, O, détection, D, IPR, action si IPR > 75).

**Q : Combien de modes de défaillance par étape ?**  
R : Variable. Certaines étapes critiques peuvent en avoir 3-4, d'autres 1-2. Minimum 15 au total.

**Q : Peut-on avoir le même mode de défaillance mais avec des causes différentes ?**  
R : Oui ! Créez alors 2 lignes distinctes (même mode, causes différentes, cotations potentiellement différentes).

**Q : Comment choisir entre réduire O ou réduire D ?**  
R : Priorité : Réduire O (prévention) > Réduire G (conception) > Réduire D (détection). Ne réduire que D est la moins bonne option.

**Q : L'IPR cible peut-il être 0 ?**  
R : Non. Tout processus a un risque résiduel. Un IPR cibleréaliste est souvent entre 20 et 80 pour les risques maîtrisés.

---

**Bon travail ! 🚀**
