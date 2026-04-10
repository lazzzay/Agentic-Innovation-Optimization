"""Typed domain models for the AIP framework.

Every innovation artifact is a Pydantic model — structured, validated, serializable.
"""

from aip.models.bmc import BusinessModelCanvas
from aip.models.innovation import (
    DissensSignal,
    GateDecision,
    Hypothesis,
    InnovationGap,
    JTBDJob,
    Opportunity,
)
from aip.models.phase_output import (
    PhaseAOutput,
    PhaseBOutput,
    PhaseCOutput,
)
from aip.models.startup import DataMaturityLevel, StartupGenome, StartupProfile

__all__ = [
    "BusinessModelCanvas",
    "DataMaturityLevel",
    "DissensSignal",
    "GateDecision",
    "Hypothesis",
    "InnovationGap",
    "JTBDJob",
    "Opportunity",
    "PhaseAOutput",
    "PhaseBOutput",
    "PhaseCOutput",
    "StartupGenome",
    "StartupProfile",
]
