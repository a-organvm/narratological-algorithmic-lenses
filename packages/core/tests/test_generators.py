"""Tests for report generators.

Tests cover:
- Base generator classes and configuration
- Beat map report generation
- Structural report generation
- Character atlas report generation
- Coverage report generation
"""

import pytest

from narratological.generators import (
    BeatMapReportGenerator,
    CharacterAtlasReportGenerator,
    CoverageReportGenerator,
    GeneratorConfig,
    GeneratorError,
    ReportType,
    StructuralReportGenerator,
)
from narratological.llm import MockProvider
from narratological.models.analysis import (
    ArcClassification,
    BeatFunction,
    Character,
    ConnectorType,
    Scene,
    Script,
)
from narratological.models.report import (
    BeatMapReport,
    CharacterAtlasReport,
    CoverageReport,
    RecommendationType,
    StructuralReport,
)

# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def simple_script():
    """Create a simple script for testing."""
    return Script(
        title="Test Script",
        format="Feature",
        page_count=100,
        primary_genre="Drama",
        tone="Serious",
        logline="A test script for unit testing.",
        scenes=[
            Scene(
                number=1,
                slug="INT. HOUSE - DAY",
                summary="We meet the protagonist",
                function=BeatFunction.SETUP,
                characters_present=["JOHN", "MARY"],
                connector_to_next=ConnectorType.THEREFORE,
                tension_level=3,
            ),
            Scene(
                number=2,
                slug="EXT. STREET - DAY",
                summary="The inciting incident occurs",
                function=BeatFunction.INCITE,
                characters_present=["JOHN"],
                connector_to_next=ConnectorType.BUT,
                tension_level=6,
            ),
            Scene(
                number=3,
                slug="INT. OFFICE - DAY",
                summary="Complications arise",
                function=BeatFunction.COMPLICATE,
                characters_present=["JOHN", "BOSS"],
                connector_to_next=ConnectorType.THEREFORE,
                tension_level=7,
            ),
            Scene(
                number=4,
                slug="INT. HOUSE - NIGHT",
                summary="The climax",
                function=BeatFunction.CLIMAX,
                characters_present=["JOHN", "MARY"],
                connector_to_next=ConnectorType.THEREFORE,
                tension_level=10,
            ),
            Scene(
                number=5,
                slug="EXT. PARK - DAY",
                summary="Resolution",
                function=BeatFunction.RESOLVE,
                characters_present=["JOHN", "MARY"],
                tension_level=4,
            ),
        ],
        characters=[
            Character(
                name="JOHN",
                role="protagonist",
                description="A man facing challenges",
                first_appearance=1,
                want="To succeed at work",
                need="To prioritize family",
                lie="Success equals happiness",
                truth="Family is what matters",
                arc_classification=ArcClassification.POSITIVE,
            ),
            Character(
                name="MARY",
                role="ally",
                description="John's supportive wife",
                first_appearance=1,
            ),
            Character(
                name="BOSS",
                role="antagonist",
                description="John's demanding boss",
                first_appearance=3,
            ),
        ],
    )


@pytest.fixture
def mock_provider():
    """Create a mock LLM provider."""
    return MockProvider()


@pytest.fixture
def config():
    """Create default generator config."""
    return GeneratorConfig()


# =============================================================================
# Test GeneratorConfig
# =============================================================================


class TestGeneratorConfig:
    """Tests for GeneratorConfig."""

    def test_default_values(self):
        """Test default configuration values."""
        config = GeneratorConfig()
        assert config.temperature == 0.7
        assert config.max_retries == 3
        assert config.include_role_notes is True
        assert config.causal_binding_target == 0.80

    def test_custom_values(self):
        """Test custom configuration values."""
        config = GeneratorConfig(
            temperature=0.5,
            causal_binding_target=0.90,
            include_role_notes=False,
        )
        assert config.temperature == 0.5
        assert config.causal_binding_target == 0.90
        assert config.include_role_notes is False


# =============================================================================
# Test ReportType
# =============================================================================


class TestReportType:
    """Tests for ReportType enum."""

    def test_report_types(self):
        """Test all report type values."""
        assert ReportType.COVERAGE.value == "coverage"
        assert ReportType.BEAT_MAP.value == "beat_map"
        assert ReportType.STRUCTURAL.value == "structural"
        assert ReportType.CHARACTER_ATLAS.value == "character_atlas"
        assert ReportType.DIAGNOSTIC.value == "diagnostic"


# =============================================================================
# Test BeatMapReportGenerator
# =============================================================================


class TestBeatMapReportGenerator:
    """Tests for BeatMapReportGenerator."""

    def test_generator_report_type(self):
        """Test generator has correct report type."""
        gen = BeatMapReportGenerator()
        assert gen.report_type == ReportType.BEAT_MAP

    def test_generate_from_annotations(self, simple_script):
        """Test generation from annotated scenes."""
        gen = BeatMapReportGenerator()
        report = gen.generate(simple_script)

        assert isinstance(report, BeatMapReport)
        assert report.title == "Test Script"
        assert report.total_scenes == 5
        assert len(report.entries) == 5

    def test_beat_functions_preserved(self, simple_script):
        """Test that beat functions are preserved from annotations."""
        gen = BeatMapReportGenerator()
        report = gen.generate(simple_script)

        functions = [e.function for e in report.entries]
        assert BeatFunction.SETUP in functions
        assert BeatFunction.INCITE in functions
        assert BeatFunction.CLIMAX in functions

    def test_connectors_preserved(self, simple_script):
        """Test that connectors are preserved from annotations."""
        gen = BeatMapReportGenerator()
        report = gen.generate(simple_script)

        connectors = [e.connector for e in report.entries if e.connector]
        assert ConnectorType.THEREFORE in connectors
        assert ConnectorType.BUT in connectors

    def test_function_distribution(self, simple_script):
        """Test function distribution calculation."""
        gen = BeatMapReportGenerator()
        report = gen.generate(simple_script)

        assert "SETUP" in report.function_distribution
        assert "CLIMAX" in report.function_distribution

    def test_connector_distribution(self, simple_script):
        """Test connector distribution calculation."""
        gen = BeatMapReportGenerator()
        report = gen.generate(simple_script)

        # 4 scenes have connectors
        total_connectors = sum(report.connector_distribution.values())
        assert total_connectors == 4

    def test_average_tension(self, simple_script):
        """Test average tension calculation."""
        gen = BeatMapReportGenerator()
        report = gen.generate(simple_script)

        assert report.average_tension is not None
        assert 1.0 <= report.average_tension <= 10.0

    def test_causal_binding_ratio(self, simple_script):
        """Test causal binding ratio method."""
        gen = BeatMapReportGenerator()
        report = gen.generate(simple_script)

        # 3 THEREFORE + 1 BUT = 4 causal, 0 AND_THEN
        ratio = report.calculate_causal_binding_ratio()
        assert ratio == 1.0  # All causal

    def test_generate_with_llm(self, simple_script, mock_provider):
        """Test generation with LLM provider."""
        mock_provider.set_response(
            "",
            structured_data={
                "entries": [
                    {
                        "scene_number": 1,
                        "function": "SETUP",
                        "connector": "THEREFORE",
                        "tension": 3,
                    }
                ],
                "function_distribution": {"SETUP": 1},
                "connector_distribution": {"THEREFORE": 1},
                "average_tension": 3.0,
            },
        )

        # Create script without annotations
        script = Script(
            title="Unannotated Script",
            scenes=[
                Scene(number=1, slug="INT. ROOM", summary="Scene one"),
            ],
        )

        gen = BeatMapReportGenerator(provider=mock_provider)
        _report = gen.generate(script)

        assert len(mock_provider.get_calls()) == 1

    def test_can_generate_validation(self):
        """Test validation of script prerequisites."""
        gen = BeatMapReportGenerator()
        script = Script(title="")  # Empty title

        can_gen, errors = gen.can_generate(script)
        assert not can_gen
        assert any("title" in e.lower() for e in errors)


# =============================================================================
# Test StructuralReportGenerator
# =============================================================================


class TestStructuralReportGenerator:
    """Tests for StructuralReportGenerator."""

    def test_generator_report_type(self):
        """Test generator has correct report type."""
        gen = StructuralReportGenerator()
        assert gen.report_type == ReportType.STRUCTURAL

    def test_requires_llm_or_annotations(self, simple_script):
        """Test that structural report needs LLM or act annotations."""
        gen = StructuralReportGenerator()

        # Script has no acts and no LLM - should raise
        with pytest.raises(GeneratorError):
            gen.generate(simple_script)

    def test_generate_with_llm(self, simple_script, mock_provider):
        """Test generation with LLM provider."""
        mock_provider.set_response(
            "",
            structured_data={
                "structure_type": "Three-Act",
                "act_count": 3,
                "acts": [
                    {
                        "number": 1,
                        "start_scene": 1,
                        "end_scene": 2,
                        "percentage": 0.40,
                        "summary": "Setup",
                        "key_events": ["Introduction"],
                    },
                    {
                        "number": 2,
                        "start_scene": 3,
                        "end_scene": 4,
                        "percentage": 0.40,
                        "summary": "Confrontation",
                        "key_events": ["Complications"],
                    },
                    {
                        "number": 3,
                        "start_scene": 5,
                        "end_scene": 5,
                        "percentage": 0.20,
                        "summary": "Resolution",
                        "key_events": ["Ending"],
                    },
                ],
                "inciting_incident": 2,
                "climax": 4,
                "act_proportions": [0.40, 0.40, 0.20],
                "pacing_notes": "Good pacing",
                "structural_issues": [],
            },
        )

        gen = StructuralReportGenerator(provider=mock_provider)
        report = gen.generate(simple_script)

        assert isinstance(report, StructuralReport)
        assert report.act_count == 3
        assert report.inciting_incident == 2
        assert report.climax == 4


# =============================================================================
# Test CharacterAtlasReportGenerator
# =============================================================================


class TestCharacterAtlasReportGenerator:
    """Tests for CharacterAtlasReportGenerator."""

    def test_generator_report_type(self):
        """Test generator has correct report type."""
        gen = CharacterAtlasReportGenerator()
        assert gen.report_type == ReportType.CHARACTER_ATLAS

    def test_generate_from_annotations(self, simple_script):
        """Test generation from annotated characters."""
        gen = CharacterAtlasReportGenerator()
        report = gen.generate(simple_script)

        assert isinstance(report, CharacterAtlasReport)
        assert report.title == "Test Script"
        assert report.total_characters == 3

    def test_protagonist_identification(self, simple_script):
        """Test protagonist is correctly identified."""
        gen = CharacterAtlasReportGenerator()
        report = gen.generate(simple_script)

        assert report.protagonist == "JOHN"

    def test_want_need_preserved(self, simple_script):
        """Test Want/Need/Lie/Truth are preserved."""
        gen = CharacterAtlasReportGenerator()
        report = gen.generate(simple_script)

        john_entry = next(e for e in report.entries if e.name == "JOHN")
        assert john_entry.want == "To succeed at work"
        assert john_entry.need == "To prioritize family"
        assert john_entry.lie == "Success equals happiness"
        assert john_entry.truth == "Family is what matters"

    def test_arc_type_preserved(self, simple_script):
        """Test arc classification is preserved."""
        gen = CharacterAtlasReportGenerator()
        report = gen.generate(simple_script)

        john_entry = next(e for e in report.entries if e.name == "JOHN")
        assert john_entry.arc_type == ArcClassification.POSITIVE

    def test_screen_time_calculation(self, simple_script):
        """Test screen time calculation."""
        gen = CharacterAtlasReportGenerator()
        report = gen.generate(simple_script)

        john_entry = next(e for e in report.entries if e.name == "JOHN")
        # John appears in all 5 scenes
        assert john_entry.screen_time == 1.0

        mary_entry = next(e for e in report.entries if e.name == "MARY")
        # Mary appears in 3 of 5 scenes
        assert mary_entry.screen_time == 0.6


# =============================================================================
# Test CoverageReportGenerator
# =============================================================================


class TestCoverageReportGenerator:
    """Tests for CoverageReportGenerator."""

    def test_generator_report_type(self):
        """Test generator has correct report type."""
        gen = CoverageReportGenerator()
        assert gen.report_type == ReportType.COVERAGE

    def test_requires_llm(self, simple_script):
        """Test that coverage report requires LLM."""
        gen = CoverageReportGenerator()

        with pytest.raises(GeneratorError, match="LLM"):
            gen.generate(simple_script)

    def test_generate_with_llm(self, simple_script, mock_provider):
        """Test generation with LLM provider."""
        mock_provider.set_response(
            "",
            structured_data={
                "logline": "A man learns to prioritize family",
                "synopsis": "John struggles with work-life balance.",
                "recommendation": "CONSIDER",
                "premise_rating": 7,
                "structure_rating": 8,
                "character_rating": 7,
                "dialogue_rating": 6,
                "originality_rating": 6,
                "marketability_rating": 7,
                "strengths": ["Strong character arc"],
                "weaknesses": ["Dialogue needs work"],
                "opportunities": ["Add subplots"],
                "comparables": ["Film A", "Film B"],
            },
        )

        gen = CoverageReportGenerator(
            provider=mock_provider,
            config=GeneratorConfig(include_role_notes=False),
        )
        report = gen.generate(simple_script, include_role_notes=False)

        assert isinstance(report, CoverageReport)
        assert report.title == "Test Script"
        assert report.recommendation == RecommendationType.CONSIDER
        assert report.premise_rating == 7
        assert "Strong character arc" in report.strengths

    def test_overall_score_calculation(self, mock_provider):
        """Test overall score weighted calculation."""
        mock_provider.set_response(
            "",
            structured_data={
                "logline": "Test",
                "synopsis": "Test",
                "recommendation": "CONSIDER",
                "premise_rating": 10,
                "structure_rating": 10,
                "character_rating": 10,
                "dialogue_rating": 10,
                "originality_rating": 10,
                "marketability_rating": 10,
                "strengths": [],
                "weaknesses": [],
                "opportunities": [],
                "comparables": [],
            },
        )

        script = Script(title="Test", scenes=[])
        gen = CoverageReportGenerator(
            provider=mock_provider,
            config=GeneratorConfig(include_role_notes=False),
        )
        report = gen.generate(script, include_role_notes=False)

        # All 10s should give perfect score
        assert report.overall_score() == 10.0


# =============================================================================
# Test GeneratorError
# =============================================================================


class TestGeneratorError:
    """Tests for GeneratorError."""

    def test_error_message(self):
        """Test error message."""
        error = GeneratorError("Test error")
        assert str(error) == "Test error"

    def test_error_with_report_type(self):
        """Test error with report type."""
        error = GeneratorError("Test error", report_type=ReportType.COVERAGE)
        assert error.report_type == ReportType.COVERAGE

    def test_error_with_cause(self):
        """Test error with underlying cause."""
        cause = ValueError("Original error")
        error = GeneratorError("Wrapper error", cause=cause)
        assert error.cause == cause
