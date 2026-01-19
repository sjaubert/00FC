"""
Script de conversion Markdown vers HTML imprimable
Génère un HTML avec CSS optimisé pour l'impression
"""

import markdown
import sys
from pathlib import Path

# CSS optimisé pour l'impression
CSS_PRINT = """
<style>
/* Styles pour l'écran */
@media screen {
    body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
        line-height: 1.6;
        max-width: 900px;
        margin: 40px auto;
        padding: 0 20px;
        color: #333;
        background: #f5f5f5;
    }
    .container {
        background: white;
        padding: 40px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        border-radius: 8px;
    }
}

/* Styles pour l'impression */
@media print {
    body {
        font-family: 'Times New Roman', Times, serif;
        font-size: 11pt;
        line-height: 1.4;
        color: #000;
        margin: 0;
        padding: 0;
    }
    .container {
        padding: 0;
    }
    h1 {
        font-size: 18pt;
        margin-top: 0;
        page-break-after: avoid;
    }
    h2 {
        font-size: 14pt;
        margin-top: 16pt;
        page-break-after: avoid;
    }
    h3 {
        font-size: 12pt;
        margin-top: 12pt;
        page-break-after: avoid;
    }
    /* Éviter les coupures de page dans les éléments */
    pre, blockquote, table, img {
        page-break-inside: avoid;
    }
    /* Contrôle des sauts de page */
    .page-break {
        page-break-before: always;
    }
    /* Images */
    img {
        max-width: 100%;
        height: auto;
    }
    /* Tableaux */
    table {
        border-collapse: collapse;
        width: 100%;
        margin: 12pt 0;
    }
    table th, table td {
        border: 1px solid #000;
        padding: 6pt;
        text-align: left;
    }
    table th {
        background-color: #f0f0f0;
        font-weight: bold;
    }
    /* Code blocks */
    pre code {
        font-size: 9pt;
    }
    /* Liens */
    a {
        color: #000;
        text-decoration: none;
    }
    a[href]:after {
        content: "";
    }
    /* Marges de page */
    @page {
        margin: 2cm;
    }
}

/* Styles communs */
h1, h2, h3, h4, h5, h6 {
    font-weight: bold;
    margin-top: 1em;
    margin-bottom: 0.5em;
}

code {
    background-color: #f4f4f4;
    padding: 2px 6px;
    border-radius: 3px;
    font-family: 'Courier New', Courier, monospace;
    font-size: 0.9em;
}

pre {
    background-color: #f4f4f4;
    padding: 12px;
    border-radius: 5px;
    overflow-x: auto;
}

pre code {
    background-color: transparent;
    padding: 0;
}

blockquote {
    border-left: 4px solid #ddd;
    margin: 1em 0;
    padding-left: 1em;
    color: #666;
}

table {
    border-collapse: collapse;
    margin: 1em 0;
}

table th, table td {
    border: 1px solid #ddd;
    padding: 8px 12px;
}

table th {
    background-color: #f8f8f8;
    font-weight: bold;
}

img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 1em 0;
}

hr {
    border: none;
    border-top: 2px solid #ddd;
    margin: 2em 0;
}

/* Bouton d'impression visible uniquement à l'écran */
@media screen {
    .print-button {
        position: fixed;
        top: 20px;
        right: 20px;
        background-color: #4CAF50;
        color: white;
        padding: 12px 24px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 14px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    .print-button:hover {
        background-color: #45a049;
    }
}
@media print {
    .print-button {
        display: none;
    }
}
</style>
"""

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    {css}
</head>
<body>
    <button class="print-button" onclick="window.print()">🖨️ Imprimer</button>
    <div class="container">
        {content}
    </div>
    <script>
        // Ajuster les images pour l'impression
        window.addEventListener('beforeprint', function() {{
            console.log('Préparation de l\'impression...');
        }});
    </script>
</body>
</html>
"""

def convert_md_to_html(md_file_path, output_path=None):
    """Convertit un fichier Markdown en HTML imprimable"""
    md_path = Path(md_file_path)
    
    if not md_path.exists():
        print(f"❌ Fichier non trouvé : {md_file_path}")
        return
    
    # Lire le fichier Markdown
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Convertir en HTML avec extensions
    html_content = markdown.markdown(
        md_content,
        extensions=[
            'extra',           # Tables, fenced code, etc.
            'codehilite',      # Coloration syntaxique
            'nl2br',           # Sauts de ligne
            'sane_lists',      # Listes améliorées
            'toc',             # Table des matières
        ]
    )
    
    # Générer le HTML complet
    title = md_path.stem.replace('_', ' ').title()
    full_html = HTML_TEMPLATE.format(
        title=title,
        css=CSS_PRINT,
        content=html_content
    )
    
    # Déterminer le chemin de sortie
    if output_path is None:
        output_path = md_path.with_suffix('.html')
    else:
        output_path = Path(output_path)
    
    # Sauvegarder le HTML
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"✅ Conversion réussie !")
    print(f"   Fichier source : {md_path}")
    print(f"   Fichier HTML   : {output_path}")
    print(f"\n💡 Pour imprimer :")
    print(f"   1. Ouvrez {output_path.name} dans votre navigateur")
    print(f"   2. Cliquez sur le bouton 'Imprimer' ou utilisez Ctrl+P")
    print(f"   3. Choisissez votre imprimante ou 'Enregistrer au format PDF'")
    
    return output_path

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python md_to_html_print.py <fichier.md> [sortie.html]")
        print("\nExemple:")
        print("  python md_to_html_print.py Kit_Indices_JDR1_QRQC.md")
        sys.exit(1)
    
    md_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    convert_md_to_html(md_file, output_file)
