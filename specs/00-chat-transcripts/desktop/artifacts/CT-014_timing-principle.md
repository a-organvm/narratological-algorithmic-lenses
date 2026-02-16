---
source_thread: CT-014
source_message: 1
extracted_from: CT-014_narratological-algorithms-from-layered-obstacles.md
---

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