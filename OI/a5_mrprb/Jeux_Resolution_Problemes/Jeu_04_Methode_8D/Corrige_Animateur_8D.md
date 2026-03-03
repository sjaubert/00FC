---
output:
  word_document: default
  html_document: default
---
![Logo UIMM](../logo_uimm.jpg)

# Pôle Formation UIMM-CVDL

---

# MÉTHODE 8D - CORRIGÉ DÉTAILLÉ ANIMATEUR

## Jeu de Rôle : Investigation d'une Réclamation Client

**Document réservé à l'animateur - Ne pas distribuer aux stagiaires**

---

## TABLE DES MATIÈRES

1. [Rappel du scénario](#rappel-du-scénario)
2. [D0 - Préparation](#d0---préparation)
3. [D1 - Formation de l'équipe](#d1---formation-de-léquipe)
4. [D2 - Description du problème](#d2---description-du-problème)
5. [D3 - Actions conservatoires](#d3---actions-conservatoires)
6. [D4 - Analyse des causes racines](#d4---analyse-des-causes-racines)
7. [D5 - Choix des actions correctives](#d5---choix-des-actions-correctives)
8. [D6 - Mise en œuvre](#d6---mise-en-œuvre)
9. [D7 - Prévention de la récurrence](#d7---prévention-de-la-récurrence)
10. [D8 - Reconnaissance et clôture](#d8---reconnaissance-et-clôture)
11. [Grille de notation](#grille-de-notation)
12. [Erreurs fréquentes et pièges](#erreurs-fréquentes-et-pièges)

---

## 1. RAPPEL DU SCÉNARIO

### Situation initiale

- **Entreprise** : METALUX SAS, équipementier automobile rang 1
- **Client** : Stellantis (ex-PSA), usine de Sochaux
- **Produit** : Support de fixation étrier de frein (SUP-FRE-2847)
- **Problème** : 12 pièces avec défaut de soudure (porosité)
- **Impact** : Arrêt de ligne client pendant 2 heures
- **Lot concerné** : L2401-2847 (5000 pièces, fabriquées les 8-9 janvier 2026)
- **Délai demandé** : Rapport 8D sous 48 heures

### Indices clés à exploiter

| Indice | Information essentielle |
|--------|------------------------|
| Fiche produit | Spécification porosité max 2% |
| Plan de contrôle | Ressuage 1/500 (trop faible) |
| Historique machine | Signalement du 07/01 ignoré |
| Fiche opérateur | Thomas L. a mis du WD-40 |
| Bon de livraison fil | Stockage près de la porte (froid) |
| Analyse labo | Humidité + résidus organiques |

---

## 2. D0 - PRÉPARATION

### Corrigé attendu

| Critère | Évaluation | Justification |
|---------|------------|---------------|
| Impact sécurité | **OUI** | Pièce de frein = sécurité véhicule |
| Arrêt client | **OUI** | 2 heures d'arrêt ligne |
| Risque financier | **ÉLEVÉ** | 20 000 € arrêt + 50 000 € pénalités |
| Risque image | **ÉLEVÉ** | Risque de déréférencement |

**Priorité globale** : **CRITIQUE**

### Points à vérifier

- Les stagiaires ont-ils identifié l'aspect sécurité (pièce de frein) ?
- Ont-ils chiffré l'impact financier ?
- La priorité CRITIQUE est-elle correctement justifiée ?

---

## 3. D1 - FORMATION DE L'ÉQUIPE

### Composition idéale de l'équipe

| Rôle | Profil attendu | Compétences clés |
|------|----------------|------------------|
| Pilote 8D | Responsable Qualité | Animation, rédaction, suivi |
| Expert Production | Chef d'atelier soudure | Connaissance process, paramètres |
| Expert Qualité | Technicien contrôle | Outils qualité, specs client |
| Expert Maintenance | Technicien maintenance | Robot KUKA, dévidoir |
| Expert Logistique | Responsable magasin | Stockage consommables |

### Points à vérifier

- L'équipe est-elle pluridisciplinaire ?
- Le pilote est-il clairement identifié ?
- Manque-t-il des compétences clés ? (logistique souvent oubliée)

---

## 4. D2 - DESCRIPTION DU PROBLÈME

### Corrigé QQOQCP

| Question | Réponse attendue |
|----------|------------------|
| **QUOI** | Défaut de soudure par porosité excessive (8-12% au lieu de 2% max) sur supports de fixation étrier de frein |
| **QUI** | Détecté par : contrôle qualité Stellantis Sochaux. Concernés : METALUX (fournisseur), Stellantis (client) |
| **OÙ** | Ligne d'assemblage Stellantis Sochaux. Origine : atelier soudure METALUX, robot KUKA KR16 |
| **QUAND** | Détection : 15 janvier 2026. Fabrication : 8-9 janvier 2026. Livraison : 12 janvier 2026 |
| **COMMENT** | Soudures poreuses visibles, non-conformes aux spécifications, arrêt ligne client |
| **COMBIEN** | 12 pièces détectées défectueuses sur 5000 livrées (0,24%). Lot L2401-2847 entièrement suspect |

### Corrigé IS / IS NOT

| Aspect | EST (IS) | N'EST PAS (IS NOT) |
|--------|----------|-------------------|
| **Quoi** | Porosité soudure SUP-FRE-2847 | Autres défauts (géométrie, aspect) |
| **Où** | Lot L2401-2847, robot KUKA KR16 | Autres lots, autres machines |
| **Quand** | 8-9 janvier 2026 | Avant le 8 janvier, après le 9 janvier |
| **Combien** | 12 pièces détectées, potentiellement tout le lot | Lots précédents (L2401-2845, etc.) |

### Points à vérifier

- Le problème est-il bien **quantifié** (8-12% vs 2%) ?
- Les stagiaires ont-ils identifié que TOUT le lot est suspect ?
- La distinction IS/IS NOT permet-elle de cibler l'investigation ?

---

## 5. D3 - ACTIONS CONSERVATOIRES

### Corrigé des actions (dans l'ordre de priorité)

| N° | Action | Responsable | Délai | Justification |
|----|--------|-------------|-------|---------------|
| 1 | **Alerte immédiate au client** : informer Stellantis du problème et des actions en cours | Responsable Qualité | Immédiat (1h) | Obligation contractuelle, maintien confiance |
| 2 | **Blocage stock interne** : bloquer les 1200 pièces restantes du lot L2401-2847 | Responsable Logistique | Immédiat | Éviter livraison de pièces suspectes |
| 3 | **Tri chez le client** : demander à Stellantis d'isoler les pièces non montées du lot | Responsable Qualité | 24h | Limiter les montages de pièces non conformes |
| 4 | **Contrôle 100% ressuage** du stock bloqué | Technicien Qualité | 48h | Identifier toutes les pièces défectueuses |
| 5 | **Renfort contrôle production** : contrôle ressuage 100% sur la production en cours | Chef d'atelier | Immédiat | Garantir la qualité des nouvelles livraisons |
| 6 | **Arrêt utilisation bobine fil suspecte** | Chef d'atelier | Immédiat | Éliminer la source potentielle |

### Points à vérifier

- L'alerte client est-elle IMMÉDIATE ?
- Les actions protègent-elles le client EN PREMIER ?
- Le stock est-il bloqué ?
- Les stagiaires pensent-ils à la production EN COURS ?

### Erreur fréquente

> **Piège** : Se lancer dans l'analyse des causes (D4) avant d'avoir protégé le client (D3).
> Rappeler que D3 doit être terminé avant de passer à D4.

---

## 6. D4 - ANALYSE DES CAUSES RACINES

### Corrigé Diagramme Ishikawa

```
                           MAIN D'ŒUVRE
                           - Opérateur intérimaire peu formé
                           - Signalement du 07/01 non pris en compte
                           - Application de WD-40 par Thomas L.
                                    |
                   +----------------+----------------+
                   |                                 |
        MÉTHODE    |                                 |    MATIÈRE
        - Pas de procédure stockage fil             - Fil de soudure oxydé
        - Plan de contrôle non revu (3 ans)         - Humidité dans le fil
        - Fréquence ressuage insuffisante           - Contamination huile (WD-40)
                   |                                 |
       +-----------+                                 +-----------+
       |                                                         |
       |              DÉFAUT DE SOUDURE                          |
       |                 POROSITÉ                                |
       |                                                         |
       +-----------+                                 +-----------+
                   |                                 |
          MILIEU   |                                 |    MACHINE
          - Stockage près de la porte               - Dévidoir difficile à tourner
          - Température négative (-5°C)             - Robot KUKA OK (maintenance faite)
          - Condensation sur bobine
                   |
                   +----------------+----------------+
                                    |
```

### Corrigé 5 Pourquoi - Cause d'OCCURRENCE

| N° | Pourquoi ? | Réponse |
|----|------------|---------|
| 1 | Pourquoi la soudure est-elle poreuse ? | Présence d'humidité et de contaminants (huile) dans le bain de fusion |
| 2 | Pourquoi y avait-il de l'humidité et de l'huile ? | Le fil de soudure était oxydé/humide ET l'opérateur a appliqué du WD-40 sur le dévidoir |
| 3 | Pourquoi le fil était-il humide ? | La bobine a été stockée près de la porte du quai, exposée au froid (-5°C) et à la condensation |
| 4 | Pourquoi la bobine a-t-elle été stockée là ? | Il n'y avait plus de place dans le magasin et aucune zone de stockage dédiée n'était définie |
| 5 | **Pourquoi pas de zone de stockage définie ?** | **Procédure de stockage des consommables inexistante** |

**CAUSE RACINE D'OCCURRENCE** : Absence de procédure de stockage des consommables de soudure (fil, gaz)

### Corrigé 5 Pourquoi - Cause de NON-DÉTECTION

| N° | Pourquoi ? | Réponse |
|----|------------|---------|
| 1 | Pourquoi le défaut n'a-t-il pas été détecté ? | Le contrôle visuel 100% ne permet pas de détecter la porosité interne |
| 2 | Pourquoi pas de contrôle adapté (ressuage) plus fréquent ? | La fréquence de ressuage est de 1/500, insuffisante pour ce type de risque |
| 3 | **Pourquoi cette fréquence est-elle insuffisante ?** | **Le plan de contrôle n'a pas été revu depuis 3 ans, l'AMDEC n'est pas à jour** |

**CAUSE RACINE DE NON-DÉTECTION** : Plan de contrôle obsolète, AMDEC process non revue depuis 3 ans

### Causes secondaires à mentionner

1. **Facteur humain** : Le signalement de Martin D. le 07/01 ("soudure moins brillante") n'a pas été pris en compte par le chef d'équipe
2. **Formation insuffisante** : Thomas L. (intérimaire) n'a pas été formé aux bonnes pratiques (interdiction d'utiliser des lubrifiants)
3. **Management** : Le chef d'équipe a minimisé le signalement ("c'est normal en hiver")

### Points à vérifier

- Les stagiaires ont-ils trouvé les DEUX causes racines (occurrence ET non-détection) ?
- Sont-ils remontés aux causes ORGANISATIONNELLES et pas seulement techniques ?
- Le rôle du WD-40 est-il identifié comme aggravant ?
- Le signalement ignoré du 07/01 est-il mentionné ?

---

## 7. D5 - CHOIX DES ACTIONS CORRECTIVES

### Corrigé des actions correctives

| Cause à traiter | Action proposée | Efficacité | Faisabilité | Score | Retenue |
|-----------------|-----------------|------------|-------------|-------|---------|
| Stockage fil non contrôlé | Créer zone stockage chauffée (>10°C, <60% HR) | 5 | 4 | 20 | OUI |
| Procédure stockage inexistante | Rédiger et déployer procédure stockage consommables | 5 | 5 | 25 | OUI |
| Opérateurs non formés | Former tous les opérateurs (CDI + intérim) aux bonnes pratiques | 5 | 4 | 20 | OUI |
| Fréquence ressuage insuffisante | Augmenter fréquence ressuage à 1/100 | 4 | 5 | 20 | OUI |
| Plan de contrôle obsolète | Réviser le plan de contrôle et l'AMDEC process | 5 | 3 | 15 | OUI |
| Signalement non pris en compte | Mettre en place système de remontée d'alertes | 4 | 4 | 16 | OUI |
| Utilisation produits non validés | Interdire formellement l'utilisation de lubrifiants sur machines | 5 | 5 | 25 | OUI |

### Points à vérifier

- Chaque cause racine a-t-elle une action corrective associée ?
- Les actions sont-elles SMART (Spécifiques, Mesurables, Atteignables, Réalistes, Temporelles) ?
- Les scores efficacité/faisabilité sont-ils cohérents ?

---

## 8. D6 - MISE EN ŒUVRE

### Corrigé du plan de mise en œuvre

| N° | Action | Responsable | Délai | Vérification | Statut |
|----|--------|-------------|-------|--------------|--------|
| 1 | Créer zone stockage fil chauffée avec contrôle température/humidité | Responsable Logistique | J+7 | Relevé T°/HR quotidien |  |
| 2 | Rédiger procédure stockage consommables soudure | Responsable Qualité | J+5 | Validation Direction |  |
| 3 | Déployer procédure (affichage, formation) | Chef d'atelier | J+10 | Émargement stagiaires |  |
| 4 | Former opérateurs CDI (bonnes pratiques soudure) | RH + Qualité | J+14 | Évaluation acquis |  |
| 5 | Former intérimaires à chaque arrivée (livret accueil) | RH + Chef équipe | Permanent | Signature livret |  |
| 6 | Augmenter fréquence ressuage à 1/100 | Qualité | Immédiat | Enregistrements contrôle |  |
| 7 | Réviser plan de contrôle | Qualité | J+30 | Approbation client |  |
| 8 | Mettre à jour AMDEC process | Qualité + Production | J+45 | Réunion AMDEC |  |
| 9 | Créer système alerte (fiche de signalement) | Qualité | J+7 | Tableau de suivi |  |
| 10 | Afficher interdiction lubrifiants sur machines | Chef d'atelier | J+2 | Audit terrain |  |

### Vérification de l'efficacité

Pour chaque action, prévoir une méthode de vérification :

- **Zone stockage** : Relevés température/humidité pendant 1 mois, absence de nouvelle non-conformité liée au fil
- **Formation** : Évaluation des connaissances, observation terrain
- **Ressuage** : Taux de détection interne vs chez client
- **Système alerte** : Nombre de fiches remplies, délai de traitement

---

## 9. D7 - PRÉVENTION DE LA RÉCURRENCE

### Corrigé des actions de prévention

| Type | Action | Responsable | Délai | Livrables |
|------|--------|-------------|-------|-----------|
| **AMDEC** | Réviser AMDEC process avec nouveau mode de défaillance "stockage consommables" | Qualité + Production | J+45 | Nouvelle cotation, actions préventives |
| **Procédure** | Créer procédure de gestion des consommables (réception, stockage, utilisation, traçabilité) | Qualité | J+30 | Document qualité validé |
| **Formation** | Intégrer module "consommables soudure" dans formation opérateurs et livret intérim | RH | J+30 | Support de formation, livret mis à jour |
| **Poka-Yoke** | Installer capteur humidité sur dévidoir avec alarme | Maintenance | J+60 | Équipement installé et validé |
| **Audit** | Programmer audit 5S + consommables trimestriel | Qualité | Permanent | Check-list audit, planning |

### Extension à d'autres risques similaires

- Appliquer la même démarche aux autres consommables (gaz, électrodes)
- Vérifier les conditions de stockage dans les autres ateliers
- Partager le retour d'expérience avec les autres sites du groupe

---

## 10. D8 - RECONNAISSANCE ET CLÔTURE

### Leçons apprises

1. **Les consommables sont critiques** : Le stockage et la manutention des consommables de soudure ont un impact direct sur la qualité. Ils doivent être gérés comme des matières premières critiques.

2. **Écouter les signalements terrain** : Le signalement de l'opérateur Martin D. le 07/01 aurait pu éviter tout le problème s'il avait été pris au sérieux. Mettre en place un système de remontée d'alertes est essentiel.

3. **Former les intérimaires** : Les opérateurs temporaires doivent recevoir une formation adaptée incluant les interdictions et bonnes pratiques. Un livret d'accueil spécifique doit être créé.

4. **Revoir régulièrement les plans de contrôle** : Un plan de contrôle qui n'est pas revu depuis 3 ans devient obsolète. Programmer des révisions annuelles.

5. **La méthode 8D fonctionne** : Cette investigation structurée a permis d'identifier des causes profondes organisationnelles et pas seulement des causes techniques superficielles.

### Reconnaissance de l'équipe

- Remercier l'équipe 8D pour sa réactivité et la qualité de l'analyse
- Mettre en avant les contributions individuelles
- Partager le succès avec les opérateurs impliqués (Martin D. qui avait signalé le problème)
- Communiquer le retour d'expérience à l'ensemble du personnel

### Communication au client

- Envoyer le rapport 8D complet à Stellantis
- Proposer une visite (ou visio) pour présenter les actions
- Planifier un suivi à 3 mois pour confirmer l'efficacité
- Demander la clôture formelle de la réclamation

---

## 11. GRILLE DE NOTATION

### Évaluation des équipes (sur 100 points)

| Critère | Points max | Éléments attendus |
|---------|------------|-------------------|
| **D0-D1 Préparation** | 10 | Urgence bien évaluée, équipe complète |
| **D2 Description** | 20 | QQOQCP complet et précis, IS/IS NOT pertinent |
| **D3 Conservatoires** | 15 | Actions immédiates, client protégé en premier |
| **D4 Causes occurrence** | 20 | 5 Pourquoi complets, cause organisationnelle identifiée |
| **D4 Causes non-détection** | 15 | Fréquence contrôle, plan obsolète identifié |
| **D5-D6 Correctives** | 15 | Actions SMART, responsables et délais définis |
| **D7-D8 Prévention** | 10 | AMDEC mentionnée, leçons pertinentes |
| **Présentation** | 5 | Clarté, synthèse, argumentation |
| **BONUS** | +5 | Signalement ignoré du 07/01 mentionné |
| **TOTAL** | **110** | (ramené sur 100 ou bonus gardé) |

### Barème détaillé D4 (Causes racines)

| Élément identifié | Points |
|-------------------|--------|
| Fil de soudure humide/oxydé | 3 |
| Stockage près de la porte (froid) | 3 |
| Absence de zone de stockage dédiée | 3 |
| Procédure stockage inexistante (cause racine) | 5 |
| WD-40 appliqué par Thomas L. | 3 |
| Contrôle visuel insuffisant | 2 |
| Fréquence ressuage 1/500 trop faible | 3 |
| Plan de contrôle non revu 3 ans (cause racine) | 5 |
| Signalement du 07/01 ignoré (bonus) | 5 |

---

## 12. ERREURS FRÉQUENTES ET PIÈGES

### Erreurs à surveiller

| Erreur | Impact | Comment la corriger |
|--------|--------|---------------------|
| Sauter D3 pour aller à D4 | Client non protégé | Rappeler l'ordre impératif |
| S'arrêter aux causes techniques | Causes réelles non traitées | Demander "Pourquoi ?" supplémentaires |
| Oublier la non-détection | Récurrence probable | Rappeler les 2 types de causes |
| Actions trop vagues | Impossibles à suivre | Exiger SMART |
| Accuser les personnes | Démobilisation | Rappeler : causes système, pas individus |
| Ignorer le signalement du 07/01 | Leçon manquée | Guider vers cet indice |

### Questions de relance si les stagiaires sont bloqués

- "Le fil a-t-il toujours été stocké à cet endroit ?"
- "Que dit la notice de stockage du fil ?"
- "Y a-t-il eu des changements récents dans l'équipe ?"
- "Comment le contrôle aurait-il pu détecter ce défaut ?"
- "Depuis quand le plan de contrôle n'a-t-il pas été revu ?"

---

**Document créé par Pôle Formation UIMM-CVDL**  
**Version 1.0 - Février 2026**  
**RÉSERVÉ À L'ANIMATEUR**
