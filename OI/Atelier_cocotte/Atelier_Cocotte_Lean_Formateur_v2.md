---
output:
  word_document: default
  html_document: default
  pdf_document: default
---
![Logo UIMM](logo_uimm_placeholder.jpg)

**Pôle Formation UIMM - CVDL**

---

# Atelier Cocotte LEAN, « Le Contrat Cadencé »

## Guide Formateur, version 2.0

> [!IMPORTANT]
> **Ce que cette version change.** La v1 mesurait le Lead Time par la loi de Little, à partir d'un WIP compté à la volée. Le calcul ne tenait pas : la loi de Little suppose un régime permanent, or un round de 20 minutes en flux poussé n'atteint jamais ce régime. La v2 mesure les trois indicateurs séparément et n'utilise la loi de Little qu'en fin de journée, comme test de cohérence. C'est plus rigoureux, et c'est devenu un temps fort du débriefing.

---

## 1. Pourquoi la version 1 échouait

Un point d'arithmétique avant tout le reste, parce qu'il explique l'essentiel des séances ratées.

La v1 utilisait 5 postes de temps de cycle 25, 35, 40, 20 et 30 secondes, soit 150 secondes de contenu travail, avec des transferts par lots de 10 et un round de 20 minutes.

En flux poussé par lots, la première pièce ne peut sortir du dernier poste qu'après que chaque poste ait traité son lot complet :

$$
10 \times 25 + 10 \times 35 + 10 \times 40 + 10 \times 20 + 10 \times 30 = 1\,500\ \text{s} = 25\ \text{min}
$$

**Le round durait 20 minutes. Aucune cocotte ne sortait.** Production nulle, taux de qualité indéfini, Lead Time non mesurable. L'atelier ne pouvait produire aucune donnée exploitable, quelle que soit l'énergie mise par le groupe.

Trois autres incohérences accompagnaient celle-là :

| Affirmation v1 | Réalité |
|:---------------|:--------|
| Round 1 : 45 cocottes, débit 2,3 /min | Le goulot à 40 s plafonne le débit à 1,5 /min |
| Round 3 : débit 3,4 /min | Exigerait un goulot à 17,6 s sur 5 postes |
| Takt Time de 36 s | Inférieur au goulot de 40 s : demande inatteignable avant même le Kaizen |

La v2 repose sur un modèle vérifié par simulation à événements discrets, avec variabilité opératoire et taux de rebut. Les valeurs attendues données dans ce guide en sont issues.

> [!NOTE]
> **Statut des chiffres.** Les valeurs « attendues » de ce document sont des résultats de simulation, moyennés sur 200 réplications avec une variabilité de 12 à 18 % sur les temps opératoires. Ce ne sont pas des relevés terrain. Elles servent au formateur à savoir si sa séance dérive, pas à être annoncées comme vérité aux participants.

---

## 2. Le scénario

### 2.1 Le contrat

L'atelier est présenté comme un sous-traitant de rang 2 qui vient de décrocher un contrat cadencé. Le formateur incarne le donneur d'ordre au premier round, puis délègue ce rôle à un participant.

Les termes du contrat sont affichés au mur pendant toute la journée :

| Clause | Valeur |
|:-------|:-------|
| **Volume par vacation** | 24 pièces conformes |
| **Durée de la vacation** | 16 minutes |
| **Enlèvements** | 1 camion toutes les 4 minutes, 6 pièces par camion |
| **Qualité** | Zéro défaut accepté, tri à la charge du fournisseur |
| **Retard** | Toute pièce manquante à l'enlèvement est reportée et reste due |

Le **Takt Time** découle directement du contrat :

$$
\text{Takt Time} = \frac{\text{Temps disponible}}{\text{Demande client}} = \frac{16 \times 60}{24} = 40\ \text{s/pièce}
$$

### 2.2 Pourquoi ce dispositif fonctionne

Le camion transforme le takt time en événement physique. Un participant ne retient pas une division, il retient un carton vide qui part sans lui. Au round 1, les deux premiers camions partent à vide et le troisième repart à moitié plein. Personne ne conteste ensuite l'intérêt du flux tiré.

Le rôle de client, joué par un participant, produit le second effet : quelqu'un refuse physiquement les pièces non conformes, devant tout le monde. Le taux de qualité cesse d'être une case à remplir.

---

## 3. Le protocole de mesure

C'est le cœur de la refonte. Trois problèmes de la v1 sont traités par un seul objet : le jeton.

### 3.1 Le jeton suiveur

Chaque pièce lancée en production reçoit un **jeton numéroté** (carton plastifié, numéros 1 à 60), fixé par un trombone et qui voyage avec elle jusqu'à la sortie.

Le jeton résout trois choses à la fois :

| Problème v1 | Ce que le jeton apporte |
|:------------|:------------------------|
| Lead Time calculé indirectement, résultat aberrant | Mesure directe : heure d'entrée et heure de sortie relevées sur registre |
| En-cours difficiles à faire apparaître | WIP = nombre de jetons absents du tableau, lisible en une seconde |
| Kanban abstrait au round 2 | Limiter le nombre de jetons plafonne physiquement le WIP (mécanisme **CONWIP**) |

> [!TIP]
> **Le tableau des jetons** est un simple panneau A3 avec 60 emplacements numérotés. Un jeton sur le panneau signifie une place libre dans le système. Un emplacement vide signifie une pièce en cours quelque part sur la ligne. En un coup d'œil, sans compter, le groupe voit le WIP monter au round 1 et rester plat au round 2.

### 3.2 Les deux registres

**Registre de lancement**, tenu par le Lanceur : numéro de jeton, heure de lancement en mm:ss.

**Registre d'expédition**, tenu par le Client : numéro de jeton, heure de sortie, conforme oui ou non, motif de rejet.

La base de temps est un **chronomètre projeté au mur** en mm:ss, démarré au top départ et visible depuis tous les postes. Un chronomètre de smartphone affiché au vidéoprojecteur suffit.

Le Lead Time de chaque pièce s'obtient par simple soustraction. On dispose ainsi d'une distribution complète, pas d'une moyenne devinée.

### 3.3 Les zones d'en-cours

Entre chaque poste, une feuille A3 posée sur la table, marquée **ZONE D'EN-COURS P1 → P2**, et ainsi de suite. Règle absolue : une pièce en attente est dans la zone, jamais ailleurs.

Cette contrainte matérielle est ce qui rend les stocks visibles. Sans elle, les piles se dispersent et l'effet visuel disparaît. C'est le point que la v1 ratait.

Au signal STOP, chaque zone est comptée séparément. Le profil d'en-cours poste par poste désigne le goulot sans aucun calcul.

### 3.4 Ce que chaque indicateur mesure, et comment

| Indicateur | Source | Qui relève |
|:-----------|:-------|:-----------|
| **Takt Time** | Imposé par le contrat, non mesuré | Formateur, affiché |
| **Temps de cycle par poste** | Chronométrage de 5 cycles consécutifs, on retient la **médiane** | Chronométreur |
| **Temps de cycle de la ligne** | Durée du round divisée par le nombre de pièces sorties | Client |
| **Lead Time** | Heure de sortie moins heure d'entrée, par pièce | Calculé après coup |
| **WIP** | Comptage par zone au signal STOP | Observateur |
| **Débit** | Pièces sorties divisées par la durée | Calculé |
| **Taux de service** | Pièces livrées à l'heure sur pièces dues | Client |

> [!NOTE]
> **Médiane et non moyenne** pour les temps de cycle. Sur 5 relevés, un incident unique (chute de ciseaux, question posée au voisin) déforme la moyenne de 20 à 30 %. La médiane l'ignore. C'est aussi un point de méthode qui parle à un public industriel habitué aux relevés de production.

---

## 4. Organisation et rôles

### 4.1 Une seule ligne, de 6 à 8 participants

| Rôle | Effectif | Mission |
|:-----|:--------:|:--------|
| **Opérateur P1 à P4** | 4 | Production |
| **Lanceur** | 1 | Attribue les jetons, tient le registre de lancement, gère le stock matière |
| **Client / Expéditeur** | 1 | Contrôle final, tient le registre d'expédition, charge les camions, refuse les non-conformes |
| **Chronométreur** | 0 ou 1 | Relève les temps de cycle poste par poste |
| **Observateur** | 0 ou 1 | Compte les en-cours par zone, remplit la grille d'observation des comportements |

À 6 participants, le formateur assure chronométrage et observation. À 7, il ne garde que l'observation. À 8, il est libre d'observer le groupe, ce qui est préférable.

### 4.2 Rotation entre les rounds

Les rôles non productifs tournent entre les rounds. Les opérateurs restent à leur poste.

C'est un arbitrage assumé : faire tourner les opérateurs remettrait à zéro la courbe d'apprentissage et les gains du round 3 deviendraient ininterprétables. On perd en équité de vécu, on gagne en lisibilité des données. Annoncer cet arbitrage au groupe, sinon il est perçu comme un oubli.

### 4.3 Les postes

Le carré n'est pas fourni découpé. Le poste 1 fait le débit matière, ce qui maintient l'étape la plus génératrice de rebuts dans le périmètre et ouvre la principale piste Kaizen.

| Poste | Opérations | Temps de cycle de référence |
|:-----:|:-----------|:---------------------------:|
| **P1** | Débit matière : triangle, découpe de la chute, carré 210 × 210 | 25 s |
| **P2** | Diagonales puis premier blintz, 4 coins au centre | 30 s |
| **P3** | Retournement puis second blintz, 4 coins au centre | 35 s |
| **P4** | Pré-formage, mise en volume | 25 s |
| | **Contenu travail total** | **115 s** |

**Goulot initial : P3 à 35 secondes.** Débit maximal théorique de la ligne : 1,71 pièce par minute, soit 27 pièces sur une vacation de 16 minutes. La demande de 24 pièces est donc atteignable, mais seulement si le système ne perd rien en attente, en reprise ou en rebut. C'est la tension qui fait tenir la journée.

---

## 5. Standard de pliage (FIP)

> **Objectif** : produire une cocotte symétrique, fonctionnelle, sans déchirure.
>
> **Matière** : 1 feuille A4 blanche 80 g/m².

### 5.1 Obtenir le carré

1. **Le triangle** : rabattre le coin supérieur gauche sur le bord droit pour former un triangle rectangle isocèle.
2. **La chute** : découper ou déchirer proprement le long du pli la bande rectangulaire restante.
3. **Résultat** : carré de 210 × 210 mm.

> [!TIP]
> La majorité des rebuts du round 1 vient d'un carré mal équerré. Ne pas le dire au groupe avant le débriefing. C'est ce constat qui déclenchera la proposition du gabarit au round 3.

### 5.2 Les étapes

| Étape | Action | Point clé | Raison |
|:-----:|:-------|:----------|:-------|
| **1** | **Les diagonales** | Marquer les deux plis en croix coin à coin | Localiser le centre exact |
| **2** | **Premier blintz** | Rabattre les 4 coins vers le centre | Les bords ne doivent pas se chevaucher |
| **3** | **Le retournement** | Retourner la feuille, face lisse vers soi | Conditionne la cinématique d'ouverture |
| **4** | **Second blintz** | Rabattre les 4 nouveaux coins vers le centre | Appuyer fort, marquer le pli |
| **5** | **Pré-formage** | Plier en deux horizontalement puis verticalement | Marquer les plis extérieurs |
| **6** | **Mise en volume** | Glisser les doigts dans les 4 poches, pousser vers le centre | Ne pas déchirer |

![Plan de pliage](Plan_Cocotte_simple.jpg)

### 5.3 Critères de conformité

| # | Critère | Contrôle |
|:-:|:--------|:---------|
| 1 | **Symétrie** | Les 4 pointes à même hauteur, vérification visuelle sur plan |
| 2 | **Mobilité** | Ouverture et fermeture sans résistance, 3 actionnements dans les deux axes |
| 3 | **Intégrité** | Aucune déchirure, aucun pli parasite |

Le contrôle est fait par le Client, à réception. Une pièce refusée est posée dans le **bac rouge**, comptée en rebut, et n'est jamais recomptée.

---

## 6. Round 1 : Flux poussé, transfert par lots de 5

### 6.1 Règles annoncées au groupe

> [!WARNING]
> - Transfert par **lots de 5**. Un poste ne transmet que lorsque ses 5 pièces sont finies.
> - Chaque poste produit **au maximum de sa capacité**, sans jamais attendre l'aval.
> - **Communication interdite** entre postes.
> - Objectif donné : « produire le maximum ».
> - Le Lanceur dispose des **60 jetons**. Il lance sans limite.

### 6.2 Pièges de conduite

> [!CAUTION]
> **Ne pas faire circuler un seul lot à la fois.** Tous les postes doivent tourner en parallèle dès qu'ils ont de la matière. C'est le parallélisme qui crée l'accumulation. Si le formateur laisse le groupe traiter un lot du début à la fin, l'effet ne se produit pas.
>
> **Le P1 ne s'arrête jamais.** Il a un stock matière de 60 feuilles devant lui. C'est lui qui alimente la montagne d'en-cours. Si le P1 ralentit par empathie pour l'aval, l'expérience s'effondre. Le formateur le relance : « votre indicateur à vous, c'est votre production ».

### 6.3 Déroulé

| Temps | Séquence |
|:------|:---------|
| 0 à 5 min | Briefing, distribution des jetons, mise en place du chrono projeté |
| 5 à 21 min | **Vacation de 16 minutes.** Le formateur circule sans intervenir. Camions à 4, 8, 12 et 16 min |
| 21 à 29 min | **STOP.** Comptage par zone, clôture des registres, remplissage du tableau de marche |
| 29 à 50 min | Débriefing |

### 6.4 Résultats attendus

| Indicateur | Valeur attendue |
|:-----------|:---------------:|
| Pièces lancées | 38 à 42 |
| Pièces sorties | 13 à 16 |
| Pièces conformes | 10 à 12 |
| **WIP en fin de vacation** | **24 à 28** |
| **Lead Time moyen** | **environ 10 min** |
| Débit | 0,9 /min |
| Temps de cycle de la ligne | environ 66 s, pour un takt de 40 s |
| **Taux de service client** | **environ 45 %** |
| Camions partis vides | **les deux premiers** |

### 6.5 Le chiffre qui frappe

$$
\text{Ratio d'efficacité du processus} = \frac{\text{Contenu travail}}{\text{Lead Time}} = \frac{115\ \text{s}}{620\ \text{s}} \approx 18\ \%
$$

Sur les dix minutes que passe une cocotte dans l'atelier, moins de deux minutes servent à la transformer. Le reste, elle attend. Écrire ce ratio au paperboard et le laisser affiché toute la journée.

### 6.6 Questions de débriefing

Dans cet ordre, sans en sauter :

1. « Qui a eu le sentiment de bien travailler ? » (presque tous lèvent la main, alors que le client n'a reçu que la moitié de sa commande)
2. « Regardez les zones d'en-cours. Où est la plus haute pile ? » (le groupe désigne le goulot lui-même, sans calcul)
3. « Combien de temps une cocotte a-t-elle passé dans l'atelier ? Combien de temps a-t-elle été travaillée ? »
4. « Quand avez-vous su qu'il y avait un défaut de découpe ? » (à la sortie, sur des pièces produites dix minutes plus tôt)
5. « Le standard était scotché sur votre table. Qui l'a lu pendant la vacation ? »
6. Identification des gaspillages observés, au paperboard, en s'appuyant sur ce qui vient d'être vécu et non sur la liste théorique

### 6.7 Gaspillages à faire émerger

| Gaspillage | Manifestation observable ce jour |
|:-----------|:---------------------------------|
| Surproduction | 40 pièces lancées pour 24 demandées |
| Stocks | Les zones d'en-cours saturées |
| Attentes | P4 inactif pendant les 7 premières minutes |
| Défauts | Rebuts détectés en fin de ligne, sur des pièces anciennes |
| Sur-processus | Reprises de pliage sur des carrés mal équerrés |
| Mouvements | Recherche de place pour poser les piles |
| Transports | Déplacements pour transférer les lots |
| Sous-emploi des compétences | Personne n'a le droit de parler ni de proposer quoi que ce soit |

---

## 7. Round 2 : Flux tiré, CONWIP à 6 jetons

### 7.1 Apport préalable, 30 minutes

Trois notions, dans cet ordre :

**Flux tiré.** On ne produit que sur demande de l'aval. Inversion du sens de l'information.

**Kanban.** Le signal de production. Ici, le jeton libre remplace la carte : pas de jeton, pas de lancement.

**CONWIP.** Plafonner le nombre de jetons en circulation revient à plafonner le WIP. Le lien avec le Lead Time se déduit ensuite du relevé du round 1, sans avoir besoin de la formule.

### 7.2 Règles

> [!TIP]
> - Transfert **pièce à pièce**. Aucun lot.
> - Le Lanceur ne dispose que de **6 jetons**. Il ne peut lancer une pièce que si un jeton est revenu.
> - Un poste ne prend une pièce que lorsqu'il est libre. Une seule pièce en attente maximum entre deux postes.
> - **Communication autorisée et encouragée.** Un poste qui reçoit une pièce douteuse la renvoie immédiatement en amont.
> - Réimplantation autorisée : rapprocher les tables.
> - Objectif donné : « livrer les 4 camions ».

### 7.3 Déroulé

| Temps | Séquence |
|:------|:---------|
| 0 à 8 min | Briefing, réimplantation, retrait de 54 jetons du tableau |
| 8 à 12 min | Essai à blanc, 4 pièces |
| 12 à 28 min | **Vacation de 16 minutes** |
| 28 à 34 min | STOP, comptage, registres, tableau de marche |
| 34 à 50 min | Débriefing |

### 7.4 Résultats attendus

| Indicateur | Round 1 | Round 2 attendu |
|:-----------|:-------:|:---------------:|
| Pièces sorties | 13 à 16 | 23 à 26 |
| Pièces conformes | 10 à 12 | 20 à 23 |
| **WIP** | 24 à 28 | **6, par construction** |
| **Lead Time** | environ 10 min | **environ 3,5 min** |
| Débit | 0,9 /min | 1,5 /min |
| Temps de cycle ligne | 66 s | environ 39 s, takt à 40 s |
| Ratio d'efficacité | 18 % | **environ 55 %** |
| Taux de service | 45 % | 80 à 100 % |

> [!IMPORTANT]
> **Le point à ne pas manquer.** Le débit n'a pas augmenté parce que les gens travaillent plus vite. Les temps de cycle par poste sont les mêmes. Ce qui a changé, c'est que la ligne ne fabrique plus ce dont personne n'a besoin. Poser la question ainsi : « qui a travaillé plus vite ce round ? Personne. Alors d'où viennent les 10 pièces de plus ? »

### 7.5 Questions de débriefing

1. « Combien de pièces avez-vous eu sous la main en même temps ? » (six, jamais plus, et ils l'ont senti)
2. « Quand avez-vous détecté les défauts cette fois ? »
3. « Le premier camion est-il parti plein ? » (non, la montée en charge existe toujours, mais le retard se rattrape au lieu de se creuser)
4. « Qu'est-ce qui vous a le plus gêné ? » (l'attente devant le goulot, ce qui ouvre le round 3)

---

## 8. Chantier Kaizen : 45 minutes

### 8.1 Yamazumi

Le chronométreur a relevé les temps de cycle des deux rounds. On construit le diagramme au paperboard :

```
Temps (s)
  40 │                    Takt Time = 40 s
     ├ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
  35 │              ████
  30 │       ████   ████
  25 │ ████  ████   ████   ████
  20 │ ████  ████   ████   ████
  15 │ ████  ████   ████   ████
  10 │ ████  ████   ████   ████
   5 │ ████  ████   ████   ████
   0 └──┬─────┬──────┬──────┬───
        P1    P2     P3     P4
       25 s  30 s   35 s   25 s
```

Aucun poste ne dépasse le takt. Le problème n'est donc pas la capacité, c'est le **déséquilibre** : 10 secondes d'écart entre P1 et P3 signifient que P1 et P4 attendent en permanence. C'est du **Mura**, et c'est ce qui limite le débit réel.

### 8.2 Conduite du brainstorming

Ne pas donner les solutions. Poser la question et laisser chercher 15 minutes en équipe complète, formateur en retrait.

Solutions généralement trouvées par les groupes :

| Piste | Effet | Nature |
|:------|:------|:-------|
| **Gabarit carton 210 × 210** au P1, on trace au lieu de mesurer | P1 : 25 s → 20 s, et rebuts de découpe quasi éliminés | Poka-yoké |
| **Retournement transféré à P2**, qui a la pièce en main en fin d'opération | P3 : 35 s → 30 s, coût marginal nul pour P2 | Rééquilibrage |
| **Un coin du second blintz transféré à P4** | P3 : 30 s → 28 s, P4 : 25 s → 27 s | Rééquilibrage |
| **Pliage contre le bord d'une règle** | P2 : 30 s → 27 s, plis mieux marqués | Standard de geste |

> [!TIP]
> Le formateur garde un gabarit carton prêt, caché. Si le groupe ne trouve pas au bout de 10 minutes, il pose la question : « qu'est-ce qui prend du temps dans la découpe, le geste ou la vérification ? ». La réponse mène au gabarit sans le donner.

Résultat cible après chantier :

| Poste | Avant | Après |
|:-----:|:-----:|:-----:|
| P1 | 25 s | 20 s |
| P2 | 30 s | 27 s |
| P3 | **35 s** | 28 s |
| P4 | 25 s | 27 s |
| **Contenu travail** | 115 s | **102 s** |
| **Goulot** | 35 s | **28 s** |

Le gain sur le contenu travail est de 11 %. Le gain sur le goulot est de 20 %. Ne pas promettre davantage : un chantier de 45 minutes ne produit pas de miracle, et annoncer des gains irréalistes discrédite la méthode auprès d'un public qui connaît son atelier.

### 8.3 Chantier 5S : 15 minutes

| # | Terme | Action concrète au poste |
|:-:|:------|:-------------------------|
| 1 | **Seiri** | Retirer de la table tout ce qui ne sert pas à l'opération |
| 2 | **Seiton** | Placer ciseaux, règle et gabarit dans la zone de préhension, toujours au même endroit |
| 3 | **Seiso** | Évacuer les chutes de découpe au fur et à mesure |
| 4 | **Seiketsu** | Photographier le poste rangé, afficher la photo au poste |
| 5 | **Shitsuke** | Le poste est remis dans l'état de la photo à chaque fin de vacation |

---

## 9. Round 3 : Ligne équilibrée, CONWIP à 4 jetons

### 9.1 Règles

Identiques au round 2, avec les améliorations en place et **4 jetons seulement**.

Réduire encore le WIP est contre-intuitif pour le groupe : « on va produire moins ». C'est le moment de le laisser tester et constater l'inverse.

### 9.2 Résultats attendus

| Indicateur | R1 | R2 | R3 attendu |
|:-----------|:--:|:--:|:----------:|
| Pièces sorties | 13-16 | 23-26 | 28-32 |
| Pièces conformes | 10-12 | 21-23 | 28-30 |
| **WIP** | 24-28 | 6 | **4** |
| **Lead Time** | ~10 min | ~3,5 min | **~2 min** |
| Débit | 0,9 /min | 1,5 /min | 1,9 /min |
| Temps de cycle ligne | 66 s | 39 s | 32 s |
| **Ratio d'efficacité** | 18 % | 55 % | **85 %** |
| Taux de service | 45 % | 90-100 % | 100 % |

### 9.3 Le piège volontaire du round 3

La ligne équilibrée produit environ 29 pièces conformes. Le client en demande 24.

**Les 5 pièces excédentaires sont de la surproduction.** Elles ne sont pas vendues, elles ont consommé de la matière et du temps, elles encombrent.

Poser la question au débriefing : « vous avez fait 29 pièces, le client en voulait 24. C'est une bonne ou une mauvaise performance ? » Le groupe répond spontanément « bonne ». C'est le moment d'introduire la règle du takt : **produire au rythme du client, ni plus vite ni moins vite.** Une ligne qui produit trop vite doit ralentir et affecter le temps libéré à autre chose, pas fabriquer du stock.

C'est le point le plus contre-intuitif de la journée et celui qui reste le plus longtemps.

### 9.4 Variante pour public confirmé

Porter la demande à 32 pièces (8 par camion, takt de 30 s) uniquement au round 3. La ligne équilibrée en est tout juste capable, à condition de zéro arrêt et de zéro rebut. On perd la comparabilité directe avec les rounds précédents, on gagne une tension réaliste. À réserver aux groupes qui ont bien tenu les rounds 1 et 2.

---

## 10. Synthèse : 30 minutes

### 10.1 Les trois indicateurs

| | Définition | Ce qu'il dit | Qui le fixe |
|:--|:-----------|:-------------|:------------|
| **Takt Time** | Temps disponible / demande client | À quel rythme il **faut** produire | Le client |
| **Temps de cycle** | Temps de traitement / pièces produites | À quel rythme on produit **réellement** | Le processus |
| **Lead Time** | Temps entre entrée matière et livraison | Combien de temps le client **attend** | Le système entier |

$$
\text{Takt Time} = \frac{\text{Temps disponible}}{\text{Demande client}}
\qquad
\text{Temps de cycle} = \frac{\text{Temps de traitement}}{\text{Nombre de pièces}}
$$

$$
\text{Lead Time} = \sum \text{Temps d'attente} + \sum \text{Temps de transport} + \sum \text{Temps de traitement}
$$

**La règle** : si le temps de cycle dépasse le takt time, la demande ne peut pas être tenue. S'il est très inférieur, on surproduit. On vise l'égalité.

### 10.2 La loi de Little, en test et non en outil

$$
\boxed{\text{WIP} = \text{Débit} \times \text{Lead Time}}
$$

On dispose maintenant des trois grandeurs **mesurées séparément**. On confronte.

| Round | WIP mesuré | Débit mesuré | Lead Time **prédit** par Little | Lead Time **mesuré** | Écart |
|:-----:|:----------:|:------------:|:-------------------------------:|:--------------------:|:-----:|
| 1 | 26 | 0,90 /min | 28,9 min | 10,4 min | **facteur 2,8** |
| 2 | 6 | 1,53 /min | 3,9 min | 3,5 min | 11 % |
| 3 | 4 | 1,89 /min | 2,1 min | 2,0 min | 5 % |

> [!IMPORTANT]
> **C'est le moment intellectuel fort de la journée.** La loi de Little est exacte, mais elle suppose un **régime permanent** : un système dont le WIP moyen ne dérive pas. Aux rounds 2 et 3, le CONWIP force ce régime, et la loi tombe juste à 5 % près. Au round 1, le WIP grimpe sans arrêt pendant toute la vacation, le système n'est jamais stationnaire, et la loi donne un résultat faux.
>
> Traduction pour l'atelier : **une usine en flux poussé est une usine dont on ne sait pas prédire les délais.** Ce n'est pas un problème de formule, c'est un problème de pilotage. On ne peut pas promettre une date de livraison à un client quand on ne maîtrise pas son propre WIP.

Cette démonstration remplace avantageusement l'usage de la loi de Little comme méthode de calcul, qui donnait des Lead Times aberrants et décrédibilisait l'ensemble.

### 10.3 TRG

Définitions conformes à la **norme NF E 60-182** :

$$
\text{TRS} = \frac{\text{Temps utile}}{\text{Temps requis}}
\qquad
\text{TRG} = \frac{\text{Temps utile}}{\text{Temps d'ouverture}}
\qquad
\text{TRE} = \frac{\text{Temps utile}}{\text{Temps total}}
$$

Dans l'atelier, temps d'ouverture et temps requis sont confondus, il n'y a pas d'arrêt planifié dans une vacation. Le TRG et le TRS coïncident donc, et on retient le **TRG**.

**Deux conventions à figer avant la journée, et à annoncer :**

1. Le **temps de cycle de référence** est celui du goulot initial, soit **35 s**, gardé identique aux trois rounds. Sinon le TRG s'améliore mécaniquement quand on améliore la ligne, et perd tout sens comparatif.
2. Le **temps utile ne compte que les pièces valorisables**, c'est-à-dire les pièces conformes dans la limite de la demande client. La surproduction ne crée pas de valeur.

$$
\text{Temps utile} = \min(\text{pièces conformes}\,;\ 24) \times 35\ \text{s}
$$

| Round | Pièces valorisables | Temps utile | TRG |
|:-----:|:-------------------:|:-----------:|:---:|
| 1 | 10 à 12 | 350 à 420 s | **environ 40 %** |
| 2 | 20 à 23 | 700 à 805 s | **73 à 84 %** |
| 3 | 24, plafonné par la demande | 840 s | **environ 88 %** |

Décomposition, à faire calculer par le groupe. La composante **Valorisation** remplace ici le taux de qualité classique, parce qu'elle englobe les deux façons de produire une pièce sans créer de valeur : la rebuter, ou la fabriquer alors que personne ne l'attend.

| Composante | Formule | R1 | R2 | R3 |
|:-----------|:--------|:--:|:--:|:--:|
| **Disponibilité** | Temps de fonctionnement / temps requis | ~100 % | ~98 % | ~97 % |
| **Performance** | (Pièces réalisées × 35 s) / temps de fonctionnement | 55 % | 89 % | **112 %** |
| **Valorisation** | Pièces valorisables / pièces réalisées | 73 % | 83 % | 80 % |
| **TRG** | Produit des trois | 40 % | 73 % | 88 % |

Le taux de qualité classique, pièces conformes sur pièces réalisées, reste affiché à part : 73 %, 83 %, 93 %.

> [!IMPORTANT]
> **La Performance dépasse 100 % au round 3, et c'est voulu.** La ligne équilibrée tourne plus vite que le temps de cycle de référence figé à 35 s. En atelier réel, ce dépassement est le signal qu'il faut réviser la cadence de référence et redéfinir le standard. Le dire au groupe : un indicateur qui sort de sa plage n'est pas forcément une erreur de calcul, c'est parfois une information sur le référentiel.
>
> Noter aussi que la Valorisation **baisse** entre le round 2 et le round 3 alors que la qualité s'améliore. La raison est la surproduction : 30 pièces réalisées pour 24 vendables. C'est la meilleure porte d'entrée vers la discussion du paragraphe 9.3.

> [!NOTE]
> Sans panne dans l'atelier, la disponibilité reste proche de 100 % et le TRG se joue sur la performance et la valorisation. Le signaler : dans un atelier réel, c'est souvent la disponibilité qui constitue le premier gisement. On peut simuler une panne au round 3 pour l'introduire (voir variantes).

### 10.4 Tableau de synthèse à remplir avec le groupe

| Indicateur | R1 Poussé | R2 Tiré | R3 Kaizen |
|:-----------|:---------:|:-------:|:---------:|
| Pièces conformes | | | |
| WIP | | | |
| Lead Time | | | |
| Débit | | | |
| Temps de cycle ligne | | | |
| Takt Time | 40 s | 40 s | 40 s |
| Ratio d'efficacité | | | |
| Taux de service | | | |
| TRG | | | |

---

## 11. Déroulé de la journée

| Horaire | Phase | Durée |
|:--------|:------|:-----:|
| 09 h 00 | Accueil, présentation du contrat client, constitution de l'équipe | 20 min |
| 09 h 20 | Fondamentaux : valeur, Muda, Muri, Mura, les 8 gaspillages | 45 min |
| 10 h 05 | Standard de pliage, entraînement individuel obligatoire (2 cocottes chacun) | 30 min |
| 10 h 35 | Pause | 15 min |
| 10 h 50 | Montage de la ligne, affectation des rôles, chronométrage initial, calcul du takt | 30 min |
| 11 h 20 | **Round 1 : Flux poussé** | 50 min |
| 12 h 10 | Déjeuner | 60 min |
| 13 h 10 | Apport : flux tiré, Kanban, CONWIP | 30 min |
| 13 h 40 | **Round 2 : Flux tiré** | 50 min |
| 14 h 30 | Chantier Kaizen : Yamazumi, brainstorming, 5S | 45 min |
| 15 h 15 | Pause | 15 min |
| 15 h 30 | **Round 3 : Ligne équilibrée** | 50 min |
| 16 h 20 | Synthèse : comparatif, loi de Little, TRG | 30 min |
| 16 h 50 | Plan d'action personnel et clôture | 10 min |

> [!TIP]
> **L'entraînement individuel de 10 h 05 n'est pas optionnel.** Chaque participant plie deux cocottes complètes avant le premier round. Sans cela, les temps de cycle du round 1 sont pollués par l'apprentissage du geste, le taux de rebut explose pour de mauvaises raisons, et la comparaison avec le round 3 mesure surtout la dextérité acquise. C'est une des causes fréquentes d'échec de ce type d'atelier.

---

## 12. Matériel

### 12.1 Consommables

- 200 feuilles A4 blanches 80 g/m²
- 60 trombones
- Post-its 3 couleurs, marqueurs, scotch

### 12.2 Kit de mesure (fourni imprimable)

- 60 jetons numérotés, à plastifier, réutilisables d'une session à l'autre
- 1 tableau des jetons A3
- 5 étiquettes de zones d'en-cours et 1 étiquette de bac rouge, format A4
- 2 registres (lancement, expédition)
- 1 tableau de marche par round
- 1 feuille de relevé Yamazumi
- 1 feuille de synthèse comparative

### 12.3 Équipement

- Vidéoprojecteur, avec un chronomètre mm:ss affiché en grand pendant les vacations
- 2 chronomètres
- 4 paires de ciseaux, 4 règles
- 1 gabarit carton 210 × 210 (tenu en réserve par le formateur)
- 1 bac rouge pour les rebuts, 5 zones d'en-cours matérialisées sur les tables
- 1 carton « CAMION » pour matérialiser l'enlèvement
- Paperboard

### 12.4 Checklist J-1

- [ ] Jetons imprimés, découpés, plastifiés, numérotés, rangés sur le tableau
- [ ] Registres et tableaux de marche imprimés en 3 exemplaires (un par round)
- [ ] Étiquettes de zones imprimées et scotchées sur les tables
- [ ] Standard FIP imprimé en A3, un par poste
- [ ] Chronomètre projeté testé et visible depuis les 4 postes
- [ ] Contrat client affiché au mur en A3
- [ ] Gabarit carton découpé et **rangé hors de vue**
- [ ] Une cocotte témoin pliée par le formateur, conforme, servant de référence de contrôle
- [ ] Tables disposées en ligne, avec espace pour réimplantation au round 2
- [ ] Classeur de calcul des KPI ouvert sur le poste formateur

---

## 13. Annexes

### 13.1 Grille d'observation des comportements

| Dimension | Round 1 | Round 2 | Round 3 |
|:----------|:--------|:--------|:--------|
| Communication | | | |
| Réaction face à un défaut | | | |
| Posture physique, tension | | | |
| Initiative, propositions | | | |
| Regard porté sur le standard | | | |

Remplie par l'Observateur, restituée par lui au débriefing final. C'est souvent le témoignage le plus marquant de la journée, parce qu'il vient d'un pair et non du formateur.

### 13.2 Variantes

**Format demi-journée, 3 h 30** : conserver rounds 1 et 2, supprimer le round 3, remplacer le chantier Kaizen par un brainstorming de 20 minutes sans mise en œuvre. La démonstration Little tient toujours, avec deux points au lieu de trois.

**Public confirmé** : demande portée à 32 pièces au round 3, ou introduction d'un aléa (panne simulée de 90 secondes sur un poste, ou variation de la demande client entre deux camions) pour aborder le **Heijunka** et faire chuter la composante Disponibilité du TRG.

**Public en insertion ou en reconversion** : conserver les trois rounds, abandonner le TRG, se limiter au triptyque Takt / Cycle / Lead Time et au taux de service. La démonstration reste entière.

### 13.3 Ce qui fait rater cet atelier

Par ordre de fréquence observée sur ce format :

1. Des temps de cycle qui rendent le premier round mathématiquement stérile (corrigé en v2)
2. L'absence d'entraînement préalable, qui transforme le round 1 en cours de pliage
3. Des en-cours non matérialisés, qui se dispersent et cessent d'être visibles
4. Un formateur qui intervient pendant le round 1 pour aider, et qui détruit l'expérience qu'il veut produire
5. Un débriefing qui commence par la théorie au lieu de commencer par le vécu
6. Des indicateurs annoncés sans être relevés, qui décrédibilisent tout le reste

### 13.4 Message de clôture

> Le Lean ne consiste pas à faire travailler les gens plus vite. Aux trois rounds, les temps de cycle par poste ont à peine bougé. Ce qui a changé, c'est ce que le système leur demandait de faire.
>
> *« Le pire gaspillage, c'est de faire efficacement quelque chose qui ne devrait pas être fait du tout. »*, Taiichi Ohno

---

## 14. Objectifs pédagogiques évaluables

À l'issue de la journée, le participant est capable de :

1. Calculer un Takt Time à partir d'une demande client et d'un temps d'ouverture
2. Distinguer temps de cycle et Lead Time, et expliquer pourquoi ils diffèrent d'un facteur 5 à 10
3. Identifier un goulot d'étranglement à partir d'un profil d'en-cours ou d'un diagramme Yamazumi
4. Expliquer l'effet d'une réduction du WIP sur le Lead Time
5. Énoncer la condition de validité de la loi de Little et dire pourquoi elle échoue en flux poussé
6. Calculer un TRG à partir de relevés bruts et en identifier la composante limitante
7. Reconnaître la surproduction comme un gaspillage, y compris quand elle prend la forme d'une performance apparente

---

*Pôle Formation UIMM CVDL  |  S. Jaubert  |  Guide Formateur v2.0  |  Juillet 2026*
