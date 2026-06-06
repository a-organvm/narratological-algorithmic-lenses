"""Base analyst class and context for the 8-role system.

Provides the foundation for role-specific analysts that apply
narratological frameworks to script analysis.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from pydantic import BaseModel, Field

from narratological.models.analyst import (
    ROLE_STUDY_MAPPING,
    AnalystContext,
    AnalystObservation,
    AnalystRole,
    RoleAnalysisResult,
)

if TYPE_CHECKING:
    from narratological.llm.providers import LLMProvider


class LLMAnalysisResponse(BaseModel):
    """LLM response model for role analysis."""

    summary: str
    observations: list[dict] = Field(default_factory=list)
    key_findings: list[str] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)
    score: float | None = None


class BaseAnalyst(ABC):
    """Abstract base class for analyst roles.

    Each analyst role implements its specific analytical perspective,
    drawing on relevant narratological frameworks.
    """

    role: AnalystRole
    description: str = ""

    def __init__(self, provider: LLMProvider | None = None):
        """Initialize the analyst.

        Args:
            provider: LLM provider for AI-assisted analysis.
        """
        self.provider = provider

    @property
    def primary_studies(self) -> list[str]:
        """Get the primary studies for this role."""
        return ROLE_STUDY_MAPPING.get(self.role, [])

    def analyze(self, context: AnalystContext) -> RoleAnalysisResult:
        """Perform analysis from this role's perspective.

        Args:
            context: The analysis context with script data.

        Returns:
            RoleAnalysisResult with observations and recommendations.
        """
        if self.provider is None:
            return self._analyze_algorithmic(context)
        return self._analyze_with_llm(context)

    def _analyze_with_llm(self, context: AnalystContext) -> RoleAnalysisResult:
        """Perform analysis using LLM."""
        if self.provider is None:
            raise ValueError("LLM provider required for LLM analysis")

        system_prompt = self._build_system_prompt()
        analysis_prompt = self._build_analysis_prompt(context)

        try:
            response = self.provider.complete_structured(
                analysis_prompt,
                LLMAnalysisResponse,
                system=system_prompt,
            )
            return self._convert_response(response)
        except Exception as e:
            # Return error result
            return RoleAnalysisResult(
                role=self.role,
                summary=f"Analysis failed: {e}",
                observations=[],
                key_findings=[],
                recommendations=[],
                frameworks_applied=self.primary_studies,
            )

    def _analyze_algorithmic(self, context: AnalystContext) -> RoleAnalysisResult:
        """Perform basic analysis without LLM.

        Override in subclasses to provide algorithmic analysis.
        """
        return RoleAnalysisResult(
            role=self.role,
            summary=f"Algorithmic analysis not implemented for {self.role.value}",
            observations=[],
            key_findings=[],
            recommendations=["Use LLM provider for full analysis"],
            frameworks_applied=self.primary_studies,
        )

    def _convert_response(self, response: LLMAnalysisResponse) -> RoleAnalysisResult:
        """Convert LLM response to RoleAnalysisResult."""
        observations = []
        for obs_dict in response.observations:
            observations.append(
                AnalystObservation(
                    role=self.role,
                    category=obs_dict.get("category", "general"),
                    observation=obs_dict.get("observation", ""),
                    location=obs_dict.get("location"),
                    confidence=obs_dict.get("confidence", 0.8),
                    evidence=obs_dict.get("evidence", []),
                    framework_source=obs_dict.get("framework_source"),
                )
            )

        return RoleAnalysisResult(
            role=self.role,
            summary=response.summary,
            observations=observations,
            key_findings=response.key_findings,
            recommendations=response.recommendations,
            score=response.score,
            frameworks_applied=self.primary_studies,
        )

    @abstractmethod
    def _build_system_prompt(self) -> str:
        """Build the system prompt for this role."""
        ...

    @abstractmethod
    def _build_analysis_prompt(self, context: AnalystContext) -> str:
        """Build the analysis prompt for this role."""
        ...

    def __repr__(self) -> str:
        """String representation."""
        return f"{self.__class__.__name__}(role={self.role.value})"
