"""LLM prompts for protocol-specific document generation.

Provides prompts that instruct the LLM to generate markdown documents
following the template specifications in specs/08-protocol-framework/.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from narratological.models.analysis import Script


def _format_scenes(script: Script) -> str:
    if not script.scenes:
        return "No scenes available."
    lines = []
    for s in script.scenes[:50]:
        chars = ", ".join(s.characters_present[:4]) if s.characters_present else "None"
        lines.append(f"- Scene {s.number}: {s.slug} (Tension: {s.tension_level or 'N/A'}) - {s.summary[:100]}... [Characters: {chars}]")
    if len(script.scenes) > 50:
        lines.append(f"... and {len(script.scenes) - 50} more scenes")
    return "\n".join(lines)


def _format_characters(script: Script) -> str:
    if not script.characters:
        return "No characters available."
    lines = []
    for c in script.characters[:25]:
        want = f" | Want: {c.want}" if c.want else ""
        need = f" | Need: {c.need}" if c.need else ""
        lines.append(f"- {c.name} ({c.role}): {c.description[:100]}...{want}{need}")
    if len(script.characters) > 25:
        lines.append(f"... and {len(script.characters) - 25} more characters")
    return "\n".join(lines)


def build_triage_prompt(script: Script) -> str:
    """Build prompt for generating a P1 Triage Report."""
    return f"""You are performing a P1-TRIAGE analysis on the script "{script.title}".
Your target is to assess viability and make a clear decision on whether to RECOMMEND, CONSIDER, or PASS.

SCRIPT DATA:
Title: {script.title}
Format: {script.format}
Total Scenes: {len(script.scenes)}
Total Characters: {len(script.characters)}

SCENE SUMMARY:
{_format_scenes(script)}

CHARACTER SUMMARY:
{_format_characters(script)}

Please generate a P1 Triage Report using the following Markdown structure exactly:

# {script.title} — Triage Report

**Date:** [Use current date]
**Analyst:** Claude (P1-TRIAGE)
**Time Spent:** 45 minutes

---

## Recommendation

[ ] **RECOMMEND** — Proceed to deeper analysis or development
[ ] **CONSIDER** — Notable elements warrant second look
[ ] **PASS** — Fundamental issues; not worth further investment
(Mark exactly one with [X])

---

## First-Reader Response

### Engagement Summary
[2-3 paragraphs capturing honest emotional journey, highs and lows, and final impression]

### Involuntary Response Check
[Table of Laughter, Fear/tension, Tears/emotion, Surprise with Yes/No and page/scene location]

---

## Structural Assessment

### Fundamental Architecture
[Table with Protagonist, Goal, Opposition, Causal progression, Satisfying resolution status and notes]

### Red Flags
[Checklist [X] or [ ] of Passive protagonist, Reorderable scenes, Missing inciting incident, Undramatized climax, Deus ex machina, etc.]

---

## Decision Rationale
[2-3 paragraphs explaining the decision recommendation]

---

## Escalation Notes
**Deeper analysis recommended?** Yes / No
**If yes, suggested protocol**: [ ] P2 Structural [ ] P3 Craft [ ] P5 Market [ ] P7 Full
**Key questions for deeper analysis**:
1. [Question 1]
2. [Question 2]
3. [Question 3]

---
*Triage Report | Protocol P1 v1.0*
"""


def build_market_positioning_prompt(script: Script) -> str:
    """Build prompt for generating a P5 Market Positioning Report."""
    return f"""You are performing a P5-MARKET analysis on the script "{script.title}".
Your focus is to assess commercial viability, comparables, target demographics, and platform fit.

SCRIPT DATA:
Title: {script.title}
Format: {script.format}
Total Scenes: {len(script.scenes)}
Total Characters: {len(script.characters)}

SCENE SUMMARY:
{_format_scenes(script)}

Please generate a Market Positioning Report using the following Markdown structure exactly:

# {script.title} — Market Positioning Report

**Date:** [Use current date]
**Analyst:** Claude (P5-MARKET)

---

## Executive Summary
[Market viability assessment table with ratings and notes, and a One-Line Positioning statement]

---

## Comparable Titles Analysis
[Identify 3 direct comparables with Year, Budget, US Gross, Platform, and Relevance. Summarize patterns and differentiation.]

---

## Target Audience Profile
[Primary and secondary demographics, Viewing behavior, size estimate, and Audience Risks]

---

## Production Considerations
[Budget Tier assessment, Location/VFX/Cast requirements, and feasibility flags]

---

## Platform Fit Analysis
[Platform fit rating table for theatrical, streaming, cable, etc. and recommended platform strategy]

---

## Commercial Strengths
[List 3 key strengths with market appeal]

---

## Commercial Risks
[List 3 key risks and mitigation strategies]

---

## Market Recommendation
[ACQUIRE/GREENLIGHT, DEVELOP, or PASS with rationale and key changes needed]

---
*Market Positioning Report | Protocol P5 v1.0*
"""


def build_mechanism_extraction_prompt(script: Script) -> str:
    """Build prompt for generating a P6 Mechanism Extraction Report."""
    return f"""You are performing a P6-EXTRACTION analysis on the script "{script.title}".
Your goal is to identify unique narrative techniques, formalize them as structural algorithms, and suggest candidate axioms.

SCRIPT DATA:
Title: {script.title}
Format: {script.format}
Total Scenes: {len(script.scenes)}

SCENE SUMMARY:
{_format_scenes(script)}

Please generate a Mechanism Extraction Report using the following Markdown structure exactly:

# {script.title} — Mechanism Extraction Report

**Date:** [Use current date]
**Analyst:** Claude (P6-EXTRACT)

---

## Extraction Overview
**Purpose**: Identify implementable narrative mechanisms for potential algorithm formalization.
**Extraction Focus**: [Describe the key focus, e.g., pacing, subtext, comedic geometry, etc.]
**Theoretical Frame**: [Which existing frameworks inform this analysis]

---

## Identified Mechanisms
### M1: [Mechanism Name]
**Location in Source**: [specific scene/page numbers]
**Operational Description**: [how it works]
**Source Evidence**: [direct description or quotes]
**Formalization Attempt**:
```
MECHANISM: [name]
PRECONDITION: [what must be true]
OPERATION: IF [condition] THEN [action] BECAUSE [principle]
EFFECT: [what it produces]
VALIDATION_TEST: [how to verify]
```
**Theoretical Correspondence**: [McKee/Aristotle concepts]
**Scope Assessment**: [Universality, Medium dependency, Formalizability, Evidence strength]

### M2: [Mechanism Name]
[Repeat for second mechanism]

---

## Candidate Axioms
[Table of candidate axioms, evidence, and confidence]

---

## Cross-Reference Analysis
[Relationship to existing algorithms and novel contributions]

---

## Algorithm Development Recommendation
[List mechanisms ready for full extraction, needing study, or not formalizable]

---
*Mechanism Extraction Report | Protocol P6 v1.0*
"""


def build_thematic_architecture_prompt(script: Script) -> str:
    """Build prompt for analyzing thematic architecture (P4, P7)."""
    return f"""Analyze the thematic architecture of "{script.title}".

SCRIPT DATA:
Title: {script.title}
Format: {script.format}
Total Scenes: {len(script.scenes)}

SCENE SUMMARY:
{_format_scenes(script)}

Please generate a Thematic Architecture Report in Markdown containing:
1. **Controlling Idea**: The central premise or primary philosophical argument of the work.
2. **Thematic Layers**: Breakdown of primary, secondary, and tertiary themes.
3. **Symbols and Motifs**: Key physical objects, repeated lines, or imagery used as thematic shorthand, tracking where they occur and what they represent.
4. **Articulation Points**: Specific scenes or exchanges where the themes are explicitly discussed or resolved.
5. **Philosophical Conflict**: The opposing values clashed in the story (e.g., Idealism vs Pragmatism) and how the climax resolves this clash.
"""


def build_theoretical_correspondence_prompt(script: Script) -> str:
    """Build prompt for theoretical correspondence analysis (P4, P6, P7)."""
    return f"""Perform a Theoretical Correspondence Analysis of "{script.title}".
Map the narrative structure and choices in this script to classical and modern story theories.

SCRIPT DATA:
Title: {script.title}
Format: {script.format}
Total Scenes: {len(script.scenes)}

SCENE SUMMARY:
{_format_scenes(script)}

Please generate a Theoretical Correspondence Report in Markdown containing:
1. **Aristotelian Poetics Map**: Evaluate against Aristotle's concepts: Mimesis (imitation), Hamartia (tragic flaw), Anagnorisis (recognition), Peripeteia (reversal), and Catharsis.
2. **McKee Story Structure Fit**: Assess value charge transitions, gap analysis (expectation vs reality), and progressive complications.
3. **Attention Mechanics Alignment**: Map how the script manages audience attention (curiosity, suspense, dramatic irony, shock).
4. **Alternative Frameworks**: Evaluate against alternative cultural or creator lenses if applicable (e.g., Kishotenketsu, Heroine's Journey, or specific auteur styles like Tarkovsky/Lynch).
5. **Framework Subversion**: Note where the script resists or subverts standard theoretical models.
"""


def build_revision_roadmap_prompt(script: Script) -> str:
    """Build prompt for generating a P3/P7 Revision Roadmap."""
    return f"""Develop a comprehensive Revision Roadmap for "{script.title}" based on the script's content.

SCRIPT DATA:
Title: {script.title}
Format: {script.format}
Total Scenes: {len(script.scenes)}

SCENE SUMMARY:
{_format_scenes(script)}

Please generate a Revision Roadmap in Markdown containing:
1. **Prioritized Issue List**: Critical (must fix), Warning (should fix), and Suggestion (nice-to-have) issues identified in structure, character, dialogue, or theme.
2. **Sequential Revision Passes**: Detail a structured plan for the writer (e.g., Pass 1: Structural Causal Binding, Pass 2: Protagonist Motivation & Active Arcs, Pass 3: Dialogue Polish).
3. **Effort and Impact Estimates**: Estimate the effort (High/Medium/Low) and anticipated impact of each major revision item.
4. **Creator Reflection Questions**: 3-5 high-impact questions to ask the writer to help clarify their creative intentions.
"""
