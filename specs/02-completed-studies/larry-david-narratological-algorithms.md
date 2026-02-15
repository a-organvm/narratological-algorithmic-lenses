# Larry David's Narratological Algorithms

> Systematic distillation of Larry David's "comedy geometry" method into formal, implementable principles for narrative construction. Derived from *Comedy Geometry: Larry David's Architecture of Cascading Consequences*.

---

## Table of Contents

0. [Meta-Principles (Axioms)](#0-meta-principles-axioms)
1. [Structural Hierarchy](#1-structural-hierarchy)
2. [The Four-Phase Architecture](#2-the-four-phase-architecture)
3. [Retrofit Plotting Algorithm](#3-retrofit-plotting-algorithm)
4. [The Storyline Independence Test](#4-the-storyline-independence-test)
5. [Collision Design Rules](#5-collision-design-rules)
6. [The Amoral Karma Engine](#6-the-amoral-karma-engine)
7. [The Outline-Improv Hybrid (Curb Protocol)](#7-the-outline-improv-hybrid-curb-protocol)
8. [Structural Diagnostic Questions](#8-structural-diagnostic-questions)
9. [Plotline Type Classification](#9-plotline-type-classification)
10. [Episode Templates](#10-episode-templates)
11. [Feydeau Ancestry Rules](#11-feydeau-ancestry-rules)
12. [Quick Reference Card](#12-quick-reference-card)

---

## 0. Meta-Principles (Axioms)

| Axiom | Formulation |
|-------|-------------|
| LD-A0 | **"No hugging, no learning."** Characters never develop, mature, or learn from mistakes. |
| LD-A1 | Consequences arise from **causal chains**, not ethical judgments. The universe is amoral. |
| LD-A2 | **Comedy geometry** = the mathematical arrangement of story intersections where actions in one plot mechanically trigger disasters in another. |
| LD-A3 | Satisfaction comes from **pattern completion**, not justice. |
| LD-A4 | The collision should feel **inevitable in retrospect, surprising in the moment**. |

### Source Quotes

> "The morality in the world of Seinfeld and in Curb is sort of the polar opposite of [traditional sitcoms]. People behave the way they actually behave." â€”Alec Berg

> "We're not moralizing about the thing." â€”Jeff Schaffer

> "A Seinfeld episode and a Curb episode are all written the exact same way: Working out a structure on a dry erase board, figuring out what the scenes are and what the beats of the scene are, making this sort of comedy geometry out of all the stories." â€”Jeff Schaffer

---

## 1. Structural Hierarchy

```
EPISODE
  â””â”€â”€ STORYLINE (3-5 parallel, apparently independent)
        â””â”€â”€ SCENE (cross-cut at increasing pace)
              â””â”€â”€ BEAT (improvised dialogue, engineered architecture)
                    â””â”€â”€ BRIDGE ELEMENT (planted connector)
```

### Definition Table

| Unit | Definition | Constraint |
|------|------------|------------|
| **Storyline** | One character's independent pursuit of a goal | Must be funny *in isolation* AND *in intersection* |
| **Bridge Element** | The planted connector between lines (**BRIDGE_ELEMENT**) | Must seem insignificant when planted |
| **Collision Point** | Moment when storylines mechanically intersect | Must be causal, not coincidental at resolution |
| **Retrofit** | Reverse-engineering setups from a discovered collision | Standard practice; non-linear composition |

### Episode Statistics (Seinfeld)

- **18-28 scenes** per episode
- **4 storylines** (one per main character)
- Cross-cutting between storylines at increasing pace
- Convergence "never really happened the same way twice" (Peter Mehlman)

---

## 2. The Four-Phase Architecture

### Phase 1: Parallel Setup (Act I)

```
PARALLEL_SETUP:
â”œâ”€â”€ Establish 3-5 apparently independent storylines
â”œâ”€â”€ Each storyline has internal logic and stakes
â”œâ”€â”€ Plant small details (bridge elements) that seem insignificant
â”œâ”€â”€ Storylines represent different types:
â”‚     WHIM/RAMIFICATION   - impulsive decision â†’ problems
â”‚     PERSONAL_ANTAGONISM - conflict with character
â”‚     GOAL_ORIENTED       - pursuit of objective
â””â”€â”€ NO STORYLINE should obviously connect to another
```

### Phase 2: Hidden Architecture (Act II)

```
HIDDEN_ARCHITECTURE:
â”œâ”€â”€ Characters pursue individual goals
â”œâ”€â”€ Introduce bridge elements across storylines:
â”‚     SHARED_LOCATION     (restaurant, event, venue)
â”‚     TRANSFERRED_OBJECT  (golf ball, organizer, underwear)
â”‚     MUTUAL_ACQUAINTANCE (person known to multiple characters)
â”œâ”€â”€ Build each storyline's tension independently
â”œâ”€â”€ Apply RETROFIT PLOTTING (see Section 3)
â””â”€â”€ Cross-cut between storylines at INCREASING PACE
```

### Phase 3: Mechanical Collision (Act III)

```
MECHANICAL_COLLISION:
â”œâ”€â”€ Bring storylines together through UNINTENDED CONSEQUENCE
â”œâ”€â”€ Collision must be:
â”‚     PHYSICAL/CAUSAL    (not emotional/moral)
â”‚     MECHANICALLY_LINKED (A's action triggers B's consequence)
â”‚     SURPRISING_YET_INEVITABLE
â””â”€â”€ BIGGEST LAUGH should occur at moment of collision
```

### Phase 4: Amoral Resolution

```
AMORAL_RESOLUTION:
â”œâ”€â”€ Restore social equilibrium
â”œâ”€â”€ Characters DO NOT learn
â”œâ”€â”€ Consequences proportionate to mechanics, not morality
â”œâ”€â”€ Final moment COMPLETES PATTERN (not delivers judgment)
â””â”€â”€ Characters end exactly where they started emotionally/morally
```

---

## 3. Retrofit Plotting Algorithm

Larry David's reverse-engineering method: "It's great to know how the scene's going to end. Then you sprinkle in stuff beforehand."

```python
def retrofit_plot(episode):
    """
    Larry David's reverse-engineering method.
    The comedy geometry is reverse-engineered from collision points.
    """
    
    # Step 1: Discover or design collision point
    collision = discover_satisfying_collision(storylines)
    
    # Step 2: Determine required bridge elements
    bridges = identify_necessary_connections(collision)
    
    # Step 3: Plant bridges in early scenes
    for bridge in bridges:
        scene = find_organic_placement(bridge, act=1)
        plant_insignificantly(bridge, scene)
    
    # Step 4: Verify causality chain
    for storyline in episode.storylines:
        assert storyline.contributes_to(collision)
        assert not storyline.reveals_connection_prematurely()
    
    return episode
```

### The Marine Biologist Discovery

The most famous example of last-minute convergence discovery:

> "It's Tuesday. We don't have the golf ball goes into the blowhole of the whale. We don't have it. No, it was never in the script... I said to Larry, 'Hey, what if what puts the whale in distress is Kramer's golf ball?' He's hitting golf balls at the beach. George is walking on the beach with the girl. We haven't connected them. We saw no connection the night before." â€”Jerry Seinfeld

**Key Insight**: Connections are often discovered *after* storylines are drafted. The collision point is then retrofitted with necessary setups.

---

## 4. The Storyline Independence Test

```
FOR each storyline S in episode:
    
    TEST_1: INTERNAL_VALIDITY
    â”‚  Does S have its own logic, stakes, and arc?
    â”‚  IF NO â†’ Storyline is underdeveloped
    
    TEST_2: ISOLATION_COMEDY
    â”‚  Is S funny when viewed in complete isolation?
    â”‚  IF NO â†’ Strengthen independent comedy
    
    TEST_3: INTERSECTION_COMEDY  
    â”‚  Is S funny in how it intersects with others?
    â”‚  IF NO â†’ Redesign collision mechanics
    
    TEST_4: INVISIBILITY
    â”‚  Can audience predict how S connects to others?
    â”‚  IF YES â†’ Hide connections better
```

### Validation Checklist

- [ ] Each storyline has independent stakes
- [ ] Each storyline could sustain a short film alone
- [ ] Bridge elements appear insignificant when introduced
- [ ] No storyline telegraphs its connection to others
- [ ] Collision creates compound comedy (funnier together than apart)

---

## 5. Collision Design Rules

### Rule 1: Causal, Not Coincidental

One character's action must **mechanically trigger** another character's consequence.

| Valid | Invalid |
|-------|---------|
| Kramer hits golf balls â†’ ball lodges in whale â†’ George must extract it | Characters happen to meet at same location with no causal linkage |
| Edible underwear in pocket â†’ Orthodox daughter eats it after ski lift jump | Two storylines merely share a location |

### Rule 2: Physical, Not Emotional

Connection should be traceable through objects, locations, or physical causation.

> "The linkage should be physical/causal, not emotional/moral."

### Rule 3: Climactic Placement

> "The hardest thing in comedy is to have the biggest laugh at the end, and it's the most satisfying thing." â€”Jerry Seinfeld

The collision point should produce the episode's biggest laugh.

### Rule 4: Inversion Option

Storylines may converge in **shared failure** rather than resolution.

Example: "The Parking Garage" â€” all plots fail together when the car won't start.

---

## 6. The Amoral Karma Engine

### Traditional Sitcom Model

```
bad_behavior  â†’ moral_punishment
good_behavior â†’ moral_reward
```

### Larry David Model

```
action â†’ causal_chain â†’ mechanical_consequence
```

### The Distinction

| Event | Traditional Interpretation | David's Actual Mechanism |
|-------|---------------------------|-------------------------|
| George extracts golf ball from whale | He deserves redemption | Kramer happened to hit Titleists into the ocean |
| Elaine loses her job | She's a bad person | She bought Jujyfruits at the wrong moment |
| Jerry's relationship fails | Cosmic punishment | JFK Jr. was coming to see Elaine at that exact moment |

### Implementation

```python
# WRONG (moralistic)
consequence = judge_moral_worth(character)

# CORRECT (mechanical)
consequence = trace_causal_chain(action)
```

### Berg's Formulation

> "People behave the way they actually behave. They do something bad, and when they get caught they lie about it, and they try to cover it up by doing something else that's worse. And eventually they get discovered, and instead of apologizing, they get f***ed for it."

---

## 7. The Outline-Improv Hybrid (Curb Protocol)

When Larry David created *Curb Your Enthusiasm*, he eliminated scripted dialogue while **intensifying structural precision**.

### Composition Method

```
FIXED (pre-written):
â”œâ”€â”€ 5-7 page outline
â”œâ”€â”€ Story beats
â”œâ”€â”€ Character motivations  
â”œâ”€â”€ ALL major plot convergences
â””â”€â”€ Collision points

FLUID (improvised):
â”œâ”€â”€ Dialogue
â”œâ”€â”€ Additional discovered connections
â””â”€â”€ Authentic character voice
```

### The Steering Constraint

> "Larry is a genius improvisor... he has the story beats of the outline in his head. He can steer the improv back to the essential story beats, while he's improvising." â€”Steve Rasch (Editor)

### Output

Comedy that feels spontaneous but is architecturally precise.

> "I have a comedy brain and I have no idea how he got there. It's transcendent... Nobody else could imitate his story style. It's like Mozart." â€”Susie Essman

---

## 8. Structural Diagnostic Questions

Before finalizing any episode, apply these questions:

1. **What object, location, or person connects multiple storylines without characters knowing?** (Bridge elements)
2. **Does an action in Storyline A mechanically affect Storyline B's outcome?** (Causal linkage)
3. **Is each storyline funny in complete isolation?** (Dual comedy test)
4. **Does the resolution feel like cause-and-effect rather than moral judgment?** (Amoral karma check)
5. **Do characters end exactly where they started, without learning a lesson?** (Static character state)
6. **Is the biggest laugh positioned at the moment of collision?** (Climactic placement)

---

## 9. Plotline Type Classification

### Type 1: Whim/Ramification

Impulsive decision creates escalating problems.

**Example**: Larry discovers Palestinian restaurant with incredible chicken.

### Type 2: Personal Antagonism

Conflict with recurring or new character.

**Example**: Marty Funkhouser's return to Orthodox Judaism.

### Type 3: Goal-Oriented

Character pursues specific objective.

**Example**: Richard Lewis needs kidney transplant.

### Distribution Constraint

Each episode should include **multiple types** distributed across storylines to create variety in conflict texture.

---

## 10. Episode Templates

### Template A: Convergent (Standard)

```
Setup:    4 independent storylines, 4 characters
Middle:   Cross-cutting, escalating tension per line
Climax:   Single moment where all collide
Example:  "The Marine Biologist"
```

**The Marine Biologist Structure**:
- A-plot: George pretends to be marine biologist
- B-plot: Elaine escorts temperamental Russian author
- C-plot: Kramer hits 600 golf balls into ocean
- D-plot: Jerry's dying t-shirt "Golden Boy"
- Collision: George extracts Kramer's golf ball from beached whale

### Template B: Shared Failure

```
Setup:    Characters in shared constrained space
Middle:   Each has independent deadline/need
Climax:   ALL fail together
Example:  "The Parking Garage"
```

**The Parking Garage Structure**:
- All four characters lost in New Jersey mall parking garage
- George: must reach parents by 6:15
- Elaine: goldfish will die without water
- Jerry: desperately needs to urinate
- Kramer: carrying heavy air conditioner
- Resolution: Car won't start. All plots fail together.

### Template C: Thematic Convergence

```
Setup:    Single thematic challenge, multiple responses
Middle:   Each character faces tailored temptation
Climax:   Social faux pas collapses multiple lines
Example:  "The Contest"
```

**The Contest Structure**:
- Shared challenge: who can go longest without masturbating
- Each faces tailored temptation (hospital patient, naked neighbor, JFK Jr.)
- Collision: Jerry's girlfriend storms out, directly into JFK Jr.
- Two romantic storylines collapse through one social faux pas

### Template D: Hourglass (Inverse Fortunes)

```
Setup:    Character A declining, Character B ascending
Middle:   Fortunes systematically invert
Climax:   Complete reversal through mechanical causes
Example:  "The Opposite"
```

**The Opposite Structure**:
- George does opposite of every instinct â†’ succeeds spectacularly
- Elaine's winning streak collapses (Jujyfruits incident)
- Jerry notes his life "evens out"
- End: George has dream job/apartment/girlfriend; Elaine unemployed/homeless/single
- Mechanism: Pure mechanical rebalancing, not moral judgment

---

## 11. Feydeau Ancestry Rules

Larry David's method inherits structural DNA from **Georges Feydeau** (1862-1921), master of French farce.

> "Mathematical perfection and flawless economy of plot... a rigorously, logically constructed machine where every word and motion matters." â€”Michael Billington on Feydeau

### Structural Parallels

| Feydeau Principle | David Adaptation |
|-------------------|------------------|
| "Meeting of characters particularly desirous of avoiding each other" | Collision of storylines through unintended encounter |
| Act I: establish need for secrecy | Phase 1: establish independent stakes |
| Act II: chaos in public space (often a hotel) | Phase 3: collision in shared location |
| Act III: restore status quo | Phase 4: equilibrium without learning |
| "Masterpieces of improbable contrivance" | Comedy geometry of cascading consequences |
| Mathematical perfection of plot | Weeks of outlining for 22-minute episode |

### The Operational Aesthetic

Academic Jason Mittell identifies the viewer pleasure in David's work as the **"operational aesthetic"**: enjoyment of watching narrative machinery work.

> "Interwoven plotting that results in unlikely coincidences and ironic repercussionsâ€”a distinct narrational mode."

---

## 12. Quick Reference Card

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚                    LARRY DAVID ALGORITHM                    â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚                                                             â”‚
â”‚  COMPOSITION SEQUENCE:                                      â”‚
â”‚  1. Design 3-5 independent storylines                       â”‚
â”‚  2. Plant bridge elements (objects, locations, people)      â”‚
â”‚  3. Discover/design collision point                         â”‚
â”‚  4. Retrofit: plant necessary setups in Act I               â”‚
â”‚  5. Cross-cut with increasing pace                          â”‚
â”‚  6. Collide through MECHANICAL cause, not moral judgment    â”‚
â”‚  7. Resolve without learning                                â”‚
â”‚  8. Biggest laugh at collision moment                       â”‚
â”‚                                                             â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚                                                             â”‚
â”‚  VALIDATION TESTS:                                          â”‚
â”‚  â–¡ Each storyline funny in isolation?                       â”‚
â”‚  â–¡ Each storyline funny in intersection?                    â”‚
â”‚  â–¡ Collision causal, not coincidental?                      â”‚
â”‚  â–¡ Resolution amoral, not moralistic?                       â”‚
â”‚  â–¡ Characters unchanged at end?                             â”‚
â”‚                                                             â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚                                                             â”‚
â”‚  CORE AXIOMS:                                               â”‚
â”‚  â€¢ "No hugging, no learning"                                â”‚
â”‚  â€¢ Consequences from causal chains, not ethics              â”‚
â”‚  â€¢ Pattern completion, not justice                          â”‚
â”‚  â€¢ Inevitable in retrospect, surprising in moment           â”‚
â”‚                                                             â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚                                                             â”‚
â”‚  BRIDGE ELEMENT TYPES:                                      â”‚
â”‚  â€¢ Shared location                                          â”‚
â”‚  â€¢ Transferred object                                       â”‚
â”‚  â€¢ Mutual acquaintance                                      â”‚
â”‚                                                             â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚                                                             â”‚
â”‚  PLOTLINE TYPES:                                            â”‚
â”‚  â€¢ Whim/Ramification (impulse â†’ problems)                   â”‚
â”‚  â€¢ Personal Antagonism (character conflict)                 â”‚
â”‚  â€¢ Goal-Oriented (pursuit of objective)                     â”‚
â”‚                                                             â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

---

## Appendix: Key Episodes as Case Studies

### "The Marine Biologist" â€” Perfect Convergence

| Storyline | Type | Bridge Element |
|-----------|------|----------------|
| George pretends to be marine biologist | Whim/Ramification | Beach location |
| Elaine escorts Russian author | Personal Antagonism | Thrown organizer |
| Kramer hits golf balls into ocean | Goal-Oriented | Titleist golf balls |
| Jerry's dying t-shirt | Whim/Ramification | None (parallel) |

**Collision**: Golf ball in whale's blowhole discovered by fake marine biologist.

### "Palestinian Chicken" â€” Mature Technique

| Storyline | Type | Bridge Element |
|-----------|------|----------------|
| Larry discovers Palestinian restaurant | Whim/Ramification | Restaurant location |
| "Social assassin" truth-telling | Personal Antagonism | Social situations |
| Funkhouser's Orthodox return | Goal-Oriented | Jewish community |
| Affair between friends | Personal Antagonism | Susie's house |
| Susie's drinking sounds | Whim/Ramification | Shared meals |

**Collision**: Dueling protestsâ€”pro-deli Jews vs. pro-Palestinian chicken supportersâ€”with Larry torn between both sides and his Palestinian love interest.

### "The Ski Lift" â€” Object Transfer Chain

| Storyline | Type | Bridge Element |
|-----------|------|----------------|
| Richard Lewis needs kidney | Goal-Oriented | Kidney consortium head |
| Orthodox consortium head | Personal Antagonism | Orthodox rules |
| Susie pretends to be Larry's Orthodox wife | Whim/Ramification | Orthodox identity |
| Edible underwear in Larry's pocket | Whim/Ramification | Physical object |

**Collision**: Orthodox daughter jumps off ski lift (can't be alone with strange man after dark), finds and eats edible underwear while waiting.

---

## References

- Berg, Alec. Writer interviews on Seinfeld and Curb Your Enthusiasm.
- Mehlman, Peter. Writer of "The Yada Yada," "The Hamptons," and 20+ Seinfeld episodes.
- Mittell, Jason. *Complex TV: The Poetics of Contemporary Television Storytelling*.
- Pierson, David P. "Comedy of Manners" analysis of Seinfeld.
- Ralkowski, Mark. Philosophical analysis of David's work.
- Schaffer, Jeff. Executive Producer, Curb Your Enthusiasm.
- Seinfeld, Jerry. Various interviews on the writing process.

---

*Document version: 1.0*
*Derived from: "Comedy Geometry: Larry David's Architecture of Cascading Consequences"*
