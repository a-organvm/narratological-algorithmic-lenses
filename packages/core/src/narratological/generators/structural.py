"""Structural Report Generator.

Generates act-by-act structural analysis with key dramatic points,
proportions, and pacing assessment.
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
    STRUCTURAL_SYSTEM_PROMPT,
    build_structural_prompt,
)
from narratological.generators.utils import (
    get_ideal_proportions,
)
from narratological.models.report import ActAnalysis, StructuralReport

if TYPE_CHECKING:
    from narratological.llm.providers import LLMProvider
    from narratological.models.analysis import Script


class LLMActAnalysis(BaseModel):
    """Intermediate model for LLM act analysis."""

    number: int
    start_scene: int
    end_scene: int
    percentage: float
    summary: str
    key_events: list[str] = Field(default_factory=list)
    character_movements: dict[str, str] = Field(default_factory=dict)


class LLMStructuralResponse(BaseModel):
    """LLM response model for structural analysis."""

    structure_type: str
    act_count: int
    acts: list[LLMActAnalysis]

    opening_image: int | None = None
    inciting_incident: int | None = None
    first_act_break: int | None = None
    midpoint: int | None = None
    all_is_lost: int | None = None
    second_act_break: int | None = None
    climax: int | None = None
    resolution: int | None = None
    closing_image: int | None = None

    act_proportions: list[float] = Field(default_factory=list)
    pacing_notes: str | None = None
    structural_issues: list[str] = Field(default_factory=list)


class StructuralReportGenerator(BaseReportGenerator[StructuralReport]):
    """Generator for Structural reports.

    Analyzes dramatic architecture:
    - Act boundaries and structure type (Three-Act, Five-Act, etc.)
    - Key structural points (inciting incident, midpoint, climax)
    - Act proportions vs ideal proportions
    - Pacing assessment and structural issues

    Requires LLM for meaningful analysis unless acts are pre-annotated.
    """

    report_type = ReportType.STRUCTURAL

    def __init__(
        self,
        provider: LLMProvider | None = None,
        config: GeneratorConfig | None = None,
    ):
        """Initialize the structural report generator.

        Args:
            provider: LLM provider for analysis.
            config: Generator configuration.
        """
        super().__init__(provider, config)

    def generate(self, script: Script, **kwargs) -> StructuralReport:
        """Generate a structural analysis report.

        Args:
            script: The script to analyze.
            **kwargs: Additional parameters:
                - structure_type: Override default structure type

        Returns:
            Complete StructuralReport with act analysis.

        Raises:
            GeneratorError: If generation fails.
        """
        can_gen, errors = self.can_generate(script)
        if not can_gen:
            raise GeneratorError(
                f"Cannot generate structural report: {'; '.join(errors)}",
                report_type=self.report_type,
            )

        structure_type = kwargs.get("structure_type", self.config.structure_type)

        # Check if we can use existing act annotations
        if self._has_act_annotations(script):
            return self._generate_from_annotations(script, structure_type)
        elif self.provider is not None:
            return self._generate_with_llm(script, structure_type)
        else:
            raise GeneratorError(
                "Structural report requires either act annotations or LLM provider",
                report_type=self.report_type,
            )

    def _requires_llm(self) -> bool:
        """Structural analysis typically requires LLM."""
        return True

    def _validate_prerequisites(self, script: Script) -> list[str]:
        """Validate script has required data."""
        errors = super()._validate_prerequisites(script)

        if not script.scenes:
            errors.append("Script must have scenes for structural analysis")

        return errors

    def _has_act_annotations(self, script: Script) -> bool:
        """Check if script has act structure annotations."""
        return len(script.acts) > 0

    def _generate_from_annotations(
        self,
        script: Script,
        structure_type: str,
    ) -> StructuralReport:
        """Generate report from existing act annotations."""
        total_scenes = len(script.scenes)

        acts = []
        for act in script.acts:
            act_scenes = act.end_scene - act.start_scene + 1
            percentage = act_scenes / total_scenes if total_scenes > 0 else 0

            acts.append(
                ActAnalysis(
                    number=act.number,
                    start_scene=act.start_scene,
                    end_scene=act.end_scene,
                    page_count=None,  # Would need page info
                    percentage=percentage,
                    summary=act.summary,
                    key_events=[],  # Would need extraction
                    character_movements={},
                )
            )

        # Calculate proportions
        act_proportions = [a.percentage for a in acts]

        # Extract structural points from acts
        inciting_incident = None
        midpoint = None
        climax = None

        for act in script.acts:
            if act.inciting_incident:
                inciting_incident = act.inciting_incident
            if act.midpoint:
                midpoint = act.midpoint
            if act.climax:
                climax = act.climax

        return StructuralReport(
            title=script.title,
            structure_type=structure_type,
            act_count=len(acts),
            acts=acts,
            inciting_incident=inciting_incident,
            midpoint=midpoint,
            climax=climax,
            act_proportions=act_proportions,
            ideal_proportions=get_ideal_proportions(structure_type),
            structural_issues=self._analyze_proportion_issues(
                act_proportions,
                get_ideal_proportions(structure_type),
            ),
        )

    def _generate_with_llm(
        self,
        script: Script,
        structure_type: str,
    ) -> StructuralReport:
        """Generate report using LLM analysis."""
        if self.provider is None:
            raise GeneratorError(
                "LLM provider required for structural analysis",
                report_type=self.report_type,
            )

        system_prompt = self._build_system_prompt()
        analysis_prompt = self._build_analysis_prompt(script)

        try:
            response = self.provider.complete_structured(
                analysis_prompt,
                LLMStructuralResponse,
                system=system_prompt,
            )
        except Exception as e:
            raise GeneratorError(
                f"LLM analysis failed: {e}",
                report_type=self.report_type,
                cause=e,
            ) from e

        return self._convert_llm_response(script, response)

    def _convert_llm_response(
        self,
        script: Script,
        response: LLMStructuralResponse,
    ) -> StructuralReport:
        """Convert LLM response to StructuralReport."""
        acts = []
        for llm_act in response.acts:
            acts.append(
                ActAnalysis(
                    number=llm_act.number,
                    start_scene=llm_act.start_scene,
                    end_scene=llm_act.end_scene,
                    page_count=None,
                    percentage=llm_act.percentage,
                    summary=llm_act.summary,
                    key_events=llm_act.key_events,
                    character_movements=llm_act.character_movements,
                )
            )

        return StructuralReport(
            title=script.title,
            structure_type=response.structure_type,
            act_count=response.act_count,
            acts=acts,
            opening_image=response.opening_image,
            inciting_incident=response.inciting_incident,
            first_act_break=response.first_act_break,
            midpoint=response.midpoint,
            all_is_lost=response.all_is_lost,
            second_act_break=response.second_act_break,
            climax=response.climax,
            resolution=response.resolution,
            closing_image=response.closing_image,
            act_proportions=response.act_proportions,
            ideal_proportions=get_ideal_proportions(response.structure_type),
            pacing_notes=response.pacing_notes,
            structural_issues=response.structural_issues,
        )

    def _analyze_proportion_issues(
        self,
        actual: list[float],
        ideal: list[float],
    ) -> list[str]:
        """Analyze proportion deviations and generate issues."""
        issues = []

        if len(actual) != len(ideal):
            issues.append(
                f"Act count mismatch: expected {len(ideal)} acts, found {len(actual)}"
            )
            return issues

        for i, (act_prop, ideal_prop) in enumerate(zip(actual, ideal, strict=False)):
            deviation = abs(act_prop - ideal_prop)
            if deviation > 0.10:  # 10% deviation threshold
                if act_prop > ideal_prop:
                    issues.append(
                        f"Act {i + 1} is {deviation * 100:.0f}% longer than ideal"
                    )
                else:
                    issues.append(
                        f"Act {i + 1} is {deviation * 100:.0f}% shorter than ideal"
                    )

        return issues

    def _build_system_prompt(self) -> str:
        """Build system prompt for LLM."""
        return STRUCTURAL_SYSTEM_PROMPT

    def _build_analysis_prompt(self, script: Script) -> str:
        """Build analysis prompt for LLM."""
        return build_structural_prompt(script, self.config.structure_type)
