# Build-Anleitung: PROJEKTARBEIT.md → PDF

Wie aus `docs/PROJEKTARBEIT.md` ein abgabereifes PDF wird. Drei Varianten, vom einfachsten zum vollständigen Workflow.

---

## Voraussetzungen

```bash
# macOS via Homebrew
brew install pandoc
brew install --cask mactex-no-gui   # LaTeX-Engine für PDF-Output (xelatex/lualatex)

# Mermaid-Diagramme rendern (Variante 2 + 3)
npm install -g @mermaid-js/mermaid-cli
npm install -g mermaid-filter
```

Prüfen:

```bash
pandoc --version
xelatex --version
mmdc --version
```

---

## Variante 1 — Schnell-PDF (ohne Mermaid-Rendering)

Mermaid-Codeblöcke erscheinen als Code, nicht als Diagramme. Gut für Zwischenversionen / Korrekturlauf.

```bash
cd /Users/cheflouis/Documents/HTWG/Projektarbeit

pandoc docs/PROJEKTARBEIT.md \
  -o build/projektarbeit_draft.pdf \
  --pdf-engine=xelatex \
  --toc --toc-depth=3 \
  --number-sections \
  -V documentclass=scrreprt \
  -V papersize=a4 \
  -V fontsize=11pt \
  -V geometry:margin=2.5cm \
  -V lang=de \
  -V linkcolor=blue \
  -V urlcolor=blue \
  -V mainfont="Times New Roman"
```

Nicht vergessen: `mkdir -p build` einmalig.

---

## Variante 2 — Mit gerenderten Mermaid-Diagrammen

Nutzt `mermaid-filter` als Pandoc-Filter. Die Mermaid-Blöcke werden zur Build-Zeit zu PNG/SVG gerendert und ins PDF eingebettet.

```bash
pandoc docs/PROJEKTARBEIT.md \
  -o build/projektarbeit.pdf \
  --filter mermaid-filter \
  --pdf-engine=xelatex \
  --toc --toc-depth=3 \
  --number-sections \
  -V documentclass=scrreprt \
  -V papersize=a4 \
  -V fontsize=11pt \
  -V geometry:margin=2.5cm \
  -V lang=de \
  -V linkcolor=blue \
  -V urlcolor=blue \
  -V mainfont="Times New Roman"
```

`mermaid-filter` legt temporäre Bilddateien neben dem Markdown an — nach dem Build aufräumen oder via `.gitignore` ausschließen.

**Alternative ohne mermaid-filter:** Diagramme manuell auf <https://mermaid.live> einfügen, als PNG exportieren, in `docs/figures/` ablegen, und Mermaid-Blöcke durch `![Beschriftung](figures/abb1_ofh.png)` ersetzen.

---

## Variante 3 — Vollständig: Mermaid + Bibliographie

Setzt voraus, dass das Literaturverzeichnis als BibTeX-Datei vorliegt (Export aus Zotero/Citavi/Mendeley als `references.bib`). Damit übernimmt Pandoc die Zitations-Verarbeitung und das Literaturverzeichnis wird konsistent automatisch erzeugt.

1. **`docs/references.bib`** anlegen — alle Quellen aus Kap. 8 dorthin exportieren.
2. **In-Text-Zitate** sukzessive von `(Autor, Jahr)` auf `[@key]` umstellen — kann schrittweise geschehen, Pandoc verarbeitet beide Varianten parallel.
3. **Build:**

```bash
pandoc docs/PROJEKTARBEIT.md \
  -o build/projektarbeit.pdf \
  --filter mermaid-filter \
  --citeproc \
  --bibliography=docs/references.bib \
  --csl=docs/apa-7.csl \
  --pdf-engine=xelatex \
  --toc --toc-depth=3 \
  --number-sections \
  -V documentclass=scrreprt \
  -V papersize=a4 \
  -V fontsize=11pt \
  -V geometry:margin=2.5cm \
  -V lang=de \
  -V linkcolor=blue \
  -V urlcolor=blue \
  -V mainfont="Times New Roman"
```

CSL-Datei (APA 7. Edition):
```bash
curl -L https://www.zotero.org/styles/apa -o docs/apa-7.csl
```

---

## Vor der Abgabe — Checkliste

- [ ] Deckblatt-TODOs in `PROJEKTARBEIT.md` ausgefüllt (Matrikelnummer, Studiengang, Prüfer, Studienabschluss, Abgabedatum)
- [ ] Eidesstattliche Erklärung mit Datum und Unterschrift (im PDF nach Druck per Hand)
- [ ] Mermaid-Diagramme rendern korrekt (Variante 2 oder 3)
- [ ] Inhaltsverzeichnis ist generiert (`--toc`)
- [ ] Seitenzahlen korrekt (`numbersections`)
- [ ] Abbildungs- und Tabellenverzeichnis aktuell (manuell pflegen, Liste in Kap. 0)
- [ ] Plagiatsprüfung durchgelaufen (Turnitin/PlagScan/o.ä.)
- [ ] Letzter Lese-Pass durch (LanguageTool / Korrekturlesen)

---

## Bekannte Probleme

- **Umlaute:** Bei xelatex problemlos. Bei pdflatex müsste `\usepackage[utf8]{inputenc}` hinzu — vermeiden, xelatex nutzen.
- **Lange Tabellen:** Brauchen ggf. `longtable`-Paket. In aktuellem Pandoc bereits Default.
- **Mermaid in xelatex:** PNG-Export via `mermaid-filter` ist robuster als SVG-Embed.
- **HTWG-Vorlage:** Falls die HTWG eine offizielle LaTeX-Vorlage vorgibt, ist der saubere Weg, die Inhalte manuell aus dem PDF in die Vorlage zu übertragen — Pandoc-Standardlayout wird dann zur Zwischenstufe.
