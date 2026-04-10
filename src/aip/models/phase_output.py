"""Typed outputs per phase — what each phase delivers as structured artifact."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from aip.models.bmc import BusinessModelCanvas
from aip.models.innovation import (
    GateDecision,
    Hypothesis,
    InnovationGap,
    Opportunity,
)


class PhaseAOutput(BaseModel):
    """Phase A (ERKENNEN) output: Where does the startup stand?"""

    current_bmc: BusinessModelCanvas = Field(description="Ist-BMC of the startup")
    exploitation_exploration_ratio: str = Field(
        description="Assessment: is the startup over-exploiting or exploring?"
    )
    market_trends: list[str] = Field(description="Relevant market & technology trends")
    competitor_insights: list[str] = Field(description="Key competitor observations")
    innovation_gaps: list[InnovationGap] = Field(description="Identified gaps")
    gate_decision: GateDecision | None = Field(
        default=None, description="Gate A→B decision"
    )
    timestamp: datetime = Field(default_factory=datetime.now)


class PhaseBOutput(BaseModel):
    """Phase B (AUSRICHTEN) output: Where should innovation go?"""

    opportunities: list[Opportunity] = Field(description="Scored opportunity list")
    search_fields: list[str] = Field(
        description="Top 3 innovation directions to explore"
    )
    innovation_class: str = Field(
        description="Recommended innovation class (incremental/progressive/radical/disruptive)"
    )
    gate_decision: GateDecision | None = Field(
        default=None, description="Gate B→C decision"
    )
    timestamp: datetime = Field(default_factory=datetime.now)


class PhaseCOutput(BaseModel):
    """Phase C (IDEIEREN) output: What could solutions look like?"""

    ideas_generated: int = Field(description="Total ideas in longlist")
    top_hypotheses: list[Hypothesis] = Field(description="Top 3-5 testable hypotheses")
    target_bmc: BusinessModelCanvas | None = Field(
        default=None, description="Soll-BMC for the top hypothesis"
    )
    gate_decision: GateDecision | None = Field(
        default=None, description="Gate C→D decision"
    )
    timestamp: datetime = Field(default_factory=datetime.now)
