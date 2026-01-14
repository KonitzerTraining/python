# Python Grundlagen Dokumentation

Eine deutschsprachige Python-Dokumentation im Jupyter Book Format.

## Inhalt

Die Dokumentation deckt folgende Themen ab:

1. Python-Grundlagen
2. Input/Output und Typumwandlung
3. Verzweigungen und Bedingungen
4. Schleifen
5. Datenstrukturen
6. Funktionen
7. Python Standard Library
8. Dateioperationen

## Buch erstellen

### HTML-Version erstellen

```bash
jupyter-book build .
```

Die HTML-Version finden Sie dann in `_build/html/index.html`.

### PDF-Version erstellen

Für PDF benötigen Sie LaTeX (z.B. TeX Live):

```bash
jupyter-book build . --builder pdflatex
```

Die PDF-Datei finden Sie in `_build/latex/python-grundlagen.pdf`.

## Installation

```bash
pip install -r requirements.txt
```

## Struktur

- `intro.md` - Einführung
- `chapters/` - Alle Kapitel
- `_config.yml` - Konfiguration
- `_toc.yml` - Inhaltsverzeichnis
- `_build/` - Generierte Ausgaben
