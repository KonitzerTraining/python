# Anhang

## A. Kommandozeilen-Befehle

### Windows CMD (Command Prompt)

#### Navigation und Verzeichnisse

```cmd
# Aktuelles Verzeichnis anzeigen
cd

# Verzeichnis wechseln
cd C:\Users\MeinName\Dokumente

# Ein Verzeichnis nach oben
cd ..

# Zur Root des Laufwerks
cd \

# Laufwerk wechseln
D:

# Verzeichnis erstellen
mkdir mein_projekt
md mein_projekt

# Verzeichnis löschen
rmdir mein_projekt
rd mein_projekt

# Verzeichnis mit Inhalt löschen
rmdir /s mein_projekt
```

#### Dateiverwaltung

```cmd
# Dateien und Ordner auflisten
dir

# Detaillierte Ansicht
dir /w

# Datei anzeigen
type datei.txt

# Datei kopieren
copy quelle.txt ziel.txt

# Datei verschieben
move quelle.txt neuer_ordner\

# Datei löschen
del datei.txt

# Mehrere Dateien löschen
del *.txt
```

#### System-Befehle

```cmd
# Bildschirm löschen
cls

# Aktuelles Datum/Zeit
date
time

# Umgebungsvariablen anzeigen
set

# Bestimmte Variable anzeigen
echo %PATH%

# Hilfe zu einem Befehl
help dir
dir /?
```

### Windows PowerShell

```powershell
# Navigation
Set-Location C:\Users\MeinName
cd C:\Users\MeinName

# Dateien auflisten
Get-ChildItem
ls
dir

# Verzeichnis erstellen
New-Item -ItemType Directory -Name "mein_projekt"
mkdir mein_projekt

# Datei erstellen
New-Item -ItemType File -Name "test.txt"

# Datei löschen
Remove-Item test.txt
rm test.txt

# Inhalt anzeigen
Get-Content datei.txt
cat datei.txt

# Nach Dateien suchen
Get-ChildItem -Recurse -Filter *.py

# Bildschirm löschen
Clear-Host
cls
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

### Deutsche Ressourcen

**Offizielle Python-Dokumentation (Deutsch):**
- Hauptseite: https://docs.python.org/de/3/
- Tutorial: https://docs.python.org/de/3/tutorial/index.html
- Standardbibliothek: https://docs.python.org/de/3/library/index.html
- Sprachreferenz: https://docs.python.org/de/3/reference/index.html

**Wichtige Themen:**
- Einführung: https://docs.python.org/de/3/tutorial/introduction.html
- Datenstrukturen: https://docs.python.org/de/3/tutorial/datastructures.html
- Module: https://docs.python.org/de/3/tutorial/modules.html
- Ein- und Ausgabe: https://docs.python.org/de/3/tutorial/inputoutput.html
- Fehler und Ausnahmen: https://docs.python.org/de/3/tutorial/errors.html
- Klassen: https://docs.python.org/de/3/tutorial/classes.html

### Englische Ressourcen

**Offizielle Dokumentation:**
- Python.org: https://www.python.org/
- Dokumentation: https://docs.python.org/3/
- Tutorial: https://docs.python.org/3/tutorial/
- Library Reference: https://docs.python.org/3/library/
- Language Reference: https://docs.python.org/3/reference/

**PEP (Python Enhancement Proposals):**
- PEP 8 - Style Guide: https://pep8.org/ oder https://www.python.org/dev/peps/pep-0008/
- PEP 20 - The Zen of Python: https://www.python.org/dev/peps/pep-0020/
- PEP Index: https://www.python.org/dev/peps/

### Zusätzliche Lernressourcen

**Interaktive Tutorials:**
- Python Tutor (Code-Visualisierung): https://pythontutor.com/
- Real Python: https://realpython.com/
- W3Schools Python: https://www.w3schools.com/python/

**Nachschlagewerke:**
- Python Module of the Week: https://pymotw.com/3/
- Python Cheatsheet: https://www.pythoncheatsheet.org/
- DevDocs (API-Dokumentation): https://devdocs.io/python~3.11/

**Community:**
- Stack Overflow (Python): https://stackoverflow.com/questions/tagged/python
- Reddit r/learnpython: https://www.reddit.com/r/learnpython/
- Python Discord: https://pythondiscord.com/

### Spezifische Module

**Häufig verwendete Module:**
- os: https://docs.python.org/de/3/library/os.html
- sys: https://docs.python.org/de/3/library/sys.html
- datetime: https://docs.python.org/de/3/library/datetime.html
- pathlib: https://docs.python.org/de/3/library/pathlib.html
- json: https://docs.python.org/de/3/library/json.html
- re (Regular Expressions): https://docs.python.org/de/3/library/re.html
- csv: https://docs.python.org/de/3/library/csv.html
- collections: https://docs.python.org/de/3/library/collections.html
- itertools: https://docs.python.org/de/3/library/itertools.html
- functools: https://docs.python.org/de/3/library/functools.html

### Package Index

**PyPI - Python Package Index:**
- Suche nach Paketen: https://pypi.org/
- Beliebte Pakete: https://pypi.org/search/?c=Development+Status+%3A%3A+5+-+Production%2FStable

**Beliebte Drittanbieter-Bibliotheken:**
- Requests (HTTP): https://requests.readthedocs.io/
- NumPy (Numerik): https://numpy.org/doc/
- Pandas (Datenanalyse): https://pandas.pydata.org/docs/
- Matplotlib (Visualisierung): https://matplotlib.org/stable/index.html
- Flask (Web-Framework): https://flask.palletsprojects.com/
- Django (Web-Framework): https://docs.djangoproject.com/

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
