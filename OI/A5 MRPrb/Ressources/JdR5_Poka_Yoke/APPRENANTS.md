# 🎭 JdR n°5 - Le "Poka-Yoke" Salvateur

## 📋 DOCUMENT POUR LES APPRENANTS

**⚠️ Ne lisez PAS le kit complet du formateur avant de jouer !**

---

## 🎬 Votre Mission

Vous travaillez sur une ligne d'assemblage de connecteurs hydrauliques. Depuis 6 mois, **15% des pièces arrivent au contrôle final avec des joints toriques inversés** (rouge au lieu de noir).

**Le problème** :

- Les opérateurs sont formés et compétents
- Les consignes sont affichées au poste
- Les rappels sont faits chaque matin
- **Mais l'erreur persiste !**

**Votre équipe doit** :

- Comprendre pourquoi les formations ne suffisent pas
- Concevoir une solution technique anti-erreur (Poka-Yoke)
- Budget maximum : **500€**

---

## 👥 Vos Rôles (4 joueurs)

### 🔧 L'INGÉNIEUR MÉTHODES

**Votre situation** :

- Vous devez proposer une solution technique
- Vous connaissez les principes du Poka-Yoke
- Vous voulez une solution robuste et pérenne

**Votre objectif** : Concevoir un système qui rend l'erreur impossible

---

### 👷 L'OPÉRATEUR EXPÉRIMENTÉ (Claire M. - 8 ans d'ancienneté)

**Votre situation** :

- Vous faites cette opération depuis des années
- En début de poste vous faites attention, mais après 2-3h c'est automatique
- Les joints se ressemblent TROP
- Vous avez des idées simples mais personne ne vous écoute

**Votre objectif** : Partager votre expérience terrain

---

### 🔨 LE TECHNICIEN MAINTENANCE

**Votre situation** :

- Vous devrez entretenir la solution proposée
- Vous préférez les solutions simples et robustes
- Vous craignez les systèmes électroniques complexes

**Votre objectif** : Valider la faisabilité et la maintenabilité

---

### 💰 LE MINIMALISTE (joué par le FORMATEUR)

**Votre rôle** :

- Vous proposez des solutions compliquées et coûteuses
- Vous parlez de capteurs, vision industrielle, automates...
- Vous détournez l'équipe des solutions simples

---

## 🎯 Contexte Technique

### Les Joints Toriques

**Caractéristiques** :

- Joint ROUGE : NBR (Nitrile) - circuit haute pression
- Joint NOIR : EPDM - circuit basse pression
- Diamètre : 12.0 mm (identique)
- Section : 2.0 mm (identique)
- **Différence** : UNIQUEMENT la couleur !

**Le problème** :

- En cadence (18 pièces/heure), l'opérateur prend sans regarder
- Les bacs sont transparents et côte à côte
- Sous l'éclairage atelier, différence rouge/noir subtile
- L'erreur n'est détectée qu'après assemblage complet

---

## 📊 Données Statistiques

### Taux d'erreur par opérateur (Décembre 2025)

| Opérateur | Expérience | Défauts | Taux |
|-----------|-----------|---------|------|
| Claire M. | 8 ans | 102/680 | 15.0% |
| Ahmed K. | 5 ans | 78/520 | 15.0% |
| Lucie P. | 12 ans | 68/450 | 15.1% |
| Thomas R. | 2 ans | 75/500 | 15.0% |

**Observation critique** : Le taux est identique pour TOUS, même les plus expérimentés !

→ Ce n'est PAS un problème de compétence  
→ C'est un problème de CONCEPTION DU POSTE

---

## 🛠️ Outils à Votre Disposition

### Grille d'Analyse Poka-Yoke

```
┌────────────────────────────────────────────────┐
│     GRILLE D'ANALYSE SOLUTION POKA-YOKE       │
└────────────────────────────────────────────────┘

Solution proposée : ____________________________

┌──────────────┬─────┬─────┬─────┬─────┐
│   CRITÈRE    │  1  │  2  │  3  │  4  │
├──────────────┼─────┼─────┼─────┼─────┤
│ EFFICACITÉ   │     │     │     │     │
│ (empêche     │Faible│Moyen│ Bon │Excell│
│  erreur)     │     │     │     │     │
├──────────────┼─────┼─────┼─────┼─────┤
│ SIMPLICITÉ   │     │     │     │     │
│ (facile à    │     │     │     │     │
│  utiliser)   │     │     │     │     │
├──────────────┼─────┼─────┼─────┼─────┤
│ COÛT         │>500€│300- │100- │<100€│
│              │     │500€ │300€ │     │
├──────────────┼─────┼─────┼─────┼─────┤
│ MAINTENANCE  │Comp│Régul│Faible│Aucune│
│              │lexe│ière │     │     │
├──────────────┼─────┼─────┼─────┼─────┤
│ DÉLAI MISE   │>1mois│2-4│1 sem│1 jour│
│ EN ŒUVRE     │     │sem │     │     │
└──────────────┴─────┴─────┴─────┴─────┘

SCORE TOTAL : ____ / 20

Recommandation :
> 16 → Excellente solution
12-16 → Acceptable
< 12 → À retravailler
```

---

## 💡 Principes Poka-Yoke à Connaître

### Types de Poka-Yoke

1. **Physique** : Empêche physiquement l'erreur
   - Exemple : Connecteur USB (ne rentre que dans un sens)

2. **Visuel** : Rend l'erreur immédiatement visible
   - Exemple : Code couleur, formes différentes

3. **Séquentiel** : Force un ordre d'opération
   - Exemple : Carte bancaire (retrait impossible avant fin paiement)

4. **Détection** : Alerte en cas d'erreur
   - Exemple : Alarme ceinture non attachée

### Règle d'Or

**Les meilleures solutions sont souvent les plus SIMPLES !**

- Préférer le visuel au procédural
- Préférer le physique au comportemental
- Préférer la prévention à la détection

---

## 📋 Cahier des Charges

### Contraintes OBLIGATOIRES

✅ **DOIT** :

- Empêcher ou réduire drastiquement l'erreur
- Fonctionner même si opérateur distrait/fatigué
- Coûter **moins de 500€**
- Ne PAS ralentir la cadence (18 pièces/heure min)
- Être simple (pas de formation complexe)

❌ **NE DOIT PAS** :

- Nécessiter système informatique complexe
- Dépendre de l'éclairage
- Se détériorer rapidement
- Nécessiter maintenance fréquente

---

## 💭 Questions à se Poser en Équipe

1. Pourquoi les formations ne suffisent-elles pas ?
2. Qu'est-ce qui rend l'erreur possible actuellement ?
3. Comment pourrait-on rendre l'erreur IMPOSSIBLE ?
4. Quelle est la solution la plus SIMPLE ?
5. Peut-on tester rapidement un prototype ?

---

## ⏱️ Déroulé Suggéré

**Durée totale** : 50 minutes

- 0-10 min : Brainstorming libre (toutes les idées)
- 10-20 min : Analyse avec grille (2-3 solutions)
- 20-30 min : Sélection de la solution optimale
- 30-45 min : Schéma/prototype de la solution
- 45-50 min : Présentation à l'équipe

---

## ✅ Critères de Réussite

Votre équipe aura réussi si :

- ✅ Vous proposez une solution SIMPLE (pas high-tech)
- ✅ Votre solution coûte moins de 500€
- ✅ Elle empêche physiquement ou visuellement l'erreur
- ✅ Elle est facile à mettre en œuvre (< 1 semaine)
- ✅ Elle ne nécessite aucune maintenance

---

## ⚠️ Pièges à Éviter

- ❌ Chercher des solutions high-tech coûteuses
- ❌ Proposer "encore plus de formation"
- ❌ Accuser les opérateurs de manque d'attention
- ❌ Solutions avec capteurs/ordinateurs/vision
- ❌ Complexifier au lieu de simplifier

---

## 💡 Inspiration

Pensez à des Poka-Yoke du quotidien :

- Prise électrique (terre en haut, impossible à l'envers)
- Carte SIM (coin coupé, un seul sens possible)
- Distributeur de billets (carte ressort avant billets)
- Bouchon d'essence (taille différente diesel/essence)

**Principe** : Rendre l'erreur physiquement ou visuellement impossible !

---

**Bon jeu de rôle ! 🎭**

*Rappelez-vous : Le meilleur Poka-Yoke est celui qui rend l'erreur IMPOSSIBLE, pas celui qui la détecte !*
