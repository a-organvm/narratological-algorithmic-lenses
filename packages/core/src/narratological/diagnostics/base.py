"""Base classes for diagnostic runners.

Provides the foundation for structural diagnostic tests.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from narratological.diagnostics.models import (
    DiagnosticContext,
    DiagnosticThresholds,
    DiagnosticType,
)
from narratological.models.report import DiagnosticIssue, DiagnosticSeverity

if TYPE_CHECKING:
    from narratological.llm.providers import LLMProvider


class BaseDiagnostic(ABC):
    """Abstract base class for diagnostic runners.

    Each diagnostic implements a specific structural test
    (causal binding, reorderability, necessity, etc.).
    """

    diagnostic_type: DiagnosticType
    description: str = ""

    def __init__(
        self,
        provider: LLMProvider | None = None,
        thresholds: DiagnosticThresholds | None = None,
    ):
        """Initialize the diagnostic runner.

        Args:
            provider: LLM provider for AI-assisted diagnostics.
            thresholds: Severity thresholds for this diagnostic.
        """
        self.provider = provider
        self.thresholds = thresholds or DiagnosticThresholds()

    @abstractmethod
    def run(self, context: DiagnosticContext) -> list[DiagnosticIssue]:
        """Run the diagnostic test.

        Args:
            context: The diagnostic context with script data.

        Returns:
            List of DiagnosticIssue objects found.
        """
        ...

    @abstractmethod
    def calculate_score(self, context: DiagnosticContext) -> float:
        """Calculate the diagnostic score.

        Args:
            context: The diagnostic context with script data.

        Returns:
            Score from 0.0 to 1.0 representing the metric.
        """
        ...

    def get_severity(self, score: float) -> DiagnosticSeverity:
        """Get severity level based on score and thresholds.

        Default implementation for "higher is better" metrics.
        Override in subclasses for different semantics.

        Args:
            score: The diagnostic score (0.0-1.0).

        Returns:
            Appropriate severity level.
        """
        # Default: higher score is better
        if score >= 0.90:
            return DiagnosticSeverity.INFO
        elif score >= 0.75:
            return DiagnosticSeverity.SUGGESTION
        elif score >= 0.60:
            return DiagnosticSeverity.WARNING
        else:
            return DiagnosticSeverity.CRITICAL

    def _requires_llm(self) -> bool:
        """Check if this diagnostic requires an LLM provider.

        Override in subclasses that can work algorithmically.

        Returns:
            True if LLM is required, False otherwise.
        """
        return True

    def can_run(self, context: DiagnosticContext) -> tuple[bool, str | None]:
        """Check if the diagnostic can run with the given context.

        Args:
            context: The diagnostic context.

        Returns:
            Tuple of (can_run, error_message).
        """
        if self._requires_llm() and self.provider is None:
            return False, f"{self.diagnostic_type.value} requires LLM provider"

        if not context.scenes:
            return False, "No scene data available"

        return True, None

    def create_issue(
        self,
        description: str,
        severity: DiagnosticSeverity,
        location: str | None = None,
        recommendation: str = "",
        category: str = "structure",
    ) -> DiagnosticIssue:
        """Create a diagnostic issue with automatic ID generation.

        Args:
            description: Issue description.
            severity: Issue severity.
            location: Where in the script.
            recommendation: How to fix it.
            category: Issue category.

        Returns:
            DiagnosticIssue instance.
        """
        # Generate ID from diagnostic type
        prefix = {
            DiagnosticType.CAUSAL_BINDING: "CB",
            DiagnosticType.REORDERABILITY: "RO",
            DiagnosticType.NECESSITY: "NE",
            DiagnosticType.INFORMATION_ECONOMY: "IE",
            DiagnosticType.FRAMEWORK: "FW",
        }.get(self.diagnostic_type, "DG")

        # Simple incrementing ID (in real usage, would track count)
        issue_id = f"{prefix}-{hash(description) % 1000:03d}"

        return DiagnosticIssue(
            id=issue_id,
            severity=severity,
            category=category,
            description=description,
            location=location,
            recommendation=recommendation,
            framework_source=self.diagnostic_type.value,
        )

    def _get_chunks(self, scenes: list[dict], chunk_size: int = 20, overlap: int = 2) -> list[list[dict]]:
        """Split scenes into overlapping chunks for exhaustive analysis.
        
        Args:
            scenes: The full list of scene dictionaries.
            chunk_size: Number of scenes per chunk.
            overlap: Number of scenes to overlap between chunks (to maintain transition context).
            
        Returns:
            List of scene lists (chunks).
        """
        if not scenes:
            return []
            
        if len(scenes) <= chunk_size:
            return [scenes]
            
        chunks = []
        start = 0
        while start < len(scenes):
            end = min(start + chunk_size, len(scenes))
            chunks.append(scenes[start:end])
            
            # If we've reached the end, stop
            if end == len(scenes):
                break
                
            # Move start forward by chunk_size - overlap
            start += (chunk_size - overlap)
            
        return chunks

    def __repr__(self) -> str:
        """String representation."""
        return f"{self.__class__.__name__}(type={self.diagnostic_type.value})"
