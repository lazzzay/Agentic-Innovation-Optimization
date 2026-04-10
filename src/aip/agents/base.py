"""Base agent — foundation for all AIP agents.

Each agent is a thin wrapper around a LangChain ChatModel call with:
- A role-specific system prompt (loaded from prompts/ directory)
- A Pydantic output schema for structured, validated responses
- Model tier routing (cheap models for simple tasks, strong for reasoning)
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import TypeVar

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import HumanMessage, SystemMessage
from pydantic import BaseModel

from aip.config import LLMProvider, ModelTier, settings
from aip.utils import LLMOutputParseError, extract_json

logger = logging.getLogger(__name__)

T = TypeVar("T", bound=BaseModel)

PROMPTS_DIR = Path(__file__).parent / "prompts"

MAX_RETRIES = 2


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

    Includes retry logic: if JSON parsing fails, the agent is called again
    with an error hint (up to MAX_RETRIES attempts).

    Args:
        agent_name: Name matching a file in prompts/ (e.g., "audit" → prompts/audit.md)
        tier: Model tier for cost/quality routing
        context: The input data the agent works with
        output_schema: Pydantic model class for structured output
        additional_instructions: Extra context (e.g., data maturity adjustments)

    Returns:
        Validated Pydantic model instance

    Raises:
        LLMOutputParseError: If all retry attempts fail
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
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=context),
    ]

    last_error: Exception | None = None

    for attempt in range(1, MAX_RETRIES + 1):
        response = await model.ainvoke(messages)

        raw_text = str(response.content)
        if isinstance(response.content, list):
            raw_text = response.content[0].get("text", "") if response.content else ""

        try:
            text = extract_json(raw_text)
            return output_schema.model_validate_json(text)
        except (json.JSONDecodeError, ValueError, LLMOutputParseError) as e:
            last_error = e
            logger.warning(
                "Agent '%s' attempt %d/%d: JSON parse failed — %s",
                agent_name, attempt, MAX_RETRIES, e,
            )
            if attempt < MAX_RETRIES:
                # Add error feedback so the LLM can self-correct
                messages.append(response)
                messages.append(HumanMessage(
                    content=(
                        f"Your previous response was not valid JSON. Error: {e}\n"
                        f"Please respond ONLY with a valid JSON object matching the schema."
                    )
                ))

    raise LLMOutputParseError(raw_text, f"agent={agent_name}") from last_error
