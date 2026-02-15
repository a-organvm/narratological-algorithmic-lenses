"""Tests for Pydantic data models."""

import pytest
from pydantic import ValidationError

from narratological.models.study import (
    Algorithm,
    Axiom,
    Category,
    Compendium,
    CompendiumMeta,
    DiagnosticQuestion,
    HierarchyLevel,
    QuickReference,
    SequencePair,
    StructuralHierarchy,
    Study,
    TheoreticalCorrespondences,
)


class TestAxiom:
    """Tests for the Axiom model."""

    def test_create_minimal_axiom(self):
        """Test creating an axiom with required fields only."""
        axiom = Axiom(
            id="TEST-A0",
            name="Test Axiom",
            statement="This is a test axiom statement.",
        )
        assert axiom.id == "TEST-A0"
        assert axiom.name == "Test Axiom"
        assert axiom.statement == "This is a test axiom statement."
        assert axiom.derivations == []

    def test_create_axiom_with_derivations(self):
        """Test creating an axiom with derivations."""
        axiom = Axiom(
            id="TEST-A1",
            name="Another Axiom",
            statement="Statement with derivations",
            derivations=["Derivation 1", "Derivation 2"],
        )
        assert len(axiom.derivations) == 2
        assert "Derivation 1" in axiom.derivations

    def test_axiom_requires_id(self):
        """Test that axiom requires an ID."""
        with pytest.raises(ValidationError):
            Axiom(name="No ID", statement="Missing ID")


class TestAlgorithm:
    """Tests for the Algorithm model."""

    def test_create_algorithm(self):
        """Test creating an algorithm."""
        algo = Algorithm(
            name="Test Algorithm",
            purpose="For testing",
            pseudocode="RETURN test_value",
            inputs=["input1", "input2"],
            outputs=["output1"],
        )
        assert algo.name == "Test Algorithm"
        assert algo.purpose == "For testing"
        assert len(algo.inputs) == 2
        assert len(algo.outputs) == 1

    def test_algorithm_empty_io(self):
        """Test algorithm with empty inputs/outputs."""
        algo = Algorithm(
            name="Simple",
            purpose="Simple algorithm",
            pseudocode="RETURN NULL",
        )
        assert algo.inputs == []
        assert algo.outputs == []


class TestDiagnosticQuestion:
    """Tests for the DiagnosticQuestion model."""

    def test_create_question(self):
        """Test creating a diagnostic question."""
        q = DiagnosticQuestion(
            id="Q1",
            question="Is the structure valid?",
            valid_if="Structure follows the pattern",
        )
        assert q.id == "Q1"
        assert "structure" in q.question.lower()


class TestStructuralHierarchy:
    """Tests for structural hierarchy models."""

    def test_create_hierarchy_level(self):
        """Test creating a hierarchy level."""
        level = HierarchyLevel(
            level=1,
            name="Top Level",
            description="The highest level",
            elements=["Element A", "Element B"],
        )
        assert level.level == 1
        assert len(level.elements) == 2

    def test_create_hierarchy(self):
        """Test creating a structural hierarchy."""
        hierarchy = StructuralHierarchy(
            levels=[
                HierarchyLevel(level=1, name="Level 1", description="First", elements=[]),
                HierarchyLevel(level=2, name="Level 2", description="Second", elements=[]),
            ]
        )
        assert len(hierarchy.levels) == 2


class TestCategory:
    """Tests for the Category enum."""

    def test_category_values(self):
        """Test that all expected categories exist."""
        expected = {"Classical", "Film", "Comics", "Literature", "Interactive", "Animation", "Television", "Meta"}
        actual = {c.value for c in Category}
        assert actual == expected


class TestStudy:
    """Tests for the Study model."""

    @pytest.fixture
    def sample_study(self):
        """Create a sample study for testing."""
        return Study(
            id="test-study",
            creator="Test Creator",
            work="Test Work",
            category=Category.FILM,
            axioms=[
                Axiom(id="T-A0", name="Axiom 0", statement="First axiom"),
                Axiom(id="T-A1", name="Axiom 1", statement="Second axiom"),
            ],
            core_algorithms=[
                Algorithm(name="Algo 1", purpose="Test", pseudocode="RETURN 1"),
                Algorithm(name="Algo 2", purpose="Test 2", pseudocode="RETURN 2"),
            ],
            diagnostic_questions=[
                DiagnosticQuestion(id="Q1", question="Test?", valid_if="Yes"),
            ],
        )

    def test_study_get_axiom(self, sample_study):
        """Test getting an axiom by ID."""
        axiom = sample_study.get_axiom("T-A0")
        assert axiom is not None
        assert axiom.name == "Axiom 0"

    def test_study_get_axiom_not_found(self, sample_study):
        """Test getting a non-existent axiom."""
        axiom = sample_study.get_axiom("INVALID")
        assert axiom is None

    def test_study_get_algorithm(self, sample_study):
        """Test getting an algorithm by name."""
        algo = sample_study.get_algorithm("Algo 1")
        assert algo is not None
        assert algo.purpose == "Test"

    def test_study_get_algorithm_not_found(self, sample_study):
        """Test getting a non-existent algorithm."""
        algo = sample_study.get_algorithm("Invalid")
        assert algo is None

    def test_study_get_diagnostic(self, sample_study):
        """Test getting a diagnostic question by ID."""
        q = sample_study.get_diagnostic("Q1")
        assert q is not None
        assert q.question == "Test?"


class TestSequencePair:
    """Tests for the SequencePair model."""

    def test_create_sequence_pair(self):
        """Test creating a sequence pair."""
        pair = SequencePair(
            id="A",
            name="Test Pair",
            studies=["study-1", "study-2"],
            shared_principles=["Principle 1"],
            contrasts=["Contrast 1"],
        )
        assert pair.id == "A"
        assert len(pair.studies) == 2


class TestCompendium:
    """Tests for the Compendium model."""

    @pytest.fixture
    def sample_compendium(self):
        """Create a sample compendium for testing."""
        return Compendium(
            meta=CompendiumMeta(
                title="Test Compendium",
                version="1.0.0",
                generated="2024-01-01T00:00:00",
                study_count=2,
                categories=["Film", "Comics"],
            ),
            studies={
                "study-1": Study(
                    id="study-1",
                    creator="Creator 1",
                    work="Work 1",
                    category=Category.FILM,
                    axioms=[Axiom(id="S1-A0", name="Test", statement="Test")],
                ),
                "study-2": Study(
                    id="study-2",
                    creator="Creator 2",
                    work="Work 2",
                    category=Category.COMICS,
                    axioms=[Axiom(id="S2-A0", name="Test 2", statement="Test 2")],
                ),
            },
            cross_references={
                "sequences": [
                    {
                        "id": "A",
                        "name": "Test Sequence",
                        "studies": ["study-1", "study-2"],
                        "shared_principles": ["Shared"],
                    }
                ]
            },
        )

    def test_compendium_get_study(self, sample_compendium):
        """Test getting a study by ID."""
        study = sample_compendium.get_study("study-1")
        assert study is not None
        assert study.creator == "Creator 1"

    def test_compendium_get_study_not_found(self, sample_compendium):
        """Test getting a non-existent study."""
        study = sample_compendium.get_study("invalid")
        assert study is None

    def test_compendium_get_studies_by_category(self, sample_compendium):
        """Test getting studies by category."""
        film_studies = sample_compendium.get_studies_by_category(Category.FILM)
        assert len(film_studies) == 1
        assert film_studies[0].id == "study-1"

    def test_compendium_list_study_ids(self, sample_compendium):
        """Test listing study IDs."""
        ids = sample_compendium.list_study_ids()
        assert set(ids) == {"study-1", "study-2"}

    def test_compendium_get_sequence_pairs(self, sample_compendium):
        """Test getting sequence pairs."""
        pairs = sample_compendium.get_sequence_pairs()
        assert len(pairs) == 1
        assert pairs[0].id == "A"

    def test_compendium_search_axioms(self, sample_compendium):
        """Test searching axioms."""
        results = sample_compendium.search_axioms("test")
        assert len(results) == 2

    def test_compendium_search_axioms_no_results(self, sample_compendium):
        """Test searching axioms with no results."""
        results = sample_compendium.search_axioms("nonexistent")
        assert len(results) == 0
