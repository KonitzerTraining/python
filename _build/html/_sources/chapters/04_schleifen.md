# Schleifen

Schleifen ermöglichen es, Code mehrfach auszuführen, ohne ihn wiederholt schreiben zu müssen. Python bietet zwei Haupttypen von Schleifen: `while` und `for`.

## While-Schleifen: Wiederholungen mit Bedingungen

Eine `while`-Schleife wiederholt einen Code-Block, solange eine Bedingung wahr ist.

### Grundlegende while-Schleife

```python
zaehler = 1

while zaehler <= 5:
    print(f"Durchlauf {zaehler}")
    zaehler += 1

print("Schleife beendet")

# Ausgabe:
# Durchlauf 1
# Durchlauf 2
# Durchlauf 3
# Durchlauf 4
# Durchlauf 5
# Schleife beendet
```

**Wichtig:** Die Bedingung muss irgendwann falsch werden, sonst entsteht eine Endlosschleife!

### Endlosschleife (vermeiden!)

```python
# VORSICHT: Diese Schleife läuft ewig!
# zaehler = 1
# while zaehler <= 5:
#     print(zaehler)
#     # Fehler: zaehler wird nie erhöht!
```

### Praktische Beispiele

**Benutzereingabe validieren:**

```python
passwort = ""

while passwort != "geheim":
    passwort = input("Bitte Passwort eingeben: ")
    if passwort != "geheim":
        print("Falsches Passwort, versuchen Sie es erneut.")

print("Zugang gewährt!")
```

**Countdown:**

```python
countdown = 10

while countdown > 0:
    print(countdown)
    countdown -= 1

print("Start!")

# Ausgabe: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, Start!
```

**Summe berechnen:**

```python
summe = 0
zahl = 1

while zahl <= 100:
    summe += zahl
    zahl += 1

print(f"Summe von 1 bis 100: {summe}")
# Ausgabe: Summe von 1 bis 100: 5050
```

## For-Schleifen: Iteration über Bereiche

Eine `for`-Schleife iteriert über eine Sequenz (Liste, String, Bereich etc.).

### For-Schleife mit range()

Die `range()`-Funktion erzeugt eine Zahlenfolge:

```python
# Von 0 bis 4 (5 ist exklusiv):
for i in range(5):
    print(i)

# Ausgabe: 0, 1, 2, 3, 4
```

**Mit Start- und Endwert:**

```python
# Von 1 bis 10:
for i in range(1, 11):
    print(i, end=" ")

print()  # Zeilenumbruch
# Ausgabe: 1 2 3 4 5 6 7 8 9 10
```

**Mit Schrittweite:**

```python
# Gerade Zahlen von 0 bis 20:
for i in range(0, 21, 2):
    print(i, end=" ")

# Ausgabe: 0 2 4 6 8 10 12 14 16 18 20
```

**Rückwärts zählen:**

```python
for i in range(10, 0, -1):
    print(i, end=" ")

# Ausgabe: 10 9 8 7 6 5 4 3 2 1
```

### Iteration über Strings

Sie können über jeden Buchstaben in einem String iterieren:

```python
text = "Python"

for buchstabe in text:
    print(buchstabe)

# Ausgabe:
# P
# y
# t
# h
# o
# n
```

Praktisches Beispiel:

```python
wort = "Hallo"
vokal_anzahl = 0

for buchstabe in wort:
    if buchstabe.lower() in "aeiou":
        vokal_anzahl += 1

print(f"Das Wort '{wort}' enthält {vokal_anzahl} Vokale.")
# Ausgabe: Das Wort 'Hallo' enthält 2 Vokale.
```

### Iteration über Listen

```python
fruechte = ["Apfel", "Banane", "Orange", "Kiwi"]

for frucht in fruechte:
    print(f"Ich mag {frucht}")

# Ausgabe:
# Ich mag Apfel
# Ich mag Banane
# Ich mag Orange
# Ich mag Kiwi
```

Mit Index:

```python
fruechte = ["Apfel", "Banane", "Orange"]

for index, frucht in enumerate(fruechte):
    print(f"{index + 1}. {frucht}")

# Ausgabe:
# 1. Apfel
# 2. Banane
# 3. Orange
```

## Die range()-Funktion

Die `range()`-Funktion ist essenziell für for-Schleifen und hat drei Formen.

### range(stop)

Erzeugt Zahlen von 0 bis stop-1:

```python
for i in range(5):
    print(i, end=" ")
# Ausgabe: 0 1 2 3 4
```

### range(start, stop)

Erzeugt Zahlen von start bis stop-1:

```python
for i in range(3, 8):
    print(i, end=" ")
# Ausgabe: 3 4 5 6 7
```

### range(start, stop, step)

Erzeugt Zahlen von start bis stop-1 mit Schrittweite step:

```python
# Ungerade Zahlen:
for i in range(1, 10, 2):
    print(i, end=" ")
# Ausgabe: 1 3 5 7 9

print()

# Rückwärts:
for i in range(20, 10, -2):
    print(i, end=" ")
# Ausgabe: 20 18 16 14 12
```

### Praktische Beispiele mit range()

**Multiplikationstabelle:**

```python
zahl = 7

print(f"Multiplikationstabelle für {zahl}:")
for i in range(1, 11):
    ergebnis = zahl * i
    print(f"{zahl} x {i} = {ergebnis}")

# Ausgabe:
# Multiplikationstabelle für 7:
# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 10 = 70
```

**Liste mit Quadratzahlen:**

```python
quadrate = []

for i in range(1, 11):
    quadrate.append(i ** 2)

print(quadrate)
# Ausgabe: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

## break und continue

Diese Schlüsselwörter ermöglichen es, den normalen Ablauf einer Schleife zu ändern.

### break - Schleife vorzeitig beenden

`break` beendet die Schleife sofort:

```python
for i in range(1, 11):
    if i == 5:
        break
    print(i)

print("Schleife wurde bei 5 abgebrochen")

# Ausgabe: 1, 2, 3, 4
# Schleife wurde bei 5 abgebrochen
```

Praktisches Beispiel:

```python
# Zahl suchen:
zahlen = [10, 23, 45, 67, 89, 12, 34]
ziel = 67
gefunden = False

for zahl in zahlen:
    if zahl == ziel:
        print(f"Zahl {ziel} gefunden!")
        gefunden = True
        break

if not gefunden:
    print(f"Zahl {ziel} nicht gefunden.")

# Ausgabe: Zahl 67 gefunden!
```

### continue - Aktuellen Durchlauf überspringen

`continue` überspringt den Rest des aktuellen Durchlaufs und geht zum nächsten:

```python
for i in range(1, 11):
    if i % 2 == 0:  # Gerade Zahlen überspringen
        continue
    print(i)

# Ausgabe: 1, 3, 5, 7, 9 (nur ungerade Zahlen)
```

Praktisches Beispiel:

```python
# Negative Zahlen ignorieren:
zahlen = [5, -3, 8, -1, 12, -7, 15]

print("Positive Zahlen:")
for zahl in zahlen:
    if zahl < 0:
        continue
    print(zahl)

# Ausgabe: 5, 8, 12, 15
```

### break vs. continue

```python
print("Beispiel mit break:")
for i in range(5):
    if i == 3:
        break
    print(i)
# Ausgabe: 0, 1, 2 (stoppt bei 3)

print("\nBeispiel mit continue:")
for i in range(5):
    if i == 3:
        continue
    print(i)
# Ausgabe: 0, 1, 2, 4 (überspringt 3)
```

## Häufige Fehler bei Schleifen vermeiden

### Endlosschleifen

Achten Sie darauf, dass die Bedingung irgendwann falsch wird:

```python
# FALSCH - Endlosschleife:
# i = 0
# while i < 10:
#     print(i)
#     # Fehler: i wird nie erhöht!

# RICHTIG:
i = 0
while i < 10:
    print(i)
    i += 1  # Bedingung wird irgendwann falsch
```

### Off-by-One Fehler

```python
# FALSCH - läuft nur 9 Mal:
# for i in range(1, 10):
#     print(i)  # Gibt 1-9 aus, nicht 1-10!

# RICHTIG - läuft 10 Mal:
for i in range(1, 11):
    print(i)  # Gibt 1-10 aus
```

### Verschachtelte Schleifen

Achten Sie auf die Laufzeit bei verschachtelten Schleifen:

```python
# Multiplikationstabelle:
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}")
    print()  # Leerzeile nach jeder Reihe

# Diese Schleife läuft 5 x 5 = 25 Mal
```

**Vorsicht bei vielen Verschachtelungen:**

```python
# Diese Schleife läuft 10 x 10 x 10 = 1000 Mal!
# for i in range(10):
#     for j in range(10):
#         for k in range(10):
#             # Rechenintensiver Code hier kann langsam werden
```

## Praktische Beispiele

### Fakultät berechnen

```python
# n! = n x (n-1) x (n-2) x ... x 2 x 1
n = 5
fakultaet = 1

for i in range(1, n + 1):
    fakultaet *= i

print(f"{n}! = {fakultaet}")
# Ausgabe: 5! = 120
```

### Primzahlen finden

```python
# Alle Primzahlen bis 50 finden:
print("Primzahlen bis 50:")

for zahl in range(2, 51):
    ist_primzahl = True

    for teiler in range(2, int(zahl ** 0.5) + 1):
        if zahl % teiler == 0:
            ist_primzahl = False
            break

    if ist_primzahl:
        print(zahl, end=" ")

# Ausgabe: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
```

### Einfaches Zahlenratespiel

```python
import random

ziel = random.randint(1, 100)
versuche = 0
max_versuche = 10

print("Zahlenratespiel: Errate die Zahl zwischen 1 und 100!")

while versuche < max_versuche:
    rate = int(input(f"Versuch {versuche + 1}/{max_versuche}: "))
    versuche += 1

    if rate == ziel:
        print(f"Richtig! Sie haben die Zahl in {versuche} Versuchen erraten.")
        break
    elif rate < ziel:
        print("Zu niedrig!")
    else:
        print("Zu hoch!")
else:
    print(f"Leider verloren. Die Zahl war {ziel}.")
```

## Zusammenfassung

In diesem Kapitel haben Sie gelernt:

- `while`-Schleifen für bedingte Wiederholungen
- `for`-Schleifen für Iteration über Sequenzen
- Die `range()`-Funktion in ihren verschiedenen Formen
- `break` zum vorzeitigen Beenden von Schleifen
- `continue` zum Überspringen von Durchläufen
- Häufige Fehler und wie man sie vermeidet

Im nächsten Kapitel lernen Sie Datenstrukturen wie Listen, Dictionaries, Sets und Tuples kennen.
