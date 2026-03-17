# Leçons apprises — Workspace 00FC

Ce fichier est prescrit par `.gemini/gemini.md` (section "Boucle d'Auto-Amélioration").
Il doit être lu en début de chaque session et mis à jour après chaque correction utilisateur.

---

## Leçon 1 — 17 mars 2026 : Ne pas lire gemini.md

**Erreur commise :** Début de session sans lecture de `.gemini/gemini.md`.
Conséquences directes :
- Mauvais fichier logo utilisé (`logo_uimm.jpg` au lieu de `logo_uimm_placeholder.jpg`)
- Emojis dans les fichiers `.md` et `.html` (interdits par le standard)
- Structure `.logo-header` non respectée dans le HTML
- Pied de page absent dans le fichier `.md`
- Sauts de page `<div style="page-break-before: always;">` manquants

**Règle interne établie :** Au tout début de chaque session dans le workspace 00FC,
AVANT toute génération de fichier, lire impérativement :
1. `.gemini/gemini.md` (standards HTML, MD, logo, emojis, index)
2. `tasks/lessons.md` (ce fichier)

**Checklist de conformité à vérifier avant tout fichier MD ou HTML :**
- [ ] Logo : `logo_uimm_placeholder.jpg` (pas `logo_uimm.jpg`)
- [ ] En-tête MD : `![Logo UIMM](logo_uimm_placeholder.jpg)` + `**Pole Formation UIMM - CVDL**`
- [ ] En-tête HTML : div `.logo-header` avec img + `.structure-name`
- [ ] Pas d'emojis dans les fichiers MD et HTML
- [ ] Sauts de page entre sections `##` dans les MD
- [ ] Pied de page `*Titre — Mois Année*` dans les MD
- [ ] MathJax dans le `<head>` des HTML
- [ ] `index.html` mis à jour si nouveau fichier HTML créé

---

## Leçon 2 — 17 mars 2026 : Ne pas utiliser les skills disponibles

**Erreur commise :** Skills disponibles dans `.claude/skills/` non consultés ni utilisés.
Les skills pertinents pour ce projet incluent notamment :
- `brainstorm` : pour raffiner des idées pédagogiques avant création
- `critique` : pour évaluer la qualité d'un support créé
- `do-in-steps` : pour orchestrer des tâches complexes multi-fichiers
- `write-concisely` : pour améliorer la qualité rédactionnelle des supports

**Règle interne établie :** Pour toute tâche non triviale (création de support, plan de formation,
analyse de ressources), évaluer si un skill peut améliorer le résultat avant de procéder.

---

*tasks/lessons.md — Mis à jour le 17 mars 2026*
