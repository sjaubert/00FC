@echo off
REM Script de commit Git rapide
REM Double-cliquez sur ce fichier pour committer rapidement vos changements

echo.
echo ========================================
echo    COMMIT GIT AUTOMATIQUE
echo ========================================
echo.

cd /d "c:\Users\s.jaubert\OneDrive - CFAI Centre\00FC"

powershell.exe -ExecutionPolicy Bypass -File "git-commit-rapide.ps1"

echo.
echo Appuyez sur une touche pour fermer...
pause > nul
