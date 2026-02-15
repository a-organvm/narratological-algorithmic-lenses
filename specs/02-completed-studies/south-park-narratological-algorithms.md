# South Park Narratological Algorithms

A systematic distillation of the **Trey Parker & Matt Stone** "But/Therefore" framework into formal, implementable principles for narrative construction.

**Source**: "The South Park But/Therefore Rule: A Complete Craft Analysis"

---

## Table of Contents

0. [Meta-Principles (Axioms)](#0-meta-principles-axioms)
1. [Structural Hierarchy](#1-structural-hierarchy)
2. [The Three-Word Diagnostic](#2-the-three-word-diagnostic)
3. [The Testing Protocol](#3-the-testing-protocol)
4. [Revision Questions](#4-revision-questions-diagnostic)
5. [Red Flags for AND_THEN Structure](#5-red-flags-for-and_then-structure)
6. [The Single A-Story Principle](#6-the-single-a-story-principle)
7. [Causal Chain Templates](#7-causal-chain-templates)
8. [Production Integration](#8-production-integration)
9. [Writers' Room Axioms](#9-writers-room-axioms)
10. [Scene Meaning Test](#10-scene-meaning-test)
11. [Before/After Transformation Examples](#11-beforeafter-transformation-examples)
12. [Quick Reference Card](#12-quick-reference-card)
13. [Theoretical Lineage](#13-theoretical-lineage)

---

## 0. Meta-Principles (Axioms)

| Axiom | Formulation |
|-------|-------------|
| SP-A0 | The technique is a **revision diagnostic**, not just a planning tool |
| SP-A1 | Causal connection transforms *sequence of events* into *story* |
| SP-A2 | Simplicity over complexity: "Just do one thing really right" |
| SP-A3 | Imperfection is assumed; systematic revision is the solution |
| SP-A4 | The technique enables both **generation** and **ruthless cutting** |

### Source Quotes

> "We found out this really simple rule... if the words 'and then' belong between those beats, you're fucked." â€”Trey Parker

> "The Rule of Replacing 'Ands' with Either 'Buts' or 'Therefores.'" â€”Trey Parker

> "That's not a movie. That's not a story... 'but,' 'because,' 'therefore' that gives you the causation between each beat, and that's a story." â€”Matt Stone

---

## 1. Structural Hierarchy

```
STORY
  â””â”€â”€ ACT (typically 3; value reversal at story level)
        â””â”€â”€ BEAT (single story event)
              â””â”€â”€ CONNECTOR (but | therefore | and_then)
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

| Connector | Function | Strength |
|-----------|----------|----------|
| **AND_THEN** | Mere temporal succession | WEAK (fail) |
| **BUT** | Introduces obstacle/conflict | STRONG |
| **THEREFORE** | Shows consequence/causation | STRONG |

### 2.2 Formal Mapping to Classical Theory

| Parker/Stone | Aristotle (335 BCE) | Forster (1927) |
|--------------|---------------------|----------------|
| "AND_THEN" | post hoc (episodic) | "story" |
| "BUT/THEREFORE" | propter hoc (causal) | "plot" |

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
    Circle all "and then" connections â†’ problem areas
    
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

- **Passive protagonist**: Character reacts to external events without making choices
- **Reorderable events**: Events could be shuffled without breaking story
- **Disconnected subplots**: Subplots never intersect with main plot
- **False alarms**: Resolutions that reset status quo
- **Exposition dumps**: Information disconnected from character goals
- **Pure world-building**: Scenes existing solely for setting establishment

---

## 6. The Single A-Story Principle

### 6.1 Discovery (from "Scott Tenorman Must Die")

```
PRE-EPIPHANY:  A-story + B-story + C-story â†’ diluted impact
POST-EPIPHANY: A-story only â†’ concentrated causation
```

> "It was the first time that we're like, 'wow, there's really not a C story in this.' We've just got this one A story of Cartman versus this guy. And it turned out so good that we really, from then on, started saying, 'let's forget B stories, let's forget C stories, let's just do a really well told A story.'" â€”Trey Parker

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
         (Randy delivers Sword of a Thousand Truths â†’ boys defeat griefer)

INVALID: B-plot exists independently, never affects A-plot
```

---

## 7. Causal Chain Templates

### 7.1 Generic Chain Pattern

```
[INCITING INCIDENT]
    â†“ THEREFORE
[CHARACTER PURSUES GOAL]
    â†“ BUT
[OBSTACLE BLOCKS GOAL]
    â†“ THEREFORE
[CHARACTER ESCALATES]
    â†“ BUT
[ANTAGONIST COUNTERS]
    â†“ THEREFORE
[CHARACTER ADAPTS STRATEGY]
    â†“ BUT
[COMPLICATION EMERGES]
    â†“ THEREFORE
[RESOLUTION]
```

### 7.2 "Scott Tenorman Must Die" Chain (Canonical)

```
1. Cartman buys pubes from Scott ($10)
   â†“ BUT
2. Discovers you're supposed to grow your own (scammed)
   â†“ THEREFORE
3. Demands money back
   â†“ BUT
4. Scott refuses + public humiliation
   â†“ THEREFORE
5. Cartman escalates to revenge schemes
   â†“ BUT
6. Scott outsmarts at every turn
   â†“ THEREFORE
7. Cartman develops elaborate plan
   â†“ BUT
8. Stan and Kyle betray Cartman (warn Scott)
   â†“ THEREFORE
9. Cartman anticipates betrayal, plans accordingly
   â†“ THEREFORE
10. Multi-layered revenge unfolds at chili cook-off
```

### 7.3 "Make Love Not Warcraft" Chain (with Causal Subplot)

**Main Plot:**
```
1. Boys play World of Warcraft
   â†“ BUT
2. Griefer kills them repeatedly
   â†“ THEREFORE
3. Gather all friends to fight back
   â†“ BUT
4. Griefer defeats them all
   â†“ THEREFORE
5. Cartman convinces them to train obsessively
   â†“ THEREFORE
6. Level up over weeks
   â†“ THEREFORE
7. Confront griefer again
   â†“ BUT
8. Still too powerful
```

**Randy Subplot (causally interlinked):**
```
- Stan dismisses Randy's gaming ability
  â†“ THEREFORE
- Randy creates character to prove him wrong
  â†“ BUT
- Randy dies immediately to griefer
  â†“ THEREFORE
- Randy quits
  â†“ BUT
- Blizzard needs someone to deliver legendary weapon; only Randy available
  â†“ THEREFORE
- Randy re-enters game
  â†“ THEREFORE
- Randy delivers Sword of a Thousand Truths to Stan
  â†“ THEREFORE
- Boys defeat griefer
```

**Key**: Subplot doesn't exist independentlyâ€”it directly causes main plot resolution.

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
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚                     ACT I    â”‚   ACT II   â”‚   ACT III      â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚ [Beat 1] THEREFORE [Beat 2] BUT [Beat 3] THEREFORE [Beat 4]â”‚
â”‚                                                             â”‚
â”‚ Any "AND_THEN" = immediately visible problem requiring fix  â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

> "Literally we'll sometimes write it out to make sure we're doing it. We'll have our beats, and we'll say, 'okay this happens, but then this happens' and that affects this and that does to that." â€”Trey Parker

---

## 9. Writers' Room Axioms

### 9.1 The "No No" Rule

```
RULE: Never say "No, that won't work because..."
      
RATIONALE: BUT/THEREFORE provides structural discipline;
           ideas can flow freely because reliable filter exists
```

> "In our writers room, you never say 'no.' You almost never go, 'No, that won't work because of this.' You don't need that energy." â€”Parker/Stone

### 9.2 The Simplicity Principle

```
Stone: "Just do one thing really right"
Parker: "All you need is clarity"

IMPLEMENTATION: Complexity = structural weakness
                Clarity = structural strength
```

### 9.3 The Anxiety Acknowledgment

> "Having that blank page in front of us is still the most terrifying thing in the world." â€”Trey Parker

> "It's so cool to talk to you guys and pretend like we know what we're doing." â€”Matt Stone

**Implication**: The technique doesn't eliminate difficultyâ€”it makes difficulty manageable through systematic process.

---

## 10. Scene Meaning Test

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

**Analysis**: Second version has conflict, consequence, and escalation. Same basic eventsâ€”completely different energy.

---

## 12. Quick Reference Card

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚           SOUTH PARK BUT/THEREFORE DIAGNOSTIC              â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚                                                             â”‚
â”‚  CONNECTOR EVALUATION:                                      â”‚
â”‚  â–¡ "And then" between beats? â†’ REWRITE                     â”‚
â”‚  â–¡ "But" between beats? â†’ PASS (complication)              â”‚
â”‚  â–¡ "Therefore" between beats? â†’ PASS (causation)           â”‚
â”‚                                                             â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚                                                             â”‚
â”‚  STRUCTURAL TESTS:                                          â”‚
â”‚  â–¡ Shuffle test: Can beats be reordered? â†’ FAIL if yes     â”‚
â”‚  â–¡ Status quo test: World unchanged? â†’ FAIL if yes         â”‚
â”‚  â–¡ Removal test: Story breaks if removed? â†’ PASS if yes    â”‚
â”‚                                                             â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚                                                             â”‚
â”‚  REVISION QUESTIONS:                                        â”‚
â”‚  1. Why does B happen BECAUSE of A?                        â”‚
â”‚  2. What PREVENTS easy goal achievement?                   â”‚
â”‚  3. How has CHARACTER changed?                             â”‚
â”‚  4. What NEW PROBLEM emerges?                              â”‚
â”‚  5. Would removal break downstream?                        â”‚
â”‚                                                             â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚                                                             â”‚
â”‚  CORE AXIOMS:                                               â”‚
â”‚  â€¢ "And then" = you're fucked                              â”‚
â”‚  â€¢ "But/Therefore" = you have a story                      â”‚
â”‚  â€¢ Revision tool, not just planning tool                   â”‚
â”‚  â€¢ Single A-story > multiple diluted stories               â”‚
â”‚  â€¢ Simplicity + clarity = structural strength              â”‚
â”‚                                                             â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚                                                             â”‚
â”‚  RED FLAGS:                                                 â”‚
â”‚  â€¢ Passive protagonist (events happen TO them)             â”‚
â”‚  â€¢ Reorderable scenes                                      â”‚
â”‚  â€¢ Disconnected subplots                                   â”‚
â”‚  â€¢ False-alarm resolutions                                 â”‚
â”‚  â€¢ Pure exposition scenes                                  â”‚
â”‚  â€¢ World-building without causation                        â”‚
â”‚                                                             â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

---

## 13. Theoretical Lineage

```
Aristotle (335 BCE)    "Episodic plots are worst"
        â†“                propter hoc vs. post hoc
Forster (1927)         "King died, queen died" vs. "queen died OF GRIEF"
        â†“                story vs. plot
McKee (1997)           Progressive complications, causal gaps
        â†“                screenwriting pedagogy
Parker/Stone (2011)    BUT/THEREFORE three-word test
        â†“                operational simplicity
Olson (ABT Framework)  Scientific communication adaptation
Sanderson              Novel revision technique
```

### Cross-Framework Equivalences

| Framework | "Weak" Structure | "Strong" Structure |
|-----------|------------------|-------------------|
| Parker/Stone | "And then" | "But" / "Therefore" |
| Aristotle | post hoc (episodic) | propter hoc (causal) |
| Forster | story | plot |
| Pixar Story Spine | â€” | "Because of that" |
| McKee | Episodic | Progressive complications |

---

## 14. Adoption Beyond South Park

The framework has been adapted across multiple domains:

**Brandon Sanderson** (fantasy novelist):
> "I hunt for the word 'and' when I rewrite, especially at big moments of my story. Then I figure out how to make it the word 'but' instead."

**Randy Olson** (marine biologist): Adapted into the ABT Framework for scientific communicationâ€”teaching researchers to structure grant proposals around And-But-Therefore.

**Film Crit Hulk** (screenwriter/critic): Dedicates attention to "The Law of Cause and Effect" in *Screenwriting 101*, calling it "the linking of your chain."

**David Perell** (writer/educator): Popularized the whiteboard testing method through his newsletter.

## 15. Diagnostic Questions

1. **Does Scene B happen BECAUSE of Scene A?** (Establish causation)
2. **What PREVENTS the character from achieving their goal easily?** (Generate obstacle)
3. **Has the character changed because of this scene?** (Verify transformation)
4. **What NEW PROBLEM emerges from the resolution?** (Ensure continuation)
5. **If I removed this scene, would anything downstream break?** (Validate necessity)
6. **Are subplots interlinked with the main plot through causation?** (Verify integration)

---

## 16. Why It Works

The technique succeeds because it **externalizes an internal cognitive process**:

1. Audiences naturally ask "why?" and "what happens next?"
2. BUT/THEREFORE structure ensures every scene answers both questions
3. "And then" structure forces audiences to supply their own causation
4. When they can't supply causation, they check out

> "They translated **2,400 years** of narrative theoryâ€”from Aristotle's condemnation of episodic plots through Forster's causation distinction through McKee's progressive complicationsâ€”into a three-word test any writer can apply while staring at a whiteboard at 3 AM."

---

**Document version**: 1.0  
**Distillation method**: Formalization into decision trees, pseudocode, and lookup tables  
**Related documents**: `mckee_narratological_algorithms.md`, `larry_david_narratological_algorithms.md`
