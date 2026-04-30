"""Innovation domain models — gaps, opportunities, hypotheses, dissent signals."""

from __future__ import annotations

from enum import Enum
from typing import Literal

from pydantic import BaseModel, Field, computed_field


class InnovationClass(str, Enum):
    """BIG Picture innovation classification."""

    INCREMENTAL = "incremental"
    PROGRESSIVE = "progressive"
    RADICAL = "radical"
    DISRUPTIVE = "disruptive"


class InnovationGap(BaseModel):
    """An identified gap between current state and market potential.

    Severity rubric (used by agents to assign the severity field):
      - low      : noticeable but no immediate revenue / retention impact;
                   addressable in normal product cycles.
      - medium   : measurable competitive / customer impact within 6-12 months
                   if unaddressed; bounded scope.
      - high     : material risk to growth, retention, or differentiation
                   within 3-6 months; touches a core BMC block.
      - critical : existential or near-existential risk (e.g. product becomes
                   competitively obsolete, accelerating churn that compounds);
                   warrants immediate intervention.
    """

    title: str = Field(description="Short gap description")
    description: str = Field(description="Detailed analysis of the gap")
    evidence: list[str] = Field(description="Supporting data points or observations")
    severity: Literal["low", "medium", "high", "critical"] = Field(
        description=(
            "Severity following the four-level rubric in this class' docstring: "
            "low = no immediate impact; medium = measurable impact within 6-12 months; "
            "high = material risk to a core BMC block within 3-6 months; "
            "critical = existential or near-existential risk."
        )
    )
    source_block: str = Field(
        default="",
        description="Which BMC block this gap relates to",
    )


class Opportunity(BaseModel):
    """A scored innovation opportunity (JTBD-based)."""

    job_statement: str = Field(description="The job-to-be-done")
    importance: float = Field(ge=0, le=10, description="How important is this job (0-10)")
    satisfaction: float = Field(ge=0, le=10, description="How well is it currently done (0-10)")
    rationale: str = Field(description="Why this is an opportunity")

    @computed_field
    @property
    def opportunity_score(self) -> float:
        """Ulwick formula: Importance + (Importance - Satisfaction)."""
        return round(self.importance + max(0, self.importance - self.satisfaction), 2)


class JTBDJob(BaseModel):
    """A Job-to-be-Done extracted from customer/market data."""

    job: str = Field(description="The functional or emotional job")
    context: str = Field(description="In what situation does this job arise")
    current_solution: str = Field(description="How is it currently solved")
    pain_points: list[str] = Field(description="What's frustrating about the current solution")


class Hypothesis(BaseModel):
    """A testable innovation hypothesis (Lean Startup style)."""

    statement: str = Field(
        description="We believe that [customer] will [behavior] if we [change]"
    )
    target_customer: str = Field(description="Who we're targeting")
    expected_outcome: str = Field(description="What we expect to happen")
    success_metric: str = Field(description="How we measure success")
    innovation_class: InnovationClass = Field(description="Type of innovation")
    risk_level: Literal["low", "medium", "high"] = Field(description="Implementation risk")
    confidence: float = Field(
        ge=0, le=1, description="Agent's confidence in this hypothesis (0-1)"
    )


class DissensSignal(BaseModel):
    """OFH: When agents fundamentally disagree, it's an innovation signal.

    This is a core AIP contribution — agent conflict is not failure,
    it's a potential innovation opportunity worth human attention.
    """

    topic: str = Field(description="What the agents disagree about")
    positions: dict[str, str] = Field(
        description="Agent name → their position (mapping of divergent views)"
    )
    divergence_score: float = Field(
        ge=0, le=1, description="How far apart the positions are (0=agreement, 1=fundamental)"
    )
    innovation_potential: str = Field(
        description="Why this disagreement might point to an innovation opportunity"
    )
    recommended_action: str = Field(
        description="What the human should consider (not a directive — a thought impulse)"
    )


class GateDecision(BaseModel):
    """Decision at a phase gate — go, iterate, or kill."""

    gate: str = Field(description="Gate identifier (e.g., 'A→B')")
    decision: Literal["go", "iterate", "kill"] = Field(description="Gate outcome")
    rationale: str = Field(description="Why this decision")
    dissent_signals: list[DissensSignal] = Field(
        default_factory=list,
        description="Any dissent signals detected during this gate",
    )
    human_override: bool = Field(
        default=False, description="Was this decision overridden by human"
    )
    confidence: float = Field(ge=0, le=1, description="Confidence in this decision")
