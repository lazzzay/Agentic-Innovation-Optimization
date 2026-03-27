# Lou's Framework V2: Agentic Innovation Process (AIP)
## Vollständiges Konzeptionsrahmenwerk für Startups

> Ein universitäres Forschungsprojekt der HTWG Konstanz für die Optimierung von Innovationsprozessen in Startups durch agentische KI-Systeme.

**Dokumentversion:** 2.0
**Datum:** 27. März 2026
**Status:** Finale konzeptionelle Dokumentation

---

## Inhaltsverzeichnis

1. [Grundlagen und Hybridansatz](#1-grundlagen-und-hybridansatz)
2. [Detaillierter Hybrid: Phasen & Agent-Mapping](#2-detaillierter-hybrid-phasen--agent-mapping)
3. [Gesamtbild: Der Zyklus](#3-gesamtbild-der-zyklus)
4. [Daten-Layer: Datenreifegradmodell (L1)](#4-daten-layer-datenreifegradmodell-l1)
5. [Agent-Governance-Modell (L2)](#5-agent-governance-modell-l2)
6. [Human-AI-Interaction-Protokoll (L3)](#6-human-ai-interaction-protokoll-l3)
7. [Adaptivitäts-Mechanismus (L4)](#7-adaptivitäts-mechanismus-l4)
8. [Lern-Loop der Agents (L5)](#8-lern-loop-der-agents-l5)
9. [Ethik- & Bias-Dimension (L6)](#9-ethik--bias-dimension-l6)
10. [Integrations-Layer (L7)](#10-integrations-layer-l7)
11. [Schwachstellen-Adressierung](#11-schwachstellen-adressierung)
12. [Framework at a Glance](#12-framework-at-a-glance)

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

**Potenzielle KI-Agents**:
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

**Potenzielle KI-Agents**:
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

**Potenzielle KI-Agents**:
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

**Potenzielle KI-Agents**:
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

**Potenzielle KI-Agents**:
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
| **2** | **Fragmentiert** | CRM mit Lücken, Google Analytics, Social Media, unstrukturierte Dokumente | Aggregations-Modus: Agents sammeln, verknüpfen und finden Muster | Mittel – Muster erkennbar |
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

---

## 5. Agent-Governance-Modell (L2)

### 5.1 Hierarchische Governance mit Lead Orchestrator

Das Governance-Modell folgt einem **hierarchischen Ansatz mit dezentraler Entscheidungsfreigabe** (hybrid zwischen hierarchisch und demokratisch, je nach Entscheidungstyp):

```
                    Lead Orchestrator Agent
                    (Master Koordinator)
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
    ┌───▼───┐           ┌───▼───┐          ┌───▼───┐
    │Phase A │           │Phase B │          │Phase C │
    │Manager │           │Manager │          │Manager │
    └───┬───┘           └───┬───┘          └───┬───┘
        │                   │                   │
    ┌───▼────────┐      ┌───▼────────┐    ┌───▼────────┐
    │Audit Agent │      │JTBD Agent  │    │Ideation    │
    │Market Agent│      │Scorer Agent│    │Agent       │
    │Gap Agent   │      │Strategy    │    │Eval Agent  │
    └────────────┘      │Agent       │    │Hypothesis  │
                        └────────────┘    │Agent       │
                                          └────────────┘
```

**Grundprinzip**: Der Lead Orchestrator entscheidet über übergreifende Ziele, während Phase-Manager über ihre spezialisierten Agenten autonome Entscheidungen treffen können.

### 5.2 Entscheidungsautoritäts-Levels

| Level | Beschreibung | Wer entscheidet | Beispiel |
|-------|-------------|-----------------|---------|
| **1 – Autonome Aktion** | Agent führt aus ohne Genehmigung | Agent | Analytics-Agent berechnet Metriken |
| **2 – Genehmigungspflichtig (Manager)** | Agent empfiehlt, Phase-Manager genehmigt | Phase-Manager + Agent | Pivot-Empfehlung muss Gründer genehmigen |
| **3 – Eskalation an Mensch** | Agent oder Manager eskaliert an Gründer/Leadership | Mensch | Strategische Pivots, Ressourcen-Umverteilung |
| **4 – Gate-Decision** | Formale Entscheidung an Gate-Checkpoint | Mensch + Agent Input | Übergang von Phase zu Phase |

### 5.3 Konfliktauflösungsmechanismus

Wenn Agenten sich widersprechen (z.B. Opportunity-Scorer empfiehlt Idee X, aber Pivot-Advisor empfiehlt Idee Y):

**Stufe 1 – Automatische Konfliktauflösung** (agent-to-agent):
- Agenten tauschen Reasoning aus
- Hierarchische Autorität entscheidet: wessen Empfehlung hat höhere Priorität?
- Beide Perspektiven werden dokumentiert

**Stufe 2 – Escalation zu Phase-Manager**:
- Falls Agenten sich nicht einigen, eskaliert an übergeordneten Phase-Manager
- Manager wertet beide Argumente und trifft Entscheidung

**Stufe 3 – Escalation zu Lead Orchestrator**:
- Falls Phase-Manager kann nicht entscheiden, eskaliert an Lead Orchestrator
- Lead Orchestrator sieht gesamte Zyklus-Kontext und entscheidet

**Stufe 4 – Human Judgment**:
- Falls auch Lead Orchestrator unsicher, eskaliert an Gründer/Leadership
- Endgültige Entscheidung bei Mensch

### 5.4 Eskalationslogik zu Menschen

**Automatische Eskalation-Trigger**:
- Hohe Unsicherheit (Konfidenz < 40%)
- Widersprechende Agent-Empfehlungen (Confidence Gap > 20 Punkte)
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
Agent-Empfehlung: [Option A mit 65% Konfidenz]
Gegenargument: [Von Agent B mit 55% Konfidenz]
Menschliche Entscheidung erforderlich bis: [Datum]
Konsequenzen bei Verzögerung: [Falls zutreffend]
```

---

## 6. Human-AI-Interaction-Protokoll (L3)

### 6.1 Levels of Autonomy nach Parasuraman et al. (2000)

Das Framework adaptiert die klassische Taxonomie von Parasuraman, Sheridan & Wickens auf die fünf Phasen des Innovationsprozesses:

**Vier generische Funktionen in jedem Phasenschritt**:
1. **Informationsakquisition** (Datensammlung)
2. **Informationsanalyse** (Interpretation)
3. **Entscheidungs- und Aktionswahl** (Was soll getan werden?)
4. **Aktionsimplementierung** (Durchführung)

Für jede Funktion kann Automatisierung auf einem Kontinuum variieren.

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

**Empfohlenes Default-Level**: **Level 3-4** – Agent macht Analyse und Synthese, Gründer validiert und entscheidet endgültig

#### Phase C: IDEIEREN

| Funktion | Level 1 | Level 3 | Level 5 |
|----------|---------|---------|---------|
| **Info-Akquisition** | Brainstorming Sessions | Agent generiert Ideen aus Suchfeldern | Agent generiert Ideen autonom kontinuierlich |
| **Info-Analyse** | Manuelle Bewertung | Evaluation-Agent bewertet, Gründer priorisiert | Agent bewertet und priorisiert autonom |
| **Entscheidung** | Gründer wählt Top-Ideen | Agent empfiehlt Top-3, Gründer wählt | Agent führt aus, Gründer informed |
| **Aktion** | Manuelle Hypothesen-Formulierung | Hypothesis-Agent formuliert, Gründer validiert | Agent formuliert autonom |

**Empfohlenes Default-Level**: **Level 3-4** – Agent generiert viele Ideen und bewertet, Gründer validiert Top-Auswahl

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

**Empfohlenes Default-Level**: **Level 3** – Agent dokumentiert, Gründer validated

### 6.3 Transparenzanforderungen pro Phase

Das Framework verpflichtet den Agent, auf Anfrage oder proaktiv zu offenbaren:

**Minimale Transparenzanforderungen**:
- **Was**: Welche Entscheidung / Empfehlung
- **Warum**: Welche Daten und Logik führten dazu
- **Wie sicher**: Konfidenzwert (0-100%)
- **Wann**: Zeitstempel und Kontext
- **Wer**: Welcher Agent oder Agent-Team traf die Entscheidung
- **Wo sind die Grenzen**: Welche Unsicherheiten oder Annahmen

**Adaptive Transparenz nach Zielgruppe**:
- **Für Gründer**: Executive Summary (1 Absatz) + Key Findings
- **Für Data Scientists**: Detaillierte Methodik + Code-Referenzen
- **Für Gate-Stakeholder**: Business Impact + Empfehlung

### 6.4 Trust Calibration Mechanismen

Das Framework verwendet vier Mechanismen zur Kalibrierung des Vertrauens zwischen Mensch und Agenten:

**1. Confidence Transparency**:
- Agent gibt immer Konfidenzwert an
- Unter 60% = Agent fordert menschliche Validierung an
- 60-80% = Agent empfiehlt, Mensch entscheidet
- >80% = Agent kann implementieren mit Notification

**2. Uncertainty Recognition**:
- Agent muss explizit Unsicherheitsquellen benennen
- Z.B.: "Ich bin mir unsicher, weil: (a) nur 3 Datenpunkte, (b) Outlier erkannt, (c) neue Marktbedingung"

**3. Drift Detection**:
- Agent monitort kontinuierlich, ob seine Empfehlungen noch aktuell sind
- Bei signifikantem Drift (>15% Abweichung) selbst eskalieren

**4. Feedback Loops**:
- Mensch gibt Feedback zu Agent-Empfehlungen
- Agent nutzt Feedback zur kontinuierlichen Verbesserung seines Modells
- Verbesserung wird dokumentiert und transparent gemacht

---

## 7. Adaptivitäts-Mechanismus (L4)

### 7.1 Framework-Konfigurationsmatrix

Das Framework skaliert sich selbst basierend auf **vier Dimensionen**:

1. **Startup-Größe** (Employees)
2. **Datenreife** (Stufe 1-4)
3. **Branche** (Technologie, E-Commerce, SaaS, etc.)
4. **Innovationsklasse** (Inkrementell bis Disruptiv)

#### Dimensionm 1: Startup-Größe

| Größe | Headcount | Agent-Konfiguration | Human Involvement |
|-------|-----------|-------------------|-------------------|
| **Micro** | 1-5 | 3 Core Agents (Audit, Opportunity-Scorer, Retrospective) | Gründer ist Entscheider bei allen Gates |
| **Small** | 5-20 | 7-8 Agents (alle Phase-Manager + 1-2 pro Phase) | Gründer + 1 Innovation Manager sind Entscheider |
| **Medium** | 20-50 | 12-15 Agents (vollständiges Team) | Gründer + Management-Team + Phase-Leads |
| **Large** | 50+ | 20+ Agents + übergreifende Governance | Formal Governance Board |

**Anpassungslogik**:
- Bei < 5 Mitarbeitern: Framework verwendet "Guided Mode" – Agent stellt explizit Fragen und führt durch Prozess
- Bei 5-20: Framework nutzt "Partnership Mode" – Agent und Mensch sind gleichberechtigte Partner
- Bei 20+: Framework nutzt "Autonomous Mode" – Agent operiert mit strategischer Aufsicht

#### Dimension 2: Datenreife

| Stufe | Entscheidungs-Motor | KI-Rollen | Menschliche Rollen |
|-------|-------------------|-----------|-------------------|
| **1 – Minimal** | Gründer Intuition + Agent Fragen | Agent: Facilitator (stellt Fragen) | Gründer: Antwortet, entscheidet |
| **2 – Fragmentiert** | Agent Muster-Erkennung + Mensch Judgement | Agent: Aggregator (sammelt, findet Muster) | Mensch: Interpretiert, validiert |
| **3 – Strukturiert** | Agent Analyse + Mensch Validierung | Agent: Analyst (quantitative Auswertung) | Mensch: Validiert, genehmigt |
| **4 – Datengetrieben** | Agent prädiktiv + Mensch Supervision | Agent: Optimizer (prädiktive Empfehlungen) | Mensch: Überwacht, interveniert |

#### Dimension 3: Branche

Das Framework passt seine **Datenquellen** und **Bewertungskriterien** je nach Branche an:

**SaaS & B2B**:
- Datenquellen: Customer Usage Analytics, Support Tickets, Renewal Rates
- Agenten fokussieren auf: Customer Cohorts, Churn Analysis, Feature Adoption
- Innovationsklassen: Mehrheitlich Inkrementell (Xpress) & Progressiv (Lite)

**E-Commerce & D2C**:
- Datenquellen: Transaction Data, Funnel Analytics, Inventory
- Agenten fokussieren auf: Conversion Optimization, Product Mix, Seasonality
- Innovationsklassen: Mehrheitlich Progressiv & Radikal

**Deeptech & Hardware**:
- Datenquellen: Patent Data, R&D Pipelines, Manufacturing Metrics
- Agenten fokussieren auf: Technical Feasibility, Patent Landscapes, Cost Analysis
- Innovationsklassen: Mehrheitlich Radikal & Disruptiv

**Marketplace & Community**:
- Datenquellen: User-Generated Content, Network Effects, Social Signals
- Agenten fokussieren auf: Network Quality, Liquidity, Retention
- Innovationsklassen: Mehrheitlich Progressiv & Disruptiv

#### Dimension 4: Innovationsklasse

Das Framework passt den **Validierungspfad** und die **Gate-Strenge** je nach Innovation-Typ an:

| Klasse | Definition | BML-Loops | Gate-Anforderungen | Agent-Autonomie |
|--------|-----------|-----------|-------------------|-----------------|
| **Inkrementell** | <10% margin improvement | Sehr schnell (1-2 Wochen) | Low: Datenbasis reicht | Sehr hoch: Agent kann eigenständig iterieren |
| **Progressiv** | 10-50% margin improvement | Moderat (3-8 Wochen) | Medium: Validierung mit Kunden | Mittel: Agent empfiehlt, Mensch genehmigt |
| **Radikal** | 50%+ margin improvement oder neue Features | Langsam (8-16 Wochen) | High: Umfassende Validierung | Niedrig: Agent unterstützt, Mensch entscheidet |
| **Disruptiv** | Neuer Markt oder neues Geschäftsmodell | Sehr langsam (16+ Wochen) | Very High: Strategic Approval | Sehr niedrig: Agent ist Analyst, Mensch ist Dezider |

### 7.2 Dynamische Neukonfiguration

Das Framework überwacht kontinuierlich, ob seine Konfiguration noch passt:

**Trigger für Rekonfiguration**:
- Startup wächst um >50% (z.B. von 3 auf 5 Mitarbeitern)
- Datenreife verbessert sich (z.B. von Stufe 2 zu Stufe 3)
- Branchenfokus ändert sich (z.B. von B2B zu D2C)
- Innovationsstrategie verschiebt sich (z.B. von Inkrementell zu Radikal)

**Rekonfigurations-Prozess**:
1. Framework erkennt Trigger
2. Framework empfiehlt neue Konfiguration
3. Gründer genehmigt (oder überschreibt)
4. Agenten werden neu trainiert
5. Wechsel wird dokumentiert

---

## 8. Lern-Loop der Agents (L5)

### 8.1 SECI-Modell (Nonaka & Takeuchi) angewendet auf Agenten

Das Framework nutzt das klassische **SECI-Modell** (Socialization-Externalization-Combination-Internalization) um zu modellieren, wie organisationales Wissen zu Agent-Wissen wird:

#### 1. **Socialization** (Wissenstaustausch Mensch-zu-Agent)

Agenten lernen **tacit knowledge** (implizites Wissen) von Menschen durch:

- **Gründer-Interviews**: Der Retrospective-Agent führt regelmäßige Interviews mit dem Gründer durch um sein implizites Erfahrungswissen zu erfassen
- **Observation von Entscheidungen**: Der Knowledge-Agent beobachtet, wie Gründer entscheiden und erfasst Entscheidungsheuristiken
- **Feedback-Loops**: Nach jeder Phase dokumentiert der Gründer „Was ich wirklich gemeint habe" vs. „Was der Agent verstanden hat"

**Output**: Agent hat Zugriff auf explizites Modell des Gründer-Know-hows

#### 2. **Externalization** (Wissen aus Daten extrahieren)

Agenten wandeln **unstrukturierte Daten** in strukturiertes Wissen um:

- **Data Mining**: Analytics-Agent extrahiert Muster aus Kundenverhalten
- **Pattern Recognition**: Gap-Detector-Agent identifiziert wiederkehrende Innovation-Lücken über mehrere Zyklen
- **Synthesis**: Knowledge-Agent kombiniert externe Datenquellen (Märkte, Konkurrenten, Trends) mit internen Daten

**Output**: Strukturiertes Wissen über Märkte, Kunden, Innovationsmuster

#### 3. **Combination** (Synthese zu neuen Konzepten)

Agenten kombinieren verschiedenes Wissen zu **neuen konzeptuellen Rahmen**:

- **Cross-Phase Learning**: Knowledge-Agent sieht, dass Ideen aus Zyklus N, die in Phase C gut waren, in Zyklus N+1 nicht gut waren – warum?
- **Meta-Learning**: Agents erkennen über Zeit: „Bei diesem Gründer-Typ funktioniert Strategie A besser als B"
- **Framework-Optimization**: Lead Orchestrator passt Phasen-Sequenzen an basierend auf Lernmuster

**Output**: Kontinuierlich verbessertes Modell von "was funktioniert wann"

#### 4. **Internalization** (Einbau in Agent-Verhalten)

Agenten wenden kombiniertes Wissen auf **zukünftige Entscheidungen** an:

- **Next-Cycle Improvements**: Zyklus N+1 startet mit verbessertem Agent-Verhalten basierend auf Zyklus N
- **Confidence Adjustments**: Agent passt seine Konfidenzwerte an basierend auf historischer Genauigkeit
- **Personalized Prompts**: Agent generiert Prompts, die spezifisch zu diesem Gründer passen

**Output**: Agents werden über Zeit besser und personalisierter

### 8.2 Single-Loop vs. Double-Loop Learning (Argyris & Schön)

#### Single-Loop Learning (Fehlerdetection & -Korrektur)

Agent beobachtet: „Meine Pivot-Empfehlung war falsch, weil ich Daten X nicht hatte"

**Single-Loop Aktion**: Agent sammelt nächstes Mal proaktiv Daten X

**Beispiel**:
- Zyklus 1: Pivot-Advisor empfahl Pivot A, aber Markt reagierte nicht
- Zyklus 2: Pivot-Advisor hat gelernt: „Sammel zuerst Customer-Feedback vor Pivot-Empfehlung"

#### Double-Loop Learning (Grundannahmen hinterfragen)

Agent beobachtet: „Meine Empfehlungen waren konsistent zu optimistisch. Vielleicht ist meine zugrunde liegende Annahme ‚der Markt folgt immer Best-Practice' falsch"

**Double-Loop Aktion**: Agent redefiniertseinen Ansatz. Z.B. von "schaue auf beste Idee" zu "schaue auf beste Idee FÜR DIESEN MARKT"

**Beispiel**:
- Zyklus 1-3: Opportunity-Scorer empfiehlt immer Premium-Ideen, aber Startup kann nicht umsetzen
- Zyklus 4: Opportunity-Scorer hat gelernt: „Meine Annahme ‚mehr Margin = besser' ist falsch. Ich sollte auch Feasibility gewichten"
- Ergebnis: Agent empfiehlt jetzt bessere Ideen für Startup-Kontext

### 8.3 Memory-Architektur: Was Agenten sich merken

Das Framework definiert explizit, **was** Agenten speichern und **wie lange**:

#### Tier 1: Working Memory (aktueller Zyklus)
- **Was**: Alle Daten aus den aktuellen Phasen (A-E)
- **Wie lange**: Während des aktuellen Zyklus
- **Beispiel**: Opportunity-Scorer speichert alle bewerteten Ideen

#### Tier 2: Episodic Memory (letzte 3 Zyklen)
- **Was**: Wichtige Entscheidungen, Learnings, Outcomes
- **Wie lange**: 3 Zyklen (6-12 Monate)
- **Beispiel**: Knowledge-Agent speichert: "Zyklus 1 führte zu Pivot A, Pivot A war erfolgreich"

#### Tier 3: Semantic Memory (kumulatives Lernen)
- **Was**: Verallgemeinerte Muster, Meta-Wissen
- **Wie lange**: Unbegrenzt (bis explizit gelöscht)
- **Beispiel**: "Bei diesem Startup funktioniert radikal Innovation besser als inkrementell" oder "In B2B-Märkten ist JTBD-Extraktion schwieriger"

#### Tier 4: Procedural Memory (Skill-Lernen)
- **Was**: Wie man bestimmte Aufgaben besser macht
- **Wie lange**: Unbegrenzt
- **Beispiel**: "Die beste Frage um tacit knowledge zu extrahieren ist: ‚Erzähle mir von der schlechtesten Entscheidung, die du getroffen hast'"

### 8.4 Cross-Cycle Learning: Von Zyklus N zu Zyklus N+1

**Expliziter Wissenstransfer-Protokoll**:

1. **Phase E (Kontrolle)**: Knowledge-Agent erstellt "Cycle N Learnings Report"
2. **Phase A (Erkennen) von Zyklus N+1**:
   - Gap-Detector-Agent liest Report
   - Passt Suchfelder an basierend auf Learnings aus Zyklus N
   - Fokussiert auf Lücken, die in Zyklus N identifiziert wurden
3. **Kontinuierlich**: Alle Agenten haben Zugriff auf aggregierte Learnings aus vorherigen Zyklen

**Beispiel einer Cross-Cycle-Verbesserung**:
```
Zyklus 1:
- Phase A: Identifiziert Lücke "Kundenunterstützung ist schlecht"
- Phase E: Lerning: "Kundensupport-Lücke schwer zu validieren mit nur Surveys"

Zyklus 2:
- Phase B: Opportunity-Scorer priorisiert "Kundensupport" basierend auf Zyklus 1
- Phase D: Analytics-Agent nutzt bessere Metriken (Support-Tickets, NPS) statt nur Surveys
```

---

## 9. Ethik- & Bias-Dimension (L6)

### 9.1 Innovations-Bias: Vermeidung von Inkrementalisierungs-Verzerrung

**Das Kernproblem** (aus RECHERCHE_AI_ETHICS):

KI-Agenten können systematisch zugunsten inkrementeller Innovationen verzerrt sein, weil:
- Sie auf historischen Daten trainiert sind (vergangene inkrementelle Innovationen als "Erfolg")
- Radikale Ideen weniger Trainingsbeispiele haben
- Sie Risikoaversion bevorzugen können, wenn Verlust-Minimierung in Training priorisiert wird

**Framework-Mitigationen**:

#### 1. Explizite Innovations-Klassifizierung
Jede Idee in Phase C wird explizit klassifiziert:
- **Inkrementell** (0-10% Verbesserung): Z.B. "bessere UI"
- **Progressiv** (10-50% Verbesserung): Z.B. "neue Feature-Kategorie"
- **Radikal** (50%+ Verbesserung): Z.B. "10x schneller als Konkurrenz"
- **Disruptiv** (neuer Markt): Z.B. "komplett neue Use-Case"

#### 2. Innovations-Mix-Quoten
Framework garantiert Diversität in Phase C Output:
- Mindestens 20% Ideen sollten "Radikal" oder "Disruptiv" sein
- Falls Agent nicht genug radikale Ideen generiert, wird explizit nachgefordert
- Gründer muss bewusst überrulen, wenn nur inkrementelle Ideen folgen

#### 3. Bias-Audit in Phase E
Knowledge-Agent überprüft kontinuierlich:
- Distribution der priorisierten Ideen nach Innovationsklasse
- Historische Erfolgsrate nach Innovationsklasse
- Ob bestimmte Innovationstypen systematisch unterschätzt werden

#### 4. Explizite Bias-Deklaration
Agent muss vor jeder Empfehlung deklarieren:
```
INNOVATION CLASS: [Inkrementell/Progressiv/Radikal/Disruptiv]
BIAS CHECK: Bin ich diese Klasse zu favorisieren/zu benachteiligen?
- Historisch erfolgreiche Rate dieser Klasse: X%
- Aktuelle Empfehlung: Klasse Y (mit Z% Konfidenz)
- Falls Konfidenz in Klasse Y < 60%, empfehle ich trotzdem, weil: [...]
```

### 9.2 Data Bias Propagation & Mitigation

Das Framework folgt dem **Lifecycle der Bias-Propagation** (aus RECHERCHE_AI_ETHICS):

#### Pre-Processing Phase
**Potenzielle Biase**:
- Data Collection Bias: Kundenreviews sind nicht repräsentativ (nur zufriedene oder sehr unzufriedene schreiben)
- Label Bias: Support-Tickets werden von voreingenommenen Annotatoren gelabelt

**Framework-Mitigationen**:
- Datenquellen-Diversifizierung: Nutze nicht nur Reviews, auch Support-Tickets, NPS-Surveys, etc.
- Multi-Annotator: Wenn möglich, lasst mehrere Menschen dieselben Daten labeln
- Transparente Datenherkunft: Dokumentiere explizit: "Diese Daten sind zu 70% von zufriedenen Kunden, 30% von unzufriedenen"

#### Processing Phase (Model Training)
**Potenzielle Biase**:
- Algorithmus-Bias: Opportunity-Scorer bevorzugt bestimmte Metriken
- Feature Engineering Bias: Proxy-Features für Geschlecht, Rasse (z.B. "Name-basierte Prediction")

**Framework-Mitigationen**:
- Explizite Feature Selection: Dokumentiere warum jedes Feature relevant ist
- Fairness Constraints: z.B. "Approval Rates sollten nicht >10% zwischen Founder-Geschlechtern unterscheiden"
- Multiple Fairness Definitions: Überprüfe nicht nur eine Fairness-Metrik

#### Post-Processing Phase
**Potenzielle Biase**:
- Threshold Bias: Opportunity-Scorer setzt unterschiedliche Schwellenwerte für verschiedene Ideen-Typen

**Framework-Mitigationen**:
- Threshold Transparency: Dokumentiere explizit: "Ich nutze Schwellenwert X für Radikal-Ideen, Y für Inkrementell"
- Threshold Audit: Überprüfe regelmäßig ob Schwellenwerte fair sind

#### Feedback Loop Phase (KRITISCH)
**Das größte Risiko**: Wenn Gründer kontinuierlich Agent-Empfehlungen akzeptiert (auch wenn falsch), lernt Agent die falschen Muster.

**Framework-Mitigation – "Feedback Loop Safety"**:
1. **Explicit Disagreement Required**: Wenn Gründer Agent-Empfehlung AKZEPTIERT, wird dies als "Training Label" genutzt
2. **Balanced Labels**: Framework stellt sicher, dass Agent auch "Rejections" als Labels sieht, nicht nur "Acceptances"
3. **Bias Detection in Loop**: Knowledge-Agent monitort kontinuierlich: "Hatte ich recht oder war der Gründer zu wohlwollend?"
4. **Recalibration**: Falls Agent merkt, dass er systematisch falsch lag, kalibriert er sich selbst neu

### 9.3 Transparenz & Explainability Requirements pro Phase

**Phase A (ERKENNEN)**:
- Agent muss offenlegen: "Diese Daten sind von [Quelle], könnte [Bias] haben"
- Agent muss Vertrauensintervalle geben: "Ich bin 65% sicher, dass X eine Lücke ist"

**Phase B (AUSRICHTEN)**:
- Agent muss zeigen: "Diese Opportunities basieren auf [Quellen], fehlen [Daten]"
- Agent muss begründen: "Ich rate zu Innovationsklasse X weil [Gründe]"

**Phase C (IDEIEREN)**:
- Agent muss offenlegen: "Diese Idee ist vom Typ [Inkrementell/Radikal], basierend auf [Kriterien]"
- Agent muss Unsicherheiten nennen: "Feasibility unsicher weil [Gründe]"

**Phase D (VALIDIEREN)**:
- Agent muss Metriken erklären: "Ich nutze diese KPIs weil [Gründe], nicht [Alternativen] weil [Gründe]"
- Agent muss Signifikanz-Level transparent machen: "Dieses Ergebnis ist statistisch signifikant mit p < 0.05"

**Phase E (KONTROLLIEREN)**:
- Agent muss Learnings mit Unsicherheit versehen: "Ich bin 70% sicher, dass X gelernt wurde"
- Agent muss Kausalität vs. Korrelation unterscheiden

### 9.4 Accountability Framework

**Wer ist verantwortlich, wenn Agent eine schlechte Empfehlung macht?**

Das Framework folgt dem **"Liability Follows Control" Prinzip** (EU AI Act Artikel 14):

| Szenario | Wer trägt Verantwortung | Warum |
|----------|------------------------|-------|
| Agent empfiehlt X, Gründer übernimmt ohne Validierung | **Gründer** | Gründer hatte Kontrolle und hätte validieren sollen |
| Agent empfiehlt X mit <40% Konfidenz, Gründer übernimmt | **Gründer** | Agent hat explizit vor Unsicherheit gewarnt |
| Agent empfiehlt X ohne Konfidenzwert zu geben, Gründer übernimmt blind | **Agent-Betreiber** (Startup) | Startup hat Agent schlecht konfiguriert |
| Agent gibt X empfohlen, aber X war biased gegen Founder-Demografie | **Agent-Betreiber** (Startup) | Startup schuld für fehlende Bias-Testing |
| Agent empfiehlt X, Gründer validates korrekt, Markt reagiert anders | **Niemand** (shared risk) | Marktrisiko, nicht Agent-Fehler |

---

## 10. Integrations-Layer (L7)

### 10.1 API-basierte Agent-Architektur

Das Framework nutzt eine **modulare API-Architektur** damit Agenten mit bestehenden Startup-Tools kommunizieren können:

```
┌─────────────────────────────────────────────────────┐
│         Lead Orchestrator (Central Hub)              │
└────────────────┬────────────────────────────────────┘
                 │
        ┌────────┼────────┐
        ▼        ▼        ▼
    ┌────────┐┌────────┐┌────────┐
    │Phase A │ Phase B │ Phase C │
    │Manager │ Manager │ Manager │
    └────┬───┘└───┬────┘└───┬────┘
         │        │         │
    ┌────┴────────┴──────────┴─────────────┐
    │     Standard Agent API Layer          │
    │  (REST/GraphQL Endpoints)             │
    └────┬─────────────────────────────────┘
         │
    ┌────┴────────────────────────────────┐
    │    Startup Tech Stack Integrations   │
    ├─────────────────────────────────────┤
    │ • CRM (Salesforce, Pipedrive, etc)  │
    │ • Analytics (Mixpanel, Amplitude)   │
    │ • PM Tools (Jira, Asana)            │
    │ • Data (Warehouse, BI Tools)        │
    │ • Communications (Slack, Email)     │
    └─────────────────────────────────────┘
```

### 10.2 Daten-Pipeline-Design pro Phase

#### Phase A: ERKENNEN
```
INPUT:
├─ CRM Export (Kundenbase)
├─ Finanzdaten (Revenue, ARR, CAC)
├─ Analytics Daten (User Behavior)
├─ Gründer-Interviews (Text/Video)
└─ Public Data (Marktforschung, Konkurrenten)

PROCESSING:
├─ Audit-Agent: Normalisiert & Strukturiert Daten
├─ Market-Scanner-Agent: Reichert externe Daten an
└─ Gap-Detector-Agent: Identifiziert Lücken

OUTPUT:
├─ Ist-BMC (structured data)
├─ Innovation-Lücke Report (PDF/Dashboard)
└─ Gründer-Validierungs-Fragebogen (Feedback-Loop)
```

#### Phase B: AUSRICHTEN
```
INPUT:
├─ CRM Support-Tickets
├─ Customer Reviews (App Stores, G2)
├─ NPS Survey Results
├─ Gründer-Interviews
└─ Marktstudien (externe Quellen)

PROCESSING:
├─ JTBD-Extractor-Agent: Strukturiert Customer Needs
├─ Opportunity-Scorer-Agent: Quantifiziert Importance × (1-Satisfaction)
└─ Strategy-Synthesizer-Agent: Generiert Suchfelder

OUTPUT:
├─ Opportunity Map (Dashboard/Report)
├─ Suchfeld-Definition (structured)
└─ Innovation-Strategie-Empfehlung
```

#### Phase C: IDEIEREN
```
INPUT:
├─ Suchfelder (aus Phase B)
├─ Patent-Datenbanken (externe API)
├─ Branchenreports (externe Quellen)
├─ Interner Ideenpool (Gründer-Input)
└─ Konkurrenten-Analyse (web scraping)

PROCESSING:
├─ Ideation-Agent: Generiert Ideen aus Suchfeldern
├─ Evaluation-Agent: Bewertet nach Impact × Feasibility
└─ Hypothesis-Agent: Formuliert testbare Hypothesen

OUTPUT:
├─ Ideen-Longlist (mit Bewertungen)
├─ Hypothesen-Statements (testable)
└─ MVP-Definition für Top-3 Ideen
```

#### Phase D: VALIDIEREN
```
INPUT:
├─ MVP Definition (aus Phase C)
├─ Experiment Daten (A/B Tests, Landing Pages)
├─ Customer Feedback (Surveys, Interviews)
├─ Analytics Data (Conversions, Retention)
└─ Markt-Feedback (externe Signals)

PROCESSING:
├─ Experiment-Designer-Agent: Plant Test-Setup
├─ Analytics-Agent: Trackt & analysiert Metriken
└─ Pivot-Advisor-Agent: Empfiehlt Pivot/Persevere/Kill

OUTPUT:
├─ Test Results Dashboard
├─ Statistical Significance Report
└─ Pivot/Persevere/Kill Empfehlung
```

#### Phase E: KONTROLLIEREN
```
INPUT:
├─ Alle Ergebnisse aus Phasen A-D
├─ Finanzielle Outcome-Daten
├─ Retrospektive-Interviews (Gründer)
└─ Externe Markt-Daten

PROCESSING:
├─ Retrospective-Agent: Analysiert Projekt-Outcomes
├─ Knowledge-Agent: Extrahiert & speichert Learnings
└─ Cycle-Initiator-Agent: Plant nächsten Zyklus

OUTPUT:
├─ Cycle Report (PDF/Dashboard)
├─ Learnings Knowledge Base (structured)
└─ Next Cycle Kick-off Plan
```

### 10.3 Minimale Tech-Stacks pro Datenreife-Level

#### Stufe 1 (Minimal): MVP Tech Stack
- **CRM**: Google Sheets (kostenlos) oder Pipedrive Free
- **Analytics**: Google Analytics 4 (kostenlos)
- **PM**: Asana Free oder Notion
- **Integration**: Zapier Free (100 Aufrufe/Monat)
- **AI Backbone**: Claude API (pay-per-use) oder OpenAI API
- **Estimated Cost**: $0-50/Monat

**Besonderheit**: Agent-Outputs sind oft Google Docs oder Sheets statt Dashboards

#### Stufe 2 (Fragmentiert): Startup Tech Stack
- **CRM**: Pipedrive oder Salesforce (niedrig-tier)
- **Analytics**: Mixpanel oder Amplitude
- **PM**: Jira oder Linear
- **Data Integration**: Fivetran oder Stitch (basic)
- **BI**: Metabase (self-hosted, kostenlos) oder Looker Studio
- **AI Backbone**: Claude API + LangChain/LangGraph
- **Estimated Cost**: $200-500/Monat

**Besonderheit**: Agents können auf BI-Tools schreiben, nicht nur Dateien

#### Stufe 3 (Strukturiert): Scale-up Stack
- **CRM**: Salesforce (mid-tier) oder HubSpot
- **Analytics**: Amplitude, Mixpanel, oder Segment
- **PM**: Jira mit Integrations-Plugins
- **Data Warehouse**: Snowflake oder BigQuery
- **BI**: Tableau oder Looker (Google Cloud)
- **AI Backbone**: Multi-Agent System (CrewAI, LangGraph, oder AutoGen)
- **Estimated Cost**: $1,000-3,000/Monat

**Besonderheit**: Agents können direkt auf Data Warehouse abfragen

#### Stufe 4 (Datengetrieben): Enterprise Stack
- **CRM**: Salesforce (full suite)
- **Analytics**: Segment, Amplitude, Mixpanel kombiniert
- **PM**: Jira Enterprise
- **Data Warehouse**: Snowflake, BigQuery, oder Databricks
- **BI**: Tableau, Looker, oder ThoughtSpot
- **AI Backbone**: Custom multi-agent orchestration mit Governance
- **Estimated Cost**: $5,000-10,000+/Monat

**Besonderheit**: Full automation möglich mit comprehensive governance

### 10.4 Privacy & Security Considerations

**Datenschutz-Anforderungen**:
1. **GDPR Compliance** (EU):
   - Kundendaten dürfen nicht auf öffentliche APIs gehen
   - Agents dürfen nicht mit externen LLMs trainiert werden
   - Mitarbeiter müssen Datenverarbeitung konsent geben

2. **Datenminimierung**:
   - Phase A Agent nutzt nur aggregierte Finanzdaten, nicht Einzeltransaktionen
   - JTBD-Agent anonymisiert Kundennamen in Support-Tickets
   - Analytics-Agent nutzt nur aggregierte Kohorten-Daten, nicht Individual User IDs

3. **Access Controls**:
   - Nur Lead Orchestrator hat Zugriff auf alle Agent-Outputs
   - Gründer sieht aggregierte Outputs, nicht Rohdaten
   - Agents können nicht auf externe Systeme ohne explizite Genehmigung zugreifen

4. **Data Retention**:
   - Working Memory (Stufe 1): Gelöscht nach Zyklus-Ende
   - Episodic Memory (Stufe 2): 3 Zyklen, dann anonymisiert
   - Semantic Memory (Stufe 3): Unbegrenzt (Learnings)
   - Procedural Memory (Stufe 4): Unbegrenzt (Skills)

---

## 11. Schwachstellen-Adressierung

### Status der strukturellen Schwächen (S1-S10)

| # | Schwachstelle | Status | Adressiert durch |
|---|--|--------|---|
| S1 | Keine explizite Datenstrategie | **ADRESSIERT** | Kapitel 4: Datenreifegrad-Modell + Degradation-Prinzip |
| S2 | Agent-Koordination ungeklärt | **ADRESSIERT** | Kapitel 5: Agent-Governance-Modell + Hierarchie |
| S3 | Menschliche Rolle unterdefiniert | **ADRESSIERT** | Kapitel 6: Human-AI Interaction Protokoll + Autonomie-Levels |
| S4 | Startup-Ressourcenrealität ignoriert | **ADRESSIERT** | Kapitel 4.3 (Degradation) + Kapitel 7.2 (Skalierung nach Größe) |
| S5 | Zyklus-Trigger fehlt | **ADRESSIERT** | Kapitel 7.2: Dynamische Neukonfiguration + Auto-Trigger |
| S6 | Keine Innovationskultur-Dimension | **TEILWEISE** | Kapitel 5.4 + 9.1: Innovation-Bias Mitigation + Diversity |
| S7 | Feedback-Schleifen zwischen Phasen fehlen | **ADRESSIERT** | Kapitel 8: Cross-Cycle Learning + SECI-Modell |
| S8 | Skalierbarkeit der Agent-Architektur | **ADRESSIERT** | Kapitel 7: Konfigurationsmatrix nach Startup-Größe |
| S9 | Messbarkeit des Framework-Erfolgs | **TEILWEISE** | Jede Phase definiert Gate-Kriterien; KPIs pro Phase |
| S10 | Kein Umgang mit Scheitern | **ADRESSIERT** | Kapitel 6: Autonomie-Levels + Gate-Entscheidungen |

### Noch offene konzeptionelle Fragen

1. **Innovationskultur**: Wie stellt man organisationale Risikoaversion sicher? (Beyond Bias-Mitigation)
2. **Framework-Metriken**: Wie misst man, dass agentische Unterstützung Innovation tatsächlich verbessert hat?
3. **Change Management**: Wie führt man das Framework in einer bestehenden Organisation ein?

---

## 12. Framework at a Glance

### Die fünf Phasen + fünf Daten-Layer

```
PHASEN:
A: ERKENNEN       B: AUSRICHTEN     C: IDEIEREN       D: VALIDIEREN     E: KONTROLLIEREN
  ↓                 ↓                 ↓                 ↓                 ↓
[Ist-BMC]      [Strategie]       [Hypothesen]      [Tests]          [Learnings]
  ↓                 ↓                 ↓                 ↓                 ↓
Gate A→B        Gate B→C          Gate C→D          Gate D→E         Gate E→A

GOVNANCE LAYER (L2):
Lead Orchestrator
  ├─ Phase Managers (delegieren zu Agenten)
  └─ Conflict Resolution (3-stufiges Eskalations-Modell)

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

**Innovationsprozesse & Agentic AI**:
- Verganti, R., Vendraminelli, L., & Iansiti, M. (2020). "Innovation and Design in the Age of Artificial Intelligence." Journal of Product Innovation Management
- Bouschery, S. G., & Piller, F. T. (2023). "Augmenting human innovation teams with AI." Journal of Product Innovation Management
- Jain, S., & Agrawal, R. (2024). "Generative AI in innovation management." Journal of Business Research

**Multi-Agent Systems & Governance**:
- Gartner (2025). "Multiagent Systems in Enterprise AI"
- Shrestha, Y. R., Ben-Menahem, S. M., & von Krogh, G. (2019). "Organizational Decision-Making Structures in the Age of AI." California Management Review

**Human-AI Collaboration**:
- Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). "A model for types and levels of automation." IEEE Transactions on Systems, Man, and Cybernetics

**AI Ethics & Governance**:
- NIST AI Risk Management Framework (2023, 2024)
- EU AI Act (2024/1689)
- ISO/IEC 42001 (2023)

**Organizational Learning**:
- Nonaka, I., & Takeuchi, H. (1995). "The Knowledge-Creating Company"
- Argyris, C., & Schön, D. A. (1974). "Theory in Practice: Increasing Professional Effectiveness"

---

**Dokumentation erstellt**: 27. März 2026
**Status**: Finale konzeptionelle Dokumentation v2.0
**Nächster Schritt**: Prototypische Implementierung und Fallstudien-Validierung
