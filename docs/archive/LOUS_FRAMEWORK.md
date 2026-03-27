# Lou's Framework: Agentic Innovation Process (AIP)

> Arbeitstitel. Ein eigenes Framework zur Optimierung von Innovationsprozessen in Startups durch agentische KI-Systeme – mit Fokus auf Unternehmen, die ungenutztes Innovationspotenzial erschließen wollen.

---

## 1. Grundlage: Der Hybridansatz

Das Framework kombiniert fünf bewährte Ansätze, die jeweils eine spezifische Rolle übernehmen:

| Rolle | Quelle | Was es beiträgt |
|-------|--------|-----------------|
| Prozessarchitektur | BIG Picture (Lercher) | Der zyklische Gesamtrahmen mit Stages & Gates |
| Taktische Iteration | Lean Startup (Ries) | Build-Measure-Learn Loops innerhalb jeder Phase |
| Business-Model-Repräsentation | BMC (Osterwalder) | Strukturierte Darstellung des Geschäftsmodells als Arbeitsgrundlage für Agents |
| Kunden-/Markt-Intelligence | JTBD (Christensen/Ulwick) | Systematische Identifikation unerfüllter Kundenbedürfnisse |
| Theoretische Linse | Ambidextrous Org (O'Reilly/Tushman) | Erklärt Exploitation-Dominanz und legitimiert den Exploration-Fokus |

---

## 2. Detaillierter Hybrid: Phasen & Agent-Mapping

### Phase A: ERKENNEN (Wo stehen wir? Wo liegt ungenutztes Potenzial?)

**Herkunft**: BIG Picture (Lifecycle Management + Innovationslücke) + Ambidextrous Org

**Ziel**: Die Innovationslücke des Startups identifizieren und ungenutztes Potenzial sichtbar machen.

**Schritte**:
1. **Ist-Analyse des Geschäftsmodells** – BMC des aktuellen Zustands erstellen
2. **Exploitation/Exploration-Audit** – Wo liegt der Fokus? Wird nur optimiert statt exploriert?
3. **Markt- & Technologie-Frühaufklärung** – Trends, Wettbewerber, technologische Entwicklungen
4. **Innovationslücke formulieren** – Gap zwischen Ist-Zustand und Marktpotenzial

**Potenzielle KI-Agents**:
- `audit-agent`: Analysiert Unternehmensdaten (Finanzen, Produkte, Kunden) und erstellt BMC
- `market-scanner-agent`: Scannt Markttrends, Wettbewerber, Patente, Startup-Datenbanken
- `gap-detector-agent`: Vergleicht Ist-BMC mit Marktdaten und identifiziert Lücken

**Gate A → B**: Innovationslücke validiert? Potenzialfelder identifiziert?

---

### Phase B: AUSRICHTEN (Wohin wollen wir innovieren?)

**Herkunft**: BIG Picture (Strategiefindung + Strategy Gate) + JTBD

**Ziel**: Aus der erkannten Lücke eine Innovationsstrategie mit konkreten Suchfeldern ableiten.

**Schritte**:
1. **Jobs-to-be-Done Analyse** – Welche "Jobs" haben Kunden, die unzureichend erfüllt werden?
2. **Opportunity Scoring** – Quantitative Bewertung: Importance × (1 - Satisfaction)
3. **Suchfeld-Definition** – Konkrete Innovationsrichtungen basierend auf Top-Opportunities
4. **Innovationsklassen-Entscheidung** – Inkrementell, progressiv, radikal oder disruptiv?
5. **Ressourcen- & Zeitplanung** – Was ist mit den vorhandenen Mitteln machbar?

**Potenzielle KI-Agents**:
- `jtbd-extractor-agent`: Extrahiert Job-Statements aus Kundendaten (Reviews, Support-Tickets, Interviews)
- `opportunity-scorer-agent`: Bewertet und rankt Opportunities quantitativ
- `strategy-synthesizer-agent`: Generiert Strategieoptionen basierend auf Opportunities + Unternehmenskontext

**Gate B → C**: Innovationsstrategie verabschiedet? Suchfelder definiert?

---

### Phase C: IDEIEREN (Wie könnten Lösungen aussehen?)

**Herkunft**: BIG Picture (Ideation) + Lean Startup (Hypothesenbildung)

**Ziel**: Aus den Suchfeldern konkrete Innovationsideen generieren und als testbare Hypothesen formulieren.

**Schritte**:
1. **Divergentes Ideieren** – Breite Ideengenerierung entlang der Suchfelder
2. **Cross-Domain-Inspiration** – Analogien aus anderen Branchen und Märkten
3. **Ideen-Clustering & -Bewertung** – Gruppieren, priorisieren (Impact vs. Feasibility)
4. **Hypothesenformulierung** – Jede Top-Idee wird als testbare Hypothese formuliert
5. **BMC-Entwurf** – Für jede Hypothese ein Soll-BMC skizzieren

**Potenzielle KI-Agents**:
- `ideation-agent`: Generiert Ideen basierend auf Suchfeldern + Cross-Domain-Wissen
- `evaluation-agent`: Bewertet Ideen nach definierten Kriterien (Impact, Feasibility, Fit)
- `hypothesis-agent`: Formuliert testbare Hypothesen mit klaren Metriken

**Gate C → D**: Top-Hypothesen ausgewählt? Bewertungskriterien klar?

---

### Phase D: VALIDIEREN (Funktioniert es?)

**Herkunft**: Lean Startup (Build-Measure-Learn) + BIG Picture (Umsetzungspfade)

**Ziel**: Hypothesen durch schnelle Experimente testen und iterativ verfeinern.

**Schritte**:
1. **MVP definieren** – Minimales Experiment pro Hypothese
2. **Build** – MVP/Experiment umsetzen
3. **Measure** – Daten sammeln (Actionable Metrics, nicht Vanity Metrics)
4. **Learn** – Ergebnisse auswerten → Pivot, Persevere oder Kill
5. **Iterieren** – Loop wiederholen bis Validierung oder Pivot

**Pfade je Innovationsklasse** (aus BIG Picture):
- Inkrementell: Schnelle Umsetzung, wenige Loops (Stage-Gate Xpress)
- Progressiv: Moderate Validierung (Stage-Gate Lite)
- Radikal: Intensive Validierung, mehrere Pivots möglich (Full Stage-Gate)
- Disruptiv: Sonderprojekt mit eigener Governance

**Potenzielle KI-Agents**:
- `experiment-designer-agent`: Entwirft MVPs und Testsetups
- `analytics-agent`: Trackt Metriken, erkennt statistische Signifikanz
- `pivot-advisor-agent`: Analysiert Ergebnisse und empfiehlt Pivot/Persevere/Kill

**Gate D → E**: Hypothese validiert? Business Case tragfähig?

---

### Phase E: KONTROLLIEREN (Was haben wir gelernt?)

**Herkunft**: BIG Picture (Erfolgskontrolle + Lifecycle Management)

**Ziel**: Ergebnisse evaluieren, Learnings sichern, nächsten Zyklus vorbereiten.

**Schritte**:
1. **Zielerreichung prüfen** – Inhaltlich und organisatorisch
2. **Innovationsprojekte analysieren** – Was hat funktioniert, was nicht?
3. **Innovationssystem evaluieren** – Prozess selbst bewerten und verbessern
4. **Learnings dokumentieren** – Für Organisation und für die KI-Agents (Lernschleife)
5. **Nächsten Zyklus initiieren** – Zurück zu Phase A mit neuem Wissen

**Potenzielle KI-Agents**:
- `retrospective-agent`: Strukturierte Analyse der Projektergebnisse
- `knowledge-agent`: Speichert Learnings für zukünftige Zyklen (organisationales Gedächtnis)
- `cycle-initiator-agent`: Identifiziert nächste Innovationslücke basierend auf Learnings

**Gate E → A**: Learnings dokumentiert? Nächster Zyklus definiert?

---

## 3. Das Gesamtbild: Der Zyklus

```
    ┌─────────────────────────────────────────────┐
    │                                             │
    ▼                                             │
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│    A      │───▶│    B      │───▶│    C      │───▶│    D      │───▶│    E      │
│ ERKENNEN  │    │AUSRICHTEN │    │ IDEIEREN  │    │VALIDIEREN │    │KONTROLL. │
│           │    │           │    │           │    │           │    │           │
│ Wo stehen │    │ Wohin     │    │ Wie       │    │Funktio-   │    │ Was haben │
│ wir?      │    │ wollen    │    │ könnten   │    │niert es?  │    │ wir       │
│           │    │ wir?      │    │ Lösungen  │    │           │    │ gelernt?  │
│           │    │           │    │ aussehen? │    │ BML-Loops │    │           │
└──────────┘    └──────────┘    └──────────┘    └──────────┘    └──────────┘
    ▲               │                │               │               │
    │          Gate A→B         Gate B→C         Gate C→D         Gate D→E
    │                                                                │
    └────────────────────────────────────────────────────────────────┘
                            Lernschleife
```

---

## 4. Agent-Governance: Orchestrierte Hierarchie mit Feedback-Loops (L2 + L3)

> Kern-Insight: Weder reine Hierarchie noch reiner Schwarm. Die Agents brauchen einen Orchestrator für Struktur, aber demokratisches Feedback für Qualität – und den Menschen als letzte Instanz an strategischen Entscheidungspunkten.

### 4.1 Das Architekturmodell: "Orchestrated Feedback Hierarchy" (OFH)

```
                    ┌─────────────┐
                    │   MENSCH    │
                    │  (Gründer/  │
                    │   Team)     │
                    └──────┬──────┘
                           │ Strategische Entscheidungen
                           │ an Gates + bei Eskalation
                           ▼
                    ┌─────────────┐
                    │ORCHESTRATOR │
                    │   AGENT     │◄──── Erhält aggregiertes
                    │             │      Feedback vom Sprecher
                    └──────┬──────┘
                           │ Delegiert Aufgaben
              ┌────────────┼────────────┐
              ▼            ▼            ▼
        ┌───────────┐┌───────────┐┌───────────┐
        │Spezialist │││Spezialist │││Spezialist │
        │    A1     │││    A2     │││    A3     │
        └─────┬─────┘└─────┬─────┘└─────┬─────┘
              │            │            │
              └─────┬──────┴──────┬─────┘
                    ▼             │
              ┌───────────┐      │
              │ SPRECHER  │◄─────┘
              │  (gewählt │  Feedback-Loop:
              │  von A1-  │  Spezialisten diskutieren,
              │  A3)      │  wählen Sprecher, der
              └───────────┘  aggregiert an Orchestrator
                             berichtet
```

### 4.2 Die vier Rollen im Detail

#### Mensch (Gründer / Innovationsteam)
- **Wann aktiv**: An jedem Gate (A→B, B→C, C→D, D→E, E→A) + bei Eskalation
- **Entscheidungsgewalt**: Strategische Richtung, Go/Kill, Ressourcenfreigabe, ethische Fragen
- **Interaktion**: Spricht primär mit dem Orchestrator, nie direkt mit Spezialisten
- **Kann jederzeit**: Eingreifen, Richtung ändern, Prozess pausieren

#### Orchestrator-Agent
- **Rolle**: Zentrale Steuerungsinstanz. Verteilt Aufgaben, sammelt Ergebnisse, bereitet Gate-Entscheidungen vor
- **Entscheidungsgewalt**: Operative Entscheidungen innerhalb einer Phase (z.B. welche Datenquelle zuerst, welche Analyse-Methode)
- **Eskaliert an Mensch wenn**: Widersprüchliches Feedback der Spezialisten; unerwartete Erkenntnisse; Ressourcenbedarf über Budget; ethische Graubereiche
- **Kernfähigkeit**: Kontext halten – kennt die Gesamtstrategie und ordnet Einzelergebnisse ein

#### Spezialisten-Agents (pro Phase 2-4 aktiv)
- **Rolle**: Domänenexperten. Führen spezifische Analysen, Recherchen, Generierungen durch
- **Entscheidungsgewalt**: Keine strategische. Dürfen innerhalb ihres Auftrags Methoden wählen
- **Feedback-Mechanismus**: Nach jeder Auftragsrunde treten die aktiven Spezialisten in eine **Feedback-Schleife**:
  1. Jeder Spezialist teilt seine Ergebnisse + Einschätzung
  2. Sie identifizieren Widersprüche, Lücken, Synergien untereinander
  3. Sie wählen einen **Sprecher**

#### Sprecher-Agent (dynamisch gewählt)
- **Rolle**: Von den Spezialisten gewählter Vertreter, der das aggregierte Feedback an den Orchestrator kommuniziert
- **Wahllogik**: Der Spezialist mit der höchsten Relevanz für die aktuelle Fragestellung wird Sprecher (z.B. in Phase A der `gap-detector-agent`, in Phase C der `evaluation-agent`)
- **Kommuniziert**: Konsens, Dissens, offene Fragen, Empfehlungen der Gruppe
- **Lebensdauer**: Wechselt pro Feedback-Runde – keine permanente Machtposition

### 4.3 Der Feedback-Loop im Detail

```
Orchestrator gibt Auftrag an Spezialisten
            │
            ▼
┌─────────────────────────────┐
│  Spezialisten arbeiten      │
│  parallel an Teilaufgaben   │
└──────────────┬──────────────┘
               ▼
┌─────────────────────────────┐
│  FEEDBACK-RUNDE             │
│                             │
│  1. Ergebnisse teilen       │
│  2. Cross-Check:            │
│     - Widersprüche?         │
│     - Blinde Flecken?       │
│     - Synergien?            │
│  3. Sprecher wählen         │
│  4. Konsens formulieren     │
└──────────────┬──────────────┘
               ▼
     Sprecher → Orchestrator
               │
               ▼
    ┌─────────────────────┐
    │ Orchestrator         │
    │ evaluiert:           │
    │                      │
    │ Ausreichend? ──YES──▶ Gate vorbereiten → Mensch
    │       │              │
    │      NO              │
    │       │              │
    │       ▼              │
    │ Neue Anweisungen     │
    │ an Spezialisten      │
    └─────────────────────┘
```

### 4.4 Human-AI-Interaction-Protokoll (L3)

| Situation | Wer entscheidet | Warum |
|-----------|----------------|-------|
| Welche Datenquelle analysieren? | Orchestrator | Operative Entscheidung |
| Welche Analysemethode verwenden? | Spezialist | Domänenkompetenz |
| Innovationslücke priorisieren | **Mensch** | Strategische Richtung |
| Suchfeld auswählen | **Mensch** | Unternehmerische Vision |
| Ideen generieren | Spezialisten | Kreative Aufgabe |
| Ideen bewerten und filtern | Orchestrator + **Mensch** | Co-Entscheidung |
| MVP-Design entscheiden | **Mensch** | Ressourcenfreigabe |
| Experiment-Ergebnisse interpretieren | Orchestrator → **Mensch** | Agent bereitet vor, Mensch entscheidet |
| Pivot / Persevere / Kill | **Mensch** | Existenzielle Entscheidung |
| Nächsten Zyklus starten | **Mensch** | Strategisch |
| Widersprüchliche Agent-Ergebnisse | Eskalation → **Mensch** | Orchestrator kann nicht auflösen |
| Ethische Graubereiche | Immer **Mensch** | Nicht delegierbar |

### 4.5 Warum dieses Modell?

**Gegenüber reiner Hierarchie (Orchestrator allein):**
- Der Feedback-Loop verhindert, dass der Orchestrator zum Bottleneck wird
- Spezialisten können Fehler des Orchestrators korrigieren (kein Single Point of Failure)
- Emergente Erkenntnisse aus der Spezialisten-Diskussion, die ein Top-Down-System verpassen würde

**Gegenüber reinem Schwarm:**
- Klare Verantwortlichkeit – der Orchestrator hält den Kontext
- Der Mensch hat einen einzigen Ansprechpartner, nicht ein Chaos aus Agents
- Ergebnisse sind nachvollziehbar und auditierbar

**Gegenüber Phasen-Agents:**
- Kein Kontextverlust zwischen Phasen – der Orchestrator überlebt alle Phasen
- Spezialisten können phasenübergreifend wiederverwendet werden

**Wissenschaftliche Einordnung:**
- Verbindet Prinzipien aus Multi-Agent-Systemen (MAS) mit organisationstheoretischen Konzepten
- Der Sprecher-Mechanismus ist inspiriert von demokratischer Entscheidungstheorie und Delphi-Methode
- Die Eskalationslogik folgt dem Prinzip der Subsidiarität: Entscheidungen werden auf der niedrigstmöglichen Ebene getroffen

---

## 5. Daten-Realität in Startups: Der Daten-Layer (L1)

> Kern-Insight: Das Framework muss mit **jeder Datenlage** funktionieren – mal besser, mal schlechter, aber nie gar nicht. Startups haben selten saubere Datenstrukturen. Das ist kein Bug, das ist die Realität.

### 4.1 Datenreifegrad-Modell

Das Framework führt ein **Datenreifegrad-Modell** ein, das bestimmt, wie die Agents arbeiten und welche Ergebnisqualität realistisch erwartbar ist:

| Stufe | Name | Typische Datenquellen | Agent-Modus | Ergebnis-Konfidenz |
|:-----:|------|----------------------|-------------|-------------------|
| **1** | **Minimal** | Gespräche, Notizen, Gründer-Wissen im Kopf, vereinzelte Dokumente | Explorativer Modus: Agents stellen vor allem Fragen, strukturieren Implizites, generieren Hypothesen aus Minimalinput | Niedrig – eher Impulse als Analysen |
| **2** | **Fragmentiert** | CRM mit Lücken, Google Analytics, Social Media, E-Mail-Verkehr, unstrukturierte Dokumente (Pitch Decks, Protokolle) | Aggregations-Modus: Agents sammeln, verknüpfen und finden Muster in unstrukturierten Quellen | Mittel – Muster erkennbar, aber lückenhaft |
| **3** | **Strukturiert** | Sauberes CRM, Finanzdaten, Produkt-Analytics, Kundenfeedback-Systeme, dokumentierte Prozesse | Analyse-Modus: Agents führen quantitative Auswertungen durch, erkennen statistische Zusammenhänge | Hoch – belastbare Aussagen möglich |
| **4** | **Datengetrieben** | Data Warehouse, BI-Tools, A/B-Test-Infrastruktur, automatisiertes Tracking, API-Integrationen | Optimierungs-Modus: Agents arbeiten datengetrieben, können eigenständig testen und iterieren | Sehr hoch – prädiktive Aussagen möglich |

### 4.2 Datenquellen-Mapping pro Phase

| Phase | Ideale Daten | Minimaldaten (Stufe 1-2) | Was Agents daraus machen |
|-------|-------------|-------------------------|-------------------------|
| **A – ERKENNEN** | Finanzdaten, Marktdaten, Produkt-Metriken, Wettbewerbsanalysen | Ein Pitch Deck + ein Gespräch mit dem Gründer | Ist-BMC rekonstruieren; offene Fragen als Innovationslücken-Hypothesen formulieren |
| **B – AUSRICHTEN** | JTBD-Surveys, Kundensupport-Daten, NPS-Scores, Marktforschung | Google Reviews, Social Media, ein paar Support-E-Mails | Job-Statements aus öffentlichen Quellen extrahieren; Opportunity-Map als Diskussionsgrundlage |
| **C – IDEIEREN** | Branchenreports, Patent-Datenbanken, Trend-Analysen, interne Ideenpools | Gründer-Vision + Wettbewerber-Websites | Cross-Domain-Analogien; Ideen-Longlist mit explizitem Unsicherheits-Label |
| **D – VALIDIEREN** | A/B-Tests, Kohortenanalysen, Conversion-Funnels | Landing Page + Google Forms | Einfache Experiment-Designs; qualitative Auswertung mit Signifikanz-Caveat |
| **E – KONTROLLIEREN** | KPI-Dashboards, Projekt-Retrospektiven, Finanzkennzahlen | Gründer-Reflexion + Notizen | Strukturierte Retrospektive; Learnings als explizites Wissen dokumentieren |

### 4.3 Das Degradation-Prinzip

> **Kernidee**: Das Framework **degradiert graceful** – es wird nicht nutzlos bei schlechter Datenlage, sondern passt seinen Output-Typ an.

- **Stufe 4**: Agents liefern *Empfehlungen mit Konfidenzwerten*
- **Stufe 3**: Agents liefern *Analysen mit Einschränkungen*
- **Stufe 2**: Agents liefern *Hypothesen und strukturierte Fragen*
- **Stufe 1**: Agents liefern *Denkanstöße und Frameworks zum Selbstausfüllen*

Der Agent kommuniziert **immer transparent**, auf welcher Datenbasis er arbeitet und wie belastbar seine Aussagen sind. Kein Halluzinieren von Sicherheit.

### 4.4 Forschungsbezug

Dieses Datenreifegrad-Modell adressiert eine reale Lücke: Bestehende Innovationsframeworks setzen implizit *strukturierte, verfügbare Daten* voraus. Die Startup-Realität zeigt aber:

- **72% der Startups** haben keine zentrale Datenstrategie (Quelle: zu validieren in Phase 2)
- Gründerwissen ist oft **tacit knowledge** (Nonaka & Takeuchi, 1995) – implizites Wissen, das nie dokumentiert wurde
- Die größte Stärke agentischer KI könnte genau hier liegen: **Implizites strukturieren, Fragmentiertes verbinden, Fehlendes durch externe Quellen ergänzen**

---

## 5. Schwachstellen & Lücken des Hybridansatzes

### Strukturelle Schwächen

| # | Schwachstelle | Beschreibung | Betroffene Phase | Schweregrad |
|---|--------------|-------------|-----------------|-------------|
| S1 | **Keine explizite Datenstrategie** | Der Hybrid sagt nicht, WELCHE Daten die Agents brauchen und WOHER sie kommen. Startups haben oft fragmentierte, unstrukturierte oder fehlende Daten. Ohne Datenstrategie laufen die Agents ins Leere. | Alle | HOCH |
| S2 | **Agent-Koordination ungeklärt** | Wie kommunizieren die Agents untereinander? Wer hat Entscheidungsautorität? Wie werden Konflikte zwischen Agent-Empfehlungen gelöst? Der Hybrid definiert Rollen, aber keine Governance. | Alle | HOCH |
| S3 | **Menschliche Rolle unterdefiniert** | Wo muss der Mensch zwingend entscheiden? Wo darf der Agent autonom handeln? Die Human-in-the-Loop-Grenze ist nicht gezogen. | Alle Gates | HOCH |
| S4 | **Startup-Ressourcenrealität ignoriert** | JTBD braucht umfangreiche Kundenforschung, BIG Picture braucht Strategie-Workshops, BMC braucht Marktdaten. Gerade ressourcenknappe Startups haben oft weder Zeit, Budget noch Personal dafür. Der Hybrid skaliert nicht nach unten. | B, C | MITTEL |
| S5 | **Zyklus-Trigger fehlt** | Wann wird der Zyklus neu gestartet? Nur nach Abschluss von Phase E? Was ist mit externen Schocks (Marktveränderung, neuer Wettbewerber)? Es fehlt ein Event-basierter Trigger-Mechanismus. | E → A | MITTEL |
| S6 | **Keine Innovationskultur-Dimension** | Alle Frameworks adressieren Prozesse, aber Innovationsblockaden sind oft ein Kulturproblem. Das Framework ignoriert organisationale Trägheit, Risikoaversion, Silo-Denken. | Querschnitt | MITTEL |
| S7 | **Feedback-Schleifen zwischen Phasen fehlen** | Der Zyklus läuft A→B→C→D→E→A. Aber was wenn Phase D zeigt, dass die Strategie aus Phase B falsch war? Es fehlen Rücksprungpfade zwischen nicht-benachbarten Phasen. | D → B, C → A | MITTEL |
| S8 | **Skalierbarkeit der Agent-Architektur** | Der Hybrid definiert ~15 spezialisierte Agents. Ist das realistisch? Wie verändert sich das Framework wenn man nur 3 Agents hat vs. 15? | Alle | NIEDRIG |
| S9 | **Messbarkeit des Framework-Erfolgs** | Wie messen wir, ob das Framework funktioniert? Welche KPIs zeigen, dass die agentische Unterstützung die Innovation tatsächlich verbessert hat? | E | MITTEL |
| S10 | **Kein Umgang mit Scheitern** | Was passiert, wenn der gesamte Zyklus keine verwertbare Innovation produziert? Kill-Kriterien auf Zyklusebene fehlen. | E | NIEDRIG |

### Konzeptionelle Lücken

| # | Lücke | Beschreibung | Potenzial |
|---|-------|-------------|-----------|
| L1 | **Daten-Layer** | ~~Eine eigene Schicht, die definiert: welche Daten, welche Qualität, welche Quellen, wie wird aufbereitet~~ **ADRESSIERT** → siehe Kapitel 4 (Datenreifegrad-Modell + Degradation-Prinzip) | EINGEARBEITET |
| L2 | **Agent-Governance-Modell** | ~~Wer orchestriert die Agents?~~ **ADRESSIERT** → siehe Kapitel 4 (Orchestrated Feedback Hierarchy + Sprecher-Mechanismus) | EINGEARBEITET |
| L3 | **Human-AI-Interaction-Protokoll** | ~~Wann entscheidet der Mensch, wann der Agent?~~ **ADRESSIERT** → siehe Kapitel 4.4 (Entscheidungsmatrix pro Situation) | EINGEARBEITET |
| L4 | **Adaptivitäts-Mechanismus** | Wie passt sich das Framework an den Kontext an? (Branche, Startup-Größe, Datenreife, Innovationsklasse) | Dein einzigartiger Beitrag |
| L5 | **Lern-Loop der Agents** | Wie lernen die Agents aus vergangenen Zyklen? Wie wird organisationales Wissen zu Agent-Wissen? | Dein einzigartiger Beitrag |
| L6 | **Ethik- & Bias-Dimension** | Wie verhindern wir, dass Agents bestimmte Innovationsrichtungen bevorzugen (z.B. nur inkrementell weil sicherer)? | Dein einzigartiger Beitrag |
| L7 | **Integrations-Layer** | Wie wird das Framework technisch in bestehende Startup-Tools eingebettet (CRM, Analytics, Projektmanagement)? | Praktischer Beitrag |

---

## 5. Nächste Schritte

**In Phase 1 (jetzt):**
- [ ] Lou priorisiert: Welche Lücken (L1-L7) werden gefüllt, welche bleiben als "Future Work"?
- [ ] Lou definiert die Human-AI-Grenze (L3) – das ist die philosophisch spannendste Frage
- [ ] Framework-Name finalisieren

**In Phase 2 (Execution):**
- [ ] Lücken füllen und ins Framework integrieren
- [ ] Prototyp des Agent-Systems bauen
- [ ] Framework an einem Szenario testen

---

*Letzte Aktualisierung: 27.03.2026 – L1, L2, L3 eingearbeitet*
