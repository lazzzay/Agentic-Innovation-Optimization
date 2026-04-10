"""AIP configuration — model routing, API keys, runtime settings.

The framework is LLM-agnostic. Set AIP_PROVIDER in .env to switch:
  - "anthropic" (default) → Claude models
  - "openai" → GPT models
  - "google" → Gemini models
  - "ollama" → Local open-source models
"""

from __future__ import annotations

from enum import Enum
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


class ModelTier(str, Enum):
    """Model tiering for cost/quality optimization."""

    ROUTING = "routing"  # cheap + fast: classification, routing, simple extraction
    REASONING = "reasoning"  # strong: innovation analysis, synthesis, evaluation
    CRITIQUE = "critique"  # strongest: OFH voting, dissent detection, gate decisions


class LLMProvider(str, Enum):
    """Supported LLM providers — the framework is provider-agnostic."""

    ANTHROPIC = "anthropic"
    OPENAI = "openai"
    GOOGLE = "google"
    OLLAMA = "ollama"


# Default models per provider and tier
PROVIDER_DEFAULTS: dict[LLMProvider, dict[ModelTier, str]] = {
    LLMProvider.ANTHROPIC: {
        ModelTier.ROUTING: "claude-haiku-4-5-20251001",
        ModelTier.REASONING: "claude-sonnet-4-6",
        ModelTier.CRITIQUE: "claude-sonnet-4-6",
    },
    LLMProvider.OPENAI: {
        ModelTier.ROUTING: "gpt-4o-mini",
        ModelTier.REASONING: "gpt-4o",
        ModelTier.CRITIQUE: "gpt-4o",
    },
    LLMProvider.GOOGLE: {
        ModelTier.ROUTING: "gemini-2.0-flash",
        ModelTier.REASONING: "gemini-2.5-pro",
        ModelTier.CRITIQUE: "gemini-2.5-pro",
    },
    LLMProvider.OLLAMA: {
        ModelTier.ROUTING: "llama3.2",
        ModelTier.REASONING: "llama3.3:70b",
        ModelTier.CRITIQUE: "llama3.3:70b",
    },
}


class Settings(BaseSettings):
    """Runtime configuration. Reads from .env or environment variables."""

    model_config = {"env_file": str(PROJECT_ROOT / ".env"), "env_prefix": "AIP_"}

    # Provider selection
    provider: LLMProvider = Field(
        default=LLMProvider.ANTHROPIC,
        description="LLM provider (anthropic, openai, google, ollama)",
    )

    # API keys (only the relevant one needs to be set)
    anthropic_api_key: str = Field(default="", description="Anthropic API key")
    openai_api_key: str = Field(default="", description="OpenAI API key")
    google_api_key: str = Field(default="", description="Google AI API key")
    ollama_base_url: str = Field(
        default="http://localhost:11434", description="Ollama server URL"
    )

    # Model overrides (optional — defaults from PROVIDER_DEFAULTS)
    model_routing: str = Field(default="", description="Override routing model")
    model_reasoning: str = Field(default="", description="Override reasoning model")
    model_critique: str = Field(default="", description="Override critique model")

    # Runtime
    checkpoint_dir: Path = Field(default=PROJECT_ROOT / "checkpoints")
    output_dir: Path = Field(default=PROJECT_ROOT / "outputs")
    max_ofh_rounds: int = Field(default=3, description="Max OFH voting rounds before escalation")
    dissent_threshold: float = Field(
        default=0.3, description="Divergence threshold for dissent-as-innovation-signal"
    )

    # Human-in-the-Loop
    auto_approve_gates: bool = Field(
        default=False, description="Skip human approval at gates (for batch runs)"
    )

    def get_model(self, tier: ModelTier) -> str:
        """Get model name for a given tier (respects overrides)."""
        # Check for explicit override first
        overrides = {
            ModelTier.ROUTING: self.model_routing,
            ModelTier.REASONING: self.model_reasoning,
            ModelTier.CRITIQUE: self.model_critique,
        }
        if overrides[tier]:
            return overrides[tier]

        # Fall back to provider defaults
        return PROVIDER_DEFAULTS[self.provider][tier]

    def get_api_key(self) -> str:
        """Get the API key for the configured provider."""
        mapping = {
            LLMProvider.ANTHROPIC: self.anthropic_api_key,
            LLMProvider.OPENAI: self.openai_api_key,
            LLMProvider.GOOGLE: self.google_api_key,
            LLMProvider.OLLAMA: "",  # Ollama doesn't need an API key
        }
        return mapping[self.provider]


settings = Settings()
