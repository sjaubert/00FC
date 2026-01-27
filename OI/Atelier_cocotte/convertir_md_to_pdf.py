"""
Script de conversion Markdown vers PDF
Utilise markdown2 et weasyprint pour générer un PDF à partir du fichier Markdown
"""

import markdown2
from weasyprint import HTML, CSS
from pathlib import Path

def convertir_md_to_pdf(fichier_md: str, fichier_pdf: str = None):
    """
    Convertit un fichier Markdown en PDF
    
    Args:
        fichier_md: Chemin du fichier Markdown source
        fichier_pdf: Chemin du fichier PDF de sortie (optionnel)
    """
    # Lire le fichier Markdown
    with open(fichier_md, 'r', encoding='utf-8') as f:
        contenu_md = f.read()
    
    # Nettoyer les blocs d'alerte GitHub qui ne sont pas standard
    contenu_md = contenu_md.replace('> [!IMPORTANT]', '> **IMPORTANT:**')
    contenu_md = contenu_md.replace('> [!WARNING]', '> **ATTENTION:**')
    contenu_md = contenu_md.replace('> [!TIP]', '> **CONSEIL:**')
    contenu_md = contenu_md.replace('> [!NOTE]', '> **NOTE:**')
    
    # Convertir Markdown en HTML
    html_content = markdown2.markdown(
        contenu_md,
        extras=['tables', 'fenced-code-blocks', 'strike', 'task_list']
    )
    
    # CSS pour améliorer le rendu
    css_style = """
    @page {
        size: A4;
        margin: 2cm;
    }
    
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 11pt;
        line-height: 1.6;
        color: #333;
    }
    
    h1 {
        color: #2c3e50;
        border-bottom: 3px solid #3498db;
        padding-bottom: 10px;
        margin-top: 30px;
    }
    
    h2 {
        color: #2980b9;
        border-bottom: 2px solid #bdc3c7;
        padding-bottom: 8px;
        margin-top: 25px;
    }
    
    h3 {
        color: #16a085;
        margin-top: 20px;
    }
    
    h4 {
        color: #27ae60;
        margin-top: 15px;
    }
    
    blockquote {
        border-left: 4px solid #3498db;
        background-color: #ecf0f1;
        padding: 10px 15px;
        margin: 15px 0;
        font-style: italic;
    }
    
    code {
        background-color: #f4f4f4;
        padding: 2px 6px;
        border-radius: 3px;
        font-family: 'Consolas', 'Monaco', monospace;
        font-size: 0.9em;
    }
    
    pre {
        background-color: #2c3e50;
        color: #ecf0f1;
        padding: 15px;
        border-radius: 5px;
        overflow-x: auto;
    }
    
    pre code {
        background-color: transparent;
        color: #ecf0f1;
        padding: 0;
    }
    
    table {
        border-collapse: collapse;
        width: 100%;
        margin: 15px 0;
    }
    
    th, td {
        border: 1px solid #bdc3c7;
        padding: 10px;
        text-align: left;
    }
    
    th {
        background-color: #3498db;
        color: white;
        font-weight: bold;
    }
    
    tr:nth-child(even) {
        background-color: #f9f9f9;
    }
    
    hr {
        border: none;
        border-top: 2px solid #bdc3c7;
        margin: 30px 0;
    }
    
    ul, ol {
        margin: 10px 0;
        padding-left: 30px;
    }
    
    li {
        margin: 5px 0;
    }
    """
    
    # HTML complet avec CSS
    html_complet = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>{css_style}</style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    # Définir le nom du PDF si non spécifié
    if fichier_pdf is None:
        fichier_pdf = Path(fichier_md).with_suffix('.pdf')
    
    # Générer le PDF
    print(f"Conversion de {fichier_md} vers {fichier_pdf}...")
    HTML(string=html_complet).write_pdf(fichier_pdf)
    print(f"✅ PDF créé avec succès : {fichier_pdf}")

if __name__ == "__main__":
    # Convertir le fichier scenario_atelier_lean_cocotte_1jour.md
    convertir_md_to_pdf("scenario_atelier_lean_cocotte_1jour.md")
