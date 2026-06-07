"""Registry of analysis protocols.

Defines the parameters, roles, and outputs for all seven protocol levels (P1-P7).
"""

from __future__ import annotations

from narratological.models.analyst import AnalystRole
from narratological.models.protocol import ProtocolLevel, ProtocolSpec

PROTOCOLS: dict[ProtocolLevel, ProtocolSpec] = {
    ProtocolLevel.P1: ProtocolSpec(
        level=ProtocolLevel.P1,
        name="Triage",
        purpose="Quick read to determine viability and whether to proceed",
        roles=[
            AnalystRole.FIRST_READER,
            AnalystRole.DRAMATURGIST,
        ],
        documents=[
            "Coverage Report (Abbreviated)",
            "Triage Decision",
        ],
        time_estimate="30-60 min",
    ),
    ProtocolLevel.P2: ProtocolSpec(
        level=ProtocolLevel.P2,
        name="Structural",
        purpose="Deep structural diagnosis and act architecture assessment",
        roles=[
            AnalystRole.FIRST_READER,
            AnalystRole.DRAMATURGIST,
            AnalystRole.NARRATOLOGIST,
            AnalystRole.CINEPHILE,
        ],
        documents=[
            "Coverage Report",
            "Structural Analysis",
            "Diagnostic Report",
        ],
        time_estimate="2-3 hours",
    ),
    ProtocolLevel.P3: ProtocolSpec(
        level=ProtocolLevel.P3,
        name="Craft",
        purpose="Actionable revision notes for a working draft",
        roles=[
            AnalystRole.FIRST_READER,
            AnalystRole.DRAMATURGIST,
            AnalystRole.NARRATOLOGIST,
            AnalystRole.CINEPHILE,
            AnalystRole.RHETORICIAN,
        ],
        documents=[
            "Coverage Report",
            "Structural Analysis",
            "Character Atlas",
            "Diagnostic Report",
            "Revision Roadmap",
        ],
        time_estimate="4-5 hours",
    ),
    ProtocolLevel.P4: ProtocolSpec(
        level=ProtocolLevel.P4,
        name="Scholarly",
        purpose="Theoretical analysis and thematic mapping for scholarly output",
        roles=[
            AnalystRole.NARRATOLOGIST,
            AnalystRole.ART_HISTORIAN,
            AnalystRole.CINEPHILE,
            AnalystRole.RHETORICIAN,
            AnalystRole.ACADEMIC,
        ],
        documents=[
            "Structural Analysis",
            "Thematic Architecture",
            "Diagnostic Report",
            "Theoretical Correspondence",
        ],
        time_estimate="6-8 hours",
    ),
    ProtocolLevel.P5: ProtocolSpec(
        level=ProtocolLevel.P5,
        name="Market",
        purpose="Commercial potential, demographic fit, and target audience definition",
        roles=[
            AnalystRole.FIRST_READER,
            AnalystRole.DRAMATURGIST,
            AnalystRole.CINEPHILE,
            AnalystRole.PRODUCER,
        ],
        documents=[
            "Coverage Report (Abbreviated)",
            "Market Positioning",
        ],
        time_estimate="3-4 hours",
    ),
    ProtocolLevel.P6: ProtocolSpec(
        level=ProtocolLevel.P6,
        name="Extraction",
        purpose="Extract narrative mechanisms to document or formalize as algorithms",
        roles=[
            AnalystRole.DRAMATURGIST,
            AnalystRole.NARRATOLOGIST,
            AnalystRole.ART_HISTORIAN,
            AnalystRole.CINEPHILE,
            AnalystRole.ACADEMIC,
        ],
        documents=[
            "Structural Analysis (Abbreviated)",
            "Theoretical Correspondence",
            "Mechanism Extraction",
        ],
        time_estimate="4-6 hours",
    ),
    ProtocolLevel.P7: ProtocolSpec(
        level=ProtocolLevel.P7,
        name="Comprehensive",
        purpose="Exhaustive multi-dimensional analysis generating full document suite",
        roles=[
            AnalystRole.AESTHETE,
            AnalystRole.DRAMATURGIST,
            AnalystRole.NARRATOLOGIST,
            AnalystRole.ART_HISTORIAN,
            AnalystRole.CINEPHILE,
            AnalystRole.RHETORICIAN,
            AnalystRole.PRODUCER,
            AnalystRole.ACADEMIC,
            AnalystRole.FIRST_READER,
        ],
        documents=[
            "Coverage Report",
            "Beat Map",
            "Structural Analysis",
            "Character Atlas",
            "Thematic Architecture",
            "Diagnostic Report",
            "Theoretical Correspondence",
            "Revision Roadmap",
            "Market Positioning",
        ],
        time_estimate="8-12 hours",
    ),
}


def get_protocol(level: str | ProtocolLevel) -> ProtocolSpec:
    """Retrieve protocol specification by level.

    Args:
        level: The protocol level (e.g., 'P3' or ProtocolLevel.P3).

    Returns:
        The ProtocolSpec configuration.

    Raises:
        KeyError: If the protocol level is invalid.
    """
    if isinstance(level, str):
        try:
            level = ProtocolLevel(level.upper())
        except ValueError as e:
            raise KeyError(f"Invalid protocol level: {level}") from e
    return PROTOCOLS[level]
