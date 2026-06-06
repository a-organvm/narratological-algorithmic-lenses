"""Beat Map Report Generator.

Generates detailed scene-by-scene beat maps with function codes,
connectors, and tension analysis.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, Field

from narratological.generators.base import (
    BaseReportGenerator,
    GeneratorConfig,
    GeneratorError,
    ReportType,
)
from narratological.generators.prompts import (
    BEAT_MAP_SYSTEM_PROMPT,
    build_beat_map_prompt,
)
from narratological.generators.utils import (
    calculate_average_tension,
    calculate_connector_distribution,
    calculate_function_distribution,
    format_page_range,
)
from narratological.models.analysis import BeatFunction, ConnectorType
from narratological.models.report import BeatMapEntry, BeatMapReport

if TYPE_CHECKING:
    from narratological.llm.providers import LLMProvider
    from narratological.models.analysis import Script


class LLMBeatMapEntry(BaseModel):
    """Intermediate model for LLM beat map response."""

    scene_number: int
    function: str
    secondary_function: str | None = None
    connector: str | None = None
    tension: int = Field(ge=1, le=10)
    notes: str | None = None


class LLMBeatMapResponse(BaseModel):
    """LLM response model for beat map generation."""

    entries: list[LLMBeatMapEntry]
    function_distribution: dict[str, int] = Field(default_factory=dict)
    connector_distribution: dict[str, int] = Field(default_factory=dict)
    average_tension: float | None = None


class BeatMapReportGenerator(BaseReportGenerator[BeatMapReport]):
    """Generator for Beat Map reports.

    Creates scene-by-scene beat maps with:
    - Function codes (15 types: SETUP, INCITE, CLIMAX, etc.)
    - Connectors (BUT, THEREFORE, AND THEN, MEANWHILE)
    - Tension levels (1-10)
    - Distribution statistics

    Can operate in two modes:
    1. LLM-assisted: Full analysis using LLM provider
    2. Algorithmic: Uses existing scene annotations from Script
    """

    report_type = ReportType.BEAT_MAP

    def __init__(
        self,
        provider: LLMProvider | None = None,
        config: GeneratorConfig | None = None,
    ):
        """Initialize the beat map generator.

        Args:
            provider: LLM provider for AI-assisted analysis.
            config: Generator configuration.
        """
        super().__init__(provider, config)

    def generate(self, script: Script, **kwargs) -> BeatMapReport:
        """Generate a beat map report for the script.

        If scenes already have function annotations, uses those.
        Otherwise, uses LLM to analyze and assign functions.

        Args:
            script: The script to analyze.
            **kwargs: Additional parameters (unused currently).

        Returns:
            Complete BeatMapReport with all scene entries.

        Raises:
            GeneratorError: If generation fails.
        """
        can_gen, errors = self.can_generate(script)
        if not can_gen:
            raise GeneratorError(
                f"Cannot generate beat map: {'; '.join(errors)}",
                report_type=self.report_type,
            )

        # Check if we need LLM analysis or can use existing annotations
        if self._has_annotations(script):
            return self._generate_from_annotations(script)
        elif self.provider is not None:
            return self._generate_with_llm(script)
        else:
            # Generate minimal report from unannotated scenes
            return self._generate_minimal(script)

    def _requires_llm(self) -> bool:
        """Beat map can work without LLM if scenes are annotated."""
        return False

    def _has_annotations(self, script: Script) -> bool:
        """Check if script scenes have function annotations."""
        if not script.scenes:
            return False

        # Need at least 50% of scenes annotated
        annotated = sum(1 for s in script.scenes if s.function is not None)
        return annotated >= len(script.scenes) * 0.5

    def _generate_from_annotations(self, script: Script) -> BeatMapReport:
        """Generate report from existing scene annotations."""
        entries = []

        for scene in script.scenes:
            entry = BeatMapEntry(
                scene_number=scene.number,
                page_range=format_page_range(scene.page_start, scene.page_end),
                slug=scene.slug,
                summary=scene.summary,
                function=scene.function or BeatFunction.SETUP,
                secondary_function=scene.secondary_function,
                characters=scene.characters_present,
                connector=scene.connector_to_next,
                tension=scene.tension_level or 5,
                notes=scene.notes,
            )
            entries.append(entry)

        return self._build_report(script, entries)

    def _generate_minimal(self, script: Script) -> BeatMapReport:
        """Generate minimal report from unannotated scenes."""
        entries = []

        for scene in script.scenes:
            entry = BeatMapEntry(
                scene_number=scene.number,
                page_range=format_page_range(scene.page_start, scene.page_end),
                slug=scene.slug,
                summary=scene.summary,
                function=BeatFunction.SETUP,  # Default
                secondary_function=None,
                characters=scene.characters_present,
                connector=None,
                tension=5,  # Default middle
                notes="Auto-generated - needs analysis",
            )
            entries.append(entry)

        return self._build_report(script, entries)

    def _generate_with_llm(self, script: Script) -> BeatMapReport:
        """Generate report using LLM analysis."""
        if self.provider is None:
            raise GeneratorError(
                "LLM provider required for unannoted scripts",
                report_type=self.report_type,
            )

        system_prompt = self._build_system_prompt()
        analysis_prompt = self._build_analysis_prompt(script)

        try:
            response = self.provider.complete_structured(
                analysis_prompt,
                LLMBeatMapResponse,
                system=system_prompt,
            )
        except Exception as e:
            raise GeneratorError(
                f"LLM analysis failed: {e}",
                report_type=self.report_type,
                cause=e,
            ) from e

        entries = self._convert_llm_entries(script, response.entries)
        return self._build_report(script, entries)

    def _convert_llm_entries(
        self,
        script: Script,
        llm_entries: list[LLMBeatMapEntry],
    ) -> list[BeatMapEntry]:
        """Convert LLM response entries to BeatMapEntry objects."""
        entries = []
        scene_map = {s.number: s for s in script.scenes}

        for llm_entry in llm_entries:
            scene = scene_map.get(llm_entry.scene_number)
            if scene is None:
                continue

            # Parse function from string
            try:
                function = BeatFunction(llm_entry.function.upper())
            except ValueError:
                function = BeatFunction.SETUP

            # Parse secondary function
            secondary_function = None
            if llm_entry.secondary_function:
                try:
                    secondary_function = BeatFunction(
                        llm_entry.secondary_function.upper()
                    )
                except ValueError:
                    pass

            # Parse connector
            connector = None
            if llm_entry.connector:
                connector_map = {
                    "BUT": ConnectorType.BUT,
                    "THEREFORE": ConnectorType.THEREFORE,
                    "AND_THEN": ConnectorType.AND_THEN,
                    "AND THEN": ConnectorType.AND_THEN,
                    "MEANWHILE": ConnectorType.MEANWHILE,
                }
                connector = connector_map.get(llm_entry.connector.upper())

            entry = BeatMapEntry(
                scene_number=scene.number,
                page_range=format_page_range(scene.page_start, scene.page_end),
                slug=scene.slug,
                summary=scene.summary,
                function=function,
                secondary_function=secondary_function,
                characters=scene.characters_present,
                connector=connector,
                tension=llm_entry.tension,
                notes=llm_entry.notes,
            )
            entries.append(entry)

        return entries

    def _build_report(
        self,
        script: Script,
        entries: list[BeatMapEntry],
    ) -> BeatMapReport:
        """Build the final report from entries."""
        return BeatMapReport(
            title=script.title,
            total_scenes=len(script.scenes),
            total_pages=script.page_count,
            entries=entries,
            function_distribution=calculate_function_distribution(entries),
            connector_distribution=calculate_connector_distribution(entries),
            average_tension=calculate_average_tension(entries),
        )

    def _build_system_prompt(self) -> str:
        """Build system prompt for LLM."""
        return BEAT_MAP_SYSTEM_PROMPT

    def _build_analysis_prompt(self, script: Script) -> str:
        """Build analysis prompt for LLM."""
        return build_beat_map_prompt(script)
