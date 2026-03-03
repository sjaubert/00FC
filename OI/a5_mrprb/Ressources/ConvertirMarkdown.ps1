# Script PowerShell pour convertir Markdown en HTML imprimable
# Usage: .\ConvertirMarkdown.ps1 "Kit_Indices_JDR1_QRQC.md"

param(
    [Parameter(Mandatory=$true, Position=0)]
    [string]$FichierMarkdown
)

# Vérifier que le fichier existe
if (-not (Test-Path $FichierMarkdown)) {
    Write-Host "❌ Fichier non trouvé : $FichierMarkdown" -ForegroundColor Red
    exit 1
}

# Installer le module markdown si nécessaire
if (-not (Get-Command ConvertFrom-Markdown -ErrorAction SilentlyContinue)) {
    Write-Host "⚠️  Installation du support Markdown..." -ForegroundColor Yellow
    # Utiliser pandoc si disponible, sinon python
}

Write-Host "🔄 Conversion en cours..." -ForegroundColor Cyan

# Utiliser le script Python
$scriptPath = Join-Path $PSScriptRoot "md_to_html_print.py"

if (Test-Path $scriptPath) {
    # Vérifier si markdown est installé
    try {
        python -c "import markdown" 2>$null
        if ($LASTEXITCODE -ne 0) {
            Write-Host "📦 Installation de la bibliothèque markdown..." -ForegroundColor Yellow
            pip install markdown
        }
        
        # Lancer la conversion
        python $scriptPath $FichierMarkdown
        
        # Ouvrir le fichier HTML dans le navigateur
        $htmlFile = [System.IO.Path]::ChangeExtension($FichierMarkdown, "html")
        if (Test-Path $htmlFile) {
            Write-Host "`n🌐 Ouverture dans le navigateur..." -ForegroundColor Green
            Start-Process $htmlFile
        }
        
    } catch {
        Write-Host "❌ Erreur : Python ou pip non trouvé" -ForegroundColor Red
        Write-Host "💡 Alternative : Utilisez Pandoc (voir ci-dessous)" -ForegroundColor Yellow
    }
} else {
    Write-Host "❌ Script Python non trouvé : $scriptPath" -ForegroundColor Red
}
