# GitHub Pages Setup für HTML-Dokumentation

## Option 1: GitHub Pages (Empfohlen)

### Aktivierung von GitHub Pages

1. **Im Repository auf GitHub:**
   - Gehen Sie zu: `Settings` → `Pages`
   - Under "Build and deployment":
     - **Source:** Deploy from a branch
     - **Branch:** `claude/find-perf-issues-mke0fhv0vosvruk0-KXCkr`
     - **Folder:** `/_build/html`
   - Klicken Sie auf `Save`

2. **Nach 1-2 Minuten ist Ihre Dokumentation verfügbar unter:**
   ```
   https://konitzertraining.github.io/python/
   ```

### Vorteile:
- ✅ Offizielles GitHub-Feature
- ✅ Automatische Updates bei Pushes
- ✅ Kostenlos
- ✅ HTTPS standardmäßig aktiviert
- ✅ Benutzerdefinierte Domains möglich

---

## Option 2: GitHub Raw Content Viewer (Sofort verfügbar)

### Mit htmlpreview.github.io

**URL-Format:**
```
https://htmlpreview.github.io/?https://raw.githubusercontent.com/KonitzerTraining/python/claude/find-perf-issues-mke0fhv0vosvruk0-KXCkr/_build/html/index.html
```

**Direktlink zu Ihrem Projekt:**
```
https://htmlpreview.github.io/?https://raw.githubusercontent.com/KonitzerTraining/python/claude/find-perf-issues-mke0fhv0vosvruk0-KXCkr/_build/html/index.html
```

### Vorteile:
- ✅ Sofort verfügbar (keine Konfiguration nötig)
- ✅ Keine Wartezeit
- ✅ Funktioniert mit jedem Branch

### Nachteile:
- ⚠️ Externe Service-Abhängigkeit
- ⚠️ Manchmal langsam bei großen Dateien
- ⚠️ CSS/JS-Ressourcen können Probleme machen

---

## Option 3: GitHack (Alternative)

**URL-Format:**
```
https://raw.githack.com/KonitzerTraining/python/claude/find-perf-issues-mke0fhv0vosvruk0-KXCkr/_build/html/index.html
```

### Für Entwicklung (aktualisiert sich schnell):
```
https://raw.githack.com/KonitzerTraining/python/claude/find-perf-issues-mke0fhv0vosvruk0-KXCkr/_build/html/index.html
```

### Für Produktion (mit CDN-Caching):
```
https://rawcdn.githack.com/KonitzerTraining/python/8913d57/_build/html/index.html
```

---

## Option 4: Direkt aus GitHub Repository navigieren

### Via GitHub's Code-Browser mit Codespaces (experimentell)

1. Gehen Sie zum Repository auf GitHub
2. Drücken Sie `.` (Punkt) auf der Tastatur
3. Öffnen Sie `_build/html/index.html` in VS Code Web
4. Nutzen Sie Live Preview Extension

---

## Empfehlung

**Beste Lösung: GitHub Pages (Option 1)**
- Professionell
- Zuverlässig
- Kostenlos
- Automatische Updates

**Schnellste Lösung: htmlpreview.github.io (Option 2)**
- Sofort nutzbar
- Keine Konfiguration
- Gut zum Testen

---

## Weitere Hosting-Optionen

### Netlify
1. Verbinden Sie GitHub-Repository
2. Build-Ordner: `_build/html`
3. Automatisches Deployment bei Push

### Vercel
1. Repository importieren
2. Output-Verzeichnis: `_build/html`
3. Automatisches Deployment

### GitLab Pages (falls Migration zu GitLab)
1. `.gitlab-ci.yml` erstellen
2. Build-Artefakte auf `public/` kopieren
3. Automatisches Deployment

---

## Custom Domain (für GitHub Pages)

Falls Sie eine eigene Domain haben:

1. **DNS konfigurieren:**
   ```
   CNAME Record: docs.ihre-domain.de → konitzertraining.github.io
   ```

2. **In GitHub Settings:**
   - Settings → Pages → Custom domain
   - Geben Sie `docs.ihre-domain.de` ein
   - Aktivieren Sie "Enforce HTTPS"

---

## Troubleshooting

### HTML-Seiten laden nicht richtig
- Prüfen Sie, ob alle CSS/JS-Dateien vorhanden sind
- Überprüfen Sie die Browser-Konsole auf Fehler
- Stellen Sie sicher, dass relative Pfade korrekt sind

### GitHub Pages zeigt 404
- Warten Sie 2-3 Minuten nach Aktivierung
- Prüfen Sie, ob der richtige Branch ausgewählt ist
- Stellen Sie sicher, dass `index.html` im Root des gewählten Ordners liegt

### Änderungen werden nicht angezeigt
- GitHub Pages cached Inhalte
- Warten Sie einige Minuten
- Hard-Refresh im Browser (Ctrl+Shift+R)
