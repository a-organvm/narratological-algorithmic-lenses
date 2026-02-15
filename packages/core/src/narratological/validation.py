"""Validation logic for narratological studies.

Ensures that structured JSON data is synchronized with its Markdown source.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from narratological.models.study import Study


@dataclass
class ValidationIssue:
    """A single validation discrepancy."""

    field: str
    message: str
    severity: str = "error"  # "error" or "warning"
    item_id: str | None = None


@dataclass
class ValidationReport:
    """Results of a study validation."""

    study_id: str
    markdown_path: Path
    issues: list[ValidationIssue] = field(default_factory=list)

    @property
    def is_valid(self) -> bool:
        """True if no errors were found."""
        return not any(i.severity == "error" for i in self.issues)

    @property
    def errors(self) -> list[ValidationIssue]:
        """List of validation errors."""
        return [i for i in self.issues if i.severity == "error"]

    @property
    def warnings(self) -> list[ValidationIssue]:
        """List of validation warnings."""
        return [i for i in self.issues if i.severity == "warning"]


class StudyValidator:
    """Validator for comparing a Study model against its Markdown source."""

    def __init__(self, study: Study, markdown_path: Path):
        self.study = study
        self.markdown_path = markdown_path
        self._content = ""
        self._report = ValidationReport(study_id=study.id, markdown_path=markdown_path)

    def _load_markdown(self) -> bool:
        """Load markdown content if the file exists."""
        if not self.markdown_path.exists():
            self._report.issues.append(
                ValidationIssue(
                    field="markdown_file",
                    message=f"Markdown file not found: {self.markdown_path}",
                    severity="error",
                )
            )
            return False

        try:
            self._content = self.markdown_path.read_text(encoding="utf-8")
            return True
        except Exception as e:
            self._report.issues.append(
                ValidationIssue(
                    field="markdown_file",
                    message=f"Error reading markdown: {e}",
                    severity="error",
                )
            )
            return False

    def validate_metadata(self) -> None:
        """Ensure creator and work match."""
        # Simple check for existence in title or intro
        if self.study.creator.lower() not in self._content.lower():
            self._report.issues.append(
                ValidationIssue(
                    field="creator",
                    message=f"Creator '{self.study.creator}' not found in markdown text.",
                    severity="warning",
                )
            )

    def validate_axioms(self) -> None:
        """Ensure every axiom ID exists in the markdown."""
        for axiom in self.study.axioms:
            # Look for axiom ID in a table row, header, or list
            # We look for the ID (e.g. AT-A0) anchored by non-word chars
            pattern = rf"\b{re.escape(axiom.id)}\b"
            if not re.search(pattern, self._content):
                self._report.issues.append(
                    ValidationIssue(
                        field="axioms",
                        message=f"Axiom ID '{axiom.id}' not found in markdown.",
                        severity="error",
                        item_id=axiom.id,
                    )
                )

    def validate_algorithms(self) -> None:
        """Ensure every algorithm name appears in headers or emphasized text."""
        for algo in self.study.core_algorithms:
            # Look for algorithm name in headers or emphasized text
            # We try:
            # 1. Exact header/bold/marker match
            # 2. Part of a header
            # 3. Normalized match (ignoring 'Algorithm' or 'Protocol' suffixes)
            
            escaped_name = re.escape(algo.name)
            
            # Pattern 1: Formal markers
            p1 = rf"(#+\s+.*{escaped_name})|(\*\*{escaped_name}\*\*)|(Algorithm:\s*{escaped_name})"
            
            # Pattern 2: Suffix-stripped match
            stripped_name = re.sub(r"\s+(Algorithm|Protocol|System|Methodology)$", "", algo.name, flags=re.I)
            escaped_stripped = re.escape(stripped_name)
            p2 = rf"#+\s+.*{escaped_stripped}"
            
            if not (re.search(p1, self._content, re.IGNORECASE) or re.search(p2, self._content, re.IGNORECASE)):
                self._report.issues.append(
                    ValidationIssue(
                        field="core_algorithms",
                        message=f"Algorithm '{algo.name}' not found in markdown structure.",
                        severity="error",
                        item_id=algo.name,
                    )
                )

    def validate_diagnostics(self) -> None:
        """Ensure diagnostic questions are present."""
        # Normalize quotes for comparison
        content_norm = self._content.replace('"', "'").replace("“", "'").replace("”", "'")
        
        for q in self.study.diagnostic_questions:
            # Try to find the question text (normalized)
            q_norm = q.question.replace('"', "'")
            snippet = q_norm[:50]
            if snippet not in content_norm:
                self._report.issues.append(
                    ValidationIssue(
                        field="diagnostic_questions",
                        message=f"Diagnostic question '{q.id}' text mismatch or missing.",
                        severity="warning",
                        item_id=q.id,
                    )
                )

    def validate_hierarchy(self) -> None:
        """Ensure structural hierarchy levels exist."""
        for level in self.study.structural_hierarchy.levels:
            if level.name not in self._content:
                self._report.issues.append(
                    ValidationIssue(
                        field="structural_hierarchy",
                        message=f"Hierarchy level '{level.name}' not found in markdown.",
                        severity="warning",
                        item_id=level.name,
                    )
                )

    def run_all(self) -> ValidationReport:
        """Run all validation checks."""
        if not self._load_markdown():
            return self._report

        self.validate_metadata()
        self.validate_axioms()
        self.validate_algorithms()
        self.validate_hierarchy()
        self.validate_diagnostics()

        return self._report


def validate_study(study: Study, markdown_path: Path) -> ValidationReport:
    """Helper function to validate a study."""
    validator = StudyValidator(study, markdown_path)
    return validator.run_all()
