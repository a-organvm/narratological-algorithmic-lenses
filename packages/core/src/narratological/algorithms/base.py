"""Base classes for executable algorithms.

Wraps the Algorithm model from study.py and adds execution capabilities
for analysis, generation, and validation using LLM providers.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import TYPE_CHECKING, Any

from pydantic import BaseModel, Field

from narratological.models.study import Algorithm

if TYPE_CHECKING:
    from narratological.llm.providers import LLMProvider


class ExecutionMode(StrEnum):
    """Mode of algorithm execution."""

    ANALYZE = "analyze"
    GENERATE = "generate"
    VALIDATE = "validate"


class AnalysisResult(BaseModel):
    """Result from analyzing text with an algorithm."""

    algorithm_name: str = Field(description="Name of the algorithm applied")
    study_id: str = Field(description="ID of the study this algorithm belongs to")
    input_summary: str = Field(description="Brief summary of the analyzed input")
    findings: list[str] = Field(
        default_factory=list,
        description="Key findings from the analysis",
    )
    elements_identified: dict[str, Any] = Field(
        default_factory=dict,
        description="Narrative elements identified based on algorithm outputs",
    )
    recommendations: list[str] = Field(
        default_factory=list,
        description="Suggestions for improving the narrative",
    )
    score: float | None = Field(
        default=None,
        description="Optional score (0-1) indicating how well input matches algorithm criteria",
    )
    raw_output: str = Field(
        default="",
        description="Raw LLM output for debugging",
    )


class GenerationResult(BaseModel):
    """Result from generating content with an algorithm."""

    algorithm_name: str = Field(description="Name of the algorithm used")
    study_id: str = Field(description="ID of the study this algorithm belongs to")
    generated_content: str = Field(description="The generated narrative content")
    structure: dict[str, Any] = Field(
        default_factory=dict,
        description="Structural elements of the generated content",
    )
    notes: list[str] = Field(
        default_factory=list,
        description="Notes about the generation process",
    )
    raw_output: str = Field(
        default="",
        description="Raw LLM output for debugging",
    )


class ValidationResult(BaseModel):
    """Result from validating content against an algorithm."""

    algorithm_name: str = Field(description="Name of the algorithm used for validation")
    study_id: str = Field(description="ID of the study this algorithm belongs to")
    is_valid: bool = Field(description="Whether the input satisfies the algorithm criteria")
    criteria_met: list[str] = Field(
        default_factory=list,
        description="Criteria from the algorithm that were satisfied",
    )
    criteria_failed: list[str] = Field(
        default_factory=list,
        description="Criteria from the algorithm that were not satisfied",
    )
    suggestions: list[str] = Field(
        default_factory=list,
        description="Suggestions for meeting failed criteria",
    )
    confidence: float = Field(
        default=0.0,
        description="Confidence score (0-1) in the validation result",
    )
    raw_output: str = Field(
        default="",
        description="Raw LLM output for debugging",
    )


@dataclass
class ExecutableAlgorithm:
    """An algorithm that can be executed using an LLM provider.

    Wraps the Algorithm model and provides methods for analysis,
    generation, and validation of narrative content.
    """

    algorithm: Algorithm
    study_id: str
    study_creator: str = ""
    study_work: str = ""

    @property
    def name(self) -> str:
        """Algorithm name."""
        return self.algorithm.name

    @property
    def purpose(self) -> str:
        """Algorithm purpose."""
        return self.algorithm.purpose

    @property
    def pseudocode(self) -> str:
        """Algorithm pseudocode."""
        return self.algorithm.pseudocode

    @property
    def inputs(self) -> list[str]:
        """Algorithm inputs."""
        return self.algorithm.inputs

    @property
    def outputs(self) -> list[str]:
        """Algorithm outputs."""
        return self.algorithm.outputs

    def _build_system_prompt(self, mode: ExecutionMode) -> str:
        """Build a system prompt for the algorithm execution."""
        return f"""You are a narratological analyst applying the "{self.name}" algorithm.

This algorithm comes from a study of {self.study_creator}'s work ({self.study_work}).

Algorithm Purpose:
{self.purpose}

Algorithm Logic (Pseudocode):
{self.pseudocode}

Expected Inputs: {', '.join(self.inputs) if self.inputs else 'narrative text'}
Expected Outputs: {', '.join(self.outputs) if self.outputs else 'analysis results'}

You are operating in {mode.value.upper()} mode."""

    def _build_analysis_prompt(self, text: str) -> str:
        """Build an analysis prompt."""
        return f"""Analyze the following narrative text using the "{self.name}" algorithm.

Apply the algorithm's logic to identify relevant narrative elements and assess how well the text embodies the principles outlined in the algorithm.

TEXT TO ANALYZE:
---
{text}
---

Provide your analysis as a JSON object with these fields:
- input_summary: Brief summary of what was analyzed
- findings: Array of key findings
- elements_identified: Object mapping algorithm outputs to identified elements
- recommendations: Array of suggestions for improvement
- score: Number from 0 to 1 indicating alignment with algorithm criteria"""

    def _build_generation_prompt(self, params: dict[str, Any]) -> str:
        """Build a generation prompt."""
        params_str = "\n".join(f"- {k}: {v}" for k, v in params.items())
        return f"""Generate narrative content using the "{self.name}" algorithm.

Follow the algorithm's logic to create narrative elements that embody its principles.

GENERATION PARAMETERS:
{params_str if params_str else "- No specific parameters provided"}

Generate content that satisfies the algorithm's requirements and produces meaningful output for each of its expected outputs.

Provide your response as a JSON object with these fields:
- generated_content: The generated narrative text
- structure: Object showing how the algorithm's structure was applied
- notes: Array of notes about the generation choices made"""

    def _build_validation_prompt(self, text: str) -> str:
        """Build a validation prompt."""
        return f"""Validate whether the following narrative text satisfies the criteria of the "{self.name}" algorithm.

Check each aspect of the algorithm's logic and determine whether the text meets the requirements.

TEXT TO VALIDATE:
---
{text}
---

Provide your validation as a JSON object with these fields:
- is_valid: Boolean indicating overall validity
- criteria_met: Array of algorithm criteria that were satisfied
- criteria_failed: Array of algorithm criteria that were not satisfied
- suggestions: Array of suggestions for meeting failed criteria
- confidence: Number from 0 to 1 indicating confidence in this assessment"""

    def analyze(self, text: str, llm: LLMProvider) -> AnalysisResult:
        """Analyze narrative text using this algorithm.

        Args:
            text: The narrative text to analyze.
            llm: The LLM provider to use for analysis.

        Returns:
            AnalysisResult with findings and recommendations.
        """
        system = self._build_system_prompt(ExecutionMode.ANALYZE)
        prompt = self._build_analysis_prompt(text)

        result = llm.complete_structured(
            prompt,
            AnalysisResult,
            system=system,
        )

        # Ensure algorithm metadata is set
        result.algorithm_name = self.name
        result.study_id = self.study_id

        return result

    def generate(self, params: dict[str, Any], llm: LLMProvider) -> GenerationResult:
        """Generate narrative content using this algorithm.

        Args:
            params: Parameters to guide generation (mapped to algorithm inputs).
            llm: The LLM provider to use for generation.

        Returns:
            GenerationResult with generated content.
        """
        system = self._build_system_prompt(ExecutionMode.GENERATE)
        prompt = self._build_generation_prompt(params)

        result = llm.complete_structured(
            prompt,
            GenerationResult,
            system=system,
        )

        # Ensure algorithm metadata is set
        result.algorithm_name = self.name
        result.study_id = self.study_id

        return result

    def validate(self, text: str, llm: LLMProvider) -> ValidationResult:
        """Validate narrative text against this algorithm's criteria.

        Args:
            text: The narrative text to validate.
            llm: The LLM provider to use for validation.

        Returns:
            ValidationResult indicating whether criteria are met.
        """
        system = self._build_system_prompt(ExecutionMode.VALIDATE)
        prompt = self._build_validation_prompt(text)

        result = llm.complete_structured(
            prompt,
            ValidationResult,
            system=system,
        )

        # Ensure algorithm metadata is set
        result.algorithm_name = self.name
        result.study_id = self.study_id

        return result

    def __str__(self) -> str:
        """String representation."""
        return f"ExecutableAlgorithm({self.study_id}.{self.name})"

    def __repr__(self) -> str:
        """Detailed representation."""
        return (
            f"ExecutableAlgorithm("
            f"name={self.name!r}, "
            f"study_id={self.study_id!r}, "
            f"inputs={self.inputs}, "
            f"outputs={self.outputs})"
        )
