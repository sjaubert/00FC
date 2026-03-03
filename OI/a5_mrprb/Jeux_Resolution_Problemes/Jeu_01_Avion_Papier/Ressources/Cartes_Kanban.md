![Logo UIMM](../../logo_uimm.jpg)

# Pole Formation UIMM-CVDL

---

# CARTES KANBAN - JEU AVION EN PAPIER

## Instructions d'utilisation

Les cartes Kanban sont utilisees a partir du Round 2. Chaque carte represente une autorisation de produire UNE piece.

**Regles :**

1. Le poste aval envoie une carte au poste amont quand il a besoin d'une piece
2. Le poste amont ne produit QUE s'il recoit une carte
3. La carte accompagne la piece jusqu'au poste suivant
4. Nombre maximum de cartes en circulation : 2 par liaison

---

## Cartes a decouper (20 cartes)

```
+------------------------+    +------------------------+
|                        |    |                        |
|  KANBAN                |    |  KANBAN                |
|                        |    |                        |
|  Produit : AVION       |    |  Produit : AVION       |
|  Quantite : 1          |    |  Quantite : 1          |
|                        |    |                        |
|  De : Poste ___        |    |  De : Poste ___        |
|  Vers : Poste ___      |    |  Vers : Poste ___      |
|                        |    |                        |
|  Carte n. ____         |    |  Carte n. ____         |
|                        |    |                        |
+------------------------+    +------------------------+

+------------------------+    +------------------------+
|                        |    |                        |
|  KANBAN                |    |  KANBAN                |
|                        |    |                        |
|  Produit : AVION       |    |  Produit : AVION       |
|  Quantite : 1          |    |  Quantite : 1          |
|                        |    |                        |
|  De : Poste ___        |    |  De : Poste ___        |
|  Vers : Poste ___      |    |  Vers : Poste ___      |
|                        |    |                        |
|  Carte n. ____         |    |  Carte n. ____         |
|                        |    |                        |
+------------------------+    +------------------------+

+------------------------+    +------------------------+
|                        |    |                        |
|  KANBAN                |    |  KANBAN                |
|                        |    |                        |
|  Produit : AVION       |    |  Produit : AVION       |
|  Quantite : 1          |    |  Quantite : 1          |
|                        |    |                        |
|  De : Poste ___        |    |  De : Poste ___        |
|  Vers : Poste ___      |    |  Vers : Poste ___      |
|                        |    |                        |
|  Carte n. ____         |    |  Carte n. ____         |
|                        |    |                        |
+------------------------+    +------------------------+

+------------------------+    +------------------------+
|                        |    |                        |
|  KANBAN                |    |  KANBAN                |
|                        |    |                        |
|  Produit : AVION       |    |  Produit : AVION       |
|  Quantite : 1          |    |  Quantite : 1          |
|                        |    |                        |
|  De : Poste ___        |    |  De : Poste ___        |
|  Vers : Poste ___      |    |  Vers : Poste ___      |
|                        |    |                        |
|  Carte n. ____         |    |  Carte n. ____         |
|                        |    |                        |
+------------------------+    +------------------------+

+------------------------+    +------------------------+
|                        |    |                        |
|  KANBAN                |    |  KANBAN                |
|                        |    |                        |
|  Produit : AVION       |    |  Produit : AVION       |
|  Quantite : 1          |    |  Quantite : 1          |
|                        |    |                        |
|  De : Poste ___        |    |  De : Poste ___        |
|  Vers : Poste ___      |    |  Vers : Poste ___      |
|                        |    |                        |
|  Carte n. ____         |    |  Carte n. ____         |
|                        |    |                        |
+------------------------+    +------------------------+
```

---

## Flux des cartes Kanban

```
CLIENT demande un avion
         |
         v
    Envoie carte au CONTROLE
         |
         v
    CONTROLE envoie carte au POSTE 4
         |
         v
    POSTE 4 envoie carte au POSTE 3
         |
         v
    POSTE 3 envoie carte au POSTE 2
         |
         v
    POSTE 2 envoie carte au POSTE 1
         |
         v
    POSTE 1 produit une piece
```

---

**Document Pole Formation UIMM-CVDL**
