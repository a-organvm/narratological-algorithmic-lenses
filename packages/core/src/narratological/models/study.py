"""Pydantic models for narratological studies.

These models represent the core data structures for the 14 narratological
algorithm studies, including axioms, algorithms, structural hierarchies,
diagnostic questions, and theoretical correspondences.
"""

from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class Category(str, Enum):
    """Study categories based on medium/tradition."""

    CLASSICAL = "Classical"
    FILM = "Film"
    TELEVISION = "Television"
    COMICS = "Comics"
    LITERATURE = "Literature"
    INTERACTIVE = "Interactive"
    ANIMATION = "Animation"
    META = "Meta"


class Axiom(BaseModel):
    """A foundational principle extracted from a creator's work.

    Axioms are the meta-principles that underpin a creator's narrative
    philosophy. They represent fundamental truths about storytelling
    as practiced by that creator.
    """

    id: str = Field(description="Unique identifier (e.g., 'IB-A0' for Bergman axiom 0)")
    name: str = Field(description="Human-readable axiom name")
    statement: str = Field(description="The principle statement")
    derivations: list[str] = Field(
        default_factory=list,
        description="Implications and derived principles",
    )


class Algorithm(BaseModel):
    """A formalized narrative process with pseudo-code implementation.

    Algorithms represent the operational procedures derived from a
    creator's practice. They can be executed (conceptually or literally)
    to generate or analyze narrative structures.
    """

    name: str = Field(description="Algorithm name")
    purpose: str = Field(description="What this algorithm does")
    pseudocode: str = Field(description="Pseudo-code implementation")
    inputs: list[str] = Field(default_factory=list, description="Required inputs")
    outputs: list[str] = Field(default_factory=list, description="Generated outputs")


class DiagnosticQuestion(BaseModel):
    """A self-assessment question for applying a framework.

    Diagnostic questions help analysts evaluate whether a narrative
    meets the criteria established by a study's axioms and algorithms.
    """

    id: str = Field(description="Question identifier (e.g., 'Q1')")
    question: str = Field(description="The diagnostic question")
    valid_if: str = Field(description="Criteria for validity")


class HierarchyLevel(BaseModel):
    """A single level in a structural hierarchy.

    Hierarchies define the nested organizational levels of a narrative
    approach (e.g., macro to micro units, story to beat).
    """

    level: int = Field(description="Level number (1 = highest)")
    name: str = Field(description="Level name")
    description: str = Field(description="What this level represents")
    elements: list[str] = Field(
        default_factory=list,
        description="Elements or components at this level",
    )


class StructuralHierarchy(BaseModel):
    """The nested organizational levels of a narrative approach."""

    levels: list[HierarchyLevel] = Field(
        default_factory=list,
        description="Hierarchy levels from highest to lowest",
    )


class TheoreticalCorrespondences(BaseModel):
    """Mappings to other theoretical frameworks and paired studies.

    Links a study to related traditions (Aristotle, McKee, Campbell, etc.)
    and identifies which other studies form thematic pairs.
    """

    maps_to: list[str] = Field(
        default_factory=list,
        description="Related theories and traditions",
    )
    sequence_pairs: list[str | dict[str, str]] = Field(
        default_factory=list,
        description="IDs of paired studies or comparison dictionaries",
    )


class QuickReference(BaseModel):
    """Condensed summary for rapid consultation."""

    core_operations: list[str] = Field(
        default_factory=list,
        description="Key operations or principles",
    )
    key_constraints: list[str] = Field(
        default_factory=list,
        description="Important constraints or requirements",
    )


class Study(BaseModel):
    """A complete narratological algorithm study.

    Each study extracts the narrative craft methodology from a primary
    source (creator, work, or tradition) and formalizes it into
    implementable algorithmic frameworks.
    """

    id: str = Field(description="Unique study identifier")
    creator: str = Field(description="Creator or source name")
    work: str = Field(description="Primary work(s) analyzed")
    category: Category = Field(description="Medium/tradition category")
    axioms: list[Axiom] = Field(default_factory=list, description="Foundational principles")
    structural_hierarchy: StructuralHierarchy = Field(
        default_factory=StructuralHierarchy,
        description="Organizational hierarchy",
    )
    core_algorithms: list[Algorithm] = Field(
        default_factory=list,
        description="Formalized processes",
    )
    diagnostic_questions: list[DiagnosticQuestion] = Field(
        default_factory=list,
        description="Self-assessment prompts",
    )
    theoretical_correspondences: TheoreticalCorrespondences = Field(
        default_factory=TheoreticalCorrespondences,
        description="Links to other frameworks",
    )
    quick_reference: QuickReference = Field(
        default_factory=QuickReference,
        description="Condensed summary",
    )

    # Optional extended fields that appear in some studies
    signature_patterns: list[dict[str, Any]] | None = Field(
        default=None,
        description="Recurring patterns specific to this creator (e.g., Lynch)",
    )

    def get_axiom(self, axiom_id: str) -> Axiom | None:
        """Get an axiom by its ID."""
        for axiom in self.axioms:
            if axiom.id == axiom_id:
                return axiom
        return None

    def get_algorithm(self, name: str) -> Algorithm | None:
        """Get an algorithm by its name."""
        for algo in self.core_algorithms:
            if algo.name == name:
                return algo
        return None

    def get_diagnostic(self, question_id: str) -> DiagnosticQuestion | None:
        """Get a diagnostic question by its ID."""
        for q in self.diagnostic_questions:
            if q.id == question_id:
                return q
        return None


class SequencePair(BaseModel):
    """A thematic pairing between two studies.

    Sequence pairs link studies that share structural or thematic
    connections despite differences in medium or tradition.
    """

    id: str = Field(description="Sequence identifier (A-G)")
    name: str = Field(description="Sequence theme name")
    studies: list[str] = Field(description="IDs of paired studies")
    shared_principles: list[str] = Field(
        default_factory=list,
        description="Principles shared by the paired studies",
    )
    contrasts: list[str] = Field(
        default_factory=list,
        description="Key differences between the paired studies",
    )


class CompendiumMeta(BaseModel):
    """Metadata for the narratological algorithm compendium."""

    title: str = Field(description="Compendium title")
    version: str = Field(description="Version string")
    generated: str = Field(description="Generation timestamp (ISO format)")
    study_count: int = Field(description="Number of studies")
    categories: list[str] = Field(description="Available categories")


class Compendium(BaseModel):
    """The complete narratological algorithm compendium.

    Contains all studies, cross-references, and metadata for the
    entire collection of narratological algorithms.
    """

    meta: CompendiumMeta = Field(description="Compendium metadata")
    studies: dict[str, Study] = Field(description="Studies keyed by ID")
    cross_references: dict[str, Any] = Field(
        default_factory=dict,
        description="Cross-reference data including sequence pairs",
    )

    def get_study(self, study_id: str) -> Study | None:
        """Get a study by its ID."""
        return self.studies.get(study_id)

    def get_studies_by_category(self, category: Category) -> list[Study]:
        """Get all studies in a category."""
        return [s for s in self.studies.values() if s.category == category]

    def get_sequence_pairs(self) -> list[SequencePair]:
        """Get all sequence pairs from cross-references."""
        sequences = self.cross_references.get("sequences", [])
        return [SequencePair.model_validate(s) for s in sequences]

    def get_pair_from_sequence(self, sequence_id: str) -> tuple[Study, Study] | None:
        """Get the two studies involved in a sequence."""
        for seq in self.get_sequence_pairs():
            if seq.id == sequence_id or seq.name.lower() == sequence_id.lower():
                if len(seq.studies) >= 2:
                    s1 = self.get_study(seq.studies[0])
                    s2 = self.get_study(seq.studies[1])
                    if s1 and s2:
                        return s1, s2
        return None

    def get_paired_study(self, study_id: str) -> Study | None:
        """Get the paired study for a given study (if any)."""
        for pair in self.get_sequence_pairs():
            if study_id in pair.studies:
                partner_id = [s for s in pair.studies if s != study_id]
                if partner_id:
                    return self.get_study(partner_id[0])
        return None

    def list_study_ids(self) -> list[str]:
        """List all study IDs."""
        return list(self.studies.keys())

    def search_axioms(self, query: str) -> list[tuple[str, Axiom]]:
        """Search axioms across all studies.

        Returns tuples of (study_id, axiom) for matches.
        """
        query_lower = query.lower()
        results = []
        for study_id, study in self.studies.items():
            for axiom in study.axioms:
                if (
                    query_lower in axiom.name.lower()
                    or query_lower in axiom.statement.lower()
                ):
                    results.append((study_id, axiom))
        return results

    def search_algorithms(self, query: str) -> list[tuple[str, Algorithm]]:
        """Search algorithms across all studies.

        Returns tuples of (study_id, algorithm) for matches.
        """
        query_lower = query.lower()
        results = []
        for study_id, study in self.studies.items():
            for algo in study.core_algorithms:
                if (
                    query_lower in algo.name.lower()
                    or query_lower in algo.purpose.lower()
                ):
                    results.append((study_id, algo))
        return results
