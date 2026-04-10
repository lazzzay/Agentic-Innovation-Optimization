"""LangGraph typed state — the single source of truth flowing through the graph.

Every node reads from and writes to this state. LangGraph checkpoints it
after each step → full reproducibility and inspectability.
"""

from __future__ import annotations

from typing import Annotated

from langgraph.graph.message import add_messages
from pydantic import BaseModel, Field
from typing_extensions import TypedDict

from aip.models.innovation import DissensSignal, GateDecision
from aip.models.phase_output import PhaseAOutput, PhaseBOutput, PhaseCOutput
from aip.models.startup import DataMaturityLevel, StartupProfile


class AIPState(TypedDict):
    """The central state object for the AIP graph.

    LangGraph uses TypedDict for state definition. Each key is a channel
    that nodes can read/write. The `messages` channel uses the built-in
    reducer for append-only message history.
    """

    # --- Input ---
    startup: StartupProfile
    data_maturity: DataMaturityLevel

    # --- Phase outputs (populated as phases complete) ---
    phase_a: PhaseAOutput | None
    phase_b: PhaseBOutput | None
    phase_c: PhaseCOutput | None

    # --- OFH state ---
    current_phase: str  # "A", "B", "C", "D", "E"
    ofh_round: int  # current OFH voting round within a phase
    dissent_signals: list[DissensSignal]  # accumulated dissent signals

    # --- Gate decisions ---
    gates: list[GateDecision]

    # --- Message history (for agent conversations) ---
    messages: Annotated[list, add_messages]

    # --- Control flow ---
    should_continue: bool  # set to False to stop the cycle
    needs_human_input: bool  # pause for human-in-the-loop
    human_feedback: str  # human's response at a gate


def initial_state(profile: StartupProfile) -> AIPState:
    """Create the initial state from a startup profile."""
    return AIPState(
        startup=profile,
        data_maturity=profile.genome.data_maturity_level,
        phase_a=None,
        phase_b=None,
        phase_c=None,
        current_phase="A",
        ofh_round=0,
        dissent_signals=[],
        gates=[],
        messages=[],
        should_continue=True,
        needs_human_input=False,
        human_feedback="",
    )
