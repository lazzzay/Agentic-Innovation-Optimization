# Phase 2: EXECUTION — Tracker

**Start:** 10. April 2026
**Deadline:** ~26. April 2026

---

## Strang 1: Prototyp (AIP Framework)

| # | Aufgabe | Status | Datum | Notizen |
|---|---------|--------|-------|---------|
| P1 | Architektur-Entscheidung | DONE | 10.04. | Python + LangGraph + Pydantic; LLM-agnostisch |
| P2 | Projektstruktur aufsetzen | DONE | 10.04. | pyproject.toml, venv, Dependencies |
| P3 | Domain-Modelle (Pydantic) | DONE | 10.04. | StartupGenome, IT-Score, BMC, InnovationGap, DissensSignal, Hypothesis |
| P4 | LangGraph State + Orchestrator | DONE | 10.04. | TypedState, StateGraph mit Checkpointing |
| P5 | OFH-Mechanismus | DONE | 10.04. | Dissent Detection, Spokesperson Synthesis, Ethical Friction |
| P6 | Phase A (ERKENNEN) komplett | DONE | 10.04. | 3 Agents (Audit, MarketScanner, GapDetector) + OFH + Gate |
| P7 | Multi-Provider-Support | DONE | 10.04. | Anthropic, OpenAI, Google, Ollama — eine Zeile .env |
| P8 | Szenario 1 (SaaS Stagnation) | DONE | 10.04. | DataPulse Analytics, Level 3 |
| P9 | CLI mit Rich-Output | DONE | 10.04. | python -m aip scenario.json |
| P10 | Phase B (AUSRICHTEN) | OFFEN | | JTBD-Extractor, Opportunity-Scorer, Strategy-Synthesizer |
| P11 | Phase C (IDEIEREN) | OFFEN | | Ideation, Evaluation, Hypothesis Agents |
| P12 | Szenario 2 (Datenreifegrad 1) | OFFEN | | Graceful Degradation demonstrieren |
| P13 | Erster Live-Run Phase A | OFFEN | | Braucht API-Key in .env |
| P14 | Outputs dokumentieren | OFFEN | | Ergebnisse für die Arbeit aufbereiten |

## Strang 2: Arbeit schreiben

| # | Aufgabe | Status | Datum | Notizen |
|---|---------|--------|-------|---------|
| A1 | Kap. 1 — Einleitung | OFFEN | | 4-5 Seiten, keine Abhängigkeit |
| A2 | Kap. 2 — Theoretische Grundlagen | OFFEN | | 7-8 Seiten, Literatur liegt vor |
| A3 | Kap. 3 — Methodik | OFFEN | | 5-6 Seiten |
| A4 | Kap. 4 — AIP Framework | OFFEN | | 10-12 Seiten, basiert auf V3.md |
| A5 | Kap. 5 — Ergebnisse & Diskussion | OFFEN | | Braucht Szenario-Ergebnisse |
| A6 | Kap. 6 — Fazit & Ausblick | OFFEN | | Braucht Kap. 5 |
| A7 | Formalia (Deckblatt, Verz., Format) | OFFEN | | |

## Tech-Stack

| Komponente | Technologie | Warum |
|------------|-------------|-------|
| Orchestrierung | LangGraph (StateGraph) | Typed State, Checkpointing, Conditional Edges |
| Agent-Output | Pydantic v2 | Strukturierte, validierte Innovation-Artefakte |
| LLM-Integration | LangChain (provider-agnostisch) | Anthropic, OpenAI, Google, Ollama |
| Model Tiering | 3-Tier (Routing/Reasoning/Critique) | Kosten-/Qualitätsoptimierung |
| CLI | Rich | Professionelle Terminal-Ausgabe |
| Persistenz | LangGraph MemorySaver (→ SQLite) | Checkpoint nach jedem Schritt |

## Entscheidungen

| Datum | Entscheidung | Begründung |
|-------|-------------|------------|
| 10.04. | Python + LangGraph + Pydantic statt raw Python | SOTA für Multi-Agent-Systeme; Checkpointing, typed state, reproduzierbar |
| 10.04. | LLM-agnostisch (Multi-Provider) | Akademisch wichtig: Framework ≠ Vendor-Lock-in; Reproduzierbarkeit |
| 10.04. | 3-Tier Model Routing | Kosteneffizient: Haiku für Routing, Sonnet für Reasoning |
| 10.04. | Phase A zuerst vollständig | Proof of Concept: eine Phase komplett durchimplementiert zeigt das Prinzip |
