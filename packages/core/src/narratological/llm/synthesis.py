"""Multi-role orchestration and synthesis.

Coordinates analysis across multiple analyst roles and synthesizes
their insights into unified assessments.
"""

from __future__ import annotations

import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import TYPE_CHECKING

from narratological.llm.roles import get_analyst
from narratological.models.analyst import (
    ActivationLayer,
    AnalystContext,
    AnalystObservation,
    AnalystRole,
    MultiRoleAnalysis,
    RoleAnalysisResult,
    SynthesisConfig,
)

if TYPE_CHECKING:
    from narratological.llm.providers import LLMProvider
    from narratological.models.analysis import Script


class MultiRoleOrchestrator:
    """Orchestrates multi-role script analysis.

    Coordinates analysis across multiple analyst perspectives,
    handles parallel execution, and synthesizes results.
    """

    def __init__(self, provider: LLMProvider | None = None):
        """Initialize the orchestrator.

        Args:
            provider: LLM provider for analysts.
        """
        self.provider = provider

    def analyze(
        self,
        text: str,
        title: str,
        config: SynthesisConfig | None = None,
        **context_kwargs,
    ) -> MultiRoleAnalysis:
        """Perform multi-role analysis on text.

        Args:
            text: The script text or summary to analyze.
            title: Script title.
            config: Synthesis configuration.
            **context_kwargs: Additional context parameters.

        Returns:
            MultiRoleAnalysis with all role results synthesized.
        """
        config = config or SynthesisConfig()
        context = AnalystContext(
            title=title,
            text=text,
            **context_kwargs,
        )

        return self.analyze_context(context, config)

    def analyze_script(
        self,
        script: Script,
        config: SynthesisConfig | None = None,
    ) -> MultiRoleAnalysis:
        """Perform multi-role analysis on a Script model.

        Args:
            script: The Script model to analyze.
            config: Synthesis configuration.

        Returns:
            MultiRoleAnalysis with all role results synthesized.
        """
        config = config or SynthesisConfig()
        context = AnalystContext.from_script(script)
        return self.analyze_context(context, config)

    def analyze_context(
        self,
        context: AnalystContext,
        config: SynthesisConfig,
    ) -> MultiRoleAnalysis:
        """Perform multi-role analysis with a pre-built context.

        Args:
            context: The analysis context.
            config: Synthesis configuration.

        Returns:
            MultiRoleAnalysis with all role results synthesized.
        """
        start_time = time.time()

        # Get active roles from config
        roles = config.activation_layer.roles

        # Execute analysis for each role
        if config.parallel_execution and self.provider is not None:
            role_results = self._execute_parallel(roles, context)
        else:
            role_results = self._execute_sequential(roles, context)

        # Synthesize results
        analysis = self._synthesize_results(
            context.title,
            role_results,
            config,
        )

        # Add execution time
        execution_time_ms = int((time.time() - start_time) * 1000)
        analysis.execution_time_ms = execution_time_ms

        return analysis

    def _execute_sequential(
        self,
        roles: list[AnalystRole],
        context: AnalystContext,
    ) -> dict[str, RoleAnalysisResult]:
        """Execute role analyses sequentially."""
        results = {}

        for role in roles:
            analyst = get_analyst(role, self.provider)
            result = analyst.analyze(context)
            results[role.value] = result

        return results

    def _execute_parallel(
        self,
        roles: list[AnalystRole],
        context: AnalystContext,
    ) -> dict[str, RoleAnalysisResult]:
        """Execute role analyses in parallel."""
        results = {}

        def analyze_role(role: AnalystRole) -> tuple[str, RoleAnalysisResult]:
            analyst = get_analyst(role, self.provider)
            return role.value, analyst.analyze(context)

        with ThreadPoolExecutor(max_workers=min(len(roles), 4)) as executor:
            futures = {
                executor.submit(analyze_role, role): role
                for role in roles
            }

            for future in as_completed(futures):
                role_name, result = future.result()
                results[role_name] = result

        return results

    def _synthesize_results(
        self,
        title: str,
        role_results: dict[str, RoleAnalysisResult],
        config: SynthesisConfig,
    ) -> MultiRoleAnalysis:
        """Synthesize individual role results into unified analysis."""
        # Collect all observations
        all_observations = []
        for result in role_results.values():
            all_observations.extend(result.observations)

        # Find consensus and divergent observations
        consensus, divergent = self._find_consensus_divergence(all_observations)

        # Calculate overall score
        scores = [
            r.score for r in role_results.values()
            if r.score is not None
        ]
        overall_score = sum(scores) / len(scores) if scores else None

        # Compile priority recommendations
        all_recommendations = []
        for result in role_results.values():
            all_recommendations.extend(result.recommendations)

        # Deduplicate and prioritize (simple approach: take unique ones)
        seen = set()
        priority_recommendations = []
        for rec in all_recommendations:
            rec_lower = rec.lower().strip()
            if rec_lower not in seen:
                seen.add(rec_lower)
                priority_recommendations.append(rec)

        priority_recommendations = priority_recommendations[:10]  # Top 10

        # Build overall summary
        overall_summary = self._build_summary(role_results, overall_score)

        return MultiRoleAnalysis(
            title=title,
            role_results=role_results,
            consensus_observations=consensus,
            divergent_observations=divergent,
            overall_summary=overall_summary,
            overall_score=overall_score,
            priority_recommendations=priority_recommendations,
            config=config,
        )

    def _find_consensus_divergence(
        self,
        observations: list[AnalystObservation],
    ) -> tuple[list[AnalystObservation], list[AnalystObservation]]:
        """Find observations with consensus vs divergence.

        Consensus: Multiple roles note similar things
        Divergence: Conflicting observations
        """
        # Group by category
        by_category: dict[str, list[AnalystObservation]] = {}
        for obs in observations:
            if obs.category not in by_category:
                by_category[obs.category] = []
            by_category[obs.category].append(obs)

        consensus = []
        divergent = []

        # Simple heuristic: if multiple roles observe in same category,
        # it's a consensus area; high variance in confidence suggests divergence
        for _category, obs_list in by_category.items():
            if len(obs_list) >= 2:
                # Multiple roles observed this category
                confidences = [o.confidence for o in obs_list]
                avg_confidence = sum(confidences) / len(confidences)

                if avg_confidence >= 0.7:
                    # High confidence consensus
                    consensus.extend(obs_list)
                else:
                    # Lower confidence suggests divergence
                    divergent.extend(obs_list)

        return consensus, divergent

    def _build_summary(
        self,
        role_results: dict[str, RoleAnalysisResult],
        overall_score: float | None,
    ) -> str:
        """Build an overall summary from role results."""
        summaries = []

        # Extract key points from each role
        for role_name, result in role_results.items():
            if result.summary:
                summaries.append(f"**{role_name.replace('_', ' ').title()}**: {result.summary}")

        if not summaries:
            return "No analysis available."

        score_note = ""
        if overall_score is not None:
            score_note = f"\n\n**Overall Score**: {overall_score:.1f}/10"

        return "\n\n".join(summaries) + score_note


class AnalysisOrchestrator:
    """High-level orchestrator combining report generation and multi-role analysis.

    Provides a unified interface for comprehensive script analysis.
    """

    def __init__(self, provider: LLMProvider | None = None):
        """Initialize the orchestrator.

        Args:
            provider: LLM provider for all analysis.
        """
        self.provider = provider
        self.multi_role = MultiRoleOrchestrator(provider)

    def full_analysis(
        self,
        script: Script,
        activation_layer: ActivationLayer = ActivationLayer.FULL,
    ) -> dict:
        """Perform comprehensive analysis with all available methods.

        Args:
            script: The script to analyze.
            activation_layer: Which roles to activate.

        Returns:
            Dictionary with all analysis results.
        """
        from narratological.generators import (
            BeatMapReportGenerator,
            CharacterAtlasReportGenerator,
            CoverageReportGenerator,
            StructuralReportGenerator,
        )

        results = {}

        # Generate reports
        try:
            beat_map_gen = BeatMapReportGenerator(self.provider)
            results["beat_map"] = beat_map_gen.generate(script)
        except Exception as e:
            results["beat_map_error"] = str(e)

        try:
            structural_gen = StructuralReportGenerator(self.provider)
            results["structural"] = structural_gen.generate(script)
        except Exception as e:
            results["structural_error"] = str(e)

        try:
            character_gen = CharacterAtlasReportGenerator(self.provider)
            results["character_atlas"] = character_gen.generate(script)
        except Exception as e:
            results["character_atlas_error"] = str(e)

        try:
            coverage_gen = CoverageReportGenerator(self.provider)
            results["coverage"] = coverage_gen.generate(script)
        except Exception as e:
            results["coverage_error"] = str(e)

        # Multi-role analysis
        config = SynthesisConfig(activation_layer=activation_layer)
        try:
            results["multi_role"] = self.multi_role.analyze_script(script, config)
        except Exception as e:
            results["multi_role_error"] = str(e)

        return results
