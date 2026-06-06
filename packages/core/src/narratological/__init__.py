"""Narratological Algorithmic Lenses - Core Library.

A comprehensive library for narrative analysis using formalized algorithms
extracted from master storytellers.
"""

from narratological.loader import load_compendium, load_study
from narratological.models.study import (
    Algorithm,
    Axiom,
    DiagnosticQuestion,
    HierarchyLevel,
    QuickReference,
    StructuralHierarchy,
    Study,
    TheoreticalCorrespondences,
)

__version__ = "0.1.0"

__all__ = [
    # Models
    "Study",
    "Axiom",
    "Algorithm",
    "DiagnosticQuestion",
    "HierarchyLevel",
    "StructuralHierarchy",
    "TheoreticalCorrespondences",
    "QuickReference",
    # Loader
    "load_compendium",
    "load_study",
]
