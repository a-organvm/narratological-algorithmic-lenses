"""Pydantic models for analysis reports.

These models represent the five report types from the SKILL.md
methodology: Coverage, Beat Map, Structural, Character Atlas, and Diagnostic.
"""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, Field

from narratological.models.analysis import (
    ArcClassification,
    BeatFunction,
    ConnectorType,
)


class RecommendationType(StrEnum):
    """Types of recommendations in coverage reports."""

    CONSIDER = "CONSIDER"  # Suggest for reading/production
    PASS = "PASS"  # Do not recommend
    DEVELOP = "DEVELOP"  # Needs work but has potential
    URGENT = "URGENT"  # High priority recommendation


class DiagnosticSeverity(StrEnum):
    """Severity levels for diagnostic issues."""

    CRITICAL = "critical"  # Must be fixed
    WARNING = "warning"  # Should be addressed
    INFO = "info"  # Worth noting
    SUGGESTION = "suggestion"  # Optional improvement


class CoverageReport(BaseModel):
    """Executive summary coverage report.

    Provides high-level assessment and recommendation for a script,
    similar to traditional studio coverage.
    """

    title: str = Field(description="Script title")
    analyst: str = Field(default="Narratological AI", description="Analyst name")
    date: datetime = Field(default_factory=datetime.now, description="Report date")

    # Core assessment
    logline: str = Field(description="One-line summary")
    synopsis: str = Field(description="Brief plot synopsis (1-2 paragraphs)")
    recommendation: RecommendationType = Field(description="Overall recommendation")

    # Ratings (1-10 scale)
    premise_rating: int = Field(ge=1, le=10, description="Premise strength")
    structure_rating: int = Field(ge=1, le=10, description="Structural integrity")
    character_rating: int = Field(ge=1, le=10, description="Character depth")
    dialogue_rating: int = Field(ge=1, le=10, description="Dialogue quality")
    originality_rating: int = Field(ge=1, le=10, description="Originality/freshness")
    marketability_rating: int = Field(ge=1, le=10, description="Commercial potential")

    # Analysis sections
    strengths: list[str] = Field(default_factory=list, description="Key strengths")
    weaknesses: list[str] = Field(default_factory=list, description="Key weaknesses")
    opportunities: list[str] = Field(
        default_factory=list,
        description="Opportunities for improvement",
    )

    # Detailed assessments by role
    aesthete_notes: str | None = Field(default=None, description="Form/style observations")
    dramaturgist_notes: str | None = Field(default=None, description="Structure notes")
    narratologist_notes: str | None = Field(default=None, description="Mechanism notes")
    art_historian_notes: str | None = Field(default=None, description="Context notes")
    cinephile_notes: str | None = Field(default=None, description="Comparison notes")
    rhetorician_notes: str | None = Field(default=None, description="Language notes")
    producer_notes: str | None = Field(default=None, description="Practical notes")
    academic_notes: str | None = Field(default=None, description="Theoretical notes")
    first_reader_notes: str | None = Field(default=None, description="Emotional response")

    # Comparable works
    comparables: list[str] = Field(
        default_factory=list,
        description="Similar films/shows for reference",
    )

    def overall_score(self) -> float:
        """Calculate weighted overall score."""
        weights = {
            "premise": 0.15,
            "structure": 0.20,
            "character": 0.25,
            "dialogue": 0.15,
            "originality": 0.15,
            "marketability": 0.10,
        }
        return (
            self.premise_rating * weights["premise"]
            + self.structure_rating * weights["structure"]
            + self.character_rating * weights["character"]
            + self.dialogue_rating * weights["dialogue"]
            + self.originality_rating * weights["originality"]
            + self.marketability_rating * weights["marketability"]
        )


class BeatMapEntry(BaseModel):
    """A single entry in the beat map."""

    scene_number: int = Field(description="Scene number")
    page_range: str = Field(description="Page range (e.g., '1-3')")
    slug: str = Field(description="Scene heading")
    summary: str = Field(description="Scene summary")
    function: BeatFunction = Field(description="Primary beat function")
    secondary_function: BeatFunction | None = Field(
        default=None,
        description="Secondary function",
    )
    characters: list[str] = Field(default_factory=list, description="Characters present")
    connector: ConnectorType | None = Field(
        default=None,
        description="Connector to next scene",
    )
    tension: int = Field(ge=1, le=10, description="Tension level 1-10")
    notes: str | None = Field(default=None, description="Additional notes")


class BeatMapReport(BaseModel):
    """Complete scene-by-scene beat map.

    Exhaustive mapping of every scene with function codes, connectors,
    tension levels, and structural notes.
    """

    title: str = Field(description="Script title")
    total_scenes: int = Field(description="Total scene count")
    total_pages: int | None = Field(default=None, description="Total page count")

    entries: list[BeatMapEntry] = Field(
        default_factory=list,
        description="Beat map entries for each scene",
    )

    # Summary statistics
    function_distribution: dict[str, int] = Field(
        default_factory=dict,
        description="Count of each beat function",
    )
    connector_distribution: dict[str, int] = Field(
        default_factory=dict,
        description="Count of each connector type",
    )
    average_tension: float | None = Field(default=None, description="Average tension level")

    def calculate_causal_binding_ratio(self) -> float:
        """Calculate BUT/THEREFORE vs AND THEN ratio.

        Higher ratios indicate stronger causal binding.
        Target is typically >80% causal (BUT/THEREFORE).
        """
        causal = sum(
            1
            for e in self.entries
            if e.connector in (ConnectorType.BUT, ConnectorType.THEREFORE)
        )
        episodic = sum(1 for e in self.entries if e.connector == ConnectorType.AND_THEN)
        total = causal + episodic
        if total == 0:
            return 0.0
        return causal / total


class StructuralReport(BaseModel):
    """Act and movement architecture analysis.

    Maps the dramatic structure to established frameworks (three-act,
    five-act, Aristotelian, etc.) and identifies key structural points.
    """

    title: str = Field(description="Script title")
    structure_type: str = Field(
        default="Three-Act",
        description="Structural paradigm (Three-Act, Five-Act, etc.)",
    )

    # Act breakdown
    act_count: int = Field(description="Number of acts")
    acts: list[ActAnalysis] = Field(default_factory=list, description="Act analyses")

    # Key structural points
    opening_image: int | None = Field(
        default=None,
        description="Opening image scene number",
    )
    inciting_incident: int | None = Field(
        default=None,
        description="Inciting incident scene number",
    )
    first_act_break: int | None = Field(
        default=None,
        description="End of Act 1 scene number",
    )
    midpoint: int | None = Field(default=None, description="Midpoint scene number")
    all_is_lost: int | None = Field(
        default=None,
        description="All is lost moment scene number",
    )
    second_act_break: int | None = Field(
        default=None,
        description="End of Act 2 scene number",
    )
    climax: int | None = Field(default=None, description="Climax scene number")
    resolution: int | None = Field(default=None, description="Resolution scene number")
    closing_image: int | None = Field(
        default=None,
        description="Closing image scene number",
    )

    # Proportions
    act_proportions: list[float] = Field(
        default_factory=list,
        description="Percentage of script for each act",
    )
    ideal_proportions: list[float] = Field(
        default_factory=lambda: [0.25, 0.50, 0.25],
        description="Ideal proportions for structure type",
    )

    # Structural health
    pacing_notes: str | None = Field(default=None, description="Pacing analysis")
    structural_issues: list[str] = Field(
        default_factory=list,
        description="Identified structural problems",
    )


class ActAnalysis(BaseModel):
    """Analysis of a single act."""

    number: int = Field(description="Act number")
    start_scene: int = Field(description="Starting scene")
    end_scene: int = Field(description="Ending scene")
    page_count: int | None = Field(default=None, description="Page count")
    percentage: float = Field(description="Percentage of total script")

    summary: str = Field(description="Act summary")
    key_events: list[str] = Field(default_factory=list, description="Key events")
    character_movements: dict[str, str] = Field(
        default_factory=dict,
        description="Character state changes in this act",
    )


class CharacterAtlasEntry(BaseModel):
    """Entry for a single character in the atlas."""

    name: str = Field(description="Character name")
    role: str = Field(description="Narrative role")
    screen_time: float | None = Field(default=None, description="Percentage of scenes")
    first_appearance: int = Field(description="First scene number")

    # Want/Need/Lie/Truth structure
    want: str | None = Field(default=None, description="Conscious goal")
    need: str | None = Field(default=None, description="Unconscious need")
    lie: str | None = Field(default=None, description="False belief")
    truth: str | None = Field(default=None, description="Truth to learn")

    # Arc
    arc_type: ArcClassification = Field(description="Arc classification")
    arc_description: str = Field(description="Arc summary")
    key_scenes: list[int] = Field(default_factory=list, description="Key scene numbers")

    # Relationships
    relationships: list[CharacterRelationship] = Field(
        default_factory=list,
        description="Relationships to other characters",
    )


class CharacterRelationship(BaseModel):
    """A relationship between two characters."""

    character_a: str = Field(description="First character")
    character_b: str = Field(description="Second character")
    relationship_type: str = Field(description="Type (ally, rival, love, etc.)")
    description: str = Field(description="Relationship description")
    evolution: str | None = Field(
        default=None,
        description="How relationship changes",
    )


class CharacterAtlasReport(BaseModel):
    """Complete character atlas.

    Maps all characters with Want/Need analysis, arc classifications,
    and relationship networks.
    """

    title: str = Field(description="Script title")
    total_characters: int = Field(description="Total named characters")
    principal_count: int = Field(description="Principal/major characters")

    entries: list[CharacterAtlasEntry] = Field(
        default_factory=list,
        description="Character entries",
    )

    # Character network
    protagonist: str | None = Field(default=None, description="Main protagonist")
    antagonist: str | None = Field(default=None, description="Main antagonist")

    # Ensemble analysis
    ensemble_balance: str | None = Field(
        default=None,
        description="Notes on ensemble balance",
    )
    missing_archetypes: list[str] = Field(
        default_factory=list,
        description="Missing archetypal roles",
    )


class DiagnosticIssue(BaseModel):
    """A single diagnostic issue found in analysis."""

    id: str = Field(description="Issue identifier")
    severity: DiagnosticSeverity = Field(description="Issue severity")
    category: str = Field(description="Issue category (structure, character, etc.)")
    description: str = Field(description="Issue description")
    location: str | None = Field(
        default=None,
        description="Where in script (scene, act, etc.)",
    )
    recommendation: str = Field(description="Suggested fix")
    framework_source: str | None = Field(
        default=None,
        description="Which study/framework identified this",
    )


class DiagnosticReport(BaseModel):
    """Structural problems and solutions diagnostic.

    Runs diagnostic questions from studies and identifies issues
    with specific recommendations.
    """

    title: str = Field(description="Script title")
    frameworks_applied: list[str] = Field(
        default_factory=list,
        description="Studies/frameworks used for diagnosis",
    )

    # Issues
    issues: list[DiagnosticIssue] = Field(
        default_factory=list,
        description="All identified issues",
    )

    # Metrics
    causal_binding_ratio: float = Field(
        description="BUT/THEREFORE vs AND THEN ratio (target >0.80)",
    )
    reorderability_score: float = Field(
        description="How many scenes could be reordered (lower is better)",
    )
    necessity_score: float = Field(
        description="Percentage of scenes that are necessary",
    )
    information_economy_score: float = Field(
        description="Efficiency of information delivery",
    )

    # Summary
    critical_count: int = Field(description="Number of critical issues")
    warning_count: int = Field(description="Number of warnings")
    overall_health: str = Field(description="Overall script health assessment")

    # Prioritized actions
    priority_fixes: list[str] = Field(
        default_factory=list,
        description="Top priority fixes in order",
    )

    def issues_by_severity(
        self, severity: DiagnosticSeverity
    ) -> list[DiagnosticIssue]:
        """Get issues filtered by severity."""
        return [i for i in self.issues if i.severity == severity]

    def issues_by_category(self, category: str) -> list[DiagnosticIssue]:
        """Get issues filtered by category."""
        return [i for i in self.issues if i.category == category]
