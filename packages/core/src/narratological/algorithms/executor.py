"""Algorithm executor for LLM-powered execution.

Provides a high-level interface for executing algorithms with different
LLM providers, handling prompt construction and result parsing.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

from narratological.algorithms.base import (
    AnalysisResult,
    ExecutableAlgorithm,
    ExecutionMode,
    GenerationResult,
    ValidationResult,
)
from narratological.algorithms.registry import AlgorithmRegistry, get_registry

if TYPE_CHECKING:
    from narratological.llm.providers import LLMProvider


class ExecutorError(Exception):
    """Error during algorithm execution."""

    pass


@dataclass
class ExecutionContext:
    """Context for an algorithm execution."""

    algorithm: ExecutableAlgorithm
    mode: ExecutionMode
    input_data: Any
    provider_name: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class ExecutionLog:
    """Log entry for an algorithm execution."""

    context: ExecutionContext
    result: AnalysisResult | GenerationResult | ValidationResult
    success: bool
    error_message: str | None = None


class AlgorithmExecutor:
    """Executor for running algorithms with LLM providers.

    Provides a unified interface for analyzing, generating, and validating
    narrative content using the formalized algorithms.
    """

    def __init__(
        self,
        provider: LLMProvider,
        registry: AlgorithmRegistry | None = None,
    ):
        """Initialize the executor.

        Args:
            provider: The LLM provider to use for execution.
            registry: Optional algorithm registry. Uses global registry if None.
        """
        self.provider = provider
        self.registry = registry or get_registry()
        self._execution_log: list[ExecutionLog] = []

    def run(
        self,
        algorithm: ExecutableAlgorithm | str,
        mode: ExecutionMode | str,
        input_data: Any,
        **kwargs: Any,
    ) -> AnalysisResult | GenerationResult | ValidationResult:
        """Execute an algorithm in the specified mode.

        Args:
            algorithm: ExecutableAlgorithm or qualified name (e.g., 'pixar.engineer_empathy').
            mode: Execution mode (analyze, generate, validate).
            input_data: Input for the algorithm (text for analyze/validate, dict for generate).
            **kwargs: Additional parameters passed to the execution method.

        Returns:
            Result object appropriate for the execution mode.

        Raises:
            ExecutorError: If execution fails.
            KeyError: If algorithm is not found.
            ValueError: If mode is invalid.
        """
        # Resolve algorithm if string
        if isinstance(algorithm, str):
            if "." in algorithm:
                algorithm = self.registry.get_by_qualified_name(algorithm)
            else:
                raise ValueError(
                    f"Algorithm must be qualified name (study.name), got: {algorithm}"
                )

        # Resolve mode if string
        if isinstance(mode, str):
            try:
                mode = ExecutionMode(mode.lower())
            except ValueError:
                valid_modes = [m.value for m in ExecutionMode]
                raise ValueError(
                    f"Invalid mode '{mode}'. Valid modes: {', '.join(valid_modes)}"
                ) from None

        # Create execution context
        context = ExecutionContext(
            algorithm=algorithm,
            mode=mode,
            input_data=input_data,
            provider_name=type(self.provider).__name__,
            metadata=kwargs,
        )

        try:
            if mode == ExecutionMode.ANALYZE:
                if not isinstance(input_data, str):
                    raise ExecutorError("Analyze mode requires text input")
                result = algorithm.analyze(input_data, self.provider)

            elif mode == ExecutionMode.GENERATE:
                if not isinstance(input_data, dict):
                    raise ExecutorError("Generate mode requires dict input")
                result = algorithm.generate(input_data, self.provider)

            elif mode == ExecutionMode.VALIDATE:
                if not isinstance(input_data, str):
                    raise ExecutorError("Validate mode requires text input")
                result = algorithm.validate(input_data, self.provider)

            else:
                raise ExecutorError(f"Unknown execution mode: {mode}")

            # Log successful execution
            self._execution_log.append(
                ExecutionLog(context=context, result=result, success=True)
            )
            return result

        except Exception as e:
            # Log failed execution
            error_result = self._create_error_result(algorithm, mode, str(e))
            self._execution_log.append(
                ExecutionLog(
                    context=context,
                    result=error_result,
                    success=False,
                    error_message=str(e),
                )
            )
            raise ExecutorError(f"Execution failed: {e}") from e

    def _create_error_result(
        self,
        algorithm: ExecutableAlgorithm,
        mode: ExecutionMode,
        error: str,
    ) -> AnalysisResult | GenerationResult | ValidationResult:
        """Create an error result for failed execution."""
        if mode == ExecutionMode.ANALYZE:
            return AnalysisResult(
                algorithm_name=algorithm.name,
                study_id=algorithm.study_id,
                input_summary="Error during execution",
                findings=[f"Error: {error}"],
                raw_output=error,
            )
        elif mode == ExecutionMode.GENERATE:
            return GenerationResult(
                algorithm_name=algorithm.name,
                study_id=algorithm.study_id,
                generated_content="",
                notes=[f"Error: {error}"],
                raw_output=error,
            )
        else:
            return ValidationResult(
                algorithm_name=algorithm.name,
                study_id=algorithm.study_id,
                is_valid=False,
                criteria_failed=[f"Error: {error}"],
                raw_output=error,
            )

    def analyze(
        self,
        algorithm: ExecutableAlgorithm | str,
        text: str,
    ) -> AnalysisResult:
        """Convenience method for analysis.

        Args:
            algorithm: Algorithm to apply.
            text: Text to analyze.

        Returns:
            AnalysisResult.
        """
        result = self.run(algorithm, ExecutionMode.ANALYZE, text)
        assert isinstance(result, AnalysisResult)
        return result

    def generate(
        self,
        algorithm: ExecutableAlgorithm | str,
        params: dict[str, Any],
    ) -> GenerationResult:
        """Convenience method for generation.

        Args:
            algorithm: Algorithm to use.
            params: Generation parameters.

        Returns:
            GenerationResult.
        """
        result = self.run(algorithm, ExecutionMode.GENERATE, params)
        assert isinstance(result, GenerationResult)
        return result

    def validate(
        self,
        algorithm: ExecutableAlgorithm | str,
        text: str,
    ) -> ValidationResult:
        """Convenience method for validation.

        Args:
            algorithm: Algorithm to validate against.
            text: Text to validate.

        Returns:
            ValidationResult.
        """
        result = self.run(algorithm, ExecutionMode.VALIDATE, text)
        assert isinstance(result, ValidationResult)
        return result

    def analyze_with_multiple(
        self,
        algorithms: list[ExecutableAlgorithm | str],
        text: str,
    ) -> list[AnalysisResult]:
        """Analyze text with multiple algorithms.

        Args:
            algorithms: List of algorithms to apply.
            text: Text to analyze.

        Returns:
            List of AnalysisResults, one per algorithm.
        """
        return [self.analyze(algo, text) for algo in algorithms]

    def analyze_with_study(
        self,
        study_id: str,
        text: str,
    ) -> list[AnalysisResult]:
        """Analyze text with all algorithms from a study.

        Args:
            study_id: Study identifier.
            text: Text to analyze.

        Returns:
            List of AnalysisResults.
        """
        algorithms = self.registry.list_by_study(study_id)
        return [self.analyze(algo, text) for algo in algorithms]

    def get_execution_log(self) -> list[ExecutionLog]:
        """Get the execution log.

        Returns:
            List of ExecutionLog entries.
        """
        return self._execution_log.copy()

    def clear_log(self) -> None:
        """Clear the execution log."""
        self._execution_log.clear()

    def get_successful_executions(self) -> list[ExecutionLog]:
        """Get only successful executions from the log."""
        return [log for log in self._execution_log if log.success]

    def get_failed_executions(self) -> list[ExecutionLog]:
        """Get only failed executions from the log."""
        return [log for log in self._execution_log if not log.success]


def create_executor(
    provider_name: str = "mock",
    **provider_kwargs: Any,
) -> AlgorithmExecutor:
    """Factory function to create an executor with a specified provider.

    Args:
        provider_name: Name of the provider ('anthropic', 'openai', 'mock').
        **provider_kwargs: Additional arguments for the provider.

    Returns:
        AlgorithmExecutor instance.
    """
    from narratological.llm.providers import get_provider

    provider = get_provider(provider_name, **provider_kwargs)
    return AlgorithmExecutor(provider)
