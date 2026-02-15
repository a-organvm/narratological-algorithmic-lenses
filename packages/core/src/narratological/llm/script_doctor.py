"""Script Doctor analyst for collaborative multi-role synthesis.

Uses pairs of creator-based studies to provide 'co-authored' feedback
and resolve creative tensions.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from narratological.models.analyst import (
    AnalystContext,
    CoAuthoringPair,
    ScriptDoctorResult,
)

if TYPE_CHECKING:
    from narratological.llm.providers import LLMProvider
    from narratological.models.study import Study


class ScriptDoctorAnalyst:
    """Specialized analyst that simulates a collaboration between two creators.

    This analyst uses Sequence Pairs from the compendium to drive synthesis,
    presenting feedback as a dialogue between two distinct narratological lenses.
    """

    def __init__(self, provider: LLMProvider):
        """Initialize the script doctor.

        Args:
            provider: LLM provider for analysis.
        """
        self.provider = provider

    def analyze(
        self,
        context: AnalystContext,
        primary_study: Study,
        secondary_study: Study,
        theme: str | None = None,
    ) -> ScriptDoctorResult:
        """Perform a 'Co-Authored' analysis pass.

        Args:
            context: The script context.
            primary_study: The first creator study.
            secondary_study: The second creator study.
            theme: Optional unifying theme for the pair.

        Returns:
            ScriptDoctorResult with collaborative feedback.
        """
        pair = CoAuthoringPair(
            primary_id=primary_study.id,
            secondary_id=secondary_study.id,
            theme=theme or f"{primary_study.creator} & {secondary_study.creator} Collaboration",
        )

        system_prompt = self._build_system_prompt(primary_study, secondary_study, pair)
        analysis_prompt = self._build_analysis_prompt(context)

        response = self.provider.complete_structured(
            analysis_prompt,
            ScriptDoctorResult,
            system=system_prompt,
        )

        return response

    def _build_system_prompt(
        self, primary: Study, secondary: Study, pair: CoAuthoringPair
    ) -> str:
        """Build the system prompt for the collaborative duo."""
        return f"""You are a 'Script Doctor' duo consisting of {primary.creator} and {secondary.creator}.
Your goal is to provide joint feedback on a script using your combined narratological frameworks.

**{primary.creator}'s Perspective:**
- Philosophy: {primary.axioms[0].statement if primary.axioms else 'N/A'}
- Primary Mode: {primary.category.value}

**{secondary.creator}'s Perspective:**
- Philosophy: {secondary.axioms[0].statement if secondary.axioms else 'N/A'}
- Primary Mode: {secondary.category.value}

**Collaboration Theme:** {pair.theme}

## Interaction Rules
1. Format your feedback as a collaborative dialogue between the two of you.
2. Identify areas where your philosophies agree (Consensus).
3. Identify areas of creative tension where you might disagree on how to fix a scene.
4. Reach a final, unified 'prescription' for the writer.
5. Use your specific algorithmic terminology (e.g., 'Causal Binding', 'Sculpting in Time', 'Poetic Logic').

## Output Format
You MUST return a JSON object matching the ScriptDoctorResult schema.
The 'dialogue' field should be a list of {{'creator': name, 'feedback': text}} entries.
"""

    def _build_analysis_prompt(self, context: AnalystContext) -> str:
        """Build the prompt for the specific script."""
        return f"""Analyze the following script from your joint perspective:

Title: {context.title}
Genre: {context.genre}
Tone: {context.tone}

Text/Summary:
{context.text}

Scene Summaries:
{chr(10).join(context.scene_summaries[:20])}

Focus Areas: {', '.join(context.focus_areas)}
"""
