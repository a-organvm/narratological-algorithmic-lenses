"""Data models for narratological analysis.

Includes models for:
- Study data (axioms, algorithms, diagnostic questions)
- Script/narrative analysis (scenes, characters, beats)
- Report generation (coverage, beat map, structural, character atlas, diagnostic)
- Analyst system (roles, observations, multi-role synthesis)
"""

from narratological.models.analysis import (
    Act,
    ArcClassification,
    Beat,
    BeatFunction,
    Character,
    ConnectorType,
    Scene,
    Script,
    ThematicElement,
)
from narratological.models.analyst import (
    ActivationLayer,
    AnalystContext,
    AnalystObservation,
    AnalystRole,
    MultiRoleAnalysis,
    RoleAnalysisResult,
    SynthesisConfig,
)
from narratological.models.report import (
    ActAnalysis,
    BeatMapEntry,
    BeatMapReport,
    CharacterAtlasEntry,
    CharacterAtlasReport,
    CharacterRelationship,
    CoverageReport,
    DiagnosticIssue,
    DiagnosticReport,
    DiagnosticSeverity,
    RecommendationType,
    StructuralReport,
)
from narratological.models.study import (
    Algorithm,
    Axiom,
    Category,
    Compendium,
    DiagnosticQuestion,
    HierarchyLevel,
    QuickReference,
    SequencePair,
    StructuralHierarchy,
    Study,
    TheoreticalCorrespondences,
)

__all__ = [
    # Study models
    "Study",
    "Axiom",
    "Algorithm",
    "DiagnosticQuestion",
    "HierarchyLevel",
    "StructuralHierarchy",
    "TheoreticalCorrespondences",
    "QuickReference",
    "Category",
    "Compendium",
    "SequencePair",
    # Analysis models
    "Script",
    "Scene",
    "Beat",
    "Character",
    "Act",
    "ThematicElement",
    "BeatFunction",
    "ArcClassification",
    "ConnectorType",
    # Report models
    "CoverageReport",
    "RecommendationType",
    "BeatMapReport",
    "BeatMapEntry",
    "StructuralReport",
    "ActAnalysis",
    "CharacterAtlasReport",
    "CharacterAtlasEntry",
    "CharacterRelationship",
    "DiagnosticReport",
    "DiagnosticIssue",
    "DiagnosticSeverity",
    # Analyst models
    "AnalystRole",
    "AnalystObservation",
    "RoleAnalysisResult",
    "ActivationLayer",
    "SynthesisConfig",
    "MultiRoleAnalysis",
    "AnalystContext",
]
