# Python Standard Library

Die Python Standard Library ist eine umfangreiche Sammlung von Modulen, die mit Python mitgeliefert werden. Sie müssen nicht separat installiert werden und bieten Funktionen für viele gängige Aufgaben. Diese Module decken Bereiche wie Dateisystemoperationen, Zeitberechnungen, mathematische Funktionen, Zufallszahlen und vieles mehr ab.

Die Verwendung der Standard Library hat mehrere Vorteile: Sie ist sofort verfügbar, gut dokumentiert, plattformübergreifend einsetzbar und von der Python-Community getestet. Anstatt eigene Lösungen für häufige Probleme zu entwickeln, können Sie auf bewährte Module zurückgreifen.

## Wichtige Module: os, sys, pathlib, datetime

Python kommt mit einer Vielzahl nützlicher Module, die den Alltag eines Entwicklers erheblich erleichtern. In diesem Abschnitt lernen Sie die wichtigsten Module kennen, die für die Arbeit mit dem Betriebssystem, Dateipfaden und Zeitberechnungen unerlässlich sind.

### Das os-Modul

Das `os`-Modul bietet Funktionen für die Interaktion mit dem Betriebssystem. Es ermöglicht Ihnen, plattformunabhängig auf Dateisysteme zuzugreifen, Verzeichnisse zu navigieren und Umgebungsvariablen auszulesen. Das Modul abstrahiert viele betriebssystemspezifische Details, sodass Ihr Code auf Windows, Linux und macOS funktioniert.

Ein häufiger Anwendungsfall ist das Arbeiten mit Dateipfaden. Mit `os.path.join()` können Sie Pfade plattformunabhängig zusammensetzen - auf Windows werden Backslashes (`\`), auf Unix-Systemen Slashes (`/`) verwendet. Die Funktion `os.getcwd()` gibt das aktuelle Arbeitsverzeichnis zurück, was besonders nützlich ist, wenn Sie relative Pfade verwenden.

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

Die Funktionen `os.path.exists()`, `os.path.isfile()` und `os.path.isdir()` sind unverzichtbar, wenn Sie prüfen möchten, ob eine Datei oder ein Verzeichnis existiert, bevor Sie darauf zugreifen. Dies verhindert Fehler und macht Ihren Code robuster. Die Funktion `os.listdir()` gibt eine Liste aller Dateien und Ordner in einem Verzeichnis zurück, was für das Durchsuchen von Verzeichnissen nützlich ist.

**Umgebungsvariablen:**

Umgebungsvariablen sind systemweite Einstellungen, die Informationen wie Benutzernamen, Home-Verzeichnisse oder Konfigurationspfade speichern. Mit dem `os`-Modul können Sie diese Variablen auslesen, um systemspezifische Informationen zu erhalten oder Konfigurationen zu laden.

```python
import os

# Umgebungsvariable lesen:
home = os.environ.get("HOME")
print(f"Home-Verzeichnis: {home}")

# Alle Umgebungsvariablen:
for key, value in os.environ.items():
    print(f"{key}: {value}")
```

Die Methode `os.environ.get()` ist sicherer als direkter Zugriff, da sie `None` zurückgibt, wenn die Variable nicht existiert, anstatt einen Fehler zu werfen. Sie können auch einen Standardwert als zweiten Parameter angeben: `os.environ.get("MEINE_VAR", "Standard")`.

### Das sys-Modul

Das `sys`-Modul bietet Zugriff auf systembezogene Funktionen und Parameter, die eng mit dem Python-Interpreter verbunden sind. Es ist besonders nützlich, wenn Sie Informationen über die Python-Laufzeitumgebung benötigen oder Ihr Programm gezielt beenden möchten.

Mit `sys.argv` können Sie Kommandozeilenargumente auslesen, die beim Aufruf eines Python-Skripts übergeben werden. Dies ist die Grundlage für einfache Kommandozeilenprogramme. Das erste Element `sys.argv[0]` enthält immer den Namen des Skripts selbst. Mit `sys.exit()` können Sie Ihr Programm mit einem bestimmten Exit-Code beenden - `0` bedeutet Erfolg, andere Werte signalisieren Fehler.

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

Die Liste `sys.path` zeigt alle Verzeichnisse, in denen Python nach Modulen sucht, wenn Sie `import` verwenden. Dies ist hilfreich beim Debuggen von Import-Problemen. Die Plattform-Information (`sys.platform`) hilft Ihnen, plattformspezifischen Code zu schreiben, falls nötig.

### Das pathlib-Modul (Modern)

`pathlib` ist die moderne, objektorientierte Alternative zu `os.path` und wurde mit Python 3.4 eingeführt. Es bietet eine elegantere und intuitivere Syntax für die Arbeit mit Dateipfaden. Anstatt Funktionen wie `os.path.join()` zu verwenden, arbeiten Sie mit `Path`-Objekten, die mit dem `/`-Operator verkettet werden können.

Die Objektorientierung macht den Code lesbarer: `pfad.exists()` ist selbsterklärender als `os.path.exists(pfad)`. Zudem bietet `pathlib` viele nützliche Methoden wie `.glob()` für das Suchen von Dateien mit Wildcards oder `.read_text()` für das direkte Lesen von Dateiinhalten. Für neue Projekte sollten Sie `pathlib` gegenüber `os.path` bevorzugen.

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

Die `.glob()`-Methode ist besonders praktisch für das Filtern von Dateien. Sie können Wildcards wie `*.py` (alle Python-Dateien) oder `**/*.txt` (alle Textdateien rekursiv) verwenden. Die Eigenschaften `.name`, `.stem`, `.suffix` und `.parent` machen es einfach, Dateinamen zu analysieren und zu manipulieren, ohne String-Operationen durchführen zu müssen.

### Das datetime-Modul

Das `datetime`-Modul ermöglicht die Arbeit mit Datum und Zeit. Es bietet Klassen für die Darstellung von Zeitpunkten, Datumsangaben und Zeitdifferenzen. Die Arbeit mit Datum und Zeit ist in vielen Anwendungen wichtig: von der Protokollierung von Ereignissen über die Berechnung von Fristen bis hin zur Planung von Aufgaben.

Python unterscheidet zwischen `date` (nur Datum), `time` (nur Uhrzeit) und `datetime` (Datum und Uhrzeit kombiniert). Die Klasse `timedelta` repräsentiert Zeitdifferenzen und ermöglicht Berechnungen wie "3 Tage später" oder "2 Stunden früher". Mit der `strftime()`-Methode können Sie Datumsangaben in verschiedenen Formaten ausgeben - zum Beispiel "14.01.2026" oder "Mittwoch, 14. Januar 2026".

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

Die Formatierungscodes für `strftime()` sind standardisiert: `%Y` für vierstelliges Jahr, `%m` für Monat, `%d` für Tag, `%H` für Stunde, `%M` für Minute, `%S` für Sekunde. Mit `%A` erhalten Sie den ausgeschriebenen Wochentag, mit `%B` den Monatsnamen. Zeitdifferenzen können Sie einfach mit `+` und `-` berechnen, was den Code sehr lesbar macht.

**Praktisches Beispiel - Alter berechnen:**

Das folgende Beispiel zeigt, wie Sie das Alter einer Person in Jahren berechnen. Die Herausforderung besteht darin, zu berücksichtigen, ob der Geburtstag im aktuellen Jahr bereits stattgefunden hat. Wenn nicht, müssen wir das Alter um eins reduzieren. Diese Art von Logik ist typisch für reale Anwendungen der datetime-Berechnungen.

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

Python bietet verschiedene Möglichkeiten, Module zu importieren. Die Wahl der richtigen Import-Methode beeinflusst die Lesbarkeit und Wartbarkeit Ihres Codes. Es ist wichtig zu verstehen, wann welche Import-Variante sinnvoll ist.

### Import-Varianten

Es gibt vier Hauptmethoden, um Module zu importieren. Jede hat ihre Vor- und Nachteile, abhängig vom Anwendungsfall. Die Wahl der Import-Methode sollte immer dem Ziel dienen, den Code klar und verständlich zu halten.

**Gesamtes Modul importieren:**

Die Standard-Import-Methode importiert das gesamte Modul. Sie müssen dann den Modulnamen als Präfix verwenden, wenn Sie Funktionen aufrufen. Dies hat den Vorteil, dass immer klar ist, woher eine Funktion stammt, und verhindert Namenskonflikte.

```python
import math

print(math.pi)        # 3.141592653589793
print(math.sqrt(16))  # 4.0
print(math.cos(0))    # 1.0
```

**Modul mit Alias importieren:**

Wenn ein Modulname sehr lang ist oder oft verwendet wird, können Sie einen kürzeren Alias definieren. Dies ist besonders bei Modulen wie `numpy` (oft als `np` importiert) oder `pandas` (oft als `pd`) üblich. Der Alias sollte jedoch immer sinnvoll und in der Community etabliert sein, um die Lesbarkeit zu gewährleisten.

```python
import math as m

print(m.pi)           # 3.141592653589793
print(m.sqrt(25))     # 5.0
```

**Bestimmte Funktionen importieren:**

Wenn Sie nur wenige spezifische Funktionen aus einem Modul benötigen, können Sie diese direkt importieren. Der Vorteil ist kürzerer Code, da Sie den Modulnamen nicht als Präfix schreiben müssen. Verwenden Sie diese Methode jedoch nur, wenn klar ist, woher die Funktionen stammen, und wenn keine Namenskonflikte entstehen können.

```python
from math import pi, sqrt, cos

print(pi)             # 3.141592653589793
print(sqrt(9))        # 3.0
print(cos(0))         # 1.0
```

**Alles aus einem Modul importieren (nicht empfohlen):**

Die `import *`-Syntax importiert alle Funktionen und Variablen aus einem Modul. Dies wird jedoch nicht empfohlen, da es zu Namenskonflikten führen kann und nicht klar ist, welche Namen importiert wurden. Es erschwert die Wartung und das Debugging. Verwenden Sie diese Methode nur in Ausnahmefällen, etwa beim interaktiven Experimentieren in der Python-Shell.

```python
from math import *

print(pi)             # 3.141592653589793
print(sqrt(4))        # 2.0
# Problem: Namenskonflikte möglich!
```

### Wichtige Module im Überblick

Die Standard Library enthält zahlreiche spezialisierte Module für verschiedene Aufgaben. Im Folgenden werden die am häufigsten verwendeten Module vorgestellt, die in fast jedem Python-Projekt nützlich sind.

**math - Mathematische Funktionen:**

Das `math`-Modul bietet mathematische Funktionen und Konstanten, die über die eingebauten Operatoren hinausgehen. Es enthält trigonometrische Funktionen, Logarithmen, Wurzeln und Konstanten wie Pi und Euler's Zahl. Dieses Modul ist unverzichtbar für wissenschaftliche Berechnungen, Geometrie und statistische Analysen.

```python
import math

print(math.sqrt(16))      # Quadratwurzel: 4.0
print(math.pow(2, 8))     # Potenz: 256.0
print(math.floor(3.7))    # Abrunden: 3
print(math.ceil(3.2))     # Aufrunden: 4
print(math.sin(math.pi))  # Sinus: 1.2246467991473532e-16 (≈ 0)
print(math.log(10))       # Natürlicher Logarithmus: 2.302585092994046
```

Die Funktionen `floor()` und `ceil()` sind nützlich für das Auf- und Abrunden, während `pow()` eine Alternative zum `**`-Operator darstellt. Beachten Sie, dass `math` nur für reelle Zahlen funktioniert - für komplexe Zahlen verwenden Sie das `cmath`-Modul.

**random - Zufallszahlen:**

Das `random`-Modul erzeugt Pseudozufallszahlen für verschiedene Verteilungen. Es ist ideal für Simulationen, Spiele, zufällige Auswahlen oder das Mischen von Daten. Beachten Sie, dass die erzeugten Zahlen nicht für kryptographische Zwecke geeignet sind - verwenden Sie dafür das `secrets`-Modul.

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

Die Funktionen `choice()` und `sample()` unterscheiden sich darin, dass `choice()` ein einzelnes Element zurückgibt, während `sample()` mehrere Elemente ohne Zurücklegen auswählt. Die Funktion `shuffle()` verändert die ursprüngliche Liste direkt (in-place), während `sample()` eine neue Liste zurückgibt.

**json - JSON-Daten verarbeiten:**

JSON (JavaScript Object Notation) ist ein weit verbreitetes Datenaustauschformat, das in Webdiensten, APIs und Konfigurationsdateien verwendet wird. Das `json`-Modul ermöglicht die Konvertierung zwischen Python-Datenstrukturen (Dictionaries, Listen) und JSON-Strings. Dies ist essentiell für die Kommunikation mit Web-APIs oder das Speichern strukturierter Daten.

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

Die Funktion `json.dumps()` konvertiert Python-Objekte in JSON-Strings (Serialisierung), während `json.loads()` JSON-Strings in Python-Objekte umwandelt (Deserialisierung). Der Parameter `indent` bei `dumps()` macht die Ausgabe für Menschen lesbar. Für das direkte Lesen und Schreiben von JSON-Dateien verwenden Sie `json.dump()` und `json.load()` (ohne das "s").

**collections - Erweiterte Datenstrukturen:**

Das `collections`-Modul bietet spezialisierte Container-Datentypen, die über die eingebauten `list`, `dict`, `set` und `tuple` hinausgehen. Diese Datenstrukturen lösen häufige Programmierprobleme effizient und elegant. Der `Counter` ist besonders nützlich für Häufigkeitsanalysen, während `defaultdict` das Arbeiten mit verschachtelten Datenstrukturen vereinfacht.

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

Der `Counter` zählt automatisch, wie oft jedes Element in einer Sequenz vorkommt. Die Methode `most_common(n)` gibt die n häufigsten Elemente zurück. Ein `defaultdict` vermeidet `KeyError`-Exceptions, indem es automatisch einen Standardwert für neue Schlüssel erstellt - im Beispiel eine leere Liste. Dies ist besonders praktisch beim Gruppieren von Daten.

## Praktisches Beispiel

### Datei-Backup mit Zeitstempel

Das folgende praktische Beispiel kombiniert mehrere Module der Standard Library: `shutil` für Dateioperationen, `datetime` für Zeitstempel und `pathlib` für die Pfadverwaltung. Es zeigt, wie Sie ein automatisches Backup-System erstellen können, das Dateien mit einem Zeitstempel versieht. Dies ist ein typisches Beispiel für die Kombination verschiedener Module, um eine nützliche Funktionalität zu implementieren.

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

Die Funktion prüft zunächst, ob die Quelldatei existiert, um Fehler zu vermeiden. Der Zeitstempel wird im Format `YYYYMMDD_HHMMSS` erstellt, was eine chronologische Sortierung ermöglicht. Mit `pathlib` wird der neue Dateiname elegant zusammengesetzt: `stem` gibt den Dateinamen ohne Erweiterung zurück, `suffix` die Erweiterung. Die Funktion `shutil.copy2()` kopiert die Datei inklusive Metadaten (Zeitstempel, Berechtigungen).

## Zusammenfassung

In diesem Kapitel haben Sie gelernt:

- Wichtige Module der Standard Library: `os`, `sys`, `pathlib`, `datetime`
- Wie Module importiert werden: `import`, `from ... import`, Aliase
- Praktische Module: `math`, `random`, `json`, `collections`
- Anwendungsbeispiele für verschiedene Aufgaben

Im nächsten Kapitel lernen Sie, wie Sie mit Dateien arbeiten: lesen, schreiben und verarbeiten.
