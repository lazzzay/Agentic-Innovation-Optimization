# Agentic Innovation Optimization

How can agentic AI systems help startups unlock their untapped innovation potential? This research project develops and evaluates the **Agentic Innovation Process (AIP)** — a hybrid framework that maps agentic AI capabilities onto established innovation methodologies through a multi-agent architecture with novel governance, dissent-as-signal handling, and a self-validation strategy (ClientZero).

The work is a project thesis at **HTWG Konstanz**, following Design Science Research (Hevner et al., 2004; Peffers et al., 2007).

## Research Question

> *Inwiefern können agentische KI-Systeme, auf Basis eines Hybridframeworks aus etablierten Innovationsmodellen, den Innovationsprozess in Startups mit ungenutztem Innovationspotenzial durch phasenübergreifende Multi-Agent-Orchestration optimieren?*

## The AIP Framework

A hybrid combining four established innovation frameworks plus a theoretical lens, instantiated as a multi-agent system with explicit governance:

- **BIG Picture** (Lercher) — cyclical process architecture with stages and gates
- **Lean Startup** (Ries) — Build-Measure-Learn loops for rapid validation
- **Business Model Canvas** (Osterwalder & Pigneur) — typed business-model representation
- **Jobs-to-be-Done** (Ulwick) — systematic customer-needs identification
- **Ambidextrous Organization** (O'Reilly & Tushman) — theoretical lens for exploration vs. exploitation

### Five phases × seven cross-cutting layers

```
ERKENNEN → AUSRICHTEN → IDEIEREN → VALIDIEREN → KONTROLLIEREN
 (Discover)  (Align)     (Ideate)   (Validate)    (Control)
    ^                                                   |
    └───────────────── Learning Loop ──────────────────┘
```

| Layer | Name | What it does |
|-------|------|-------------|
| L1 | Data Maturity | Graceful degradation — framework adapts to any data quality |
| L2 | Agent Governance | OFH — spokesperson mechanism with dissent detection |
| L3 | Human-AI Interaction | Gate-based human-in-the-loop |
| L4 | Adaptivity | Startup Genome & IT-Score — per-startup auto-configuration |
| L5 | Learning | Cycle-spanning knowledge accumulation |
| L6 | Ethics & Bias | Ethical Friction — proactive groupthink protection |
| L7 | Integration | Provider-agnostic LLM stack |

### Key contributions

- **Orchestrated Feedback Hierarchy (OFH)** — democratic agent governance via a spokesperson synthesizer instead of hierarchical control.
- **Dissent-as-Innovation-Signal** — fundamental disagreements between agents are treated as potential innovation signals, not failures to resolve.
- **Startup Genome & IT-Score** — six-dimensional startup profile that auto-configures the framework and identifies the biggest leverage point.
- **Ethical Friction** — when agents converge too easily, the system raises structured reflection questions to counter groupthink.
- **ClientZero** — the framework is applied to its own development as the first validation case (Action Research, Hevner Guideline 3).

## Repository structure

```
.
├── docs/
│   ├── PROJEKTARBEIT.md         — The thesis (~820 lines, single source of truth)
│   ├── BUILD.md                 — Pandoc PDF export workflow
│   ├── LOUS_FRAMEWORK_V3.md     — Framework reference document
│   ├── FORSCHUNGSDESIGN.md      — Research design and methodology
│   ├── PROJECT_LOG.md           — Working journal across the project
│   ├── CLIENT_ZERO.md           — Meta-validation strategy
│   └── material/                — Research material and framework analysis
├── src/aip/                     — Prototype implementation
│   ├── agents/                  — Audit, Market Scanner, Gap Detector
│   ├── ofh.py                   — Dissent detection, spokesperson, ethical friction
│   ├── phases/erkennen.py       — Phase A pipeline
│   ├── models/                  — Pydantic domain types
│   └── graph.py                 — LangGraph StateGraph orchestration
├── tests/                       — 47 tests (10 for OFH, 37 for models/utils)
├── scenarios/                   — Sample startup profiles for the prototype
└── pyproject.toml               — Python package definition
```

## Prototype: Quick start

Phase A (ERKENNEN) is fully implemented. Multi-provider: switch between Anthropic, OpenAI, Google, and Ollama via one environment variable.

```bash
# 1. Setup
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e .[dev]

# 2. Configure
cp .env.example .env   # then edit AIP_PROVIDER + API key
# AIP_PROVIDER=anthropic
# ANTHROPIC_API_KEY=sk-ant-...

# 3. Run
python -m aip scenarios/saas_stagnation.json

# 4. Tests
pytest                  # 47/47, OFH logic mocked, no API calls
```

## Building the thesis PDF

See [`docs/BUILD.md`](docs/BUILD.md) — three Pandoc workflows from quick draft to full BibTeX-citation pipeline with rendered Mermaid diagrams.

## Academic context

Project thesis at HTWG Konstanz, supervised within the program. Methodology: Design Science Research (Hevner et al., 2004; Peffers et al., 2007); methodological triangulation across systematic literature analysis, framework synthesis, ClientZero meta-validation, and prototypical instantiation.

## Citing this work

If you use the AIP framework, its constructs (OFH, Dissens-Signal, IT-Score, Ethical Friction, ClientZero), or build upon this work:

> Lazay, L. (2026). *Agentic Innovation Process (AIP): A Multi-Agent Framework for Innovation Optimization in Startups with Untapped Innovation Potential*. Project thesis, HTWG Konstanz. https://github.com/lazzzay/Agentic-Innovation-Optimization

GitHub also provides a "Cite this repository" button via the `CITATION.cff` file.

## Contributing

Feedback, ideas, and discussions are welcome. Open an issue or reach out via GitHub.

## License

MIT
