---
ct_id: CT-014
uuid: e1cd0d3b-e3ce-46df-8d35-1c2b31153a9f
title: "Narratological algorithms from layered obstacles"
created_at: 2026-01-22T21:41:50.765591Z
updated_at: 2026-01-22T21:47:50.098603Z
message_count: 4
tags: [ALGO, TELEVISION, SCENE_DESIGN, PWB]
source: claude-desktop-export
---

# Narratological algorithms from layered obstacles

**CT-014** | 4 messages | Source: Claude Desktop

---

## Human *(2026-01-22 21:41 UTC)*

distill all of the referenced-document's rules as narratological-algorithms;

reference: 
The Three Things Going On Technique: Phoebe Waller-Bridge and Scene Construction Through Layered Obstacles

---

## Assistant *(2026-01-22 21:43 UTC)*

Now I'll distill this document into a formal narratological-algorithms format, consistent with the other algorithm documents in your project.

---

```markdown
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

# TIMING PRINCIPLE:
#   Comedy → Drama transition should occur when "they least expect it"
#   The obstacles CREATE the comedy
#   The comedy ENABLES the drama
```

### Comedy-Drama Oscillation Pattern

```
OSCILLATION_SEQUENCE:
  
  COMPLICATION → LAUGH → COMPLICATION → LAUGH → EMOTIONAL_BEAT
       ↑                                              ↓
       └──────────────── RESET ──────────────────────┘
  
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
├── VOWS/COMMITMENTS (celibacy, marriage, promises)
├── PROFESSIONAL_ROLES (can't mix personal/professional)
├── IDENTITY_CONSTRAINTS (class, background, reputation)
├── PSYCHOLOGICAL_PATTERNS (defense mechanisms, trauma responses)
└── RELATIONSHIP_HISTORY (can't escape past with certain people)
```

---

## 8. Theoretical Correspondence Table

| Theorist | Terminology | Waller-Bridge Equivalent |
|----------|-------------|-------------------------|
| **McKee** | "The Gap" | Layer 4 (intention ≠ result) |
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
    Obstacle₁ → Obstacle₂ → Obstacle₃ → ...
    
  EXAMPLE: Raising Arizona convenience store
    rob store → civilians → police → dogs → location change → ...
  
  LABEL: "Fantastic realism" — ordinary people, extraordinary complications
```

### British Cringe Comedy (Fawlty Towers Pattern)

```
ESCALATION_ENGINE:
  
  METRICS:
    - Script length: 2× standard (135-140 pages vs 65)
    - Camera cuts: 2× standard (400 vs 200)
  
  TECHNIQUE:
    - Initial obstacle seems manageable
    - Each solution creates new obstacle
    - Trained behaviors prevent hearing warnings
    - Escalate until catastrophic convergence
  
  EXAMPLE: "The Germans"
    fire drill botched → triggers alarm → concussion → 
    actual fire starts → Manuel's warning dismissed
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
  Obstacle₁ → Obstacle₂ → Obstacle₃
  
  Each new obstacle adds to (but doesn't multiply) existing problems.
  Tension increases arithmetically.
```

### Exponential Escalation

```
EXPONENTIAL:
  Obstacle₁ × Obstacle₂ × Obstacle₃
  
  Obstacles interact and multiply each other's effects.
  Tension increases geometrically.
  
  EXAMPLE: Engagement dinner (Fleabag S2E1)
    Claire's miscarriage × waitress interruptions × 
    Martin drinking × Godmother brags × 
    Priest attraction × ignored for 45 minutes
    
  RESULT: "Editing becomes absurdly fast for a stationary scene"
```

### Convergent Escalation

```
CONVERGENT:
  Multiple separate obstacles → single crisis point
  
  TECHNIQUE: "Smoke break escape valves"
    When tension becomes unbearable, provide momentary relief
    before resuming escalation toward convergence.
```

---

## 11. Quick Reference Card

### Scene Construction Checklist

```
□ LAYER 1: What does character WANT in this scene?
□ LAYER 2: What PHYSICAL obstacles complicate pursuit?
□ LAYER 3: What INTERPERSONAL complications exist?
□ LAYER 4: Does scene end DIFFERENTLY than character expected?
□ VALIDATION: Can you count ≥3 DISTINCT SIMULTANEOUS obstacles?
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

```
1. "Is this just a conversation about [topic]?"
   → If yes, add obstacles
   
2. "Does character get what they expect?"
   → If yes, introduce gap
   
3. "Could this scene happen in neutral conditions?"
   → If yes, violate those conditions
   
4. "Am I TELLING character's nature or SHOWING through navigation?"
   → If telling, force obstacle navigation
```

### The Fundamental Test

> "Can you identify at least three distinct things the character is dealing with simultaneously?"
> 
> If NO → scene is dramatically inert
> If YES → scene has reality
```

---

## Appendix: Implementation Notes

### Interoperability with Other Frameworks

This technique integrates with:

- **McKee's Scene Analysis**: The four-layer protocol maps to McKee's beat/gap structure
- **South Park But/Therefore**: Obstacles generate the "but" connectors between beats
- **Larry David's Collision Architecture**: Multiple obstacles can represent parallel storylines converging

### Common Pitfalls

1. **Obstacles too similar**: Three variations of "time pressure" = 1 obstacle, not 3
2. **Sequential not simultaneous**: Problems occurring one-after-another ≠ layered obstacles
3. **Abstract not concrete**: "Emotional conflict" is weak; "hiding miscarriage while waitress won't stop interrupting" is strong
4. **Obstacles don't interact**: Best scenes have obstacles that multiply each other's difficulty
```

---

Shall I save this as a file to the outputs directory, or refine any specific section?

---

## Human *(2026-01-22 21:46 UTC)*

provide md

---

## Assistant *(2026-01-22 21:47 UTC)*

Document delivered. 

**Structure summary**:
- 11 sections mirroring the format of your existing narratological algorithm documents (McKee, Larry David, South Park)
- Core formula: `SCENE = INTENTION + ≥3 OBSTACLES`
- Four-layer protocol formalized as pseudocode
- Obstacle taxonomy with interaction matrix
- Genre-specific application patterns (Tarantino tension, Coen absurdism, Fawlty escalation, etc.)
- Theoretical correspondence table mapping PWB terminology to McKee/Sorkin/Mamet/Snyder
- Quick reference card for practical scene diagnosis

---
