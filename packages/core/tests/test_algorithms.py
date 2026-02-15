"""Tests for the algorithm engine.

Tests cover the algorithm registry, base classes, executor,
and LLM provider implementations.
"""

from pathlib import Path

import pytest

from narratological.algorithms import (
    AlgorithmExecutor,
    AlgorithmInfo,
    AlgorithmRegistry,
    AnalysisResult,
    ExecutableAlgorithm,
    ExecutionMode,
    ExecutorError,
    GenerationResult,
    ValidationResult,
    create_executor,
    get_registry,
    reset_registry,
)
from narratological.llm import MockProvider, MockResponse, get_provider


# Path to the actual unified JSON for integration tests
SPECS_PATH = Path(__file__).parent.parent.parent.parent / "specs" / "03-structured-data"
UNIFIED_JSON = SPECS_PATH / "narratological-algorithms-unified.json"


@pytest.fixture
def compendium_path():
    """Get path to the unified JSON if it exists."""
    if UNIFIED_JSON.exists():
        return UNIFIED_JSON
    pytest.skip("Unified JSON not found - skipping integration tests")


@pytest.fixture
def registry(compendium_path):
    """Create an algorithm registry."""
    return AlgorithmRegistry.from_path(compendium_path)


@pytest.fixture
def mock_provider():
    """Create a mock LLM provider."""
    return MockProvider()


class TestAlgorithmRegistry:
    """Tests for AlgorithmRegistry."""

    def test_registry_loads_all_algorithms(self, registry):
        """Test that the registry loads all algorithms from the compendium."""
        total = registry.count()
        # We expect ~110+ algorithms across 27+ studies
        assert total >= 100, f"Expected at least 100 algorithms, got {total}"

    def test_registry_has_all_studies(self, registry):
        """Test that the registry has algorithms from all core studies."""
        studies = registry.list_studies()
        assert len(studies) >= 27, f"Expected at least 27 studies, got {len(studies)}"

    def test_registry_get_algorithm(self, registry):
        """Test getting a specific algorithm."""
        algo = registry.get("bergman", "Chamber Drama Construction")
        assert isinstance(algo, ExecutableAlgorithm)
        assert algo.study_id == "bergman"
        assert "Chamber Drama" in algo.name

    def test_registry_get_algorithm_case_insensitive(self, registry):
        """Test that algorithm lookup is case-insensitive."""
        algo1 = registry.get("bergman", "Chamber Drama Construction")
        algo2 = registry.get("BERGMAN", "chamber drama construction")
        assert algo1.name == algo2.name

    def test_registry_get_algorithm_not_found(self, registry):
        """Test that KeyError is raised for unknown algorithms."""
        with pytest.raises(KeyError, match="not found"):
            registry.get("bergman", "Nonexistent Algorithm")

    def test_registry_get_by_qualified_name(self, registry):
        """Test getting algorithm by qualified name."""
        algo = registry.get_by_qualified_name("bergman.Chamber Drama Construction")
        assert algo.study_id == "bergman"

    def test_registry_list_by_study(self, registry):
        """Test listing algorithms for a specific study."""
        bergman_algos = registry.list_by_study("bergman")
        assert len(bergman_algos) >= 5, "Bergman should have at least 5 algorithms"
        assert all(a.study_id == "bergman" for a in bergman_algos)

    def test_registry_list_by_study_not_found(self, registry):
        """Test that empty list is returned for unknown study."""
        algos = registry.list_by_study("nonexistent")
        assert algos == []

    def test_registry_search(self, registry):
        """Test searching algorithms."""
        results = registry.search("empathy")
        assert len(results) >= 1
        assert any("empathy" in a.name.lower() for a in results)

    def test_registry_search_no_results(self, registry):
        """Test search with no matches."""
        results = registry.search("xyznonexistent123")
        assert results == []

    def test_registry_all(self, registry):
        """Test getting all algorithms."""
        all_algos = registry.all()
        assert len(all_algos) == registry.count()

    def test_registry_info(self, registry):
        """Test getting algorithm info."""
        infos = registry.info()
        assert len(infos) == registry.count()
        assert all(isinstance(info, AlgorithmInfo) for info in infos)

    def test_registry_count_by_study(self, registry):
        """Test getting counts per study."""
        counts = registry.count_by_study()
        assert len(counts) >= 27
        assert all(c >= 1 for c in counts.values())

    def test_registry_contains(self, registry):
        """Test the __contains__ method."""
        assert "bergman.Chamber Drama Construction" in registry
        assert "nonexistent.algorithm" not in registry

    def test_registry_iter(self, registry):
        """Test iterating over the registry."""
        count = 0
        for algo in registry:
            assert isinstance(algo, ExecutableAlgorithm)
            count += 1
        assert count == registry.count()


class TestGlobalRegistry:
    """Tests for the global registry functions."""

    def test_get_registry(self, compendium_path):
        """Test getting the global registry."""
        reset_registry()  # Ensure clean state
        reg = get_registry()
        assert isinstance(reg, AlgorithmRegistry)

    def test_get_registry_singleton(self, compendium_path):
        """Test that get_registry returns the same instance."""
        reset_registry()
        reg1 = get_registry()
        reg2 = get_registry()
        assert reg1 is reg2

    def test_reset_registry(self, compendium_path):
        """Test resetting the global registry."""
        reset_registry()
        reg1 = get_registry()
        reset_registry()
        reg2 = get_registry()
        assert reg1 is not reg2


class TestExecutableAlgorithm:
    """Tests for ExecutableAlgorithm."""

    def test_algorithm_properties(self, registry):
        """Test algorithm property accessors."""
        algo = registry.get("bergman", "Chamber Drama Construction")
        assert algo.name == "Chamber Drama Construction"
        assert algo.study_id == "bergman"
        assert len(algo.purpose) > 0
        assert len(algo.pseudocode) > 0
        assert isinstance(algo.inputs, list)
        assert isinstance(algo.outputs, list)

    def test_algorithm_str(self, registry):
        """Test algorithm string representation."""
        algo = registry.get("bergman", "Chamber Drama Construction")
        s = str(algo)
        assert "bergman" in s
        assert "Chamber Drama" in s

    def test_algorithm_repr(self, registry):
        """Test algorithm detailed representation."""
        algo = registry.get("bergman", "Chamber Drama Construction")
        r = repr(algo)
        assert "ExecutableAlgorithm" in r
        assert "bergman" in r


class TestMockProvider:
    """Tests for MockProvider."""

    def test_mock_provider_complete(self):
        """Test mock provider text completion."""
        provider = MockProvider(default_response="Test response")
        result = provider.complete("Test prompt")
        assert result.content == "Test response"
        assert result.model == "mock-model"

    def test_mock_provider_set_response(self):
        """Test setting a specific response."""
        provider = MockProvider()
        provider.set_response("Custom response")
        result = provider.complete("Test")
        assert result.content == "Custom response"

    def test_mock_provider_tracks_calls(self):
        """Test that calls are tracked."""
        provider = MockProvider()
        provider.complete("First prompt", system="System message")
        provider.complete("Second prompt")

        calls = provider.get_calls()
        assert len(calls) == 2
        assert calls[0]["prompt"] == "First prompt"
        assert calls[0]["system"] == "System message"
        assert calls[1]["prompt"] == "Second prompt"

    def test_mock_provider_last_call(self):
        """Test getting the last call."""
        provider = MockProvider()
        provider.complete("First")
        provider.complete("Second")

        last = provider.get_last_call()
        assert last["prompt"] == "Second"

    def test_mock_provider_reset(self):
        """Test resetting the provider."""
        provider = MockProvider()
        provider.set_response("Response")
        provider.complete("Test")

        provider.reset()
        assert provider.get_calls() == []

    def test_mock_provider_structured(self):
        """Test structured completion."""
        provider = MockProvider()
        provider.set_response("", structured_data={
            "algorithm_name": "test",
            "study_id": "test",
            "input_summary": "Summary",
            "findings": ["Finding 1"],
        })

        result = provider.complete_structured("Test", AnalysisResult)
        assert isinstance(result, AnalysisResult)
        assert result.input_summary == "Summary"


class TestGetProvider:
    """Tests for get_provider factory function."""

    def test_get_mock_provider(self):
        """Test getting mock provider."""
        provider = get_provider("mock")
        assert isinstance(provider, MockProvider)

    def test_get_unknown_provider(self):
        """Test getting unknown provider raises error."""
        with pytest.raises(ValueError, match="Unknown provider"):
            get_provider("nonexistent")


class TestAlgorithmExecutor:
    """Tests for AlgorithmExecutor."""

    def test_executor_analyze(self, registry, mock_provider):
        """Test executing analysis."""
        mock_provider.set_response("", structured_data={
            "algorithm_name": "test",
            "study_id": "test",
            "input_summary": "A story about change",
            "findings": ["Uses transformation"],
            "elements_identified": {"theme": "metamorphosis"},
            "recommendations": ["Strengthen the emotional arc"],
            "score": 0.75,
        })

        executor = AlgorithmExecutor(mock_provider, registry)
        algo = registry.get("bergman", "Chamber Drama Construction")

        result = executor.analyze(algo, "Once upon a time...")

        assert isinstance(result, AnalysisResult)
        assert result.score == 0.75
        assert len(mock_provider.get_calls()) == 1

    def test_executor_generate(self, registry, mock_provider):
        """Test executing generation."""
        mock_provider.set_response("", structured_data={
            "algorithm_name": "test",
            "study_id": "test",
            "generated_content": "A chamber drama unfolds...",
            "structure": {"setting": "isolated island"},
            "notes": ["Applied constraint principles"],
        })

        executor = AlgorithmExecutor(mock_provider, registry)
        algo = registry.get("bergman", "Chamber Drama Construction")

        result = executor.generate(algo, {"setting": "island"})

        assert isinstance(result, GenerationResult)
        assert "chamber drama" in result.generated_content.lower()

    def test_executor_validate(self, registry, mock_provider):
        """Test executing validation."""
        mock_provider.set_response("", structured_data={
            "algorithm_name": "test",
            "study_id": "test",
            "is_valid": True,
            "criteria_met": ["Constrained setting", "Limited cast"],
            "criteria_failed": [],
            "suggestions": [],
            "confidence": 0.85,
        })

        executor = AlgorithmExecutor(mock_provider, registry)
        algo = registry.get("bergman", "Chamber Drama Construction")

        result = executor.validate(algo, "In a remote cabin...")

        assert isinstance(result, ValidationResult)
        assert result.is_valid is True
        assert result.confidence == 0.85

    def test_executor_run_by_qualified_name(self, registry, mock_provider):
        """Test running by qualified algorithm name."""
        mock_provider.set_response("", structured_data={
            "algorithm_name": "test",
            "study_id": "test",
            "input_summary": "Summary",
            "findings": [],
        })

        executor = AlgorithmExecutor(mock_provider, registry)
        result = executor.run(
            "bergman.Chamber Drama Construction",
            "analyze",
            "Test text",
        )

        assert isinstance(result, AnalysisResult)

    def test_executor_invalid_mode(self, registry, mock_provider):
        """Test that invalid mode raises error."""
        executor = AlgorithmExecutor(mock_provider, registry)
        algo = registry.get("bergman", "Chamber Drama Construction")

        with pytest.raises(ValueError, match="Invalid mode"):
            executor.run(algo, "invalid_mode", "text")

    def test_executor_wrong_input_type(self, registry, mock_provider):
        """Test that wrong input type raises error."""
        executor = AlgorithmExecutor(mock_provider, registry)
        algo = registry.get("bergman", "Chamber Drama Construction")

        with pytest.raises(ExecutorError, match="requires text input"):
            executor.run(algo, ExecutionMode.ANALYZE, {"wrong": "type"})

    def test_executor_logs_executions(self, registry, mock_provider):
        """Test that executions are logged."""
        mock_provider.set_response("", structured_data={
            "algorithm_name": "test",
            "study_id": "test",
            "input_summary": "Summary",
        })

        executor = AlgorithmExecutor(mock_provider, registry)
        algo = registry.get("bergman", "Chamber Drama Construction")

        executor.analyze(algo, "Text 1")
        executor.analyze(algo, "Text 2")

        log = executor.get_execution_log()
        assert len(log) == 2
        assert all(entry.success for entry in log)

    def test_executor_clear_log(self, registry, mock_provider):
        """Test clearing the execution log."""
        mock_provider.set_response("", structured_data={
            "algorithm_name": "test",
            "study_id": "test",
            "input_summary": "Summary",
        })

        executor = AlgorithmExecutor(mock_provider, registry)
        algo = registry.get("bergman", "Chamber Drama Construction")

        executor.analyze(algo, "Text")
        executor.clear_log()

        assert len(executor.get_execution_log()) == 0


class TestCreateExecutor:
    """Tests for create_executor factory function."""

    def test_create_mock_executor(self, compendium_path):
        """Test creating executor with mock provider."""
        executor = create_executor("mock")
        assert isinstance(executor, AlgorithmExecutor)
        assert isinstance(executor.provider, MockProvider)


class TestAlgorithmCounts:
    """Tests to verify expected algorithm counts."""

    EXPECTED_ALGORITHM_COUNTS = {
        "bergman": 6,
        "tarkovsky": 6,
        "pixar": 8,
        "zelda": 11,
        "alan-moore": 7,
        "morrison": 7,
        "final-fantasy": 8,
        "kirby-new-gods": 6,
        "tolkien": 7,
        "ovid-metamorphoses": 6,
        "gaiman-sandman": 6,
        "tarantino": 5,
        "warren-ellis": 6,
        "david-lynch": 6,
    }

    @pytest.mark.parametrize("study_id,expected_count", EXPECTED_ALGORITHM_COUNTS.items())
    def test_study_algorithm_count(self, registry, study_id, expected_count):
        """Test that each study has the expected number of algorithms."""
        algos = registry.list_by_study(study_id)
        # Allow some variance since exact counts may change
        assert len(algos) >= expected_count - 2, (
            f"{study_id} has {len(algos)} algorithms, expected ~{expected_count}"
        )


class TestAlgorithmExecutionModes:
    """Tests for different execution modes."""

    def test_execution_mode_enum(self):
        """Test ExecutionMode enum values."""
        assert ExecutionMode.ANALYZE.value == "analyze"
        assert ExecutionMode.GENERATE.value == "generate"
        assert ExecutionMode.VALIDATE.value == "validate"

    def test_execution_mode_from_string(self):
        """Test creating ExecutionMode from string."""
        assert ExecutionMode("analyze") == ExecutionMode.ANALYZE
        assert ExecutionMode("generate") == ExecutionMode.GENERATE
        assert ExecutionMode("validate") == ExecutionMode.VALIDATE


class TestAnalysisResult:
    """Tests for AnalysisResult model."""

    def test_analysis_result_defaults(self):
        """Test AnalysisResult default values."""
        result = AnalysisResult(
            algorithm_name="test",
            study_id="test",
            input_summary="Summary",
        )
        assert result.findings == []
        assert result.elements_identified == {}
        assert result.recommendations == []
        assert result.score is None
        assert result.raw_output == ""


class TestGenerationResult:
    """Tests for GenerationResult model."""

    def test_generation_result_defaults(self):
        """Test GenerationResult default values."""
        result = GenerationResult(
            algorithm_name="test",
            study_id="test",
            generated_content="Content",
        )
        assert result.structure == {}
        assert result.notes == []
        assert result.raw_output == ""


class TestValidationResult:
    """Tests for ValidationResult model."""

    def test_validation_result_defaults(self):
        """Test ValidationResult default values."""
        result = ValidationResult(
            algorithm_name="test",
            study_id="test",
            is_valid=True,
        )
        assert result.criteria_met == []
        assert result.criteria_failed == []
        assert result.suggestions == []
        assert result.confidence == 0.0
        assert result.raw_output == ""
