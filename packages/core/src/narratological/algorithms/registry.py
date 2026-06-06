"""Algorithm registry for loading and indexing all algorithms.

Provides centralized access to all 92 algorithms across 14 studies,
with support for searching, filtering, and retrieval.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from narratological.algorithms.base import ExecutableAlgorithm
from narratological.loader import load_compendium
from narratological.models.study import Compendium

if TYPE_CHECKING:
    from os import PathLike


@dataclass
class AlgorithmInfo:
    """Summary information about an algorithm."""

    name: str
    study_id: str
    study_creator: str
    purpose: str
    input_count: int
    output_count: int

    @property
    def qualified_name(self) -> str:
        """Full qualified name: study_id.algorithm_name."""
        return f"{self.study_id}.{self.name}"


class AlgorithmRegistry:
    """Registry for loading and accessing all algorithms.

    Loads algorithms from the unified JSON compendium and provides
    methods for retrieval, search, and filtering.
    """

    def __init__(self, compendium: Compendium | None = None):
        """Initialize the registry.

        Args:
            compendium: Optional pre-loaded compendium. If None, loads from default path.
        """
        self._compendium = compendium or load_compendium()
        self._algorithms: dict[str, ExecutableAlgorithm] = {}
        self._by_study: dict[str, list[str]] = {}
        self._load_algorithms()

    def _load_algorithms(self) -> None:
        """Load all algorithms from the compendium."""
        for study_id, study in self._compendium.studies.items():
            self._by_study[study_id] = []

            for algo in study.core_algorithms:
                key = f"{study_id}.{algo.name}"
                executable = ExecutableAlgorithm(
                    algorithm=algo,
                    study_id=study_id,
                    study_creator=study.creator,
                    study_work=study.work,
                )
                self._algorithms[key] = executable
                self._by_study[study_id].append(key)

    @classmethod
    def from_path(cls, path: str | PathLike[str]) -> AlgorithmRegistry:
        """Create a registry from a specific compendium path.

        Args:
            path: Path to the unified JSON file.

        Returns:
            AlgorithmRegistry instance.
        """
        compendium = load_compendium(path)
        return cls(compendium)

    def get(self, study_id: str, algo_name: str) -> ExecutableAlgorithm:
        """Get a specific algorithm by study ID and name.

        Args:
            study_id: The study identifier (e.g., 'pixar', 'bergman').
            algo_name: The algorithm name (e.g., 'engineer_empathy').

        Returns:
            ExecutableAlgorithm instance.

        Raises:
            KeyError: If the algorithm is not found.
        """
        key = f"{study_id}.{algo_name}"
        if key not in self._algorithms:
            # Try case-insensitive match
            key_lower = key.lower()
            for k in self._algorithms:
                if k.lower() == key_lower:
                    return self._algorithms[k]

            # Try partial match on algorithm name
            for k, algo in self._algorithms.items():
                if algo.name.lower() == algo_name.lower() and k.startswith(study_id):
                    return algo

            available = self.list_by_study(study_id)
            if available:
                algo_names = [a.name for a in available]
                raise KeyError(
                    f"Algorithm '{algo_name}' not found in study '{study_id}'. "
                    f"Available: {', '.join(algo_names)}"
                )
            raise KeyError(
                f"Study '{study_id}' not found. "
                f"Available studies: {', '.join(self.list_studies())}"
            )

        return self._algorithms[key]

    def get_by_qualified_name(self, qualified_name: str) -> ExecutableAlgorithm:
        """Get an algorithm by its qualified name (study_id.algo_name).

        Args:
            qualified_name: Full name like 'pixar.engineer_empathy'.

        Returns:
            ExecutableAlgorithm instance.

        Raises:
            KeyError: If the algorithm is not found.
        """
        if qualified_name in self._algorithms:
            return self._algorithms[qualified_name]

        # Try case-insensitive and partial matching
        name_lower = qualified_name.lower()
        for key, algo in self._algorithms.items():
            if key.lower() == name_lower:
                return algo

        raise KeyError(f"Algorithm '{qualified_name}' not found.")

    def list_by_study(self, study_id: str) -> list[ExecutableAlgorithm]:
        """Get all algorithms for a specific study.

        Args:
            study_id: The study identifier.

        Returns:
            List of ExecutableAlgorithm instances.
        """
        if study_id not in self._by_study:
            # Try case-insensitive match
            for sid in self._by_study:
                if sid.lower() == study_id.lower():
                    return [self._algorithms[key] for key in self._by_study[sid]]
            return []

        return [self._algorithms[key] for key in self._by_study[study_id]]

    def list_studies(self) -> list[str]:
        """Get all study IDs with algorithms.

        Returns:
            List of study IDs.
        """
        return list(self._by_study.keys())

    def search(self, query: str) -> list[ExecutableAlgorithm]:
        """Search algorithms by name, purpose, or pseudocode content.

        Args:
            query: Search query (case-insensitive).

        Returns:
            List of matching ExecutableAlgorithm instances.
        """
        query_lower = query.lower()
        results = []

        for algo in self._algorithms.values():
            if (
                query_lower in algo.name.lower()
                or query_lower in algo.purpose.lower()
                or query_lower in algo.pseudocode.lower()
            ):
                results.append(algo)

        return results

    def all(self) -> list[ExecutableAlgorithm]:
        """Get all algorithms.

        Returns:
            List of all ExecutableAlgorithm instances.
        """
        return list(self._algorithms.values())

    def count(self) -> int:
        """Get total number of algorithms.

        Returns:
            Number of algorithms in the registry.
        """
        return len(self._algorithms)

    def count_by_study(self) -> dict[str, int]:
        """Get algorithm counts per study.

        Returns:
            Dict mapping study_id to algorithm count.
        """
        return {sid: len(keys) for sid, keys in self._by_study.items()}

    def info(self) -> list[AlgorithmInfo]:
        """Get summary information for all algorithms.

        Returns:
            List of AlgorithmInfo objects.
        """
        return [
            AlgorithmInfo(
                name=algo.name,
                study_id=algo.study_id,
                study_creator=algo.study_creator,
                purpose=algo.purpose,
                input_count=len(algo.inputs),
                output_count=len(algo.outputs),
            )
            for algo in self._algorithms.values()
        ]

    def info_by_study(self, study_id: str) -> list[AlgorithmInfo]:
        """Get summary information for algorithms in a study.

        Args:
            study_id: The study identifier.

        Returns:
            List of AlgorithmInfo objects.
        """
        return [
            AlgorithmInfo(
                name=algo.name,
                study_id=algo.study_id,
                study_creator=algo.study_creator,
                purpose=algo.purpose,
                input_count=len(algo.inputs),
                output_count=len(algo.outputs),
            )
            for algo in self.list_by_study(study_id)
        ]

    def __len__(self) -> int:
        """Number of algorithms in the registry."""
        return len(self._algorithms)

    def __contains__(self, key: str) -> bool:
        """Check if an algorithm exists by qualified name."""
        return key in self._algorithms or key.lower() in (
            k.lower() for k in self._algorithms
        )

    def __iter__(self):
        """Iterate over all algorithms."""
        return iter(self._algorithms.values())


# Global registry instance (lazy-loaded)
_registry: AlgorithmRegistry | None = None


def get_registry() -> AlgorithmRegistry:
    """Get the global algorithm registry.

    Lazily loads the registry on first access.

    Returns:
        AlgorithmRegistry instance.
    """
    global _registry
    if _registry is None:
        _registry = AlgorithmRegistry()
    return _registry


def reset_registry() -> None:
    """Reset the global registry (useful for testing)."""
    global _registry
    _registry = None
