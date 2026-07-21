---
exported: 2026-07-21T07:08:32.030Z
source: NotebookLM
type: note
title: "Guide Pratique de la Maîtrise Statistique des Processus"
---

# Guide Pratique de la Maîtrise Statistique des Processus

导出时间: 21/07/2026 09:08:32

---

Voici une proposition de 4 Travaux Pratiques (TP) de découverte, conçus spécifiquement pour des Techniciens Qualité. Ces ateliers sont inspirés des meilleures pratiques industrielles, des normes statistiques et des approches pédagogiques reconnues (comme celles de W. Edwards Deming ou de l'AIAG).

Ils suivent une progression logique : sensibilisation, contrôle, mesure de la performance, et réaction.

### TP 1 : La Variabilité et le Piège du Sur-réglage (L'expérience de l'entonnoir)

**Objectif :** Comprendre la différence entre causes communes (bruit de fond) et causes spéciales, et démontrer que vouloir corriger un processus stable dégrade la qualité\[1\].**Matériel :** Un entonnoir sur un support, une bille, une feuille de papier avec une cible dessinée, un stylo\[1\]\[3\].

**Déroulement :**Demandez aux techniciens de simuler un processus de fabrication en faisant tomber la bille à travers l'entonnoir pour atteindre la cible, en testant 4 stratégies (règles de Deming) avec 50 lancers chacune\[1\]\[3\] :

1.  **Règle 1 (Ne rien toucher) :** L'entonnoir reste fixe au-dessus de la cible. On marque les points de chute\[1\]\[4\].
2.  **Règle 2 (Compensation inverse) :** Après chaque lancer, on mesure l'écart et on déplace l'entonnoir de cette même distance dans la direction opposée par rapport à sa _position précédente_\[1\]\[4\].
3.  **Règle 3 (Effet Nœud papillon) :** On déplace l'entonnoir à l'exact opposé du point de chute de la dernière bille, par rapport _au centre de la cible_\[1\]\[4\].
4.  **Règle 4 (Marche aléatoire) :** L'opérateur déplace l'entonnoir exactement sur le point de chute de la dernière bille\[1\]\[4\].

**Conclusion du TP :**Les techniciens constateront visuellement que la Règle 1 produit la plus faible dispersion\[4\]. Les ajustements intempestifs (sur-réglage) détériorent les performances et augmentent la variance\[1\]. La leçon : **on ne règle jamais un processus soumis uniquement à des causes communes (aléatoires)**\[2\]\[4\].

* * *

### TP 2 : Le Tir sur Cible (Découverte de Cp et Cpk)

**Objectif :** Assimiler les concepts de Capabilité Potentielle (Cp) et de Capabilité Réelle (Cpk) sans se perdre dans les mathématiques\[5\]\[6\].**Matériel :** Une cible de fléchettes (ou une représentation graphique) et des gommettes\[5\].

**Déroulement :**La cible représente l'intervalle de tolérance, le centre est la valeur nominale, et les impacts sont les pièces produites\[5\]. Proposez 3 scénarios à analyser aux techniciens :

-   **Scénario 1 :** Les impacts sont très groupés (faible dispersion), mais décalés hors du centre de la cible.
    -   _Analyse :_ Le **Cp est bon** (le procédé est précis), mais le **Cpk est mauvais** car le processus est décentré\[2\]\[5\].
    -   _Action qualité :_ Un simple recentrage de la machine suffit\[2\].
-   **Scénario 2 :** Les impacts sont centrés, mais très éparpillés partout sur la cible et en dehors.
    -   _Analyse :_ Le **Cp est mauvais** et le **Cpk est mauvais**\[5\].
    -   _Action qualité :_ Il faut réduire la variabilité (usure de l'outil, jeu mécanique, méthode). Un réglage ne servira à rien\[2\]\[6\].
-   **Scénario 3 :** Les impacts sont parfaitement groupés et centrés.
    -   _Analyse :_ Les deux indices **Cp et Cpk sont bons** (ex: > 1,33). La machine ne produit que des pièces conformes\[2\]\[5\].

**Conclusion du TP :**Le Cp mesure la largeur de la dispersion par rapport à la tolérance (la voiture rentre-t-elle dans le garage ?), tandis que le Cpk vérifie le centrage (la voiture est-elle garée au milieu ?)\[7\].

* * *

### TP 3 : Construction d'une Carte de Contrôle Xbar-R pas-à-pas

**Objectif :** Créer l'outil visuel de pilotage de la MSP pour passer d'une logique de détection à une logique de prévention\[7\]\[8\].**Prérequis stipulé :** Avant toute carte, on vérifie que le système de mesure est valide (étude Gage R&R < 10%) pour ne pas mesurer l'erreur de l'instrument\[2\]\[9\].**Matériel :** Un pied à coulisse, un lot de 50 pièces produites (ou des données simulées), un calculateur ou un tableur\[6\]\[10\].

**Déroulement :**

1.  **Échantillonnage :** Diviser les pièces en 10 sous-groupes de 5 pièces fabriquées consécutivement\[6\]\[10\].
2.  **Calculs :** Pour chaque sous-groupe, les techniciens calculent la moyenne (Xˉ) et l'étendue (R = valeur Max - valeur Min)\[8\]\[10\].
3.  **Traçage :** Sur un graphique, ils placent les moyennes journalières/horaires\[10\].
4.  **Définition des Limites :** Ils calculent la Ligne Centrale, la Limite Supérieure de Contrôle (UCL) et la Limite Inférieure de Contrôle (LCL) en utilisant les constantes statistiques (ex: A2​, D3​, D4​)\[2\]\[11\]._Attention piège formateur :_ Insistez sur le fait que **les limites de contrôle ne sont pas les limites de tolérance client (LSL/USL)**\[2\]\[10\]. Elles représentent la voix du processus, pas la voix du client.

* * *

### TP 4 : Détecter et Réagir avec l'OCAP (Out of Control Action Plan)

**Objectif :** S'entraîner à lire les signaux d'alarme sur une carte de contrôle et appliquer une procédure de réaction standardisée\[2\]\[12\].**Matériel :** Plusieurs exemples imprimés de cartes de contrôle présentant des dérives typiques (Règles de Nelson/Western Electric)\[2\]\[8\].

**Déroulement :**Distribuez les graphiques aux techniciens. Demandez-leur d'identifier les signaux de "causes spéciales" d'instabilité, par exemple :

-   Un point en dehors des limites de contrôle (UCL/LCL)\[2\].
-   6 points consécutifs en hausse ou en baisse constante (tendance)\[2\]\[11\].
-   9 points consécutifs du même côté de la ligne centrale\[2\]\[11\].

Une fois l'alarme identifiée, faites-leur dérouler un **OCAP (Plan d'Action Hors-Contrôle)** en 5 étapes, comme sur le terrain\[2\] :

1.  **Blocage (Hold) :** Stopper la production et isoler le lot suspect\[2\]\[13\].
2.  **Validation :** Vérifier que l'instrument de mesure ou l'opérateur n'est pas en cause (faux positif)\[2\].
3.  **Analyse Causes Racines :** Utiliser un diagramme d'Ishikawa (5M) pour trouver ce qui a perturbé le système\[2\]\[14\].
4.  **Correction :** Régler le problème et mesurer un échantillon de requalification pour vérifier le retour sous contrôle\[2\].
5.  **Capitalisation :** Enregistrer l'incident dans le journal de bord\[2\].

Ces exercices pratiques permettront aux Techniciens Qualité de comprendre que la MSP n'est pas qu'un exercice mathématique, mais un véritable outil de pilotage pour éviter la "surqualité" et les rebuts, tout en rendant le processus prévisible\[7\]\[15\].
---

## 引用来源

[1] Capabilités selon l'ISO 22514 - EURO-SYMBIOSE
[2] Choisir les bornes dans les cartes de contrôle
[3] Choisir les bornes dans les cartes de contrôle
[4] Capabilités selon l'ISO 22514 - EURO-SYMBIOSE
[5] Améliorer la performance de production par la MSP - SMACA
[6] Cartes de contrôle - explication simple | numiqo - Calculateur statistique
[7] Cartes de contrôle - explication simple | numiqo - Calculateur statistique
[8] Comment calculer Cp et Cpk - Cabinet de Conseil et de Formation en Qualité | ISO 9001
[9] Améliorer la performance de production par la MSP - SMACA
[10] Améliorer la performance de production par la MSP - SMACA
[11] Choisir les bornes dans les cartes de contrôle
[12] Cartes de contrôle - explication simple | numiqo - Calculateur statistique
[13] Choisir les bornes dans les cartes de contrôle
[14] Cartes de contrôle - explication simple | numiqo - Calculateur statistique
[15] Améliorer la performance de production par la MSP - SMACA
