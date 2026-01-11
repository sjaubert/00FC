# Script de commit Git automatique
# Auteur: S. Jaubert
# Date: 11 janvier 2026

param(
    [string]$Message = ""
)

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   COMMIT GIT AUTOMATIQUE" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Se positionner dans le bon répertoire
$repoPath = "c:\Users\s.jaubert\OneDrive - CFAI Centre\00FC"
Set-Location $repoPath

# Vérifier si on est dans un dépôt Git
if (-not (Test-Path ".git")) {
    Write-Host "ERREUR: Ce répertoire n'est pas un dépôt Git!" -ForegroundColor Red
    exit 1
}

# Vérifier l'état du dépôt
Write-Host "Vérification de l'état du dépôt..." -ForegroundColor Yellow
git status --short

# Compter les fichiers modifiés/nouveaux
$statusOutput = git status --short
if ([string]::IsNullOrWhiteSpace($statusOutput)) {
    Write-Host "`nAucun changement à committer." -ForegroundColor Green
    Write-Host "Votre dépôt est déjà à jour!" -ForegroundColor Green
    exit 0
}

Write-Host "`nFichiers à committer trouvés!" -ForegroundColor Green

# Ajouter tous les fichiers
Write-Host "`nÉtape 1: Ajout de tous les fichiers..." -ForegroundColor Yellow
git add -A
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERREUR lors de l'ajout des fichiers!" -ForegroundColor Red
    exit 1
}
Write-Host "Fichiers ajoutés avec succès!" -ForegroundColor Green

# Créer le message de commit
if ([string]::IsNullOrWhiteSpace($Message)) {
    $dateStr = Get-Date -Format "dd/MM/yyyy HH:mm"
    $Message = "Mise à jour du $dateStr"
}

# Effectuer le commit
Write-Host "`nÉtape 2: Création du commit..." -ForegroundColor Yellow
Write-Host "Message: $Message" -ForegroundColor Cyan
git commit -m $Message
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERREUR lors du commit!" -ForegroundColor Red
    exit 1
}
Write-Host "Commit créé avec succès!" -ForegroundColor Green

# Vérifier la connexion réseau avant de pousser
Write-Host "`nÉtape 3: Vérification de la connexion..." -ForegroundColor Yellow
$connected = Test-Connection -ComputerName "github.com" -Count 1 -Quiet -ErrorAction SilentlyContinue
if (-not $connected) {
    $connected = Test-Connection -ComputerName "8.8.8.8" -Count 1 -Quiet -ErrorAction SilentlyContinue
}

if (-not $connected) {
    Write-Host "ATTENTION: Pas de connexion internet détectée." -ForegroundColor Yellow
    Write-Host "Le commit est créé localement mais ne sera pas poussé vers le serveur." -ForegroundColor Yellow
    Write-Host "Relancez ce script plus tard quand vous aurez une connexion." -ForegroundColor Yellow
    exit 0
}

# Pousser vers le dépôt distant
Write-Host "`nÉtape 4: Push vers le dépôt distant..." -ForegroundColor Yellow
git push origin main 2>&1 | Out-String | Write-Host

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n========================================" -ForegroundColor Green
    Write-Host "   SUCCÈS COMPLET!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "Vos modifications ont été:" -ForegroundColor Green
    Write-Host "  - Ajoutées au suivi Git" -ForegroundColor Green
    Write-Host "  - Commitées localement" -ForegroundColor Green
    Write-Host "  - Poussées vers le serveur distant" -ForegroundColor Green
} else {
    Write-Host "`n========================================" -ForegroundColor Yellow
    Write-Host "   COMMIT PARTIEL" -ForegroundColor Yellow
    Write-Host "========================================" -ForegroundColor Yellow
    Write-Host "Le commit local a réussi mais le push a échoué." -ForegroundColor Yellow
    Write-Host "Raisons possibles:" -ForegroundColor Yellow
    Write-Host "  - Problème d'authentification" -ForegroundColor Yellow
    Write-Host "  - Branche distante en avance" -ForegroundColor Yellow
    Write-Host "  - Problème de connexion temporaire" -ForegroundColor Yellow
    Write-Host "`nEssayez ces commandes manuellement:" -ForegroundColor Cyan
    Write-Host "  git pull origin main" -ForegroundColor White
    Write-Host "  git push origin main" -ForegroundColor White
}

Write-Host ""
