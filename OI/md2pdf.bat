@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

REM ============================================================
REM  md2pdf.bat — Convertir un Markdown en PDF avec sauts de page
REM  Usage : Glisser-déposer un .md sur ce fichier
REM          ou : md2pdf.bat mon_fichier.md
REM  Nécessite : pandoc + Google Chrome
REM ============================================================

if "%~1"=="" (
    echo.
    echo  ╔══════════════════════════════════════════════╗
    echo  ║   md2pdf — Convertisseur Markdown → PDF     ║
    echo  ║   Sauts de page et MathJax respectés        ║
    echo  ╚══════════════════════════════════════════════╝
    echo.
    echo  Usage : Glissez un fichier .md sur ce script
    echo          ou : md2pdf.bat mon_fichier.md
    echo.
    pause
    exit /b 1
)

REM === Vérifier pandoc ===
where pandoc >nul 2>&1
if errorlevel 1 (
    echo ERREUR : pandoc n'est pas installé.
    pause
    exit /b 1
)

REM === Trouver Chrome ===
set "CHROME="
for %%G in (
    "%ProgramFiles%\Google\Chrome\Application\chrome.exe"
    "%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"
    "%LocalAppData%\Google\Chrome\Application\chrome.exe"
) do (
    if exist %%G set "CHROME=%%~G"
)

if "%CHROME%"=="" (
    echo ERREUR : Google Chrome introuvable.
    echo Installez Chrome ou modifiez le chemin dans ce script.
    pause
    exit /b 1
)

REM === Variables ===
set "INPUT=%~1"
set "BASENAME=%~n1"
set "INPUT_DIR=%~dp1"
set "HTML_TEMP=%TEMP%\%BASENAME%_temp.html"
set "OUTPUT_PDF=%~dpn1.pdf"
set "CSS_DIR=%~dp0_templates"
set "CSS_FILE=%CSS_DIR%\style_formation.css"

if not exist "%INPUT%" (
    echo ERREUR : Fichier introuvable : %INPUT%
    pause
    exit /b 1
)

echo.
echo  ┌─────────────────────────────────────┐
echo  │  Conversion : %~nx1
echo  └─────────────────────────────────────┘
echo.

REM === Étape 1 : MD → HTML (pandoc) ===
echo  [1/3] Conversion Markdown → HTML...

if exist "%CSS_FILE%" (
    set "CSS_OPT=--css="%CSS_FILE%""
) else (
    set "CSS_OPT="
    echo        (Template CSS non trouvé, style par défaut)
)

pandoc "%INPUT%" ^
    -o "%HTML_TEMP%" ^
    --standalone ^
    --metadata title="%BASENAME%" ^
    --mathjax ^
    --resource-path="%INPUT_DIR%" ^
    %CSS_OPT%

if errorlevel 1 (
    echo  ERREUR pandoc.
    pause
    exit /b 1
)
echo        ✓ HTML temporaire généré

REM === Étape 2 : Injecter un script pour attendre MathJax ===
echo  [2/3] Préparation pour le rendu MathJax...

REM On ajoute un délai avant impression pour laisser MathJax rendre les formules
powershell -Command "$c = [IO.File]::ReadAllText('%HTML_TEMP%', [Text.Encoding]::UTF8); $script = '<script>window.addEventListener(\"load\", function() { if (window.MathJax) { MathJax.startup.promise.then(function() { setTimeout(function() { document.title = \"READY\"; }, 500); }); } else { document.title = \"READY\"; } });</script>'; $c = $c -replace '</head>', ($script + '`n</head>'); [IO.File]::WriteAllText('%HTML_TEMP%', $c, [Text.Encoding]::UTF8)"

echo        ✓ Script MathJax injecté

REM === Étape 3 : HTML → PDF (Chrome headless) ===
echo  [3/3] Génération du PDF via Chrome...

"%CHROME%" ^
    --headless ^
    --disable-gpu ^
    --no-sandbox ^
    --run-all-compositor-stages-before-draw ^
    --virtual-time-budget=5000 ^
    --print-to-pdf="%OUTPUT_PDF%" ^
    --print-to-pdf-no-header ^
    "%HTML_TEMP%"

if errorlevel 1 (
    echo  ERREUR Chrome headless.
    del "%HTML_TEMP%" >nul 2>&1
    pause
    exit /b 1
)

REM Nettoyage
del "%HTML_TEMP%" >nul 2>&1

echo.
echo  ════════════════════════════════════════
echo  ✓ PDF généré : %OUTPUT_PDF%
echo  ════════════════════════════════════════
echo.

REM Ouvrir le PDF
start "" "%OUTPUT_PDF%"

exit /b 0
