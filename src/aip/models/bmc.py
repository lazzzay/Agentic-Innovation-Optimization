"""Business Model Canvas — structured representation used across all phases."""

from __future__ import annotations

from pydantic import BaseModel, Field


class BMCBlock(BaseModel):
    """A single block of the Business Model Canvas with entries and analysis."""

    entries: list[str] = Field(default_factory=list, description="Current items in this block")
    strengths: list[str] = Field(default_factory=list, description="Identified strengths")
    weaknesses: list[str] = Field(default_factory=list, description="Identified weaknesses")
    opportunities: list[str] = Field(default_factory=list, description="Potential improvements")


class BusinessModelCanvas(BaseModel):
    """Osterwalder's BMC as typed structure — agents read and write to this.

    Used as shared language across all AIP phases:
    - Phase A: Ist-BMC (current state)
    - Phase C: Soll-BMC (target state per hypothesis)
    - Phase E: Delta-BMC (what changed)
    """

    key_partners: BMCBlock = Field(default_factory=BMCBlock)
    key_activities: BMCBlock = Field(default_factory=BMCBlock)
    key_resources: BMCBlock = Field(default_factory=BMCBlock)
    value_propositions: BMCBlock = Field(default_factory=BMCBlock)
    customer_relationships: BMCBlock = Field(default_factory=BMCBlock)
    channels: BMCBlock = Field(default_factory=BMCBlock)
    customer_segments: BMCBlock = Field(default_factory=BMCBlock)
    cost_structure: BMCBlock = Field(default_factory=BMCBlock)
    revenue_streams: BMCBlock = Field(default_factory=BMCBlock)

    def summary(self) -> str:
        """One-paragraph summary of the business model."""
        vp = ", ".join(self.value_propositions.entries[:3]) or "not defined"
        cs = ", ".join(self.customer_segments.entries[:3]) or "not defined"
        rs = ", ".join(self.revenue_streams.entries[:3]) or "not defined"
        return (
            f"Value Propositions: {vp}. "
            f"Customer Segments: {cs}. "
            f"Revenue Streams: {rs}."
        )

    def all_weaknesses(self) -> list[str]:
        """Collect weaknesses across all blocks."""
        result = []
        for field_name in self.model_fields:
            block: BMCBlock = getattr(self, field_name)
            for w in block.weaknesses:
                result.append(f"[{field_name}] {w}")
        return result
