# Lou's Framework V3: Agentic Innovation Process (AIP)
## Vollständiges Konzeptionsrahmenwerk für Startups

> Ein universitäres Forschungsprojekt der HTWG Konstanz für die Optimierung von Innovationsprozessen in Startups durch agentische KI-Systeme – mit Fokus auf Unternehmen, die ungenutztes Innovationspotenzial erschließen wollen.

**Dokumentversion:** 3.0
**Datum:** 27. März 2026
**Status:** Konsolidierte Dokumentation (V1 + V2 Merge)
**Changelog V3:** OFH-Architektur aus V1 als Agent-Governance integriert; Dissens-als-Innovationssignal-Mechanismus hinzugefügt; V2-Layers L1-L7 vollständig übernommen und mit OFH harmonisiert.

---

## Inhaltsverzeichnis

1. [Grundlagen und Hybridansatz](#1-grundlagen-und-hybridansatz)
2. [Detaillierter Hybrid: Phasen & Agent-Mapping](#2-detaillierter-hybrid-phasen--agent-mapping)
3. [Gesamtbild: Der Zyklus](#3-gesamtbild-der-zyklus)
4. [Daten-Layer: Datenreifegradmodell (L1)](#4-daten-layer-datenreifegradmodell-l1)
5. [Agent-Governance: Orchestrated Feedback Hierarchy (L2)](#5-agent-governance-orchestrated-feedback-hierarchy-l2)
6. [Human-AI-Interaction-Protokoll (L3)](#6-human-ai-interaction-protokoll-l3)
7. [Adaptivitäts-Mechanismus (L4): Startup Genome & IT-Score](#7-adaptivitäts-mechanismus-l4-startup-genome--it-score)
8. [Lern-Loop der Agents (L5)](#8-lern-loop-der-agents-l5)
9. [Ethik- & Bias-Dimension (L6)](#9-ethik--bias-dimension-l6)
10. [Integrations-Layer (L7)](#10-integrations-layer-l7)
11. [Schwachstellen-Adressierung](#11-schwachstellen-adressierung)
12. [Change Management: Framework-Einführung](#12-change-management-framework-einführung)
13. [Framework at a Glance](#13-framework-at-a-glance)

---

## 1. Grundlagen und Hybridansatz

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
2. **Exploitation/Exploration-Audit** – Wo liegt der Fokus?
3. **Markt- & Technologie-Frühaufklärung** – Trends, Wettbewerber, technologische Entwicklungen
4. **Innovationslücke formulieren** – Gap zwischen Ist-Zustand und Marktpotenzial

**KI-Agents**:
- `audit-agent`: Analysiert Unternehmensdaten und erstellt BMC
- `market-scanner-agent`: Scannt Markttrends, Wettbewerber, Patente
- `gap-detector-agent`: Vergleicht Ist-BMC mit Marktdaten und identifiziert Lücken

**Gate A → B**: Innovationslücke validiert? Potenzialfelder identifiziert?

### Phase B: AUSRICHTEN (Wohin wollen wir innovieren?)

**Herkunft**: BIG Picture (Strategiefindung) + JTBD

**Ziel**: Aus der erkannten Lücke eine Innovationsstrategie mit konkreten Suchfeldern ableiten.

**Schritte**:
1. **Jobs-to-be-Done Analyse** – Welche „Jobs" haben Kunden, die unzureichend erfüllt werden?
2. **Opportunity Scoring** – Quantitative Bewertung: Importance × (1 - Satisfaction)
3. **Suchfeld-Definition** – Konkrete Innovationsrichtungen
4. **Innovationsklassen-Entscheidung** – Inkrementell, progressiv, radikal oder disruptiv?
5. **Ressourcen- & Zeitplanung** – Realistisches Scope

**KI-Agents**:
- `jtbd-extractor-agent`: Extrahiert Job-Statements aus Kundendaten
- `opportunity-scorer-agent`: Bewertet und rankt Opportunities quantitativ
- `strategy-synthesizer-agent`: Generiert Strategieoptionen

**Gate B → C**: Innovationsstrategie verabschiedet? Suchfelder definiert?

### Phase C: IDEIEREN (Wie könnten Lösungen aussehen?)

**Herkunft**: BIG Picture (Ideation) + Lean Startup (Hypothesenbildung)

**Ziel**: Aus den Suchfeldern konkrete Innovationsideen generieren und als testbare Hypothesen formulieren.

**Schritte**:
1. **Divergentes Ideieren** – Breite Ideengenerierung
2. **Cross-Domain-Inspiration** – Analogien aus anderen Branchen
3. **Ideen-Clustering & -Bewertung** – Gruppieren, priorisieren
4. **Hypothesenformulierung** – Jede Top-Idee als testbare Hypothese
5. **BMC-Entwurf** – Für jede Hypothese ein Soll-BMC skizzieren

**KI-Agents**:
- `ideation-agent`: Generiert Ideen basierend auf Suchfeldern
- `evaluation-agent`: Bewertet Ideen nach Kriterien (Impact, Feasibility, Fit)
- `hypothesis-agent`: Formuliert testbare Hypothesen mit Metriken

**Gate C → D**: Top-Hypothesen ausgewählt? Bewertungskriterien klar?

### Phase D: VALIDIEREN (Funktioniert es?)

**Herkunft**: Lean Startup (Build-Measure-Learn) + BIG Picture (Umsetzungspfade)

**Ziel**: Hypothesen durch schnelle Experimente testen und iterativ verfeinern.

**Schritte**:
1. **MVP definieren** – Minimales Experiment pro Hypothese
2. **Build** – MVP/Experiment umsetzen
3. **Measure** – Daten sammeln (Actionable Metrics)
4. **Learn** – Ergebnisse auswerten → Pivot, Persevere oder Kill
5. **Iterieren** – Loop wiederholen bis Validierung

**Pfade je Innovationsklasse** (aus BIG Picture):
- Inkrementell: Schnelle Umsetzung, wenige Loops (Stage-Gate Xpress)
- Progressiv: Moderate Validierung (Stage-Gate Lite)
- Radikal: Intensive Validierung, mehrere Pivots möglich (Full Stage-Gate)
- Disruptiv: Sonderprojekt mit eigener Governance

**KI-Agents**:
- `experiment-designer-agent`: Entwirft MVPs und Testsetups
- `analytics-agent`: Trackt Metriken, erkennt statistische Signifikanz
- `pivot-advisor-agent`: Analysiert Ergebnisse und empfiehlt Pivot/Persevere/Kill

**Gate D → E**: Hypothese validiert? Business Case tragfähig?

### Phase E: KONTROLLIEREN (Was haben wir gelernt?)

**Herkunft**: BIG Picture (Erfolgskontrolle + Lifecycle Management)

**Ziel**: Ergebnisse evaluieren, Learnings sichern, nächsten Zyklus vorbereiten.

**Schritte**:
1. **Zielerreichung prüfen** – Inhaltlich und organisatorisch
2. **Innovationsprojekte analysieren** – Was hat funktioniert, was nicht?
3. **Innovationssystem evaluieren** – Prozess selbst bewerten
4. **Learnings dokumentieren** – Für Organisation und für die KI-Agents
5. **Nächsten Zyklus initiieren** – Zurück zu Phase A mit neuem Wissen

**KI-Agents**:
- `retrospective-agent`: Strukturierte Analyse der Projektergebnisse
- `knowledge-agent`: Speichert Learnings (organisationales Gedächtnis)
- `cycle-initiator-agent`: Identifiziert nächste Innovationslücke

**Gate E → A**: Learnings dokumentiert? Nächster Zyklus definiert?

---

## 3. Gesamtbild: Der Zyklus

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

## 4. Daten-Layer: Datenreifegradmodell (L1)

> **Kern-Insight**: Das Framework muss mit **jeder Datenlage** funktionieren – mal besser, mal schlechter, aber nie gar nicht.

### 4.1 Datenreifegrad-Modell

| Stufe | Name | Typische Datenquellen | Agent-Modus | Ergebnis-Konfidenz |
|:-----:|------|----------------------|-------------|-------------------|
| **1** | **Minimal** | Gespräche, Notizen, Gründer-Wissen, vereinzelte Dokumente | Explorativer Modus: Agents stellen Fragen, strukturieren Implizites, generieren Hypothesen | Niedrig – eher Impulse als Analysen |
| **2** | **Fragmentiert** | CRM mit Lücken, Google Analytics, Social Media, unstrukturierte Dokumente | Aggregation & Mustererkennung: Agents sammeln, verknüpfen und finden Muster | Mittel – Muster erkennbar |
| **3** | **Strukturiert** | Sauberes CRM, Finanzdaten, Produkt-Analytics, dokumentierte Prozesse | Analyse-Modus: Agents führen quantitative Auswertungen durch | Hoch – belastbare Aussagen |
| **4** | **Datengetrieben** | Data Warehouse, BI-Tools, A/B-Test-Infrastruktur, API-Integrationen | Optimierungs-Modus: Agents arbeiten datengetrieben, können eigenständig testen | Sehr hoch – prädiktive Aussagen |

### 4.2 Datenquellen-Mapping pro Phase

| Phase | Ideale Daten | Minimaldaten (Stufe 1-2) | Was Agents daraus machen |
|-------|-------------|-------------------------|-------------------------|
| **A – ERKENNEN** | Finanzdaten, Marktdaten, Produkt-Metriken | Pitch Deck + Gründer-Gespräch | Ist-BMC rekonstruieren; Lücken-Hypothesen |
| **B – AUSRICHTEN** | JTBD-Surveys, Support-Daten, NPS | Google Reviews, Social Media, Support-E-Mails | Job-Statements extrahieren; Opportunity-Map |
| **C – IDEIEREN** | Branchenreports, Patent-Datenbanken, Trend-Analysen | Gründer-Vision + Wettbewerber-Websites | Cross-Domain-Analogien; Ideen-Longlist |
| **D – VALIDIEREN** | A/B-Tests, Kohortenanalysen, Funnels | Landing Page + Google Forms | Experiment-Designs; qualitative Auswertung |
| **E – KONTROLLIEREN** | KPI-Dashboards, Retrospektiven, Finanzkennzahlen | Gründer-Reflexion + Notizen | Strukturierte Retrospektive; Learnings |

### 4.3 Das Degradation-Prinzip

> **Kernidee**: Das Framework **degradiert graceful** – es wird nicht nutzlos bei schlechter Datenlage, sondern passt seinen Output-Typ an.

- **Stufe 4**: Agents liefern *Empfehlungen mit Konfidenzwerten*
- **Stufe 3**: Agents liefern *Analysen mit Einschränkungen*
- **Stufe 2**: Agents liefern *Hypothesen und strukturierte Fragen*
- **Stufe 1**: Agents liefern *Denkanstöße und Frameworks zum Selbstausfüllen*

Der Agent kommuniziert **immer transparent**, auf welcher Datenbasis er arbeitet und wie belastbar seine Aussagen sind.

### 4.4 Forschungsbezug

Bestehende Innovationsframeworks setzen implizit *strukturierte, verfügbare Daten* voraus. Die Startup-Realität zeigt aber:

- Gründerwissen ist oft **tacit knowledge** (Nonaka & Takeuchi, 1995) – implizites Wissen, das nie dokumentiert wurde
- Die größte Stärke agentischer KI könnte genau hier liegen: **Implizites strukturieren, Fragmentiertes verbinden, Fehlendes durch externe Quellen ergänzen**

---

## 5. Agent-Governance: Orchestrated Feedback Hierarchy (L2)

> **Kern-Insight**: Weder reine Hierarchie noch reiner Schwarm. Die Agents brauchen einen Orchestrator für Struktur, aber demokratisches Feedback für Qualität – und den Menschen als letzte Instanz an strategischen Entscheidungspunkten.

### 5.1 Das Architekturmodell: "Orchestrated Feedback Hierarchy" (OFH)

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
        │Spezialist ││Spezialist ││Spezialist │
        │    A1     ││    A2     ││    A3     │
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

### 5.2 Die vier Rollen im Detail

#### Mensch (Gründer / Innovationsteam)
- **Wann aktiv**: An jedem Gate (A→B, B→C, C→D, D→E, E→A) + bei Eskalation
- **Entscheidungsgewalt**: Strategische Richtung, Go/Kill, Ressourcenfreigabe, ethische Fragen
- **Interaktion**: Spricht primär mit dem Orchestrator, nie direkt mit Spezialisten
- **Kann jederzeit**: Eingreifen, Richtung ändern, Prozess pausieren

#### Orchestrator-Agent
- **Rolle**: Zentrale Steuerungsinstanz. Verteilt Aufgaben, sammelt Ergebnisse, bereitet Gate-Entscheidungen vor
- **Entscheidungsgewalt**: Operative Entscheidungen innerhalb einer Phase (z.B. welche Datenquelle zuerst, welche Analyse-Methode)
- **Eskaliert an Mensch wenn**: Unaufgelöster Dissens der Spezialisten; unerwartete Erkenntnisse; Ressourcenbedarf über Budget; ethische Graubereiche; Konfidenz < 40%
- **Kernfähigkeit**: Kontext halten – kennt die Gesamtstrategie und ordnet Einzelergebnisse ein
- **Überlebt alle Phasen**: Kein Kontextverlust zwischen A→B→C→D→E

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

### 5.3 Der Feedback-Loop im Detail

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
│  4. Konsens oder Dissens    │
│     formulieren             │
└──────────────┬──────────────┘
               ▼
     Sprecher → Orchestrator
               │
               ▼
    ┌──────────────────────┐
    │ Orchestrator          │
    │ evaluiert:            │
    │                       │
    │ Konsens? ────YES────▶ Gate vorbereiten → Mensch
    │    │                  │
    │   NO (Dissens)        │
    │    │                  │
    │    ▼                  │
    │ Auflösbar? ──YES───▶ Neue Anweisungen
    │    │                  │ an Spezialisten
    │   NO                  │
    │    │                  │
    │    ▼                  │
    │ DISSENS-SIGNAL ─────▶ Eskalation an Mensch
    │ (Innovationschance!)  │ mit Dissens-Report
    └──────────────────────┘
```

### 5.4 Dissens als Innovationssignal

> **Kern-Insight**: Wenn Spezialisten fundamental widersprechen und keiner nachgibt, ist der Dissens selbst ein wertvolles Signal. Genau dort, wo Widersprüche unlösbar erscheinen, liegt oft die echte Innovationschance.

**Das Prinzip**: Nicht jeder Dissens ist ein Problem. Manche Dissense sind die wertvollsten Outputs des gesamten Systems.

**Dissens-Klassifizierung durch den Orchestrator**:

| Dissens-Typ | Beschreibung | Aktion |
|-------------|-------------|--------|
| **Datendissens** | Spezialisten widersprechen wegen unterschiedlicher Datengrundlage | Auflösbar: Orchestrator fordert einheitliche Datenbasis |
| **Methodendissens** | Spezialisten widersprechen über die richtige Analysemethode | Auflösbar: Orchestrator entscheidet oder lässt beide Methoden laufen |
| **Bewertungsdissens** | Spezialisten bewerten dasselbe Ergebnis fundamental anders | **Innovationssignal**: Hier prallen verschiedene Perspektiven aufeinander → an Mensch eskalieren |
| **Richtungsdissens** | Spezialisten empfehlen fundamental verschiedene strategische Richtungen | **Innovationssignal**: Hier liegt möglicherweise eine nicht-offensichtliche Chance → an Mensch eskalieren |

**Dissens-Report an den Menschen**:
```
DISSENS-REPORT (Innovationssignal)
──────────────────────────────────
Phase: [aktuelle Phase]
Beteiligte Spezialisten: [Agent A, Agent B]

POSITION A:
  Agent: [Name]
  Empfehlung: [Was]
  Begründung: [Warum]
  Konfidenz: [X%]
  Datengrundlage: [Welche Daten]

POSITION B:
  Agent: [Name]
  Empfehlung: [Was]
  Begründung: [Warum]
  Konfidenz: [X%]
  Datengrundlage: [Welche Daten]

DISSENS-KERN:
  [Worin genau besteht der Widerspruch?]

WARUM DIES EIN INNOVATIONSSIGNAL SEIN KÖNNTE:
  [Orchestrator-Analyse: Was sagt dieser Widerspruch über
   unentdeckte Möglichkeiten, blinde Flecken oder
   nicht-offensichtliche Marktdynamiken aus?]

OPTIONEN FÜR DEN MENSCHEN:
  1. Position A folgen
  2. Position B folgen
  3. Beide Richtungen parallel als Hypothesen verfolgen
  4. Den Dissens selbst als neues Suchfeld für Phase C nutzen
```

**Wissenschaftliche Einordnung**:
- Der Dissens-Mechanismus ist inspiriert von der **Delphi-Methode** (Dalkey & Helmer, 1963), die kontrollierte Debatte zur Entscheidungsfindung nutzt
- Das Konzept, dass Widersprüche Innovationsquellen sind, findet sich in der **dialektischen Innovationstheorie** und in Christensens Beobachtung, dass disruptive Innovationen oft dort entstehen, wo Experten sich nicht einig sind
- Das Prinzip der **konstruktiven Kontroverse** (Johnson & Johnson, 2009) zeigt, dass Gruppen mit explizitem Dissens zu besseren Entscheidungen kommen als Gruppen mit erzwungenem Konsens

### 5.5 Eskalationslogik zu Menschen

**Automatische Eskalation-Trigger**:
- Hohe Unsicherheit (Konfidenz < 40%)
- Widersprechende Agent-Empfehlungen (Confidence Gap > 20 Punkte)
- Dissens-Signal identifiziert (Bewertungs- oder Richtungsdissens)
- Gate-Entscheidung (immer Mensch)
- Strategische Pivots (immer Mensch)
- Ressourcen-Allokation > 10% des Budgets (immer Mensch)
- Ethische Bedenken identifiziert (immer Mensch)

**Eskalations-Format**:
```
ESCALATION REPORT
─────────────────
Agent: [Name]
Trigger: [Grund]
Situation: [Kontext, 2-3 Sätze]
Agent-Empfehlung: [Option A mit X% Konfidenz]
Gegenargument: [Von Agent B mit Y% Konfidenz]
Menschliche Entscheidung erforderlich bis: [Datum]
Konsequenzen bei Verzögerung: [Falls zutreffend]
```

### 5.6 Warum dieses Modell?

**Gegenüber reiner Hierarchie (Orchestrator allein)**:
- Der Feedback-Loop verhindert, dass der Orchestrator zum Bottleneck wird
- Spezialisten können Fehler des Orchestrators korrigieren (kein Single Point of Failure)
- Emergente Erkenntnisse aus der Spezialisten-Diskussion, die ein Top-Down-System verpassen würde
- **Dissens wird produktiv genutzt statt unterdrückt**

**Gegenüber reinem Schwarm**:
- Klare Verantwortlichkeit – der Orchestrator hält den Kontext
- Der Mensch hat einen einzigen Ansprechpartner, nicht ein Chaos aus Agents
- Ergebnisse sind nachvollziehbar und auditierbar

**Gegenüber Phasen-Agents (V2-Modell)**:
- Kein Kontextverlust zwischen Phasen – der Orchestrator überlebt alle Phasen
- Spezialisten können phasenübergreifend wiederverwendet werden
- Der Sprecher-Mechanismus ist demokratischer als ein fest zugewiesener Phase-Manager

**Wissenschaftliche Einordnung**:
- Verbindet Prinzipien aus Multi-Agent-Systemen (MAS) mit organisationstheoretischen Konzepten
- Der Sprecher-Mechanismus ist inspiriert von demokratischer Entscheidungstheorie und Delphi-Methode
- Die Eskalationslogik folgt dem Prinzip der Subsidiarität: Entscheidungen werden auf der niedrigstmöglichen Ebene getroffen

---

## 6. Human-AI-Interaction-Protokoll (L3)

### 6.1 Levels of Autonomy nach Parasuraman et al. (2000)

Das Framework adaptiert die klassische Taxonomie von Parasuraman, Sheridan & Wickens auf die fünf Phasen des Innovationsprozesses:

**Vier generische Funktionen in jedem Phasenschritt**:
1. **Informationsakquisition** (Datensammlung)
2. **Informationsanalyse** (Interpretation)
3. **Entscheidungs- und Aktionswahl** (Was soll getan werden?)
4. **Aktionsimplementierung** (Durchführung)

### 6.2 Autonomie-Levels pro Phase

#### Phase A: ERKENNEN

| Funktion | Level 1 (Manual) | Level 3 (Hybrid) | Level 5 (AI) |
|----------|-----------------|-----------------|------------|
| **Info-Akquisition** | Gründer sammelt Daten manuell | Audit-Agent sammelt, Gründer validiert | Agent sammelt autonom aus APIs |
| **Info-Analyse** | Gründer interpretiert | Agent interpretiert, Gründer sieht Ergebnisse | Agent interpretiert und präsentiert |
| **Entscheidung** | Gründer definiert Lücke | Agent empfiehlt Lücken, Gründer validiert | Agent definiert Lücken, Gründer bestätigt |
| **Aktion** | Gründer dokumentiert | Agent dokumentiert, Gründer genehmigt | Agent dokumentiert, Gründer informed |

**Empfohlenes Default-Level**: **Level 3 (Hybrid)** – Agent sammelt und analysiert, Gründer validiert und entscheidet

#### Phase B: AUSRICHTEN

| Funktion | Level 1 | Level 3 | Level 5 |
|----------|---------|---------|---------|
| **Info-Akquisition** | Manuelle Kundenforschung | JTBD-Agent sammelt Daten aus Reviews + Support | Agent autonome Sammlung + Synthese |
| **Info-Analyse** | Gründer wertet aus | Agent identifiziert Jobs, Gründer verifiziert | Agent generiert komplette Opportunity-Map |
| **Entscheidung** | Gründer wählt Strategie | Strategy-Agent schlägt vor, Gründer wählt | Agent definiert Strategie, Gründer bestätigt |
| **Aktion** | Manuelle Strategie-Dokumente | Agent generiert, Gründer überprüft | Agent generiert autonom |

**Empfohlenes Default-Level**: **Level 3-4**

#### Phase C: IDEIEREN

| Funktion | Level 1 | Level 3 | Level 5 |
|----------|---------|---------|---------|
| **Info-Akquisition** | Brainstorming Sessions | Agent generiert Ideen aus Suchfeldern | Agent generiert Ideen autonom kontinuierlich |
| **Info-Analyse** | Manuelle Bewertung | Evaluation-Agent bewertet, Gründer priorisiert | Agent bewertet und priorisiert autonom |
| **Entscheidung** | Gründer wählt Top-Ideen | Agent empfiehlt Top-3, Gründer wählt | Agent führt aus, Gründer informed |
| **Aktion** | Manuelle Hypothesen-Formulierung | Hypothesis-Agent formuliert, Gründer validiert | Agent formuliert autonom |

**Empfohlenes Default-Level**: **Level 3-4**

#### Phase D: VALIDIEREN

| Funktion | Level 1 | Level 3 | Level 5 |
|----------|---------|---------|---------|
| **Info-Akquisition** | Manuelle Test-Durchführung | Experiment-Designer plant, Gründer führt durch | Agent führt MVPs autonom durch |
| **Info-Analyse** | Manuelle Datenanalyse | Analytics-Agent trackt, Gründer interpretiert | Agent interpretiert kontinuierlich |
| **Entscheidung** | Gründer entscheidet Pivot/Persevere | Pivot-Advisor empfiehlt, Gründer entscheidet | Agent empfiehlt, Gründer validiert |
| **Aktion** | Manuelle Umsetzung | Agent implementiert Pivot, Gründer genehmigt | Agent implementiert autonom |

**Empfohlenes Default-Level**: **Level 4** – Agent führt aus und empfiehlt, Gründer genehmigt bei Pivots

#### Phase E: KONTROLLIEREN

| Funktion | Level 1 | Level 3 | Level 5 |
|----------|---------|---------|---------|
| **Info-Akquisition** | Retrospektive-Workshop | Retrospective-Agent sammelt Daten | Agent sammelt autonom kontinuierlich |
| **Info-Analyse** | Gründer analysiert | Agent analysiert, Gründer bewertet | Agent analysiert und identifiziert Muster |
| **Entscheidung** | Gründer zieht Learnings | Agent schlägt vor, Gründer validiert | Agent schlägt vor, Gründer genehmigt |
| **Aktion** | Manuelle Dokumentation | Knowledge-Agent dokumentiert, Gründer reviewed | Agent dokumentiert autonom |

**Empfohlenes Default-Level**: **Level 3**

### 6.3 Entscheidungsmatrix: Wer entscheidet wann?

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
| Dissens-Signal auswerten | **Mensch** | Innovationschance erkennen |
| Ethische Graubereiche | Immer **Mensch** | Nicht delegierbar |

### 6.4 Transparenzanforderungen

Das Framework verpflichtet den Agent, auf Anfrage oder proaktiv zu offenbaren:

- **Was**: Welche Entscheidung / Empfehlung
- **Warum**: Welche Daten und Logik führten dazu
- **Wie sicher**: Konfidenzwert (0-100%)
- **Wann**: Zeitstempel und Kontext
- **Wer**: Welcher Agent oder Agent-Team traf die Entscheidung
- **Wo sind die Grenzen**: Welche Unsicherheiten oder Annahmen

### 6.5 Trust Calibration Mechanismen

**1. Confidence Transparency**:
- Agent gibt immer Konfidenzwert an
- Unter 60% = Agent fordert menschliche Validierung an
- 60-80% = Agent empfiehlt, Mensch entscheidet
- Über 80% = Agent kann implementieren mit Notification

**2. Uncertainty Recognition**:
- Agent benennt explizit Unsicherheitsquellen

**3. Drift Detection**:
- Agent monitort, ob seine Empfehlungen noch aktuell sind
- Bei signifikantem Drift (>15% Abweichung) selbst eskalieren

**4. Feedback Loops**:
- Mensch gibt Feedback zu Agent-Empfehlungen
- Agent nutzt Feedback zur kontinuierlichen Verbesserung

---

## 7. Adaptivitäts-Mechanismus (L4): Startup Genome & IT-Score

### 7.1 Das Problem mit generischen Konfigurationen

Bestehende Frameworks konfigurieren sich nach Schablone: klein/mittel/groß, Branche A/B/C. Das ignoriert, dass jedes Startup einzigartig ist. Ein 5-Personen-SaaS-Startup mit brillanten Gründern und schlechter Technologie braucht eine völlig andere Konfiguration als ein 5-Personen-SaaS-Startup mit mittelmäßigen Gründern und exzellenter Technologie.

**Lou's Ansatz: Jedes Startup bekommt ein individuelles Profil — sein "Genome" — und das Framework konfiguriert sich danach.**

### 7.2 Das Startup Genome

Der Audit-Agent erstellt in **Phase A** das Startup Genome: ein strukturiertes Profil über sechs Dimensionen, das die DNA des Unternehmens erfasst.

#### Die sechs Genome-Dimensionen

| Dimension | Was wird bewertet | Datenquellen | Skala |
|-----------|------------------|-------------|-------|
| **Struktur** | Corporate-Reife: Prozesse, Hierarchien, Rollenklarheit, Entscheidungswege | Organigramm, Prozessdoku, Gründer-Interview | 1-10 |
| **Kultur** | Innovationsbereitschaft, Risikoappetit, Fehlerkultur, Experimentierfreude | Team-Befragung, Meeting-Kultur, Entscheidungshistorie | 1-10 |
| **Gründer** | Persönlichkeit, Fähigkeiten, Erfahrung, Belastbarkeit, Lernbereitschaft | Gründer-Interview, Track Record, Selbsteinschätzung | 1-10 |
| **Technologie** | Tech-Stack-Reife, Dateninfrastruktur, Automatisierungsgrad, Skalierbarkeit | Code-Audit, Stack-Analyse, Infrastruktur-Review | 1-10 |
| **Marktbild** | Public Perception, Brand-Stärke, Kundenzufriedenheit, Wettbewerbsposition | Reviews, NPS, Social Media Sentiment, Marktanteil | 1-10 |
| **Datenreife** | Verfügbarkeit, Qualität und Strukturierung der Unternehmensdaten | Datenquellen-Inventar, Qualitäts-Assessment | 1-10 (→ mappt auf L1 Stufe 1-4) |

#### Genome-Erstellung

```
STARTUP GENOME — [Firmenname]          Erstellt: Phase A, Zyklus N
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Struktur:     ██████░░░░  6/10   Prozesse vorhanden, aber informell
Kultur:       ████████░░  8/10   Hohe Experimentierfreude
Gründer:      █████████░  9/10   Technisch stark, strategisch erfahren
Technologie:  ████░░░░░░  4/10   Legacy-Stack, wenig Automatisierung
Marktbild:    ███████░░░  7/10   Gute Reviews, schwache Brand
Datenreife:   ███░░░░░░░  3/10   Fragmentierte Daten (→ L1 Stufe 2)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IT-SCORE:     6.2/10  →  "Mittleres Innovationspotenzial"
SCHWÄCHSTE:   Technologie (4/10) → primärer Hebel
STÄRKSTE:     Gründer (9/10) → größtes Asset
```

Der Audit-Agent erhebt die Daten durch eine Kombination aus:
- **Automatisiert**: Technologie (Code-Analyse), Marktbild (Sentiment-Analyse), Datenreife (Quellen-Scan)
- **Semi-automatisiert**: Struktur (Dokument-Analyse + Gründer-Validierung)
- **Manuell**: Kultur (Team-Gespräche), Gründer (Selbst- + Fremdeinschätzung)

### 7.3 Der Innovations-Treiber-Score (IT-Score)

Der **IT-Score** ist die zentrale Kennzahl des Frameworks: Er bewertet, wie gut ein Startup positioniert ist, um Innovation zu treiben — und wo die größten Hebel liegen.

#### Berechnung

Der IT-Score ist der **gewichtete Durchschnitt** der sechs Genome-Dimensionen:

```
IT-Score = (Struktur × w₁ + Kultur × w₂ + Gründer × w₃
          + Technologie × w₄ + Marktbild × w₅ + Datenreife × w₆) / Σw
```

**Default-Gewichtung** (anpassbar pro Branche und Innovationsklasse):

| Dimension | Gewicht | Begründung |
|-----------|---------|------------|
| Kultur | 0.20 | Stärkster Prädiktor für Innovationsfähigkeit |
| Gründer | 0.20 | Entscheidend für Richtung und Durchhaltevermögen |
| Technologie | 0.18 | Enabler für Skalierung und Datennutzung |
| Datenreife | 0.17 | Bestimmt Framework-Modus (L1) |
| Struktur | 0.13 | Wichtig, aber bei Startups oft bewusst flach |
| Marktbild | 0.12 | Relevant, aber eher Outcome als Treiber |

#### Interpretation

| IT-Score | Bewertung | Framework-Empfehlung |
|----------|-----------|---------------------|
| **8-10** | Hohes Innovationspotenzial | Vollständiger AIP-Zyklus, höhere Agent-Autonomie (Level 3-4) |
| **5-7** | Mittleres Innovationspotenzial | AIP-Zyklus mit Fokus auf schwächste Dimension; Guided Mode für Schwachstellen |
| **3-5** | Niedriges Innovationspotenzial | Reduzierter Zyklus: Erst Grundlagen stärken (Struktur, Daten), dann innovieren |
| **1-3** | Kritisch | Framework empfiehlt: Erst Fundament bauen; Innovation ohne Basis ist Aktionismus |

#### Der Hebel-Mechanismus

**Kernidee**: Das Framework fokussiert automatisch auf die **schwächste Genome-Dimension**, weil dort der größte Marginalnutzen liegt.

- IT-Score 6.2 mit Technologie als Schwachstelle (4/10) → Framework priorisiert in Phase B technologienahe Innovationssuchfelder
- IT-Score 6.2 mit Kultur als Schwachstelle (4/10) → Framework empfiehlt erst Kultur-Interventionen, bevor radikale Innovation versucht wird
- Wenn zwei Dimensionen gleich schwach sind → Gründer entscheidet Priorität (Gate A→B)

### 7.4 Genome-Evolution über Zyklen

Das Genome ist kein statisches Profil — es **evoliert** über Innovationszyklen:

```
Zyklus 1:  Technologie 4/10 → IT-Score 6.2
           Framework-Fokus: Tech-Stack modernisieren

Zyklus 2:  Technologie 6/10 (verbessert!) → IT-Score 7.0
           Neue Schwachstelle: Datenreife (3/10)
           Framework-Fokus: Dateninfrastruktur aufbauen

Zyklus 3:  Datenreife 5/10, Technologie 7/10 → IT-Score 7.8
           Framework: "Startup bereit für radikale Innovation"
```

**Trigger für Genome-Update**:
- Nach jedem abgeschlossenen Zyklus (Phase E → Retrospective-Agent aktualisiert Genome)
- Bei signifikanten externen Ereignissen (Funding-Runde, Team-Wachstum, Pivot)
- Gründer kann manuelles Update anfordern

### 7.5 Framework-Konfiguration aus dem Genome

Statt generischer Schablonen konfiguriert sich das Framework **individuell** aus dem Genome:

| Genome-Ergebnis | Agent-Konfiguration | Autonomie | Modus |
|----------------|-------------------|-----------|-------|
| Gründer stark, Technologie schwach | Fokus auf Tech-Scouting-Agents, Audit-Agent prüft Stack | Level 3 | Partnership |
| Kultur stark, Struktur schwach | Agents unterstützen Prozess-Design, weniger Ideation | Level 2-3 | Guided |
| Alles > 7/10 | Vollständiges 15-Agent-Team, hohe Autonomie | Level 3-4 | Delegated |
| Datenreife < 3/10 | Nur 3 Core Agents, Explorativer Modus, Graceful Degradation | Level 1-2 | Guided |

### 7.6 Vergleichbarkeit: Benchmarking gegen Peers

Der IT-Score gewinnt an Aussagekraft durch **Vergleich mit ähnlichen Startups**:

- **Branche**: SaaS-Startups im selben Markt
- **Phase**: Vergleich mit Startups in gleicher Wachstumsphase (Pre-Seed, Seed, Series A)
- **Region**: Lokale vs. globale Benchmarks

```
Dein IT-Score:     6.2/10
Branchendurchschnitt: 5.8/10  → Du liegst über dem Schnitt
Top-Quartil:       7.5/10  → Aufholpotenzial: +1.3 Punkte
Größter Gap:       Technologie (du: 4, Branche: 6.5)
```

**Datenquelle für Benchmarks**: Aggregierte, anonymisierte Genome-Daten aus vorherigen AIP-Zyklen anderer Startups. In der Frühphase (wenige Clients) → Branchenreports und öffentliche Daten als Proxy.

---

## 8. Lern-Loop der Agents (L5)

### 8.1 SECI-Modell (Nonaka & Takeuchi) angewendet auf Agenten

#### 1. Socialization (Wissenstausch Mensch-zu-Agent)
Agenten lernen **tacit knowledge** von Menschen durch:
- **Gründer-Interviews**: Retrospective-Agent erfasst implizites Erfahrungswissen
- **Observation von Entscheidungen**: Knowledge-Agent beobachtet Entscheidungsheuristiken
- **Feedback-Loops**: Gründer dokumentiert „Was ich wirklich gemeint habe" vs. „Was der Agent verstanden hat"

#### 2. Externalization (Wissen aus Daten extrahieren)
Agenten wandeln **unstrukturierte Daten** in strukturiertes Wissen um:
- **Data Mining**: Analytics-Agent extrahiert Muster
- **Pattern Recognition**: Gap-Detector-Agent identifiziert wiederkehrende Lücken
- **Synthesis**: Knowledge-Agent kombiniert externe mit internen Daten

#### 3. Combination (Synthese zu neuen Konzepten)
- **Cross-Phase Learning**: Warum waren Ideen aus Zyklus N in N+1 nicht mehr gut?
- **Meta-Learning**: Agents erkennen: „Bei diesem Gründer-Typ funktioniert Strategie A besser als B"
- **Framework-Optimization**: Orchestrator passt Phasen-Sequenzen an

#### 4. Internalization (Einbau in Agent-Verhalten)
- **Next-Cycle Improvements**: Verbessertes Agent-Verhalten basierend auf vorherigem Zyklus
- **Confidence Adjustments**: Agent passt Konfidenzwerte an
- **Personalized Prompts**: Agent generiert Prompts spezifisch für diesen Gründer

### 8.2 Single-Loop vs. Double-Loop Learning (Argyris & Schön)

**Single-Loop** (Fehlerkorrektur): Agent beobachtet Fehler und korrigiert Verhalten.
- Beispiel: Pivot-Advisor sammelt nächstes Mal proaktiv Customer-Feedback

**Double-Loop** (Grundannahmen hinterfragen): Agent erkennt, dass seine Grundannahme falsch war.
- Beispiel: Opportunity-Scorer lernt, dass „mehr Margin ≠ besser" – Feasibility muss gewichtet werden

### 8.3 Memory-Architektur

| Tier | Was | Wie lange | Beispiel |
|------|-----|-----------|---------|
| **1: Working Memory** | Aktuelle Phasen-Daten | Aktueller Zyklus | Alle bewerteten Ideen |
| **2: Episodic Memory** | Wichtige Entscheidungen, Learnings, Outcomes | 3 Zyklen (6-12 Monate) | "Zyklus 1: Pivot A war erfolgreich" |
| **3: Semantic Memory** | Verallgemeinerte Muster, Meta-Wissen | Unbegrenzt | "Radikale Innovation funktioniert hier besser" |
| **4: Procedural Memory** | Wie man Aufgaben besser macht | Unbegrenzt | "Beste Frage für tacit knowledge: ..." |

### 8.4 Cross-Cycle Learning

**Expliziter Wissenstransfer-Protokoll**:
1. **Phase E**: Knowledge-Agent erstellt "Cycle N Learnings Report"
2. **Phase A von Zyklus N+1**: Gap-Detector liest Report, passt Suchfelder an
3. **Kontinuierlich**: Alle Agenten haben Zugriff auf aggregierte Learnings

### 8.5 Second Brain: Persistente Wissensbasis

#### Das Problem mit reinem LLM-Memory

LLM-basierte Agents haben kein echtes Langzeitgedächtnis. Context Windows sind begrenzt, und jeder neue API-Call "vergisst" den vorherigen. Für ein Framework, das über **mehrere Innovationszyklen** hinweg lernen soll, ist das unzureichend.

#### Lösung: Obsidian als Second Brain

Das Framework nutzt einen **strukturierten Knowledge Vault** (z.B. Obsidian) als persistente Wissensbasis — das "Second Brain" des Agent-Systems:

```
📁 AIP-Brain/
├── 📁 Genome/
│   ├── genome-v1.md          ← Startup Genome aus Zyklus 1
│   ├── genome-v2.md          ← Aktualisiertes Genome
│   └── genome-evolution.md   ← Veränderungen über Zeit
├── 📁 Zyklen/
│   ├── zyklus-01/
│   │   ├── phase-a-audit.md
│   │   ├── phase-b-strategie.md
│   │   ├── phase-c-ideen.md
│   │   ├── phase-d-tests.md
│   │   └── phase-e-learnings.md
│   └── zyklus-02/
├── 📁 Patterns/
│   ├── was-funktioniert.md    ← Bestätigte Muster
│   ├── was-scheitert.md       ← Anti-Patterns
│   └── dissens-log.md         ← Alle Dissens-Signale + Outcomes
├── 📁 Markt/
│   ├── wettbewerber.md
│   ├── trends.md
│   └── kundenfeedback.md
└── 📁 Meta/
    ├── agent-performance.md   ← Welcher Agent liefert am besten?
    └── framework-anpassungen.md
```

#### Wie Agents das Second Brain nutzen

| Operation | Wann | Wer | Token-Kosten |
|-----------|------|-----|-------------|
| **Lesen** | Vor jeder Phase: Agent liest relevante Notizen | Alle Agents | Minimal (nur relevante Dateien) |
| **Schreiben** | Nach jeder Phase: Ergebnisse + Learnings ablegen | Knowledge-Agent | Keine LLM-Kosten (File I/O) |
| **Verlinken** | Querverweise zwischen Erkenntnissen (Obsidian-Links) | Knowledge-Agent | Keine LLM-Kosten |
| **Suchen** | Bei Bedarf: Semantische Suche über alle Zyklen | Orchestrator | 1 LLM-Call (Embedding) |

**Vorteil**: Agents brauchen nicht den gesamten Kontext im Context Window. Sie lesen gezielt die 2-3 relevanten Notizen → drastisch reduzierte Token-Kosten bei besserem Langzeitgedächtnis.

#### Zwei-Schichten-Architektur: Client-Vault & Pattern-Pool

Das Second Brain existiert auf zwei strikt getrennten Ebenen:

```
┌─────────────────────────────────────────────────────────────┐
│  SCHICHT 1: Client-Vault (privat, isoliert)                 │
│                                                             │
│  • Alle Rohdaten, Genome, Strategien, Empfehlungen          │
│  • Verlässt NIEMALS den Client-Kontext                      │
│  • Gehört dem Startup — volle Datenhoheit                   │
│  • Bei Vertragsende: Export oder Löschung                   │
│                                                             │
│  Inhalt: Genome-Versionen, Phasen-Ergebnisse,              │
│  Gate-Entscheidungen, Dissens-Logs, Agent-Traces            │
└──────────────────────────┬──────────────────────────────────┘
                           │
                   Anonymisierung &
                   Abstraktion (One-Way)
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  SCHICHT 2: Pattern-Pool (anonymisiert, aggregiert)         │
│                                                             │
│  • Nur abstrahierte Muster — keine Rohdaten                 │
│  • Kein Rückschluss auf einzelne Clients möglich            │
│  • Verbessert das Framework für ALLE zukünftigen Clients    │
│                                                             │
│  Beispiel-Patterns:                                         │
│  → "SaaS-Startups mit Technologie < 4/10 profitieren       │
│     am meisten von Phase-B-Fokus auf Tech-Scouting"         │
│  → "Bei Datenreife Stufe 2 liefert Adversarial Learning     │
│     in 70% der Fälle bessere Gate-Entscheidungen"           │
│  → "Ethical Friction wurde in 12% der Fälle getriggert;     │
│     in 40% davon änderte der Gründer seine Entscheidung"    │
└─────────────────────────────────────────────────────────────┘
```

#### Datenschutz-Regeln für den Pattern-Pool

| Regel | Umsetzung |
|-------|-----------|
| **Keine Firmennamen** | Patterns referenzieren nur Archetypen ("SaaS-Startup, Series A, 12 MA") |
| **Keine Strategien** | Kein "Firma X hat zu Abo-Modell gewechselt", nur "Pivot-Typ B war in 65% erfolgreich" |
| **Keine Finanzdaten** | Nur Kategorien ("Umsatz < 1M ARR"), keine konkreten Zahlen |
| **Keine Genome-Rohdaten** | Nur Dimensionen-Ranges ("Kultur 7-9, Technologie 3-5"), keine vollständigen Profile |
| **Opt-in** | Client entscheidet, ob seine abstrahierten Patterns in den Pool fließen |
| **Mindest-Aggregation** | Ein Pattern wird erst sichtbar, wenn es aus ≥5 verschiedenen Clients stammt |
| **Kein Reverse Engineering** | Patterns werden so abstrahiert, dass kein Rückschluss auf einzelne Clients möglich ist |

#### Was der Pattern-Pool verbessert

Mit jedem Client wird das Framework in drei Bereichen besser:

1. **IT-Score Kalibrierung**: Gewichtungen (w₁-w₆) werden empirisch validiert — welche Dimension korreliert tatsächlich mit Innovationserfolg?
2. **Branchen-Benchmarks**: Der Peer-Vergleich (Kap. 7.6) wird mit echten Daten gefüttert statt Proxies
3. **Agent-Performanz**: Welche Agent-Konfigurationen liefern die besten Ergebnisse bei welchem Genome-Profil?

**Das Ergebnis**: Ein Framework, das **mit jedem Einsatz klüger wird** — ohne die Vertraulichkeit einzelner Clients zu verletzen. Die Datenschutz-Architektur macht Cross-Client Learning möglich, ohne Vertrauen zu riskieren.

### 8.6 Adversarial Learning: Der provozierte Dissens

#### Vom passiven zum aktiven Dissens

Das Dissens-als-Innovationssignal (Kap. 5.4) erkennt **zufällig auftretende** Widersprüche zwischen Agents. Adversarial Learning geht einen Schritt weiter: Es **provoziert** Dissens systematisch.

#### Der Devil's Advocate Protokoll

In definierten Momenten wird ein Agent beauftragt, die **Gegenposition** zur Mehrheitsmeinung einzunehmen:

**Wann wird Adversarial Learning aktiviert?**
- Nach jeder Gate-Entscheidung (bevor der Mensch entscheidet)
- Bei strategisch kritischen Empfehlungen (Pivot, Kill, neue Innovationsklasse)
- Wenn der IT-Score eine Dimension als "stark" (>8/10) bewertet → wirklich so stark?

**Wie funktioniert es?**

```
1. Agents liefern Empfehlung: "Fokus auf Feature X, Konfidenz 85%"
2. Devil's Advocate Agent erhält Auftrag:
   → "Finde die 3 stärksten Argumente GEGEN Feature X"
   → Liest dazu aus dem Second Brain: Vergangene Fehlentscheidungen, Marktdaten, Anti-Patterns
3. Gegenargumente werden dem Orchestrator präsentiert
4. Orchestrator erstellt Synthese: Pro + Contra + Empfehlung
5. Mensch erhält beides und entscheidet
```

**Kostenkontrolle**: Der Devil's Advocate ist kein separater teurer LLM-Call. Er arbeitet primär aus dem **Second Brain** — liest dokumentierte Anti-Patterns und historische Fehlentscheidungen. Nur die Synthese erfordert einen LLM-Call.

#### Abgrenzung: Adversarial Learning vs. Ethical Friction

| | Adversarial Learning (L5) | Ethical Friction (L6) |
|---|---|---|
| **Trigger** | Immer bei Gate-Entscheidungen | Nur bei ~100% Agent-Konsens |
| **Ziel** | Bessere Entscheidungen durch Gegenargumente | Groupthink verhindern |
| **Mechanismus** | Devil's Advocate argumentiert aktiv dagegen | System fragt: "Warum seid ihr euch so einig?" |
| **Ergebnis** | Pro/Contra-Synthese für den Menschen | Denkanstoß, kein Gegenargument |

---

## 9. Ethik- & Bias-Dimension (L6)

### 9.1 Innovations-Bias: Vermeidung von Inkrementalisierungs-Verzerrung

**Das Kernproblem**: KI-Agenten können systematisch inkrementelle Innovationen bevorzugen, weil historische Daten diese als „Erfolg" labeln und radikale Ideen weniger Trainingsbeispiele haben.

**Framework-Mitigationen**:

1. **Explizite Innovations-Klassifizierung**: Jede Idee in Phase C wird klassifiziert (Inkrementell / Progressiv / Radikal / Disruptiv)
2. **Innovations-Mix-Quoten**: Mindestens 20% Ideen sollten „Radikal" oder „Disruptiv" sein
3. **Bias-Audit in Phase E**: Knowledge-Agent überprüft Distribution und historische Erfolgsraten
4. **Explizite Bias-Deklaration**: Agent muss vor jeder Empfehlung deklarieren, ob er eine Klasse bevorzugt

### 9.2 Data Bias Propagation & Mitigation

**Pre-Processing**: Datenquellen-Diversifizierung, Multi-Annotator, transparente Datenherkunft
**Processing**: Explizite Feature Selection, Fairness Constraints
**Post-Processing**: Threshold Transparency, Threshold Audit
**Feedback Loop (KRITISCH)**: Balanced Labels, Bias Detection in Loop, Recalibration

### 9.3 Transparenz & Explainability pro Phase

- **Phase A**: Datenherkunft offenlegen, Vertrauensintervalle geben
- **Phase B**: Quellen und fehlende Daten zeigen, Innovationsklassen-Empfehlung begründen
- **Phase C**: Ideen-Typ klassifizieren, Unsicherheiten bei Feasibility benennen
- **Phase D**: KPI-Auswahl begründen, Signifikanz-Level transparent machen
- **Phase E**: Learnings mit Unsicherheit versehen, Kausalität vs. Korrelation unterscheiden

### 9.4 Ethical Friction: Proaktiver Groupthink-Schutz

#### Das Problem: Künstlicher Konsens

Wenn alle Agents dasselbe empfehlen, gibt es zwei Möglichkeiten:
1. Die Empfehlung ist tatsächlich korrekt → gut.
2. Alle Agents haben **denselben Bias** (gleiche Trainingsdaten, gleiche Heuristiken, gleiche blinden Flecken) → gefährlich.

Ethical Friction adressiert Möglichkeit 2.

#### Trigger: Wann wird Ethical Friction aktiviert?

Ethical Friction wird **ausschließlich** aktiviert, wenn:
- **≥95% der beteiligten Agents** dieselbe Empfehlung geben (nahezu perfekter Konsens)
- UND die Entscheidung **strategische Tragweite** hat (Gate-Entscheidung, Pivot, Kill, Innovationsklassen-Wechsel)

**Nicht aktiviert** bei: operativen Entscheidungen, Einzelagent-Outputs, niedrigen Autonomie-Levels (Level 1-2).

#### Mechanismus: Der Denkanstoß

Ethical Friction ist **kein Veto und keine Gegenposition**. Es ist ein strukturierter Denkanstoß:

```
┌─────────────────────────────────────────────────┐
│  ⚡ ETHICAL FRICTION — Konsens-Prüfung          │
│                                                 │
│  Alle 5 beteiligten Agents empfehlen:           │
│  "Pivot zu Abo-Modell" (Konsens: 100%)          │
│                                                 │
│  Fragen zur Reflexion:                          │
│  1. Haben alle Agents dieselben Daten gesehen?  │
│  2. Gibt es Perspektiven, die NICHT vertreten   │
│     sind? (z.B. Bestandskunden, Mitarbeiter)    │
│  3. Welche Annahme müsste falsch sein, damit    │
│     diese Empfehlung schadet?                   │
│                                                 │
│  → Dieser Hinweis ist ein Denkanstoß.           │
│    Er kann die Empfehlung NICHT überstimmen.     │
│    Die Entscheidung liegt beim Menschen.         │
└─────────────────────────────────────────────────┘
```

#### Schutzschranken

| Regel | Warum |
|-------|-------|
| Ethical Friction kann Agents **nicht überstimmen** | Kein Veto-Recht — nur Reflexionsimpuls |
| Maximal **3 Reflexionsfragen** pro Trigger | Kein Overload für den Gründer |
| Gründer kann Ethical Friction **quittieren** ohne Begründung | Autonomie des Menschen bleibt unantastbar |
| Kein eigener LLM-Call — Fragen sind **template-basiert** | Token-Kosten = $0 |
| Wird **dokumentiert** im Second Brain (Dissens-Log) | Nachvollziehbar für Phase E Retrospektive |

#### Zusammenspiel: Dissens-Signal → Adversarial Learning → Ethical Friction

Das Framework hat drei Stufen der Meinungsdiversität:

```
Normaler Betrieb          → Agents diskutieren, Sprecher aggregiert
         ↓
Dissens-Signal (L2)       → Fundamentaler Widerspruch erkannt → Mensch entscheidet
         ↓
Adversarial Learning (L5) → Devil's Advocate liefert Gegenargumente bei Gates
         ↓
Ethical Friction (L6)     → Bei ~100% Konsens: "Seid ihr sicher?" → Denkanstoß
```

Diese drei Mechanismen bilden zusammen ein **Anti-Groupthink-System**, das sowohl natürlichen Dissens nutzt als auch künstlichen Konsens hinterfragt — ohne die Entscheidungshoheit des Menschen einzuschränken.

### 9.5 Accountability Framework

**"Liability Follows Control" Prinzip** (EU AI Act Artikel 14):

| Szenario | Verantwortung | Grund |
|----------|--------------|-------|
| Agent empfiehlt, Gründer übernimmt ohne Validierung | **Gründer** | Hätte validieren sollen |
| Agent empfiehlt mit <40% Konfidenz, Gründer übernimmt | **Gründer** | Agent hat gewarnt |
| Agent empfiehlt ohne Konfidenzwert | **Agent-Betreiber** | Schlecht konfiguriert |
| Agent-Empfehlung war biased | **Agent-Betreiber** | Fehlendes Bias-Testing |
| Korrekte Empfehlung, Markt reagiert anders | **Niemand** (shared risk) | Marktrisiko |

---

## 10. Integrations-Layer (L7)

### 10.1 API-basierte Agent-Architektur

```
┌─────────────────────────────────────────────────────┐
│              Orchestrator (Central Hub)              │
└────────────────┬────────────────────────────────────┘
                 │
    ┌────────────┼────────────────┐
    ▼            ▼                ▼
┌────────┐ ┌────────┐      ┌────────┐
│ Spez.  │ │ Spez.  │ ...  │ Spez.  │
│ Agents │ │ Agents │      │ Agents │
└────┬───┘ └───┬────┘      └───┬────┘
     │         │                │
┌────┴─────────┴────────────────┴────────────┐
│     Standard Agent API Layer               │
│  (REST/GraphQL Endpoints)                  │
└────┬───────────────────────────────────────┘
     │
┌────┴────────────────────────────────┐
│    Startup Tech Stack Integrations  │
├─────────────────────────────────────┤
│ • CRM (Salesforce, Pipedrive)      │
│ • Analytics (Mixpanel, Amplitude)  │
│ • PM Tools (Jira, Asana)          │
│ • Data (Warehouse, BI Tools)      │
│ • Communications (Slack, Email)   │
└─────────────────────────────────────┘
```

### 10.2 Daten-Pipeline-Design pro Phase

**Phase A: ERKENNEN** – Input: CRM Export, Finanzdaten, Analytics, Gründer-Interviews, Public Data → Output: Ist-BMC, Innovation-Lücke Report

**Phase B: AUSRICHTEN** – Input: Support-Tickets, Reviews, NPS, Interviews → Output: Opportunity Map, Suchfeld-Definition

**Phase C: IDEIEREN** – Input: Suchfelder, Patent-DBs, Branchenreports, Ideenpool → Output: Ideen-Longlist, Hypothesen, MVP-Definition

**Phase D: VALIDIEREN** – Input: MVP Definition, Experiment-Daten, Customer Feedback → Output: Test Results, Statistical Significance, Pivot-Empfehlung

**Phase E: KONTROLLIEREN** – Input: Alle Ergebnisse A-D, Finanzen, Retrospektive → Output: Cycle Report, Learnings Knowledge Base, Next Cycle Plan

### 10.3 Minimale Tech-Stacks pro Datenreife-Level

| Stufe | Stack | Kosten/Monat |
|-------|-------|-------------|
| **1 (Minimal)** | Google Sheets, GA4, Notion, Zapier Free, Claude API | $0-50 |
| **2 (Fragmentiert)** | Pipedrive, Mixpanel, Linear, Metabase, LangChain | $200-500 |
| **3 (Strukturiert)** | Salesforce, Amplitude, Snowflake, Tableau, Multi-Agent | $1.000-3.000 |
| **4 (Datengetrieben)** | Full Salesforce, Segment+Amplitude, Databricks, Custom Orchestration | $5.000-10.000+ |

### 10.4 Privacy & Security

1. **GDPR Compliance**: Keine Kundendaten an öffentliche APIs; Agents nicht mit externen LLMs trainiert
2. **Datenminimierung**: Aggregierte Finanzdaten, anonymisierte Support-Tickets, Kohorten-Daten
3. **Access Controls**: Nur Orchestrator hat Zugriff auf alle Outputs; Gründer sieht Aggregationen
4. **Data Retention**: Working Memory → gelöscht nach Zyklus; Episodic → 3 Zyklen; Semantic/Procedural → unbegrenzt

### 10.5 Technische Implementierung: Agent SDK als Umsetzungsebene

Die 15 im Framework definierten Agents (Kap. 2) lassen sich technisch über ein **Agent SDK** (z.B. Anthropic Claude Agent SDK) realisieren. Das SDK bildet die Brücke zwischen der konzeptionellen AIP-Architektur und einer lauffähigen Implementierung.

**Mapping: AIP-Konzepte → Agent SDK**

| AIP-Konzept | SDK-Realisierung |
|-------------|-----------------|
| **Orchestrator Agent** (L2) | SDK-Orchestrator mit Tool-Routing und Agent-Delegation |
| **Spezialisierte Agents** (Phase A-E) | Individuelle Agent-Instanzen mit phasenspezifischen System-Prompts und Tool-Sets |
| **OFH-Sprecher-Mechanismus** | SDK-Koordinationslogik: Agents diskutieren, Sprecher aggregiert, Orchestrator entscheidet |
| **Dissens-als-Innovationssignal** | Divergenz-Detektion in Agent-Outputs → Eskalation an Human-in-the-Loop |
| **Gate-Entscheidungen** | Strukturierte Outputs (JSON) mit Konfidenzwerten → Human-Approval-Workflow |
| **Datenreifegrad-Adaption** (L1) | Dynamische Tool-Konfiguration: Stufe 1 = nur Gründer-Input-Tools; Stufe 4 = API-Connectors |
| **Memory-Architektur** (L5) | SDK-persistente Memory (Working → Episodic → Semantic → Procedural) |
| **Autonomie-Levels** (L3) | Konfigurierbare Human-Approval-Gates im SDK-Workflow |

**Vorteile des SDK-Ansatzes:**
- **Deklarative Agent-Definition**: Jeder der 15 Agents wird durch System-Prompt + Tool-Set + Constraints definiert — kein Low-Level-Code nötig
- **Native OFH-Unterstützung**: Multi-Agent-Diskussion und Sprecher-Aggregation sind SDK-Primitiven
- **Graceful Degradation**: Tool-Sets werden zur Laufzeit basierend auf Datenreifegrad konfiguriert
- **Auditierbarkeit**: Alle Agent-Entscheidungen werden im SDK-Trace protokolliert (→ L6 Ethik-Compliance)

---

## 11. Schwachstellen-Adressierung

### Status der strukturellen Schwächen (S1-S10)

| # | Schwachstelle | Status | Adressiert durch |
|---|--|--------|---|
| S1 | Keine explizite Datenstrategie | **ADRESSIERT** | Kap. 4: Datenreifegrad-Modell + Degradation |
| S2 | Agent-Koordination ungeklärt | **ADRESSIERT** | Kap. 5: OFH mit Sprecher + Dissens-Signal |
| S3 | Menschliche Rolle unterdefiniert | **ADRESSIERT** | Kap. 6: Autonomie-Levels + Entscheidungsmatrix |
| S4 | Startup-Ressourcenrealität ignoriert | **ADRESSIERT** | Kap. 4.3 (Degradation) + Kap. 7 (Skalierung) |
| S5 | Zyklus-Trigger fehlt | **ADRESSIERT** | Kap. 7.2: Dynamische Neukonfiguration |
| S6 | Keine Innovationskultur-Dimension | **TEILWEISE** | Kap. 5.4 (Dissens als Signal) + Kap. 9.1 (Bias-Mix) |
| S7 | Feedback-Schleifen fehlen | **ADRESSIERT** | Kap. 8: SECI + Cross-Cycle Learning |
| S8 | Skalierbarkeit | **ADRESSIERT** | Kap. 7: Konfigurationsmatrix |
| S9 | Messbarkeit | **TEILWEISE** | Gate-Kriterien pro Phase; KPIs definiert |
| S10 | Kein Umgang mit Scheitern | **ADRESSIERT** | Kap. 6: Gate-Entscheidungen + Kill-Option |

### Noch offene konzeptionelle Fragen

1. **Innovationskultur**: Wie stellt man organisationale Bereitschaft sicher? (Beyond Bias-Mitigation)
2. **Framework-Metriken**: Wie misst man, dass agentische Unterstützung Innovation tatsächlich verbessert hat?

---

## 12. Change Management: Framework-Einführung

### 12.1 Das Problem

Kein Framework entfaltet Wirkung, wenn es nicht angenommen wird. Die größte Hürde für das AIP-Framework ist nicht technischer, sondern psychologischer Natur: Gründer müssen bereit sein, strategische Entscheidungen mit KI-Agents zu teilen. Typische Widerstände:

- **Kontrollverlust-Angst**: "Die KI trifft Entscheidungen über mein Unternehmen"
- **Halluzinations-Misstrauen**: "Was wenn der Agent falsche Daten liefert?"
- **Zeitdruck**: "Ich habe keine Zeit für Agent-Governance-Meetings"
- **Komplexitäts-Aversion**: "7 Layers, 15 Agents — das ist zu viel für mein 5-Personen-Team"

### 12.2 Trust-Building-Path (4 Wochen)

| Woche | Fokus | Aktivität | Erwartetes Ergebnis |
|-------|-------|-----------|-------------------|
| **1** | Kennenlernen | Nur Audit-Agent (Phase A): Ist-Analyse des Unternehmens | Gründer sieht: Agent liefert nützliche Insights, keine Überraschungen |
| **2** | Erste Interaktion | Audit-Agent + Opportunity-Scorer: Innovationslücken identifizieren | Gründer erlebt OFH: Agent empfiehlt, Mensch entscheidet |
| **3** | Erweiterung | Phase A komplett (3 Agents) + Gate A→B mit Gründer-Approval | Gründer versteht Gate-Logik und Autonomie-Levels |
| **4** | Review | Retrospektive: Was hat funktioniert? Wo braucht es Anpassung? | Go/No-Go für Phase B-E Rollout |

**Prinzip**: Start klein, Vertrauen aufbauen, schrittweise erweitern. Kein Big-Bang-Rollout.

### 12.3 Konfiguration nach Akzeptanz-Level

| Gründer-Bereitschaft | Empfohlene Konfiguration | Agents | Autonomie-Default |
|----------------------|-------------------------|--------|-------------------|
| **Skeptisch** | Guided Mode: Agent stellt nur Fragen, Gründer antwortet | 1-3 (Audit, Opportunity-Scorer, Retrospective) | Level 1-2 (Manual/Assisted) |
| **Offen** | Collaborative Mode: Agent analysiert, empfiehlt; Gründer entscheidet | 5-8 (Phase A-C Agents) | Level 3 (Hybrid) |
| **Erfahren** | Delegated Mode: Agent operiert semi-autonom mit Gate-Approvals | 10-15 (Alle Phasen) | Level 3-4 (Hybrid/Supervised) |

### 12.4 Governance-Kickoff

Vor dem ersten Einsatz wird einmalig festgelegt:

1. **Welche Datenquellen** darf der Agent nutzen? (Datenschutz, Vertraulichkeit)
2. **Welche Entscheidungen** bleiben immer beim Menschen? (→ Entscheidungsmatrix Kap. 6.3)
3. **Wer ist Orchestrator?** (Gründer? CPO? Externer Berater?)
4. **Wie oft findet Review statt?** (Wöchentlich empfohlen in den ersten 4 Wochen)
5. **Exit-Kriterium**: Wann wird das Framework abgeschaltet, wenn es nicht funktioniert?

---

## 13. Framework at a Glance

```
PHASEN:
A: ERKENNEN       B: AUSRICHTEN     C: IDEIEREN       D: VALIDIEREN     E: KONTROLLIEREN
  ↓                 ↓                 ↓                 ↓                 ↓
[Ist-BMC]      [Strategie]       [Hypothesen]      [Tests]          [Learnings]
  ↓                 ↓                 ↓                 ↓                 ↓
Gate A→B        Gate B→C          Gate C→D          Gate D→E         Gate E→A

GOVERNANCE LAYER (L2) – Orchestrated Feedback Hierarchy:
Orchestrator Agent
  ├─ Spezialisten (arbeiten parallel, diskutieren)
  ├─ Sprecher (dynamisch gewählt, aggregiert Feedback)
  └─ Dissens-Signal (Widersprüche = Innovationschancen)

HUMAN-AI LAYER (L3):
Autonomie-Levels pro Phase (1: Manual bis 5: Fully Autonomous)
Default: Level 3 (Hybrid) für meisten Phasen

ADAPTIVITY LAYER (L4):
Konfiguration nach: Startup-Größe, Datenreife, Branche, Innovationsklasse
Auto-Rekonfiguration wenn sich Kontext ändert

LEARNING LAYER (L5):
SECI-Modell: Socialization → Externalization → Combination → Internalization
Cross-Cycle Learning: Zyklus N Learnings → Zyklus N+1 Improvements

ETHICS LAYER (L6):
Anti-Bias: Innovation-Mix Quoten + Explizite Klassifikation
Data Bias: Lifecycle-Monitoring + Feedback-Loop Safety
Accountability: "Liability Follows Control" Prinzip

INTEGRATION LAYER (L7):
API-basierte Architektur zu CRM, Analytics, PM, BI
Data Pipelines pro Phase
Tech-Stacks je nach Datenreife-Level
```

### Die 15 Standard-Agenten (für Full-Scale Setup)

| Phase | Agent | Aufgabe |
|-------|-------|---------|
| **A** | Audit-Agent | Ist-Analyse des BMC |
| **A** | Market-Scanner-Agent | Markt- & Trend-Daten |
| **A** | Gap-Detector-Agent | Identifiziert Lücken |
| **B** | JTBD-Extractor-Agent | Kundenneeds strukturieren |
| **B** | Opportunity-Scorer-Agent | Quantitative Bewertung |
| **B** | Strategy-Synthesizer-Agent | Strategieoptionen |
| **C** | Ideation-Agent | Ideen-Generierung |
| **C** | Evaluation-Agent | Ideen-Bewertung |
| **C** | Hypothesis-Agent | Hypothesen-Formulierung |
| **D** | Experiment-Designer-Agent | MVP-Definition |
| **D** | Analytics-Agent | Metrik-Tracking |
| **D** | Pivot-Advisor-Agent | Pivot/Persevere/Kill |
| **E** | Retrospective-Agent | Projekt-Analyse |
| **E** | Knowledge-Agent | Learnings Speicherung |
| **E** | Cycle-Initiator-Agent | Nächster Zyklus |

---

## Literaturquellen

**Innovationsprozesse**:
- Lercher, H. (2017). "Das Grazer Innovationsmodell BIG Picture." SSRN.
- Cooper, R. G. (1990). "Stage-Gate Systems." Business Horizons.
- Ries, E. (2011). The Lean Startup. Crown Business.
- Osterwalder, A. & Pigneur, Y. (2010). Business Model Generation. Wiley.
- Christensen, C. M. & Raynor, M. E. (2003). The Innovator's Solution. HBS Press.
- Ulwick, A. W. (2016). Jobs to be Done: Theory to Practice. IDEA BITE PRESS.
- O'Reilly, C. A. & Tushman, M. L. (2004). "The Ambidextrous Organization." HBR.

**Agentic AI & Innovation**:
- Verganti, R., Vendraminelli, L., & Iansiti, M. (2020). "Innovation and Design in the Age of AI." JPIM.
- Bouschery, S. G. & Piller, F. T. (2023). "Augmenting Human Innovation Teams with AI." JPIM.
- Jain, S. & Agrawal, R. (2024). "Generative AI in Innovation Management." JBR.
- Shrestha, Y. R. et al. (2019). "Organizational Decision-Making Structures in the Age of AI." CMR.

**Multi-Agent Systems & Governance**:
- Gartner (2025). "Multiagent Systems in Enterprise AI."
- Dalkey, N. & Helmer, O. (1963). "An Experimental Application of the Delphi Method." Management Science.
- Johnson, D. W. & Johnson, R. T. (2009). "Energizing Learning: The Instructional Power of Conflict." Educational Researcher.

**Human-AI Collaboration**:
- Parasuraman, R., Sheridan, T. B. & Wickens, C. D. (2000). "A Model for Types and Levels of Automation." IEEE Trans. SMC.

**Organizational Learning**:
- Nonaka, I. & Takeuchi, H. (1995). The Knowledge-Creating Company.
- Argyris, C. & Schön, D. A. (1974). Theory in Practice.

**AI Ethics & Governance**:
- NIST AI Risk Management Framework (2023, 2024).
- EU AI Act (2024/1689).
- ISO/IEC 42001 (2023).

---

**Dokumentation erstellt**: 27. März 2026
**Status**: Konsolidierte Dokumentation V3.0
**Changelog**: V1 (OFH + Sprecher) + V2 (L1-L7 vollständig) + Dissens-als-Innovationssignal = V3
**Nächster Schritt**: Lücken füllen (Phase 2) + Prototypische Implementierung
