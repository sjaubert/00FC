@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

REM ============================================================
REM  md2html.bat — Convertir un fichier Markdown en HTML stylé
REM  Usage : Glisser-déposer un .md sur ce fichier
REM          ou : md2html.bat mon_fichier.md
REM ============================================================

REM Vérifier qu'un argument est fourni
if "%~1"=="" (
    echo.
    echo  ╔══════════════════════════════════════════════╗
    echo  ║   md2html — Convertisseur Markdown → HTML   ║
    echo  ╚══════════════════════════════════════════════╝
    echo.
    echo  Usage : Glissez un fichier .md sur ce script
    echo          ou : md2html.bat mon_fichier.md
    echo.
    pause
    exit /b 1
)

REM Vérifier que pandoc est installé
where pandoc >nul 2>&1
if errorlevel 1 (
    echo ERREUR : pandoc n'est pas installé ou pas dans le PATH.
    echo Installez-le depuis https://pandoc.org/installing.html
    pause
    exit /b 1
)

REM Variables
set "INPUT=%~1"
set "OUTPUT=%~dpn1.html"
set "CSS_DIR=%~dp0_templates"
set "CSS_FILE=%CSS_DIR%\style_formation.css"

REM Vérifier que le fichier existe
if not exist "%INPUT%" (
    echo ERREUR : Fichier introuvable : %INPUT%
    pause
    exit /b 1
)

REM Vérifier que le CSS existe
if not exist "%CSS_FILE%" (
    echo NOTE : Template CSS non trouvé (%CSS_FILE%)
    echo        Conversion avec style pandoc par défaut.
    set "CSS_OPTION="
) else (
    set "CSS_OPTION=--css="%CSS_FILE%""
)

echo.
echo  Conversion en cours : %~nx1
echo  ─────────────────────────────────────

REM Conversion avec pandoc
pandoc "%INPUT%" ^
    -o "%OUTPUT%" ^
    --standalone ^
    --metadata title="%~n1" ^
    --mathjax ^
    %CSS_OPTION%

if errorlevel 1 (
    echo  ERREUR lors de la conversion pandoc.
    pause
    exit /b 1
)

echo  ✓ HTML généré : %OUTPUT%
echo.

REM Ouvrir dans le navigateur par défaut
echo  Ouverture dans le navigateur...
start "" "%OUTPUT%"

echo  ✓ Prêt ! Utilisez Ctrl+P pour imprimer.
echo.
timeout /t 3 >nul
