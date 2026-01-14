# Build-Anleitung für die Python Grundlagen Dokumentation

## Voraussetzungen

Installieren Sie die benötigten Pakete:

```bash
pip install -r requirements.txt
```

## HTML-Version erstellen

Die HTML-Version kann mit folgendem Befehl erstellt werden:

```bash
jupyter-book build .
```

Die fertige HTML-Dokumentation finden Sie dann in `_build/html/index.html`.

## PDF-Version erstellen

Für die PDF-Version benötigen Sie eine LaTeX-Installation:

### Linux (Debian/Ubuntu)
```bash
sudo apt-get install texlive-xetex texlive-fonts-recommended texlive-lang-german
```

### macOS
```bash
brew install basictex
```

### Windows
Laden Sie MiKTeX herunter: https://miktex.org/download

### PDF bauen
```bash
jupyter-book build . --builder pdflatex
```

Oder für bessere deutsche Unterstützung:
```bash
jupyter-book build . --builder pdflatex
```

Die PDF-Datei finden Sie in `_build/latex/python-grundlagen.pdf`.

## Fehlerbehebung

### "Error reading file: EISDIR"
Falls beim Build Probleme mit Verzeichnissen auftreten, stellen Sie sicher, dass:
- `exclude_patterns` in `_config.yml` korrekt konfiguriert ist
- `.git/` und `_build/` ausgeschlossen sind

### Dateien validieren
Führen Sie das Validierungsskript aus:
```bash
python3 validate.py
```

Dies prüft:
- Ob alle Codeblöcke korrekt geschlossen sind
- Ob problematische Unicode-Zeichen vorhanden sind
- Ob Dateien leer sind

## Struktur

```
.
├── _config.yml              # Jupyter Book Konfiguration
├── _toc.yml                 # Inhaltsverzeichnis
├── intro.md                 # Einführungsseite
├── chapters/                # Alle Kapitel
│   ├── 01_grundlagen.md
│   ├── 02_input_output.md
│   ├── 03_verzweigungen.md
│   ├── 04_schleifen.md
│   ├── 05_datenstrukturen.md
│   ├── 06_funktionen.md
│   ├── 07_standard_library.md
│   └── 08_dateioperationen.md
├── _build/                  # Generierte Ausgaben (nicht im Git)
├── requirements.txt         # Python-Abhängigkeiten
└── validate.py             # Validierungsskript
```

## Inhalt

Die Dokumentation deckt folgende Themen ab:

1. **Python-Grundlagen** - Installation, Konsole, Variablen, Datentypen, Namenskonventionen
2. **Input/Output** - Benutzereingaben, formatierte Ausgaben, Typumwandlung, Debugging
3. **Verzweigungen** - if/elif/else, Vergleichsoperatoren, logische Operatoren
4. **Schleifen** - while, for, range(), break, continue
5. **Datenstrukturen** - Listen, Dictionaries, Sets, Tuples
6. **Funktionen** - Definition, Parameter, Rückgabewerte, Scope, DRY-Prinzip
7. **Standard Library** - os, sys, pathlib, datetime, math, random, json
8. **Dateioperationen** - Lesen, Schreiben, Context Manager, CSV-Verarbeitung

## Verhältnis Text/Code

Alle Kapitel sind so gestaltet, dass das Verhältnis von Erklärungen zu Codebeispielen etwa 50:50 beträgt.

## Sprache

Die gesamte Dokumentation ist auf Deutsch und verwendet deutsche Spracheinstellungen für LaTeX/PDF.
