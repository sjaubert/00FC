# Kit d'Indices - Jeu de Rôle n°2 : "Méthode 8D en Crise"

## 📋 Contexte de la Mission

**Date** : 16 janvier 2026  
**Heure de convocation** : 09h00  
**Urgence** : ⚠️⚠️⚠️ CRITIQUE - Client majeur menace de rupture contrat  
**Produit** : Pièce usinée référence PU-3847-B (axe de transmission)  
**Client** : AutoTech Industries (30% de notre CA)  
**Problème** : 3ème retour en 2 mois pour côtes hors tolérances

---

## 📊 INDICE 1 : Historique des Réclamations Client

```
RÉCLAMATIONS CLIENT - AutoTech Industries
Produit : PU-3847-B (Axe de transmission Ø50mm)

┌─────────────┬──────────┬──────────────┬─────────────────────┐
│    Date     │ N° Lot   │ Qté retour   │  Motif              │
├─────────────┼──────────┼──────────────┼─────────────────────┤
│ 15/11/2025  │ L-2511A  │   45/200     │ Ø hors tolérance    │
│             │          │              │ (+0.18mm)           │
├─────────────┼──────────┼──────────────┼─────────────────────┤
│ 08/12/2025  │ L-2512B  │   38/200     │ Ø hors tolérance    │
│             │          │              │ (+0.12mm)           │
├─────────────┼──────────┼──────────────┼─────────────────────┤
│ 12/01/2026  │ L-2601A  │   52/200     │ Ø hors tolérance    │
│             │          │              │ (+0.15mm)           │
└─────────────┴──────────┴──────────────┴─────────────────────┘

📧 DERNIER EMAIL CLIENT (13/01/2026) :
"Cette situation est inacceptable. Nous exigeons un rapport 8D 
complet d'ici 5 jours avec actions correctives et préventives 
démontrées. Sans cela, nous serons contraints de chercher un 
nouveau fournisseur."

⚠️ ENJEU : Contrat de 2.5M€/an en jeu
```

---

## 📋 INDICE 2 : Spécifications Techniques

```
PLAN DE DEFINITION - PU-3847-B
────────────────────────────────────────────────

Axe de transmission - Acier 42CrMo4 traité

CÔTE CRITIQUE : Ø50.00mm ± 0.10mm
                (Tolérance : 49.90 à 50.10mm)

PROCESS :
1. Ébauche sur Tour CN T1 → Ø50.50mm
2. Traitement thermique (trempe)
3. Finition sur Tour CN (T1, T2 ou T3) → Ø50.00 ±0.10

Cadence : 200 pièces/semaine
Contrôle : 20% des pièces (contrôle statistique)

NOTE QUALITÉ :
"Les dépassements constatés (+0.12 à +0.18mm) dépassent 
largement la tolérance. Origine à déterminer."
```

---

## 📊 INDICE 3 : Données de Production (2 derniers mois)

```
PRODUCTION PU-3847-B - Nov 2025 à Jan 2026

┌────────────┬─────────┬─────────┬──────────┬──────────────┐
│    Date    │  Tour   │  Lot    │ Qté      │ Taux rebut   │
├────────────┼─────────┼─────────┼──────────┼──────────────┤
│ 10/11/2025 │   T1    │ L-2511A │   200    │   0%         │
│ 17/11/2025 │   T2    │ L-2511B │   200    │   0%         │
│ 24/11/2025 │   T1    │ L-2511C │   200    │   0%         │
│ 01/12/2025 │   T3    │ L-2512A │   200    │   0%         │
│ 08/12/2025 │   T2    │ L-2512B │   200    │   0%         │
│ 15/12/2025 │   T1    │ L-2512C │   200    │   0%         │
│ 22/12/2025 │   T3    │ L-2512D │   200    │   0%         │
│ 05/01/2026 │   T1    │ L-2601A │   200    │   0%         │
│ 12/01/2026 │   T2    │ L-2601B │   200    │   0%         │
└────────────┴─────────┴─────────┴──────────┴──────────────┘

⚠️ OBSERVATION :
Tous les contrôles en sortie production sont OK !
Les défauts sont détectés uniquement chez le client.
```

---

## 🔍 INDICE 4 : Relevés de Mesures Chez le Client

```
MESURES EFFECTUÉES PAR AutoTech Industries

LOT L-2511A (Premier retour - 15/11/2025)
─────────────────────────────────────────
Pièces mesurées : 45/200 NOK
Moyenne Ø : 50.18mm (au lieu de 50.00 ± 0.10)
Écart : +0.18mm

LOT L-2512B (Deuxième retour - 08/12/2025)
──────────────────────────────────────────
Pièces mesurées : 38/200 NOK
Moyenne Ø : 50.12mm
Écart : +0.12mm

LOT L-2601A (Troisième retour - 12/01/2026)
───────────────────────────────────────────
Pièces mesurées : 52/200 NOK
Moyenne Ø : 50.15mm
Écart : +0.15mm

💡 QUESTION CLÉ :
Pourquoi nos mesures sont OK et celles du client NOK ?
```

---

## 📋 INDICE 5 : Planning d'Occupation des Tours

```
PLANNING UTILISATION TOURS - Nov 2025 à Jan 2026

TOUR T1 (Ancien modèle, 1998)
─────────────────────────────
✓ Utilisé pour : L-2511A, L-2511C, L-2512C, L-2601A
✓ Disponibilité : 80%
✓ Opérateur principal : Claude M.

TOUR T2 (Modèle intermédiaire, 2010)
────────────────────────────────────
✓ Utilisé pour : L-2511B, L-2512B, L-2601B
✓ Disponibilité : 85%
✓ Opérateur principal : Sarah L.

TOUR T3 (Récent, 2020)
──────────────────────
✓ Utilisé pour : L-2512A, L-2512D
✓ Disponibilité : 90%
✓ Opérateur principal : Thomas R.

NOTE MÉTHODES :
"Les 3 tours sont réglés avec les mêmes paramètres selon 
la gamme opératoire standard."
```

---

## 🔍 INDICE 6 : Corrélation Lots Défectueux / Tours

> **[À construire par l'équipe - exercice de corrélation]**

**Lots retournés par le client** :

- L-2511A → Tour ?
- L-2512B → Tour ?
- L-2601A → Tour ?

**Question** : Y a-t-il un pattern ?

---

## 📋 INDICE 7 : Fiches de Réglage des 3 Tours

```
PARAMÈTRES DE RÉGLAGE - Opération Finition Ø50mm

┌────────────────────┬─────────┬─────────┬─────────┐
│    Paramètre       │   T1    │   T2    │   T3    │
├────────────────────┼─────────┼─────────┼─────────┤
│ Vitesse (tr/min)   │  1200   │  1200   │  1200   │
│ Avance (mm/tour)   │  0.15   │  0.15   │  0.15   │
│ Profondeur passe   │  0.25mm │  0.25mm │  0.25mm │
│ Outil (plaquette)  │ CNMG120│ CNMG120 │ CNMG120 │
│ Arrosage           │  Oui    │  Oui    │  Oui    │
└────────────────────┴─────────┴─────────┴─────────┘

✅ CONFORMITÉ : Tous les paramètres conformes à la gamme
```

---

## 🌡️ INDICE 8 : Données Environnementales

> **[À demander explicitement par l'équipe]**

```
RELEVÉS TEMPÉRATURE ATELIER - Période Nov-Jan

┌────────────────┬──────────┬──────────┬──────────┐
│  Emplacement   │   Nov    │   Déc    │   Jan    │
├────────────────┼──────────┼──────────┼──────────┤
│ Zone Tour T1   │  18°C    │  16°C    │  14°C    │
│ Zone Tour T2   │  20°C    │  18°C    │  17°C    │
│ Zone Tour T3   │  22°C    │  22°C    │  22°C    │
│ Salle contrôle │  20°C    │  20°C    │  20°C    │
└────────────────┴──────────┴──────────┴──────────┘

NOTE :
T1 est proche d'un portail d'expédition (courants d'air)
T2 est dans la zone centrale
T3 est dans une zone climatisée (installation récente)

⚠️ RAPPEL MÉTALLURGIE :
Coefficient de dilatation acier : 11.7 × 10⁻⁶ /°C
Pour Ø50mm et ΔT=6°C → Variation ≈ +0.0035mm

Mais sur 200mm de longueur : 
ΔL = 200 × 11.7×10⁻⁶ × 6 ≈ 0.014mm (négligeable)

💡 Donc la température seule n'explique PAS les +0.15mm
```

---

## 🔧 INDICE 9 : Historique Maintenance Tours

```
TOUR T1 (1998) - Dernières interventions
────────────────────────────────────────
05/10/2025 : Maintenance préventive annuelle
           - Vérification géométrie ✓
           - Compensation usure ✗ (Non faite - oubli)
           - Graissage ✓

TOUR T2 (2010)
──────────────
12/11/2025 : Maintenance préventive semestrielle
           - Vérification complète ✓
           - Compensation usure ✓

TOUR T3 (2020)
──────────────
20/12/2025 : Maintenance préventive
           - Contrôle machine neuve ✓
           - Aucun défaut détecté
```

---

## 📋 INDICE 10 : Procédure de Contrôle Qualité

```
PROCÉDURE DE CONTRÔLE - PU-3847-B

1. CONTRÔLE EN PRODUCTION (20% des pièces)
   ├─ Instrument : Pied à coulisse numérique
   ├─ Localisation : Poste de travail (à côté du tour)
   └─ Température ambiante : Variable selon zone

2. CONTRÔLE CHEZ LE CLIENT
   ├─ Instrument : Colonne de mesure 3D
   ├─ Localisation : Salle métrologie climatisée 20°C
   └─ Température contrôlée : 20°C ± 1°C

⚠️ DIFFÉRENCE CRITIQUE :
Nos pièces sont mesurées CHAUDES (juste après usinage)
Pièces client mesurées FROIDES (en salle climatisée)

💡 CALCUL DILATATION THERMIQUE :
Si pièce mesurée à 20°C → Ø50.00mm (conforme)
Si même pièce mesurée à 14°C → Ø50.00 - δ

Δ Température Tour T1 : 14°C (hiver)
Δ Pièce juste après usinage : ~35-40°C (friction + chaleur)
Différence de température : ΔT ≈ 25°C

Calcul contraction au refroidissement :
δ = 50 × 11.7×10⁻⁶ × 25 = 0.0146mm ≈ 0.015mm

⚠️ MAIS : Si la pièce est chaude au contrôle production,
elle est dilatée → on mesure trop grand → on valide NOK !

HYPOTHÈSE : Tour T1 chauffe plus que les autres (vieux modèle)
→ Pièces chaudes au contrôle
→ Mesurées Ø50.00mm alors qu'elles font réellement 49.85mm froides
→ Client mesure à froid → détecte hors tolérance
```

---

## 📊 INDICE 11 : Test de Validation (Si équipe demande)

```
EXPÉRIENCE DEMANDÉE PAR L'ÉQUIPE 8D
───────────────────────────────────

Protocole :
1. Produire 10 pièces sur Tour T1
2. Mesurer immédiatement (< 2 min après usinage)
3. Laisser refroidir 2h en salle climatisée
4. Mesurer à nouveau

RÉSULTATS :
┌──────────┬─────────────────┬─────────────────┬─────────┐
│  Pièce   │ Mesure CHAUDE   │ Mesure FROIDE   │  Écart  │
├──────────┼─────────────────┼─────────────────┼─────────┤
│    1     │   50.02mm       │   49.88mm       │ -0.14mm │
│    2     │   50.01mm       │   49.86mm       │ -0.15mm │
│    3     │   50.03mm       │   49.89mm       │ -0.14mm │
│    4     │   50.00mm       │   49.87mm       │ -0.13mm │
│    5     │   50.02mm       │   49.88mm       │ -0.14mm │
└──────────┴─────────────────┴─────────────────┴─────────┘

✅ CONFIRMATION : Pièces T1 hors tolérance à froid !
Cause : Dilatation thermique non compensée au contrôle
```

---

## 📋 INDICE 12 : Diagramme Ishikawa (5M) - Template Vierge

```
                      PROBLÈME : Pièces hors tolérance chez client
                                        │
        ┌──────────────────────────────┼──────────────────────────────┐
        │                              │                              │
    MATIÈRE                        MÉTHODE                        MILIEU
        │                              │                              │
        │                              │                              │
        │                              │                              │
        └──────────────────────────────┼──────────────────────────────┘
                                       │
        ┌──────────────────────────────┼──────────────────────────────┐
        │                              │                              │
    MAIN D'ŒUVRE                   MACHINES                       MESURES
        │                              │                              │
        │                              │                              │
        │                              │                              │
        └──────────────────────────────┴──────────────────────────────┘

À REMPLIR PAR L'ÉQUIPE
```

---

## 🎯 FICHE 8D (Template à Remplir)

```
┌────────────────────────────────────────────────────────────┐
│                 RAPPORT 8D - FICHE VIERGE                  │
└────────────────────────────────────────────────────────────┘

D0 - PRÉPARATION
────────────────
□ Problème identifié : ____________________________________
□ Urgence justifiant 8D : _________________________________
□ Équipe formée (qui ?) : __________________________________

D1 - CONSTITUER L'ÉQUIPE
────────────────────────
Membres :                           Rôle :
1. ____________________________  │ ________________________
2. ____________________________  │ ________________________
3. ____________________________  │ ________________________
4. ____________________________  │ ________________________
5. ____________________________  │ ________________________

Leader 8D : _____________________________________________

D2 - DÉCRIRE LE PROBLÈME
────────────────────────
Utiliser QQOQCP :

QUI ?    : _________________________________________________
QUOI ?   : _________________________________________________
OÙ ?     : _________________________________________________
QUAND ?  : _________________________________________________
COMMENT ?: _________________________________________________
COMBIEN ?: _________________________________________________
POURQUOI?: _________________________________________________

D3 - METTRE EN PLACE DES ACTIONS DE CONFINEMENT
────────────────────────────────────────────────
Actions immédiates pour protéger le client :
□ _________________________________________________________
□ _________________________________________________________
□ _________________________________________________________

Date de mise en œuvre : _____________
Efficacité vérifiée : □ OUI  □ NON

D4 - IDENTIFIER LA CAUSE RACINE
───────────────────────────────
Utiliser : Ishikawa (5M) + 5 Pourquoi

Cause racine identifiée :
_____________________________________________________________

Preuves / Vérifications :
_____________________________________________________________

D5 - DÉFINIR LES ACTIONS CORRECTIVES PERMANENTES
─────────────────────────────────────────────────
┌─────────────────┬─────────────┬──────────┬──────────┐
│     Action      │Responsable  │  Délai   │  Statut  │
├─────────────────┼─────────────┼──────────┼──────────┤
│                 │             │          │          │
│                 │             │          │          │
│                 │             │          │          │
└─────────────────┴─────────────┴──────────┴──────────┘

D6 - METTRE EN ŒUVRE LES ACTIONS CORRECTIVES
─────────────────────────────────────────────
Date de déploiement : _______________
Plan de validation : _______________________________________

D7 - PRÉVENIR LA RÉCURRENCE (ACTIONS PRÉVENTIVES)
──────────────────────────────────────────────────
□ Modifier procédure : ____________________________________
□ Former personnel : ______________________________________
□ Mettre à jour documentation : ___________________________
□ Partager retour d'expérience : __________________________

D8 - FÉLICITER L'ÉQUIPE
───────────────────────
Date de clôture : _______________
Reconnaissance : ___________________________________________
```

---

## 🎯 SOLUTION ATTENDUE (Pour le Formateur)

### Analyse par la Méthode 8D

#### D0 - PRÉPARATION

- **Problème** : 3 réclamations client en 2 mois, pièces hors tolérance
- **Urgence** : Contrat 2.5M€/an en jeu, ultimatum client 5 jours

#### D1 - ÉQUIPE

- Leader 8D : Responsable Qualité
- Production (chef d'atelier)
- Méthodes (ingénieur process)
- Métrologie (technicien contrôle)
- Maintenance (technicien)

#### D2 - DESCRIPTION (QQOQCP)

- **QUI** : Client AutoTech Industries
- **QUOI** : Pièces PU-3847-B, Ø hors tolérance (+0.12 à +0.18mm)
- **OÙ** : Lots L-2511A, L-2512B, L-2601A
- **QUAND** : Nov-Dec-Jan, intermittent
- **COMMENT** : 20-25% des pièces de certains lots
- **COMBIEN** : 135 pièces sur 600 (22.5%)
- **POURQUOI** : À déterminer (cause racine)

#### D3 - CONFINEMENT

**Actions immédiates** :

1. Bloquer tous les stocks en cours (inspection 100%)
2. Contrôler à FROID toutes les pièces avant expédition
3. Envoyer pièces de remplacement au client (express)
4. Inspecter 100% production Tour T1 tant que problème non résolu

#### D4 - CAUSE RACINE

**Ishikawa (5M)** :

- **MATIÈRE** : Acier conforme (écarter)
- **MÉTHODE** : Procédure de contrôle inadaptée ⚠️
- **MILIEU** : Température atelier variable (T1 zone froide) ⚠️
- **MAIN D'ŒUVRE** : Opérateurs formés (écarter)
- **MACHINES** : Tour T1 ancien modèle ⚠️
- **MESURES** : Contrôle à chaud vs froid ⚠️⚠️

**5 Pourquoi** :

1. Pourquoi pièces hors tolérance ? → Ø trop grand de +0.15mm à froid
2. Pourquoi Ø trop grand ? → Pièces validées OK à chaud mais NOK à froid
3. Pourquoi validées à chaud ? → Contrôle fait immédiatement après usinage
4. Pourquoi contrôler à chaud ? → Procédure ne spécifie pas d'attendre refroidissement
5. Pourquoi procédure inadaptée ? → Dilatation thermique non prise en compte

**CAUSE RACINE** :
Procédure de contrôle inadaptée : mesure sur pièces chaudes au lieu de froides, combinée à une dilatation thermique significative sur Tour T1 (zone non climatisée).

#### D5 - ACTIONS CORRECTIVES

**Action 1** : Modifier procédure contrôle

- Imposer refroidissement 30 min avant contrôle
- OU contrôler en salle métrologie climatisée
- Responsable : Responsable Qualité
- Délai : 2 jours

**Action 2** : Installer Tour T1 en zone climatisée

- OU installer un système de refroidissement forcé pièces
- Responsable : Maintenance
- Délai : 1 mois

**Action 3** : Compenser usure Tour T1 (oubliée en Oct)

- Recalibrage machine
- Responsable : Maintenance
- Délai : Immédiat

#### D6 - MISE EN ŒUVRE

- Nouvelle procédure diffusée : 18/01/2026
- Formation opérateurs : 19/01/2026
- Test de validation : 100 pièces contrôlées selon nouvelle procédure

#### D7 - PRÉVENTION

- ✅ Procédure contrôle mise à jour (référence PC-047 v2.0)
- ✅ Formation de tous les opérateurs (fiche émargement)
- ✅ Audit trimestriel respect procédure
- ✅ Partage REX à toutes les lignes de production
- ✅ Checklist maintenance : compensation usure obligatoire

#### D8 - CLÔTURE

- Rapport 8D envoyé au client : 20/01/2026 (dans les délais !)
- Félicitations équipe pour résolution rapide
- Prime de performance équipe 8D

---

## ⏱️ Déroulé Pédagogique Attendu

| Temps | Phase | Action Équipe |
|-------|-------|---------------|
| 0-10 min | D0-D1 | Constitution équipe, lecture problème |
| 10-20 min | D2 | Remplissage QQOQCP |
| 20-30 min | D3 | Définition actions confinement |
| 30-45 min | D4 | Construction Ishikawa + hypothèses |
| 45-50 min | Piège | Tentation d'accuser Tour T1 seul |
| 50-60 min | D4 | Découverte delta thermique (demande test) |
| 60-75 min | D5-D6 | Plan d'actions correctives |
| 75-90 min | D7-D8 | Actions préventives + clôture |

---

## 📝 Points de Débriefing

### Erreurs Fréquentes ❌

1. **Sauter des étapes** : Aller directement aux solutions (D6) sans analyser (D4-D5)
2. **Cause symptôme** : Accuser "Tour T1 défaillant" au lieu de "procédure contrôle inadaptée"
3. **Oublier D3** : Ne pas protéger le client immédiatement
4. **Oublier D7** : Corriger sans prévenir la récurrence
5. **Action partielle** : Réparer Tour T1 sans changer procédure contrôle

### Messages Clés 💡

> "La méthode 8D est un marathon, pas un sprint. Chaque discipline a son importance."

> "La cause racine est rarement la première cause identifiée. Creusez avec les 5 Pourquoi !"

> "D3 (confinement) est vital : protéger le client pendant qu'on cherche la vraie cause."

> "D7 (prévention) transforme un problème en opportunité d'amélioration durable."

---

**Durée totale du jeu** : 90 minutes  
**Débriefing** : 45 minutes  

*Kit créé pour la formation Méthode 8D - Résolution Structurée*  
*Pôle Formation UIMM - CVDL*
