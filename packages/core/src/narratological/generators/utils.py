"""Utility functions for report generators.

Provides helper functions for common calculations and data transformations
used across multiple report generators.
"""

from __future__ import annotations

from collections import Counter
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from narratological.models.analysis import Character, Scene, Script
    from narratological.models.report import BeatMapEntry


def calculate_screen_time(
    character_name: str,
    scenes: list[Scene],
) -> float:
    """Calculate the screen time percentage for a character.

    Screen time is calculated as the percentage of scenes in which
    the character appears.

    Args:
        character_name: Name of the character to calculate for.
        scenes: List of all scenes in the script.

    Returns:
        Float between 0.0 and 1.0 representing screen time percentage.
    """
    if not scenes:
        return 0.0

    appearances = sum(1 for scene in scenes if character_name in scene.characters_present)

    return appearances / len(scenes)


def find_protagonist(script: Script) -> str | None:
    """Identify the protagonist from script characters.

    Uses multiple heuristics:
    1. Character explicitly marked as protagonist
    2. Character with highest screen time
    3. Character appearing first if tie

    Args:
        script: The script to analyze.

    Returns:
        Name of the protagonist, or None if no characters exist.
    """
    if not script.characters:
        return None

    # Check for explicit protagonist role
    for char in script.characters:
        if char.role.lower() == "protagonist":
            return char.name

    # Fall back to screen time calculation
    if not script.scenes:
        # Return first character if no scenes
        return script.characters[0].name if script.characters else None

    screen_times = {
        char.name: calculate_screen_time(char.name, script.scenes) for char in script.characters
    }

    if not screen_times:
        return None

    return max(screen_times, key=lambda name: screen_times[name])


def find_antagonist(script: Script) -> str | None:
    """Identify the antagonist from script characters.

    Uses multiple heuristics:
    1. Character explicitly marked as antagonist
    2. Character opposing the protagonist

    Args:
        script: The script to analyze.

    Returns:
        Name of the antagonist, or None if not identifiable.
    """
    if not script.characters:
        return None

    # Check for explicit antagonist role
    for char in script.characters:
        if char.role.lower() == "antagonist":
            return char.name

    return None


def calculate_function_distribution(
    entries: list[BeatMapEntry],
) -> dict[str, int]:
    """Calculate the distribution of beat functions.

    Args:
        entries: List of beat map entries.

    Returns:
        Dictionary mapping function names to counts.
    """
    return dict(Counter(entry.function.value for entry in entries))


def calculate_connector_distribution(
    entries: list[BeatMapEntry],
) -> dict[str, int]:
    """Calculate the distribution of scene connectors.

    Args:
        entries: List of beat map entries.

    Returns:
        Dictionary mapping connector types to counts.
    """
    connectors = [entry.connector.value for entry in entries if entry.connector is not None]
    return dict(Counter(connectors))


def calculate_average_tension(entries: list[BeatMapEntry]) -> float | None:
    """Calculate the average tension level across scenes.

    Args:
        entries: List of beat map entries.

    Returns:
        Average tension (1-10 scale) or None if no entries.
    """
    if not entries:
        return None

    return sum(entry.tension for entry in entries) / len(entries)


def calculate_tension_variance(entries: list[BeatMapEntry]) -> float | None:
    """Calculate the variance in tension levels.

    Higher variance indicates more dynamic pacing.

    Args:
        entries: List of beat map entries.

    Returns:
        Variance value or None if insufficient entries.
    """
    if len(entries) < 2:
        return None

    avg = calculate_average_tension(entries)
    if avg is None:
        return None

    variance = sum((entry.tension - avg) ** 2 for entry in entries) / len(entries)
    return variance


def calculate_act_proportions(
    act_boundaries: list[int],
    total_scenes: int,
) -> list[float]:
    """Calculate the proportion of each act.

    Args:
        act_boundaries: Scene numbers where each act ends.
        total_scenes: Total number of scenes.

    Returns:
        List of proportions (0.0-1.0) for each act.
    """
    if not act_boundaries or total_scenes == 0:
        return []

    proportions = []
    prev_boundary = 0

    for boundary in act_boundaries:
        act_scenes = boundary - prev_boundary
        proportions.append(act_scenes / total_scenes)
        prev_boundary = boundary

    # Add final act if boundaries don't reach total
    if act_boundaries[-1] < total_scenes:
        remaining = total_scenes - act_boundaries[-1]
        proportions.append(remaining / total_scenes)

    return proportions


def get_ideal_proportions(structure_type: str) -> list[float]:
    """Get ideal act proportions for a given structure type.

    Args:
        structure_type: Structure type (Three-Act, Five-Act, etc.).

    Returns:
        List of ideal proportions for each act.
    """
    proportions = {
        "Three-Act": [0.25, 0.50, 0.25],
        "Five-Act": [0.10, 0.25, 0.30, 0.25, 0.10],
        "Hero's Journey": [0.25, 0.50, 0.25],  # Similar to three-act
        "Two-Act": [0.50, 0.50],
        "Four-Act": [0.25, 0.25, 0.25, 0.25],
    }
    return proportions.get(structure_type, [0.25, 0.50, 0.25])


def calculate_causal_binding_ratio(entries: list[BeatMapEntry]) -> float:
    """Calculate the BUT/THEREFORE vs AND THEN ratio.

    Higher ratios indicate stronger causal binding.
    Target is typically >80% causal (BUT/THEREFORE).

    Args:
        entries: List of beat map entries.

    Returns:
        Ratio from 0.0 to 1.0 (proportion of causal connectors).
    """
    from narratological.models.analysis import ConnectorType

    causal = sum(1 for e in entries if e.connector in (ConnectorType.BUT, ConnectorType.THEREFORE))
    episodic = sum(1 for e in entries if e.connector == ConnectorType.AND_THEN)
    total = causal + episodic

    if total == 0:
        return 0.0

    return causal / total


def classify_pacing(entries: list[BeatMapEntry]) -> str:
    """Classify the overall pacing based on tension patterns.

    Args:
        entries: List of beat map entries.

    Returns:
        Pacing classification string.
    """
    if not entries:
        return "Unknown"

    variance = calculate_tension_variance(entries)
    avg_tension = calculate_average_tension(entries)

    if variance is None or avg_tension is None:
        return "Unknown"

    # Classification based on tension metrics
    if variance < 1.0:
        if avg_tension > 7:
            return "Consistently High"
        elif avg_tension < 4:
            return "Consistently Low"
        else:
            return "Flat/Monotonous"
    elif variance < 3.0:
        return "Moderate Variation"
    elif variance < 6.0:
        return "Dynamic"
    else:
        return "Highly Variable"


def identify_tension_peaks(
    entries: list[BeatMapEntry],
    threshold: float = 8.0,
) -> list[int]:
    """Identify scene numbers with peak tension levels.

    Args:
        entries: List of beat map entries.
        threshold: Minimum tension level to consider a peak.

    Returns:
        List of scene numbers with peak tension.
    """
    return [entry.scene_number for entry in entries if entry.tension >= threshold]


def identify_tension_valleys(
    entries: list[BeatMapEntry],
    threshold: float = 3.0,
) -> list[int]:
    """Identify scene numbers with low tension (breathing room).

    Args:
        entries: List of beat map entries.
        threshold: Maximum tension level to consider a valley.

    Returns:
        List of scene numbers with low tension.
    """
    return [entry.scene_number for entry in entries if entry.tension <= threshold]


def group_characters_by_role(
    characters: list[Character],
) -> dict[str, list[str]]:
    """Group character names by their narrative role.

    Args:
        characters: List of character objects.

    Returns:
        Dictionary mapping role types to lists of character names.
    """
    groups: dict[str, list[str]] = {}

    for char in characters:
        role = char.role.lower()
        if role not in groups:
            groups[role] = []
        groups[role].append(char.name)

    return groups


def estimate_page_count(scenes: list[Scene]) -> int | None:
    """Estimate total page count from scene data.

    Args:
        scenes: List of scenes with page information.

    Returns:
        Estimated page count or None if insufficient data.
    """
    if not scenes:
        return None

    # Use last scene's end page if available
    for scene in reversed(scenes):
        if scene.page_end is not None:
            return scene.page_end

    # Fall back to counting scenes
    return None


def format_page_range(start: int | None, end: int | None) -> str:
    """Format a page range as a string.

    Args:
        start: Starting page number.
        end: Ending page number.

    Returns:
        Formatted string like "1-3" or "1" or "".
    """
    if start is None and end is None:
        return ""
    if start is None:
        return str(end)
    if end is None:
        return str(start)
    if start == end:
        return str(start)
    return f"{start}-{end}"
