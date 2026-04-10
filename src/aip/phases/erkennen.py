"""Phase A: ERKENNEN — Where does the startup stand? Where is untapped potential?

This phase runs three agents in parallel, then synthesizes via OFH:
1. Audit Agent → BMC analysis
2. Market Scanner → External intelligence
3. Gap Detector → Innovation gaps (uses outputs of 1 & 2)

Then: OFH voting → Dissent detection → Ethical Friction check → Gate A→B
"""

from __future__ import annotations

import json
from typing import Any

from aip.agents.base import ModelTier, run_agent
from aip.models.bmc import BusinessModelCanvas
from aip.models.innovation import InnovationGap
from aip.models.phase_output import PhaseAOutput
from aip.models.startup import DataMaturityLevel
from aip.ofh import detect_dissent, ethical_friction_check, spokesperson_synthesis
from aip.state import AIPState


# -- Pydantic models for agent-specific structured outputs --

from pydantic import BaseModel, Field


class AuditOutput(BaseModel):
    """Structured output from the Audit Agent."""

    current_bmc: BusinessModelCanvas
    exploitation_exploration_ratio: str = Field(
        description="Assessment of exploitation vs exploration balance"
    )
    key_findings: list[str] = Field(description="Top findings from the audit")


class MarketScannerOutput(BaseModel):
    """Structured output from the Market Scanner Agent."""

    market_trends: list[str] = Field(description="Key market and technology trends")
    competitor_insights: list[str] = Field(description="Competitor observations")
    emerging_opportunities: list[str] = Field(description="Untapped market opportunities")
    threat_signals: list[str] = Field(description="Potential threats or disruptions")


class GapDetectorOutput(BaseModel):
    """Structured output from the Gap Detector Agent."""

    innovation_gaps: list[InnovationGap] = Field(description="Identified innovation gaps")
    priority_ranking: list[str] = Field(
        description="Gap titles ranked by innovation potential"
    )


# -- Data maturity instructions --

DATA_MATURITY_INSTRUCTIONS: dict[DataMaturityLevel, str] = {
    DataMaturityLevel.MINIMAL: (
        "DATA MATURITY: Level 1 (Minimal). You have very limited data. "
        "Generate structured questions and hypotheses rather than definitive analyses. "
        "Frame outputs as 'areas to investigate' with low confidence markers."
    ),
    DataMaturityLevel.FRAGMENTED: (
        "DATA MATURITY: Level 2 (Fragmented). You have some data but it's scattered. "
        "Connect fragments where possible. Note confidence levels explicitly. "
        "Distinguish clearly between data-backed and inferred conclusions."
    ),
    DataMaturityLevel.STRUCTURED: (
        "DATA MATURITY: Level 3 (Structured). You have organized data available. "
        "Make quantitative assessments where the data supports it. "
        "Provide specific metrics and comparisons."
    ),
    DataMaturityLevel.DATA_DRIVEN: (
        "DATA MATURITY: Level 4 (Data-Driven). Comprehensive data is available. "
        "Provide statistical backing, confidence intervals, and quantified assessments. "
        "Use data to challenge assumptions, not just confirm them."
    ),
}


async def run_phase_a(state: AIPState) -> dict[str, Any]:
    """Execute Phase A: ERKENNEN.

    Returns a partial state update dict (LangGraph pattern).
    """
    startup = state["startup"]
    maturity = state["data_maturity"]
    maturity_instruction = DATA_MATURITY_INSTRUCTIONS[maturity]

    # Serialize startup context for agents
    startup_context = json.dumps(
        startup if isinstance(startup, dict) else startup.model_dump(),
        indent=2,
        ensure_ascii=False,
    )

    # -- Step 1: Run Audit + Market Scanner in parallel --
    # (Gap Detector needs their outputs, so it runs after)

    audit_result = await run_agent(
        agent_name="audit",
        tier=ModelTier.REASONING,
        context=f"## Startup Data\n{startup_context}",
        output_schema=AuditOutput,
        additional_instructions=maturity_instruction,
    )

    market_result = await run_agent(
        agent_name="market_scanner",
        tier=ModelTier.REASONING,
        context=f"## Startup Data\n{startup_context}",
        output_schema=MarketScannerOutput,
        additional_instructions=maturity_instruction,
    )

    # -- Step 2: Gap Detector uses outputs from Audit + Market Scanner --
    gap_context = (
        f"## Startup Data\n{startup_context}\n\n"
        f"## Audit Agent Findings\n"
        f"BMC Summary: {audit_result.current_bmc.summary()}\n"
        f"Weaknesses: {json.dumps(audit_result.current_bmc.all_weaknesses(), ensure_ascii=False)}\n"
        f"Exploitation/Exploration: {audit_result.exploitation_exploration_ratio}\n\n"
        f"## Market Scanner Findings\n"
        f"Trends: {json.dumps(market_result.market_trends, ensure_ascii=False)}\n"
        f"Opportunities: {json.dumps(market_result.emerging_opportunities, ensure_ascii=False)}\n"
        f"Threats: {json.dumps(market_result.threat_signals, ensure_ascii=False)}"
    )

    gap_result = await run_agent(
        agent_name="gap_detector",
        tier=ModelTier.REASONING,
        context=gap_context,
        output_schema=GapDetectorOutput,
        additional_instructions=maturity_instruction,
    )

    # -- Step 3: OFH — Dissent Detection --
    agent_outputs = {
        "audit_agent": audit_result.model_dump(),
        "market_scanner": market_result.model_dump(),
        "gap_detector": gap_result.model_dump(),
    }

    dissent_signals = await detect_dissent(agent_outputs, phase="A: ERKENNEN")

    # -- Step 4: Ethical Friction Check --
    friction = await ethical_friction_check(agent_outputs, phase="A: ERKENNEN")

    # -- Step 5: OFH Spokesperson → Gate Decision --
    gate_decision = await spokesperson_synthesis(
        agent_outputs=agent_outputs,
        dissent_signals=dissent_signals,
        phase="A: ERKENNEN",
        gate_name="A→B",
    )

    # -- Assemble Phase A Output --
    phase_output = PhaseAOutput(
        current_bmc=audit_result.current_bmc,
        exploitation_exploration_ratio=audit_result.exploitation_exploration_ratio,
        market_trends=market_result.market_trends,
        competitor_insights=market_result.competitor_insights,
        innovation_gaps=gap_result.innovation_gaps,
        gate_decision=gate_decision,
    )

    # Return partial state update
    return {
        "phase_a": phase_output,
        "dissent_signals": state.get("dissent_signals", []) + dissent_signals,
        "gates": state.get("gates", []) + [gate_decision],
        "current_phase": "B" if gate_decision.decision == "go" else "A",
        "needs_human_input": gate_decision.decision != "go" or bool(dissent_signals),
    }
