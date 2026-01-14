# Verzweigungen und Bedingungen

Verzweigungen ermöglichen es Ihrem Programm, Entscheidungen zu treffen und unterschiedliche Code-Pfade basierend auf Bedingungen auszuführen.

## if, elif, else

Die grundlegenden Kontrollstrukturen für Verzweigungen in Python sind `if`, `elif` (else if) und `else`.

### Die if-Anweisung

Eine `if`-Anweisung führt Code nur aus, wenn eine Bedingung wahr (True) ist:

```python
alter = 18

if alter >= 18:
    print("Sie sind volljährig.")
    print("Sie dürfen wählen.")

# Ausgabe: Sie sind volljährig.
#          Sie dürfen wählen.
```

**Wichtig:** In Python wird die Einrückung verwendet, um Code-Blöcke zu definieren. Der eingerückte Code gehört zur if-Anweisung.

```python
temperatur = 25

if temperatur > 20:
    print("Es ist warm draußen.")

print("Dieser Code wird immer ausgeführt.")
```

### if-else

Mit `else` definieren Sie einen alternativen Code-Pfad, der ausgeführt wird, wenn die Bedingung falsch ist:

```python
alter = 16

if alter >= 18:
    print("Sie sind volljährig.")
else:
    print("Sie sind noch minderjährig.")

# Ausgabe: Sie sind noch minderjährig.
```

Praktisches Beispiel:

```python
temperatur = int(input("Temperatur in °C: "))

if temperatur >= 25:
    print("Es ist warm, tragen Sie leichte Kleidung.")
else:
    print("Es ist kühl, nehmen Sie eine Jacke mit.")
```

### if-elif-else

Für mehrere Bedingungen verwenden Sie `elif` (else if):

```python
note = 2

if note == 1:
    print("Sehr gut!")
elif note == 2:
    print("Gut!")
elif note == 3:
    print("Befriedigend.")
elif note == 4:
    print("Ausreichend.")
else:
    print("Nicht bestanden.")

# Ausgabe: Gut!
```

**Mehrere Bedingungsbereiche:**

```python
punkte = 85

if punkte >= 90:
    note = 1
elif punkte >= 80:
    note = 2
elif punkte >= 70:
    note = 3
elif punkte >= 60:
    note = 4
else:
    note = 5

print(f"Sie haben {punkte} Punkte erreicht: Note {note}")
# Ausgabe: Sie haben 85 Punkte erreicht: Note 2
```

### Verschachtelte if-Anweisungen

Sie können if-Anweisungen ineinander verschachteln:

```python
alter = 20
fuehrerschein = True

if alter >= 18:
    print("Sie sind volljährig.")
    if fuehrerschein:
        print("Sie dürfen Auto fahren.")
    else:
        print("Sie benötigen einen Führerschein.")
else:
    print("Sie sind zu jung zum Autofahren.")
```

## Vergleichsoperatoren und Bedingungen

Vergleichsoperatoren werden verwendet, um Werte zu vergleichen und Bedingungen zu formulieren.

### Die wichtigsten Vergleichsoperatoren

```python
a = 10
b = 20

# Gleichheit
print(a == b)   # False (ist a gleich b?)

# Ungleichheit
print(a != b)   # True (ist a ungleich b?)

# Größer als
print(a > b)    # False (ist a größer als b?)

# Kleiner als
print(a < b)    # True (ist a kleiner als b?)

# Größer oder gleich
print(a >= 10)  # True (ist a größer oder gleich 10?)

# Kleiner oder gleich
print(b <= 20)  # True (ist b kleiner oder gleich 20?)
```

### Vergleiche mit Strings

Strings können ebenfalls verglichen werden:

```python
name = "Anna"

if name == "Anna":
    print("Hallo Anna!")

# Alphabetische Sortierung:
print("apple" < "banana")  # True (a kommt vor b)
print("Anna" < "anna")     # True (Großbuchstaben vor Kleinbuchstaben)

# Groß-/Kleinschreibung ignorieren:
eingabe = "PYTHON"
if eingabe.lower() == "python":
    print("Richtig!")  # Ausgabe: Richtig!
```

### Mitgliedschaft prüfen (in, not in)

```python
text = "Python ist großartig"

if "Python" in text:
    print("Python wurde gefunden!")  # Ausgabe: Python wurde gefunden!

if "Java" not in text:
    print("Java wurde nicht gefunden!")  # Ausgabe: Java wurde nicht gefunden!

# Mit Listen:
zahlen = [1, 2, 3, 4, 5]

if 3 in zahlen:
    print("3 ist in der Liste")  # Ausgabe: 3 ist in der Liste

if 10 not in zahlen:
    print("10 ist nicht in der Liste")  # Ausgabe: 10 ist nicht in der Liste
```

## Code-Einrückung in Python

Python verwendet Einrückungen (Indentation), um Code-Blöcke zu definieren. Dies ist ein wichtiges Konzept!

### Richtige Einrückung

```python
alter = 25

if alter >= 18:
    print("Volljährig")          # Gehört zu if
    print("Darf wählen")         # Gehört zu if
print("Programm Ende")           # Gehört NICHT zu if

# Ausgabe:
# Volljährig
# Darf wählen
# Programm Ende
```

### Falsche Einrückung führt zu Fehlern

```python
# Fehler: Inkonsistente Einrückung
# if alter >= 18:
#     print("Zeile 1")
#       print("Zeile 2")  # Zu weit eingerückt!

# Fehler: Fehlende Einrückung
# if alter >= 18:
# print("Fehler")  # Muss eingerückt sein!
```

### Empfehlung: 4 Leerzeichen

Der Python Style Guide (PEP 8) empfiehlt 4 Leerzeichen für jede Einrückungsebene:

```python
if True:
    print("Ebene 1")
    if True:
        print("Ebene 2")
        if True:
            print("Ebene 3")
```

## Logische Operatoren (and, or, not)

Logische Operatoren ermöglichen es, mehrere Bedingungen zu kombinieren.

### Der and-Operator

Beide Bedingungen müssen wahr sein:

```python
alter = 25
fuehrerschein = True

if alter >= 18 and fuehrerschein:
    print("Sie dürfen Auto fahren.")
# Ausgabe: Sie dürfen Auto fahren.

# Beispiel 2:
temperatur = 22
sonnig = True

if temperatur > 20 and sonnig:
    print("Perfektes Wetter für einen Ausflug!")
# Ausgabe: Perfektes Wetter für einen Ausflug!
```

Wahrheitstabelle für `and`:

```python
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False
```

### Der or-Operator

Mindestens eine Bedingung muss wahr sein:

```python
tag = "Samstag"

if tag == "Samstag" or tag == "Sonntag":
    print("Wochenende!")
# Ausgabe: Wochenende!

# Beispiel 2:
alter = 67

if alter < 18 or alter >= 65:
    print("Ermäßigter Eintritt")
# Ausgabe: Ermäßigter Eintritt
```

Wahrheitstabelle für `or`:

```python
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False
```

### Der not-Operator

Kehrt einen Wahrheitswert um:

```python
regen = False

if not regen:
    print("Kein Regen, gehen Sie spazieren!")
# Ausgabe: Kein Regen, gehen Sie spazieren!

# Beispiel 2:
ist_gesperrt = False

if not ist_gesperrt:
    print("Zugang erlaubt")
# Ausgabe: Zugang erlaubt
```

Wahrheitstabelle für `not`:

```python
print(not True)   # False
print(not False)  # True
```

### Komplexe Bedingungen

Sie können mehrere logische Operatoren kombinieren:

```python
alter = 25
einkommen = 30000
kreditwuerdig = True

if alter >= 18 and einkommen > 20000 and kreditwuerdig:
    print("Kreditantrag genehmigt")
else:
    print("Kreditantrag abgelehnt")
# Ausgabe: Kreditantrag genehmigt

# Klammern für bessere Lesbarkeit:
x = 10
if (x > 5 and x < 15) or x == 0:
    print("Bedingung erfüllt")
# Ausgabe: Bedingung erfüllt
```

## Verschachtelte Bedingungen

Manchmal müssen Entscheidungen von mehreren aufeinanderfolgenden Bedingungen abhängen.

### Mehrfach verschachtelte if-Anweisungen

```python
benutzername = "admin"
passwort = "geheim123"
aktiv = True

if benutzername == "admin":
    if passwort == "geheim123":
        if aktiv:
            print("Login erfolgreich")
        else:
            print("Account ist deaktiviert")
    else:
        print("Falsches Passwort")
else:
    print("Benutzername nicht gefunden")
```

### Vereinfachung mit logischen Operatoren

Der obige Code kann vereinfacht werden:

```python
benutzername = "admin"
passwort = "geheim123"
aktiv = True

if benutzername == "admin" and passwort == "geheim123" and aktiv:
    print("Login erfolgreich")
elif benutzername != "admin":
    print("Benutzername nicht gefunden")
elif passwort != "geheim123":
    print("Falsches Passwort")
else:
    print("Account ist deaktiviert")
```

### Praktisches Beispiel: Ticketpreis berechnen

```python
alter = int(input("Ihr Alter: "))
student = input("Sind Sie Student? (ja/nein): ").lower() == "ja"
wochentag = input("Welcher Tag? (Mo-So): ")

preis = 12.00  # Standardpreis

if alter < 6:
    preis = 0
    print("Kinder unter 6: kostenlos")
elif alter < 18:
    preis = 8.00
    print("Jugendliche: ermäßigt")
elif alter >= 65:
    preis = 9.00
    print("Senioren: ermäßigt")
elif student:
    preis = 10.00
    print("Studenten: ermäßigt")

if wochentag in ["Montag", "Dienstag"]:
    preis = preis * 0.8
    print("Wochentag-Rabatt: 20%")

print(f"\nIhr Ticketpreis: {preis:.2f} Euro")
```

## Zusammenfassung

In diesem Kapitel haben Sie gelernt:

- `if`, `elif` und `else` für Verzweigungen
- Vergleichsoperatoren: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Die Bedeutung der Code-Einrückung in Python
- Logische Operatoren: `and`, `or`, `not`
- Verschachtelte Bedingungen und deren Vereinfachung

Im nächsten Kapitel lernen Sie Schleifen kennen, um Code wiederholt auszuführen.
