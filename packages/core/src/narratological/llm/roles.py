"""Implementation of the 9 analyst roles.

Each role provides a distinct analytical perspective on scripts,
drawing from specific narratological frameworks.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from narratological.llm.analyst import BaseAnalyst
from narratological.models.analyst import AnalystContext, AnalystRole

if TYPE_CHECKING:
    from narratological.llm.providers import LLMProvider


class AestheteAnalyst(BaseAnalyst):
    """Analyst focused on form, beauty, style, and sensory patterns.

    Primary frameworks: Tarkovsky (Sculpting in Time), Bergman (Chamber Drama),
    David Lynch (Dream Logic).
    """

    role = AnalystRole.AESTHETE
    description = "Analyzes form, beauty, style, and sensory patterns"

    def _build_system_prompt(self) -> str:
        return """You are the AESTHETE analyst, focused on form and beauty in storytelling.

Your analytical lens:
- Visual and sensory patterns in the narrative
- Tonal consistency and register
- Stylistic distinctiveness and elegance
- Formal innovation or classical beauty
- The relationship between form and content

You draw on the techniques of:
- Andrei Tarkovsky (temporal poetry, image as truth)
- Ingmar Bergman (chamber drama aesthetics)
- David Lynch (dream logic, mood as meaning)

Provide observations about aesthetic merit, stylistic choices, and formal qualities.
Be specific about what creates beauty or dissonance in the work."""

    def _build_analysis_prompt(self, context: AnalystContext) -> str:
        return f"""Analyze the aesthetic qualities of this script.

TITLE: {context.title}
GENRE: {context.genre or 'Not specified'}
TONE: {context.tone or 'Not specified'}
FORMAT: {context.format}

CONTENT/SUMMARY:
{context.text[:3000] if context.text else 'No content provided'}

SCENES:
{self._format_scenes(context.scene_summaries)}

Provide your analysis as JSON with:
- summary: Your aesthetic assessment (2-3 sentences)
- observations: Array of observations, each with:
  - category: "visual", "tonal", "stylistic", or "formal"
  - observation: What you noticed
  - location: Where in the script (optional)
  - confidence: 0.0-1.0
- key_findings: Array of most important aesthetic observations
- recommendations: Array of suggestions for aesthetic improvement
- score: Overall aesthetic score 0-10"""

    def _format_scenes(self, summaries: list[str]) -> str:
        if not summaries:
            return "No scene data available"
        return "\n".join(f"- Scene {i+1}: {s[:100]}" for i, s in enumerate(summaries[:10]))


class DramaturgistAnalyst(BaseAnalyst):
    """Analyst focused on structure, rhythm, and dramatic tension.

    Primary frameworks: Pixar (emotional engineering), Tarantino (non-linear).
    """

    role = AnalystRole.DRAMATURGIST
    description = "Analyzes structure, rhythm, and dramatic tension"

    def _build_system_prompt(self) -> str:
        return """You are the DRAMATURGIST analyst, focused on dramatic structure and rhythm.

Your analytical lens:
- Dramatic tension and release patterns
- Pacing and rhythmic structure
- Act architecture effectiveness
- Scene transitions and flow
- Stakes escalation and climax building

You draw on the techniques of:
- Pixar (emotional engineering, clear stakes)
- Quentin Tarantino (non-linear structure, tension building)

Identify what works structurally and what needs dramaturgical attention.
Be specific about pacing issues and structural opportunities."""

    def _build_analysis_prompt(self, context: AnalystContext) -> str:
        return f"""Analyze the dramaturgical qualities of this script.

TITLE: {context.title}
FORMAT: {context.format}
PAGE COUNT: {context.page_count or 'Unknown'}

CONTENT/SUMMARY:
{context.text[:3000] if context.text else 'No content provided'}

SCENE COUNT: {len(context.scene_summaries)}
SCENES:
{self._format_scenes(context.scene_summaries)}

Provide your analysis as JSON with:
- summary: Your dramaturgical assessment (2-3 sentences)
- observations: Array of observations, each with:
  - category: "structure", "pacing", "tension", or "rhythm"
  - observation: What you noticed
  - location: Where in the script (scene/act)
  - confidence: 0.0-1.0
- key_findings: Array of most important structural observations
- recommendations: Array of suggestions for structural improvement
- score: Overall structural score 0-10"""

    def _format_scenes(self, summaries: list[str]) -> str:
        if not summaries:
            return "No scene data available"
        return "\n".join(f"- Scene {i+1}: {s[:100]}" for i, s in enumerate(summaries[:15]))


class NarratologistAnalyst(BaseAnalyst):
    """Analyst focused on narrative mechanisms and causal binding.

    Primary frameworks: Pixar (emotional engineering), Ovid (metamorphosis logic).
    """

    role = AnalystRole.NARRATOLOGIST
    description = "Analyzes narrative mechanisms and causal binding"

    def _build_system_prompt(self) -> str:
        return """You are the NARRATOLOGIST analyst, focused on narrative mechanisms.

Your analytical lens:
- Causal chains and plot logic (BUT/THEREFORE vs AND THEN)
- Information management (setup/payoff)
- Point of view and narrative distance
- Temporal structure (flashbacks, parallel timelines)
- Story vs discourse separation
- Transformation logic and character change

You draw on the techniques of:
- Pixar (clear causal chains, emotional logic)
- Ovid (metamorphosis as narrative engine)

Identify the narrative engines driving the story and their effectiveness.
Focus on causality and whether scenes earn their consequences."""

    def _build_analysis_prompt(self, context: AnalystContext) -> str:
        return f"""Analyze the narrative mechanisms of this script.

TITLE: {context.title}
GENRE: {context.genre or 'Not specified'}

CONTENT/SUMMARY:
{context.text[:3000] if context.text else 'No content provided'}

SCENES:
{self._format_scenes(context.scene_summaries)}

CHARACTERS: {', '.join(context.character_list[:10]) if context.character_list else 'Unknown'}

Provide your analysis as JSON with:
- summary: Your narratological assessment (2-3 sentences)
- observations: Array of observations, each with:
  - category: "causality", "information", "perspective", or "temporal"
  - observation: What you noticed
  - location: Where in the script
  - confidence: 0.0-1.0
- key_findings: Array of most important narrative observations
- recommendations: Array of suggestions for narrative improvement
- score: Overall narrative score 0-10"""

    def _format_scenes(self, summaries: list[str]) -> str:
        if not summaries:
            return "No scene data available"
        return "\n".join(f"- Scene {i+1}: {s[:100]}" for i, s in enumerate(summaries[:15]))


class ArtHistorianAnalyst(BaseAnalyst):
    """Analyst focused on historical context, influences, and lineages.

    Primary frameworks: Kirby (cosmic mythopoeia), Tolkien (subcreation).
    """

    role = AnalystRole.ART_HISTORIAN
    description = "Analyzes historical context, influences, and lineages"

    def _build_system_prompt(self) -> str:
        return """You are the ART HISTORIAN analyst, focused on context and influences.

Your analytical lens:
- Genre traditions and conventions
- Historical and cultural context
- Artistic influences and lineages
- How the work relates to its moment
- Tradition vs innovation balance
- Mythological and archetypal patterns

You draw on the techniques of:
- Jack Kirby (cosmic mythopoeia, genre innovation)
- J.R.R. Tolkien (subcreation, depth through history)

Situate the work in its artistic context and identify its influences.
Note both what traditions it honors and where it innovates."""

    def _build_analysis_prompt(self, context: AnalystContext) -> str:
        return f"""Analyze the historical/contextual aspects of this script.

TITLE: {context.title}
GENRE: {context.genre or 'Not specified'}
TONE: {context.tone or 'Not specified'}

CONTENT/SUMMARY:
{context.text[:3000] if context.text else 'No content provided'}

Provide your analysis as JSON with:
- summary: Your contextual assessment (2-3 sentences)
- observations: Array of observations, each with:
  - category: "genre", "influence", "tradition", or "innovation"
  - observation: What you noticed
  - confidence: 0.0-1.0
- key_findings: Array of most important contextual observations
- recommendations: Array of suggestions for better contextual positioning
- score: Overall contextual sophistication score 0-10"""


class CinephileAnalyst(BaseAnalyst):
    """Analyst focused on comparable works and genre conventions.

    Provides reference points for marketing and positioning.
    """

    role = AnalystRole.CINEPHILE
    description = "Identifies comparable works and genre conventions"

    def _build_system_prompt(self) -> str:
        return """You are the CINEPHILE analyst, focused on comparables and references.

Your analytical lens:
- Similar films/shows in genre, tone, or theme
- Reference points for marketing and positioning
- Both obvious and unexpected comparisons
- Audience targeting and appeal
- Genre conventions honored or subverted

Draw on your deep knowledge of cinema and television to identify
meaningful comparisons that illuminate what this work is trying to be
and who it's for."""

    def _build_analysis_prompt(self, context: AnalystContext) -> str:
        return f"""Identify comparables and genre positioning for this script.

TITLE: {context.title}
GENRE: {context.genre or 'Not specified'}
TONE: {context.tone or 'Not specified'}
FORMAT: {context.format}

CONTENT/SUMMARY:
{context.text[:3000] if context.text else 'No content provided'}

Provide your analysis as JSON with:
- summary: Genre/comparable positioning (2-3 sentences)
- observations: Array of observations, each with:
  - category: "comparable", "genre", "audience", or "convention"
  - observation: What you noticed (name specific films/shows)
  - confidence: 0.0-1.0
- key_findings: Array of 5-7 most apt comparables with brief explanations
- recommendations: Array of suggestions for clearer positioning
- score: Distinctiveness/positioning clarity score 0-10"""


class RhetoricianAnalyst(BaseAnalyst):
    """Analyst focused on argument structure and dialogue craft.

    Primary frameworks: Alan Moore (formalism), Grant Morrison (hypersigil).
    """

    role = AnalystRole.RHETORICIAN
    description = "Analyzes argument structure and dialogue craft"

    def _build_system_prompt(self) -> str:
        return """You are the RHETORICIAN analyst, focused on language and dialogue.

Your analytical lens:
- Dialogue craft and authenticity
- Voice distinctiveness per character
- Subtext and implied meaning
- Argumentative structure (if applicable)
- Language as character/worldbuilding
- Rhetorical effectiveness

You draw on the techniques of:
- Alan Moore (dense, layered language)
- Grant Morrison (metafictional dialogue)

Assess the linguistic and rhetorical effectiveness of the writing.
Be specific about dialogue strengths and weaknesses."""

    def _build_analysis_prompt(self, context: AnalystContext) -> str:
        return f"""Analyze the dialogue and rhetorical qualities of this script.

TITLE: {context.title}
TONE: {context.tone or 'Not specified'}

CONTENT/SUMMARY:
{context.text[:3000] if context.text else 'No content provided'}

CHARACTERS: {', '.join(context.character_list[:10]) if context.character_list else 'Unknown'}

Provide your analysis as JSON with:
- summary: Your rhetorical assessment (2-3 sentences)
- observations: Array of observations, each with:
  - category: "dialogue", "voice", "subtext", or "rhetoric"
  - observation: What you noticed
  - location: Where in the script
  - confidence: 0.0-1.0
- key_findings: Array of most important language observations
- recommendations: Array of suggestions for dialogue/rhetoric improvement
- score: Overall dialogue/rhetoric score 0-10"""


class ProducerAnalyst(BaseAnalyst):
    """Analyst focused on practical feasibility and budget implications.

    Provides the practical lens for production considerations.
    """

    role = AnalystRole.PRODUCER
    description = "Assesses practical viability and budget implications"

    def _build_system_prompt(self) -> str:
        return """You are the PRODUCER analyst, focused on practical viability.

Your analytical lens:
- Production complexity (locations, effects, cast size)
- Budget implications and tier
- Casting considerations and star vehicle potential
- Market positioning and timing
- Potential production challenges
- Commercial viability

Provide a practical assessment of bringing this script to screen.
Be specific about production considerations and challenges."""

    def _build_analysis_prompt(self, context: AnalystContext) -> str:
        return f"""Assess the practical production viability of this script.

TITLE: {context.title}
FORMAT: {context.format}
PAGE COUNT: {context.page_count or 'Unknown'}
GENRE: {context.genre or 'Not specified'}

CONTENT/SUMMARY:
{context.text[:3000] if context.text else 'No content provided'}

SCENE COUNT: {len(context.scene_summaries)}
CHARACTER COUNT: {len(context.character_list)}

Provide your analysis as JSON with:
- summary: Your production viability assessment (2-3 sentences)
- observations: Array of observations, each with:
  - category: "budget", "casting", "logistics", or "market"
  - observation: What you noticed
  - confidence: 0.0-1.0
- key_findings: Array of most important production considerations
- recommendations: Array of suggestions for improved production viability
- score: Overall production viability score 0-10"""


class AcademicAnalyst(BaseAnalyst):
    """Analyst focused on theoretical frameworks and rigor.

    Applies classical and contemporary narrative theory.
    """

    role = AnalystRole.ACADEMIC
    description = "Applies theoretical frameworks with rigor"

    def _build_system_prompt(self) -> str:
        return """You are the ACADEMIC analyst, focused on theoretical rigor.

Your analytical lens:
- Classical dramaturgy (Aristotle's Poetics)
- Hero's Journey / Monomyth (Campbell)
- Three-Act Structure (Field, Snyder)
- Character-driven story (McKee)
- Contemporary narrative theory
- Thematic coherence and depth

Apply relevant theoretical frameworks to assess the work's
formal qualities and theoretical coherence."""

    def _build_analysis_prompt(self, context: AnalystContext) -> str:
        return f"""Apply theoretical frameworks to analyze this script.

TITLE: {context.title}
GENRE: {context.genre or 'Not specified'}
FORMAT: {context.format}

CONTENT/SUMMARY:
{context.text[:3000] if context.text else 'No content provided'}

SCENE COUNT: {len(context.scene_summaries)}

Provide your analysis as JSON with:
- summary: Your theoretical assessment (2-3 sentences)
- observations: Array of observations, each with:
  - category: "aristotelian", "campbellian", "structural", or "thematic"
  - observation: What you noticed
  - framework_source: Which theory applies
  - confidence: 0.0-1.0
- key_findings: Array of most important theoretical observations
- recommendations: Array of suggestions for theoretical improvement
- score: Overall theoretical coherence score 0-10"""


class FirstReaderAnalyst(BaseAnalyst):
    """Analyst focused on emotional response and engagement.

    Provides the gut-reaction, audience-surrogate perspective.
    Primary framework: Pixar (emotional engineering).
    """

    role = AnalystRole.FIRST_READER
    description = "Provides emotional response and engagement assessment"

    def _build_system_prompt(self) -> str:
        return """You are the FIRST-READER analyst, providing gut emotional response.

Your analytical lens:
- Initial engagement (did it hook you?)
- Emotional journey (what did you feel?)
- Satisfaction with ending
- What stuck with you
- Overall impression as a reader/viewer
- Entertainment value

You draw on the techniques of:
- Pixar (emotional engineering, making audiences feel)

Be honest about your gut reaction. This is about emotional truth,
not intellectual analysis. What worked? What didn't land?"""

    def _build_analysis_prompt(self, context: AnalystContext) -> str:
        return f"""Describe your emotional response to this script.

TITLE: {context.title}
GENRE: {context.genre or 'Not specified'}
TONE: {context.tone or 'Not specified'}

CONTENT/SUMMARY:
{context.text[:3000] if context.text else 'No content provided'}

SCENES:
{self._format_scenes(context.scene_summaries)}

Provide your analysis as JSON with:
- summary: Your emotional reaction (2-3 sentences, be honest)
- observations: Array of observations, each with:
  - category: "engagement", "emotion", "satisfaction", or "memorable"
  - observation: What you felt/noticed
  - location: Where in the script (optional)
  - confidence: 0.0-1.0
- key_findings: Array of strongest emotional moments/issues
- recommendations: Array of suggestions for emotional improvement
- score: Overall emotional impact score 0-10"""

    def _format_scenes(self, summaries: list[str]) -> str:
        if not summaries:
            return "No scene data available"
        return "\n".join(f"- Scene {i+1}: {s[:100]}" for i, s in enumerate(summaries[:10]))


# Factory function to get analyst by role
def get_analyst(role: AnalystRole | str, provider: LLMProvider | None = None) -> BaseAnalyst:
    """Get an analyst instance for a given role.

    Args:
        role: The analyst role (enum or string).
        provider: LLM provider for the analyst.

    Returns:
        BaseAnalyst instance for the role.

    Raises:
        ValueError: If the role is not recognized.
    """
    if isinstance(role, str):
        try:
            role = AnalystRole(role.lower())
        except ValueError:
            raise ValueError(f"Unknown analyst role: {role}") from None

    analyst_classes = {
        AnalystRole.AESTHETE: AestheteAnalyst,
        AnalystRole.DRAMATURGIST: DramaturgistAnalyst,
        AnalystRole.NARRATOLOGIST: NarratologistAnalyst,
        AnalystRole.ART_HISTORIAN: ArtHistorianAnalyst,
        AnalystRole.CINEPHILE: CinephileAnalyst,
        AnalystRole.RHETORICIAN: RhetoricianAnalyst,
        AnalystRole.PRODUCER: ProducerAnalyst,
        AnalystRole.ACADEMIC: AcademicAnalyst,
        AnalystRole.FIRST_READER: FirstReaderAnalyst,
    }

    analyst_class = analyst_classes.get(role)
    if analyst_class is None:
        raise ValueError(f"No analyst implementation for role: {role}")

    return analyst_class(provider)


def get_all_analysts(provider: LLMProvider | None = None) -> list[BaseAnalyst]:
    """Get instances of all analyst roles.

    Args:
        provider: LLM provider for the analysts.

    Returns:
        List of BaseAnalyst instances.
    """
    return [get_analyst(role, provider) for role in AnalystRole]
