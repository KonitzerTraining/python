# Funktionen

Funktionen sind wiederverwendbare Code-Blöcke, die eine bestimmte Aufgabe erfüllen. Sie machen Code übersichtlicher, wartbarer und vermeiden Wiederholungen.

## Was sind Funktionen und warum brauchen wir sie?

Funktionen gruppieren zusammengehörigen Code unter einem Namen und ermöglichen es, diesen Code mehrfach aufzurufen, ohne ihn zu wiederholen.

### Vorteile von Funktionen

**Ohne Funktionen (Code-Wiederholung):**

```python
# Berechnung 1:
radius1 = 5
flaeche1 = 3.14159 * radius1 ** 2
print(f"Fläche: {flaeche1}")

# Berechnung 2:
radius2 = 10
flaeche2 = 3.14159 * radius2 ** 2
print(f"Fläche: {flaeche2}")

# Berechnung 3:
radius3 = 7
flaeche3 = 3.14159 * radius3 ** 2
print(f"Fläche: {flaeche3}")
```

**Mit Funktion (DRY - Don't Repeat Yourself):**

```python
def kreis_flaeche(radius):
    """Berechnet die Fläche eines Kreises."""
    return 3.14159 * radius ** 2

# Jetzt einfach mehrfach verwenden:
print(f"Fläche: {kreis_flaeche(5)}")
print(f"Fläche: {kreis_flaeche(10)}")
print(f"Fläche: {kreis_flaeche(7)}")
```

### Vorteile auf einen Blick

- **Wiederverwendbarkeit:** Code einmal schreiben, mehrfach nutzen
- **Lesbarkeit:** Aussagekräftige Namen dokumentieren, was der Code tut
- **Wartbarkeit:** Änderungen nur an einer Stelle nötig
- **Testbarkeit:** Funktionen können isoliert getestet werden

## Funktionen definieren und aufrufen

Eine Funktion wird mit dem Schlüsselwort `def` definiert.

### Einfache Funktion ohne Parameter

```python
def begruessung():
    """Gibt eine Begrüßung aus."""
    print("Hallo und willkommen!")
    print("Schön, dass Sie da sind.")

# Funktion aufrufen:
begruessung()
# Ausgabe:
# Hallo und willkommen!
# Schön, dass Sie da sind.

# Funktion mehrfach aufrufen:
begruessung()
begruessung()
```

### Funktion mit einem Parameter

```python
def begruesse(name):
    """Begrüßt eine Person mit ihrem Namen."""
    print(f"Hallo {name}!")
    print(f"Schön, Sie zu sehen, {name}.")

# Funktionsaufrufe:
begruesse("Anna")
begruesse("Max")
begruesse("Lisa")

# Ausgabe:
# Hallo Anna!
# Schön, Sie zu sehen, Anna.
# Hallo Max!
# Schön, Sie zu sehen, Max.
# ...
```

### Funktion mit mehreren Parametern

```python
def addiere(a, b):
    """Addiert zwei Zahlen und gibt das Ergebnis aus."""
    summe = a + b
    print(f"{a} + {b} = {summe}")

addiere(5, 3)      # 5 + 3 = 8
addiere(10, 20)    # 10 + 20 = 30
addiere(7, -2)     # 7 + -2 = 5
```

### Funktion mit return-Wert

Funktionen können Werte zurückgeben, die weiterverwendet werden können:

```python
def multipliziere(a, b):
    """Multipliziert zwei Zahlen und gibt das Ergebnis zurück."""
    return a * b

# Rückgabewert verwenden:
ergebnis = multipliziere(4, 5)
print(ergebnis)  # 20

# Direkt in Ausdrücken verwenden:
gesamt = multipliziere(3, 4) + multipliziere(2, 5)
print(gesamt)  # 12 + 10 = 22

# In Bedingungen verwenden:
if multipliziere(2, 3) > 5:
    print("Größer als 5")  # Wird ausgegeben
```

## Parameter und Rückgabewerte

Parameter ermöglichen es, Daten an Funktionen zu übergeben. Rückgabewerte ermöglichen es Funktionen, Ergebnisse zurückzugeben.

### Positionsparameter

Die Reihenfolge der Argumente muss der Reihenfolge der Parameter entsprechen:

```python
def vorstellen(name, alter, stadt):
    """Stellt eine Person vor."""
    print(f"Ich bin {name}, {alter} Jahre alt und komme aus {stadt}.")

vorstellen("Anna", 25, "Berlin")
# Ausgabe: Ich bin Anna, 25 Jahre alt und komme aus Berlin.

# Falsche Reihenfolge führt zu falschem Ergebnis:
vorstellen("Berlin", 25, "Anna")
# Ausgabe: Ich bin Berlin, 25 Jahre alt und komme aus Anna.
```

### Schlüsselwort-Parameter (Keyword Arguments)

Sie können Parameter explizit benennen:

```python
def vorstellen(name, alter, stadt):
    print(f"Ich bin {name}, {alter} Jahre alt und komme aus {stadt}.")

# Mit Keyword Arguments (Reihenfolge egal):
vorstellen(alter=30, name="Max", stadt="München")
vorstellen(stadt="Hamburg", name="Lisa", alter=28)

# Mischung aus Positions- und Keyword-Argumenten:
vorstellen("Tom", stadt="Köln", alter=35)
```

### Standardwerte (Default Parameters)

Parameter können Standardwerte haben:

```python
def begruesse(name, gruß="Hallo"):
    """Begrüßt eine Person mit einem optionalen Gruß."""
    print(f"{gruß}, {name}!")

begruesse("Anna")                    # Hallo, Anna!
begruesse("Max", "Guten Morgen")     # Guten Morgen, Max!
begruesse("Lisa", gruß="Hi")         # Hi, Lisa!
```

Praktisches Beispiel:

```python
def potenz(basis, exponent=2):
    """Berechnet basis hoch exponent (Standard: Quadrat)."""
    return basis ** exponent

print(potenz(5))       # 25 (5²)
print(potenz(5, 3))    # 125 (5³)
print(potenz(2, 10))   # 1024 (2¹⁰)
```

### Mehrere Rückgabewerte

Funktionen können mehrere Werte als Tuple zurückgeben:

```python
def min_max(zahlen):
    """Gibt das Minimum und Maximum einer Liste zurück."""
    return min(zahlen), max(zahlen)

# Rückgabewerte entpacken:
minimum, maximum = min_max([3, 7, 1, 9, 4])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 9

# Oder als Tuple verwenden:
ergebnis = min_max([10, 20, 5, 15])
print(ergebnis)  # (5, 20)
```

Weiteres Beispiel:

```python
def kreisberechnung(radius):
    """Berechnet Umfang und Fläche eines Kreises."""
    pi = 3.14159
    umfang = 2 * pi * radius
    flaeche = pi * radius ** 2
    return umfang, flaeche

u, f = kreisberechnung(5)
print(f"Umfang: {u:.2f}, Fläche: {f:.2f}")
# Ausgabe: Umfang: 31.42, Fläche: 78.54
```

### Funktionen ohne Rückgabewert

Funktionen ohne `return` geben implizit `None` zurück:

```python
def ausgabe(text):
    print(text)

ergebnis = ausgabe("Hallo")
print(ergebnis)  # None
```

## Lokale vs. globale Variablen

Variablen haben unterschiedliche Gültigkeitsbereiche (Scopes).

### Lokale Variablen

Variablen, die innerhalb einer Funktion definiert werden, sind lokal:

```python
def meine_funktion():
    x = 10  # Lokale Variable
    print(f"Innerhalb der Funktion: x = {x}")

meine_funktion()  # Innerhalb der Funktion: x = 10

# print(x)  # Fehler: NameError - x existiert außerhalb nicht
```

### Globale Variablen

Variablen, die außerhalb von Funktionen definiert werden, sind global:

```python
y = 20  # Globale Variable

def zeige_global():
    print(f"y in Funktion: {y}")

zeige_global()  # y in Funktion: 20
print(f"y außerhalb: {y}")  # y außerhalb: 20
```

### Lokale Variable verdeckt globale

```python
x = 100  # Globale Variable

def funktion():
    x = 50  # Lokale Variable (verdeckt globale)
    print(f"Lokal: {x}")

funktion()  # Lokal: 50
print(f"Global: {x}")  # Global: 100 (unverändert)
```

### Globale Variablen ändern (nicht empfohlen)

```python
counter = 0  # Globale Variable

def inkrementiere():
    global counter  # Explizit als global deklarieren
    counter += 1

print(counter)  # 0
inkrementiere()
print(counter)  # 1
inkrementiere()
print(counter)  # 2
```

**Warnung:** Die Verwendung von `global` sollte vermieden werden, da sie zu schwer nachvollziehbarem Code führt. Besser: Rückgabewerte verwenden.

```python
# Besser: Ohne global
def inkrementiere(wert):
    return wert + 1

counter = 0
counter = inkrementiere(counter)  # 1
counter = inkrementiere(counter)  # 2
print(counter)  # 2
```

## Best Practices: DRY-Prinzip (Don't Repeat Yourself)

Das DRY-Prinzip besagt: Schreiben Sie keinen Code mehrfach. Nutzen Sie stattdessen Funktionen.

### Schlechtes Beispiel (Code-Wiederholung)

```python
# Preisberechnung für verschiedene Produkte:
preis1 = 100
rabatt1 = preis1 * 0.1
endpreis1 = preis1 - rabatt1
print(f"Endpreis: {endpreis1} Euro")

preis2 = 250
rabatt2 = preis2 * 0.1
endpreis2 = preis2 - rabatt2
print(f"Endpreis: {endpreis2} Euro")

preis3 = 75
rabatt3 = preis3 * 0.1
endpreis3 = preis3 - rabatt3
print(f"Endpreis: {endpreis3} Euro")
```

### Gutes Beispiel (mit Funktion)

```python
def berechne_endpreis(preis, rabatt_prozent=10):
    """Berechnet den Endpreis nach Rabattabzug."""
    rabatt = preis * (rabatt_prozent / 100)
    endpreis = preis - rabatt
    return endpreis

print(f"Endpreis: {berechne_endpreis(100)} Euro")
print(f"Endpreis: {berechne_endpreis(250)} Euro")
print(f"Endpreis: {berechne_endpreis(75)} Euro")

# Oder mit unterschiedlichen Rabatten:
print(f"Endpreis: {berechne_endpreis(200, 20)} Euro")  # 20% Rabatt
```

### Funktionen für komplexe Logik

```python
def ist_schaltjahr(jahr):
    """Prüft, ob ein Jahr ein Schaltjahr ist."""
    if jahr % 4 != 0:
        return False
    elif jahr % 100 != 0:
        return True
    elif jahr % 400 != 0:
        return False
    else:
        return True

# Verwendung:
print(ist_schaltjahr(2024))  # True
print(ist_schaltjahr(2100))  # False
print(ist_schaltjahr(2000))  # True

# Statt die Logik mehrfach zu schreiben:
jahre = [2020, 2021, 2022, 2023, 2024]
for jahr in jahre:
    if ist_schaltjahr(jahr):
        print(f"{jahr} ist ein Schaltjahr")
```

### Funktionen zur Code-Organisation

```python
def eingabe_validieren(wert, minimum, maximum):
    """Prüft, ob ein Wert im gültigen Bereich liegt."""
    return minimum <= wert <= maximum

def temperatur_einlesen():
    """Liest eine gültige Temperatur ein."""
    while True:
        temp = float(input("Temperatur (-50 bis 50°C): "))
        if eingabe_validieren(temp, -50, 50):
            return temp
        else:
            print("Ungültiger Wert!")

def temperatur_bewerten(temp):
    """Bewertet eine Temperatur."""
    if temp < 0:
        return "Kalt"
    elif temp < 20:
        return "Kühl"
    elif temp < 30:
        return "Warm"
    else:
        return "Heiß"

# Hauptprogramm:
temperatur = temperatur_einlesen()
bewertung = temperatur_bewerten(temperatur)
print(f"Es ist {bewertung}.")
```

## Praktische Beispiele

### Beispiel 1: BMI-Rechner mit Funktionen

```python
def bmi_berechnen(gewicht, groesse):
    """Berechnet den Body Mass Index.

    Args:
        gewicht: Gewicht in kg
        groesse: Größe in Metern

    Returns:
        BMI als Float
    """
    return gewicht / (groesse ** 2)

def bmi_kategorie(bmi):
    """Gibt die BMI-Kategorie zurück."""
    if bmi < 18.5:
        return "Untergewicht"
    elif bmi < 25:
        return "Normalgewicht"
    elif bmi < 30:
        return "Übergewicht"
    else:
        return "Adipositas"

def bmi_programm():
    """Führt BMI-Berechnung durch."""
    print("=== BMI-Rechner ===")
    gewicht = float(input("Gewicht in kg: "))
    groesse = float(input("Größe in m: "))

    bmi = bmi_berechnen(gewicht, groesse)
    kategorie = bmi_kategorie(bmi)

    print(f"\nIhr BMI: {bmi:.1f}")
    print(f"Kategorie: {kategorie}")

# Programm ausführen:
bmi_programm()
```

### Beispiel 2: Notenverwaltung

```python
def durchschnitt_berechnen(noten):
    """Berechnet den Notendurchschnitt."""
    if len(noten) == 0:
        return 0
    return sum(noten) / len(noten)

def note_ist_bestanden(note):
    """Prüft, ob eine Note bestanden ist (Note <= 4)."""
    return note <= 4

def notenstatistik(noten):
    """Erstellt eine Statistik über Noten."""
    durchschnitt = durchschnitt_berechnen(noten)
    bestanden = sum(1 for note in noten if note_ist_bestanden(note))
    nicht_bestanden = len(noten) - bestanden

    return {
        "durchschnitt": durchschnitt,
        "bestanden": bestanden,
        "nicht_bestanden": nicht_bestanden,
        "anzahl": len(noten)
    }

# Verwendung:
noten = [1, 2, 3, 2, 4, 5, 3, 1]
statistik = notenstatistik(noten)

print(f"Anzahl Noten: {statistik['anzahl']}")
print(f"Durchschnitt: {statistik['durchschnitt']:.2f}")
print(f"Bestanden: {statistik['bestanden']}")
print(f"Nicht bestanden: {statistik['nicht_bestanden']}")
```

## Zusammenfassung

In diesem Kapitel haben Sie gelernt:

- Funktionen mit `def` definieren und aufrufen
- Parameter übergeben (Positions- und Keyword-Parameter)
- Standardwerte für Parameter festlegen
- Werte mit `return` zurückgeben
- Den Unterschied zwischen lokalen und globalen Variablen
- Das DRY-Prinzip (Don't Repeat Yourself) anwenden

Im nächsten Kapitel lernen Sie die Python Standard Library kennen, die viele nützliche Module bereitstellt.
