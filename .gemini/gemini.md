---
description: Instructions récurrentes pour le workspace 00FC — Organisation Industrielle
---
# Instructions Récurrentes — Pôle Formation UIMM-CVDL

## Identité de la structure

- **Nom de la structure** : Pôle Formation UIMM - CVDL
- **Formateur principal** : S. Jaubert
- **Logo** : Utiliser le fichier `logo_uimm_placeholder.jpg` situé à la racine du projet (`00FC/logo_uimm_placeholder.jpg`). Ce logo doit être copié dans le dossier de chaque document si nécessaire.

## Standards pour les fichiers Markdown (.md)

#### Pas d'émoji

1. **En-tête obligatoire** : Chaque fichier `.md` doit commencer par :

   ```markdown
   ![Logo UIMM](logo_uimm_placeholder.jpg)

   **Pôle Formation UIMM - CVDL**

   ---
   ```

2. **Sauts de page** : Insérer un saut de page entre chaque section principale (`##`) avec :

   ```markdown
   <div style="page-break-before: always;"></div>
   ```

3. **Formules mathématiques** : Utiliser la syntaxe LaTeX avec les délimiteurs `$$` pour les formules en bloc et `$` pour les formules en ligne. Exemple :

   ```markdown
   $$
   \text{TRG} = \text{Disponibilité} \times \text{Performance} \times \text{Qualité}
   $$
   ```

4. **Numérotation des sections** : Numéroter manuellement les sections principales (ex. `## 1. Titre`, `## 2. Titre`).
5. **Pied de page** : Terminer chaque document par :

   ```markdown
   ---

   *Titre du document — Mois Année*
   ```

## Standards pour les fichiers HTML

#### Pas d'émoji

1. **En-tête avec logo** : Inclure un div `.logo-header` après la balise `<body>` :

   ```html
   <div class="logo-header">
     <img src="logo_uimm_placeholder.jpg" alt="Logo UIMM" />
     <div class="structure-name">Pôle Formation UIMM - CVDL</div>
   </div>
   ```

2. **CSS professionnel** : Utiliser le template CSS disponible dans `OI/templates/style_formation.css`. Pour les fichiers HTML générés avec pandoc, utiliser l'option `--css`.
3. **Sauts de page** : Ajouter la classe `page-break` aux `<h2>` pour les sections principales, avec le CSS associé :

   ```css
   h2.page-break { page-break-before: always; }
   ```

4. **MathJax** : Inclure MathJax dans le `<head>` :

   ```html
   <script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml-full.js"></script>
   ```

5. **Google Font Inter** : Utiliser la police Inter :

   ```html
   <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" />
   ```

## Outils disponibles

- **`OI/md2pdf.bat`** : Convertisseur Markdown → PDF (via pandoc + Chrome headless). Respecte les sauts de page CSS.
- **`OI/md2html.bat`** : Convertisseur Markdown → HTML (via pandoc + CSS template).
- **Template CSS** : `OI/templates/style_formation.css`

## Mise à jour de l'index

Quand un nouveau fichier HTML est créé ou modifié dans ce repo, **mettre à jour `index.html`** à la racine pour qu'il apparaisse dans le portail en ligne. L'index est organisé en 3 sections :

1. **Activités Pédagogiques** (A0–A7) : cartes avec liens vers les dossiers de ressources
2. **Simulations & Ateliers LEAN** : Atelier Cocotte, Jeu du KANBAN, etc.
3. **Documents de Référence** : plans de formation, supports, outils

## Conventions de nommage

- Fichiers : `Nom_Du_Document.md` / `Nom_Du_Document.html` (underscores, pas d'espaces)
- Dossiers activités : `A[N] Nom` (ex. `A0_Pareto_Ishikawa`)
- Versions apprenant : suffixe `_Apprenant` (ex. `Atelier_Cocotte_Lean_Apprenant.md`)
- Tous les noms de répertoires et fichiers seront sans accent et espace

## Orchestration du Flux de Travail

### 1. Mode Planification par Défaut

- Entrer en mode planification pour TOUTE tâche non triviale (3+ étapes ou décisions architecturales).
- Si une erreur survient, ARRÊTER et replanifier immédiatement - ne pas forcer l'exécution.
- Utiliser le mode planification pour les étapes de vérification, pas uniquement pour la construction.
- Rédiger des spécifications détaillées à l'avance pour réduire l'ambiguïté.

### 2. Stratégie des Sous-Agents

- Utiliser généreusement les sous-agents pour maintenir la fenêtre de contexte principale dégagée.
- Déléguer la recherche, l'exploration et l'analyse parallèle aux sous-agents.
- Pour les problèmes complexes, allouer une puissance de calcul supérieure via les sous-agents.
- Assigner une seule tâche par sous-agent pour garantir une exécution ciblée.

### 3. Boucle d'Auto-Amélioration

- Après TOUTE correction de l'utilisateur : mettre à jour le fichier `tasks/lessons.md` avec le modèle d'erreur.
- Définir des règles internes pour prévenir la répétition de la même erreur.
- Itérer rigoureusement sur ces leçons jusqu'à la diminution du taux d'erreur.
- Examiner les leçons au démarrage de chaque session pour le projet concerné.

### 4. Vérification Avant Achèvement

- Ne jamais marquer une tâche comme terminée sans prouver son fonctionnement.
- Comparer le comportement (diff) entre la branche principale et les modifications apportées lorsque pertinent.
- Appliquer le critère d'évaluation : "Un ingénieur principal (Staff Engineer) approuverait-il ceci ?"
- Exécuter les tests, inspecter les journaux (logs) et démontrer l'exactitude de la solution.

### 5. Exigence d'Élégance (Équilibrée)

- Pour les modifications non triviales : suspendre l'action et évaluer : "existe-t-il une approche plus élégante ?"
- Si une correction semble précaire (hacky) : "Sachant tout ce que je sais maintenant, implémenter la solution élégante."
- Omettre cette étape pour les corrections simples et évidentes - éviter la sur-ingénierie.
- Évaluer de manière critique son propre travail avant de le présenter.

### 6. Résolution Autonome des Bugs

- Lors de la réception d'un rapport de bug : exécuter la correction. Ne pas solliciter d'assistance pas-à-pas.
- Cibler les journaux, les messages d'erreur et les tests en échec, puis les résoudre.
- Exiger un changement de contexte nul de la part de l'utilisateur.
- Corriger les tests d'intégration continue (CI) en échec sans instruction explicite sur la méthode.

---

## Gestion des Tâches

1. **Planifier d'Abord** : Rédiger le plan d'action dans `tasks/todo.md` avec des éléments vérifiables.
2. **Vérifier le Plan** : Valider avant le début de l'implémentation.
3. **Suivre la Progression** : Marquer les éléments comme terminés au fur et à mesure.
4. **Expliquer les Changements** : Fournir un résumé de haut niveau à chaque étape.
5. **Documenter les Résultats** : Intégrer une section de révision dans `tasks/todo.md`.
6. **Capturer les Leçons** : Mettre à jour `tasks/lessons.md` après les corrections.

---

## Principes Fondamentaux

- **Simplicité d'Abord** : Rendre chaque modification aussi simple que possible. Impact minimal sur le code.
- **Aucune Paresse** : Trouver les causes profondes. Aucun correctif temporaire. Standards de développeur senior.
- **Impact Minimal** : Les modifications ne doivent toucher que ce qui est nécessaire. Éviter d'introduire des bugs.
