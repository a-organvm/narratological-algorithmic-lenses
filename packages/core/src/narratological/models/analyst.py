"""Pydantic models for the 8-role analyst system.

These models represent the analytical perspectives and their outputs
for multi-dimensional script analysis.
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class AnalystRole(str, Enum):
    """The nine analyst roles for multi-perspective analysis.

    Each role brings a distinct analytical lens to script evaluation,
    based on the SKILL.md methodology.
    """

    AESTHETE = "aesthete"  # Form, beauty, style, sensory patterns
    DRAMATURGIST = "dramaturgist"  # Structure, rhythm, dramatic tension
    NARRATOLOGIST = "narratologist"  # Narrative mechanisms, causal binding
    ART_HISTORIAN = "art_historian"  # Historical context, influences, lineages
    CINEPHILE = "cinephile"  # Comparable works, genre conventions
    RHETORICIAN = "rhetorician"  # Argument structure, dialogue craft
    PRODUCER = "producer"  # Practical feasibility, budget implications
    ACADEMIC = "academic"  # Theoretical frameworks, rigor
    FIRST_READER = "first_reader"  # Emotional response, engagement


# Mapping of roles to their primary studies from the compendium
ROLE_STUDY_MAPPING: dict[AnalystRole, list[str]] = {
    AnalystRole.AESTHETE: ["tarkovsky", "bergman", "david-lynch"],
    AnalystRole.DRAMATURGIST: ["pixar", "tarantino"],
    AnalystRole.NARRATOLOGIST: ["pixar", "ovid-metamorphoses"],
    AnalystRole.ART_HISTORIAN: ["kirby-new-gods", "tolkien"],
    AnalystRole.CINEPHILE: [],  # Genre knowledge, not study-specific
    AnalystRole.RHETORICIAN: ["alan-moore", "morrison"],
    AnalystRole.PRODUCER: [],  # Practical knowledge, not study-specific
    AnalystRole.ACADEMIC: [],  # Uses all studies
    AnalystRole.FIRST_READER: ["pixar"],  # Emotional engineering
}


class AnalystObservation(BaseModel):
    """A single observation from an analyst role.

    Observations are the atomic units of analysis, each tied to
    a specific location or aspect of the script.
    """

    role: AnalystRole = Field(description="Which analyst role made this observation")
    category: str = Field(description="Observation category (structure, character, etc.)")
    observation: str = Field(description="The observation content")
    location: str | None = Field(
        default=None,
        description="Where in the script (scene, act, page)",
    )
    confidence: float = Field(
        default=0.8,
        ge=0.0,
        le=1.0,
        description="Confidence level (0.0-1.0)",
    )
    evidence: list[str] = Field(
        default_factory=list,
        description="Supporting evidence from the script",
    )
    framework_source: str | None = Field(
        default=None,
        description="Which study/framework informs this observation",
    )


class RoleAnalysisResult(BaseModel):
    """Complete analysis result from a single analyst role.

    Contains all observations and assessments from one analytical perspective.
    """

    role: AnalystRole = Field(description="The analyst role")
    summary: str = Field(description="Executive summary of this role's analysis")
    observations: list[AnalystObservation] = Field(
        default_factory=list,
        description="All observations from this role",
    )
    key_findings: list[str] = Field(
        default_factory=list,
        description="Most important findings",
    )
    recommendations: list[str] = Field(
        default_factory=list,
        description="Suggestions for improvement",
    )
    score: float | None = Field(
        default=None,
        ge=0.0,
        le=10.0,
        description="Overall score from this role (0-10)",
    )
    frameworks_applied: list[str] = Field(
        default_factory=list,
        description="Studies/frameworks used in analysis",
    )
    raw_output: str = Field(
        default="",
        description="Raw LLM output for debugging",
    )

    def observation_count_by_category(self) -> dict[str, int]:
        """Count observations by category."""
        counts: dict[str, int] = {}
        for obs in self.observations:
            counts[obs.category] = counts.get(obs.category, 0) + 1
        return counts


class ActivationLayer(str, Enum):
    """Activation layers for multi-role orchestration.

    Controls which roles are activated for analysis, allowing
    for quick/full analysis modes.
    """

    ESSENTIAL = "essential"  # Dramaturgist, Narratologist, First-Reader
    CREATIVE = "creative"  # + Aesthete, Rhetorician
    CONTEXTUAL = "contextual"  # + Art Historian, Cinephile
    PRACTICAL = "practical"  # + Producer
    FULL = "full"  # All roles including Academic

    @property
    def roles(self) -> list[AnalystRole]:
        """Get the roles activated in this layer."""
        layer_roles = {
            ActivationLayer.ESSENTIAL: [
                AnalystRole.DRAMATURGIST,
                AnalystRole.NARRATOLOGIST,
                AnalystRole.FIRST_READER,
            ],
            ActivationLayer.CREATIVE: [
                AnalystRole.DRAMATURGIST,
                AnalystRole.NARRATOLOGIST,
                AnalystRole.FIRST_READER,
                AnalystRole.AESTHETE,
                AnalystRole.RHETORICIAN,
            ],
            ActivationLayer.CONTEXTUAL: [
                AnalystRole.DRAMATURGIST,
                AnalystRole.NARRATOLOGIST,
                AnalystRole.FIRST_READER,
                AnalystRole.AESTHETE,
                AnalystRole.RHETORICIAN,
                AnalystRole.ART_HISTORIAN,
                AnalystRole.CINEPHILE,
            ],
            ActivationLayer.PRACTICAL: [
                AnalystRole.DRAMATURGIST,
                AnalystRole.NARRATOLOGIST,
                AnalystRole.FIRST_READER,
                AnalystRole.AESTHETE,
                AnalystRole.RHETORICIAN,
                AnalystRole.ART_HISTORIAN,
                AnalystRole.CINEPHILE,
                AnalystRole.PRODUCER,
            ],
            ActivationLayer.FULL: list(AnalystRole),
        }
        return layer_roles[self]


class SynthesisConfig(BaseModel):
    """Configuration for multi-role synthesis."""

    activation_layer: ActivationLayer = Field(
        default=ActivationLayer.ESSENTIAL,
        description="Which roles to activate",
    )
    parallel_execution: bool = Field(
        default=True,
        description="Execute role analyses in parallel",
    )
    include_raw_outputs: bool = Field(
        default=False,
        description="Include raw LLM outputs in results",
    )
    active_studies: list[str] = Field(
        default_factory=list,
        description="Specific studies to emphasize",
    )
    synthesis_depth: str = Field(
        default="standard",
        description="Synthesis depth: quick, standard, or deep",
    )


class CoAuthoringPair(BaseModel):
    """A pair of creators acting as collaborative 'Script Doctors'.

    Uses Sequence Pairs from the compendium to drive synthesis.
    """

    primary_id: str = Field(description="First creator/study ID")
    secondary_id: str = Field(description="Second creator/study ID")
    theme: str | None = Field(default=None, description="The unifying theme of this pair")
    synergy_instruction: str | None = Field(
        default=None,
        description="Specific instructions on how these two should collaborate",
    )


class ScriptDoctorResult(BaseModel):
    """The output of a Script Doctor analysis pass.

    Synthesizes feedback as a collaborative dialogue between creators.
    """

    pair: CoAuthoringPair
    dialogue: list[dict[str, str]] = Field(
        description="Collaborative feedback formatted as a dialogue (creator: feedback)"
    )
    joint_recommendations: list[str] = Field(
        description="Merged recommendations agreed upon by both creators"
    )
    creative_tension: list[str] = Field(
        description="Areas where the creators' philosophies diverge regarding the script"
    )
    final_prescription: str = Field(description="The singular 'next step' for the writer")


class MultiRoleAnalysis(BaseModel):
    """Complete multi-role analysis result.

    Synthesizes insights from multiple analyst perspectives into
    a unified assessment.
    """

    title: str = Field(description="Script title")
    date: datetime = Field(default_factory=datetime.now)

    # Individual role results
    role_results: dict[str, RoleAnalysisResult] = Field(
        default_factory=dict,
        description="Results keyed by role name",
    )

    # Synthesized insights
    consensus_observations: list[AnalystObservation] = Field(
        default_factory=list,
        description="Observations agreed upon by multiple roles",
    )
    divergent_observations: list[AnalystObservation] = Field(
        default_factory=list,
        description="Observations where roles disagree",
    )

    # Overall assessment
    overall_summary: str = Field(
        default="",
        description="Synthesized summary from all roles",
    )
    overall_score: float | None = Field(
        default=None,
        description="Weighted average score",
    )
    priority_recommendations: list[str] = Field(
        default_factory=list,
        description="Top recommendations across all roles",
    )

    # Metadata
    config: SynthesisConfig = Field(
        default_factory=SynthesisConfig,
        description="Configuration used for this analysis",
    )
    execution_time_ms: int | None = Field(
        default=None,
        description="Total execution time in milliseconds",
    )

    def get_role_result(self, role: AnalystRole | str) -> RoleAnalysisResult | None:
        """Get result for a specific role."""
        if isinstance(role, AnalystRole):
            role = role.value
        return self.role_results.get(role)

    def get_all_observations(self) -> list[AnalystObservation]:
        """Get all observations from all roles."""
        observations = []
        for result in self.role_results.values():
            observations.extend(result.observations)
        return observations

    def observations_by_category(self) -> dict[str, list[AnalystObservation]]:
        """Group all observations by category."""
        by_category: dict[str, list[AnalystObservation]] = {}
        for obs in self.get_all_observations():
            if obs.category not in by_category:
                by_category[obs.category] = []
            by_category[obs.category].append(obs)
        return by_category

    def role_count(self) -> int:
        """Get number of roles that provided analysis."""
        return len(self.role_results)

    def average_score(self) -> float | None:
        """Calculate average score across all roles."""
        scores = [
            r.score for r in self.role_results.values()
            if r.score is not None
        ]
        if not scores:
            return None
        return sum(scores) / len(scores)


class AnalystContext(BaseModel):
    """Context provided to analyst roles for analysis.

    Contains the script content and metadata needed for analysis.
    """

    title: str = Field(description="Script title")
    text: str = Field(description="Full script text or summary")
    genre: str | None = Field(default=None, description="Primary genre")
    tone: str | None = Field(default=None, description="Tonal register")
    format: str = Field(default="Feature", description="Script format")
    page_count: int | None = Field(default=None, description="Page count")

    # Structured data if available
    scene_summaries: list[str] = Field(
        default_factory=list,
        description="Brief summaries of each scene",
    )
    character_list: list[str] = Field(
        default_factory=list,
        description="Names of characters",
    )

    # Analysis parameters
    focus_areas: list[str] = Field(
        default_factory=list,
        description="Specific areas to focus analysis on",
    )
    previous_analyses: dict[str, Any] = Field(
        default_factory=dict,
        description="Results from previous analysis passes",
    )

    @classmethod
    def from_script(cls, script) -> AnalystContext:
        """Create context from a Script model."""
        scene_summaries = [s.summary for s in script.scenes] if script.scenes else []
        character_list = [c.name for c in script.characters] if script.characters else []

        return cls(
            title=script.title,
            text=script.logline or "",
            genre=script.primary_genre,
            tone=script.tone,
            format=script.format,
            page_count=script.page_count,
            scene_summaries=scene_summaries,
            character_list=character_list,
        )
