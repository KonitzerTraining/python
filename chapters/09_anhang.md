# Anhang

## A. Grundlegende Kommandozeilen-Befehle

Diese Befehle funktionieren plattformübergreifend in Windows CMD, PowerShell und Unix-Shell (bash/zsh):

### Aktuelles Verzeichnis anzeigen

```bash
# Windows CMD:
cd

# PowerShell, bash, zsh:
pwd
```

### Verzeichnis wechseln

```bash
# Funktioniert überall (Windows, Linux, macOS):
cd Dokumente
cd ..                    # Ein Verzeichnis nach oben
cd C:\Pfad\zum\Ordner   # Windows: Absoluter Pfad
cd /home/user/ordner    # Linux/macOS: Absoluter Pfad
```

### Dateien und Ordner auflisten

```bash
# Windows CMD:
dir

# PowerShell, bash, zsh:
ls

# In PowerShell funktioniert auch:
dir
```

### Bildschirm löschen

```bash
# Windows CMD und PowerShell:
cls

# bash, zsh:
clear
```

## B. Python-Skripte ausführen

### Python-Skript erstellen und ausführen

#### 1. Skript erstellen

Erstellen Sie eine Datei `hallo.py`:
```python
print("Hallo Welt!")
```

#### 2. Skript ausführen

**Windows CMD:**
```cmd
# Python-Version prüfen
python --version
python3 --version

# Skript ausführen
python hallo.py
python3 hallo.py

# Mit vollständigem Pfad
python C:\Users\MeinName\Projekte\hallo.py

# Im Hintergrund ausführen (keine Ausgabe)
python hallo.py > nul
```

**Windows PowerShell:**
```powershell
# Skript ausführen
python .\hallo.py
python3 .\hallo.py

# Mit Parameter
python .\mein_script.py argument1 argument2

# Ausgabe in Datei umleiten
python .\hallo.py > ausgabe.txt
```

**Linux/macOS Terminal:**
```bash
# Skript ausführen
python3 hallo.py

# Skript direkt ausführbar machen (Shebang)
# Erste Zeile in hallo.py: #!/usr/bin/env python3
chmod +x hallo.py
./hallo.py
```

### Python Interactive Shell

```cmd
# Python-Shell starten
python
python3

# Python-Shell beenden
exit()
Ctrl+Z (Windows) oder Ctrl+D (Linux/macOS)

# IPython starten (falls installiert)
ipython
```

### Pip - Paketmanager

```cmd
# Pip-Version prüfen
pip --version
pip3 --version

# Paket installieren
pip install requests
pip install pandas numpy

# Paket deinstallieren
pip uninstall requests

# Installierte Pakete auflisten
pip list
pip freeze

# Requirements installieren
pip install -r requirements.txt

# Requirements-Datei erstellen
pip freeze > requirements.txt

# Paket upgraden
pip install --upgrade requests
```

### Virtuelle Umgebungen

**Erstellen und Aktivieren:**

```cmd
# Windows CMD:
python -m venv meinenv
meinenv\Scripts\activate

# Windows PowerShell:
python -m venv meinenv
meinenv\Scripts\Activate.ps1

# Linux/macOS:
python3 -m venv meinenv
source meinenv/bin/activate

# Deaktivieren (alle Systeme):
deactivate
```

### Python-Skripte mit Argumenten

**Skript (args.py):**
```python
import sys

print(f"Script-Name: {sys.argv[0]}")
print(f"Anzahl Argumente: {len(sys.argv) - 1}")

for i, arg in enumerate(sys.argv[1:], 1):
    print(f"Argument {i}: {arg}")
```

**Ausführen:**
```cmd
python args.py eins zwei drei
# Ausgabe:
# Script-Name: args.py
# Anzahl Argumente: 3
# Argument 1: eins
# Argument 2: zwei
# Argument 3: drei
```

## C. Offizielle Python-Dokumentation

### Wichtigste Ressourcen

**Deutsche Dokumentation:**
- Hauptseite: https://docs.python.org/de/3/
- Tutorial: https://docs.python.org/de/3/tutorial/
- Standardbibliothek: https://docs.python.org/de/3/library/

**Englische Dokumentation:**
- Python.org: https://www.python.org/
- Vollständige Dokumentation: https://docs.python.org/3/
- PEP 8 Style Guide: https://pep8.org/

**PyPI - Python Package Index:**
- Pakete suchen und installieren: https://pypi.org/

## D. Nützliche Tastenkombinationen

### Python Interactive Shell

```
Ctrl+D (Linux/macOS) oder Ctrl+Z (Windows) - Shell beenden
Ctrl+C - Aktuellen Befehl abbrechen
Pfeil hoch/runter - Befehlshistorie durchsuchen
Tab - Auto-Vervollständigung
Ctrl+L - Bildschirm löschen
```

### Windows CMD

```
Tab - Dateinamen-Vervollständigung
F7 - Befehlshistorie anzeigen
Pfeil hoch/runter - Vorherige Befehle
Ctrl+C - Prozess abbrechen
```

### Editoren

**VS Code:**
```
Ctrl+Space - Auto-Vervollständigung
F5 - Debugger starten
Ctrl+/ - Zeile kommentieren
Shift+Alt+F - Code formatieren
Ctrl+` - Terminal öffnen/schließen
```

**IDLE (Python IDE):**
```
F5 - Skript ausführen
Alt+P - Vorheriger Befehl
Alt+N - Nächster Befehl
Ctrl+C - Kopieren
Ctrl+V - Einfügen
```

## E. Häufige Fehler und Lösungen

### ImportError / ModuleNotFoundError

```python
# Fehler:
# ModuleNotFoundError: No module named 'requests'

# Lösung:
# pip install requests
```

### SyntaxError: invalid syntax

```python
# Häufige Ursachen:
# - Fehlende Klammern: print "Hallo"  # Falsch
# - Fehlende Doppelpunkte: if x > 5  # Falsch
# - Falsche Einrückung

# Korrekt:
print("Hallo")
if x > 5:
    print("Größer als 5")
```

### IndentationError

```python
# Fehler: Inkonsistente Einrückung (Tabs und Leerzeichen gemischt)
# Lösung: Nur Leerzeichen verwenden (4 pro Ebene)
```

### NameError: name 'x' is not defined

```python
# Fehler: Variable vor Zuweisung verwendet
# print(ergebnis)  # NameError

# Lösung: Variable zuerst definieren
ergebnis = 42
print(ergebnis)
```

### FileNotFoundError

```python
# Fehler: Datei nicht gefunden
# with open("datei.txt") as f:  # FileNotFoundError

# Lösungen:
# 1. Pfad prüfen
import os
print(os.getcwd())  # Aktuelles Verzeichnis

# 2. Absoluten Pfad verwenden
# with open("C:\\Users\\Name\\datei.txt") as f:

# 3. Existenz prüfen
from pathlib import Path
if Path("datei.txt").exists():
    with open("datei.txt") as f:
        print(f.read())
```

---

**Weitere Hilfe:**
- Python-FAQ: https://docs.python.org/de/3/faq/
- Häufige Fehler: https://docs.python.org/de/3/faq/programming.html
