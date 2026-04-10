"""AIP Main Graph — LangGraph StateGraph orchestrating all phases.

This is the heart of the framework: a directed graph where each node
is a phase, edges are gate decisions, and the state flows through
with full checkpointing at every step.

Architecture:
    START → Phase A → Gate A→B → Phase B → Gate B→C → ... → Phase E → END
                ↑                                              |
                └──────────── Learning Loop ────────────────────┘
"""

from __future__ import annotations

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph

from aip.phases.erkennen import run_phase_a
from aip.state import AIPState


def should_continue_after_gate(state: AIPState) -> str:
    """Routing logic after a gate decision.

    If human input is needed (dissent signals, iterate decision),
    route to human-in-the-loop node. Otherwise, continue to next phase.
    """
    if state.get("needs_human_input"):
        return "human_review"

    current = state.get("current_phase", "A")
    phase_map = {
        "A": "phase_a",
        "B": "phase_b",
        "C": "phase_c",
        "D": "phase_d",
        "E": "phase_e",
    }
    return phase_map.get(current, END)


async def human_review_node(state: AIPState) -> dict:
    """Human-in-the-loop checkpoint.

    LangGraph pauses here. The state is persisted.
    When the human provides feedback, execution resumes.
    """
    # In interactive mode, this node signals a pause.
    # The graph runner checks needs_human_input and prompts the user.
    # After receiving feedback, the graph resumes with human_feedback populated.
    return {
        "needs_human_input": False,
        "human_feedback": state.get("human_feedback", ""),
    }


def build_graph() -> StateGraph:
    """Construct the AIP state graph.

    Currently implements Phase A fully.
    Phases B-E are stubs that will be implemented incrementally.
    """
    graph = StateGraph(AIPState)

    # -- Add nodes --
    graph.add_node("phase_a", run_phase_a)
    graph.add_node("human_review", human_review_node)

    # -- Add edges --
    # Start → Phase A
    graph.add_edge(START, "phase_a")

    # Phase A → conditional routing
    graph.add_conditional_edges(
        "phase_a",
        should_continue_after_gate,
        {
            "human_review": "human_review",
            "phase_b": END,  # Phase B not yet implemented → end for now
            END: END,
        },
    )

    # Human review → back to routing
    graph.add_conditional_edges(
        "human_review",
        should_continue_after_gate,
        {
            "phase_b": END,  # Will route to Phase B when implemented
            "phase_a": "phase_a",  # Re-run Phase A if gate said "iterate"
            END: END,
        },
    )

    return graph


def compile_graph(checkpointer: MemorySaver | None = None):
    """Compile the graph with optional checkpointing.

    Args:
        checkpointer: LangGraph checkpointer for state persistence.
                      If None, uses in-memory checkpointer.
    """
    graph = build_graph()

    if checkpointer is None:
        checkpointer = MemorySaver()

    return graph.compile(checkpointer=checkpointer)
