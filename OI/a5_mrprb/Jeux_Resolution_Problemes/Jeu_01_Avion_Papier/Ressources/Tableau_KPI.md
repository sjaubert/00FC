![Logo UIMM](../../logo_uimm.jpg)

# Pole Formation UIMM-CVDL

---

# TABLEAU DE SUIVI KPI - JEU AVION EN PAPIER

## Tableau principal (a afficher en grand format)

| Indicateur | Round 1 | Round 2 | Round 3 | Round 4 | Evolution |
|------------|---------|---------|---------|---------|-----------|
| **Lead Time** (min:sec) | | | | | |
| **WIP** (pieces en cours) | | | | | |
| **Avions livres** | | | | | |
| **Avions rebutes** | | | | | |
| **Taux qualite** (%) | | | | | |
| **Productivite** (avions/min) | | | | | |

---

## Formules de calcul

### Lead Time

Temps ecoule entre l'entree de la matiere premiere au Poste 1 et la livraison au Client.

### WIP (Work In Process)

Nombre de pieces en cours de fabrication a un instant T (entre les postes, non livrees).

### Taux de qualite

```
Taux qualite = (Avions conformes / Total produit) x 100
```

### Productivite

```
Productivite = Avions livres conformes / Temps de production (minutes)
```

### Evolution

```
Evolution = ((Valeur Round 4 - Valeur Round 1) / Valeur Round 1) x 100
```

---

## Graphique d'evolution (a tracer)

```
Lead Time (min)
    ^
 15 |  *
    |
 12 |     
    |        
  9 |     *
    |
  6 |         
    |             *
  3 |
    |                 *
  0 +--------------------> Rounds
       1     2     3     4
```

```
WIP (pieces)
    ^
 25 |  *
    |
 20 |     
    |        
 15 |     
    |
 10 |     *
    |         *
  5 |             *
    |
  0 +--------------------> Rounds
       1     2     3     4
```

---

## Comparatif systeme PUSH vs PULL

| Critere | PUSH (Round 1) | PULL (Rounds 2-4) |
|---------|----------------|-------------------|
| Declencheur production | Prevision | Demande reelle |
| Stocks intermediaires | Eleves | Limites |
| Lead Time | Long | Court |
| Visibilite problemes | Faible | Forte |
| Flexibilite | Faible | Forte |

---

## Objectifs cibles

| Indicateur | Objectif Round 4 |
|------------|------------------|
| Lead Time | < 2 minutes |
| WIP | < 4 pieces |
| Taux qualite | > 95% |
| Productivite | > 2 avions/min |

---

**Document Pole Formation UIMM-CVDL**
