---
output:
  word_document: default
  html_document: default
---

![](../Atelier_cocotte/logo_uimm_placeholder.jpg)

# TP : Pilotage de la Performance - Le TRS (Taux de Rendement Synthétique)

* **Thème** : Analyse des pertes et calcul d'indicateurs de performance
  **Public** : Électriciens de Maintenance de Systèmes Automatisés (EIMSA)

---

## 1. Mise en situation

Vous intervenez sur une **ensacheuse automatisée** de produits chimiques. Le responsable de production tire la sonnette d'alarme : *"La machine est censée produire 12 sacs par minute, mais à la fin de la journée, on est loin du compte. C'est encore la faute de la maintenance !"*

Votre mission est de calculer le TRS de la journée d'hier pour identifier si les pertes sont dues à la **disponibilité** (pannes), à la **performance** (vitesse) ou à la **qualité** (réglages).

---

## 2. Données de l'activité (Poste du 01 Avril)

* **Durée du poste** : 8 heures (08h00 - 16h00).
* **Pauses prévues** : 2 pauses de 15 min (machine arrêtée).
* **Nettoyage de fin de poste** : 20 min.
* **Arrêts machine constatés** :
  * Bourrage plastique (intervention opérateur) : 15 min.
  * **Panne capteur de pesage (votre intervention) : 45 min.**
  * Changement de série (format des sacs) : 30 min.
* **Vitesse de référence (Cadence théorique)** : 12 sacs / minute.
* **Production totale réalisée** : 3 200 sacs sur la journée.
* **Rebuts (Sacs percés ou poids incorrect)** : 85 sacs.

---

## 3. Activité 1 : Analyse du Temps de Production

L'objectif est de décomposer le temps pour comprendre où les minutes s'échappent.

**Travail à réaliser :**

1. **Temps d'Ouverture ($T_{o}$)** : Quelle est la durée totale du poste en minutes ?
2. **Temps Requis ($T_{r}$)** : Retranchez les arrêts planifiés (pauses et nettoyage). C'est le temps où la machine *doit* produire.
3. **Temps de Fonctionnement ($T_{f}$)** : Retranchez les arrêts non planifiés (pannes, réglages, bourrages). C'est le temps où la machine a *réellement* tourné.

---

## 4. Activité 2 : Calcul des Taux de Performance

**Travail à réaliser (Utilisez les formules suivantes) :**

1. **Taux de Disponibilité ($D_{o}$)** :

   $$
   \frac{Temps \ de \ Fonctionnement \ (T_{f})}{Temps \ Requis \ (T_{r})}
   $$
2. **Taux de Performance ($T_{p}$)** :

   $$
   \frac{Production \ réelle \times Temps \ de \ cycle \ théorique}{Temps \ de \ Fonctionnement \ (T_{f})}
   $$

   *(Note : Temps de cycle théorique = 1 minute / 12 sacs)*
3. **Taux de Qualité ($T_{q}$)** :

   $$
   \frac{Production \ totale - Rebuts}{Production \ totale}
   $$

---

## 5. Activité 3 : Synthèse et Diagnostic (30 min)

1. **Calcul du TRS** : Multipliez les trois taux obtenus ($TRS = D_{o} \times T_{p} \times T_{q}$).
2. **Analyse critique** :
   * Quel indicateur est le plus faible ?
   * Le responsable de production a-t-il raison de dire que c'est "uniquement" la faute de la maintenance ?
   * Proposez une solution technique pour améliorer le $T_{p}$ (Taux de Performance).

---

# CORRIGÉ (Réservé au Formateur)

### 1. Analyse des Temps

* **$T_{o}$** : 8h x 60 min = **480 min**.
* **$T_{r}$** : 480 - (2 x 15) - 20 = **430 min**.
* **$T_{f}$** : 430 - 15 (bourrage) - 45 (panne) - 30 (série) = **340 min**.

### 2. Calcul des Taux

* **Disponibilité ($D_{o}$)** : 340 / 430 = **79,07%**.
* **Performance ($T_{p}$)** :
  * Production idéale possible en 340 min : 340 x 12 = 4 080 sacs.
  * Taux : 3 200 / 4 080 = **78,43%**.
* **Qualité ($T_{q}$)** : (3 200 - 85) / 3 200 = **97,34%**.

### 3. Résultat Final

* **TRS** : 0,7907 x 0,7843 x 0,9734 = **60,37%**.

**Interprétation pour le groupe :** Le TRS est médiocre (~60%). La qualité est excellente, mais la machine perd énormément en **Disponibilité** (Pannes + Changements de série) et en **Performance** (elle tourne moins vite que sa capacité nominale).
