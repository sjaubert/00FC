"""
Script pour extraire le texte des PDF VSM
"""
import PyPDF2
import sys
from pathlib import Path

def extract_text_from_pdf(pdf_path):
    """
    Extrait le texte d'un fichier PDF
    
    Args:
        pdf_path: Chemin vers le fichier PDF
        
    Returns:
        str: Texte extrait du PDF
    """
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            
            print(f"\nExtraction de: {Path(pdf_path).name}")
            print(f"Nombre de pages: {len(pdf_reader.pages)}")
            print("-" * 80)
            
            for page_num, page in enumerate(pdf_reader.pages, 1):
                page_text = page.extract_text()
                text += f"\n\n--- PAGE {page_num} ---\n\n"
                text += page_text
                
            return text
    except Exception as e:
        print(f"Erreur lors de l'extraction de {pdf_path}: {e}")
        return None

def main():
    # Définir les chemins des PDF
    base_path = Path(r"c:\Users\steph\projets\00FC\OI\A1 VSM")
    output_path = base_path / "TP_VSM"
    
    pdf_files = [
        base_path / "Formation VSM Maîtriser le Flux et la Valeur Ajoutée.pdf",
        base_path / "Synchroniser la Production sur le Takt Time.pdf",
        base_path / "L_Organisation_Physique_du_Management_Visuel_Kanban.pdf"
    ]
    
    # Extraire le texte de chaque PDF
    all_texts = {}
    for pdf_file in pdf_files:
        if pdf_file.exists():
            text = extract_text_from_pdf(pdf_file)
            if text:
                all_texts[pdf_file.stem] = text
                
                # Sauvegarder le texte dans un fichier
                output_file = output_path / f"{pdf_file.stem}_extracted.txt"
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(text)
                print(f"✓ Texte sauvegardé dans: {output_file.name}\n")
        else:
            print(f"⚠ Fichier non trouvé: {pdf_file}")
    
    # Créer un fichier consolidé
    consolidated_file = output_path / "VSM_documents_consolidated.txt"
    with open(consolidated_file, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("EXTRACTION CONSOLIDÉE DES DOCUMENTS VSM\n")
        f.write("=" * 80 + "\n\n")
        
        for title, text in all_texts.items():
            f.write("\n" + "=" * 80 + "\n")
            f.write(f"DOCUMENT: {title}\n")
            f.write("=" * 80 + "\n")
            f.write(text)
            f.write("\n\n")
    
    print(f"\n✓ Fichier consolidé créé: {consolidated_file.name}")
    print(f"\nNombre de documents extraits: {len(all_texts)}")

if __name__ == "__main__":
    main()
