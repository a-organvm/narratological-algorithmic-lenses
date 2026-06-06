"""Tests for the 8-role analyst system.

Tests cover:
- Analyst role enumeration
- Individual analyst implementations
- Multi-role orchestration
- Synthesis and aggregation
"""

import pytest

from narratological.llm import (
    BaseAnalyst,
    MockProvider,
    MultiRoleOrchestrator,
    get_all_analysts,
    get_analyst,
)
from narratological.models.analysis import Scene, Script
from narratological.models.analyst import (
    ROLE_STUDY_MAPPING,
    ActivationLayer,
    AnalystContext,
    AnalystObservation,
    AnalystRole,
    MultiRoleAnalysis,
    RoleAnalysisResult,
    SynthesisConfig,
)

# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def mock_provider():
    """Create a mock LLM provider."""
    return MockProvider()


@pytest.fixture
def simple_context():
    """Create a simple analysis context."""
    return AnalystContext(
        title="Test Script",
        text="A story about transformation and growth.",
        genre="Drama",
        tone="Serious",
        format="Feature",
        scene_summaries=[
            "Introduction of protagonist",
            "Inciting incident occurs",
            "Rising action",
            "Climax",
            "Resolution",
        ],
        character_list=["JOHN", "MARY", "BOSS"],
    )


@pytest.fixture
def simple_script():
    """Create a simple script for testing."""
    return Script(
        title="Test Script",
        format="Feature",
        primary_genre="Drama",
        tone="Serious",
        scenes=[
            Scene(number=1, slug="INT. HOUSE", summary="Introduction"),
            Scene(number=2, slug="EXT. STREET", summary="Inciting incident"),
        ],
    )


# =============================================================================
# Test AnalystRole Enum
# =============================================================================


class TestAnalystRole:
    """Tests for AnalystRole enumeration."""

    def test_all_roles_defined(self):
        """Test all 9 analyst roles are defined."""
        roles = list(AnalystRole)
        assert len(roles) == 9

    def test_role_values(self):
        """Test role values are lowercase strings."""
        assert AnalystRole.AESTHETE.value == "aesthete"
        assert AnalystRole.DRAMATURGIST.value == "dramaturgist"
        assert AnalystRole.NARRATOLOGIST.value == "narratologist"
        assert AnalystRole.ART_HISTORIAN.value == "art_historian"
        assert AnalystRole.CINEPHILE.value == "cinephile"
        assert AnalystRole.RHETORICIAN.value == "rhetorician"
        assert AnalystRole.PRODUCER.value == "producer"
        assert AnalystRole.ACADEMIC.value == "academic"
        assert AnalystRole.FIRST_READER.value == "first_reader"

    def test_role_study_mapping(self):
        """Test role-to-study mapping exists for key roles."""
        assert AnalystRole.AESTHETE in ROLE_STUDY_MAPPING
        assert "tarkovsky" in ROLE_STUDY_MAPPING[AnalystRole.AESTHETE]
        assert "bergman" in ROLE_STUDY_MAPPING[AnalystRole.AESTHETE]

        assert AnalystRole.DRAMATURGIST in ROLE_STUDY_MAPPING
        assert "pixar" in ROLE_STUDY_MAPPING[AnalystRole.DRAMATURGIST]


# =============================================================================
# Test ActivationLayer
# =============================================================================


class TestActivationLayer:
    """Tests for ActivationLayer enumeration."""

    def test_essential_roles(self):
        """Test essential layer includes core roles."""
        roles = ActivationLayer.ESSENTIAL.roles
        assert AnalystRole.DRAMATURGIST in roles
        assert AnalystRole.NARRATOLOGIST in roles
        assert AnalystRole.FIRST_READER in roles
        assert len(roles) == 3

    def test_full_roles(self):
        """Test full layer includes all roles."""
        roles = ActivationLayer.FULL.roles
        assert len(roles) == 9
        for role in AnalystRole:
            assert role in roles

    def test_layer_progression(self):
        """Test layers progressively add roles."""
        essential = len(ActivationLayer.ESSENTIAL.roles)
        creative = len(ActivationLayer.CREATIVE.roles)
        contextual = len(ActivationLayer.CONTEXTUAL.roles)
        practical = len(ActivationLayer.PRACTICAL.roles)
        full = len(ActivationLayer.FULL.roles)

        assert essential <= creative <= contextual <= practical <= full


# =============================================================================
# Test get_analyst Factory
# =============================================================================


class TestGetAnalyst:
    """Tests for get_analyst factory function."""

    def test_get_analyst_by_enum(self):
        """Test getting analyst by AnalystRole enum."""
        analyst = get_analyst(AnalystRole.AESTHETE)
        assert isinstance(analyst, BaseAnalyst)
        assert analyst.role == AnalystRole.AESTHETE

    def test_get_analyst_by_string(self):
        """Test getting analyst by string name."""
        analyst = get_analyst("dramaturgist")
        assert analyst.role == AnalystRole.DRAMATURGIST

    def test_get_analyst_case_insensitive(self):
        """Test string lookup is case-insensitive."""
        analyst = get_analyst("NARRATOLOGIST")
        assert analyst.role == AnalystRole.NARRATOLOGIST

    def test_get_analyst_with_provider(self, mock_provider):
        """Test analyst gets provider."""
        analyst = get_analyst(AnalystRole.AESTHETE, mock_provider)
        assert analyst.provider == mock_provider

    def test_get_analyst_unknown_role(self):
        """Test error for unknown role."""
        with pytest.raises(ValueError, match="Unknown"):
            get_analyst("nonexistent")

    def test_get_all_analysts(self):
        """Test getting all analyst instances."""
        analysts = get_all_analysts()
        assert len(analysts) == 9

        roles = {a.role for a in analysts}
        assert roles == set(AnalystRole)


# =============================================================================
# Test Individual Analysts
# =============================================================================


class TestIndividualAnalysts:
    """Tests for individual analyst implementations."""

    @pytest.mark.parametrize("role", list(AnalystRole))
    def test_analyst_has_role(self, role):
        """Test each analyst has correct role."""
        analyst = get_analyst(role)
        assert analyst.role == role

    @pytest.mark.parametrize("role", list(AnalystRole))
    def test_analyst_has_primary_studies(self, role):
        """Test each analyst has primary studies list."""
        analyst = get_analyst(role)
        assert isinstance(analyst.primary_studies, list)

    @pytest.mark.parametrize("role", list(AnalystRole))
    def test_analyst_analyze_without_llm(self, role, simple_context):
        """Test analyst can analyze without LLM (returns placeholder)."""
        analyst = get_analyst(role)
        result = analyst.analyze(simple_context)

        assert isinstance(result, RoleAnalysisResult)
        assert result.role == role

    def test_analyst_analyze_with_llm(self, simple_context, mock_provider):
        """Test analyst analysis with LLM provider."""
        mock_provider.set_response(
            "",
            structured_data={
                "summary": "Beautiful visual patterns identified",
                "observations": [
                    {
                        "category": "visual",
                        "observation": "Strong imagery",
                        "confidence": 0.9,
                    }
                ],
                "key_findings": ["Finding 1"],
                "recommendations": ["Recommendation 1"],
                "score": 8.0,
            },
        )

        analyst = get_analyst(AnalystRole.AESTHETE, mock_provider)
        result = analyst.analyze(simple_context)

        assert result.summary == "Beautiful visual patterns identified"
        assert len(result.observations) == 1
        assert result.score == 8.0


# =============================================================================
# Test AnalystContext
# =============================================================================


class TestAnalystContext:
    """Tests for AnalystContext model."""

    def test_context_creation(self):
        """Test creating analyst context."""
        context = AnalystContext(
            title="Test",
            text="Content",
        )
        assert context.title == "Test"
        assert context.format == "Feature"  # Default

    def test_context_from_script(self, simple_script):
        """Test creating context from Script model."""
        context = AnalystContext.from_script(simple_script)

        assert context.title == "Test Script"
        assert context.genre == "Drama"
        assert len(context.scene_summaries) == 2


# =============================================================================
# Test RoleAnalysisResult
# =============================================================================


class TestRoleAnalysisResult:
    """Tests for RoleAnalysisResult model."""

    def test_result_creation(self):
        """Test creating analysis result."""
        result = RoleAnalysisResult(
            role=AnalystRole.AESTHETE,
            summary="Test summary",
            observations=[],
        )
        assert result.role == AnalystRole.AESTHETE
        assert result.summary == "Test summary"

    def test_observation_count_by_category(self):
        """Test counting observations by category."""
        result = RoleAnalysisResult(
            role=AnalystRole.AESTHETE,
            summary="Test",
            observations=[
                AnalystObservation(
                    role=AnalystRole.AESTHETE,
                    category="visual",
                    observation="Obs 1",
                ),
                AnalystObservation(
                    role=AnalystRole.AESTHETE,
                    category="visual",
                    observation="Obs 2",
                ),
                AnalystObservation(
                    role=AnalystRole.AESTHETE,
                    category="tonal",
                    observation="Obs 3",
                ),
            ],
        )

        counts = result.observation_count_by_category()
        assert counts["visual"] == 2
        assert counts["tonal"] == 1


# =============================================================================
# Test MultiRoleOrchestrator
# =============================================================================


class TestMultiRoleOrchestrator:
    """Tests for MultiRoleOrchestrator."""

    def test_orchestrator_creation(self, mock_provider):
        """Test creating orchestrator."""
        orchestrator = MultiRoleOrchestrator(mock_provider)
        assert orchestrator.provider == mock_provider

    def test_analyze_text(self, mock_provider):
        """Test analyzing text with orchestrator."""
        # Set up mock responses for each role
        mock_provider.set_response(
            "",
            structured_data={
                "summary": "Test summary",
                "observations": [],
                "key_findings": ["Finding"],
                "recommendations": ["Recommendation"],
                "score": 7.0,
            },
        )

        orchestrator = MultiRoleOrchestrator(mock_provider)
        config = SynthesisConfig(activation_layer=ActivationLayer.ESSENTIAL)

        result = orchestrator.analyze(
            text="A test script about transformation",
            title="Test Script",
            config=config,
        )

        assert isinstance(result, MultiRoleAnalysis)
        assert result.title == "Test Script"

    def test_analyze_script(self, simple_script, mock_provider):
        """Test analyzing Script model."""
        mock_provider.set_response(
            "",
            structured_data={
                "summary": "Test summary",
                "observations": [],
                "key_findings": [],
                "recommendations": [],
                "score": 7.0,
            },
        )

        orchestrator = MultiRoleOrchestrator(mock_provider)
        config = SynthesisConfig(activation_layer=ActivationLayer.ESSENTIAL)

        result = orchestrator.analyze_script(simple_script, config)

        assert result.title == "Test Script"
        assert result.role_count() >= 1

    def test_orchestrator_execution_time(self, mock_provider):
        """Test that execution time is tracked."""
        mock_provider.set_response(
            "",
            structured_data={
                "summary": "Test",
                "observations": [],
                "key_findings": [],
                "recommendations": [],
                "score": 5.0,
            },
        )

        orchestrator = MultiRoleOrchestrator(mock_provider)
        config = SynthesisConfig(activation_layer=ActivationLayer.ESSENTIAL)

        result = orchestrator.analyze("Test", "Test Script", config)

        assert result.execution_time_ms is not None
        assert result.execution_time_ms >= 0


# =============================================================================
# Test MultiRoleAnalysis
# =============================================================================


class TestMultiRoleAnalysis:
    """Tests for MultiRoleAnalysis model."""

    def test_get_role_result(self):
        """Test getting result by role."""
        aesthete_result = RoleAnalysisResult(
            role=AnalystRole.AESTHETE,
            summary="Aesthete analysis",
        )

        analysis = MultiRoleAnalysis(
            title="Test",
            role_results={"aesthete": aesthete_result},
        )

        result = analysis.get_role_result(AnalystRole.AESTHETE)
        assert result is not None
        assert result.role == AnalystRole.AESTHETE

        result_by_string = analysis.get_role_result("aesthete")
        assert result_by_string is not None

    def test_get_all_observations(self):
        """Test aggregating all observations."""
        obs1 = AnalystObservation(
            role=AnalystRole.AESTHETE,
            category="visual",
            observation="Obs 1",
        )
        obs2 = AnalystObservation(
            role=AnalystRole.DRAMATURGIST,
            category="structure",
            observation="Obs 2",
        )

        analysis = MultiRoleAnalysis(
            title="Test",
            role_results={
                "aesthete": RoleAnalysisResult(
                    role=AnalystRole.AESTHETE,
                    summary="Test",
                    observations=[obs1],
                ),
                "dramaturgist": RoleAnalysisResult(
                    role=AnalystRole.DRAMATURGIST,
                    summary="Test",
                    observations=[obs2],
                ),
            },
        )

        all_obs = analysis.get_all_observations()
        assert len(all_obs) == 2

    def test_observations_by_category(self):
        """Test grouping observations by category."""
        analysis = MultiRoleAnalysis(
            title="Test",
            role_results={
                "aesthete": RoleAnalysisResult(
                    role=AnalystRole.AESTHETE,
                    summary="Test",
                    observations=[
                        AnalystObservation(
                            role=AnalystRole.AESTHETE,
                            category="visual",
                            observation="Visual obs",
                        ),
                        AnalystObservation(
                            role=AnalystRole.AESTHETE,
                            category="structure",
                            observation="Structure obs",
                        ),
                    ],
                ),
            },
        )

        by_category = analysis.observations_by_category()
        assert "visual" in by_category
        assert "structure" in by_category

    def test_average_score(self):
        """Test calculating average score."""
        analysis = MultiRoleAnalysis(
            title="Test",
            role_results={
                "role1": RoleAnalysisResult(
                    role=AnalystRole.AESTHETE,
                    summary="Test",
                    score=8.0,
                ),
                "role2": RoleAnalysisResult(
                    role=AnalystRole.DRAMATURGIST,
                    summary="Test",
                    score=6.0,
                ),
            },
        )

        avg = analysis.average_score()
        assert avg == 7.0


# =============================================================================
# Test SynthesisConfig
# =============================================================================


class TestSynthesisConfig:
    """Tests for SynthesisConfig model."""

    def test_default_config(self):
        """Test default configuration."""
        config = SynthesisConfig()
        assert config.activation_layer == ActivationLayer.ESSENTIAL
        assert config.parallel_execution is True

    def test_custom_config(self):
        """Test custom configuration."""
        config = SynthesisConfig(
            activation_layer=ActivationLayer.FULL,
            parallel_execution=False,
            active_studies=["pixar", "bergman"],
        )
        assert config.activation_layer == ActivationLayer.FULL
        assert config.parallel_execution is False
        assert "pixar" in config.active_studies
