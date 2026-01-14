# Input/Output und Typumwandlung

In diesem Kapitel lernen Sie, wie Sie mit Benutzereingaben arbeiten, Ausgaben formatieren und zwischen verschiedenen Datentypen konvertieren.

## Benutzereingaben und formatierte Ausgaben

Interaktive Programme benötigen die Möglichkeit, Daten vom Benutzer entgegenzunehmen und Ergebnisse ansprechend auszugeben.

### Die input()-Funktion

Mit `input()` können Sie Benutzereingaben entgegennehmen. Die Funktion gibt immer einen String zurück:

```python
# Einfache Eingabe
name = input("Wie heißen Sie? ")
print("Hallo", name)

# Beispiel-Interaktion:
# Wie heißen Sie? Anna
# Hallo Anna
```

**Wichtig:** `input()` gibt immer einen String zurück, auch wenn der Benutzer eine Zahl eingibt:

```python
eingabe = input("Geben Sie eine Zahl ein: ")
print(type(eingabe))  # <class 'str'>
# Auch bei Eingabe von "42" ist der Typ str!
```

### Mehrere Eingaben verarbeiten

```python
# Persönliche Daten abfragen
vorname = input("Vorname: ")
nachname = input("Nachname: ")
alter = input("Alter: ")

print("Willkommen,", vorname, nachname)
print("Sie sind", alter, "Jahre alt.")
```

### Formatierte Ausgaben

Python bietet verschiedene Möglichkeiten, Ausgaben zu formatieren:

**String-Konkatenation:**

```python
name = "Max"
alter = 30
print("Name: " + name + ", Alter: " + str(alter))
# Achtung: alter muss zu String konvertiert werden!
```

**Format mit Komma-Separation:**

```python
name = "Anna"
punkte = 95
print("Spieler:", name, "- Punkte:", punkte)
# Ausgabe: Spieler: Anna - Punkte: 95
```

**F-Strings (empfohlen ab Python 3.6):**

```python
name = "Lisa"
alter = 28
stadt = "Berlin"

print(f"Mein Name ist {name}, ich bin {alter} Jahre alt und wohne in {stadt}.")
# Ausgabe: Mein Name ist Lisa, ich bin 28 Jahre alt und wohne in Berlin.

# Mit Berechnungen:
preis = 19.99
menge = 3
print(f"Gesamtpreis: {preis * menge} Euro")
# Ausgabe: Gesamtpreis: 59.97 Euro
```

**Format-Methode:**

```python
name = "Tom"
note = 1.7

print("Student: {}, Note: {}".format(name, note))
# Ausgabe: Student: Tom, Note: 1.7

# Mit benannten Platzhaltern:
print("Name: {n}, Alter: {a}".format(n="Eva", a=25))
# Ausgabe: Name: Eva, Alter: 25
```

### Formatierung von Zahlen

F-Strings ermöglichen präzise Zahlenformatierung:

```python
pi = 3.14159265

# Auf 2 Dezimalstellen runden:
print(f"Pi: {pi:.2f}")        # Pi: 3.14

# Auf 4 Dezimalstellen:
print(f"Pi: {pi:.4f}")        # Pi: 3.1416

# Prozentangaben:
anteil = 0.856
print(f"Anteil: {anteil:.1%}")  # Anteil: 85.6%

# Tausendertrennzeichen:
betrag = 1234567.89
print(f"Betrag: {betrag:,.2f} Euro")  # Betrag: 1,234,567.89 Euro
```

## Typumwandlung (Type Conversion)

Oft müssen Daten von einem Typ in einen anderen konvertiert werden. Dies nennt man Type Casting oder Type Conversion.

### Von String zu Zahl

Da `input()` immer Strings zurückgibt, ist die Konvertierung zu Zahlen besonders wichtig:

```python
# String zu Integer:
alter_str = "25"
alter_int = int(alter_str)
print(type(alter_int))  # <class 'int'>

# Direkt bei der Eingabe konvertieren:
alter = int(input("Ihr Alter: "))
print("In 10 Jahren sind Sie", alter + 10, "Jahre alt.")

# String zu Float:
preis_str = "19.99"
preis_float = float(preis_str)
print(type(preis_float))  # <class 'float'>

temperatur = float(input("Temperatur in Celsius: "))
fahrenheit = temperatur * 9/5 + 32
print(f"{temperatur}°C entspricht {fahrenheit:.1f}°F")
```

### Von Zahl zu String

Um Zahlen mit Strings zu kombinieren, müssen sie oft zu Strings konvertiert werden:

```python
alter = 30
text = "Ich bin " + str(alter) + " Jahre alt."
print(text)  # Ich bin 30 Jahre alt.

# Oder verwenden Sie f-Strings (einfacher):
print(f"Ich bin {alter} Jahre alt.")
```

### Zwischen Integer und Float

```python
# Float zu Integer (Nachkommastellen werden abgeschnitten):
kommazahl = 3.99
ganzzahl = int(kommazahl)
print(ganzzahl)  # 3 (nicht gerundet!)

# Integer zu Float:
zahl = 5
gleitkomma = float(zahl)
print(gleitkomma)  # 5.0
```

### String zu Boolean

```python
# Nicht-leere Strings sind True:
text = "Hallo"
wahrheit = bool(text)
print(wahrheit)  # True

# Leerer String ist False:
leer = ""
print(bool(leer))  # False

# Achtung: String "False" ist True!
falsch = "False"
print(bool(falsch))  # True (weil nicht leer)
```

### Praktisches Beispiel: Einfacher Rechner

```python
# Zwei Zahlen vom Benutzer einlesen:
zahl1 = float(input("Erste Zahl: "))
zahl2 = float(input("Zweite Zahl: "))

# Berechnungen durchführen:
summe = zahl1 + zahl2
differenz = zahl1 - zahl2
produkt = zahl1 * zahl2
quotient = zahl1 / zahl2

# Ergebnisse formatiert ausgeben:
print(f"\nErgebnisse:")
print(f"{zahl1} + {zahl2} = {summe}")
print(f"{zahl1} - {zahl2} = {differenz}")
print(f"{zahl1} * {zahl2} = {produkt}")
print(f"{zahl1} / {zahl2} = {quotient:.2f}")
```

## Debugging-Grundlagen und Fehlerbehandlung

Beim Arbeiten mit Benutzereingaben und Typkonvertierungen können Fehler auftreten. Es ist wichtig, diese zu verstehen und zu behandeln.

### Häufige Fehler bei der Typkonvertierung

**ValueError - Ungültige Konvertierung:**

```python
# Fehler: Kann "abc" nicht zu int konvertieren
# zahl = int("abc")  # ValueError: invalid literal for int()

# Fehler: Kann "3.14" nicht direkt zu int konvertieren
# zahl = int("3.14")  # ValueError: invalid literal for int()

# Lösung: Erst zu float, dann zu int:
zahl = int(float("3.14"))  # Funktioniert: 3
```

**ZeroDivisionError - Division durch Null:**

```python
# Fehler bei Division durch Null:
# ergebnis = 10 / 0  # ZeroDivisionError

# Besser: Prüfen vor der Division
nenner = 0
if nenner != 0:
    ergebnis = 10 / nenner
else:
    print("Fehler: Division durch Null nicht möglich!")
```

### Einfaches Debugging mit print()

Die `print()`-Funktion ist das einfachste Debugging-Tool:

```python
# Variablenwerte ausgeben:
x = 10
y = 20
print("Debug: x =", x, "y =", y)

# Typ einer Variable prüfen:
eingabe = input("Zahl: ")
print("Typ der Eingabe:", type(eingabe))

# An verschiedenen Stellen Ausgaben einfügen:
print("Vor der Berechnung")
ergebnis = 5 * 10
print("Nach der Berechnung, Ergebnis:", ergebnis)
```

### Try-Except für Fehlerbehandlung (Vorschau)

Ein kurzer Ausblick auf Fehlerbehandlung (wird später detailliert behandelt):

```python
# Sichere Eingabe einer Zahl:
try:
    alter = int(input("Ihr Alter: "))
    print(f"Sie sind {alter} Jahre alt.")
except ValueError:
    print("Fehler: Bitte geben Sie eine gültige Zahl ein!")

# Beispiel-Interaktionen:
# Ihr Alter: 25
# Sie sind 25 Jahre alt.

# Ihr Alter: abc
# Fehler: Bitte geben Sie eine gültige Zahl ein!
```

### Praktisches Beispiel: Robuste Benutzereingabe

```python
# Programm zur Berechnung des BMI (Body Mass Index)

print("=== BMI-Rechner ===\n")

# Größe eingeben:
groesse_cm = float(input("Ihre Größe in cm: "))
groesse_m = groesse_cm / 100

# Gewicht eingeben:
gewicht = float(input("Ihr Gewicht in kg: "))

# BMI berechnen:
bmi = gewicht / (groesse_m ** 2)

# Ergebnis ausgeben:
print(f"\nIhr BMI: {bmi:.1f}")

if bmi < 18.5:
    print("Kategorie: Untergewicht")
elif bmi < 25:
    print("Kategorie: Normalgewicht")
elif bmi < 30:
    print("Kategorie: Übergewicht")
else:
    print("Kategorie: Starkes Übergewicht")
```

## Zusammenfassung

In diesem Kapitel haben Sie gelernt:

- Mit `input()` Benutzereingaben entgegenzunehmen
- Ausgaben mit f-Strings, format() und Komma-Separation zu formatieren
- Zwischen Datentypen zu konvertieren: `int()`, `float()`, `str()`, `bool()`
- Häufige Fehler bei der Typkonvertierung zu erkennen
- Einfache Debugging-Techniken mit `print()`

Im nächsten Kapitel lernen Sie Verzweigungen und Bedingungen kennen, um Ihren Code entscheidungsfähig zu machen.
