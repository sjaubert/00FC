![Logo UIMM](../logo_uimm.jpg)

# Pole Formation UIMM-CVDL

---

# TPM / MAINTENANCE - LIVRET STAGIAIRE

## Le Dilemme de Production

**Duree** : 4 heures  
**Votre role** : Responsable d'atelier

---

## CONTEXTE

Vous dirigez l'atelier de production de **PRODMAX Industries**. Votre mission : maximiser la production et la rentabilite sur 10 semaines, tout en gerant la maintenance de vos 4 machines.

---

## VOTRE ATELIER

```
[Machine A] --> [Machine B] --> [Machine C] --> [Machine D] --> Client
  Decoupe        Pliage          Soudure        Peinture
```

### Caracteristiques des machines

| Machine | Age | Fiabilite | Cout panne |
|---------|-----|-----------|------------|
| A - Decoupe | 8 ans | Moyenne | 2000 EUR |
| B - Pliage | 5 ans | Bonne | 1500 EUR |
| C - Soudure | 12 ans | Faible | 3000 EUR |
| D - Peinture | 3 ans | Tres bonne | 2500 EUR |

---

## VOTRE EQUIPE

### Nom : _________________________________

### Membres de l'equipe

1. _________________________________
2. _________________________________
3. _________________________________

---

## PARAMETRES ECONOMIQUES

| Element | Valeur |
|---------|--------|
| Prix de vente piece | 50 EUR |
| Cout production piece | 30 EUR |
| **Marge par piece** | **20 EUR** |
| Cadence | 10 pieces/heure |
| Temps disponible | 40h/semaine |
| Cout maintenance preventive | 500 EUR/machine/semaine |
| Cout horaire arret | 500 EUR/heure |

---

## REGLES DU JEU

### A chaque semaine

1. **Decider** : Maintenance preventive sur quelles machines ? (500 EUR chacune)
2. **Lancer les des** : Determiner les pannes eventuelles
3. **Gerer les pannes** : Priorite de reparation (1 seule equipe maintenance)
4. **Calculer** : Production et couts

### Regles des pannes

| Machine | Probabilite panne (sans preventif) |
|---------|-----------------------------------|
| A (8 ans) | De 1-2 sur D6 |
| B (5 ans) | De 1 sur D6 |
| C (12 ans) | De 1-2-3 sur D6 |
| D (3 ans) | De 1 sur D6 + D20 < 5 |

**Avec maintenance preventive** : Probabilite divisee par 2

---

## TABLEAU DE SUIVI - TOUR 1 (Semaines 1-4)

### Semaine 1

| Machine | Preventif ? | De | Panne ? | Duree arret | Cout |
|---------|-------------|----|---------| ------------|------|
| A | [ ] | | | | |
| B | [ ] | | | | |
| C | [ ] | | | | |
| D | [ ] | | | | |

**Heures disponibles apres pannes** : _____ h

**Production** : _____ pieces

**Calcul financier :**

- Chiffre d'affaires : _____ x 50 = _____ EUR
- Cout production : _____ x 30 = _____ EUR
- Cout pannes : _____ EUR
- Cout preventif : _____ EUR
- **Marge semaine** : _____ EUR

---

### Semaine 2

| Machine | Preventif ? | De | Panne ? | Duree arret | Cout |
|---------|-------------|----|---------| ------------|------|
| A | [ ] | | | | |
| B | [ ] | | | | |
| C | [ ] | | | | |
| D | [ ] | | | | |

**Production** : _____ pieces | **Marge** : _____ EUR

---

### Semaine 3

| Machine | Preventif ? | De | Panne ? | Duree arret | Cout |
|---------|-------------|----|---------| ------------|------|
| A | [ ] | | | | |
| B | [ ] | | | | |
| C | [ ] | | | | |
| D | [ ] | | | | |

**Production** : _____ pieces | **Marge** : _____ EUR

---

### Semaine 4

| Machine | Preventif ? | De | Panne ? | Duree arret | Cout |
|---------|-------------|----|---------| ------------|------|
| A | [ ] | | | | |
| B | [ ] | | | | |
| C | [ ] | | | | |
| D | [ ] | | | | |

**Production** : _____ pieces | **Marge** : _____ EUR

---

### Bilan Tour 1

| Indicateur | Valeur |
|------------|--------|
| Production totale | pieces |
| Nombre de pannes | |
| Cout total pannes | EUR |
| Cout total preventif | EUR |
| Marge totale | EUR |
| TRG moyen | % |

---

## FORMULES DE CALCUL

### MTBF (Mean Time Between Failures)

```
MTBF = Heures de fonctionnement / Nombre de pannes
```

### MTTR (Mean Time To Repair)

```
MTTR = Heures de reparation / Nombre de pannes
```

### TRG (Taux de Rendement Global)

```
TRG = Disponibilite x Performance x Qualite

Disponibilite = (Temps dispo - Arrets) / Temps dispo
Performance = Production reelle / Production theorique
Qualite = Pieces bonnes / Pieces totales
```

---

## TABLEAU DE SUIVI - TOUR 2 (Semaines 5-7)

### Semaine 5

| Machine | Preventif ? | De | Panne ? | Duree arret | Cout |
|---------|-------------|----|---------| ------------|------|
| A | [ ] | | | | |
| B | [ ] | | | | |
| C | [ ] | | | | |
| D | [ ] | | | | |

**Production** : _____ pieces | **Marge** : _____ EUR

---

### Semaine 6

| Machine | Preventif ? | De | Panne ? | Duree arret | Cout |
|---------|-------------|----|---------| ------------|------|
| A | [ ] | | | | |
| B | [ ] | | | | |
| C | [ ] | | | | |
| D | [ ] | | | | |

**Production** : _____ pieces | **Marge** : _____ EUR

---

### Semaine 7

| Machine | Preventif ? | De | Panne ? | Duree arret | Cout |
|---------|-------------|----|---------| ------------|------|
| A | [ ] | | | | |
| B | [ ] | | | | |
| C | [ ] | | | | |
| D | [ ] | | | | |

**Production** : _____ pieces | **Marge** : _____ EUR

---

### Bilan Tour 2

| Indicateur | Tour 1 | Tour 2 | Evolution |
|------------|--------|--------|-----------|
| Production | | | |
| Nb pannes | | | |
| Cout pannes | | | |
| Marge | | | |
| TRG | | | |

---

## TABLEAU DE SUIVI - TOUR 3 (Semaines 8-10)

### Semaine 8

| Machine | Preventif ? | De | Panne ? | Duree arret | Cout |
|---------|-------------|----|---------| ------------|------|
| A | [ ] | | | | |
| B | [ ] | | | | |
| C | [ ] | | | | |
| D | [ ] | | | | |

**Production** : _____ pieces | **Marge** : _____ EUR

---

### Semaine 9

| Machine | Preventif ? | De | Panne ? | Duree arret | Cout |
|---------|-------------|----|---------| ------------|------|
| A | [ ] | | | | |
| B | [ ] | | | | |
| C | [ ] | | | | |
| D | [ ] | | | | |

**Production** : _____ pieces | **Marge** : _____ EUR

---

### Semaine 10

| Machine | Preventif ? | De | Panne ? | Duree arret | Cout |
|---------|-------------|----|---------| ------------|------|
| A | [ ] | | | | |
| B | [ ] | | | | |
| C | [ ] | | | | |
| D | [ ] | | | | |

**Production** : _____ pieces | **Marge** : _____ EUR

---

## BILAN FINAL

| Indicateur | Tour 1 | Tour 2 | Tour 3 | Total |
|------------|--------|--------|--------|-------|
| Production | | | | |
| Pannes | | | | |
| Cout pannes | | | | |
| Cout preventif | | | | |
| **Marge nette** | | | | |
| TRG moyen | | | | |

---

## MA STRATEGIE OPTIMALE

Quelle strategie de maintenance ai-je adoptee ?

- Machine A : [ ] Curatif [ ] Preventif
- Machine B : [ ] Curatif [ ] Preventif
- Machine C : [ ] Curatif [ ] Preventif
- Machine D : [ ] Curatif [ ] Preventif

Pourquoi ?
_______________________________________________
_______________________________________________

---

## CE QUE J'AI APPRIS

### Sur le MTBF et MTTR

_______________________________________________

### Sur le TRG

_______________________________________________

### Sur l'arbitrage production/maintenance

_______________________________________________

---

## TRANSFERT VERS MON ENTREPRISE

Dans mon entreprise, quelle machine/equipement meriterait une meilleure maintenance preventive ?
_______________________________________________

Quel indicateur vais-je suivre ?
_______________________________________________

---

**Document Pole Formation UIMM-CVDL**
