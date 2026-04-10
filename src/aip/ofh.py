"""Orchestrated Feedback Hierarchy (OFH) — the core governance mechanism.

OFH implements a democratic agent coordination model:
1. Multiple agents analyze the same situation independently
2. A spokesperson agent synthesizes all positions
3. Dissent is detected and treated as innovation signal
4. Gate decisions are made based on synthesis + dissent analysis

This is AIP's primary contribution to multi-agent governance.
"""

from __future__ import annotations

import json
import logging
from typing import Any

from langchain_core.messages import HumanMessage, SystemMessage

from aip.agents.base import get_model
from aip.config import ModelTier, settings
from aip.models.innovation import DissensSignal, GateDecision
from aip.utils import LLMOutputParseError, extract_json

logger = logging.getLogger(__name__)


OFH_SPOKESPERSON_PROMPT = """\
You are the OFH Spokesperson — the synthesizer in the Orchestrated Feedback Hierarchy.

Your role:
1. Review all agent positions on the current topic
2. Identify areas of CONSENSUS (where agents agree)
3. Identify areas of DISSENT (where agents fundamentally disagree)
4. For each dissent: assess whether it might be an INNOVATION SIGNAL
5. Synthesize a recommendation for the gate decision

CRITICAL RULE — Dissent-as-Innovation-Signal:
When agents fundamentally disagree, do NOT simply pick the majority view.
Instead, flag the disagreement as a potential innovation opportunity.
Fundamental disagreements often reveal unexplored territory.

You must output valid JSON matching the provided schema.
"""

DISSENT_DETECTOR_PROMPT = """\
You are the Dissent Detector in the OFH system.

Analyze the agent positions below and identify fundamental disagreements.
A disagreement is "fundamental" when agents reach opposite conclusions
based on different interpretations of the same data.

For each fundamental disagreement:
- Describe the topic
- State each agent's position
- Score the divergence (0 = minor nuance, 1 = complete opposition)
- Explain why this disagreement might point to an innovation opportunity

Trivial disagreements (wording differences, minor emphasis shifts) should
be IGNORED. Only flag disagreements that a human decision-maker would
benefit from examining.

You must output valid JSON: a list of DissensSignal objects.
"""


async def detect_dissent(
    agent_outputs: dict[str, Any],
    phase: str,
    dissent_threshold: float | None = None,
) -> list[DissensSignal]:
    """Analyze multiple agent outputs for fundamental disagreements.

    Args:
        agent_outputs: Mapping of agent_name → their output/analysis
        phase: Current phase identifier (for context)
        dissent_threshold: Minimum divergence score to keep (from config if None)

    Returns:
        List of detected dissent signals (may be empty if agents agree)
    """
    if len(agent_outputs) < 2:
        return []

    if dissent_threshold is None:
        dissent_threshold = settings.dissent_threshold

    context = (
        f"Phase: {phase}\n\n"
        f"Agent Positions:\n"
        + "\n---\n".join(
            f"**{name}**:\n{json.dumps(output, indent=2, default=str, ensure_ascii=False)}"
            for name, output in agent_outputs.items()
        )
    )

    schema = {
        "type": "array",
        "items": DissensSignal.model_json_schema(),
    }

    model = get_model(ModelTier.CRITIQUE)

    response = await model.ainvoke([
        SystemMessage(
            content=DISSENT_DETECTOR_PROMPT
            + f"\n\nOutput JSON schema:\n```json\n{json.dumps(schema, indent=2)}\n```\n"
            + "Respond ONLY with a JSON array."
        ),
        HumanMessage(content=context),
    ])

    try:
        raw = str(response.content)
        parsed = extract_json(raw)
        items = json.loads(parsed)
    except (json.JSONDecodeError, LLMOutputParseError) as e:
        logger.warning("Dissent detection JSON parse failed: %s — returning empty", e)
        return []

    signals = [DissensSignal.model_validate(item) for item in items]

    # Filter by threshold from config
    return [s for s in signals if s.divergence_score >= dissent_threshold]


async def spokesperson_synthesis(
    agent_outputs: dict[str, Any],
    dissent_signals: list[DissensSignal],
    phase: str,
    gate_name: str,
) -> GateDecision:
    """Spokesperson synthesizes all positions into a gate decision.

    This is the democratic core of OFH: no single agent decides alone.
    The spokesperson weighs all inputs and produces a recommendation.

    Args:
        agent_outputs: All agent analyses for this phase
        dissent_signals: Detected dissent signals
        phase: Current phase
        gate_name: Gate identifier (e.g., "A→B")

    Returns:
        Gate decision with rationale and attached dissent signals
    """
    dissent_section = ""
    if dissent_signals:
        dissent_section = (
            "\n\n## Detected Dissent Signals\n"
            + "\n".join(
                f"- **{d.topic}** (divergence: {d.divergence_score}): {d.innovation_potential}"
                for d in dissent_signals
            )
        )

    context = (
        f"Phase: {phase}\nGate: {gate_name}\n\n"
        f"## Agent Analyses\n"
        + "\n---\n".join(
            f"**{name}**:\n{json.dumps(output, indent=2, default=str, ensure_ascii=False)}"
            for name, output in agent_outputs.items()
        )
        + dissent_section
    )

    schema_json = json.dumps(GateDecision.model_json_schema(), indent=2)

    model = get_model(ModelTier.CRITIQUE)

    response = await model.ainvoke([
        SystemMessage(
            content=OFH_SPOKESPERSON_PROMPT
            + f"\n\nOutput JSON schema:\n```json\n{schema_json}\n```\n"
            + "Respond ONLY with the JSON object."
        ),
        HumanMessage(content=context),
    ])

    try:
        raw = str(response.content)
        text = extract_json(raw)
        decision = GateDecision.model_validate_json(text)
    except (json.JSONDecodeError, ValueError, LLMOutputParseError) as e:
        logger.error("Spokesperson synthesis JSON parse failed: %s", e)
        # Fallback: create a conservative "iterate" decision
        decision = GateDecision(
            gate=gate_name,
            decision="iterate",
            rationale=f"Automatic fallback — spokesperson output could not be parsed: {e}",
            confidence=0.0,
        )

    decision.dissent_signals = dissent_signals
    return decision


async def ethical_friction_check(
    agent_outputs: dict[str, Any],
    phase: str,
) -> str | None:
    """L6: Ethical Friction — when all agents agree too easily, raise questions.

    If consensus is ~100%, the system generates structured reflection
    questions. Not a veto — a thought impulse to prevent groupthink.

    Returns:
        Reflection questions string, or None if consensus isn't suspicious.
    """
    dissent = await detect_dissent(agent_outputs, phase, dissent_threshold=0.2)

    # If there's meaningful dissent, friction isn't needed
    if dissent:
        return None

    # Full consensus → generate reflection questions
    model = get_model(ModelTier.CRITIQUE)

    response = await model.ainvoke([
        SystemMessage(
            content=(
                "You are the Ethical Friction mechanism in the AIP framework.\n"
                "All agents have reached near-complete consensus. This is suspicious.\n"
                "Generate 2-3 provocative reflection questions that challenge the consensus.\n"
                "These are NOT vetoes — they are thought impulses for the human decision-maker.\n"
                "Focus on blind spots, unstated assumptions, and unexplored alternatives."
            )
        ),
        HumanMessage(
            content=f"Phase: {phase}\n\nConsensus position:\n"
            + json.dumps(
                {k: str(v)[:500] for k, v in agent_outputs.items()},
                indent=2,
                ensure_ascii=False,
            )
        ),
    ])

    return str(response.content)
