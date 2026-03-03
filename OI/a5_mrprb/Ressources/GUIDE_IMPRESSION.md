# 🖨️ Guide d'Impression des Kits d'Indices

**Comment obtenir de belles impressions de vos documents Markdown**

---

## ❌ Problème Connu

La conversion directe **Markdown → PDF** donne souvent un résultat décevant :

- Mise en page cassée
- Images mal placées
- Tableaux déformés
- Pas de contrôle sur le rendu

---

## ✅ Solutions Recommandées

### 🥇 **Solution 1 : Via HTML (RECOMMANDÉE)**

Cette méthode donne le **meilleur résultat** avec un contrôle total sur la mise en page.

#### Étape par étape

1. **Convertir en HTML avec le script**

   ```powershell
   # Dans PowerShell
   .\ConvertirMarkdown.ps1 "JdR1_QRQC\Kit_Indices_JDR1_QRQC.md"
   ```

   Ou directement avec Python :

   ```powershell
   python md_to_html_print.py "JdR1_QRQC\Kit_Indices_JDR1_QRQC.md"
   ```

2. **Le fichier HTML s'ouvre automatiquement** dans votre navigateur

3. **Cliquez sur le bouton "🖨️ Imprimer"** ou utilisez `Ctrl+P`

4. **Options d'impression recommandées** :
   - Destination : Votre imprimante OU "Enregistrer au format PDF"
   - Marges : Normales (2cm)
   - Échelle : 100%
   - ✅ Cocher : "Graphiques d'arrière-plan"

#### Avantages

- ✅ Excellent rendu
- ✅ Images bien placées
- ✅ Tableaux parfaits
- ✅ Contrôle total (CSS personnalisable)

---

### 🥈 **Solution 2 : Via Pandoc (Alternative)**

Si vous avez Pandoc installé :

```powershell
pandoc "JdR1_QRQC\Kit_Indices_JDR1_QRQC.md" -o output.pdf --pdf-engine=wkhtmltopdf -V geometry:margin=2cm
```

#### Installation Pandoc

```powershell
# Avec Chocolatey
choco install pandoc

# Ou télécharger : https://pandoc.org/installing.html
```

---

### 🥉 **Solution 3 : Via Word (Plus simple mais moins joli)**

1. Convertir Markdown → DOCX :

   ```powershell
   pandoc "Kit_Indices_JDR1_QRQC.md" -o output.docx
   ```

2. Ouvrir dans Word et imprimer normalement

#### Avantages

- ✅ Familier (interface Word)
- ✅ Modifications faciles avant impression

---

### 🔧 **Solution 4 : Extension VSCode (Si vous utilisez VSCode)**

1. Installer l'extension **"Markdown PDF"**
2. Ouvrir le .md
3. `Ctrl+Shift+P` → "Markdown PDF: Export (pdf)"

---

## 📋 Prérequis

### Pour la Solution 1 (HTML - Recommandée)

Installer Python et markdown :

```powershell
# Vérifier si Python est installé
python --version

# Installer la bibliothèque markdown
pip install markdown
```

### Pour la Solution 2 (Pandoc)

```powershell
# Installer Pandoc
choco install pandoc wkhtmltopdf
```

---

## 🎨 Personnalisation du CSS (Avancé)

Le fichier `md_to_html_print.py` contient un CSS optimisé pour l'impression. Vous pouvez le modifier pour :

- Changer les polices
- Ajuster les marges
- Modifier les couleurs
- Contrôler les sauts de page

**Exemple** : Forcer un saut de page avant chaque h2 :

```css
@media print {
    h2 {
        page-break-before: always;
    }
}
```

---

## 💡 Conseils d'Impression

### Pour les Kits d'Indices

1. **Imprimer en couleur** : Les images sont importantes
2. **Recto-verso** : Économique et professionnel
3. **Qualité** : "Normale" suffit (pas besoin de "Haute qualité")
4. **Reliure** : Prévoir une marge gauche de 1cm supplémentaire

### Pour les Images Séparées

Les images sont dans `Images/` et peuvent être imprimées séparément si besoin :

- Format recommandé : A4
- Qualité : Normale
- Orientation : Selon l'image

---

## 🚀 Utilisation Rapide

### Convertir UN kit

```powershell
python md_to_html_print.py "JdR1_QRQC\Kit_Indices_JDR1_QRQC.md"
```

### Convertir TOUS les kits

```powershell
# Script batch pour convertir tous les kits
Get-ChildItem "JdR*\Kit_Indices*.md" -Recurse | ForEach-Object {
    python md_to_html_print.py $_.FullName
}
```

Ensuite, ouvrez chaque fichier `.html` dans votre navigateur et imprimez.

---

## ❓ Dépannage

### "Python n'est pas reconnu..."

→ Installer Python : <https://www.python.org/downloads/>
→ Cocher "Add Python to PATH" lors de l'installation

### "Module 'markdown' introuvable"

```powershell
pip install markdown
```

### Les images ne s'affichent pas

→ Vérifier que le dossier `Images/` est au bon endroit
→ Vérifier les chemins relatifs dans le .md

### Le HTML affiche du code brut

→ Vérifier que le fichier .md n'a pas de syntaxe markdown cassée
→ Vérifier l'encodage UTF-8

---

## 📞 Résumé

| Méthode | Qualité | Simplicité | Recommandation |
|---------|---------|------------|----------------|
| **HTML + CSS** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ✅ **Meilleur choix** |
| Pandoc PDF | ⭐⭐⭐⭐ | ⭐⭐⭐ | Alternative solide |
| Word DOCX | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Si vous préférez Word |
| Extension VSCode | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Rapide mais basique |

---

**Recommandation finale** : Utilisez la **Solution 1 (HTML)** pour vos kits d'indices. Le rendu sera professionnel et les images parfaitement intégrées !

---

*Guide créé le 16 janvier 2026*  
*Pôle Formation UIMM-CVDL*
