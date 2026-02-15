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
        debate_mode: bool = False,
    ) -> ScriptDoctorResult:
        """Perform a 'Co-Authored' analysis pass.

        Args:
            context: The script context.
            primary_study: The first creator study.
            secondary_study: The second creator study.
            theme: Optional unifying theme for the pair.
            debate_mode: Whether to run in exhaustive multi-agent debate mode.

        Returns:
            ScriptDoctorResult with collaborative feedback.
        """
        pair = CoAuthoringPair(
            primary_id=primary_study.id,
            secondary_id=secondary_study.id,
            theme=theme or f"{primary_study.creator} & {secondary_study.creator} Collaboration",
        )

        system_prompt = self._build_system_prompt(primary_study, secondary_study, pair, debate_mode)
        analysis_prompt = self._build_analysis_prompt(context, debate_mode)

        response = self.provider.complete_structured(
            analysis_prompt,
            ScriptDoctorResult,
            system=system_prompt,
        )

        return response

    def _build_system_prompt(
        self, primary: Study, secondary: Study, pair: CoAuthoringPair, debate_mode: bool = False
    ) -> str:
        """Build the system prompt for the collaborative duo."""
        return f"""You are a 'Script Doctor' duo consisting of {primary.creator} and {secondary.creator}.
Your goal is to provide joint feedback on a script using your combined narratological frameworks.

**{primary.creator}'s Perspective:**
- Philosophy: {primary.axioms[0].statement if primary.axioms else 'N/A'}
- Core Algorithms: {', '.join([a.name for a in primary.core_algorithms[:2]])}

**{secondary.creator}'s Perspective:**
- Philosophy: {secondary.axioms[0].statement if secondary.axioms else 'N/A'}
- Core Algorithms: {', '.join([a.name for a in secondary.core_algorithms[:2]])}

## Interaction Rules
1. Respond ONLY with a strictly formatted JSON object matching the ScriptDoctorResult schema.
2. Use specific terminology: '{primary.creator}' should use {primary.core_algorithms[0].name if primary.core_algorithms else 'their algorithms'}, and '{secondary.creator}' should use {secondary.core_algorithms[0].name if secondary.core_algorithms else 'their algorithms'}.
3. Reach a final, unified 'prescription'.
"""

    def _build_analysis_prompt(self, context: AnalystContext, debate_mode: bool = False) -> str:
        """Build the prompt for the specific script."""
        debate_instruction = ""
        if debate_mode:
            debate_instruction = """
## DEBATE TASK
Perform a 3-round dialectical analysis:
- ROUND 1: Initial individual critiques.
- ROUND 2: Challenge each other's structural assumptions.
- ROUND 3: Resolve conflicts into joint recommendations.
Populate 'debate_rounds' with these details.
"""

        return f"""Analyze the script "{context.title}" ({context.genre}, {context.tone}) from your joint perspective.

SCRIPT DATA:
{context.text}
Scenes: {', '.join(context.scene_summaries[:10])}
{debate_instruction}

Respond with a JSON object containing:
- pair: {{primary_id, secondary_id, theme}}
- dialogue: list of {{creator, feedback}}
- debate_rounds: list of {{round, content}}
- joint_recommendations: list of strings
- creative_tension: list of strings
- final_prescription: string
"""
