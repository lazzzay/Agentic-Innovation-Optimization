"""Tests for Pydantic domain models — the typed backbone of the AIP framework."""

import pytest
from pydantic import ValidationError

from aip.models.bmc import BMCBlock, BusinessModelCanvas
from aip.models.innovation import (
    DissensSignal,
    GateDecision,
    Hypothesis,
    InnovationClass,
    InnovationGap,
    Opportunity,
)
from aip.models.startup import DataMaturityLevel, StartupGenome, StartupProfile


# -- StartupGenome --


class TestStartupGenome:
    def test_it_score_calculation(self):
        genome = StartupGenome(
            structure=3, culture=2, founders=4, technology=3, market_image=3, data_maturity=3,
        )
        # Weighted: 3*0.10 + 2*0.20 + 4*0.15 + 3*0.20 + 3*0.10 + 3*0.25 = 2.95
        assert genome.it_score == 2.95

    def test_weakest_dimension(self):
        genome = StartupGenome(
            structure=3, culture=1, founders=4, technology=3, market_image=3, data_maturity=3,
        )
        assert genome.weakest_dimension == "culture"

    def test_data_maturity_level_mapping(self):
        cases = [
            (1, DataMaturityLevel.MINIMAL),
            (2, DataMaturityLevel.FRAGMENTED),
            (3, DataMaturityLevel.STRUCTURED),
            (4, DataMaturityLevel.DATA_DRIVEN),
            (5, DataMaturityLevel.DATA_DRIVEN),
        ]
        for score, expected in cases:
            genome = StartupGenome(
                structure=3, culture=3, founders=3, technology=3, market_image=3,
                data_maturity=score,
            )
            assert genome.data_maturity_level == expected, f"score={score}"

    def test_validation_rejects_out_of_range(self):
        with pytest.raises(ValidationError):
            StartupGenome(
                structure=0, culture=3, founders=3, technology=3, market_image=3, data_maturity=3,
            )
        with pytest.raises(ValidationError):
            StartupGenome(
                structure=3, culture=6, founders=3, technology=3, market_image=3, data_maturity=3,
            )

    def test_genome_serialization_includes_computed_fields(self):
        genome = StartupGenome(
            structure=3, culture=2, founders=4, technology=3, market_image=3, data_maturity=3,
        )
        data = genome.model_dump()
        assert "it_score" in data
        assert "weakest_dimension" in data
        assert "data_maturity_level" in data


# -- BusinessModelCanvas --


class TestBusinessModelCanvas:
    def test_summary(self):
        bmc = BusinessModelCanvas(
            value_propositions=BMCBlock(entries=["VP1", "VP2"]),
            customer_segments=BMCBlock(entries=["CS1"]),
            revenue_streams=BMCBlock(entries=["RS1", "RS2"]),
        )
        summary = bmc.summary()
        assert "VP1" in summary
        assert "CS1" in summary
        assert "RS1" in summary

    def test_all_weaknesses(self):
        bmc = BusinessModelCanvas(
            key_partners=BMCBlock(weaknesses=["W1"]),
            value_propositions=BMCBlock(weaknesses=["W2", "W3"]),
        )
        weaknesses = bmc.all_weaknesses()
        assert len(weaknesses) == 3
        assert any("[key_partners]" in w for w in weaknesses)

    def test_empty_bmc(self):
        bmc = BusinessModelCanvas()
        assert bmc.summary() == "Value Propositions: not defined. Customer Segments: not defined. Revenue Streams: not defined."
        assert bmc.all_weaknesses() == []


# -- Innovation Models --


class TestOpportunity:
    def test_opportunity_score_ulwick(self):
        opp = Opportunity(
            job_statement="Analyze data faster",
            importance=8.0,
            satisfaction=3.0,
            rationale="High importance, low satisfaction",
        )
        # Ulwick: 8 + max(0, 8-3) = 13.0
        assert opp.opportunity_score == 13.0

    def test_opportunity_score_when_satisfied(self):
        opp = Opportunity(
            job_statement="Send emails",
            importance=5.0,
            satisfaction=9.0,
            rationale="Already well served",
        )
        # Ulwick: 5 + max(0, 5-9) = 5 + 0 = 5.0
        assert opp.opportunity_score == 5.0

    def test_opportunity_score_serialized(self):
        opp = Opportunity(
            job_statement="Test",
            importance=8.0,
            satisfaction=3.0,
            rationale="test",
        )
        data = opp.model_dump()
        assert "opportunity_score" in data
        assert data["opportunity_score"] == 13.0


class TestDissensSignal:
    def test_basic_creation(self):
        signal = DissensSignal(
            topic="Market direction",
            positions={"agent_a": "Go B2C", "agent_b": "Stay B2B"},
            divergence_score=0.8,
            innovation_potential="Hybrid B2B2C model might be unexplored",
            recommended_action="Evaluate B2B2C positioning",
        )
        assert signal.divergence_score == 0.8
        assert len(signal.positions) == 2


class TestGateDecision:
    def test_gate_go(self):
        gate = GateDecision(
            gate="A→B", decision="go", rationale="Strong analysis", confidence=0.85,
        )
        assert gate.decision == "go"
        assert gate.dissent_signals == []

    def test_gate_rejects_invalid_decision(self):
        with pytest.raises(ValidationError):
            GateDecision(
                gate="A→B", decision="maybe", rationale="Uncertain", confidence=0.5,
            )


class TestHypothesis:
    def test_hypothesis_creation(self):
        hyp = Hypothesis(
            statement="We believe SMBs will adopt AI analytics if we offer self-service",
            target_customer="SMB marketing teams",
            expected_outcome="20% conversion from trial",
            success_metric="Trial-to-paid conversion rate",
            innovation_class=InnovationClass.PROGRESSIVE,
            risk_level="medium",
            confidence=0.6,
        )
        assert hyp.innovation_class == InnovationClass.PROGRESSIVE


# -- StartupProfile --


class TestStartupProfile:
    def test_full_profile(self):
        profile = StartupProfile(
            name="TestCo",
            industry="SaaS",
            stage="seed",
            employees=10,
            description="A test startup",
            genome=StartupGenome(
                structure=3, culture=3, founders=3, technology=3,
                market_image=3, data_maturity=3,
            ),
            available_data=["crm", "analytics"],
            current_challenges=["Stagnation"],
            past_innovations=[],
            strategic_goals=["Growth"],
        )
        assert profile.genome.it_score == 3.0
        assert profile.genome.data_maturity_level == DataMaturityLevel.STRUCTURED

    def test_profile_minimal(self):
        profile = StartupProfile(
            name="MinCo",
            industry="Tech",
            stage="pre-seed",
            employees=1,
            description="Minimal",
            genome=StartupGenome(
                structure=1, culture=1, founders=1, technology=1,
                market_image=1, data_maturity=1,
            ),
        )
        assert profile.genome.it_score == 1.0
