![Logo UIMM](../../logo_uimm.jpg)

# Pole Formation UIMM-CVDL

---

# PLATEAU DE JEU - BEER GAME

## Disposition des postes

Le plateau se compose de 4 zones principales plus les zones de delai.

---

## Schema du plateau (a reproduire sur une grande table)

```
+==============================================================================+
|                                                                              |
|   +----------------+                                                         |
|   |                |                                                         |
|   |     USINE      |                                                         |
|   |                |                                                         |
|   |  Stock: ____   |                                                         |
|   |  Arrieres: ___ |                                                         |
|   +----------------+                                                         |
|          |                                                                   |
|          | Livraison                                                         |
|          v                                                                   |
|   +----------------+     +----------------+                                  |
|   |  DELAI S1      | --> |  DELAI S2      |                                  |
|   | (en production)|     | (en livraison) |                                  |
|   +----------------+     +----------------+                                  |
|                                 |                                            |
|                                 v                                            |
|   +----------------+                                                         |
|   |                |                                                         |
|   |  DISTRIBUTEUR  |<-- Commandes                                            |
|   |                |                                                         |
|   |  Stock: ____   |                                                         |
|   |  Arrieres: ___ |                                                         |
|   +----------------+                                                         |
|          |                                                                   |
|          | Livraison                                                         |
|          v                                                                   |
|   +----------------+     +----------------+                                  |
|   |  DELAI S1      | --> |  DELAI S2      |                                  |
|   +----------------+     +----------------+                                  |
|                                 |                                            |
|                                 v                                            |
|   +----------------+                                                         |
|   |                |                                                         |
|   |   GROSSISTE    |<-- Commandes                                            |
|   |                |                                                         |
|   |  Stock: ____   |                                                         |
|   |  Arrieres: ___ |                                                         |
|   +----------------+                                                         |
|          |                                                                   |
|          | Livraison                                                         |
|          v                                                                   |
|   +----------------+     +----------------+                                  |
|   |  DELAI S1      | --> |  DELAI S2      |                                  |
|   +----------------+     +----------------+                                  |
|                                 |                                            |
|                                 v                                            |
|   +----------------+                                                         |
|   |                |                                                         |
|   |   DETAILLANT   |<-- Commandes                                            |
|   |                |                                                         |
|   |  Stock: ____   |                                                         |
|   |  Arrieres: ___ |                                                         |
|   +----------------+                                                         |
|          |                                                                   |
|          | Livraison au client final                                         |
|          v                                                                   |
|   +----------------+                                                         |
|   |                |                                                         |
|   |  CONSOMMATEUR  |  (Joue par le formateur)                                |
|   |                |                                                         |
|   +----------------+                                                         |
|                                                                              |
+==============================================================================+
```

---

## Configuration initiale

Chaque poste demarre avec :

| Element | Quantite |
|---------|----------|
| Stock | 12 caisses |
| Arrieres | 0 |
| En transit (Delai S1) | 4 caisses |
| En transit (Delai S2) | 4 caisses |

---

## Materiel par zone

| Zone | Materiel |
|------|----------|
| Stock | Jetons ou pieces empilees |
| Arrieres | Pile de bons "non livres" |
| Delai S1 | Zone marquee au sol ou sur table |
| Delai S2 | Zone marquee au sol ou sur table |

---

## Legende des flux

```
-------> : Flux physique (caisses de biere)
<------- : Flux d'information (bons de commande)
```

---

**Document Pole Formation UIMM-CVDL**
