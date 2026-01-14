# Python Standard Library

Die Python Standard Library ist eine umfangreiche Sammlung von Modulen, die mit Python mitgeliefert werden. Sie müssen nicht separat installiert werden und bieten Funktionen für viele gängige Aufgaben.

## Wichtige Module: os, sys, pathlib, datetime

Python kommt mit einer Vielzahl nützlicher Module. Hier sind einige der wichtigsten.

### Das os-Modul

Das `os`-Modul bietet Funktionen für die Interaktion mit dem Betriebssystem.

```python
import os

# Aktuelles Arbeitsverzeichnis anzeigen:
aktuelles_verzeichnis = os.getcwd()
print(f"Aktuelles Verzeichnis: {aktuelles_verzeichnis}")

# Dateien und Ordner im Verzeichnis auflisten:
inhalt = os.listdir(".")
print(f"Inhalt: {inhalt}")

# Prüfen, ob Datei oder Ordner existiert:
if os.path.exists("datei.txt"):
    print("Datei existiert")
else:
    print("Datei existiert nicht")

# Prüfen, ob es sich um eine Datei handelt:
if os.path.isfile("dokument.pdf"):
    print("Es ist eine Datei")

# Prüfen, ob es sich um einen Ordner handelt:
if os.path.isdir("ordner"):
    print("Es ist ein Ordner")

# Dateipfade zusammenfügen:
pfad = os.path.join("ordner", "unterordner", "datei.txt")
print(pfad)  # ordner/unterordner/datei.txt (oder ordner\unterordner\datei.txt auf Windows)
```

**Umgebungsvariablen:**

```python
import os

# Umgebungsvariable lesen:
home = os.environ.get("HOME")
print(f"Home-Verzeichnis: {home}")

# Alle Umgebungsvariablen:
for key, value in os.environ.items():
    print(f"{key}: {value}")
```

### Das sys-Modul

Das `sys`-Modul bietet Zugriff auf systembezogene Funktionen und Parameter.

```python
import sys

# Python-Version:
print(f"Python-Version: {sys.version}")

# Plattform:
print(f"Plattform: {sys.platform}")  # z.B. 'linux', 'win32', 'darwin'

# Kommandozeilenargumente:
print(f"Script-Name: {sys.argv[0]}")
print(f"Alle Argumente: {sys.argv}")

# Python-Suchpfade für Module:
print("Module-Pfade:")
for pfad in sys.path:
    print(f"  {pfad}")
```

### Das pathlib-Modul (Modern)

`pathlib` ist die moderne, objektorientierte Alternative zu `os.path`:

```python
from pathlib import Path

# Aktuelles Verzeichnis:
aktuell = Path.cwd()
print(f"Aktuelles Verzeichnis: {aktuell}")

# Home-Verzeichnis:
home = Path.home()
print(f"Home-Verzeichnis: {home}")

# Pfade zusammenfügen:
pfad = Path("ordner") / "unterordner" / "datei.txt"
print(pfad)

# Prüfungen:
datei = Path("beispiel.txt")
print(f"Existiert: {datei.exists()}")
print(f"Ist Datei: {datei.is_file()}")
print(f"Ist Ordner: {datei.is_dir()}")

# Dateiinformationen:
if datei.exists():
    print(f"Dateiname: {datei.name}")
    print(f"Erweiterung: {datei.suffix}")
    print(f"Ohne Erweiterung: {datei.stem}")
    print(f"Elternverzeichnis: {datei.parent}")

# Alle Python-Dateien in einem Verzeichnis finden:
verzeichnis = Path(".")
for datei in verzeichnis.glob("*.py"):
    print(datei)
```

### Das datetime-Modul

Das `datetime`-Modul ermöglicht die Arbeit mit Datum und Zeit.

```python
from datetime import datetime, date, time, timedelta

# Aktuelles Datum und Zeit:
jetzt = datetime.now()
print(f"Jetzt: {jetzt}")
print(f"Jahr: {jetzt.year}")
print(f"Monat: {jetzt.month}")
print(f"Tag: {jetzt.day}")
print(f"Stunde: {jetzt.hour}")
print(f"Minute: {jetzt.minute}")

# Nur Datum:
heute = date.today()
print(f"Heute: {heute}")

# Datum erstellen:
geburtstag = date(1990, 5, 15)
print(f"Geburtstag: {geburtstag}")

# Formatierte Ausgabe:
print(jetzt.strftime("%d.%m.%Y %H:%M:%S"))  # 14.01.2026 15:30:45
print(heute.strftime("%A, %d. %B %Y"))      # Mittwoch, 14. Januar 2026

# Zeitdifferenzen:
morgen = heute + timedelta(days=1)
print(f"Morgen: {morgen}")

in_einer_woche = heute + timedelta(weeks=1)
print(f"In einer Woche: {in_einer_woche}")

# Differenz zwischen zwei Daten:
differenz = heute - geburtstag
print(f"Tage seit Geburtstag: {differenz.days}")
```

**Praktisches Beispiel - Alter berechnen:**

```python
from datetime import date

def berechne_alter(geburtsdatum):
    """Berechnet das Alter in Jahren."""
    heute = date.today()
    alter = heute.year - geburtsdatum.year

    # Korrektur, falls Geburtstag noch nicht war:
    if (heute.month, heute.day) < (geburtsdatum.month, geburtsdatum.day):
        alter -= 1

    return alter

geburtstag = date(1995, 8, 20)
alter = berechne_alter(geburtstag)
print(f"Alter: {alter} Jahre")
```

## Module importieren und verwenden

Python bietet verschiedene Möglichkeiten, Module zu importieren.

### Import-Varianten

**Gesamtes Modul importieren:**

```python
import math

print(math.pi)        # 3.141592653589793
print(math.sqrt(16))  # 4.0
print(math.cos(0))    # 1.0
```

**Modul mit Alias importieren:**

```python
import math as m

print(m.pi)           # 3.141592653589793
print(m.sqrt(25))     # 5.0
```

**Bestimmte Funktionen importieren:**

```python
from math import pi, sqrt, cos

print(pi)             # 3.141592653589793
print(sqrt(9))        # 3.0
print(cos(0))         # 1.0
```

**Alles aus einem Modul importieren (nicht empfohlen):**

```python
from math import *

print(pi)             # 3.141592653589793
print(sqrt(4))        # 2.0
# Problem: Namenskonflikte möglich!
```

### Wichtige Module im Überblick

**math - Mathematische Funktionen:**

```python
import math

print(math.sqrt(16))      # Quadratwurzel: 4.0
print(math.pow(2, 8))     # Potenz: 256.0
print(math.floor(3.7))    # Abrunden: 3
print(math.ceil(3.2))     # Aufrunden: 4
print(math.sin(math.pi))  # Sinus: 1.2246467991473532e-16 (≈ 0)
print(math.log(10))       # Natürlicher Logarithmus: 2.302585092994046
```

**random - Zufallszahlen:**

```python
import random

# Zufällige Ganzzahl:
print(random.randint(1, 10))          # z.B. 7

# Zufällige Fließkommazahl:
print(random.random())                # z.B. 0.734... (0.0 bis 1.0)

# Zufällige Auswahl aus Liste:
farben = ["rot", "blau", "grün"]
print(random.choice(farben))          # z.B. "blau"

# Liste mischen:
zahlen = [1, 2, 3, 4, 5]
random.shuffle(zahlen)
print(zahlen)                         # z.B. [3, 1, 5, 2, 4]

# Mehrere zufällige Elemente:
print(random.sample([1, 2, 3, 4, 5], 3))  # z.B. [2, 5, 1]
```

**json - JSON-Daten verarbeiten:**

```python
import json

# Python-Dictionary zu JSON:
daten = {
    "name": "Anna",
    "alter": 25,
    "hobbys": ["Lesen", "Sport"]
}

json_string = json.dumps(daten, indent=2)
print(json_string)
# {
#   "name": "Anna",
#   "alter": 25,
#   "hobbys": ["Lesen", "Sport"]
# }

# JSON zu Python-Dictionary:
json_text = '{"name": "Max", "alter": 30}'
person = json.loads(json_text)
print(person["name"])  # Max
```

**collections - Erweiterte Datenstrukturen:**

```python
from collections import Counter, defaultdict

# Counter - Elemente zählen:
buchstaben = "abracadabra"
zaehler = Counter(buchstaben)
print(zaehler)  # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
print(zaehler.most_common(2))  # [('a', 5), ('b', 2)]

# defaultdict - Dictionary mit Standardwert:
noten = defaultdict(list)
noten["Anna"].append(1)
noten["Anna"].append(2)
noten["Max"].append(3)
print(dict(noten))  # {'Anna': [1, 2], 'Max': [3]}
```

## Praktisches Beispiel

### Datei-Backup mit Zeitstempel

```python
import shutil
from datetime import datetime
from pathlib import Path

def backup_erstellen(quelldatei):
    """Erstellt ein Backup einer Datei mit Zeitstempel."""
    quelle = Path(quelldatei)

    if not quelle.exists():
        print(f"Fehler: {quelldatei} existiert nicht!")
        return

    # Zeitstempel erstellen:
    zeitstempel = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Backup-Dateinamen erstellen:
    backup_name = f"{quelle.stem}_backup_{zeitstempel}{quelle.suffix}"
    backup_pfad = quelle.parent / backup_name

    # Datei kopieren:
    shutil.copy2(quelle, backup_pfad)
    print(f"Backup erstellt: {backup_pfad}")

# Verwendung:
# backup_erstellen("wichtige_datei.txt")
# Erstellt z.B.: wichtige_datei_backup_20260114_153045.txt
```
## Zusammenfassung

In diesem Kapitel haben Sie gelernt:

- Wichtige Module der Standard Library: `os`, `sys`, `pathlib`, `datetime`
- Wie Module importiert werden: `import`, `from ... import`, Aliase
- Praktische Module: `math`, `random`, `json`, `collections`
- Anwendungsbeispiele für verschiedene Aufgaben

Im nächsten Kapitel lernen Sie, wie Sie mit Dateien arbeiten: lesen, schreiben und verarbeiten.
