![Logo UIMM](logo_uimm_placeholder.jpg)

**Pôle Formation UIMM - CVDL**

---

# Atelier Cocotte LEAN — « L'Excellence par le Flux »

## Livret Participant

> [!IMPORTANT]
> **Objectif de la journée** : Découvrir les fondamentaux du LEAN à travers une simulation pratique de fabrication de cocottes en papier. Vous allez comparer trois modes de production (flux poussé, flux tiré Kanban, optimisé Kaizen) et constater par vous-même l'impact sur le Lead Time, le WIP, la qualité et le bien-être.

<div style="page-break-before: always;"></div>

## 1. Matériel à votre disposition

### Par participant

- 100 feuilles A4 blanches (80 g/m²)

### Par ligne de production

- 1 chronomètre
- 1 tableau d'indicateurs vierge (format A3)
- Des marqueurs de couleur
- Cartes Kanban (rouge = occupé, verte = disponible) — 2 par poste

<div style="page-break-before: always;"></div>

## 2. Fiche d'Instruction Standard (FIP) — Fabrication de la Cocotte

> **Objectif** : Produire une cocotte symétrique, fonctionnelle et esthétique.
>
> **Matériel** : 1 feuille A4 blanche (80 g/m²).

### 2.1 Phase Préparatoire : Obtenir un Carré Parfait

> [!TIP]
> La majorité des rebuts viennent d'un carré mal coupé. Cette phase est critique !

1. **Le Triangle d'Or** : Prenez le coin supérieur gauche et rabattez-le sur le bord droit pour former un triangle rectangle isocèle.
2. **L'Élimination du Muda** : Découpez (ou déchirez proprement le long du pli) la bande rectangulaire restante.
3. **Résultat** : Vous obtenez un carré parfait de **210 × 210 mm**.

### 2.2 Étapes de Pliage

| Étape | Action | Points clés |
|:-----:|:-------|:------------|
| **1** | **Les Diagonales** | Marquer les deux plis en croix en repliant coin à coin. |
| **2** | **Le 1er Blintz** | Rabattre les 4 coins vers le point central — les bords ne doivent pas se chevaucher. |
| **3** | **Le Retournement** | Retourner la feuille, face lisse vers vous. **Crucial** pour la cinématique d'ouverture. |
| **4** | **Le 2ème Blintz** | Rabattre les 4 nouveaux coins vers le centre. Appuyer fort sur chaque pli. |
| **5** | **Le Pré-formage** | Plier le carré en deux (horizontal) puis en deux (vertical). Bien marquer les plis. |
| **6** | **L'Ouverture** | Glisser les doigts dans les 4 poches et pousser vers le centre. Ne pas déchirer le papier. |

### 2.3 Schéma Visuel du Pliage

![Plan de pliage de la cocotte en 12 étapes](Plan_Cocotte_simple.jpg)

<div style="page-break-before: always;"></div>

## 3. Description des 5 Postes de Travail

Chaque ligne de production est organisée en **5 postes séquentiels**. Votre équipe nomme un **responsable d'équipe** et un **contrôleur qualité** (au Poste 5).

| Poste | Opérations | Temps indicatif |
|:-----:|:-----------|:---------------:|
| **P1** | Formation du carré (triangle, découpe, vérification 210 × 210 mm) | ~25 s |
| **P2** | Diagonales + 1er Blintz (4 coins au centre, face recto) | ~35 s |
| **P3** | Retournement + 2ème Blintz (4 coins au centre, face verso) | ~40 s |
| **P4** | Pré-formage (pli horizontal + pli vertical) | ~20 s |
| **P5** | Ouverture (mise en volume) + **Contrôle Qualité** | ~30 s |

<div style="page-break-before: always;"></div>

## 4. Critères de Contrôle Qualité

Pour être déclarée **« Conforme »**, chaque cocotte doit passer les 3 critères suivants :

| # | Critère | Description | Méthode de contrôle |
|:-:|:--------|:------------|:--------------------|
| 1 | **Symétrie** | Les 4 pointes doivent être de même hauteur | Poser la cocotte, vérifier visuellement l'alignement |
| 2 | **Mobilité** | S'ouvre et se ferme sans résistance | Actionner 3 fois la cocotte dans les deux axes |
| 3 | **Propreté** | Absence de déchirures ou de traces de doigts excessives | Inspection visuelle |

**Cocotte non conforme** → Comptabilisée comme **défaut** dans les KPI.

<div style="page-break-before: always;"></div>

## 5. Calcul des Indicateurs (KPI)

### 5.1 Production Totale et Taux de Qualité

$$
\text{Taux de Qualité} = \frac{\text{Cocottes conformes}}{\text{Cocottes terminées}} \times 100\%
$$

### 5.2 WIP (Work In Progress / En-cours)

Le WIP correspond au **nombre total de cocottes en cours de fabrication** — c'est-à-dire toutes les cocottes qui ont quitté le stock de matière première mais n'ont pas encore passé le contrôle qualité au Poste 5.

### 5.3 Lead Time (Temps de traversée)

Le Lead Time est le **temps total** entre l'entrée d'une feuille au Poste 1 et la sortie de la cocotte terminée au Poste 5.

### 5.4 Débit (Throughput)

$$
\text{Débit} = \frac{\text{Cocottes terminées}}{\text{Durée du round (en minutes)}}
$$

### 5.5 Loi de Little

La **Loi de Little** relie les trois indicateurs fondamentaux :

$$
\boxed{\text{WIP} = \text{Débit} \times \text{Lead Time}}
$$

Ou de manière équivalente :

$$
\text{Lead Time} = \frac{\text{WIP}}{\text{Débit}}
$$

| Indicateur | Signification | Unité typique |
|:-----------|:--------------|:--------------|
| **WIP** | Nombre moyen de pièces dans le système | cocottes |
| **Débit** | Nombre de pièces terminées par unité de temps | cocottes/min |
| **Lead Time** | Temps de traversée moyen d'une pièce | min |

**Traduction opérationnelle** : Pour réduire le **Lead Time**, on peut soit **réduire le WIP**, soit **augmenter le Débit**.

### 5.6 Takt Time

Le Takt Time est le **rythme de production imposé par la demande client**.

$$
\text{Takt Time} = \frac{\text{Temps disponible}}{\text{Demande client}}
$$

> [!IMPORTANT]
> **Calcul du Takt Time pour l'atelier :**
>
> | Donnée | Valeur |
> |:-------|:------:|
> | **Demande client** | **100 cocottes / heure** |
> | **Temps disponible** | **60 minutes** |
> | **Takt Time** | **60 min / 100 = 0,6 min = 36 secondes / cocotte** |
>
> ➡️ **Chaque poste doit réaliser son opération en 36 secondes maximum** pour satisfaire la demande client.

### 5.7 TRG (Taux de Rendement Global)

$$
\boxed{\text{TRG} = \text{Disponibilité} \times \text{Performance} \times \text{Qualité}}
$$

| Composante | Formule |
|:-----------|:--------|
| **Disponibilité** | Temps effectif / Temps d'ouverture |
| **Performance** | Production réelle / Production théorique au Takt |
| **Qualité** | Pièces bonnes / Pièces produites |

**Repères** :

- TRG ≈ 40–50 % → production désorganisée
- TRG ≈ 85 % → classe mondiale
- TRG > 90 % → excellence opérationnelle

<div style="page-break-before: always;"></div>

## 6. Round 1 — Flux Poussé : « L'Usine à Stocks »

### 6.1 Règles

> [!WARNING]
> **Mode production de masse**
>
> - Travail par **lots de 10 cocottes** : chaque poste termine un lot complet de 10 pièces avant de le transférer au poste suivant.
> - **Production continue pendant 20 minutes** : chaque poste produit **au maximum de sa capacité, sans s'arrêter**. Dès qu'un lot de 10 est terminé et envoyé au poste suivant, l'opérateur **recommence immédiatement** un nouveau lot de 10 (s'il a de la matière disponible).
> - **Communication interdite** entre les postes
> - Objectif : « Produire le **maximum** en 20 minutes »

> [!CAUTION]
> **⚠️ Piège fréquent** : Il ne s'agit **PAS** de faire passer un seul lot de 10 à travers toute la ligne ! Le P1 doit **enchaîner les lots** sans attendre que les postes suivants aient fini. C'est cette production en continu qui génère l'**accumulation de stocks entre les postes** (WIP) — le phénomène central que le Round 1 cherche à démontrer.
>
> **Exemple concret** : Pendant que P2 travaille encore sur le 1er lot, P1 a déjà terminé et poussé un 2ème lot. Ce 2ème lot **s'empile en attente** devant P2. Au bout de 20 minutes, on observe souvent 30 à 40 cocottes en cours dans le système !

> [!NOTE]
> **Démarrage** : Tous les postes démarrent **à vide**. Seul le **Poste 1** reçoit un **gros stock de feuilles A4 brutes** (50 à 100 feuilles). Au signal « TOP Départ ! », le P1 commence immédiatement et **ne s'arrête plus** pendant 20 minutes. Les postes suivants attendent de recevoir leur premier lot pour démarrer.

> [!TIP]
> **Mesure du WIP** : À mi-parcours (10 min) ou à la fin des 20 minutes, le formateur demande **STOP**. Chaque équipe compte alors toutes les cocottes « dans le tuyau » : celles en cours de traitement + celles en attente entre les postes. Ce total = **WIP instantané**. C'est ce chiffre qui, combiné au débit, permet de calculer le Lead Time par la **Loi de Little**.

### 6.2 Relevé KPI — Round 1

| Indicateur | Valeur |
|:-----------|:------:|
| Production totale | ___ cocottes |
| En-cours (WIP) | ___ cocottes |
| Lead Time moyen | ___ s |
| Débit | ___ cocottes/min |
| Taux de qualité | ___ % |
| Stress perçu | ⭐⭐⭐⭐⭐ |

<div style="page-break-before: always;"></div>

## 7. Round 2 — Flux Tiré & Kanban : « L'Usine Fluide »

### 7.1 Concepts Clés

- **Flux Tiré (Pull)** : On ne produit que si le poste suivant (le « client ») le demande.
- **Kanban** : Signal visuel de déclenchement de production (carte verte = « je suis disponible, envoie une pièce »).
- **One Piece Flow** : Fabrication pièce par pièce (lot de 1) au lieu de lots de 10.

### 7.2 Règles

> [!TIP]
> **Mode Flux Tiré**
>
> - Production **pièce à pièce** uniquement (lot = 1)
> - On ne produit que si le **poste aval** affiche sa **carte verte** (Kanban)
> - Carte **rouge** = poste occupé, ne pas envoyer
> - Carte **verte** = poste disponible, demande une pièce
> - **Communication autorisée** et encouragée
> - Objectif : **Réduire le Lead Time** et le WIP

### 7.3 Mise en Place du Kanban

1. Chaque poste reçoit **2 cartes Kanban** (1 rouge, 1 verte)
2. Le poste affiche la carte **verte** quand il est prêt à recevoir une pièce
3. Le poste amont ne transfert la pièce que s'il voit la carte verte
4. Dès réception, le poste passe en carte **rouge**
5. Réorganisation physique : **rapprocher les postes** pour minimiser les transports

### 7.4 Relevé KPI — Round 2

| Indicateur | Valeur |
|:-----------|:------:|
| Production totale | ___ cocottes |
| En-cours (WIP) | ___ cocottes |
| Lead Time moyen | ___ s |
| Débit | ___ cocottes/min |
| Taux de qualité | ___ % |
| Stress perçu | ⭐⭐⭐ |

<div style="page-break-before: always;"></div>

## 8. Round 3 — Équilibrage & Kaizen

### 8.1 Objectifs

- Équilibrer les charges de travail entre postes
- Calculer et appliquer le Takt Time
- Mettre en place le 5S
- Pratiquer l'amélioration continue (Kaizen)

### 8.2 Atelier Yamazumi (Diagramme d'Équilibrage)

1. **Chronométrer** chaque poste individuellement : mesurer le temps de cycle de son opération sur **3 cycles consécutifs**, puis calculer la **moyenne**.
2. **Construire** le diagramme Yamazumi :
   - Axe vertical : Temps (secondes)
   - Axe horizontal : Postes P1 à P5
   - Ligne horizontale : **Takt Time cible** (36 s)

```
Temps (sec)
   60│         █████
   50│  ████   █████  ████
   40│  ████   █████  ████  ████
   30│  ████ ┆ █████  ████  ████  ████  ← Takt Time = 36 s
   20│  ████   █████  ████  ████  ████
   10│  ████   █████  ████  ████  ████
    0└─────┬────┬────┬────┬────┬────
         P1   P2   P3   P4   P5
```

1. **Identifier le goulot** (poste au-dessus du Takt Time)
2. **Brainstorming** en équipe pour réduire ce temps :
   - Redistribuer certaines opérations
   - Simplifier les gestes
   - Améliorer l'ergonomie

### 8.3 Mise en Place du 5S

| # | Japonais | Signification | Action concrète |
|:-:|:---------|:--------------|:----------------|
| 1 | **Seiri** | Trier | Retirer le matériel inutile des tables |
| 2 | **Seiton** | Ranger | Placer chaque outil à portée de main |
| 3 | **Seiso** | Nettoyer | Remettre les tables en ordre |
| 4 | **Seiketsu** | Standardiser | Photographier la disposition (standard visuel) |
| 5 | **Shitsuke** | Respecter | S'engager collectivement à maintenir l'organisation |

### 8.4 Production Round 3 (20 min)

- Application des améliorations (nouveau layout, tâches rééquilibrées, 5S)
- Objectif : qualité maximale + respect du Takt Time

### 8.5 Relevé KPI — Round 3

| Indicateur | Valeur |
|:-----------|:------:|
| Production totale | ___ cocottes |
| En-cours (WIP) | ___ cocottes |
| Lead Time moyen | ___ s |
| Débit | ___ cocottes/min |
| Taux de qualité | ___ % |
| Stress perçu | ⭐⭐ |

<div style="page-break-before: always;"></div>

## 9. Tableau Comparatif des 3 Rounds

*À remplir ensemble à la fin de la journée :*

| Indicateur | Round 1 — Flux Poussé | Round 2 — Flux Tiré | Round 3 — Kaizen |
|:-----------|:---------------------:|:-------------------:|:----------------:|
| **Production totale** | | | |
| **En-cours (WIP)** | | | |
| **Lead Time moyen** | | | |
| **Débit** | | | |
| **Taux de qualité** | | | |
| **TRG** | | | |
| **Stress perçu** | | | |
| **Collaboration** | | | |

<div style="page-break-before: always;"></div>

## 10. Ce qu'il faut retenir

> [!IMPORTANT]
> **Le LEAN n'est pas une méthode pour travailler plus vite, mais pour travailler mieux en supprimant ce qui ne sert à rien.**
>
> *« Le pire gaspillage, c'est de faire efficacement quelque chose qui ne devrait pas être fait du tout. »* — Taiichi Ohno

### Les points clés

1. ✅ Les 3 démons du LEAN : **Muda** (gaspillage), **Muri** (surcharge), **Mura** (irrégularité)
2. ✅ **Flux tiré** > Flux poussé : on produit uniquement ce que le client demande
3. ✅ **WIP** en baisse = **Lead Time** en baisse (Loi de Little)
4. ✅ Le **Takt Time** cadence la production sur la demande client
5. ✅ Le **TRG** mesure la performance globale (Disponibilité × Performance × Qualité)
6. ✅ L'**amélioration continue** (Kaizen) est l'affaire de tous

### Mon plan d'action personnel

*Qu'allez-vous changer concrètement dans votre travail quotidien ?*

| Action d'amélioration | Quand ? | Comment ? |
|:----------------------|:--------|:----------|
| | | |
| | | |
| | | |

---

*Atelier Cocotte LEAN — Livret Participant — Février 2026*
