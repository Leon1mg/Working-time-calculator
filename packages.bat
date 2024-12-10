@echo off
REM Überprüfen, ob Python installiert ist
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python ist nicht installiert. Bitte Python 3.x installieren und erneut versuchen.
    pause
    exit /b
)

REM Virtuelle Umgebung erstellen (optional, wenn gewünscht)
IF NOT EXIST venv (
    echo Erstelle virtuelle Umgebung...
    python -m venv venv
)

REM Aktivieren der virtuellen Umgebung
call venv\Scripts\activate

REM Überprüfen, ob tkinter installiert ist (normalerweise enthalten)
echo Überprüfen der Abhängigkeiten...
python -c "import tkinter" >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Tkinter ist nicht installiert. Bitte sicherstellen, dass Ihre Python-Installation vollständig ist.
    pause
    exit /b
)

REM Start des Programms
echo Starte Arbeitszeitrechner...
python arbeitszeitrechner.py

REM Deaktivieren der virtuellen Umgebung (optional)
call venv\Scripts\deactivate
pause
