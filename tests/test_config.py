"""Tests for configuration and model routing."""

from aip.config import LLMProvider, ModelTier, PROVIDER_DEFAULTS, Settings


class TestModelTiering:
    def test_all_providers_have_all_tiers(self):
        for provider in LLMProvider:
            for tier in ModelTier:
                assert tier in PROVIDER_DEFAULTS[provider], (
                    f"Missing {tier} for {provider}"
                )

    def test_get_model_defaults(self):
        s = Settings(provider=LLMProvider.ANTHROPIC)
        assert "claude" in s.get_model(ModelTier.REASONING).lower()

    def test_get_model_override(self):
        s = Settings(provider=LLMProvider.ANTHROPIC, model_reasoning="custom-model")
        assert s.get_model(ModelTier.REASONING) == "custom-model"

    def test_get_api_key_ollama_empty(self):
        s = Settings(provider=LLMProvider.OLLAMA)
        assert s.get_api_key() == ""

    def test_dissent_threshold_default(self):
        s = Settings()
        assert s.dissent_threshold == 0.3
