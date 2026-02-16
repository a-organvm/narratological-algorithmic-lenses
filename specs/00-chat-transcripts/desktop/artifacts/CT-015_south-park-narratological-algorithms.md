---
source_thread: CT-015
source_message: 1
extracted_from: CT-015_south-parks-narratological-algorithms.md
---

# South Park Narratological Algorithms

A systematic distillation of the Parker/Stone "But/Therefore" framework into formal, implementable principles for narrative construction.

---

## 0. Meta-Principles (Axioms)

| Axiom | Formulation |
|-------|-------------|
| A0 | The technique is a **revision diagnostic**, not just a planning tool |
| A1 | Causal connection transforms *sequence of events* into *story* |
| A2 | Simplicity over complexity: "Just do one thing really right" |
| A3 | Imperfection is assumed; systematic revision is the solution |
| A4 | The technique enables both **generation** and **ruthless cutting** |

### Source Quotes

> "We found out this really simple rule... if the words 'and then' belong between those beats, you're fucked." —Trey Parker

> "The Rule of Replacing 'Ands' with Either 'Buts' or 'Therefores.'" —Trey Parker

---

## 1. Structural Hierarchy

```
STORY
  └── ACT (typically 3; value reversal at story level)
        └── BEAT (single story event)
              └── CONNECTOR (but | therefore | and_then)
```

### Definition Table

| Unit | Definition | Constraint |
|------|------------|------------|
| **Beat** | A single story event or plot point | Must connect causally to adjacent beats |
| **Connector** | The logical relationship between beats | Must be BUT or THEREFORE; never AND_THEN |
| **Causal Chain** | The complete sequence of causally-linked beats | Must be unidirectional; no reorderability |

---

## 2. The Three-Word Diagnostic

### 2.1 Connector Classification

```
┌─────────────┬────────────────────────────────┬──────────────┐
│ Connector   │ Function                       │ Strength     │
├─────────────┼────────────────────────────────┼──────────────┤
│ AND_THEN    │ Mere temporal succession       │ WEAK (fail)  │
│ BUT         │ Introduces obstacle/conflict   │ STRONG       │
│ THEREFORE   │ Shows consequence/causation    │ STRONG       │
└─────────────┴────────────────────────────────┴──────────────┘
```

### 2.2 Formal Mapping to Classical Theory

```
Parker/Stone          Aristotle (335 BCE)         Forster (1927)
─────────────────────────────────────────────────────────────────
"AND_THEN"      →     post hoc (episodic)    →   "story"
"BUT/THEREFORE" →     propter hoc (causal)   →   "plot"
```

### 2.3 Connector Decision Function

```python
def classify_connector(beat_a: Beat, beat_b: Beat) -> Connector:
    """
    Determine the logical relationship between two beats.
    """
    if beat_b.is_consequence_of(beat_a):
        return THEREFORE
    elif beat_b.is_complication_of(beat_a):
        return BUT
    else:
        return AND_THEN  # FAILURE STATE
```

---

## 3. The Testing Protocol

### 3.1 Six-Step Procedure

```
STEP 1: ENUMERATE
    List all beats on whiteboard/cards (one beat per unit)
    
STEP 2: CONNECT
    Between each adjacent pair, write: "and then" | "but" | "therefore"
    
STEP 3: FLAG
    Circle all "and then" connections → problem areas
    
STEP 4: REVISE
    For each flagged connection, ask:
      - What OBSTACLE could complicate this transition?
      - What CONSEQUENCE could this beat cause?
      - How can character CHOICE produce the next beat?
    
STEP 5: VERIFY_AGENCY
    Confirm protagonist CHOICES drive each transition
    (not external events happening TO character)
    
STEP 6: STATUS_QUO_CHECK
    Verify each beat changes something that PERSISTS
```

### 3.2 The Shuffle Test

```python
def shuffle_test(beats: List[Beat]) -> bool:
    """
    If beats can be reordered without breaking the story,
    the structure is episodic (failure).
    
    Returns True if structure passes (causal), False if fails (episodic).
    """
    for permutation in all_permutations(beats):
        if story_still_works(permutation):
            return False  # FAILURE: reorderable = episodic
    return True  # PASS: sequence is necessary
```

### 3.3 The Status Quo Test

```python
def status_quo_test(scene: Scene) -> bool:
    """
    If world state is identical before and after scene,
    scene is AND_THEN (excisable).
    """
    if scene.world_state_before == scene.world_state_after:
        return False  # FAILURE: no change = "and then"
    return True  # PASS: something persisted
```

---

## 4. Revision Questions (Diagnostic)

When a beat is flagged as AND_THEN, apply these five questions:

| # | Question | Purpose |
|---|----------|---------|
| 1 | Why does Scene B happen **BECAUSE** of Scene A? | Establish causation |
| 2 | What **PREVENTS** the character from achieving their goal easily? | Generate obstacle |
| 3 | How has the **CHARACTER** changed because of this scene? | Verify transformation |
| 4 | What **NEW PROBLEM** emerges from the resolution? | Ensure continuation |
| 5 | If I removed this scene, would anything downstream break? | Validate necessity |

---

## 5. Red Flags for AND_THEN Structure

```
FLAG: Character reacts to external events without making choices
FLAG: Events could be reordered without breaking story (shuffle test)
FLAG: Subplots never intersect with main plot
FLAG: "False alarm" resolutions that reset status quo
FLAG: Information dumps disconnected from character goals
FLAG: Scenes existing solely for world-building/setting
```

---

## 6. The Single A-Story Principle

### 6.1 Discovery (from "Scott Tenorman Must Die")

```
PRE-EPIPHANY:  A-story + B-story + C-story → diluted impact
POST-EPIPHANY: A-story only → concentrated causation
```

### 6.2 Implementation Rule

```python
def story_focus_rule(storylines: List[Storyline]) -> bool:
    """
    Constraint: One tight causal chain outperforms multiple weak chains.
    """
    if len([s for s in storylines if s.is_primary]) > 1:
        return False  # Multiple A-stories = structural weakness
    return True
```

### 6.3 Subplot Integration (when used)

If subplots exist, they must **causally interlink** with main plot:

```
VALID:   B-plot resolution CAUSES A-plot resolution
         (Randy delivers Sword of a Thousand Truths → boys defeat griefer)

INVALID: B-plot exists independently, never affects A-plot
```

---

## 7. Causal Chain Templates

### 7.1 Generic Chain Pattern

```
[INCITING INCIDENT]
    ↓ THEREFORE
[CHARACTER PURSUES GOAL]
    ↓ BUT
[OBSTACLE BLOCKS GOAL]
    ↓ THEREFORE
[CHARACTER ESCALATES]
    ↓ BUT
[ANTAGONIST COUNTERS]
    ↓ THEREFORE
[CHARACTER ADAPTS STRATEGY]
    ↓ BUT
[COMPLICATION EMERGES]
    ↓ THEREFORE
[RESOLUTION]
```

### 7.2 "Scott Tenorman Must Die" Chain (Canonical)

```
1. Cartman buys pubes from Scott ($10)
   ↓ BUT
2. Discovers you're supposed to grow your own (scammed)
   ↓ THEREFORE
3. Demands money back
   ↓ BUT
4. Scott refuses + public humiliation
   ↓ THEREFORE
5. Cartman escalates to revenge schemes
   ↓ BUT
6. Scott outsmarts at every turn
   ↓ THEREFORE
7. Cartman develops elaborate plan
   ↓ BUT
8. Stan and Kyle betray Cartman (warn Scott)
   ↓ THEREFORE
9. Cartman anticipates betrayal, plans accordingly
   ↓ THEREFORE
10. Multi-layered revenge unfolds at chili cook-off
```

---

## 8. Production Integration

### 8.1 The 6-Day Constraint Enablers

The BUT/THEREFORE framework enables extreme compression because:

| Feature | Effect |
|---------|--------|
| **Immediate diagnosis** | No debate needed; AND_THEN visible instantly |
| **No wasted scenes** | Every scene earns place through causation |
| **Built-in conflict engine** | BUT auto-generates obstacles; THEREFORE auto-generates consequences |
| **Single A-story focus** | One chain easier to execute under deadline |

### 8.2 Visual Process (Whiteboard Method)

```
┌─────────────────────────────────────────────────────────────┐
│                     ACT I    │   ACT II   │   ACT III      │
├─────────────────────────────────────────────────────────────┤
│ [Beat 1] THEREFORE [Beat 2] BUT [Beat 3] THEREFORE [Beat 4]│
│                                                             │
│ Any "AND_THEN" = immediately visible problem requiring fix  │
└─────────────────────────────────────────────────────────────┘
```

---

## 9. Writers' Room Axioms

### 9.1 The "No No" Rule

```
RULE: Never say "No, that won't work because..."
      
RATIONALE: BUT/THEREFORE provides structural discipline;
           ideas can flow freely because reliable filter exists
```

### 9.2 The Simplicity Principle

```
Stone: "Just do one thing really right"
Parker: "All you need is clarity"

IMPLEMENTATION: Complexity = structural weakness
                Clarity = structural strength
```

---

## 10. Scene Meaning Test (Film Crit Hulk Derivative)

For each scene, answer affirmatively or delete:

| # | Question |
|---|----------|
| 1 | What did the character **learn** by going into this scene? |
| 2 | Did they gain **new insight** into their problem? |
| 3 | How did this scene **push** the character further on their journey? |
| 4 | Does the outcome **push toward** the next scene goal? |

```python
def scene_meaning_test(scene: Scene) -> bool:
    """
    If scene doesn't change anything that persists,
    it's IN the story but not OF the story.
    """
    return (
        scene.character_learns_something() or
        scene.provides_new_insight() or
        scene.pushes_character_forward() or
        scene.outcome_causes_next_scene()
    )
```

---

## 11. Before/After Transformation Examples

### Example 1: Weather Event

**AND_THEN (fail):**
```
James goes out for a run, and then it rains, and then he goes 
swimming, and his ex-girlfriend is there, and then he goes home.
```

**BUT/THEREFORE (pass):**
```
James goes out for a run, BUT it starts raining; THEREFORE he 
goes swimming instead. BUT his ex-girlfriend is at the pool, 
THEREFORE he hurries home to avoid an awkward conversation.
```

### Example 2: Mall Trip

**AND_THEN (fail):**
```
Jimmy went to the mall, and then he realized he was tired, and 
then he got a coffee, and then he walked back to the parking 
lot, and then he drove home.
```

**BUT/THEREFORE (pass):**
```
Jimmy went to the mall, BUT realized he was exhausted the moment 
he stepped inside. THEREFORE he picked up coffee before shopping. 
BUT since he was tired, he'd parked in an illegal spot to shorten 
his walk. THEREFORE by the time he returned, his car had been towed.
```

---

## 12. Quick Reference Card

```
┌─────────────────────────────────────────────────────────────┐
│           SOUTH PARK BUT/THEREFORE DIAGNOSTIC              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  CONNECTOR EVALUATION:                                      │
│  □ "And then" between beats? → REWRITE                     │
│  □ "But" between beats? → PASS (complication)              │
│  □ "Therefore" between beats? → PASS (causation)           │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  STRUCTURAL TESTS:                                          │
│  □ Shuffle test: Can beats be reordered? → FAIL if yes     │
│  □ Status quo test: World unchanged? → FAIL if yes         │
│  □ Removal test: Story breaks if removed? → PASS if yes    │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  REVISION QUESTIONS:                                        │
│  1. Why does B happen BECAUSE of A?                        │
│  2. What PREVENTS easy goal achievement?                   │
│  3. How has CHARACTER changed?                             │
│  4. What NEW PROBLEM emerges?                              │
│  5. Would removal break downstream?                        │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  CORE AXIOMS:                                               │
│  • "And then" = you're fucked                              │
│  • "But/Therefore" = you have a story                      │
│  • Revision tool, not just planning tool                   │
│  • Single A-story > multiple diluted stories               │
│  • Simplicity + clarity = structural strength              │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  RED FLAGS:                                                  │
│  • Passive protagonist (events happen TO them)             │
│  • Reorderable scenes                                       │
│  • Disconnected subplots                                    │
│  • False-alarm resolutions                                  │
│  • Pure exposition scenes                                   │
│  • World-building without causation                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 13. Theoretical Lineage

```
Aristotle (335 BCE)    "Episodic plots are worst"
        ↓                propter hoc vs. post hoc
Forster (1927)         "King died, queen died" vs. "queen died OF GRIEF"
        ↓                story vs. plot
McKee (1997)           Progressive complications, causal gaps
        ↓                screenwriting pedagogy
Parker/Stone (2011)    BUT/THEREFORE three-word test
        ↓                operational simplicity
Olson (ABT Framework)  Scientific communication adaptation
Sanderson              Novel revision technique
```

---

**Document version**: 1.0  
**Source**: "The South Park But/Therefore Rule: A Complete Craft Analysis"  
**Distillation method**: Formalization into decision trees, pseudocode, and lookup tables