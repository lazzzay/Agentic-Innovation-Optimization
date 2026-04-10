"""Startup domain models — Genome, IT-Score, Data Maturity (L1 + L4)."""

from __future__ import annotations

from enum import IntEnum

from pydantic import BaseModel, Field, computed_field


class DataMaturityLevel(IntEnum):
    """L1: Data maturity determines how agents operate (Graceful Degradation).

    Level 1 → agents ask questions, generate templates
    Level 2 → agents aggregate fragments, detect patterns
    Level 3 → agents make quantitative statements
    Level 4 → agents identify statistical anomalies, give confidence scores
    """

    MINIMAL = 1
    FRAGMENTED = 2
    STRUCTURED = 3
    DATA_DRIVEN = 4


class StartupGenome(BaseModel):
    """L4: Six-dimensional startup profile for framework auto-configuration.

    Each dimension is scored 1-5. The weighted composite produces the IT-Score
    which identifies the single biggest leverage point for innovation.
    """

    structure: int = Field(ge=1, le=5, description="Organizational structure maturity")
    culture: int = Field(ge=1, le=5, description="Innovation culture & openness")
    founders: int = Field(ge=1, le=5, description="Founder capability & vision")
    technology: int = Field(ge=1, le=5, description="Technology stack maturity")
    market_image: int = Field(ge=1, le=5, description="Market positioning & brand")
    data_maturity: int = Field(ge=1, le=5, description="Data infrastructure quality")

    # Weights for IT-Score calculation (sum = 1.0)
    _weights: dict[str, float] = {
        "structure": 0.10,
        "culture": 0.20,
        "founders": 0.15,
        "technology": 0.20,
        "market_image": 0.10,
        "data_maturity": 0.25,
    }

    @computed_field
    @property
    def it_score(self) -> float:
        """Innovation-Treiber-Score: weighted composite across all dimensions."""
        total = sum(
            getattr(self, dim) * weight for dim, weight in self._weights.items()
        )
        return round(total, 2)

    @computed_field
    @property
    def weakest_dimension(self) -> str:
        """The dimension with the lowest score — the biggest leverage point."""
        dims = {
            "structure": self.structure,
            "culture": self.culture,
            "founders": self.founders,
            "technology": self.technology,
            "market_image": self.market_image,
            "data_maturity": self.data_maturity,
        }
        return min(dims, key=dims.get)  # type: ignore[arg-type]

    @computed_field
    @property
    def data_maturity_level(self) -> DataMaturityLevel:
        """Map data_maturity score to L1 DataMaturityLevel for Graceful Degradation."""
        if self.data_maturity <= 1:
            return DataMaturityLevel.MINIMAL
        if self.data_maturity <= 2:
            return DataMaturityLevel.FRAGMENTED
        if self.data_maturity <= 3:
            return DataMaturityLevel.STRUCTURED
        return DataMaturityLevel.DATA_DRIVEN


class StartupProfile(BaseModel):
    """Complete startup input data for an AIP cycle."""

    name: str = Field(description="Startup name")
    industry: str = Field(description="Industry/vertical")
    stage: str = Field(description="Current stage (pre-seed, seed, series-a, growth)")
    employees: int = Field(ge=1, description="Number of employees")
    description: str = Field(description="What the startup does (1-3 sentences)")
    genome: StartupGenome = Field(description="Six-dimensional startup profile")

    # Available data sources — determines what agents can work with
    available_data: list[str] = Field(
        default_factory=list,
        description="Available data sources (e.g., 'crm', 'analytics', 'surveys', 'financials')",
    )

    # Context for innovation analysis
    current_challenges: list[str] = Field(
        default_factory=list,
        description="Current business challenges / pain points",
    )
    past_innovations: list[str] = Field(
        default_factory=list,
        description="Previous innovation attempts and their outcomes",
    )
    strategic_goals: list[str] = Field(
        default_factory=list,
        description="Where the startup wants to be in 12-18 months",
    )
