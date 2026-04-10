"""Base agent — foundation for all AIP agents.

Each agent is a thin wrapper around a LangChain ChatModel call with:
- A role-specific system prompt (loaded from prompts/ directory)
- A Pydantic output schema for structured, validated responses
- Model tier routing (cheap models for simple tasks, strong for reasoning)
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import TypeVar

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import HumanMessage, SystemMessage
from pydantic import BaseModel

from aip.config import LLMProvider, ModelTier, settings

T = TypeVar("T", bound=BaseModel)

PROMPTS_DIR = Path(__file__).parent / "prompts"


def load_prompt(agent_name: str) -> str:
    """Load system prompt from prompts/ directory."""
    prompt_file = PROMPTS_DIR / f"{agent_name}.md"
    if not prompt_file.exists():
        raise FileNotFoundError(
            f"No prompt found for agent '{agent_name}' at {prompt_file}"
        )
    return prompt_file.read_text(encoding="utf-8")


def get_model(tier: ModelTier) -> BaseChatModel:
    """Get a chat model for the given tier — provider-agnostic.

    The AIP framework is LLM-agnostic. This factory returns the right
    LangChain model class based on the configured provider.
    """
    model_name = settings.get_model(tier)
    temperature = 0.3 if tier == ModelTier.REASONING else 0.1

    if settings.provider == LLMProvider.ANTHROPIC:
        from langchain_anthropic import ChatAnthropic

        return ChatAnthropic(
            model=model_name,
            api_key=settings.anthropic_api_key,
            max_tokens=4096,
            temperature=temperature,
        )

    if settings.provider == LLMProvider.OPENAI:
        from langchain_openai import ChatOpenAI

        return ChatOpenAI(
            model=model_name,
            api_key=settings.openai_api_key,
            max_tokens=4096,
            temperature=temperature,
        )

    if settings.provider == LLMProvider.GOOGLE:
        from langchain_google_genai import ChatGoogleGenerativeAI

        return ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=settings.google_api_key,
            max_output_tokens=4096,
            temperature=temperature,
        )

    if settings.provider == LLMProvider.OLLAMA:
        from langchain_ollama import ChatOllama

        return ChatOllama(
            model=model_name,
            base_url=settings.ollama_base_url,
            temperature=temperature,
        )

    raise ValueError(f"Unsupported provider: {settings.provider}")


async def run_agent(
    agent_name: str,
    tier: ModelTier,
    context: str,
    output_schema: type[T],
    additional_instructions: str = "",
) -> T:
    """Run a single agent and return a typed, validated output.

    Args:
        agent_name: Name matching a file in prompts/ (e.g., "audit" → prompts/audit.md)
        tier: Model tier for cost/quality routing
        context: The input data the agent works with
        output_schema: Pydantic model class for structured output
        additional_instructions: Extra context (e.g., data maturity adjustments)

    Returns:
        Validated Pydantic model instance
    """
    system_prompt = load_prompt(agent_name)

    if additional_instructions:
        system_prompt += f"\n\n## Additional Context\n{additional_instructions}"

    # Instruct the model to return valid JSON matching the schema
    schema_json = json.dumps(output_schema.model_json_schema(), indent=2)
    system_prompt += (
        f"\n\n## Output Format\n"
        f"You MUST respond with a valid JSON object matching this schema:\n"
        f"```json\n{schema_json}\n```\n"
        f"Respond ONLY with the JSON object, no other text."
    )

    model = get_model(tier)
    response = await model.ainvoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=context),
    ])

    # Parse and validate the response
    raw_text = response.content
    if isinstance(raw_text, list):
        raw_text = raw_text[0]["text"] if raw_text else ""

    # Extract JSON from potential markdown code blocks
    text = str(raw_text).strip()
    if text.startswith("```"):
        lines = text.split("\n")
        text = "\n".join(lines[1:-1])

    return output_schema.model_validate_json(text)
