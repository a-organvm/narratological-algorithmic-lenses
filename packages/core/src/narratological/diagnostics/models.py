"""Pydantic models for diagnostic runners.

These models represent the context, assessments, and results
for structural diagnostic tests.
"""

from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field

from narratological.models.analysis import ConnectorType
from narratological.models.report import DiagnosticIssue, DiagnosticSeverity


class DiagnosticType(str, Enum):
    """Types of diagnostic tests available."""

    CAUSAL_BINDING = "causal_binding"
    REORDERABILITY = "reorderability"
    NECESSITY = "necessity"
    INFORMATION_ECONOMY = "information_economy"
    FRAMEWORK = "framework"


class SceneTransition(BaseModel):
    """Represents a transition between two scenes.

    Used for causal binding analysis.
    """

    from_scene: int = Field(description="Source scene number")
    to_scene: int = Field(description="Target scene number")
    connector: ConnectorType | None = Field(
        default=None,
        description="Connector type (BUT, THEREFORE, AND_THEN, MEANWHILE)",
    )
    explanation: str | None = Field(
        default=None,
        description="Why this connector type applies",
    )
    is_causal: bool = Field(
        default=False,
        description="Whether the transition is causally bound",
    )


class ReorderabilityAssessment(BaseModel):
    """Assessment of whether a scene could be reordered.

    Scenes that can be moved without affecting narrative logic
    indicate weak causal binding.
    """

    scene_number: int = Field(description="Scene being assessed")
    is_reorderable: bool = Field(
        description="Whether the scene could be moved without narrative damage"
    )
    constraints: list[int] = Field(
        default_factory=list,
        description="Scene numbers this scene depends on",
    )
    dependents: list[int] = Field(
        default_factory=list,
        description="Scene numbers that depend on this scene",
    )
    reason: str | None = Field(
        default=None,
        description="Explanation of reorderability assessment",
    )
    alternative_positions: list[int] = Field(
        default_factory=list,
        description="Other positions this scene could occupy",
    )


class NecessityAssessment(BaseModel):
    """Assessment of whether a scene is necessary.

    Scenes that could be removed without losing essential
    information indicate potential redundancy.
    """

    scene_number: int = Field(description="Scene being assessed")
    is_necessary: bool = Field(
        description="Whether the scene is essential to the narrative"
    )
    narrative_functions: list[str] = Field(
        default_factory=list,
        description="Functions this scene serves",
    )
    unique_information: list[str] = Field(
        default_factory=list,
        description="Information only available in this scene",
    )
    removal_impact: str | None = Field(
        default=None,
        description="What would be lost if this scene were cut",
    )
    redundant_with: list[int] = Field(
        default_factory=list,
        description="Scene numbers that could cover this scene's content",
    )


class InformationUnit(BaseModel):
    """A unit of information delivery in the script.

    Tracks setup-payoff patterns and exposition efficiency.
    """

    content: str = Field(description="What information is conveyed")
    introduced_scene: int = Field(description="Where first introduced")
    payoff_scenes: list[int] = Field(
        default_factory=list,
        description="Where the information pays off",
    )
    is_redundant: bool = Field(
        default=False,
        description="Whether information is repeated unnecessarily",
    )
    redundant_scenes: list[int] = Field(
        default_factory=list,
        description="Scenes where information is unnecessarily repeated",
    )


class DiagnosticContext(BaseModel):
    """Context for running diagnostic tests.

    Contains all necessary data for structural analysis.
    """

    title: str = Field(description="Script title")
    scenes: list[dict] = Field(
        default_factory=list,
        description="Scene data with summaries, functions, connectors",
    )
    characters: list[str] = Field(
        default_factory=list,
        description="Character names",
    )
    active_studies: list[str] = Field(
        default_factory=list,
        description="Study IDs to use for framework diagnostics",
    )

    # Pre-computed analysis if available
    transitions: list[SceneTransition] = Field(
        default_factory=list,
        description="Pre-computed scene transitions",
    )
    beat_map_available: bool = Field(
        default=False,
        description="Whether beat map data is available",
    )

    @classmethod
    def from_script(cls, script) -> DiagnosticContext:
        """Create context from a Script model."""
        scenes = []
        for s in script.scenes:
            scenes.append({
                "number": s.number,
                "slug": s.slug,
                "summary": s.summary,
                "function": s.function.value if s.function else None,
                "connector": s.connector_to_next.value if s.connector_to_next else None,
                "characters": s.characters_present,
                "tension": s.tension_level,
            })

        characters = [c.name for c in script.characters] if script.characters else []

        return cls(
            title=script.title,
            scenes=scenes,
            characters=characters,
            beat_map_available=any(s.get("function") for s in scenes),
        )


class DiagnosticThresholds(BaseModel):
    """Thresholds for diagnostic severity classification.

    Based on the templates from SKILL.md methodology.
    """

    # Causal binding thresholds
    # Empirically derived from Open View analysis:
    # Draft 1 (Episodic) = 27%
    # Draft 2 (Tightly Wound) = 78%
    causal_binding_excellent: float = Field(
        default=0.80,
        description="Above this = excellent (South Park ideal)",
    )
    causal_binding_good: float = Field(
        default=0.60,
        description="Above this = good (Professional standard)",
    )
    causal_binding_adequate: float = Field(
        default=0.30,
        description="Above this = adequate, below = episodic/loose",
    )
    causal_binding_critical: float = Field(
        default=0.15,
        description="Below this = broken/disconnected",
    )

    # Reorderability thresholds (lower is better)
    reorderability_excellent: float = Field(
        default=0.05,
        description="Below this = excellent",
    )
    reorderability_good: float = Field(
        default=0.15,
        description="Below this = good",
    )
    reorderability_warning: float = Field(
        default=0.30,
        description="Above this = warning",
    )
    reorderability_critical: float = Field(
        default=0.50,
        description="Above this = critical",
    )

    # Necessity thresholds (higher is better)
    necessity_excellent: float = Field(
        default=0.95,
        description="Above this = excellent",
    )
    necessity_good: float = Field(
        default=0.85,
        description="Above this = good",
    )
    necessity_warning: float = Field(
        default=0.70,
        description="Below this = warning",
    )
    necessity_critical: float = Field(
        default=0.50,
        description="Below this = critical",
    )

    # Information economy thresholds (higher is better)
    info_economy_excellent: float = Field(
        default=0.90,
        description="Above this = excellent",
    )
    info_economy_good: float = Field(
        default=0.75,
        description="Above this = good",
    )
    info_economy_warning: float = Field(
        default=0.60,
        description="Below this = warning",
    )
    info_economy_critical: float = Field(
        default=0.40,
        description="Below this = critical",
    )


class DiagnosticMetrics(BaseModel):
    """Computed metrics from diagnostic tests."""

    causal_binding_ratio: float = Field(
        default=0.0,
        description="BUT/THEREFORE vs AND THEN ratio (0-1)",
    )
    reorderability_score: float = Field(
        default=0.0,
        description="Proportion of reorderable scenes (0-1, lower is better)",
    )
    necessity_score: float = Field(
        default=1.0,
        description="Proportion of necessary scenes (0-1, higher is better)",
    )
    information_economy_score: float = Field(
        default=1.0,
        description="Information efficiency score (0-1, higher is better)",
    )

    # Derived health indicators
    causal_binding_health: str = Field(default="unknown")
    reorderability_health: str = Field(default="unknown")
    necessity_health: str = Field(default="unknown")
    information_economy_health: str = Field(default="unknown")
    overall_health: str = Field(default="unknown")

    def compute_health(self, thresholds: DiagnosticThresholds | None = None) -> None:
        """Compute health indicators from scores using thresholds."""
        thresholds = thresholds or DiagnosticThresholds()

        # Causal binding health
        if self.causal_binding_ratio >= thresholds.causal_binding_excellent:
            self.causal_binding_health = "Excellent"
        elif self.causal_binding_ratio >= thresholds.causal_binding_good:
            self.causal_binding_health = "Good"
        elif self.causal_binding_ratio >= thresholds.causal_binding_adequate:
            self.causal_binding_health = "Adequate"
        elif self.causal_binding_ratio >= thresholds.causal_binding_critical:
            self.causal_binding_health = "Warning"
        else:
            self.causal_binding_health = "Critical"

        # Reorderability health (lower is better)
        if self.reorderability_score <= thresholds.reorderability_excellent:
            self.reorderability_health = "Excellent"
        elif self.reorderability_score <= thresholds.reorderability_good:
            self.reorderability_health = "Good"
        elif self.reorderability_score <= thresholds.reorderability_warning:
            self.reorderability_health = "Adequate"
        elif self.reorderability_score <= thresholds.reorderability_critical:
            self.reorderability_health = "Warning"
        else:
            self.reorderability_health = "Critical"

        # Necessity health (higher is better)
        if self.necessity_score >= thresholds.necessity_excellent:
            self.necessity_health = "Excellent"
        elif self.necessity_score >= thresholds.necessity_good:
            self.necessity_health = "Good"
        elif self.necessity_score >= thresholds.necessity_warning:
            self.necessity_health = "Adequate"
        else:
            self.necessity_health = "Warning" if self.necessity_score >= thresholds.necessity_critical else "Critical"

        # Information economy health (higher is better)
        if self.information_economy_score >= thresholds.info_economy_excellent:
            self.information_economy_health = "Excellent"
        elif self.information_economy_score >= thresholds.info_economy_good:
            self.information_economy_health = "Good"
        elif self.information_economy_score >= thresholds.info_economy_warning:
            self.information_economy_health = "Adequate"
        else:
            self.information_economy_health = "Warning" if self.information_economy_score >= thresholds.info_economy_critical else "Critical"

        # Overall health (weighted average)
        health_scores = {
            "Excellent": 5,
            "Good": 4,
            "Adequate": 3,
            "Warning": 2,
            "Critical": 1,
        }

        healths = [
            self.causal_binding_health,
            self.reorderability_health,
            self.necessity_health,
            self.information_economy_health,
        ]

        avg_score = sum(health_scores.get(h, 0) for h in healths) / len(healths)

        if avg_score >= 4.5:
            self.overall_health = "Excellent"
        elif avg_score >= 3.5:
            self.overall_health = "Good"
        elif avg_score >= 2.5:
            self.overall_health = "Fair"
        elif avg_score >= 1.5:
            self.overall_health = "Poor"
        else:
            self.overall_health = "Critical"
