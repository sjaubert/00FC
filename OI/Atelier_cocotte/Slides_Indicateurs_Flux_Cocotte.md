![Logo UIMM](logo_uimm_placeholder.jpg)

**Pôle Formation UIMM - CVDL**

---

# Les Indicateurs des Flux de Production
## Synthèse pour l'Atelier Cocotte LEAN

---

## 1. Pourquoi mesurer le flux ?

*   **Rendre visible** la performance (Qualité, Délais, Productivité)
*   **Identifier les gaspillages** (Muda) et les goulots d'étranglement
*   **Fixer un cap** : mesurer permet de savoir d'où l'on part pour s'améliorer (Kaizen)
*   Trois piliers interdépendants mesurés dans cet atelier : **WIP, Débit et Lead Time**

---

## 2. Le Taux de Qualité

**Principe : La conformité passe toujours avant la quantité.**

*   **Production Totale** = Nombre de cocottes terminées (bonnes + défectueuses)
*   **Taux de Qualité** = `(Cocottes conformes / Cocottes terminées) × 100`%
*   **Règle d'or** : Une cocotte présentant un défaut (symétrie, mobilité, propreté) n'est jamais recomptée en production bonne.

---

## 3. Le WIP (Work In Progress / En-cours)

**Indicateur : Les en-cours de production.**

*   **Définition** : Nombre total de pièces en cours de fabrication à un instant précis.
*   **Périmètre** : Toutes les cocottes ayant quitté le stock de matière première, mais qui n'ont pas encore passé le contrôle qualité (P5).
*   **Constat** : Un WIP élevé masque les vrais problèmes, engendre du stress et allonge drastiquement les délais de livraison. 
*   **Solution** : Le Kanban limite mathématiquement le WIP (Round 2).

---

## 4. Le Débit (Throughput) et le Goulot

**Indicateur : La vitesse de sortie du système.**

*   **Définition** : Le nombre de cocottes terminées par unité de temps.
*   **Calcul** : `Débit = Cocottes terminées / Durée (en minutes)`
*   **Le Goulot** : Le débit global de toute la ligne est dicté par le poste le plus lent. Augmenter la capacité des autres postes ne sert à rien s'ils ne sont pas le goulot.

---

## 5. Le Lead Time (Temps de traversée)

**Indicateur : Le délai promis au client.**

*   **Définition** : Le temps total qui s'écoule entre l'entrée d'une feuille brute au Poste 1 et la sortie d'une cocotte terminée au Poste 5.
*   **Enjeux** : Plus le système est chargé en en-cours (Round 1), plus une pièce met du temps à le traverser. (Ex : ~18 min)
*   Réduire le Lead Time, c'est gagner en agilité logistique et en temps de réponse aux clients. (Ex : ~5 min en flux tiré Kanban)

---

## 6. La Loi de Little

**L'équation fondamentale de gestion des flux de production.**

> **WIP = Débit × Lead Time**

*   **Ce que cela signifie :**
    Si l'on cherche à réduire nos délais (Lead Time) pour un débit donné, il n'y a qu'une méthode efficace et immédiate : **il faut réduire le nombre d'en-cours (WIP) sur les lignes**.

---

## 7. Le Takt Time

**Indicateur : Le rythme du monde extérieur.**

*   **Définition** : Le rythme de production imposé par la demande du client. 
*   **Calcul** : `Takt Time = Temps d'ouverture / Demande client`
*   **Exemple** : 
    Demande de 100 cocottes sur 60 minutes disponibles = 1 pièce demandée toutes les 36 secondes. 
    **Aucun** poste ne doit consommer un temps de cycle supérieur à ce Takt Time sous peine de générer des retards sur toute la ligne.

---

## 8. Le TRG (Taux de Rendement Global)

**Indicateur : La mesure universelle de performance.**

*   **Définition** : Mesure synthétique évaluant la performance des moyens disponibles.
*   `TRG = Disponibilité × Performance × Qualité`
*   **Le voyage vers l'excellence :**
    *   **Round 1 (Poussé)** : ~45% (La quantité ne compense pas les défauts)
    *   **Round 3 (Kaizen)** : > 90% (Classe mondiale, sérénité au poste)

---

## Synthèse Conclusion

| Indicateur clé | Pourquoi le suivre ? |
| :--- | :--- |
| **Taux de Qualité** | S'assurer qu'on produit utile et conforme. |
| **WIP (En-cours)** | C'est le cholestérol de l'atelier ! À réduire. |
| **Lead Time** | C'est le délai subi par notre client. |
| **Débit** | Prouve la régularité et la capacité de la ligne. |
| **Takt Time** | C'est le "métronome" calé sur les commandes. |
| **TRG** | L'indicateur final qui atteste de l'Excellence. |
