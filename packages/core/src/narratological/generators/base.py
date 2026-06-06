"""Base classes for report generators.

Provides the foundational ABC and configuration for all report generators,
enabling consistent interfaces across Coverage, Beat Map, Structural,
Character Atlas, and Diagnostic report types.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import StrEnum
from typing import TYPE_CHECKING, Generic, TypeVar

if TYPE_CHECKING:
    from narratological.llm.providers import LLMProvider
    from narratological.models.analysis import Script


class ReportType(StrEnum):
    """Types of reports that can be generated."""

    COVERAGE = "coverage"
    BEAT_MAP = "beat_map"
    STRUCTURAL = "structural"
    CHARACTER_ATLAS = "character_atlas"
    DIAGNOSTIC = "diagnostic"


@dataclass
class GeneratorConfig:
    """Configuration for report generators.

    Controls LLM behavior, output formatting, and analysis parameters.
    """

    # LLM settings
    temperature: float = 0.7
    max_retries: int = 3

    # Analysis settings
    include_role_notes: bool = True
    active_studies: list[str] = field(default_factory=list)
    primary_framework: str | None = None

    # Output settings
    verbose: bool = False
    include_raw_output: bool = False

    # Thresholds
    causal_binding_target: float = 0.80
    minimum_tension_variance: float = 2.0

    # Coverage-specific
    include_comparables: bool = True
    max_comparables: int = 5

    # Character atlas-specific
    include_minor_characters: bool = False
    screen_time_threshold: float = 0.05  # 5% minimum screen time for inclusion

    # Structural-specific
    structure_type: str = "Three-Act"  # Three-Act, Five-Act, Hero's Journey


# Type variable for report output types
T = TypeVar("T")


class BaseReportGenerator(ABC, Generic[T]):
    """Abstract base class for all report generators.

    Provides common functionality for generating narrative analysis reports
    using LLM providers and the narratological framework.

    Type parameter T represents the specific report model being generated
    (CoverageReport, BeatMapReport, etc.).
    """

    report_type: ReportType

    def __init__(
        self,
        provider: LLMProvider | None = None,
        config: GeneratorConfig | None = None,
    ):
        """Initialize the report generator.

        Args:
            provider: LLM provider for AI-assisted analysis. If None,
                     only algorithmic analysis will be performed.
            config: Generator configuration. Uses defaults if not provided.
        """
        self.provider = provider
        self.config = config or GeneratorConfig()

    @abstractmethod
    def generate(self, script: Script, **kwargs) -> T:
        """Generate a report for the given script.

        Args:
            script: The script/narrative to analyze.
            **kwargs: Additional report-specific parameters.

        Returns:
            A report instance of type T.
        """
        ...

    @abstractmethod
    def _build_system_prompt(self) -> str:
        """Build the system prompt for LLM analysis.

        Returns:
            System prompt string describing the analyst role and task.
        """
        ...

    @abstractmethod
    def _build_analysis_prompt(self, script: Script) -> str:
        """Build the analysis prompt for the specific report type.

        Args:
            script: The script being analyzed.

        Returns:
            User prompt string with script data and instructions.
        """
        ...

    def _requires_llm(self) -> bool:
        """Check if this generator requires an LLM provider.

        Some reports can be generated algorithmically without LLM assistance.
        Override in subclasses to indicate LLM requirement.

        Returns:
            True if LLM is required, False otherwise.
        """
        return True

    def _validate_prerequisites(self, script: Script) -> list[str]:
        """Validate that the script has required data for report generation.

        Args:
            script: The script to validate.

        Returns:
            List of validation error messages (empty if valid).
        """
        errors = []

        if not script.title:
            errors.append("Script must have a title")

        if self._requires_llm() and self.provider is None:
            errors.append(f"{self.report_type.value} report requires an LLM provider")

        return errors

    def can_generate(self, script: Script) -> tuple[bool, list[str]]:
        """Check if the generator can produce a report for this script.

        Args:
            script: The script to check.

        Returns:
            Tuple of (can_generate, error_messages).
        """
        errors = self._validate_prerequisites(script)
        return len(errors) == 0, errors

    def __repr__(self) -> str:
        """Detailed representation."""
        return (
            f"{self.__class__.__name__}("
            f"report_type={self.report_type.value!r}, "
            f"has_provider={self.provider is not None})"
        )


class GeneratorError(Exception):
    """Exception raised when report generation fails."""

    def __init__(
        self,
        message: str,
        report_type: ReportType | None = None,
        cause: Exception | None = None,
    ):
        """Initialize the error.

        Args:
            message: Error description.
            report_type: The type of report that failed.
            cause: The underlying exception, if any.
        """
        super().__init__(message)
        self.report_type = report_type
        self.cause = cause
