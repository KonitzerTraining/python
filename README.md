# Python Grundlagen Dokumentation

Eine deutschsprachige Python-Dokumentation im Jupyter Book Format.

## 🌐 Online ansehen

### GitHub Pages (empfohlen)
Nach Aktivierung von GitHub Pages (siehe unten) ist die Dokumentation verfügbar unter:
```
https://konitzertraining.github.io/python/
```

### Sofort verfügbar (ohne Setup)
Die HTML-Dokumentation können Sie direkt ansehen über:
```
https://htmlpreview.github.io/?https://raw.githubusercontent.com/KonitzerTraining/python/claude/find-perf-issues-mke0fhv0vosvruk0-KXCkr/_build/html/index.html
```

Oder mit GitHack:
```
https://raw.githack.com/KonitzerTraining/python/claude/find-perf-issues-mke0fhv0vosvruk0-KXCkr/_build/html/index.html
```

## 📖 Inhalt

Die Dokumentation deckt folgende Themen ab:

1. **Python-Grundlagen** - Installation, Konsole, Variablen, Datentypen, Namenskonventionen
2. **Input/Output und Typumwandlung** - Benutzereingaben, formatierte Ausgaben, Type Casting
3. **Verzweigungen und Bedingungen** - if/elif/else, Vergleichsoperatoren, logische Operatoren
4. **Schleifen** - while, for, range(), break, continue
5. **Datenstrukturen** - Listen, Dictionaries, Sets, Tuples
6. **Funktionen** - Definition, Parameter, Rückgabewerte, Scope, DRY-Prinzip
7. **Python Standard Library** - os, sys, pathlib, datetime, math, random, json
8. **Dateioperationen** - Lesen, Schreiben, Context Manager, CSV-Verarbeitung

**Besonderheit:** Alle Kapitel sind mit einem **50:50 Verhältnis** zwischen Erklärungen und Codebeispielen gestaltet.

## 🚀 GitHub Pages einrichten

Um die Dokumentation über GitHub Pages zu hosten:

1. Gehen Sie zu: **Settings** → **Pages**
2. Under "Build and deployment":
   - **Source:** Deploy from a branch
   - **Branch:** `claude/find-perf-issues-mke0fhv0vosvruk0-KXCkr`
   - **Folder:** `/_build/html`
3. Klicken Sie auf **Save**

Nach 1-2 Minuten ist die Dokumentation verfügbar.

Detaillierte Anleitung: Siehe [GITHUB_PAGES_SETUP.md](GITHUB_PAGES_SETUP.md)

## 🔧 Lokal bauen

### Installation

```bash
pip install -r requirements.txt
```

### HTML-Version erstellen

```bash
jupyter-book build .
```

Die fertige HTML-Dokumentation finden Sie dann in `_build/html/index.html`.

### Lokal als Webserver testen

```bash
cd _build/html
python3 -m http.server 8000
```

Dann öffnen Sie: http://localhost:8000

### PDF-Version erstellen

Für PDF benötigen Sie eine LaTeX-Installation:

**Linux (Debian/Ubuntu):**
```bash
sudo apt-get install texlive-xetex texlive-fonts-recommended texlive-lang-german
```

**macOS:**
```bash
brew install basictex
```

**PDF bauen:**
```bash
jupyter-book build . --builder pdflatex
```

Die PDF-Datei finden Sie in `_build/latex/python-grundlagen.pdf`.

## 📁 Struktur

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
├── _build/html/             # Generierte HTML-Ausgabe (im Repository)
├── requirements.txt         # Python-Abhängigkeiten
├── validate.py             # Validierungsskript
└── BUILD_INSTRUCTIONS.md   # Detaillierte Build-Anleitung
```

## 📊 Statistiken

- **Anzahl Kapitel:** 8
- **Gesamte Zeilen:** ~3.700
- **Markdown-Dateien:** ~91 KB
- **HTML-Build:** ~6.1 MB (inkl. alle Assets)
- **Code-Blöcke:** 356 (alle validiert)

## ✅ Qualitätssicherung

Alle Dateien wurden validiert:

```bash
python3 validate.py
```

Prüft:
- ✅ Korrekt geschlossene Code-Blöcke
- ✅ Keine problematischen Unicode-Zeichen
- ✅ Keine leeren Dateien

## 🌍 Sprache

Die gesamte Dokumentation ist auf **Deutsch** und verwendet deutsche Spracheinstellungen für LaTeX/PDF.

## 📝 Lizenz

Diese Dokumentation wurde für Bildungszwecke erstellt.

## 🤝 Beitragen

Verbesserungsvorschläge sind willkommen! Bitte erstellen Sie einen Issue oder Pull Request.

## 🔗 Weitere Ressourcen

- [Jupyter Book Dokumentation](https://jupyterbook.org/)
- [MyST Markdown Syntax](https://myst-parser.readthedocs.io/)
- [Python Offizielle Dokumentation](https://docs.python.org/de/)
