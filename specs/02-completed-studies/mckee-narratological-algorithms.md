# McKee's "Story" â€” Complete Narratological Algorithms

> Comprehensive extraction of all principles, rules, and procedures from Robert McKee's *Story: Substance, Structure, Style, and the Principles of Screenwriting* (1997), organized as implementable algorithms, decision tables, and pseudocode.

---

## Table of Contents

0. [Meta-Principles (Axioms)](#0-meta-principles-axioms)
1. [Structural Hierarchy](#1-structural-hierarchy)
2. [The Story Triangle (Design Space)](#2-the-story-triangle-design-space)
3. [Structure and Setting](#3-structure-and-setting)
4. [Structure and Genre](#4-structure-and-genre)
5. [Structure and Character](#5-structure-and-character)
6. [Structure and Meaning](#6-structure-and-meaning)
7. [The Substance of Story](#7-the-substance-of-story)
8. [The Gap Algorithm](#8-the-gap-algorithm)
9. [Value Charge System](#9-value-charge-system)
10. [Conflict Architecture](#10-conflict-architecture)
11. [The Inciting Incident Protocol](#11-the-inciting-incident-protocol)
12. [Act Design Formulas](#12-act-design-formulas)
13. [Scene Design Algorithm](#13-scene-design-algorithm)
14. [Scene Analysis Technique](#14-scene-analysis-technique)
15. [Composition Principles](#15-composition-principles)
16. [Crisis, Climax, Resolution](#16-crisis-climax-resolution)
17. [The Principle of Antagonism](#17-the-principle-of-antagonism)
18. [Exposition Protocol](#18-exposition-protocol)
19. [Problems and Solutions](#19-problems-and-solutions)
20. [Character Design](#20-character-design)
21. [The Text (Dialogue & Description)](#21-the-text-dialogue--description)
22. [A Writer's Method](#22-a-writers-method)
23. [Quick Reference Card](#23-quick-reference-card)

---

## 0. Meta-Principles (Axioms)

### 0.1 Principles vs. Rules
```
AXIOM RM-A0: "Anxious, inexperienced writers obey rules. Rebellious, 
       unschooled writers break rules. Artists master the form."

IMPLICATION: Rules are contextual; principles are universal.
             Learn the form deeply before deviating.
```

### 0.2 Story as Universal Form
```
AXIOM RM-A1: "Story is not flight from reality but a vehicle that 
       carries us on our search for reality."

FUNCTION: Story serves as equipment for living.
          A story is "the creative demonstration of truth."
```

### 0.3 Archetype vs. Stereotype
```
AXIOM RM-A3: "Archetype = universal human patterns (use these)
  - Stereotype = shallow, overused patterns (avoid these)

TEST: Does this pattern reveal deep human truth, or does it 
      merely repeat surface conventions?"
```

### 0.4 The Master Law
```
AXIOM RM-A2: "You must not tell the audience what to think or feel.
            You must show and let them discover it themselves."

DERIVATIVE: "Show, don't tell" â€” the supreme creative discipline.
```

---

## 1. Structural Hierarchy

### 1.1 Formal Definitions

```
BEAT: The smallest unit of story structure.
      An exchange of behavior in action/reaction.
      Definition: A change in behavior that happens when 
      one character's action meets another's reaction.

SCENE: A sequence of beats unified by:
       - Time (continuous or elliptical)
       - Place (single location or related spaces)
       - Action (one dramatic question)
       
       CONSTRAINT: A scene MUST turn on a value change.
       VALIDITY_TEST: IF opening_value == closing_value THEN scene is invalid

SEQUENCE: A series of scenes (2-5 typically) that:
          - Build toward a moderate reversal
          - Have greater impact than any single component scene
          - Are unified by a single dramatic question

ACT: A series of sequences (3-5 typically) that:
     - Build toward a major reversal
     - Climax with a turning point more powerful than any sequence
     - Creates irreversible change in protagonist's situation

STORY: The overarching structure containing all acts.
       - Opens with Inciting Incident
       - Closes with Story Climax + Resolution
       - Satisfies the master dramatic question
```

### 1.2 Hierarchy Constraints

```python
def validate_hierarchy(story):
    """All levels must exhibit value change"""
    for act in story.acts:
        assert act.has_major_reversal()
        for sequence in act.sequences:
            assert sequence.has_moderate_reversal()
            for scene in sequence.scenes:
                assert scene.opening_value != scene.closing_value
                for beat in scene.beats:
                    assert beat.has_action_reaction_exchange()
    return True
```

---

## 2. The Story Triangle (Design Space)

### 2.1 The Triangle Model

```
                    ARCHPLOT (Classical Design)
                          /\
                         /  \
                        /    \
                       /      \
                      /        \
            MINIPLOT /          \ ANTIPLOT
         (Minimalism)            (Anti-structure)
                    \            /
                     \          /
                      \        /
                       \      /
                        \    /
                         \  /
                          \/
                       NONPLOT
                    (Portraiture)
```

### 2.2 Archplot (Classical Design) â€” The Default

| Attribute | Archplot Value |
|-----------|----------------|
| Protagonist | Single, active |
| Conflict | External, primarily |
| Time | Linear chronology |
| Causality | Tight causeâ†’effect |
| Reality | Consistent |
| Ending | Closed, irreversible change |
| Audience | Largest |

### 2.3 Miniplot (Minimalism)

| Attribute | Miniplot Deviation |
|-----------|-------------------|
| Protagonist | Passive or multiple |
| Conflict | Internal, primarily |
| Time | May be non-linear |
| Ending | Open (ambiguous) |
| Audience | Smaller |

### 2.4 Antiplot (Anti-structure)

| Attribute | Antiplot Deviation |
|-----------|-------------------|
| Causality | Coincidence, randomness |
| Time | Non-linear, fragmented |
| Reality | Inconsistent realities |
| Ending | May be contradictory |
| Audience | Smallest (cinephiles) |

### 2.5 The Mastery Principle

```
PRINCIPLE: "First, the masters mastered the Archplot."

ALGORITHM:
  1. Learn classical form thoroughly
  2. Demonstrate competence in classical form
  3. THEN (and only then) experiment with Miniplot/Antiplot
  4. Reason: Miniplot/Antiplot are REACTIONS to classical form
     - Cannot effectively subvert what you don't understand
```

### 2.6 Budget-Audience Law

```
LAW: IF audience_size_shrinks THEN budget_must_shrink

IMPLICATION:
  - Archplot â†’ Largest audience â†’ Largest viable budget
  - Miniplot â†’ Smaller audience â†’ Moderate budget
  - Antiplot â†’ Smallest audience â†’ Minimal budget
  
ROBBE-GRILLET_RULE: "Never spend more than you can recoup 
                    from your faithful but meager audience."
```

---

## 3. Structure and Setting

### 3.1 The Principle of Creative Limitation

```
PRINCIPLE: "Limitation is vital. The first step toward a well-told 
           story is to create a small, knowable world."

PARADOX: The larger the world, the MORE clichÃ©d the story.
         The smaller the world, the MORE original the story.

REASON: 
  - Large world â†’ Diluted knowledge â†’ Fewer creative choices â†’ ClichÃ©
  - Small world â†’ Complete knowledge â†’ Greater creative choices â†’ Originality
```

### 3.2 Setting Dimensions

```
SETTING = {
    PERIOD: "The story's place in time"
    DURATION: "The story's length through time"  
    LOCATION: "The story's place in space"
    LEVEL_OF_CONFLICT: "The story's position in the hierarchy of human struggles"
}

CONSTRAINT: "There is no such thing as a portable story.
            An honest story is at home in one, and only one, place and time."
```

### 3.3 Research Methods

```python
def research_story_world():
    """Three methods of research, all needed"""
    
    # 1. Research of Memory
    memory_research = ask("What do I know from personal experience 
                          that touches on my characters' lives?")
    # Write it down â€” "In your head it's only memory, 
    # but written down it becomes working knowledge."
    
    # 2. Research of Imagination  
    imagination_research = ask("What would it be like to live my 
                               character's life hour by hour, day by day?")
    # Sketch scenes that may never appear but build world knowledge
    
    # 3. Research of Fact
    fact_research = library_research()
    # "You're blocked because you have nothing to say."
    # "Talent must be stimulated by facts and ideas."
    
    return combine(memory_research, imagination_research, fact_research)
```

### 3.4 Writer's Block Cure

```
DIAGNOSIS: "You're blocked because you have nothing to say."
CURE: "A trip to the library."
EXPLANATION: "You can't kill your talent, but you can starve it 
             into a coma through ignorance."
```

### 3.5 The ClichÃ© War

```python
def fight_cliche_war(scene_idea):
    """The 10-to-1 creativity principle"""
    
    # Never trust first inspiration â€” it's usually a clichÃ©
    alternatives = []
    for i in range(10):  # Generate AT LEAST 10 alternatives
        alternatives.append(generate_alternative(scene_idea))
    
    # Selection criteria
    for alt in alternatives:
        if (is_true_to_character(alt) and 
            is_true_to_world(alt) and 
            has_never_been_done_this_way(alt)):
            return alt
    
    # If all alternatives are clichÃ© but setting is right,
    # go deeper into that setting
    return research_deeper_into_setting(scene_idea)
```

---

## 4. Structure and Genre

### 4.1 Genre Definition

```
GENRE: A set of conventions that create audience expectations.

CONVENTION_TYPES:
  - Setting conventions (Western = frontier)
  - Role conventions (Crime = criminal, detective)
  - Event conventions (Love Story = boy meets girl)
  - Value conventions (Disillusionment = hope â†’ cynicism)
```

### 4.2 Master Genre List

| # | Genre | Core Convention |
|---|-------|-----------------|
| 1 | Love Story | Blocking characters oppose love |
| 2 | Horror | Monster(s) threaten protagonist |
| 3 | Modern Epic | Individual vs. State |
| 4 | Western | Frontier setting, civilization vs. wilderness |
| 5 | War Genre | Combat as crucible |
| 6 | Maturation Plot | Protagonist grows from youth to maturity |
| 7 | Redemption Plot | Protagonist changes from bad to good |
| 8 | Punitive Plot | Protagonist changes from good to bad |
| 9 | Testing Plot | Willpower challenged to its limits |
| 10 | Education Plot | Protagonist gains profound knowledge |
| 11 | Disillusionment Plot | Optimism â†’ cynicism |
| 12 | Comedy | Nobody gets hurt; social satire |
| 13 | Crime | Criminal, detective, clues, apprehension |
| 14 | Social Drama | Societal problem as antagonist |
| 15 | Action/Adventure | Physical spectacle, external obstacles |
| 16 | Historical Drama | Past era as setting |
| 17 | Biography | Person's life as story |
| 18 | Docu-Drama | Recent events dramatized |
| 19 | Mockumentary | Fake documentary satirizing institutions |
| 20 | Musical | Characters sing/dance their stories |
| 21 | Science Fiction | Hypothetical futures |
| 22 | Sports Genre | Athletic competition as crucible |
| 23 | Fantasy | Physical laws bent or broken |
| 24 | Animation | Universal metamorphism |
| 25 | Art Film | Minimalism or Antistructure |

### 4.3 Genre Evolution Algorithm

```python
def evolve_genre(genre, social_climate):
    """Genres must evolve with social attitudes"""
    
    # Example: Love Story blocking characters
    if era == "pre_1960s":
        blocking_force = "parents"
    elif era == "1960s_1980s":
        blocking_force = ["culture", "law", "society", "identity"]
    elif era == "1990s+":
        blocking_force = ["internal_belief", "timing", "fate", "death"]
    
    # The lesson
    if convention_feels_antiquated(social_climate):
        reinvent_convention()  # CHINATOWN broke "detective catches criminal"
    
    return updated_genre
```

### 4.4 Genre Comedy Conventions

```
COMEDY_MASTER_CONVENTION: "Nobody gets hurt."
  - Audience must feel characters bounce off walls but survive
  - Once real harm occurs, comedy becomes drama/tragedy

COMEDY_TARGET: A social institution perceived as hypocritical
  - Military â†’ M*A*S*H
  - Rich â†’ MY MAN GODFREY  
  - Courtship â†’ WHEN HARRY MET SALLY
  - Theatre â†’ THE PRODUCERS
```

### 4.5 The Gift of Endurance

```
PRINCIPLE: Genre creates AUDIENCE ENDURANCE.

MECHANISM:
  1. Audience brings genre expectations to the story
  2. These expectations allow tolerance of darker/more intense content
  3. Without genre frame, same content would be unbearable
  
EXAMPLE: Horror audiences endure terror because they've "signed up for it."
```

---

## 5. Structure and Character

### 5.1 Character vs. Characterization

```
CHARACTERIZATION: The sum of all observable qualities.
  - Age, IQ, sex, sexuality, style of speech
  - Gesture, education, occupation, personality
  - Values, attitudes, where they live, how they dress
  
  FUNCTION: Makes characters believable and vivid
  
CHARACTER (True/Deep): The choices made under pressure.
  - Revealed ONLY through action under pressure
  - "Pressure is essential. True character is revealed 
    in the choices a human being makes under pressure."
  
DISTINCTION: "The greater the pressure, the deeper the revelation,
             the truer the choice to the character's essential nature."
```

### 5.2 Character Revelation Algorithm

```python
def reveal_character(protagonist, story):
    """Five-step character revelation process"""
    
    # Step 1: Establish characterization
    establish_surface_traits(protagonist)  # Hamlet is melancholy
    
    # Step 2: Reveal true nature through choice under pressure
    choice = force_choice_under_pressure(protagonist)
    # Hamlet's cautious nature revealed in decision to verify before acting
    
    # Step 3: Create contradiction between mask and nature
    # "He is not what he appears to be"
    assert characterization != true_character
    
    # Step 4: Escalate pressure, force harder choices
    for pressure_level in increasing_pressure:
        harder_choice = force_choice(protagonist, pressure_level)
        reveal_deeper_nature(harder_choice)
    
    # Step 5: Climax profoundly changes character
    final_choice = crisis_decision(protagonist)
    transform_character(protagonist, final_choice)
```

### 5.3 Structure/Character Functions

```
FUNCTION OF STRUCTURE:
  "To provide progressively building pressures that force characters 
   into more and more difficult dilemmas where they must make 
   more and more difficult risk-taking choices and actions, 
   gradually revealing their true natures, even down to the 
   unconscious self."

FUNCTION OF CHARACTER:
  "To bring to the story the qualities of characterization necessary 
   to convincingly act out choices."

INTERLOCK: "If you change one, you change the other."
```

### 5.4 Character Arc Types

```
CHARACTER_ARC = change in deep character over story duration

TYPES:
  - Positive arc: Worse â†’ Better (most common)
  - Negative arc: Better â†’ Worse (tragedy)
  - Flat arc: Character reveals but doesn't change (Bond films)
  
REQUIREMENT: Arc must be EXPRESSED through action, not stated.
```

---

## 6. Structure and Meaning

### 6.1 Controlling Idea Formula

```
CONTROLLING_IDEA = VALUE + CAUSE

FORMAT: "[VALUE] is [achieved/lost] because [CAUSE]"

EXAMPLES:
  - "Justice triumphs because the protagonist is more 
     cunning than the criminal." (Up-ending crime story)
  - "Love is lost because lovers value career over intimacy."
     (Down-ending love story)
  - "Happiness is achieved because we learn to accept our flaws."
     (Education plot)
```

### 6.2 Controlling Idea Discovery

```python
def discover_controlling_idea(story):
    """The idea emerges from the climax, not from planning"""
    
    # The controlling idea is discovered, not imposed
    climax = story.story_climax
    final_value_charge = climax.value_at_close
    cause = identify_cause_of_climax(climax)
    
    controlling_idea = f"{final_value_charge} because {cause}"
    
    # Verify unity
    for event in story.all_events:
        assert event.reinforces(controlling_idea)
    
    return controlling_idea
```

### 6.3 Meaning Types

```
IDEALIST: "Up-ending expressing the optimism, hopes, and dreams 
          of mankind."
          
PESSIMIST: "Down-ending expressing mankind's cynicism."

IRONIST: "Climax that simultaneously expresses both optimism 
         and pessimism â€” life's bittersweet truth."
         
IRONY_FORMS:
  - Up-ending with down-undertone (bitter victory)
  - Down-ending with up-undertone (meaningful defeat)
```

### 6.4 Didacticism Warning

```
WARNING: "When the meaning of life is at stake, no one wants to 
         be told what to think."

RULE: Story must DEMONSTRATE truth, not LECTURE it.

TEST: Remove all dialogue stating the theme.
      Does the story still express its meaning through action?
      IF NO â†’ rewrite to show, not tell.
```

---

## 7. The Substance of Story

### 7.1 Story Events

```
STORY_EVENT: An event that creates meaningful change in the 
             character's life situation, expressed and experienced 
             in terms of value.

REQUIREMENTS:
  1. Must change a value (from + to - or - to +)
  2. Change must be expressed through conflict
  3. Conflict must be expressed through action
  
NON-EVENTS: Activity that doesn't change values
            (exposition dumps, travelogue, description without conflict)
```

### 7.2 The Law of Conflict

```
LAW: "Nothing moves forward in a story except through conflict."

COROLLARY: "When talented people write badly, it's generally 
           for one of two reasons: either they're blinded by an 
           idea they feel compelled to prove, or they're driven 
           by an emotion they must express."

SOLUTION: "Subordinate ideas and emotions to story."
```

### 7.3 Backstory and Memory

```
BACKSTORY: "The set of significant events that occurred in the 
           characters' past."

PRINCIPLE: "Backstory is exposition, and exposition is 
           ammunition, not exploration."

USE: Reveal backstory only when:
  1. It serves as ammunition in present conflict
  2. It creates dramatic irony
  3. It explains present motivation at moment of crisis
```

---

## 8. The Gap Algorithm

### 8.1 Core Engine

```python
def gap_algorithm(character, desire):
    """The fundamental engine of narrative tension"""
    
    while not story_resolved:
        # Character takes action expecting a result
        action = character.choose_action(desire)
        expected_result = character.anticipate_outcome(action)
        
        # Reality does not cooperate
        actual_result = world.respond(action)
        
        # THE GAP: Difference between expectation and result
        gap = expected_result - actual_result
        
        if gap == 0:
            # No tension â€” scene is dead
            raise InvalidScene("No gap between expectation and result")
        
        # Gap forces escalation
        if actual_result.is_worse_than(expected_result):
            # Risk increases
            character.capacity_must_increase()
            character.take_greater_risk()
            # Story progresses
```

### 8.2 Gap Visualization

```
Character's Subjective Reality
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚ EXPECTATION                 â”‚
â”‚ "If I do X, Y will happen"  â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
              â†“
         [ACTION X]
              â†“
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚ THE GAP                     â”‚
â”‚ "Reality splits open"       â”‚
â”‚ "Forces of antagonism       â”‚
â”‚  stronger than expected"    â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
              â†“
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚ ACTUAL RESULT               â”‚
â”‚ "Not Y, but Z (worse)"      â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
              â†“
         [ESCALATION]
         (Repeat with higher stakes)
```

### 8.3 Gap Placement

```
PRINCIPLE: Every scene must contain at least one gap.
           Major scenes (act climaxes) contain major gaps.

CLIMAX_GAP: The largest gap, at the Story Climax, opens the 
            most profound difference between expectation and result.
            
EXAMPLE (EMPIRE STRIKES BACK):
  Luke's expectation: "I will defeat Vader"
  Gap 1: "I am your father" â€” reality shatters
  Gap 2: Vader wants Luke to join him, not die
  Gap 3: Luke must choose suicide over evil
```

---

## 9. Value Charge System

### 9.1 Value Pairs

```
VALUES: Binary pairs that define human experience

EXAMPLES:
  - Life / Death
  - Love / Hate  
  - Freedom / Slavery
  - Truth / Lie
  - Courage / Cowardice
  - Hope / Despair
  - Meaning / Meaninglessness
  - Justice / Injustice
  - Maturity / Immaturity
  - Strength / Weakness
```

### 9.2 Value Progression Model

```
POSITIVE â†â†’ CONTRARY â†â†’ CONTRADICTORY â†â†’ NEGATION OF NEGATION

EXAMPLE (Justice):
  POSITIVE:        Justice (laws upheld fairly)
  CONTRARY:        Unfairness (nepotism, bias, delay)
  CONTRADICTORY:   Injustice (laws broken)
  NEGATION:        Tyranny ("Might Makes Right")

PRINCIPLE: "A story that progresses to the limit of human 
           experience must move through a pattern that includes 
           the Contrary, the Contradictory, and the Negation 
           of the Negation."
```

### 9.3 Four Ending Types

| Type | Final Charge | Example |
|------|--------------|---------|
| Up-ending | Positive | STAR WARS |
| Down-ending | Negative | CHINATOWN |
| Ironic up | Positive with negative undertone | THE GODFATHER |
| Ironic down | Negative with positive undertone | THELMA & LOUISE |

### 9.4 Scene Value Tracking

```python
def track_scene_values(scene):
    """Every scene must turn on at least one value"""
    
    opening_charge = scene.value_at_opening  # e.g., "hope +"
    closing_charge = scene.value_at_closing  # e.g., "hope -"
    
    if opening_charge == closing_charge:
        raise InvalidScene("Scene has no value change â€” delete or rewrite")
    
    return ValueTurn(
        value=scene.primary_value,
        direction=closing_charge.sign - opening_charge.sign,
        magnitude=abs(closing_charge - opening_charge)
    )
```

---

## 10. Conflict Architecture

### 10.1 Three Levels of Conflict

```
LEVEL 3: EXTRA-PERSONAL CONFLICT
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚ Society, Nature, Time, Space, Fate      â”‚
â”‚ Institutions, environment, supernatural â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                    â”‚
                    â–¼
LEVEL 2: PERSONAL CONFLICT  
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚ Relationships with family, friends,     â”‚
â”‚ lovers, colleagues, rivals              â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                    â”‚
                    â–¼
LEVEL 1: INNER CONFLICT
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚ Conflicts within the protagonist:       â”‚
â”‚ mind vs. heart, conscious vs. unconsciousâ”‚
â”‚ morality vs. desire                     â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

### 10.2 Conflict Distribution by Form

```
ARCHPLOT:     Emphasizes EXTRA-PERSONAL (but all levels present)
MINIPLOT:     Emphasizes INNER (but all levels present)
ANTIPLOT:     May abandon coherent conflict entirely

CINEMA_BIAS: Film naturally expresses EXTRA-PERSONAL conflict 
             (camera sees surfaces, not thoughts)
             
NOVEL_BIAS:  Prose naturally expresses INNER conflict
             (narrator can enter consciousness)
```

### 10.3 Conflict Sufficiency Test

```python
def test_conflict_sufficiency(story):
    """Forces of antagonism must equal or exceed protagonist's capacities"""
    
    protagonist_power = sum([
        protagonist.willpower,
        protagonist.intelligence,
        protagonist.emotional_capacity,
        protagonist.social_capacity,
        protagonist.physical_capacity
    ])
    
    antagonist_power = sum([
        inner_conflicts,
        personal_conflicts,
        extra_personal_conflicts
    ])
    
    # Protagonist must be underdog
    assert antagonist_power >= protagonist_power
    
    # But victory must be possible
    assert protagonist_has_chance_to_win()
```

---

## 11. The Inciting Incident Protocol

### 11.1 Definition and Requirements

```
INCITING_INCIDENT: "An event that radically upsets the balance 
                   of forces in the protagonist's life."

REQUIREMENTS:
  1. Must be a SINGLE event (not gradual)
  2. Must be DYNAMIC (not static situation)
  3. Must upset BALANCE (protagonist had equilibrium before)
  4. Must create SPINE (story's dramatic question)
  
THE_SPINE: The desire aroused by the Inciting Incident that 
           unifies all subsequent events toward the Story Climax.
```

### 11.2 Inciting Incident Timing

```python
def place_inciting_incident(story):
    """Timing depends on audience knowledge needs"""
    
    if audience_needs_setup_to_understand_protagonist:
        # Delay incident to allow establishment
        placement = "within_first_quarter"  # After setup scenes
    else:
        # Open with incident
        placement = "opening_scene"  # JAWS, KRAMER VS KRAMER
    
    # Absolute constraint
    assert inciting_incident.occurs_before(act_one_climax)
    
    return placement
```

### 11.3 Central Plot vs. Subplot Incidents

```
CENTRAL_PLOT_INCIDENT: The major inciting incident that creates 
                       the story's primary spine.
                       
SUBPLOT_INCIDENTS:     Secondary incidents for subplots.
                       May occur later in the story.
                       
RULE: "Main plot and major subplot incidents should ideally 
      occur within the first quarter of the storytelling."
```

### 11.4 Inciting Incident Categories

```
TWO_TYPES:
  
  1. RANDOM (Coincidental)
     - Comes from outside protagonist's control
     - "Fate throws a bolt"
     - Example: Body discovered (murder mystery)
     
  2. CAUSED (Deliberate)
     - Protagonist takes an action that triggers events
     - Example: Decides to leave spouse (divorce drama)

RULE: After the Inciting Incident, coincidence should diminish
      and character choice should increase.
```

---

## 12. Act Design Formulas

### 12.1 Minimum Act Requirement

```
MINIMUM: Three acts (Setup, Confrontation, Resolution)

PRINCIPLE: "There is no maximum, but there is a minimum."

WHY_THREE:
  - Act 1: Establishes and complicates
  - Act 2: Develops through progressive complications
  - Act 3: Resolves through crisis, climax, resolution
```

### 12.2 Act Proportions (Three-Act Model)

```
TYPICAL_PROPORTIONS:
  
  Act 1:  ~25% of screenplay (25-30 pages)
          - Inciting Incident through Act One Climax
          
  Act 2:  ~50% of screenplay (50-60 pages)
          - May contain Mid-Act Climax
          - Longest act with most progressive complications
          
  Act 3:  ~25% of screenplay (25-30 pages)
          - Crisis, Climax, Resolution
          - Often shorter than Act 1
          
IDEAL_ACT_THREE: ~10-15% (lean and fast)
```

### 12.3 Act Climax Requirements

```python
def validate_act_climax(act, story_position):
    """Each act climax must be more powerful than the last"""
    
    # Act climax must be major turning point
    assert act.climax.is_major_reversal()
    
    # Must be most powerful moment of the act
    for sequence in act.sequences[:-1]:  # All but final
        assert act.climax.power > sequence.climax.power
    
    # Progressive power
    if story_position > 1:
        previous_act = story.acts[story_position - 1]
        assert act.climax.power > previous_act.climax.power
```

### 12.4 Subplot Design

```
PURPOSE_OF_SUBPLOTS:
  1. Contradict Controlling Idea to enrich meaning
  2. Resonate with Controlling Idea to reinforce meaning
  3. Complicate Central Plot (create obstacles)
  4. Reveal character dimensions

SUBPLOT_RULES:
  - Subplots must connect to Central Plot
  - May not be cut without damaging Central Plot
  - May have their own act structure
  
FALSE_ENDING_TECHNIQUE:
  Use subplot climax to create false ending before true Story Climax
  (Common in Art Films and some Action films)
```

---

## 13. Scene Design Algorithm

### 13.1 Scene Construction

```python
def construct_scene(dramatic_question):
    """Build a scene from beats toward a turning point"""
    
    # 1. Define the scene's value at stake
    value = identify_value(dramatic_question)
    opening_charge = assess_value_charge(value)
    
    # 2. Build through beats
    beats = []
    current_charge = opening_charge
    
    while not turning_point_reached:
        beat = create_beat(
            action=character_action,
            reaction=opposing_reaction
        )
        beats.append(beat)
        current_charge = update_charge(beat)
    
    # 3. Create turning point (THE GAP)
    gap = create_gap(
        expectation=character_expectation,
        reality=actual_result
    )
    
    # 4. Verify value change
    closing_charge = assess_value_charge(value)
    assert closing_charge != opening_charge
    
    return Scene(beats, gap, value_turn=(opening_charge, closing_charge))
```

### 13.2 Beat Design

```
BEAT_STRUCTURE:
  
  ACTION â†â†’ REACTION
  
  - Character A takes action based on expectation
  - Character B reacts in unexpected way
  - Creates micro-gap within scene
  - Builds toward scene's major gap

BEAT_CHANGE_RULE:
  "A new beat doesn't occur until behavior clearly changes."
  Same action/reaction pattern = same beat (even if repeated)
```

### 13.3 Text vs. Subtext

```
TEXT:    What is said and done (surface behavior)
SUBTEXT: What is thought and felt (inner life)

PRINCIPLE: "Nothing is what it seems."

RULE: "No text without a subtext."
      Even when characters try to tell the truth, 
      there is an unconscious level beneath.

SCENE_TEST: Can actor play the subtext?
            If text = subtext, scene has no depth.
```

### 13.4 Turning Point Placement

```
TURNING_POINT: The moment when THE GAP opens.
               Creates irreversible change in the scene's value.

PLACEMENT_OPTIONS:
  1. END of scene (most common) â€” build to climactic moment
  2. MIDDLE of scene â€” allows aftermath/reaction
  3. BEGINNING of scene (rare) â€” starts in medias res

TECHNIQUE: "Split probability from necessity just one more time"
           Keep surprising the audience while remaining inevitable.
```

---

## 14. Scene Analysis Technique

### 14.1 Five-Step Analysis Protocol

```python
def analyze_scene(scene):
    """McKee's five-step scene analysis technique"""
    
    # STEP 1: Define Conflict
    driver = identify_who_drives_scene(scene)
    driver_desire = identify_desire(driver)  # as infinitive: "to do X"
    antagonism = identify_opposing_forces(scene)
    antagonism_desire = identify_opposing_desire(antagonism)
    
    # Verify direct opposition (not tangential)
    assert desires_directly_oppose(driver_desire, antagonism_desire)
    
    # STEP 2: Note Opening Value
    opening_value = identify_value_at_stake(scene.opening)
    opening_charge = assess_charge(opening_value)  # positive or negative
    
    # STEP 3: Break into Beats
    beats = []
    for exchange in scene.action_reaction_exchanges:
        action_phrase = describe_action(exchange.action)  # gerund phrase
        reaction_phrase = describe_reaction(exchange.reaction)
        beats.append(Beat(action_phrase, reaction_phrase))
    
    # STEP 4: Note Closing Value
    closing_value = identify_value_at_stake(scene.closing)
    closing_charge = assess_charge(closing_value)
    
    # Compare
    if closing_charge == opening_charge:
        return "NONEVENT â€” scene is flat, cut or rewrite"
    
    # STEP 5: Locate Turning Point
    turning_point = find_moment_gap_opens(beats)
    
    return SceneAnalysis(
        conflict=(driver_desire, antagonism_desire),
        value_change=(opening_charge, closing_charge),
        beats=beats,
        turning_point=turning_point
    )
```

### 14.2 Action Description Convention

```
DESCRIBE_WITH_GERUND_PHRASES:

BAD:  "He says he loves her"
GOOD: "Begging for forgiveness"

BAD:  "She looks away"  
GOOD: "Rejecting his advances"

PRINCIPLE: Name the SUBTEXTUAL action with emotive connotations.
           Not what literally happens, but what it MEANS.
```

---

## 15. Composition Principles

### 15.1 Unity

```
UNITY_TEST: "Because of the Inciting Incident, the Climax had to happen."

PRINCIPLE: Remove any scene that can be removed without 
           damaging the story. What remains is unified.

ARISTOTLE'S_UNITY: "A story is about one thingâ€”not many things."
```

### 15.2 Pacing

```
PACING = The rhythm of story movement

VARIABLES:
  - Scene length (shorter = faster)
  - Scene density (more beats = more intense)
  - Gap frequency (more gaps = more tension)
  - Rest beats (slower scenes for relief)

TEMPO_PRINCIPLE: Generally accelerate toward climax.
                 But vary rhythm to prevent monotony.

LAW_OF_DIMINISHING_RETURNS:
  "The more dialogue you write, the less effect dialogue has."
  Same applies to action, spectacle, emotion, etc.
```

### 15.3 Progression Types

```
SOCIAL_PROGRESSION:
  Widen impact through larger social circles
  (Individual â†’ Family â†’ Community â†’ Nation â†’ World)

PERSONAL_PROGRESSION:
  Deepen into more intimate relationships
  (Acquaintance â†’ Friend â†’ Lover â†’ Family)

SYMBOLIC_PROGRESSION:
  Ascend from literal to archetypal meaning
  (Specific event â†’ Universal truth)

IRONIC_PROGRESSION:
  Turn from one value to its opposite
  (Comedy â†’ Tragedy, or vice versa)
```

### 15.4 Transition Principles

```
SCENE_TRANSITIONS: How to link scenes

TECHNIQUES:
  1. CUT ON ACTION â€” Movement carries across cut
  2. CUT ON SIMILARITY â€” Visual or thematic echo
  3. CUT ON CONTRAST â€” Deliberate opposition
  4. CUT ON QUESTION â€” Scene ends on unanswered question

PRINCIPLE: "Third world, third possibility"
           Instead of A â†’ B, try A â†’ C â†’ B for richer meaning.
```

---

## 16. Crisis, Climax, Resolution

### 16.1 Crisis Definition

```
CRISIS: "The ultimate decision. Danger/Opportunity."

CHINESE_IDEOGRAM: Crisis = Danger + Opportunity

REQUIREMENTS:
  1. Must be TRUE DILEMMA:
     - Choice between irreconcilable goods, OR
     - Choice between lesser of two evils, OR
     - Both simultaneously
  2. Must place protagonist under MAXIMUM PRESSURE
  3. Must be OBLIGATORY SCENE (audience has been waiting for it)
  
REVELATION: "How the protagonist chooses here gives us the most 
            penetrating view of his deep character."
```

### 16.2 Crisis Dilemma Types

```
TYPE_1: IRRECONCILABLE GOODS
  Character must choose between two positive values
  Example: Love vs. Duty, Freedom vs. Security
  
TYPE_2: LESSER OF TWO EVILS
  Character must choose between two negative outcomes
  Example: Die vs. Betray friend
  
TYPE_3: COMBINATION
  Good/Evil on both sides simultaneously
  Richest form of dilemma
```

### 16.3 Climax Design

```
CLIMAX: "The action the protagonist takes at Crisis creates 
        the Story Climax."

CLIMAX_TYPES:
  1. STRAIGHT ACTION from Crisis Decision
     (STAR WARS â€” Luke uses Force, destroys Death Star)
     
  2. CLIMAX WITH EMBEDDED TURNING POINT
     (EMPIRE STRIKES BACK â€” Multiple gaps within climax)

CLIMAX_WITH_GAPS:
  "If we can split probability from necessity just one more time,
   we may create a majestic ending the audience will treasure 
   for a lifetime."
```

### 16.4 Crisis Placement

```python
def place_crisis(story):
    """Crisis placement depends on climactic action length"""
    
    if climactic_action.is_brief():
        # Crisis and Climax in same scene, last minutes
        placement = "final_scene"
        # Example: THELMA & LOUISE â€” decision and action nearly simultaneous
        
    elif climactic_action.is_extended():
        # Crisis at Act 2 Climax, Act 3 is climactic action
        placement = "end_of_act_2"
        # Example: CASABLANCA â€” Rick's decision fills entire Act 3
        
    elif climactic_action.spans_entire_film():
        # Crisis immediately after Inciting Incident
        placement = "after_inciting_incident"
        # Example: JAMES BOND â€” takes assignment, rest is pursuit
```

### 16.5 Resolution

```
RESOLUTION: "Any material after the Story Climax"

PURPOSES:
  1. Subplots: Complete subplot climaxes not yet resolved
  2. Spread climax: Show effects of climax radiating outward
  3. Courtesy: Let audience recover emotionally ("slow curtain")

PRINCIPLE: "A few seconds, not a few minutes"
           Resolution should be brief; emotional weight 
           already carried by climax.
```

---

## 17. The Principle of Antagonism

### 17.1 The Master Principle

```
PRINCIPLE_OF_ANTAGONISM:
  "A protagonist and his story can only be as intellectually 
   fascinating and emotionally compelling as the forces of 
   antagonism make them."

COROLLARY: "All other factors of talent, craft, and knowledge 
           being equal, greatness is found in the writer's 
           treatment of the negative side."
```

### 17.2 Negation of Negation

```
VALUE_PROGRESSION_TO_THE_END_OF_THE_LINE:

POSITIVE â†’ CONTRARY â†’ CONTRADICTORY â†’ NEGATION OF NEGATION

JUSTICE EXAMPLE:
  Positive:     Justice
  Contrary:     Unfairness (bias, but not illegal)
  Contradictory: Injustice (laws broken)
  Negation:     Tyranny ("Might Makes Right")

LOVE EXAMPLE:
  Positive:     Love
  Contrary:     Indifference  
  Contradictory: Hate
  Negation:     Self-hatred masked as love

TRUTH EXAMPLE:
  Positive:     Truth
  Contrary:     White lie
  Contradictory: Lie
  Negation:     Self-deception

PRINCIPLE: "If a story does not reach the Negation of the Negation,
           it may strike the audience as satisfyingâ€”but never 
           brilliant, never sublime."
```

### 17.3 Underdog Requirement

```python
def ensure_underdog(protagonist, forces_of_antagonism):
    """Protagonist must be overmatched at start"""
    
    protagonist_capacity = (
        protagonist.willpower +
        protagonist.intellect +
        protagonist.emotion +
        protagonist.social_power +
        protagonist.physical_power
    )
    
    antagonism_total = (
        inner_conflicts +
        personal_conflicts +
        extra_personal_conflicts
    )
    
    # Protagonist must be underdog
    assert antagonism_total > protagonist_capacity
    
    # But must have a chance
    assert protagonist_can_possibly_win()
    
    # SUPERMAN example: 
    # Give seemingly invincible hero impossible dilemmas
```

---

## 18. Exposition Protocol

### 18.1 Two Laws of Exposition

```
LAW_1: "Never include anything the audience can reasonably 
        and easily assume has happened."

LAW_2: "Never pass on exposition unless the missing fact 
        would cause confusion."

COROLLARY: "You do not keep the audience's interest by giving 
           it information, but by withholding information."
```

### 18.2 Dramatized Exposition

```
AXIOM: "Show, don't tell."

TECHNIQUE: "Convert exposition to ammunition."

BAD_EXPOSITION:
  "Harry, how long have we known each other? Twenty years, 
   since college, right?"
  (Tells audience facts with no dramatic purpose)

GOOD_EXPOSITION:
  "Harry, look at you. Same hippie haircut, still stoned by noon,
   same stunts that got you kicked out of school twenty years ago."
  (Uses facts as WEAPONS in present conflict)

PRINCIPLE: Characters use what they know to get what they want.
           Exposition emerges naturally from conflict.
```

### 18.3 Exposition Pacing

```
PACING_RULE: "Least important facts come early,
             most important facts come last."

CRITICAL_EXPOSITION = SECRETS
  The painful truths characters don't want known.
  Hold these until dramatically necessary.

THE_ICEBERG: Like Hemingway's iceberg principle,
             story implies far more than it states.
             
             "The audience should be unaware of exposition 
              as they absorb it. If they feel it, it's failed."
```

### 18.4 Flashback Protocol

```python
def use_flashback(story, past_event):
    """Two principles for flashback use"""
    
    # PRINCIPLE 1: Must accelerate pace
    if flashback.slows_pace:
        return "Don't use flashback"
    # Example: CASABLANCA Paris flashback speeds up after slow opening
    
    # PRINCIPLE 2: Create need before revealing
    if not audience.needs_and_desires_to_know:
        return "Don't use flashback yet"
    # Example: CASABLANCA â€” audience burning with curiosity about past
    #          THEN flashback occurs
```

### 18.5 Exposition Delivery Methods

```
METHODS (from best to worst):

1. DRAMATIZED â€” Characters use facts as ammunition in conflict
2. VISUAL â€” Camera shows without dialogue
3. COUNTERPOINT NARRATION â€” Woody Allen style (ironic commentary)
4. BRIEF NARRATION â€” Quick bridges between acts
5. MONTAGE â€” Compressed information sequences
6. DREAM SEQUENCE â€” Disguised exposition (usually weak)
7. TELLING NARRATION â€” Voice-over explaining (worst)

WARNING: "The trend toward using telling narration throughout 
         a film threatens the future of our art."
```

---

## 19. Problems and Solutions

### 19.1 The Problem of Interest

```
INTEREST = CURIOSITY + CONCERN

CURIOSITY (Intellectual):
  - Need to answer questions, close open patterns
  - "What's going to happen next?"
  - "How will it turn out?"
  
CONCERN (Emotional):
  - Need for positive values (justice, love, truth)
  - Audience seeks "Center of Good"
  - Empathy with protagonist

CENTER_OF_GOOD:
  - Must be located at least in protagonist
  - Created through contrast with surrounding negativity
  - "Good" is relative to the story's moral landscape
```

### 19.2 Mystery, Suspense, Dramatic Irony

```
THREE_MODES:

MYSTERY: Audience knows LESS than characters
  - "Whodunit?"
  - Curiosity about the past (what happened?)
  
SUSPENSE: Audience knows SAME as characters  
  - Experience together with protagonist
  - Anxiety about outcome
  
DRAMATIC_IRONY: Audience knows MORE than characters
  - "Don't go in there!"
  - Superior position creates tension
  
HITCHCOCK_BOMB_EXAMPLE:
  - Two men talking, bomb under table
  - If audience doesn't know â†’ surprise (weak)
  - If audience knows â†’ suspense for 5 minutes (strong)
```

### 19.3 Coincidence Rules

```
COINCIDENCE_RULE_1:
  "Use coincidence early to trigger complications."
  Coincidence is acceptable to START things.
  
COINCIDENCE_RULE_2:
  "Do not use coincidence beyond the midpoint."
  Story must move into characters' hands.
  
COINCIDENCE_RULE_3:
  "NEVER use coincidence to turn an ending."
  This is DEUS EX MACHINA â€” the writer's greatest sin.
  
DEUS_EX_MACHINA:
  "An insult to the audience because it is a lie.
   We all know we must choose and act to determine 
   the meaning of our lives."

EXCEPTION: Antiplot films use coincidence as meaning
           (WEEKEND, AFTER HOURS) â€” "Life is absurd."
```

### 19.4 The Problem of Comedy

```
COMIC_VISION: "In the best of circumstances human beings 
              find some way to screw up."

COMIC_WRITER: "Frustrated idealist."
              Wants world to be perfect, sees it isn't.
              Uses laughter to criticize institutions.

COMIC_CHARACTER: Marked by BLIND OBSESSION
  - Does not see their own mania
  - The moment they see it, comedy ends
  - Example: Clouseau as "perfect detective"
  
COMIC_DESIGN:
  - Comedy allows halting narrative drive for comic setpieces
  - But must still progress through value changes
  - Ending: Nobody gets permanently hurt
```

### 19.5 The Problem of Melodrama

```
DEFINITION: "Melodrama is not the result of overexpression,
            but of undermotivation."

CAUSE: Motivation doesn't match action.
       Action feels unearned.

CURE: "Lift the forces that drive your characters to equal 
      or surpass the extremities of their actions."

PRINCIPLE: There is nothing human beings do that is inherently
           melodramatic. Any extreme can be believed if 
           properly motivated.
```

### 19.6 The Problem of Holes

```
HOLE: A missing link in the chain of cause and effect.

SOLUTIONS:
  1. FORGE A LINK â€” Create scene that logically connects
     (Risk: scene has no purpose except logic)
     
  2. LET IT PASS â€” "Will they notice?"
     In the flow of time, holes often pass unnoticed
     
  3. ACKNOWLEDGE IT â€” Have character mention the illogic
     "Never, ever write a scene that tells an audience 
      what's about to happen. Instead, use that scene 
      to make the audience anticipate something else."
```

### 19.7 The Problem of Adaptation

```
ADAPTATION_PRINCIPLES:

PRINCIPLE_1: "The more purely the work expresses itself 
             in one medium, the less likely it will 
             translate to another."
  - Interior novels â†’ Hard to film
  - Dialogue-heavy plays â†’ Better candidates
  
PRINCIPLE_2: "Be willing to reinvent."
  - Tell the story in filmic rhythms
  - Keep the spirit, change the structure
  - Turn mental into physical
  
PRINCIPLE_3: Choose adaptable material
  - Look for conflict on all three levels
  - Emphasis on extra-personal (camera-attractive)
  - Avoid "pure" interior literature

PROCESS:
  1. Read repeatedly until infused with spirit
  2. Reduce each event to 1-2 sentence statement
  3. Ask: "Is this story well told?"
  4. Reorder in chronology, create step-outline
  5. Create new scenes as needed
  6. Turn what is mental into the physical
```

---

## 20. Character Design

### 20.1 Dimension Formula

```
DIMENSION: A contradiction within character.

FORMULA: Characterization A + Deep Character B
         where A contradicts B
         
EXAMPLE: Hamlet
  - Characterization: Melancholy, thoughtful, cautious
  - Deep Character: Rash, passionate, impulsive
  - Dimension: The contradiction creates complexity
  
PRINCIPLE: "Dimension means contradiction: either within 
           deep character (guilt-ridden criminal) or between 
           characterization and deep character (charm-masked killer)."
```

### 20.2 Cast Design (Constellation)

```
CAST_AS_CONSTELLATION:
  
         â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
         â”‚   PROTAGONIST   â”‚ â† Center of gravity
         â””â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                  â”‚
    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
    â”‚             â”‚             â”‚
    â–¼             â–¼             â–¼
â”Œâ”€â”€â”€â”€â”€â”€â”€â”    â”Œâ”€â”€â”€â”€â”€â”€â”€â”    â”Œâ”€â”€â”€â”€â”€â”€â”€â”
â”‚ Char Bâ”‚    â”‚ Char Câ”‚    â”‚ Char Dâ”‚
â”‚(friend)    â”‚(rival)â”‚    â”‚(lover)â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”˜    â””â”€â”€â”€â”€â”€â”€â”€â”˜    â””â”€â”€â”€â”€â”€â”€â”€â”˜
    â”‚             â”‚             â”‚
    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                  â”‚
                  â–¼
           â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
           â”‚ Tertiary  â”‚
           â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜

PRINCIPLE: Each character brings out dimensions of others.
           Cast exists to reveal protagonist's complexity.
```

### 20.3 Comic Character Design

```
COMIC_CHARACTER = CHARACTER + BLIND_OBSESSION

OBSESSION_PROPERTIES:
  - Character does NOT see it (crucial)
  - Drives all behavior
  - Creates comic situations
  
IF character.sees_obsession():
    character.becomes_dramatic()  # Comedy ends

EXAMPLES:
  - Clouseau: Obsessed with being perfect detective
  - Archie Bunker: Obsessed with bigoted worldview
  - Otto (WANDA): Obsessed with being intellectual
```

### 20.4 Tips for Screen Characters

```
TIP_1: "Leave room for the actor."
  - Don't overwrite behaviors and gestures
  - Actor needs: What do I want? Why? How? What stops me?
  - Characterization is actor's work as much as writer's
  
TIP_2: "Fall in love with all your characters."
  - Even villains see themselves as heroes
  - Write each character's scene from their POV
  - Understand their justifications
  
TIP_3: "Character is self-knowledge."
  - Write characters who know themselves deeply
  - But still have unconscious blind spots
  - Creates truthful complexity
```

### 20.5 Bit Part Design

```
BIT_PARTS: "Should be drawn deliberately flat... but not dull."

RULE: "Give each a freshly observed trait that makes the role 
      worth playing for the moment the actor's onscreen, but no more."

DANGER: Don't make bit parts too interesting
        - Creates false anticipation
        - Audience expects them to return
        - If they don't, audience is annoyed
```

---

## 21. The Text (Dialogue & Description)

### 21.1 Dialogue Principles

```
DIALOGUE_AS_LAST_LAYER:
  "The best advice for writing film dialogue is don't."
  
HIERARCHY:
  1. First, try to write scene purely visually
  2. If dialogue is necessary, write it last
  3. The less dialogue, the more impact dialogue has
  
LAW_OF_DIMINISHING_RETURNS:
  "The more dialogue you write, the less effect dialogue has."
```

### 21.2 The Suspense Sentence

```
SUSPENSE_SENTENCE: Periodic sentence with meaning at END.

BAD: "I really didn't want you to do it, you know, 
      because of how things were between us."
     (Meaning buried, tail-end is empty)

GOOD: "If you didn't want me to do it, why'd you give me that... look?"
      (Meaning comes at final word)

PRINCIPLE: Meaning delayed to last word forces listener 
           (and actor taking cue) to attend to entire line.
```

### 21.3 The Silent Screenplay

```
HITCHCOCK: "When the screenplay has been written and the 
           dialogue has been added, we're ready to shoot."

BERGMAN_EXAMPLE (THE SILENCE):
  - Waiter seducing customer scene
  - No words spoken
  - He sniffs her head to toe, she draws delirious breath
  - CUT TO: They're in hotel room
  - "Perfect, isn't it? Erotic, purely visual."
  
PRINCIPLE: "Image is our first choice, dialogue the regretful 
           second choice."
```

### 21.4 Description Principles

```
DESCRIPTION_GOAL: Put a film in the reader's head.

RULE_1: Describe only what is photographic.
  BAD: "He's been sitting there for a long time."
  GOOD: "He stubs out his tenth cigarette."

RULE_2: Use vivid, specific nouns and verbs.
  BAD: "The car moves down the road"
  GOOD: "The Chevy fishtails down the gravel road"
  
RULE_3: Avoid generic terms.
  Use names of things, not categories.
  
ONTOLOGY: "The screen is an absolute present tense 
          in constant vivid movement."
```

### 21.5 Image Systems

```
IMAGE_SYSTEM: "A strategy of motifs, a category of imagery 
              embedded in the film that repeats in sight 
              and sound from beginning to end."

PURPOSE:
  - Adds subliminal layer of meaning
  - Reinforces theme without stating it
  - Creates unity through repetition

TYPES:
  1. EXTERNAL IMAGERY â€” Things in the world (water, fire, birds)
  2. INTERNAL IMAGERY â€” Recurring motifs (seeing falsely, imprisonment)

EXAMPLES:
  - LES DIABOLIQUES: Water motifs â†’ Death/terror
  - CASABLANCA: Bars/shadows â†’ Imprisonment; Rick â†’ America
  - CHINATOWN: Eyes/seeing â†’ Blind seeing; water vs drought
  
TECHNIQUE: Repeat and intensify through story.
           Climax gathers and releases image power.
```

---

## 22. A Writer's Method

### 22.1 Inside-Out vs. Outside-In

```
OUTSIDE-IN (avoid):
  1. Screenwriter writes dialogue first
  2. Searches for scenes through dialogue
  3. Searches for story through scenes
  - Slow, traps creativity, produces weak work
  
INSIDE-OUT (recommended):
  1. Create step-outline first (no dialogue)
  2. Expand to treatment (no dialogue)
  3. Add dialogue last
  - Faster, frees creativity, produces strong work

PRINCIPLE: "The premature writing of dialogue chokes creativity."
           Once you love your dialogue, you won't change events.
```

### 22.2 Step-Outline Phase

```python
def create_step_outline():
    """4+ months of a 6-month screenplay"""
    
    # Use index cards â€” one per scene
    cards = []
    
    for scene in imagined_scenes:
        card = Card(
            front=describe_scene_in_1_2_sentences(),
            # "He enters expecting to find her, discovers note saying she's left"
            back=indicate_structural_function()
            # "Inciting Incident" or "Act Two Climax"
        )
        cards.append(card)
    
    # Create stacks by act
    act_stacks = organize_by_act(cards)
    
    # DESTROY freely at this stage
    # 90% of everything is mediocre
    # Trash anything less than best
    
    # Discover Story Climax
    story_climax = discover_climax()
    
    # Rework backward from climax
    for act in reversed(story.acts):
        ensure_builds_to_climax(act, story_climax)
    
    return step_outline
```

### 22.3 The Pitch Test

```
PITCH_TEST:
  When step-outline is complete, PITCH the story.
  
  1. Don't show the outline (too cryptic for others)
  2. Tell the story aloud in 10 minutes
  3. Watch listener's eyes:
     - Hooked at Inciting Incident?
     - Leaning in through progressions?
     - Strong emotional reaction at Climax?
  
  "Any story pitched from its step-outline to an intelligent,
   sensitive person must be able to grab attention, hold interest
   for ten minutes, and pay it off by moving them to a meaningful,
   emotional experience."
  
  If pitch doesn't work, story won't work.
  Fix it in outline, not in screenplay.
```

### 22.4 Treatment Phase

```
TREATMENT: Expand step-outline to 60-90 pages.
           Moment-by-moment description.
           NO DIALOGUE YET.

INCLUDE:
  - Present-tense action description
  - Subtext (what characters think and feel)
  - Indicate what characters talk ABOUT (not actual words)

PURPOSE:
  - Discover if outline scenes actually work
  - Create rich subtext before dialogue
  - Build material to draw screenplay from
  
STUDIO_ERA: Treatments were 200-300 pages
            "Extract screenplay from larger work"
```

### 22.5 Screenplay Phase

```
SCREENPLAY_PHASE:
  - Now convert treatment to screen description
  - NOW add dialogue
  
BENEFIT: "Dialogue written at this point is invariably 
         the finest dialogue we've ever written."
         Characters have been silent so long, they're 
         bursting to speak.
         
REVISION: Still needed, but changes are refinements,
          not structural overhauls.

"Until you have a step-outline that pitches brilliantly,
 there's no point going forward."
```

---

## 23. Quick Reference Card

### Scene Validity Test
```
IF opening_value == closing_value: DELETE SCENE
```

### Gap Formula
```
ACTION â†’ EXPECTATION â†’ RESULT â‰  EXPECTATION â†’ ESCALATE â†’ REPEAT
```

### Unity Test
```
"Because of the Inciting Incident, the Climax HAD to happen."
```

### Risk Test
```
IF failure_consequence == "return_to_normal": STORY NOT WORTH TELLING
```

### Controlling Idea Template
```
"[VALUE] is [achieved/lost] because [CAUSE]"
```

### Value Progression
```
POSITIVE â†’ CONTRARY â†’ CONTRADICTORY â†’ NEGATION OF NEGATION
```

### Crisis Dilemma Types
```
1. Irreconcilable goods
2. Lesser of two evils
3. Both simultaneously
```

### Exposition Rule
```
Convert exposition to AMMUNITION in present conflict.
Never tell unless missing fact causes confusion.
```

### Character Formula
```
CHARACTERIZATION (observable) â‰  TRUE CHARACTER (revealed under pressure)
DIMENSION = CONTRADICTION between mask and nature
```

### Antagonism Principle
```
Protagonist strength â‰¤ Total forces of antagonism
(but victory must be possible)
```

### Dialogue Priority
```
1. Can scene be purely visual? â†’ Do that.
2. Must have dialogue? â†’ Add LAST, keep LEAN.
```

### Writing Method
```
STEP-OUTLINE (months) â†’ TREATMENT (weeks) â†’ SCREENPLAY (days)
Never write dialogue until structure is locked.
```

### Coincidence Rules
```
âœ“ Use early to start complications
âœ— Don't use beyond midpoint
âœ— NEVER use to turn ending (deus ex machina)
```

### Center of Good
```
Audience seeks positive identification.
Protagonist needs at least one admirable quality
that shines against surrounding negativity.
```

---

## Appendix: Chapter Cross-Reference

| Chapter | Key Principles |
|---------|----------------|
| 1. The Story Problem | Art vs. Craft; Story as universal form |
| 2. Structure Spectrum | Story Triangle; Archplot/Miniplot/Antiplot |
| 3. Structure & Setting | Creative Limitation; Research methods; ClichÃ© war |
| 4. Structure & Genre | 25 genres; Conventions; Evolution; Comedy |
| 5. Structure & Character | Character vs. Characterization; Arc; Dimension |
| 6. Structure & Meaning | Controlling Idea; Idealist/Pessimist/Ironist |
| 7. Substance of Story | Story Events; Law of Conflict |
| 8. The Inciting Incident | Requirements; Timing; Spine creation |
| 9. Act Design | Proportions; Subplots; False endings |
| 10. Scene Design | Beats; Turning Points; Text/Subtext |
| 11. Scene Analysis | Five-step technique; Beat breakdown |
| 12. Composition | Unity; Pacing; Progressions; Transitions |
| 13. Crisis, Climax, Resolution | Dilemma types; Placement; Resolution purposes |
| 14. Principle of Antagonism | Underdog requirement; Negation of Negation |
| 15. Exposition | Two Laws; Dramatization; Flashback; Delivery methods |
| 16. Problems & Solutions | Interest; Mystery/Suspense/Irony; Coincidence; Melodrama |
| 17. Character | Dimension; Cast design; Comic character; Tips |
| 18. The Text | Dialogue principles; Suspense sentence; Description; Image Systems |
| 19. A Writer's Method | Inside-out; Step-outline; Treatment; Pitch test |

## 24. Diagnostic Questions

1. **Does every scene contain a value turn (opening value != closing value)?** (YES)
2. **Is there a clear 'Gap' between character expectation and world response?** (YES)
3. **Does the character's choice under pressure contradict their surface characterization?** (YES)
4. **Do the forces of antagonism equal or exceed the protagonist's capacities?** (YES)
5. **Is the climax a true dilemma between irreconcilable goods or lesser evils?** (YES)
6. **Is exposition converted into ammunition in present conflict?** (YES)

---

*Document generated from Robert McKee's "Story: Substance, Structure, Style, and the Principles of Screenwriting" (1997). All principles extracted and formalized for practical narrative construction.*
