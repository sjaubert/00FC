import markdown
import sys

# Configuration
input_file = r"c:\Users\s.jaubert\OneDrive - CFAI Centre\00FC\OI\00 LEAN SS\Les fondamentaux de l'Organisation Industrielle - ENRICHI.md"
output_file = r"c:\Users\s.jaubert\OneDrive - CFAI Centre\00FC\OI\00 LEAN SS\Les fondamentaux de l'Organisation Industrielle - ENRICHI.html"

# Lire le fichier Markdown
print("Lecture du fichier Markdown...")
with open(input_file, 'r', encoding='utf-8') as f:
    md_content = f.read()

# Convertir Markdown en HTML
print("Conversion en HTML...")
html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code', 'nl2br'])

# Template HTML avec style professionnel
html_template = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Les Fondamentaux de l'Organisation Industrielle - Formation Interactive</title>
    <style>
        @page {{
            margin: 2cm;
            size: A4;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #fff;
        }}
        
        h1 {{
            color: #2c3e50;
            border-bottom: 4px solid #3498db;
            padding-bottom: 10px;
            margin-top: 30px;
            page-break-before: always;
        }}
        
        h1:first-of-type {{
            page-break-before: auto;
        }}
        
        h2 {{
            color: #34495e;
            border-left: 5px solid #3498db;
            padding-left: 15px;
            margin-top: 25px;
        }}
        
        h3 {{
            color: #546e7a;
            margin-top: 20px;
        }}
        
        h4 {{
            color: #607d8b;
            font-style: italic;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        
        th {{
            background-color: #3498db;
            color: white;
            padding: 12px;
            text-align: left;
            font-weight: bold;
        }}
        
        td {{
            padding: 10px;
            border: 1px solid #ddd;
        }}
        
        tr:nth-child(even) {{
            background-color: #f8f9fa;
        }}
        
        blockquote {{
            border-left: 4px solid #f39c12;
            background-color: #fff9e6;
            padding: 15px;
            margin: 20px 0;
            font-style: italic;
        }}
        
        code {{
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }}
        
        pre {{
            background-color: #2c3e50;
            color: #ecf0f1;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }}
        
        pre code {{
            background-color: transparent;
            color: inherit;
        }}
        
        ul, ol {{
            margin: 15px 0;
            padding-left: 30px;
        }}
        
        li {{
            margin: 8px 0;
        }}
        
        hr {{
            border: none;
            border-top: 2px solid #ecf0f1;
            margin: 30px 0;
        }}
        
        strong {{
            color: #2c3e50;
        }}
        
        em {{
            color: #555;
        }}
        
        .page-break {{
            page-break-after: always;
        }}
        
        @media print {{
            body {{
                max-width: 100%;
                padding: 0;
            }}
            
            h1, h2, h3, h4 {{
                page-break-after: avoid;
            }}
            
            table {{
                page-break-inside: avoid;
            }}
            
            tr {{
                page-break-inside: avoid;
            }}
        }}
    </style>
</head>
<body>
{html_content}
</body>
</html>
"""

# Écrire le fichier HTML
print("Ecriture du fichier HTML...")
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html_template)

print("Conversion terminee !")
print(f"Fichier genere : {output_file}")
print("\nPour creer le PDF :")
print("   1. Ouvrez le fichier HTML dans votre navigateur")
print("   2. Appuyez sur Ctrl+P (ou Cmd+P sur Mac)")
print("   3. Selectionnez 'Enregistrer au format PDF'")
print("   4. Ajustez les marges si necessaire")
print("   5. Cliquez sur 'Enregistrer'")
