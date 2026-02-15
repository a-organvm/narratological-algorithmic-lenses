"""Causal Binding Diagnostic.

Tests the BUT/THEREFORE vs AND THEN ratio to assess
narrative causal strength.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated

from pydantic import BaseModel, Field, BeforeValidator

from narratological.diagnostics.base import BaseDiagnostic
from narratological.diagnostics.models import (
    DiagnosticContext,
    DiagnosticType,
    SceneTransition,
)
from narratological.models.analysis import ConnectorType
from narratological.models.report import DiagnosticIssue, DiagnosticSeverity

if TYPE_CHECKING:
    from narratological.llm.providers import LLMProvider


def ensure_list(v):
    if isinstance(v, str):
        return [v]
    return v


class LLMTransitionAnalysis(BaseModel):
    """LLM response for scene transition analysis."""

    from_scene: int
    to_scene: int
    connector: str
    explanation: str
    is_causal: bool


class LLMCausalResponse(BaseModel):
    """LLM response for causal binding analysis."""

    transitions: list[LLMTransitionAnalysis] = Field(default_factory=list)
    weak_transitions: list[int] = Field(
        default_factory=list,
        description="Scene numbers with weak causal binding",
    )
    recommendations: Annotated[list[str], BeforeValidator(ensure_list)] = Field(default_factory=list)


class CausalBindingDiagnostic(BaseDiagnostic):
    """Diagnostic for scene-to-scene causal binding.

    Analyzes transitions between scenes to determine if they're
    connected by causal logic (BUT/THEREFORE) or mere sequence (AND THEN).

    The "South Park rule": Strong stories use BUT/THEREFORE between beats,
    not AND THEN. Target is >80% causal connectors.
    """

    diagnostic_type = DiagnosticType.CAUSAL_BINDING
    description = "Analyzes causal binding between scenes"

    def run(self, context: DiagnosticContext) -> list[DiagnosticIssue]:
        """Run the causal binding diagnostic.

        Args:
            context: The diagnostic context with scene data.

        Returns:
            List of issues found with weak causal binding.
        """
        can_run, error = self.can_run(context)
        if not can_run:
            return [
                self.create_issue(
                    description=error or "Cannot run diagnostic",
                    severity=DiagnosticSeverity.INFO,
                    recommendation="Provide scene data with connectors",
                )
            ]

        issues = []

        # Check if transitions are available or need analysis
        if context.transitions:
            transitions = context.transitions
        elif context.beat_map_available:
            transitions = self._extract_transitions_from_context(context)
        elif self.provider is not None:
            transitions = self._analyze_transitions_with_llm(context)
        else:
            # Cannot analyze without data or LLM
            return [
                self.create_issue(
                    description="Cannot analyze causal binding without scene connectors or LLM",
                    severity=DiagnosticSeverity.INFO,
                    recommendation="Provide scene connector annotations or use LLM provider",
                )
            ]

        # Calculate score
        score = self._calculate_score_from_transitions(transitions)

        # Generate issues for weak transitions
        weak_transitions = [t for t in transitions if not t.is_causal]

        for trans in weak_transitions:
            issues.append(
                self.create_issue(
                    description=f"Weak causal binding: Scene {trans.from_scene} → {trans.to_scene} connected by AND THEN",
                    severity=DiagnosticSeverity.WARNING,
                    location=f"Scenes {trans.from_scene}-{trans.to_scene}",
                    recommendation=f"Consider how Scene {trans.to_scene} could be a consequence of (THEREFORE) or contradiction to (BUT) Scene {trans.from_scene}",
                )
            )

        # Add overall score issue
        overall_severity = self._get_severity_for_causal_binding(score)
        
        if score >= self.thresholds.causal_binding_excellent:
            recommendation = "Excellent causal density. The narrative drive is self-sustaining."
        elif score >= self.thresholds.causal_binding_good:
            recommendation = "Strong binding. Focus on tightening the remaining 'AND THEN' transitions."
        elif score >= self.thresholds.causal_binding_adequate:
            recommendation = "Loose binding. The narrative feels episodic. Replace 'AND THEN' with 'THEREFORE' or 'BUT'."
        else:
            recommendation = "Critical failure of causality. The story is a series of disconnected events. Rewrite for causal logic."

        issues.append(
            self.create_issue(
                description=f"Overall causal binding ratio: {score:.0%} (Target >{self.thresholds.causal_binding_good:.0%})",
                severity=overall_severity,
                recommendation=recommendation,
            )
        )

        return issues

    def calculate_score(self, context: DiagnosticContext) -> float:
        """Calculate the causal binding ratio.

        Args:
            context: The diagnostic context.

        Returns:
            Ratio from 0.0 to 1.0 (proportion of causal transitions).
        """
        if context.transitions:
            return self._calculate_score_from_transitions(context.transitions)
        elif context.beat_map_available:
            transitions = self._extract_transitions_from_context(context)
            return self._calculate_score_from_transitions(transitions)

        # Cannot calculate without data
        return 0.0

    def _requires_llm(self) -> bool:
        """Can work algorithmically if connectors are annotated."""
        return False

    def _get_severity_for_causal_binding(self, score: float) -> DiagnosticSeverity:
        """Get severity based on causal binding score."""
        if score >= self.thresholds.causal_binding_excellent:
            return DiagnosticSeverity.INFO
        elif score >= self.thresholds.causal_binding_good:
            return DiagnosticSeverity.SUGGESTION
        elif score >= self.thresholds.causal_binding_adequate:
            return DiagnosticSeverity.WARNING
        else:
            return DiagnosticSeverity.CRITICAL

    def _extract_transitions_from_context(
        self,
        context: DiagnosticContext,
    ) -> list[SceneTransition]:
        """Extract transitions from scene data."""
        transitions = []

        for i in range(len(context.scenes) - 1):
            scene = context.scenes[i]
            next_scene = context.scenes[i + 1]

            connector_str = scene.get("connector")
            connector = None
            is_causal = False

            if connector_str:
                connector_map = {
                    "BUT": (ConnectorType.BUT, True),
                    "THEREFORE": (ConnectorType.THEREFORE, True),
                    "AND_THEN": (ConnectorType.AND_THEN, False),
                    "AND THEN": (ConnectorType.AND_THEN, False),
                    "MEANWHILE": (ConnectorType.MEANWHILE, False),
                }
                result = connector_map.get(connector_str.upper())
                if result:
                    connector, is_causal = result

            transitions.append(
                SceneTransition(
                    from_scene=scene.get("number", i + 1),
                    to_scene=next_scene.get("number", i + 2),
                    connector=connector,
                    is_causal=is_causal,
                )
            )

        return transitions

    def _analyze_transitions_with_llm(
        self,
        context: DiagnosticContext,
    ) -> list[SceneTransition]:
        """Use LLM to analyze scene transitions."""
        if self.provider is None:
            return []

        prompt = self._build_analysis_prompt(context)

        try:
            response = self.provider.complete_structured(
                prompt,
                LLMCausalResponse,
                system=self._build_system_prompt(),
            )

            transitions = []
            for llm_trans in response.transitions:
                connector_map = {
                    "BUT": ConnectorType.BUT,
                    "THEREFORE": ConnectorType.THEREFORE,
                    "AND_THEN": ConnectorType.AND_THEN,
                    "AND THEN": ConnectorType.AND_THEN,
                    "MEANWHILE": ConnectorType.MEANWHILE,
                }
                connector = connector_map.get(llm_trans.connector.upper())

                transitions.append(
                    SceneTransition(
                        from_scene=llm_trans.from_scene,
                        to_scene=llm_trans.to_scene,
                        connector=connector,
                        explanation=llm_trans.explanation,
                        is_causal=llm_trans.is_causal,
                    )
                )

            return transitions

        except Exception as e:
            print(f"[DEBUG] LLM Causal Analysis failed: {e}")
            import traceback
            traceback.print_exc()
            return []

    def _calculate_score_from_transitions(
        self,
        transitions: list[SceneTransition],
    ) -> float:
        """Calculate causal binding ratio from transitions."""
        if not transitions:
            return 0.0

        causal_count = sum(1 for t in transitions if t.is_causal)
        # Only count transitions that have connectors for the ratio
        evaluated = [t for t in transitions if t.connector is not None]

        if not evaluated:
            return 0.0

        return causal_count / len(evaluated)

    def _build_system_prompt(self) -> str:
        """Build system prompt for LLM analysis."""
        return """You are analyzing scene transitions for causal binding.

For each transition between scenes, determine the connector type:
- BUT: The next scene contradicts, challenges, or obstacles what came before
- THEREFORE: The next scene is a direct consequence of what came before
- AND_THEN: The next scene simply happens after, without causal connection
- MEANWHILE: Parallel action (also non-causal)

Strong narratives use BUT and THEREFORE (causal connectors).
Weak narratives use AND_THEN (episodic, non-causal)."""

    def _build_analysis_prompt(self, context: DiagnosticContext) -> str:
        """Build analysis prompt for LLM."""
        scenes_text = []
        for s in context.scenes[:30]:  # Limit for context window
            scenes_text.append(
                f"Scene {s.get('number', '?')}: {s.get('summary', 'No summary')}"
            )

        return f"""Analyze the causal binding between scenes in this script.

TITLE: {context.title}

SCENES:
{chr(10).join(scenes_text)}

For each transition between consecutive scenes, determine:
1. The connector type (BUT, THEREFORE, AND_THEN, MEANWHILE)
2. Whether it's causal (BUT/THEREFORE = causal, others = non-causal)
3. Brief explanation of why

Respond with JSON containing:
- transitions: Array of transition analyses
- weak_transitions: Scene numbers with weak (AND_THEN) binding
- recommendations: Suggestions for improving causal binding"""
