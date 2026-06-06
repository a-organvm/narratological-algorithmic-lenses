"""Pydantic models for script/narrative analysis.

These models represent the structures used when analyzing scripts
and stories using the narratological algorithms.
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field


class BeatFunction(StrEnum):
    """Scene/beat function codes based on the SKILL.md methodology.

    These 15 codes classify the narrative function of each scene or beat.
    """

    SETUP = "SETUP"  # Establishing information
    INCITE = "INCITE"  # Inciting incident
    COMPLICATE = "COMPLICATE"  # Adding complexity
    ESCALATE = "ESCALATE"  # Raising stakes
    REVEAL = "REVEAL"  # Information disclosure
    CRISIS = "CRISIS"  # Decision point
    CLIMAX = "CLIMAX"  # Peak of action/emotion
    RESOLVE = "RESOLVE"  # Resolution
    TRANSITION = "TRANSITION"  # Scene/act connector
    BREATHE = "BREATHE"  # Pacing relief
    PLANT = "PLANT"  # Setup for payoff
    PAYOFF = "PAYOFF"  # Delivery of setup
    MIRROR = "MIRROR"  # Thematic echo
    SUBPLOT = "SUBPLOT"  # Secondary story
    CODA = "CODA"  # Ending commentary


class ArcClassification(StrEnum):
    """Character arc types based on transformation patterns."""

    POSITIVE = "positive"  # Growth toward better state
    NEGATIVE = "negative"  # Decline toward worse state
    FLAT = "flat"  # No change, tests existing beliefs
    CORRUPTED = "corrupted"  # Twisted positive to negative
    REDEEMED = "redeemed"  # Recovered from negative to positive


class ConnectorType(StrEnum):
    """Scene connector types for causal binding analysis.

    Based on the South Park "therefore" rule: BUT/THEREFORE indicates
    strong causal binding, AND THEN indicates weak episodic structure.
    """

    BUT = "BUT"  # Contradiction/obstacle
    THEREFORE = "THEREFORE"  # Direct consequence
    AND_THEN = "AND THEN"  # Sequential but not causal
    MEANWHILE = "MEANWHILE"  # Parallel action


class Script(BaseModel):
    """A script or story being analyzed."""

    title: str = Field(description="Script title")
    draft: str | None = Field(default=None, description="Draft version/date")
    format: str = Field(
        default="Feature",
        description="Format: Feature, Pilot, Limited Series, Short",
    )
    page_count: int | None = Field(default=None, description="Total pages")
    scene_count: int | None = Field(default=None, description="Total scenes")
    time_span: str | None = Field(default=None, description="Diegetic duration")
    primary_genre: str | None = Field(default=None, description="Main genre")
    tone: str | None = Field(default=None, description="Dominant tonal register")
    logline: str | None = Field(default=None, description="One-line summary")

    scenes: list[Scene] = Field(default_factory=list, description="All scenes")
    characters: list[Character] = Field(default_factory=list, description="All characters")
    acts: list[Act] = Field(default_factory=list, description="Act structure")


class Scene(BaseModel):
    """A single scene in a script."""

    number: int = Field(description="Scene number")
    slug: str = Field(description="Scene heading/slug line")
    page_start: int | None = Field(default=None, description="Starting page")
    page_end: int | None = Field(default=None, description="Ending page")
    summary: str = Field(description="Brief scene summary")

    # Analysis fields
    function: BeatFunction | None = Field(default=None, description="Primary beat function")
    secondary_function: BeatFunction | None = Field(
        default=None,
        description="Secondary function if applicable",
    )
    characters_present: list[str] = Field(
        default_factory=list,
        description="Characters appearing in scene",
    )
    connector_to_next: ConnectorType | None = Field(
        default=None,
        description="How this scene connects to the next",
    )
    tension_level: int | None = Field(
        default=None,
        ge=1,
        le=10,
        description="Tension level 1-10",
    )
    notes: str | None = Field(default=None, description="Analysis notes")

    # Role-specific observations (from 8-role analyst system)
    role_observations: dict[str, str] = Field(
        default_factory=dict,
        description="Observations tagged by analyst role",
    )


class Beat(BaseModel):
    """A micro-unit of dramatic action within a scene.

    Beats are the smallest unit of narrative change - a shift in
    value, power, or information.
    """

    scene_number: int = Field(description="Parent scene number")
    beat_number: int = Field(description="Beat number within scene")
    description: str = Field(description="What happens in this beat")
    function: BeatFunction = Field(description="Beat function")
    value_shift: str | None = Field(
        default=None,
        description="What value changes (e.g., 'hope -> despair')",
    )
    information_shift: str | None = Field(
        default=None,
        description="What information changes hands",
    )


class Character(BaseModel):
    """A character in the analyzed script."""

    name: str = Field(description="Character name")
    role: str = Field(description="Narrative role (protagonist, antagonist, etc.)")
    description: str = Field(description="Brief character description")
    first_appearance: int | None = Field(default=None, description="First scene number")

    # Want vs Need (McKee/story structure)
    want: str | None = Field(default=None, description="Conscious external goal")
    need: str | None = Field(default=None, description="Unconscious internal need")
    lie: str | None = Field(default=None, description="False belief character holds")
    truth: str | None = Field(default=None, description="Truth character must learn")

    # Arc analysis
    arc_classification: ArcClassification | None = Field(
        default=None,
        description="Type of character arc",
    )
    arc_summary: str | None = Field(default=None, description="Summary of transformation")

    # Key scenes
    introduction_scene: int | None = Field(
        default=None,
        description="Scene where character is introduced",
    )
    crisis_scene: int | None = Field(
        default=None,
        description="Scene of character's major crisis",
    )
    transformation_scene: int | None = Field(
        default=None,
        description="Scene where transformation completes",
    )

    # Relationships
    relationships: dict[str, str] = Field(
        default_factory=dict,
        description="Relationships to other characters",
    )


class Act(BaseModel):
    """An act in the dramatic structure."""

    number: int = Field(description="Act number")
    name: str | None = Field(default=None, description="Act name if applicable")
    start_scene: int = Field(description="Starting scene number")
    end_scene: int = Field(description="Ending scene number")
    summary: str = Field(description="Act summary")

    # Structural markers
    inciting_incident: int | None = Field(
        default=None,
        description="Scene number of inciting incident (Act 1)",
    )
    midpoint: int | None = Field(
        default=None,
        description="Scene number of midpoint (Act 2)",
    )
    crisis: int | None = Field(
        default=None,
        description="Scene number of crisis",
    )
    climax: int | None = Field(
        default=None,
        description="Scene number of climax",
    )


class ThematicElement(BaseModel):
    """A thematic element tracked across the script."""

    name: str = Field(description="Theme or motif name")
    statement: str = Field(description="Thematic statement or question")
    instances: list[int] = Field(
        default_factory=list,
        description="Scene numbers where theme appears",
    )
    resolution: str | None = Field(default=None, description="How theme resolves")


class AnalysisContext(BaseModel):
    """Context for applying narratological frameworks to a script.

    Links a script to the studies being used for analysis and
    tracks which frameworks are active.
    """

    script: Script = Field(description="The script being analyzed")
    active_studies: list[str] = Field(
        default_factory=list,
        description="IDs of studies being applied",
    )
    primary_framework: str | None = Field(
        default=None,
        description="Primary study/framework for analysis",
    )
    analysis_metadata: dict[str, Any] = Field(
        default_factory=dict,
        description="Additional analysis metadata",
    )
