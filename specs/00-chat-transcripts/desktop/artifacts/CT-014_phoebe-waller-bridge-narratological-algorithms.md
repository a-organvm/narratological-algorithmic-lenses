---
source_thread: CT-014
source_message: 1
extracted_from: CT-014_narratological-algorithms-from-layered-obstacles.md
---

# Phoebe Waller-Bridge Narratological Algorithms

A systematic distillation of the "Three Things Going On" technique into formal, implementable principles for scene construction through layered obstacles.

**Source**: "The Three Things Going On Technique: Phoebe Waller-Bridge and Scene Construction Through Layered Obstacles"

---

## Table of Contents

0. [Meta-Principles (Axioms)](#0-meta-principles-axioms)
1. [Core Formula](#1-core-formula)
2. [The Four-Layer Scene Construction Protocol](#2-the-four-layer-scene-construction-protocol)
3. [Obstacle Taxonomy](#3-obstacle-taxonomy)
4. [The Reality Generation Principle](#4-the-reality-generation-principle)
5. [The Disarm-Then-Punch Algorithm](#5-the-disarm-then-punch-algorithm)
6. [Scene Diagnostic Test](#6-scene-diagnostic-test)
7. [Character-Design-Level Obstacles](#7-character-design-level-obstacles)
8. [Theoretical Correspondence Table](#8-theoretical-correspondence-table)
9. [Genre-Specific Applications](#9-genre-specific-applications)
10. [Escalation Patterns](#10-escalation-patterns)
11. [Quick Reference Card](#12-quick-reference-card)

---

## 0. Meta-Principles (Axioms)

| Axiom | Formulation |
|-------|-------------|
| A0 | Scenes require obstacles to generate drama, reveal character, and propel narrative forward |
| A1 | "The more you put on a person, the more real it feels" |
| A2 | Obstacles force *showing* rather than *telling*—character is revealed through navigation, not declaration |
| A3 | Complications create comedy that opens viewers to emotional impact |
| A4 | The technique operates fractally: what works for story works for act, scene, and beat |
| A5 | Concrete/physical obstacles are preferable to abstract complications |

### Source Quotes

> "I always think there should be at least three things going on in one scene at the same time." —Phoebe Waller-Bridge (Deadline, 2019)

> "Otherwise it's just a conversation about a bank loan." —PWB

> "I try to disarm an audience as much as I can with comedy and then punch them in the gut with drama when they least expect it." —PWB

---

## 1. Core Formula

```
MINIMUM_SCENE_COMPLEXITY = 3

SCENE_VALIDITY_TEST:
  IF count(distinct_obstacles) < 3:
    scene = "DRAMATICALLY_INERT"
  ELSE:
    scene = "HAS_REALITY"
```

### The Fundamental Equation

```
SCENE = INTENTION + OBSTACLE₁ + OBSTACLE₂ + OBSTACLE₃ + ... + OBSTACLEₙ
        where n ≥ 3

DRAMA = f(INTENTION × OBSTACLES)
        Drama increases multiplicatively with obstacle count
```

---

## 2. The Four-Layer Scene Construction Protocol

```python
def construct_scene(character, context):
    """
    Waller-Bridge's formalized scene construction method.
    Each layer adds complexity; minimum 3 layers required.
    """
    
    # LAYER 1: Primary Intention
    intention = define_intention(
        what=character.concrete_want,  # Must be specific
        urgency=HIGH,                   # Must be pressing
        stakes=character.consequences_of_failure
    )
    
    # LAYER 2: Physical/Environmental Obstacles
    physical_obstacles = select_from([
        "hot_room",
        "eating_during_conversation",
        "malfunctioning_clothes",
        "being_drunk",
        "time_pressure",
        "physical_barriers",
        "intrusive_third_party",
        "bodily_discomfort",
        "arriving_late",
        "being_unprepared"
    ])
    
    # LAYER 3: Interpersonal Complications
    interpersonal = define_complications(
        who_else_present=other_characters,
        their_wants=conflicting_desires,
        hidden_secrets=beneath_surface,
        relationship_tensions=subtext
    )
    
    # LAYER 4: The Gap (Intention ≠ Result)
    gap = ensure_gap(
        expected_result=character.expectation,
        actual_result=different_from_expected,
        propulsion=leads_to_next_scene
    )
    
    # VALIDATION
    obstacle_count = count_distinct([
        physical_obstacles,
        interpersonal,
        gap_complications
    ])
    
    assert obstacle_count >= 3, "Scene is dramatically inert"
    
    return Scene(intention, obstacles, gap)
```

### Layer Definitions

| Layer | Question | Examples |
|-------|----------|----------|
| **1. Intention** | What does the character want/need in THIS scene? | Secure funding, survive dinner, confess feelings |
| **2. Physical** | What in space/body/circumstances makes it difficult? | Hot room, eating, drunk, late, wardrobe malfunction |
| **3. Interpersonal** | Who else is present? What do they want? What's hidden? | Conflicting agendas, secrets, relationship tensions |
| **4. Gap** | How does the scene end differently than expected? | Failure, complication, unexpected consequence |

---

## 3. Obstacle Taxonomy

```
OBSTACLE_TYPES:
├── PHYSICAL/ENVIRONMENTAL
│   ├── SPATIAL (hot room, cramped space, barriers)
│   ├── TEMPORAL (late, time pressure, deadline)
│   ├── BODILY (sweating, hunger, intoxication, injury)
│   ├── MATERIAL (malfunctioning objects, wardrobe issues)
│   └── INTRUSIVE (third parties, interruptions, noise)
│
├── INTERPERSONAL
│   ├── CONFLICTING_DESIRES (others want different things)
│   ├── HIDDEN_AGENDAS (secrets beneath surface)
│   ├── RELATIONSHIP_HISTORY (tensions, grudges, attraction)
│   ├── POWER_DYNAMICS (status differentials)
│   └── DEFENSE_MECHANISMS (deflection, humor as armor)
│
├── STRUCTURAL/RULE-BASED
│   ├── INSTITUTIONAL (can't break rules, protocol)
│   ├── IDENTITY (celibacy, professional role, social position)
│   └── GENRE_COLLISION (wrong tone for situation)
│
└── INFORMATION
    ├── KNOWLEDGE_GAPS (doesn't know crucial fact)
    ├── MISINTERPRETATION (reads situation wrong)
    └── EXPOSURE_RISK (others might discover truth)
```

### Obstacle Interaction Matrix

```
OBSTACLE_INTERACTION:
  Physical × Interpersonal = AMPLIFIED_AWKWARDNESS
  (sweating while trying to impress someone)
  
  Physical × Information = COMEDY_OF_ERRORS
  (arriving late AND unprepared AND being misread)
  
  Interpersonal × Structural = TRAGIC_CONSTRAINT
  (mutual attraction + celibacy vow)
```

---

## 4. The Reality Generation Principle

```
REALITY_ALGORITHM:
  
  INPUT:  Two characters discussing a topic
  OUTPUT: Scene that feels authentic
  
  METHOD:
    1. Identify what neutral conditions would look like
    2. Systematically violate neutral conditions
    3. Add complications that real humans experience:
       - hunger, lateness, interruption
       - hiding something, wanting something else
       - physical discomfort, social awkwardness
    4. Force characters to navigate complications WHILE pursuing goal
  
  PRINCIPLE:
    "Real conversations rarely happen in neutral conditions."
    
  RESULT:
    Navigation of obstacles = authentic human behavior under pressure
```

### Show-Don't-Tell Resolution

```
SHOW_DONT_TELL_THROUGH_OBSTACLES:
  
  INSTEAD OF: Character declares their nature
  USE:        Character navigates obstacles
  
  REVELATION_MECHANISM:
    HOW character handles obstacle → WHO character is
    
  EXAMPLES:
    - How Fleabag handles banker's suspicion → reveals self-sabotage
    - How Basil handles mounting disasters → reveals fragile ego
    - How character eats while talking → reveals anxiety/ease/status
```

---

## 5. The Disarm-Then-Punch Algorithm

```python
def disarm_then_punch(scene, emotional_payload):
    """
    PWB's technique for emotional impact through tonal oscillation.
    Comedy opens the door; drama walks through.
    """
    
    # Phase 1: DISARM
    complications = add_comic_obstacles(scene)
    audience_state = "guard_lowered"
    # Complications generate laughter/engagement
    # Audience not expecting emotional weight
    
    # Phase 2: PUNCH
    if audience_state == "guard_lowered":
        deliver_emotional_payload(scene, emotional_payload)
        # Drama lands harder because unexpected
    
    return scene
