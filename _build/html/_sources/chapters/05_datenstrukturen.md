# Datenstrukturen

Datenstrukturen ermöglichen es, mehrere Werte in einer einzigen Variable zu speichern und effizient zu verwalten. Python bietet vier grundlegende Datenstrukturen: Listen, Dictionaries, Sets und Tuples.

## Listen erstellen und verwenden

Listen sind geordnete, veränderbare Sammlungen von Elementen. Sie können Elemente unterschiedlicher Datentypen enthalten.

### Listen erstellen

```python
# Leere Liste:
leere_liste = []

# Liste mit Zahlen:
zahlen = [1, 2, 3, 4, 5]

# Liste mit Strings:
fruechte = ["Apfel", "Banane", "Orange"]

# Gemischte Liste:
gemischt = [1, "Text", 3.14, True]

print(zahlen)      # [1, 2, 3, 4, 5]
print(fruechte)    # ['Apfel', 'Banane', 'Orange']
```

### Auf Listenelemente zugreifen (Indexierung)

Listen verwenden null-basierte Indexierung:

```python
fruechte = ["Apfel", "Banane", "Orange", "Kiwi"]

# Erstes Element (Index 0):
print(fruechte[0])    # Apfel

# Zweites Element:
print(fruechte[1])    # Banane

# Letztes Element:
print(fruechte[-1])   # Kiwi

# Vorletztes Element:
print(fruechte[-2])   # Orange
```

### Slicing - Teillisten extrahieren

```python
zahlen = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Von Index 2 bis 5 (exklusive):
print(zahlen[2:5])     # [2, 3, 4]

# Von Anfang bis Index 4:
print(zahlen[:4])      # [0, 1, 2, 3]

# Von Index 6 bis Ende:
print(zahlen[6:])      # [6, 7, 8, 9]

# Jedes zweite Element:
print(zahlen[::2])     # [0, 2, 4, 6, 8]

# Liste umkehren:
print(zahlen[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

## Listen-Operationen: append, remove, insert, sort

Listen sind veränderbar (mutable), d.h. Sie können Elemente hinzufügen, entfernen und ändern.

### Elemente hinzufügen

**append() - Am Ende anfügen:**

```python
fruechte = ["Apfel", "Banane"]
fruechte.append("Orange")
print(fruechte)  # ['Apfel', 'Banane', 'Orange']

# Mehrere Elemente hinzufügen:
zahlen = [1, 2, 3]
zahlen.append(4)
zahlen.append(5)
print(zahlen)  # [1, 2, 3, 4, 5]
```

**insert() - An bestimmter Position einfügen:**

```python
fruechte = ["Apfel", "Orange"]
fruechte.insert(1, "Banane")  # An Index 1 einfügen
print(fruechte)  # ['Apfel', 'Banane', 'Orange']

# Am Anfang einfügen:
zahlen = [2, 3, 4]
zahlen.insert(0, 1)
print(zahlen)  # [1, 2, 3, 4]
```

**extend() - Mehrere Elemente anfügen:**

```python
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
liste1.extend(liste2)
print(liste1)  # [1, 2, 3, 4, 5, 6]

# Alternative: + Operator
liste_a = [1, 2]
liste_b = [3, 4]
liste_c = liste_a + liste_b
print(liste_c)  # [1, 2, 3, 4]
```

### Elemente entfernen

**remove() - Erstes Vorkommen entfernen:**

```python
fruechte = ["Apfel", "Banane", "Orange", "Banane"]
fruechte.remove("Banane")
print(fruechte)  # ['Apfel', 'Orange', 'Banane']
```

**pop() - Element an Index entfernen (und zurückgeben):**

```python
zahlen = [10, 20, 30, 40]

# Letztes Element entfernen:
letztes = zahlen.pop()
print(letztes)  # 40
print(zahlen)   # [10, 20, 30]

# Element an Index 1 entfernen:
element = zahlen.pop(1)
print(element)  # 20
print(zahlen)   # [10, 30]
```

**clear() - Alle Elemente entfernen:**

```python
liste = [1, 2, 3, 4, 5]
liste.clear()
print(liste)  # []
```

### Listen sortieren und umkehren

**sort() - Liste sortieren (in-place):**

```python
zahlen = [3, 1, 4, 1, 5, 9, 2]
zahlen.sort()
print(zahlen)  # [1, 1, 2, 3, 4, 5, 9]

# Absteigend sortieren:
zahlen.sort(reverse=True)
print(zahlen)  # [9, 5, 4, 3, 2, 1, 1]

# Strings alphabetisch sortieren:
namen = ["Zoe", "Anna", "Max", "Ben"]
namen.sort()
print(namen)  # ['Anna', 'Ben', 'Max', 'Zoe']
```

**sorted() - Neue sortierte Liste erstellen:**

```python
original = [3, 1, 4, 1, 5]
sortiert = sorted(original)
print(original)   # [3, 1, 4, 1, 5] (unverändert)
print(sortiert)   # [1, 1, 3, 4, 5]
```

**reverse() - Liste umkehren:**

```python
zahlen = [1, 2, 3, 4, 5]
zahlen.reverse()
print(zahlen)  # [5, 4, 3, 2, 1]
```

### Weitere nützliche Listen-Methoden

```python
fruechte = ["Apfel", "Banane", "Orange", "Banane"]

# Länge der Liste:
print(len(fruechte))  # 4

# Anzahl eines Elements:
print(fruechte.count("Banane"))  # 2

# Index eines Elements finden:
print(fruechte.index("Orange"))  # 2

# Prüfen, ob Element vorhanden:
print("Apfel" in fruechte)  # True
print("Kiwi" in fruechte)   # False
```

## Auf Listenelemente zugreifen (Indexierung)

Wir haben bereits Indexierung kennengelernt. Hier weitere wichtige Konzepte:

### Negative Indizes

```python
zahlen = [10, 20, 30, 40, 50]

print(zahlen[-1])   # 50 (letztes Element)
print(zahlen[-2])   # 40 (vorletztes Element)
print(zahlen[-5])   # 10 (erstes Element)
```

### Listen verschachteln

```python
# Matrix (2D-Liste):
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Auf Elemente zugreifen:
print(matrix[0])        # [1, 2, 3] (erste Zeile)
print(matrix[0][0])     # 1
print(matrix[1][2])     # 6
print(matrix[2][1])     # 8

# Über Matrix iterieren:
for zeile in matrix:
    for element in zeile:
        print(element, end=" ")
    print()
# Ausgabe:
# 1 2 3
# 4 5 6
# 7 8 9
```

### List Comprehensions

Eine kompakte Methode, Listen zu erstellen:

```python
# Traditionell:
quadrate = []
for x in range(10):
    quadrate.append(x ** 2)
print(quadrate)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Mit List Comprehension:
quadrate = [x ** 2 for x in range(10)]
print(quadrate)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Mit Bedingung:
gerade = [x for x in range(20) if x % 2 == 0]
print(gerade)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

## Listen mit Schleifen durchlaufen

### Mit for-Schleife

```python
fruechte = ["Apfel", "Banane", "Orange"]

# Über Elemente iterieren:
for frucht in fruechte:
    print(f"Ich mag {frucht}")

# Mit Index:
for i in range(len(fruechte)):
    print(f"{i}: {fruechte[i]}")

# Mit enumerate (empfohlen):
for index, frucht in enumerate(fruechte):
    print(f"{index}: {frucht}")
```

### Liste filtern und transformieren

```python
zahlen = [1, -5, 3, -2, 8, -7, 4]

# Nur positive Zahlen:
positive = []
for zahl in zahlen:
    if zahl > 0:
        positive.append(zahl)
print(positive)  # [1, 3, 8, 4]

# Oder mit List Comprehension:
positive = [zahl for zahl in zahlen if zahl > 0]
print(positive)  # [1, 3, 8, 4]

# Alle Werte verdoppeln:
verdoppelt = [zahl * 2 for zahl in zahlen]
print(verdoppelt)  # [2, -10, 6, -4, 16, -14, 8]
```

## Dictionaries (Schlüssel-Wert-Paare)

Dictionaries speichern Daten als Schlüssel-Wert-Paare. Sie sind ungeordnet (ab Python 3.7 Einfügereihenfolge erhalten) und veränderbar.

### Dictionaries erstellen

```python
# Leeres Dictionary:
leeres_dict = {}

# Dictionary mit Daten:
person = {
    "name": "Anna",
    "alter": 25,
    "stadt": "Berlin"
}

# Alternative Syntax:
produkt = dict(name="Laptop", preis=999, lagerbestand=50)

print(person)   # {'name': 'Anna', 'alter': 25, 'stadt': 'Berlin'}
print(produkt)  # {'name': 'Laptop', 'preis': 999, 'lagerbestand': 50}
```

### Auf Werte zugreifen

```python
person = {
    "name": "Max",
    "alter": 30,
    "beruf": "Programmierer"
}

# Mit Schlüssel:
print(person["name"])   # Max
print(person["alter"])  # 30

# Mit get() (sicherer):
print(person.get("beruf"))        # Programmierer
print(person.get("telefon"))      # None (kein Fehler)
print(person.get("telefon", "Nicht vorhanden"))  # Nicht vorhanden
```

### Werte ändern und hinzufügen

```python
person = {"name": "Lisa", "alter": 28}

# Wert ändern:
person["alter"] = 29
print(person)  # {'name': 'Lisa', 'alter': 29}

# Neues Schlüssel-Wert-Paar hinzufügen:
person["stadt"] = "München"
print(person)  # {'name': 'Lisa', 'alter': 29, 'stadt': 'München'}

# Mehrere Paare hinzufügen mit update():
person.update({"beruf": "Ärztin", "hobby": "Lesen"})
print(person)
# {'name': 'Lisa', 'alter': 29, 'stadt': 'München', 'beruf': 'Ärztin', 'hobby': 'Lesen'}
```

### Elemente entfernen

```python
person = {"name": "Tom", "alter": 35, "stadt": "Hamburg"}

# Mit pop():
alter = person.pop("alter")
print(alter)   # 35
print(person)  # {'name': 'Tom', 'stadt': 'Hamburg'}

# Mit del:
del person["stadt"]
print(person)  # {'name': 'Tom'}

# Alle Elemente entfernen:
person.clear()
print(person)  # {}
```

### Über Dictionaries iterieren

```python
noten = {"Anna": 1, "Max": 2, "Lisa": 1, "Tom": 3}

# Über Schlüssel iterieren:
for name in noten:
    print(name)

# Über Schlüssel (explizit):
for name in noten.keys():
    print(name, noten[name])

# Über Werte:
for note in noten.values():
    print(note)

# Über Schlüssel und Werte:
for name, note in noten.items():
    print(f"{name} hat Note {note}")
# Ausgabe:
# Anna hat Note 1
# Max hat Note 2
# Lisa hat Note 1
# Tom hat Note 3
```

### Nützliche Dictionary-Methoden

```python
person = {"name": "Eva", "alter": 27, "stadt": "Köln"}

# Alle Schlüssel:
print(person.keys())    # dict_keys(['name', 'alter', 'stadt'])

# Alle Werte:
print(person.values())  # dict_values(['Eva', 27, 'Köln'])

# Alle Paare:
print(person.items())   # dict_items([('name', 'Eva'), ('alter', 27), ('stadt', 'Köln')])

# Prüfen, ob Schlüssel existiert:
print("name" in person)      # True
print("telefon" in person)   # False

# Anzahl der Einträge:
print(len(person))  # 3
```

## Sets und Tuples (Überblick)

### Sets - Ungeordnete Mengen ohne Duplikate

Sets sind ungeordnete Sammlungen eindeutiger Elemente:

```python
# Set erstellen:
fruechte = {"Apfel", "Banane", "Orange"}
zahlen = set([1, 2, 3, 2, 1])  # Duplikate werden entfernt
print(zahlen)  # {1, 2, 3}

# Element hinzufügen:
fruechte.add("Kiwi")
print(fruechte)  # {'Apfel', 'Banane', 'Orange', 'Kiwi'}

# Element entfernen:
fruechte.remove("Banane")
print(fruechte)  # {'Apfel', 'Orange', 'Kiwi'}

# Mengenoperationen:
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(set_a | set_b)  # Vereinigung: {1, 2, 3, 4, 5, 6}
print(set_a & set_b)  # Schnittmenge: {3, 4}
print(set_a - set_b)  # Differenz: {1, 2}
```

**Praktisches Beispiel - Duplikate entfernen:**

```python
zahlen_mit_duplikaten = [1, 2, 2, 3, 4, 4, 4, 5]
eindeutige_zahlen = list(set(zahlen_mit_duplikaten))
print(eindeutige_zahlen)  # [1, 2, 3, 4, 5] (Reihenfolge kann variieren)
```

### Tuples - Unveränderbare Sequenzen

Tuples sind wie Listen, aber unveränderbar (immutable):

```python
# Tuple erstellen:
koordinaten = (10, 20)
person = ("Anna", 25, "Berlin")

# Auf Elemente zugreifen:
print(koordinaten[0])  # 10
print(person[1])       # 25

# Tuple Unpacking:
x, y = koordinaten
print(f"x={x}, y={y}")  # x=10, y=20

name, alter, stadt = person
print(f"{name} ist {alter} Jahre alt")  # Anna ist 25 Jahre alt

# Tuples sind unveränderbar:
# koordinaten[0] = 15  # Fehler: TypeError
```

**Wann Tuples verwenden?**

```python
# Für unveränderliche Daten:
rgb_farbe = (255, 128, 0)

# Als Dictionary-Schlüssel (Listen gehen nicht):
koordinaten_dict = {
    (0, 0): "Ursprung",
    (1, 0): "X-Achse",
    (0, 1): "Y-Achse"
}

# Mehrere Werte aus Funktion zurückgeben:
def min_max(zahlen):
    return min(zahlen), max(zahlen)

minimum, maximum = min_max([1, 5, 3, 9, 2])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 9
```

## Zusammenfassung

In diesem Kapitel haben Sie gelernt:

- **Listen:** Geordnete, veränderbare Sequenzen mit Methoden wie `append()`, `remove()`, `insert()`, `sort()`
- **Indexierung und Slicing:** Zugriff auf Elemente mit `[]`, negative Indizes, Slicing mit `[start:stop:step]`
- **Dictionaries:** Schlüssel-Wert-Paare mit Methoden wie `get()`, `keys()`, `values()`, `items()`
- **Sets:** Ungeordnete Mengen ohne Duplikate
- **Tuples:** Unveränderbare Sequenzen

Im nächsten Kapitel lernen Sie, wie Sie Funktionen definieren und verwenden, um Code wiederverwendbar zu machen.
