# Dateioperationen

In diesem Kapitel lernen Sie, wie Sie Dateien lesen, schreiben und verarbeiten. Dateioperationen sind essenziell für viele Programme.

## Dateien lesen und schreiben

Python bietet einfache Möglichkeiten, mit Textdateien zu arbeiten.

### Datei zum Lesen öffnen

Die `open()`-Funktion öffnet eine Datei:

```python
# Datei öffnen und lesen:
datei = open("beispiel.txt", "r")  # "r" = read (lesen)
inhalt = datei.read()
print(inhalt)
datei.close()  # Wichtig: Datei schließen!
```

**Verschiedene Lesemethoden:**

```python
# Gesamten Inhalt lesen:
datei = open("beispiel.txt", "r")
alles = datei.read()
datei.close()

# Datei zeilenweise lesen:
datei = open("beispiel.txt", "r")
for zeile in datei:
    print(zeile, end="")  # end="" verhindert doppelten Zeilenumbruch
datei.close()

# Alle Zeilen als Liste lesen:
datei = open("beispiel.txt", "r")
zeilen = datei.readlines()  # Liste von Strings
datei.close()

for zeile in zeilen:
    print(zeile.strip())  # strip() entfernt Zeilenumbrüche
```

### Datei zum Schreiben öffnen

```python
# Neue Datei erstellen oder überschreiben:
datei = open("ausgabe.txt", "w")  # "w" = write (schreiben)
datei.write("Hallo Welt!\n")
datei.write("Dies ist eine neue Zeile.\n")
datei.close()

# An bestehende Datei anhängen:
datei = open("ausgabe.txt", "a")  # "a" = append (anhängen)
datei.write("Diese Zeile wird angehängt.\n")
datei.close()
```

**Modi im Überblick:**

- `"r"` - Lesen (Datei muss existieren)
- `"w"` - Schreiben (überschreibt existierende Datei)
- `"a"` - Anhängen (fügt am Ende hinzu)
- `"r+"` - Lesen und Schreiben
- `"rb"` - Binärdatei lesen
- `"wb"` - Binärdatei schreiben

### Best Practice: Dateien mit Context Manager öffnen

Mit `with` müssen Sie die Datei nicht manuell schließen:

```python
# Lesen mit Context Manager:
with open("beispiel.txt", "r") as datei:
    inhalt = datei.read()
    print(inhalt)
# Datei wird automatisch geschlossen!

# Schreiben mit Context Manager:
with open("ausgabe.txt", "w") as datei:
    datei.write("Zeile 1\n")
    datei.write("Zeile 2\n")
    datei.write("Zeile 3\n")
```

**Vorteile des Context Managers:**
- Datei wird automatisch geschlossen
- Auch bei Fehlern wird die Datei korrekt geschlossen
- Sauberer und lesbarer Code

### Praktisches Beispiel: Datei zeilenweise verarbeiten

```python
# Zahlen aus Datei lesen und summieren:
summe = 0

with open("zahlen.txt", "r") as datei:
    for zeile in datei:
        zahl = int(zeile.strip())
        summe += zahl

print(f"Summe: {summe}")
```

## Context Manager (with-Statement)

Der Context Manager stellt sicher, dass Ressourcen (wie Dateien) ordnungsgemäß geschlossen werden.

### Ohne Context Manager (alt, fehleranfällig)

```python
# Riskant - was passiert bei einem Fehler?
datei = open("datei.txt", "r")
try:
    inhalt = datei.read()
    # Verarbeitung...
finally:
    datei.close()  # Sicherstellen, dass Datei geschlossen wird
```

### Mit Context Manager (modern, sicher)

```python
# Sicher und elegant:
with open("datei.txt", "r") as datei:
    inhalt = datei.read()
    # Verarbeitung...
# Datei wird automatisch geschlossen
```

### Mehrere Dateien gleichzeitig

```python
# Mehrere Dateien gleichzeitig öffnen:
with open("eingabe.txt", "r") as quelle, open("ausgabe.txt", "w") as ziel:
    for zeile in quelle:
        # Zeile verarbeiten und in Zieldatei schreiben:
        verarbeitet = zeile.upper()  # Großbuchstaben
        ziel.write(verarbeitet)
```

### Eigene Context Manager erstellen (Vorschau)

```python
class DateiLogger:
    """Einfacher Context Manager für Logging."""

    def __init__(self, dateiname):
        self.dateiname = dateiname
        self.datei = None

    def __enter__(self):
        self.datei = open(self.dateiname, "a")
        return self.datei

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.datei:
            self.datei.close()

# Verwendung:
with DateiLogger("log.txt") as log:
    log.write("Programm gestartet\n")
    log.write("Vorgang abgeschlossen\n")
```

## CSV-Dateien verarbeiten

CSV (Comma-Separated Values) ist ein häufiges Format für tabellarische Daten.

### CSV manuell lesen

```python
# Einfaches CSV-Lesen:
with open("daten.csv", "r") as datei:
    for zeile in datei:
        spalten = zeile.strip().split(",")
        print(spalten)

# Beispiel-CSV-Inhalt:
# Name,Alter,Stadt
# Anna,25,Berlin
# Max,30,München

# Ausgabe:
# ['Name', 'Alter', 'Stadt']
# ['Anna', '25', 'Berlin']
# ['Max', '30', 'München']
```

### CSV-Modul verwenden (empfohlen)

Das `csv`-Modul bietet robustere Funktionen:

```python
import csv

# CSV-Datei lesen:
with open("daten.csv", "r") as datei:
    reader = csv.reader(datei)

    # Header überspringen:
    header = next(reader)
    print(f"Spalten: {header}")

    # Daten lesen:
    for zeile in reader:
        name, alter, stadt = zeile
        print(f"{name} ist {alter} Jahre alt und wohnt in {stadt}")
```

### CSV mit DictReader (mit Spaltenüberschriften)

```python
import csv

# CSV als Dictionary lesen:
with open("daten.csv", "r") as datei:
    reader = csv.DictReader(datei)

    for zeile in reader:
        print(f"Name: {zeile['Name']}")
        print(f"Alter: {zeile['Alter']}")
        print(f"Stadt: {zeile['Stadt']}")
        print()
```

### CSV schreiben

```python
import csv

# CSV-Datei schreiben:
personen = [
    ["Name", "Alter", "Stadt"],
    ["Anna", 25, "Berlin"],
    ["Max", 30, "München"],
    ["Lisa", 28, "Hamburg"]
]

with open("ausgabe.csv", "w", newline="") as datei:
    writer = csv.writer(datei)

    for zeile in personen:
        writer.writerow(zeile)

# Mit DictWriter:
personen_dict = [
    {"Name": "Tom", "Alter": 35, "Stadt": "Köln"},
    {"Name": "Eva", "Alter": 27, "Stadt": "Dresden"}
]

with open("ausgabe2.csv", "w", newline="") as datei:
    feldnamen = ["Name", "Alter", "Stadt"]
    writer = csv.DictWriter(datei, fieldnames=feldnamen)

    writer.writeheader()  # Header schreiben
    writer.writerows(personen_dict)  # Alle Zeilen schreiben
```

### Praktisches Beispiel: CSV-Statistik

```python
import csv

def csv_statistik(dateiname):
    """Erstellt eine Statistik aus einer CSV-Datei mit Zahlen."""
    zahlen = []

    with open(dateiname, "r") as datei:
        reader = csv.DictReader(datei)

        for zeile in reader:
            # Annahme: Spalte "Wert" enthält Zahlen
            wert = float(zeile["Wert"])
            zahlen.append(wert)

    if zahlen:
        print(f"Anzahl: {len(zahlen)}")
        print(f"Summe: {sum(zahlen)}")
        print(f"Durchschnitt: {sum(zahlen) / len(zahlen):.2f}")
        print(f"Minimum: {min(zahlen)}")
        print(f"Maximum: {max(zahlen)}")

# Verwendung:
# csv_statistik("verkaufszahlen.csv")
```

## Praktisches Beispiel: Einfaches Logbuch-System

Ein kompaktes Beispiel für ein Logbuch mit verschiedenen Log-Levels:

```python
from datetime import datetime

class Logbuch:
    """Einfaches Logbuch-System."""

    def __init__(self, dateiname="logbuch.txt"):
        self.dateiname = dateiname

    def eintrag(self, nachricht, level="INFO"):
        """Fügt einen Logbuch-Eintrag hinzu."""
        zeitstempel = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_zeile = f"[{zeitstempel}] {level}: {nachricht}\n"

        with open(self.dateiname, "a") as datei:
            datei.write(log_zeile)

    def info(self, nachricht):
        """Info-Level Eintrag."""
        self.eintrag(nachricht, "INFO")

    def warnung(self, nachricht):
        """Warnungs-Level Eintrag."""
        self.eintrag(nachricht, "WARNUNG")

    def fehler(self, nachricht):
        """Fehler-Level Eintrag."""
        self.eintrag(nachricht, "FEHLER")

    def anzeigen(self, anzahl=10):
        """Zeigt die letzten n Einträge an."""
        try:
            with open(self.dateiname, "r") as datei:
                zeilen = datei.readlines()
                letzte_zeilen = zeilen[-anzahl:]

                print(f"=== Letzte {len(letzte_zeilen)} Einträge ===")
                for zeile in letzte_zeilen:
                    print(zeile, end="")
        except FileNotFoundError:
            print("Keine Logbuch-Datei gefunden.")

# Verwendung:
log = Logbuch()
log.info("Programm gestartet")
log.info("Datei verarbeitet")
log.warnung("Speicher wird knapp")
log.fehler("Datei nicht gefunden")
log.anzeigen()
```
## Zusammenfassung

In diesem Kapitel haben Sie gelernt:

- Dateien mit `open()` lesen und schreiben
- Den Context Manager (`with`-Statement) für sicheres Dateihandling
- Modi: `"r"` (lesen), `"w"` (schreiben), `"a"` (anhängen)
- CSV-Dateien mit dem `csv`-Modul verarbeiten
- Praktische Anwendungen: Logbuch, Kontaktliste, Datei-Verschlüsselung

## Ausblick

Sie haben nun die Grundlagen von Python kennengelernt:
- Variablen, Datentypen und Operatoren
- Verzweigungen und Schleifen
- Datenstrukturen (Listen, Dictionaries, Sets, Tuples)
- Funktionen und Code-Organisation
- Standard Library und Module
- Dateioperationen

Mit diesem Wissen können Sie bereits viele praktische Programme schreiben. Weiterführende Themen könnten sein:
- Objektorientierte Programmierung (Klassen und Objekte)
- Fehlerbehandlung und Exceptions
- Reguläre Ausdrücke
- Web-Entwicklung mit Flask oder Django
- Datenanalyse mit Pandas
- GUI-Programmierung mit Tkinter oder PyQt

Viel Erfolg beim Programmieren mit Python!
