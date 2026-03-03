![Logo UIMM](../logo_uimm.jpg)

# Pole Formation UIMM-CVDL

---

# LE BEER GAME - LIVRET STAGIAIRE

## Simulation de Chaine d'Approvisionnement

**Duree** : 4 heures  
**Votre role** : Gestionnaire d'un maillon de la chaine logistique

---

## CONTEXTE

Vous travaillez dans une chaine d'approvisionnement de biere. Votre entreprise fait partie d'une chaine a 4 niveaux :

```
USINE --> DISTRIBUTEUR --> GROSSISTE --> DETAILLANT --> CONSOMMATEUR
```

Votre mission : **gerer votre stock** pour satisfaire vos clients tout en minimisant vos couts.

---

## VOTRE POSTE

### Nom : _________________________________

### Role attribue (cochez)

- [ ] **DETAILLANT** : Vous vendez au consommateur final
- [ ] **GROSSISTE** : Vous approvisionnez les detaillants
- [ ] **DISTRIBUTEUR** : Vous approvisionnez les grossistes
- [ ] **USINE** : Vous produisez la biere

---

## LES COUTS

| Type | Cout | Ce que ca signifie |
|------|------|-------------------|
| **Stockage** | 0,50 EUR / caisse / semaine | Chaque caisse que vous gardez en stock vous coute |
| **Rupture** | 1,00 EUR / caisse manquante / semaine | Chaque caisse que vous devez mais ne pouvez pas livrer coute le double |

**Objectif** : Minimiser le total de vos couts sur 40 semaines.

---

## SEQUENCE D'UNE SEMAINE

A chaque tour (= 1 semaine), effectuez ces etapes DANS L'ORDRE :

### Etape 1 : Recevoir les livraisons

Prenez les caisses qui arrivent de votre fournisseur (zone "Delai S2") et ajoutez-les a votre stock.

### Etape 2 : Recevoir la commande client

Lisez la commande que votre client vous envoie. Ne la montrez pas aux autres joueurs.

### Etape 3 : Livrer

Envoyez les caisses demandees a votre client.

- Si vous avez assez de stock : livrez la totalite
- Si vous n'avez pas assez : livrez ce que vous pouvez et notez le reste en "arrieres"

### Etape 4 : Enregistrer

Notez sur votre fiche :

- Votre stock restant
- Vos arrieres (commandes non satisfaites)

### Etape 5 : Passer commande

Decidez combien de caisses vous voulez commander a votre fournisseur.
Ecrivez ce nombre sur un bon de commande et envoyez-le.

### Etape 6 : Calculer vos couts

```
Cout semaine = (Stock x 0,50) + (Arrieres x 1,00)
```

---

## REGLES IMPORTANTES

1. **PAS DE COMMUNICATION** entre les postes (sauf bons de commande)
2. Vous ne pouvez pas annuler une commande deja passee
3. Les arrieres s'accumulent d'une semaine a l'autre
4. Il y a un delai de 2 semaines entre votre commande et la livraison

---

## TABLEAU DE DECISIONS (40 semaines)

| Sem | Recu fournisseur | Commande client | Livre | Stock fin | Arrieres | Commande passee | Cout semaine |
|-----|------------------|-----------------|-------|-----------|----------|-----------------|--------------|
| 1 | | | | 12 | 0 | | |
| 2 | | | | | | | |
| 3 | | | | | | | |
| 4 | | | | | | | |
| 5 | | | | | | | |
| 6 | | | | | | | |
| 7 | | | | | | | |
| 8 | | | | | | | |
| 9 | | | | | | | |
| 10 | | | | | | | |
| 11 | | | | | | | |
| 12 | | | | | | | |
| 13 | | | | | | | |
| 14 | | | | | | | |
| 15 | | | | | | | |
| 16 | | | | | | | |
| 17 | | | | | | | |
| 18 | | | | | | | |
| 19 | | | | | | | |
| 20 | | | | | | | |
| 21 | | | | | | | |
| 22 | | | | | | | |
| 23 | | | | | | | |
| 24 | | | | | | | |
| 25 | | | | | | | |
| 26 | | | | | | | |
| 27 | | | | | | | |
| 28 | | | | | | | |
| 29 | | | | | | | |
| 30 | | | | | | | |
| 31 | | | | | | | |
| 32 | | | | | | | |
| 33 | | | | | | | |
| 34 | | | | | | | |
| 35 | | | | | | | |
| 36 | | | | | | | |
| 37 | | | | | | | |
| 38 | | | | | | | |
| 39 | | | | | | | |
| 40 | | | | | | | |

**TOTAL COUTS** : _____________ EUR

---

## CALCUL FINAL

### Mes couts totaux

| Type | Formule | Montant |
|------|---------|---------|
| Stockage | Somme des stocks x 0,50 | EUR |
| Ruptures | Somme des arrieres x 1,00 | EUR |
| **TOTAL** | | **EUR** |

### Comparaison avec les autres postes

| Poste | Cout total |
|-------|------------|
| Detaillant | EUR |
| Grossiste | EUR |
| Distributeur | EUR |
| Usine | EUR |
| **TOTAL CHAINE** | **EUR** |

---

## MES OBSERVATIONS

### Pendant le jeu

A quel moment me suis-je senti deborde ?
_______________________________________________

Qu'est-ce qui m'a le plus frustre ?
_______________________________________________

De qui pensais-je que c'etait la faute ?
_______________________________________________

### Apres le debriefing

Quelle etait la vraie demande du consommateur ?
_______________________________________________

Pourquoi les commandes ont-elles autant fluctue ?
_______________________________________________

Qu'aurais-je du faire differemment ?
_______________________________________________

---

## SYNTHESE - L'EFFET COUP DE FOUET

### Definition

L'effet coup de fouet (Bullwhip Effect) est l'amplification des variations de demande au fur et a mesure qu'on remonte la chaine d'approvisionnement.

### Causes principales

| Cause | Explication |
|-------|-------------|
| Delais | Les informations et livraisons prennent du temps |
| Batching | On commande par gros lots plutot que au fil de l'eau |
| Anticipation | On sur-commande par peur de manquer |
| Isolement | Chaque maillon ne voit que son voisin immediat |

### Solutions industrielles

| Solution | Principe |
|----------|----------|
| VMI | Le fournisseur gere le stock du client |
| EDI | Partage electronique des donnees |
| CPFR | Planification collaborative des previsions |
| Cross-docking | Suppression des stocks intermediaires |

---

## TRANSFERT VERS MON ENTREPRISE

**Un phenomene similaire que j'ai observe dans mon entreprise/stage :**
_______________________________________________
_______________________________________________

**Une action d'amelioration que je peux proposer :**
_______________________________________________
_______________________________________________

**Ce que j'ai appris aujourd'hui :**
_______________________________________________
_______________________________________________

---

## LEXIQUE

| Terme | Definition |
|-------|------------|
| **Arrieres** | Commandes recues mais non encore livrees |
| **Bullwhip Effect** | Effet coup de fouet, amplification des variations |
| **CPFR** | Collaborative Planning, Forecasting and Replenishment |
| **EDI** | Echange de Donnees Informatise |
| **Lead Time** | Delai entre la commande et la livraison |
| **Stock** | Quantite de produits disponibles |
| **VMI** | Vendor Managed Inventory (stock gere par le fournisseur) |

---

**Document Pole Formation UIMM-CVDL**
