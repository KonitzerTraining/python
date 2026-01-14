# Python-Grundlagen

Dieses Kapitel behandelt die grundlegenden Konzepte von Python, von der Installation bis zu den wichtigsten Datentypen und Namenskonventionen.

## Python-Installation und Entwicklungsumgebung einrichten

Python ist eine interpretierte, objektorientierte Programmiersprache, die sich besonders gut für Einsteiger eignet. Um mit Python zu arbeiten, müssen Sie zunächst Python auf Ihrem System installieren.

### Installation unter verschiedenen Betriebssystemen

**Windows:**
- Laden Sie Python von [python.org](https://python.org) herunter
- Führen Sie den Installer aus und aktivieren Sie "Add Python to PATH"
- Öffnen Sie die Eingabeaufforderung und prüfen Sie die Installation

**Linux/Mac:**
Python ist oft vorinstalliert. Prüfen Sie die Version:

```bash
python3 --version
```

Falls nicht installiert, nutzen Sie den Paketmanager (z.B. `apt`, `brew`):

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3

# macOS mit Homebrew
brew install python3
```

## Erste Schritte: Python-Konsole und einfache Befehle

Die Python-Konsole (auch REPL - Read-Eval-Print-Loop genannt) ist ein interaktives Tool zum Testen von Code-Schnipseln.

### Starten der Python-Konsole

Öffnen Sie ein Terminal und geben Sie ein:

```bash
python3
```

Sie sehen dann den Python-Prompt:

```python
>>>
```

### Einfache Berechnungen

Python kann direkt als Taschenrechner verwendet werden:

```python
>>> 5 + 3
8

>>> 10 - 4
6

>>> 6 * 7
42

>>> 15 / 3
5.0

>>> 17 // 3  # Ganzzahldivision
5

>>> 17 % 3   # Modulo (Rest)
2

>>> 2 ** 8   # Potenz
256
```

### Ausgabe mit print()

Die `print()`-Funktion gibt Text oder Werte auf der Konsole aus:

```python
>>> print("Hallo Welt!")
Hallo Welt!

>>> print(42)
42

>>> print("Die Antwort ist:", 42)
Die Antwort ist: 42
```

## Variablen und grundlegende Datentypen

Variablen sind Container für Werte. In Python müssen Sie Variablen nicht deklarieren - Sie weisen ihnen einfach einen Wert zu.

### Variablen erstellen und verwenden

```python
# Einfache Zuweisung
name = "Anna"
alter = 25
groesse = 1.75
ist_student = True

# Variablen ausgeben
print(name)          # Anna
print(alter)         # 25
print(groesse)       # 1.75
print(ist_student)   # True
```

### Die wichtigsten Datentypen

Python hat mehrere grundlegende Datentypen:

**Integer (int)** - Ganze Zahlen:

```python
anzahl = 10
temperatur = -5
jahr = 2024

# Operationen mit Integers
summe = anzahl + 100      # 110
produkt = anzahl * 5      # 50
```

**Float** - Fließkommazahlen (Dezimalzahlen):

```python
preis = 19.99
pi = 3.14159
temperatur = -12.5

# Operationen mit Floats
total = preis * 2         # 39.98
umfang = 2 * pi * 5       # 31.4159
```

**String (str)** - Zeichenketten:

```python
vorname = "Max"
nachname = 'Mustermann'
text = """Dies ist ein
mehrzeiliger Text"""

# String-Operationen
vollname = vorname + " " + nachname  # Max Mustermann
gruß = "Hallo " * 3                   # Hallo Hallo Hallo
```

**Boolean (bool)** - Wahrheitswerte:

```python
ist_aktiv = True
ist_abgeschlossen = False

# Boolean-Operationen
ergebnis = ist_aktiv and ist_abgeschlossen    # False
ergebnis2 = ist_aktiv or ist_abgeschlossen    # True
ergebnis3 = not ist_aktiv                     # False
```

### Typ einer Variable prüfen

Mit `type()` können Sie den Datentyp einer Variable ermitteln:

```python
zahl = 42
print(type(zahl))           # <class 'int'>

kommazahl = 3.14
print(type(kommazahl))      # <class 'float'>

text = "Python"
print(type(text))           # <class 'str'>

wahrheit = True
print(type(wahrheit))       # <class 'bool'>
```

## Namenskonventionen und Code-Formatierung

Guter Code ist lesbarer Code. Python hat etablierte Konventionen für die Benennung von Variablen und die Formatierung von Code.

### Regeln für Variablennamen

**Erlaubt:**
- Buchstaben (a-z, A-Z), Zahlen (0-9) und Unterstriche (_)
- Müssen mit einem Buchstaben oder Unterstrich beginnen
- Groß- und Kleinschreibung wird unterschieden

```python
# Gültige Variablennamen
name = "Max"
alter_in_jahren = 25
_private_variable = 100
mitarbeiter2 = "Anna"
```

**Nicht erlaubt:**

```python
# Ungültige Variablennamen (führen zu Fehlern)
# 2name = "Max"           # Beginnt mit Zahl
# mein-name = "Anna"      # Enthält Bindestrich
# for = 5                 # Reserviertes Schlüsselwort
```

### Python Namenskonventionen (PEP 8)

PEP 8 ist der offizielle Style Guide für Python-Code:

```python
# Variablen und Funktionen: snake_case (Kleinbuchstaben mit Unterstrichen)
benutzer_name = "Max"
anzahl_versuche = 3
max_wert = 100

# Konstanten: SCREAMING_SNAKE_CASE (Großbuchstaben mit Unterstrichen)
MAX_VERBINDUNGEN = 100
PI = 3.14159
DATENBANKNAME = "users"

# Klassen: PascalCase (jedes Wort beginnt mit Großbuchstaben)
# (wird später behandelt)
# class BankKonto:
#     pass
```

### Code-Formatierung Best Practices

Gut formatierter Code ist leichter zu lesen und zu warten:

```python
# Leerzeichen um Operatoren
x = 5 + 3        # Gut
# x=5+3          # Schlecht (schwer lesbar)

# Leerzeichen nach Kommas
werte = [1, 2, 3, 4, 5]    # Gut
# werte = [1,2,3,4,5]      # Schlecht

# Aussagekräftige Variablennamen
benutzer_alter = 25              # Gut, selbsterklärend
# a = 25                         # Schlecht, unklar

anzahl_fehler = 0                # Gut
# f = 0                          # Schlecht

# Kommentare für komplexe Logik
# Berechne den Rabatt basierend auf der Bestellmenge
if bestellmenge > 100:
    rabatt = 0.15
else:
    rabatt = 0.05
```

## Zusammenfassung

In diesem Kapitel haben Sie gelernt:

- Wie Sie Python installieren und die Konsole verwenden
- Was Variablen sind und wie Sie diese erstellen
- Die grundlegenden Datentypen: `int`, `float`, `str`, `bool`
- Namenskonventionen und Code-Formatierung nach PEP 8

Im nächsten Kapitel lernen Sie, wie Sie Benutzereingaben verarbeiten und zwischen verschiedenen Datentypen konvertieren.
