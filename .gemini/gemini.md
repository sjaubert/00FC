---
description: Instructions récurrentes pour le workspace 00FC — Organisation Industrielle
---

# Instructions Récurrentes — Pôle Formation UIMM-CVDL

## Identité de la structure

- **Nom de la structure** : Pôle Formation UIMM - CVDL
- **Formateur principal** : S. Jaubert
- **Logo** : Utiliser le fichier `logo_uimm_placeholder.jpg` situé à la racine du projet (`00FC/logo_uimm_placeholder.jpg`). Ce logo doit être copié dans le dossier de chaque document si nécessaire.

## Standards pour les fichiers Markdown (.md)

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

1. **En-tête avec logo** : Inclure un div `.logo-header` après la balise `<body>` :

   ```html
   <div class="logo-header">
     <img src="logo_uimm_placeholder.jpg" alt="Logo UIMM" />
     <div class="structure-name">Pôle Formation UIMM - CVDL</div>
   </div>
   ```

2. **CSS professionnel** : Utiliser le template CSS disponible dans `OI/_templates/style_formation.css`. Pour les fichiers HTML générés avec pandoc, utiliser l'option `--css`.

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
- **Template CSS** : `OI/_templates/style_formation.css`

## Mise à jour de l'index

Quand un nouveau fichier HTML est créé ou modifié dans ce repo, **mettre à jour `index.html`** à la racine pour qu'il apparaisse dans le portail en ligne. L'index est organisé en 3 sections :

1. **Activités Pédagogiques** (A0–A7) : cartes avec liens vers les dossiers de ressources
2. **Simulations & Ateliers LEAN** : Atelier Cocotte, Jeu du KANBAN, etc.
3. **Documents de Référence** : plans de formation, supports, outils

## Conventions de nommage

- Fichiers : `Nom_Du_Document.md` / `Nom_Du_Document.html` (underscores, pas d'espaces)
- Dossiers activités : `A[N] Nom` (ex. `A0 Pareto - Ishikawa`)
- Versions apprenant : suffixe `_Apprenant` (ex. `Atelier_Cocotte_Lean_Apprenant.md`)
