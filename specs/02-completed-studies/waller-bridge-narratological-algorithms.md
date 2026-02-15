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
11. [Quick Reference Card](#11-quick-reference-card)

---

## 0. Meta-Principles (Axioms)



| Axiom | Formulation |

|-------|-------------|

| PWB-A0 | Scenes require obstacles to generate drama, reveal character, and propel narrative forward |

| PWB-A1 | "The more you put on a person, the more real it feels" |

| PWB-A2 | Obstacles force *showing* rather than *telling*

â€”character is revealed through navigation, not declaration |
| PWB-A3 | Complications create comedy that opens viewers to emotional impact |
| PWB-A4 | The technique operates fractally: what works for story works for act, scene, and beat |
| PWB-A5 | Concrete/physical obstacles are preferable to abstract complications |

### Source Quotes

> "I always think there should be at least three things going on in one scene at the same time." â€”Phoebe Waller-Bridge (Deadline, 2019)

> "Otherwise it's just a conversation about a bank loan." â€”PWB

> "I try to disarm an audience as much as I can with comedy and then punch them in the gut with drama when they least expect it." â€”PWB

---

## 1. The Three Things Rule (Core Formula)

The structural unit of the show is the **EPISODE**.

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
SCENE = INTENTION + OBSTACLEâ‚ + OBSTACLEâ‚‚ + OBSTACLEâ‚ƒ + ... + OBSTACLEâ‚™
        where n â‰¥ 3

DRAMA = f(INTENTION Ã— OBSTACLES)
        Drama increases multiplicatively with obstacle count
```

---

## 2. The Four-Layer Scene Construction Protocol

The atomic unit is the **SCENE**, constructed from multiple **LAYER** tracks.

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
    
    # LAYER 4: The Gap (Intention â‰  Result)
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
â”œâ”€â”€ PHYSICAL/ENVIRONMENTAL
â”‚   â”œâ”€â”€ SPATIAL (hot room, cramped space, barriers)
â”‚   â”œâ”€â”€ TEMPORAL (late, time pressure, deadline)
â”‚   â”œâ”€â”€ BODILY (sweating, hunger, intoxication, injury)
â”‚   â”œâ”€â”€ MATERIAL (malfunctioning objects, wardrobe issues)
â”‚   â””â”€â”€ INTRUSIVE (third parties, interruptions, noise)
â”‚
â”œâ”€â”€ INTERPERSONAL
â”‚   â”œâ”€â”€ CONFLICTING_DESIRES (others want different things)
â”‚   â”œâ”€â”€ HIDDEN_AGENDAS (secrets beneath surface)
â”‚   â”œâ”€â”€ RELATIONSHIP_HISTORY (tensions, grudges, attraction)
â”‚   â”œâ”€â”€ POWER_DYNAMICS (status differentials)
â”‚   â””â”€â”€ DEFENSE_MECHANISMS (deflection, humor as armor)
â”‚
â”œâ”€â”€ STRUCTURAL/RULE-BASED
â”‚   â”œâ”€â”€ INSTITUTIONAL (can't break rules, protocol)
â”‚   â”œâ”€â”€ IDENTITY (celibacy, professional role, social position)
â”‚   â””â”€â”€ GENRE_COLLISION (wrong tone for situation)
â”‚
â””â”€â”€ INFORMATION
    â”œâ”€â”€ KNOWLEDGE_GAPS (doesn't know crucial fact)
    â”œâ”€â”€ MISINTERPRETATION (reads situation wrong)
    â””â”€â”€ EXPOSURE_RISK (others might discover truth)
```

### Obstacle Interaction Matrix

```
OBSTACLE_INTERACTION:
  Physical Ã— Interpersonal = AMPLIFIED_AWKWARDNESS
  (sweating while trying to impress someone)
  
  Physical Ã— Information = COMEDY_OF_ERRORS
  (arriving late AND unprepared AND being misread)
  
  Interpersonal Ã— Structural = TRAGIC_CONSTRAINT
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
    HOW character handles obstacle â†’ WHO character is
    
  EXAMPLES:
    - How Fleabag handles banker's suspicion â†’ reveals self-sabotage
    - How Basil handles mounting disasters â†’ reveals fragile ego
    - How character eats while talking â†’ reveals anxiety/ease/status
```

---

## 5. The Disarm-Then-Punch Protocol

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

# TIMING PRINCIPLE:
#   Comedy â†’ Drama transition should occur when "they least expect it"
#   The obstacles CREATE the comedy
#   The comedy ENABLES the drama
```

### Comedy-Drama Oscillation Pattern

```
OSCILLATION_SEQUENCE:
  
  COMPLICATION â†’ LAUGH â†’ COMPLICATION â†’ LAUGH â†’ EMOTIONAL_BEAT
       â†‘                                              â†“
       â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ RESET â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
  
  Each cycle:
  - Deepens engagement
  - Lowers defenses
  - Prepares for impact
```

---

## 6. Scene Diagnostic Test

```python
def waller_bridge_test(scene):
    """
    The diagnostic: Can you identify at least three distinct things
    the character is dealing with simultaneously?
    """
    
    obstacles = extract_obstacles(scene)
    
    # Must be DISTINCT (not variations of same problem)
    distinct_obstacles = deduplicate(obstacles)
    
    # Must be SIMULTANEOUS (not sequential)
    simultaneous = verify_concurrency(distinct_obstacles)
    
    if len(simultaneous) < 3:
        return {
            "status": "FAIL",
            "diagnosis": "Scene is 'a conversation about a bank loan'",
            "prescription": "Add obstacles until count >= 3"
        }
    else:
        return {
            "status": "PASS",
            "obstacles": simultaneous,
            "reality_index": len(simultaneous) / 3  # >1.0 is richer
        }
```

### Red Flags

| Symptom | Diagnosis | Prescription |
|---------|-----------|--------------|
| Scene "about" one thing | No obstacle layering | Add 2+ concurrent complications |
| Characters achieve goal smoothly | No gap between intention/result | Introduce failure/unexpected outcome |
| Dialogue feels expository | Neutral conditions | Add physical/environmental pressure |
| Character seems flat | No obstacle navigation | Force character to reveal through action |
| Scene lacks tension | Single-track conflict | Layer interpersonal beneath physical |

---

## 7. Character-Design-Level Obstacles

```
STRUCTURAL_OBSTACLE_EMBEDDING:
  
  Obstacles can be embedded at CHARACTER DESIGN level,
  not just SCENE level.
  
  EXAMPLE: Hot Priest
    CHARACTER_TRAIT: celibate
    STRUCTURAL_OBSTACLE: cannot act on attraction
    EFFECT: "made the whole thing even more tense"
  
  TECHNIQUE:
    When designing character, ask:
    "What rule/constraint/identity makes their goals harder?"
    Build obstacle INTO the character.
```

### Character-Level Obstacle Types

```
CHARACTER_OBSTACLES:
â”œâ”€â”€ VOWS/COMMITMENTS (celibacy, marriage, promises)
â”œâ”€â”€ PROFESSIONAL_ROLES (can't mix personal/professional)
â”œâ”€â”€ IDENTITY_CONSTRAINTS (class, background, reputation)
â”œâ”€â”€ PSYCHOLOGICAL_PATTERNS (defense mechanisms, trauma responses)
â””â”€â”€ RELATIONSHIP_HISTORY (can't escape past with certain people)
```

---

## 8. Theoretical Correspondence Table

| Theorist | Terminology | Waller-Bridge Equivalent |
|----------|-------------|-------------------------|
| **McKee** | "The Gap" | Layer 4 (intention â‰  result) |
| **Sorkin** | "Temple of intention and obstacle" | Core formula |
| **Mamet** | "What prevents them" | Layers 2-3 |
| **Snyder** | "Pope in the Pool" | Physical/environmental obstacles |
| **Yorke** | "Fractal structure" | Technique at all levels |

### Unified Principle

```
UNIFIED_FORMULATION:
  
  McKee:    "Gap between expectation and result"
  Sorkin:   "Intention + formidable obstacle = friction"
  Mamet:    "Attempt to meet need WILL lead to failure"
  Snyder:   "Two things going on simultaneously"
  PWB:      "At least three things going on at once"
  
  SYNTHESIS:
    Drama = Character pursuing intention through
            multiple concurrent obstacles toward
            a result different from expectation
```

---

## 9. Genre-Specific Applications

### Tension/Thriller (Tarantino Pattern)

```
MUNDANE_OBSTACLE_TENSION:
  
  SETUP: Audience knows threat exists
  OBSTACLES: Mundane rituals that delay confrontation
    - hospitality (must drink milk)
    - politeness (must complete conversation)
    - social norms (can't break protocol)
  
  EFFECT: Unbearable tension through delay
  
  EXAMPLE: Inglourious Basterds opening
    INTENTION: Discover hidden Jews
    OBSTACLES: Drinking milk, discussing dairy, smoking pipe
    DURATION: 8 minutes of mundane obstacles
```

### Absurdist Comedy (Coen Brothers Pattern)

```
CASCADING_PHYSICAL_COMPLICATIONS:
  
  STRUCTURE: Each obstacle triggers next obstacle
  RATE: Exponential multiplication
  
  SEQUENCE:
    Obstacleâ‚ â†’ Obstacleâ‚‚ â†’ Obstacleâ‚ƒ â†’ ...
    
  EXAMPLE: Raising Arizona convenience store
    rob store â†’ civilians â†’ police â†’ dogs â†’ location change â†’ ...
  
  LABEL: "Fantastic realism" â€” ordinary people, extraordinary complications
```

### British Cringe Comedy (Fawlty Towers Pattern)

```
ESCALATION_ENGINE:
  
  METRICS:
    - Script length: 2Ã— standard (135-140 pages vs 65)
    - Camera cuts: 2Ã— standard (400 vs 200)
  
  TECHNIQUE:
    - Initial obstacle seems manageable
    - Each solution creates new obstacle
    - Trained behaviors prevent hearing warnings
    - Escalate until catastrophic convergence
  
  EXAMPLE: "The Germans"
    fire drill botched â†’ triggers alarm â†’ concussion â†’ 
    actual fire starts â†’ Manuel's warning dismissed
```

### Prestige Drama (Barry Pattern)

```
GENRE_COLLISION_AS_OBSTACLE:
  
  DUAL_WORLD_STRUCTURE:
    WORLD_A: hitman mode = "high stakes, no drama"
    WORLD_B: acting class = "high drama, no stakes"
  
  INVERSION:
    - Violence becomes slapstick
    - Acting class becomes life-or-death
  
  OBSTACLE = genre expectations themselves
```

### Surrealist (Atlanta Pattern)

```
SURREAL_INTRUSION_AS_OBSTACLE:
  
  TECHNIQUE: "Subvert at least one expectation per scene"
  
  FUNCTION:
    - Prevents scene from being "about what it's about"
    - Forces viewer to confront assumptions
    - Reality itself becomes unreliable obstacle
  
  EXAMPLES:
    - Invisible car that runs over people
    - Black Justin Bieber at basketball game
```

---

## 10. Escalation Patterns

### Linear Escalation

```
LINEAR:
  Obstacleâ‚ â†’ Obstacleâ‚‚ â†’ Obstacleâ‚ƒ
  
  Each new obstacle adds to (but doesn't multiply) existing problems.
  Tension increases arithmetically.
```

### Exponential Escalation

```
EXPONENTIAL:
  Obstacleâ‚ Ã— Obstacleâ‚‚ Ã— Obstacleâ‚ƒ
  
  Obstacles interact and multiply each other's effects.
  Tension increases geometrically.
  
  EXAMPLE: Engagement dinner (Fleabag S2E1)
    Claire's miscarriage Ã— waitress interruptions Ã— 
    Martin drinking Ã— Godmother brags Ã— 
    Priest attraction Ã— ignored for 45 minutes
    
  RESULT: "Editing becomes absurdly fast for a stationary scene"
```

### Convergent Escalation

```
CONVERGENT:
  Multiple separate obstacles â†’ single crisis point
  
  TECHNIQUE: "Smoke break escape valves"
    When tension becomes unbearable, provide momentary relief
    before resuming escalation toward convergence.
```

---

## 11. Quick Reference Card

### Scene Construction Checklist

```
â–¡ LAYER 1: What does character WANT in this scene?
â–¡ LAYER 2: What PHYSICAL obstacles complicate pursuit?
â–¡ LAYER 3: What INTERPERSONAL complications exist?
â–¡ LAYER 4: Does scene end DIFFERENTLY than character expected?
â–¡ VALIDATION: Can you count â‰¥3 DISTINCT SIMULTANEOUS obstacles?
```

### Obstacle Quick-Add Menu

```
PHYSICAL:          INTERPERSONAL:         STRUCTURAL:
- hot/cold room    - conflicting wants    - rules can't break
- eating           - hidden secrets       - role constraints
- late/rushed      - relationship tension - identity barriers
- drunk            - power dynamics       
- wardrobe issue   - defense mechanisms   
- interruptions    - attraction/repulsion
```

### Diagnostic Questions

1. **Are there at least three distinct things going on in this scene simultaneously?** (YES)
2. **Could this scene happen in neutral conditions?** (NO)
3. **Is the character revealed through how they navigate obstacles?** (YES)
4. **Does comedy disarm the audience before a dramatic punch?** (YES)
5. **Is the environment actively making the character's goal harder?** (YES)
6. **Do obstacles interact and multiply each other?** (YES)

### The Fundamental Test

> "Can you identify at least three distinct things the character is dealing with simultaneously?"
> 
> If NO â†’ scene is dramatically inert
> If YES â†’ scene has reality

---

## 12. Fourth Wall Breaking (Direct Address)

The camera is a character (the friend/confidant).

```python
def check_direct_address(character_state):
    """
    Establish intimacy and complicity.
    """
    if character.feels_misunderstood_by_world:
        turn_to_camera()
        share_private_judgment()
        establish_complicity()
```

## Appendix: Implementation Notes

### Interoperability with Other Frameworks

This technique integrates with:

- **McKee's Scene Analysis**: The four-layer protocol maps to McKee's beat/gap structure
- **South Park But/Therefore**: Obstacles generate the "but" connectors between beats
- **Larry David's Collision Architecture**: Multiple obstacles can represent parallel storylines converging

### Common Pitfalls

1. **Obstacles too similar**: Three variations of "time pressure" = 1 obstacle, not 3
2. **Sequential not simultaneous**: Problems occurring one-after-another â‰  layered obstacles
3. **Abstract not concrete**: "Emotional conflict" is weak; "hiding miscarriage while waitress won't stop interrupting" is strong
4. **Obstacles don't interact**: Best scenes have obstacles that multiply each other's difficulty
