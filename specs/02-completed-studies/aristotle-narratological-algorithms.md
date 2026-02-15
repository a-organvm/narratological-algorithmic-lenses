# Aristotle's Narratological Algorithms

A systematic distillation of Aristotle's *Poetics* (~335 BCE) into formal, implementable principles for narrative construction. Based on the S. H. Butcher translation.

---

## 0. Meta-Principles (Axioms)

Aristotle's *Poetics* operates from first principles about the nature of art, imitation, and human psychology.

| Axiom | Formulation |
|-------|-------------|
| A0 | All art is **imitation** (mimesis)â€”poetry imitates action, character, and thought |
| A1 | Imitation is **natural** to humans; we learn through imitation and take pleasure in recognizing representations |
| A2 | Poetry is **more philosophical than history**â€”it expresses the universal, not merely the particular |
| A3 | The **probable impossible** is preferable to the **improbable possible** |
| A4 | Everything must follow from **necessity or probability**; nothing should happen by chance |
| A5 | The standard of correctness **differs** between poetry and other arts (politics, medicine, etc.) |

### 0.1 The Pleasure of Recognition

```
GIVEN:
  - humans have natural imitative instinct
  - humans take pleasure in learning
  
WHEN:
  viewer encounters representation R of reality X
  
THEN:
  IF viewer recognizes X in R:
    pleasure = learning_pleasure + craft_pleasure
  ELSE:
    pleasure = execution_pleasure_only (color, technique)
    
THEREFORE:
  recognition is primary source of aesthetic pleasure
```

### 0.2 The Three Objects of Imitation

```
POET_MUST_IMITATE_ONE_OF_THREE:
  1. things as they WERE or ARE (historical/actual)
  2. things as they are SAID or THOUGHT to be (traditional/received)
  3. things as they OUGHT to be (ideal/normative)

DEFENSE_APPLICATIONS:
  IF criticism = "not true to fact":
    RESPOND: "objects are as they OUGHT to be" (Sophocles' method)
    OR: "this is how men SAY the thing is" (traditional defense)
    OR: "still, it WAS the fact" (historical defense)
```

---

## 1. Taxonomy of Imitative Arts

Arts differ along three dimensions: **medium**, **object**, and **manner**.

### 1.1 Medium (What Is Used to Imitate)

| Medium | Arts |
|--------|------|
| Rhythm alone | Dance |
| Harmony + Rhythm | Music (flute, lyre) |
| Language alone | Poetry, prose narrative |
| Language + Harmony + Rhythm | Tragedy, Comedy, Dithyramb |

### 1.2 Object (What Is Imitated)

```
object_of_imitation = {
  BETTER_THAN_REALITY:   Tragedy, Epic, Noble Painting (Polygnotus)
  AS_THEY_ARE:           Realistic portraiture (Dionysius), Cleophon
  WORSE_THAN_REALITY:    Comedy, Parody, Caricature (Pauson)
}

RULE: Tragedy imitates persons BETTER than average
      Comedy imitates persons WORSE than average
      
CONSTRAINT: "Worse" in comedy means the LUDICROUS
            = defect or ugliness WITHOUT pain or destruction
```

### 1.3 Manner (How Imitation Is Presented)

| Manner | Description | Example |
|--------|-------------|---------|
| Narrative (author's voice) | Poet speaks as self | Lyric poetry |
| Narrative (assumed voice) | Poet speaks as character | Epic (Homer) |
| Dramatic | Characters act directly | Tragedy, Comedy |

---

## 2. The Definition of Tragedy (Canonical Formulation)

> "Tragedy, then, is an imitation of an action that is serious, complete, and of a certain magnitude; in language embellished with each kind of artistic ornament, the several kinds being found in separate parts of the play; in the form of action, not of narrative; through pity and fear effecting the proper purgation of these emotions."

The highest level of structural organization is the **TRAGEDY**.

### 2.1 Decomposition

```
TRAGEDY = {
  OBJECT:     action that is serious, complete, of magnitude
  MEDIUM:     embellished language (rhythm, harmony, song)
  MANNER:     dramatic (not narrative)
  EFFECT:     catharsis of pity and fear
}
```

### 2.2 The Six Constituent Elements

Ordered by importance (descending):

| Rank | Element | Definition | Category |
|------|---------|------------|----------|
| 1 | **Plot** (mythos) | Arrangement of incidents | Object |
| 2 | **Character** (ethos) | That by which we ascribe qualities to agents | Object |
| 3 | **Thought** (dianoia) | Proof, general truths, arguments | Object |
| 4 | **Diction** (lexis) | Expression of meaning in words | Medium |
| 5 | **Song** (melos) | Musical composition | Medium |
| 6 | **Spectacle** (opsis) | Visual staging | Manner |

### 2.3 The Primacy of Plot

```
AXIOM: Plot is the SOUL of tragedy

PROOF:
  1. Tragedy imitates ACTION, not persons
  2. Life consists in action; end is a mode of action
  3. Character determines quality; action determines happiness
  4. Without action â†’ no tragedy
  5. Without character â†’ tragedy possible (though inferior)
  
THEREFORE:
  plot > character > thought > diction > song > spectacle
  
COROLLARY:
  Spectacle is "least artistic" and "connected least with the art of poetry"
  Power of tragedy felt even WITHOUT representation and actors
  
PAINTING_ANALOGY:
  "The most beautiful colors, laid on confusedly, will not give 
   as much pleasure as the chalk outline of a portrait."
```

### 2.4 Thought vs. Character (Distinction)

```
CHARACTER (ethos):
  - reveals MORAL PURPOSE
  - shows what a person CHOOSES or AVOIDS
  - speeches without choice/avoidance = NOT expressive of character

THOUGHT (dianoia):
  - proves something IS or IS NOT
  - enunciates GENERAL MAXIMS
  - function of political art and rhetoric
  
RULE:
  IF speech.reveals_moral_choice():
    category = CHARACTER
  ELIF speech.proves_or_generalizes():
    category = THOUGHT
```

---

## 3. Plot Structure (The Core Algorithm)

### 3.1 Completeness and Unity

The primary unit of structure is the **WHOLE**, consisting of a Beginning, Middle, and End.

```
DEFINITION: A WHOLE has:
  - BEGINNING: does not follow from prior cause, but causes what follows
  - MIDDLE: follows from something AND causes something else
  - END: follows from prior cause, but nothing follows it

RULE: Plot must neither begin nor end "at haphazard"

UNITY TEST:
  IF any_part.is_displaced() OR any_part.is_removed():
    IF whole.is_disturbed():
      part = ORGANIC (essential)
    ELSE:
      part = INORGANIC (delete it)
```

### 3.2 The Unity Principle

```
WRONG: Unity of plot = unity of hero
       (infinitely various incidents in one man's life 
        cannot be reduced to unity)

RIGHT: Unity of plot = unity of ACTION
       - one action, whole and complete
       - structural union of parts
       
HOMER'S METHOD (exemplar):
  - Did NOT include all adventures of Odysseus
  - Made Odyssey CENTER on ONE action
  - Excluded incidents with no necessary/probable connection
```

### 3.3 Magnitude (Proper Length)

```
CONSTRAINT: length that can be "easily embraced by memory"

LOWER_BOUND: sufficient for change from fortune to misfortune
             OR from misfortune to fortune
             (following probability/necessity)

UPPER_BOUND: the whole must be "perspicuous" (graspable)

FORMULA:
  proper_magnitude = min(length) WHERE:
    sequence_of_events BY probability OR necessity
    ADMITS change(fortune) from goodâ†’bad OR badâ†’good
    
NOTE: "The greater the length, the more beautiful...
       provided that the whole be perspicuous"

ORGANISM_ANALOGY:
  - Too small: "view is confused, seen in imperceptible moment"
  - Too vast: "unity and sense of whole is lost"
  - Like animal: certain magnitude necessary, easily embraced in one view
```

### 3.4 Probability and Necessity

```
MASTER_RULE:
  EVERY event must follow by NECESSITY or PROBABILITY
  
def validate_sequence(event_a, event_b):
    if event_b.follows_necessarily_from(event_a):
        return VALID
    if event_b.follows_probably_from(event_a):
        return VALID
    return INVALID  # episodic, worst kind of plot
    
DISTINCTION:
  propter_hoc (because of this) â†’ VALID
  post_hoc (after this) â†’ INVALID
```

### 3.5 The Episodic Plot (Anti-Pattern)

```
DEFINITION: 
  episodic_plot = episodes succeed without probable/necessary sequence

VERDICT: "Of all plots and actions the episodic are the WORST"

CAUSES:
  - Bad poets: by their own fault
  - Good poets: to please actors, stretch plot beyond capacity
```

### 3.6 Surprise Within Causation

```
RULE: 
  tragic wonder = surprise + causation COMBINED
  
PRINCIPLE:
  "The effect is heightened when, at the same time, 
   they follow as cause and effect."
   
EXAMPLE (Statue of Mitys):
  - Statue fell upon murderer at festival
  - Killed him
  - Seems NOT due to mere chance (designed coincidence)
  
FORMULA:
  best_events = surprising AND causally connected
  
  IF event.is_surprising AND event.follows_causally:
    tragic_wonder = MAXIMUM
  ELIF event.follows_causally:
    tragic_effect = GOOD
  ELIF event.is_random:
    tragic_effect = WEAK
```

---

## 4. Simple vs. Complex Plots

Each plot is composed of several **PLOT_ELEMENT** units.

### 4.1 Definitions

```
SIMPLE_PLOT:
  change_of_fortune occurs
  WITHOUT reversal
  WITHOUT recognition
  
COMPLEX_PLOT:
  change_of_fortune accompanied by:
    REVERSAL (peripeteia) AND/OR
    RECOGNITION (anagnorisis)
    
CONSTRAINT:
  Reversal and Recognition must arise from INTERNAL STRUCTURE
  Must be necessary or probable result of preceding action
  
PREFERENCE:
  "A perfect tragedy should be arranged not on the simple 
   but on the complex plan."
```

### 4.2 Reversal (Peripeteia)

```
DEFINITION:
  reversal = change by which action VEERS TO OPPOSITE
             subject to probability/necessity
             
PARADIGM (Oedipus):
  INPUT:  Messenger comes to FREE Oedipus from fear about mother
  ACTION: Reveals who Oedipus is
  OUTPUT: PRODUCES OPPOSITE EFFECT (confirms fear)
  
TEMPLATE:
def reversal(intended_outcome, action):
    actual_outcome = action.execute()
    assert actual_outcome == opposite(intended_outcome)
    assert actual_outcome.follows_probably_from(action)
    return actual_outcome
```

### 4.3 Recognition (Anagnorisis)

```
DEFINITION:
  recognition = change from IGNORANCE to KNOWLEDGE
                producing LOVE or HATE
                between persons destined for fortune/misfortune

BEST_FORM:
  recognition COINCIDENT with reversal (e.g., Oedipus)
  
TYPES (ranked by artistry, worst to best):
  1. BY SIGNS (birthmarks, tokens) - least artistic
  2. BY POET'S INVENTION (forced, unmotivated) - unartistic
  3. BY MEMORY (sight awakens feeling) - better
  4. BY REASONING (inference, deduction) - good
  5. FROM INCIDENTS THEMSELVES (natural, surprising) - BEST
  
RULE:
  recognition_quality âˆ integration_with_plot
  
BEST_RECOGNITION:
  "Dispenses with artificial aid of tokens or amulets"
  Arises naturally from the incidents (e.g., Iphigenia's letter)
```

### 4.4 Scene of Suffering (Pathos)

```
DEFINITION:
  pathos = destructive or painful action
           (death, bodily agony, wounds, etc.)
           
POSITION: Third part of plot after Reversal and Recognition
```

---

## 5. The Tragic Effect Algorithm

### 5.1 Catharsis

```
GOAL: effect CATHARSIS (purgation) of PITY and FEAR

def generate_tragic_effect(plot):
    pity = aroused_by(unmerited_misfortune)
    fear = aroused_by(misfortune_of_someone_like_us)
    
    if plot.produces(pity) AND plot.produces(fear):
        return CATHARSIS
    else:
        return FAILURE
        
PROPER_PLEASURE:
  "The pleasure which the poet should afford is that which 
   comes from pity and fear THROUGH IMITATION"
```

### 5.2 The Proper Tragic Character

```
REJECTED CONFIGURATIONS:

1. virtuous_person: prosperity â†’ adversity
   RESULT: shocks us, neither pity nor fear
   
2. bad_person: adversity â†’ prosperity  
   RESULT: nothing tragic, no pity, no fear, morally repugnant
   
3. utter_villain: prosperity â†’ adversity
   RESULT: satisfies moral sense, but no pity/fear

CORRECT CONFIGURATION:
  character = {
    not_eminently_good: true,
    not_eminently_just: true,
    not_depraved: true,
    not_vicious: true,
    renowned: true,
    prosperous: true,
    falls_by_HAMARTIA: true  # error or frailty, NOT vice
  }
  
  change = good_fortune â†’ bad_fortune
  cause = great_error_or_frailty (not vice)
```

### 5.3 The Hamartia Principle

```
DEFINITION:
  hamartia = error, mistake, miscalculation
             NOT moral depravity
             NOT wickedness
             
FUNCTION:
  hamartia makes fall PITIFUL (unmerited in intention)
  hamartia makes fall FEARFUL (could happen to us)
  
PARADIGM: Oedipus, Thyestes, other "illustrious men"
```

### 5.4 The Relationship Proximity Rule

```
RULE: Suffering between INTIMATES generates maximum pity

RELATIONSHIP_MATRIX:
  IF killer AND victim are ENEMIES:
    pity = NONE (except for suffering itself)
    
  IF killer AND victim are STRANGERS:
    pity = NONE
    
  IF killer AND victim are NEAR/DEAR:
    pity = MAXIMUM
    
MOST_EFFECTIVE_SITUATIONS:
  - Brother kills/intends to kill brother
  - Son kills father
  - Mother kills son
  - Son kills mother
  
NOTE: "These are the situations to be looked for by the poet"
```

### 5.5 Best Sources of Fear and Pity

```
RULE: Fear and pity BEST arise from STRUCTURE OF PLOT
      NOT from spectacular effects (inferior method)
      
TEST:
  if HEARING_ONLY(tale) produces thrill_of_horror AND melt_to_pity:
    plot = SUCCESSFUL
    
THE MONSTROUS vs. THE TERRIBLE:
  spectacle â†’ creates sense of MONSTROUS (not tragic)
  plot_structure â†’ creates sense of TERRIBLE (truly tragic)
  
  "Those who employ spectacular means to create a sense 
   not of the terrible but only of the monstrous, 
   are strangers to the purpose of Tragedy."
```

### 5.6 The Four Tragic Scenarios (Ranked)

```
FOUR SCENARIOS (ranked):
  1. WORST: Know person, intend deed, don't act
     (shocking without tragicâ€”no disaster follows)
     EXAMPLE: Haemon threatens Creon in Antigone
     
  2. BETTER: Deed done with knowledge
     (tragic, but lacks surprise)
     EXAMPLE: Medea slays children knowingly
     
  3. BETTER STILL: Deed done in ignorance, discovered after
     (nothing to shock, discovery is striking)
     EXAMPLE: Oedipus
     
  4. BEST: About to act in ignorance, RECOGNIZE before deed
     (maximum tension, no pollution)
     EXAMPLES: 
       - Merope about to slay son, recognizes him
       - Iphigenia recognizes brother just in time
```

---

## 6. Character Rules

### 6.1 Four Requirements for Character

```
CHARACTER_REQUIREMENTS = [
    {
        "name": "GOODNESS",
        "priority": 1,  # most important
        "rule": "Purpose must be good",
        "note": "Good is relative to classâ€”even slave can be good"
    },
    {
        "name": "PROPRIETY", 
        "priority": 2,
        "rule": "Character must be appropriate to type",
        "example": "Valor inappropriate for woman in Aristotle's view"
    },
    {
        "name": "TRUE TO LIFE",
        "priority": 3,
        "rule": "Character must be realistic/believable",
        "distinct_from": "goodness and propriety"
    },
    {
        "name": "CONSISTENCY",
        "priority": 4,
        "rule": "Even if inconsistent, be CONSISTENTLY inconsistent",
        "example": "Iphigenia suppliant â‰  Iphigenia later (violation)"
    }
]
```

### 6.2 Character-Action Binding

```
RULE:
  character.speech AND character.action MUST follow
  BY necessity OR probability FROM character's nature
  
def validate_character_action(character, action):
    if action.follows_necessarily_from(character.nature):
        return VALID
    if action.follows_probably_from(character.nature):
        return VALID
    return INCONSISTENT
```

### 6.3 The Deus Ex Machina Prohibition

```
RULE: Unraveling MUST arise from PLOT ITSELF

PROHIBITED:
  deus_ex_machina for resolving action
  
PERMITTED:
  deus_ex_machina for:
    - antecedent events (before play)
    - subsequent events (after play)
    - things beyond human knowledge
    - prophecy and foretelling
    
EXAMPLE_VIOLATION: Medea's chariot escape

COROLLARY:
  "Within the action there must be nothing IRRATIONAL"
  If irrational unavoidable â†’ place OUTSIDE tragedy scope
```

### 6.4 Character Elevation

```
RULE: Tragedy imitates persons BETTER than ordinary
      Like good portrait painters who:
        - Reproduce distinctive form
        - Make likeness TRUE to life
        - Yet make it MORE BEAUTIFUL
        
APPLICATION:
  when representing defective characters:
    preserve_type(character)
    ennoble(character)
    
PARADIGM: Achilles portrayed by Homer and Agathon

SOPHOCLES_PRINCIPLE:
  "Sophocles said that he drew men as they OUGHT to be;
   Euripides, as they ARE."
```

---

## 7. Structural Components

Dramatic structure also includes **QUANTITATIVE_PART** divisions.

### 7.1 Quantitative Parts of Tragedy

```
PARTS = {
    "Prologue":   "Part before Parode of Chorus",
    "Episode":    "Part between complete choric songs",
    "Exode":      "Part with no choric song after it",
    "Parode":     "First undivided utterance of Chorus",
    "Stasimon":   "Choric ode without anapaests/trochaic tetrameters",
    "Commos":     "Joint lamentation of Chorus and actors"
}
```

### 7.2 Complication and Unraveling

```
STRUCTURE:
  tragedy = COMPLICATION + UNRAVELING (denouement)
  
COMPLICATION:
  - extends from BEGINNING to TURNING POINT
  - includes incidents extraneous to action
  - includes portion of action proper
  
UNRAVELING:
  - extends from TURNING POINT to END
  - the "change" to good or bad fortune
  
TEST:
  tragedy_A == tragedy_B IF AND ONLY IF:
    complication_A == complication_B AND
    unraveling_A == unraveling_B
    
WARNING:
  "Many poets tie the knot well, but unravel it ill.
   Both arts should always be mastered."
```

### 7.3 Four Kinds of Tragedy

| Type | Primary Element | Example |
|------|-----------------|---------|
| **Complex** | Reversal + Recognition | Oedipus |
| **Pathetic** | Suffering/Passion | Ajax, Ixion |
| **Ethical** | Moral character | Phthiotides, Peleus |
| **Simple** | Spectacle/Setting | Prometheus, Hades scenes |

```
GOAL: Combine ALL elements if possible
      OR the greatest number and most important
```

---

## 8. Epic vs. Tragedy

### 8.1 Similarities

```
SHARED:
  - imitation in verse of higher types
  - same constituent elements (plot, character, thought, diction)
  - requirements for good plot apply equally
  - must be simple, complex, ethical, or pathetic
  - requires reversals, recognitions, scenes of suffering
```

### 8.2 Differences

| Property | Tragedy | Epic |
|----------|---------|------|
| Meter | Various (iambic primarily) | Hexameter only |
| Manner | Dramatic | Narrative |
| Length | Single revolution of sun (roughly) | No time limit |
| Unity | Stricter (single action) | Looser (multiple episodes) |
| Effect | Concentrated, more pleasurable | Diluted over length |
| Simultaneity | Single line of action | Multiple parallel actions |

### 8.3 Epic's Unique Capabilities

```
SIMULTANEITY_ADVANTAGE:
  TRAGEDY: cannot imitate several lines of action at same time
           confined to action on stage
           
  EPIC: many events simultaneously transacted can be presented
        adds mass and dignity
        diverts mind, relieves story with varying episodes
        
ANTI-SATIETY PRINCIPLE:
  "Sameness of incident soon produces satiety,
   and makes tragedies fail on the stage."
   
  Epic episodes â†’ prevent satiety through variety
```

### 8.4 The Marvelous in Epic

```
EPIC ADVANTAGE: 
  marvelous is easier in narrative
  (audience doesn't see, so implausibility hidden)
  
TRAGEDY CONSTRAINT:
  irrational exposed on stage
  
EPIC PERMISSION:
  irrational adds wonder
  the "marvelous" is pleasing
  
EXAMPLE:
  "The pursuit of Hector would be LUDICROUS if placed upon the stageâ€”
   the Greeks standing still and not joining in the pursuit,
   and Achilles waving them back.
   But in the Epic poem the absurdity passes unnoticed."
```

### 8.5 Homer's Authorial Restraint

```
RULE:
  "The poet should speak as little as possible in his own person,
   for it is NOT THIS that makes him an imitator."
   
HOMER'S METHOD:
  - "After a few prefatory words, at once brings in a man, 
     or woman, or other personage"
  - None wanting in characteristic qualities
  - Each with a character of his own
  
ANTI-PATTERN:
  "Other poets appear themselves upon the scene throughout,
   and imitate but little and rarely."
```

### 8.6 The Art of Skillful Lies

```
HOMER'S_TECHNIQUE:
  "Homer has chiefly taught other poets the art of 
   telling lies skilfully."
   
THE_FALLACY:
  GIVEN: If A exists, then B exists
  AUDIENCE assumes: If B exists, then A exists
  BUT: This is FALSE INFERENCE
  
APPLICATION:
  - First thing (A) may be untrue
  - Second thing (B) is true
  - Mind, knowing B true, falsely infers A true
  - No need to prove A if B is convincingly true
  
EXAMPLE: The Bath Scene in the Odyssey
```

---

## 9. Diction and Style

### 9.1 Style Principles

```
GOAL: Clear without being MEAN (commonplace)

def evaluate_style(text):
    if uses_only_current_words(text):
        return CLEAR but MEAN
    if uses_only_strange_words(text):
        return JARGON or RIDDLE
    return optimal_mix(current, strange, metaphorical, ornamental)
    
FORMULA:
  perfect_style = clarity + elevation
  clarity â† current/proper words
  elevation â† unusual words, metaphors, ornaments
  
MODERATION_RULE:
  "In any mode of poetic diction there must be moderation.
   Even metaphors... would produce the like effect 
   if used without propriety."
```

### 9.2 Types of Words

| Type | Definition |
|------|------------|
| **Current** | In general use among people |
| **Strange** | In use in another country |
| **Metaphorical** | Application of alien name by transference |
| **Ornamental** | Added for beauty |
| **Newly-coined** | Invented by poet |
| **Lengthened** | Vowel extended or syllable added |
| **Contracted** | Part removed |
| **Altered** | Part unchanged, part recast |

### 9.3 Metaphor (Central to Diction)

```
DEFINITION:
  metaphor = application of ALIEN name by TRANSFERENCE
  
TYPES:
  1. Genus â†’ Species: "There lies my ship" (lying at anchor is species of lying)
  2. Species â†’ Genus: "Ten thousand deeds" (ten thousand = species of "many")
  3. Species â†’ Species: "Drew away life" / "Cleft water" (both species of taking away)
  4. ANALOGY: A:B :: C:D â†’ use D for B or B for D
  
ANALOGY_EXAMPLE:
  cup : Dionysus :: shield : Ares
  âˆ´ cup = "shield of Dionysus"
  âˆ´ shield = "cup of Ares"
  
HIGHEST_FORM:
  "The greatest thing by far is to have a command of metaphor.
   This alone cannot be imparted by another; 
   it is the mark of genius,
   for to make good metaphors implies an eye for resemblances."
```

### 9.4 Genre-Appropriate Diction

```
WORD_TYPE_BY_GENRE:
  DITHYRAMB:    compound words best adapted
  HEROIC/EPIC:  rare/strange words most appropriate
  IAMBIC:       metaphors most suitable
  
IAMBIC_PRINCIPLE:
  "Iambic verse reproduces, as far as may be, familiar speech"
  Most appropriate words: current, proper, metaphorical, ornamental
```

### 9.5 The Diction-Action Separation Rule

```
RULE:
  "The diction should be elaborated in the PAUSES of the action,
   where there is no expression of character or thought."
   
COROLLARY:
  "Character and thought are merely OBSCURED 
   by a diction that is over-brilliant."
   
APPLICATION:
  DURING character/thought expression â†’ simple diction
  DURING pauses/transitions â†’ elaborate diction permitted
```

---

## 10. Probability and the Impossible

### 10.1 The Core Principle

```
HIERARCHY:
  probable_impossibility > improbable_possibility
  
EXPLANATION:
  - A probable impossibility maintains internal logic
  - An improbable possibility breaks believability
  
RULE:
  "With respect to the requirements of art,
   a probable impossibility is to be preferred
   to a thing improbable and yet possible."
```

### 10.2 Justifying the Irrational

```
VALID_JUSTIFICATIONS = [
    "artistic_requirements",    # the art demands it
    "higher_reality",          # represents the ideal
    "received_opinion",        # people believe it
    "poetic_tradition"         # how things are said to be
]

DEFENSE_ARGUMENT:
  "The impossible is the higher thing;
   for the ideal type must surpass reality."
  
ZEUXIS_EXAMPLE:
  "Impossible that men exist as Zeuxis painted.
   Yes, but the impossible is higherâ€”ideal must surpass real."
```

### 10.3 Handling the Irrational

```
RULE:
  "Everything irrational should, if possible, be EXCLUDED"
  
IF irrational UNAVOIDABLE:
  place OUTSIDE the action of the play
  
EXAMPLES:
  ACCEPTABLE: Oedipus' ignorance of Laius' death manner (outside play)
  PROBLEMATIC: Messenger's account of Pythian games in Electra (within)
  
ONCE_INTRODUCED:
  "Once the irrational has been introduced and an air of 
   likelihood imparted to it, we must accept it in spite 
   of the absurdity."
   
HOMER'S_SKILL:
  "The absurdity is veiled by the poetic charm 
   with which the poet invests it."
```

### 10.4 Essential vs. Accidental Errors

```
TWO_KINDS_OF_FAULTS:
  1. ESSENTIAL: errors touching poetry's essence
     - poet chose to imitate but imitated INCORRECTLY
     - error inherent in the poetry itself
     
  2. ACCIDENTAL: errors touching incidentals
     - wrong choice of subject matter
     - technical inaccuracies (medicine, etc.)
     - not essential to poetry
     
JUDGMENT:
  "Not to know that a hind has no horns is a LESS serious matter
   than to paint it inartistically."
   
  technical_error < artistic_error
```

### 10.5 Sources of Critical Objection

```
CRITICISM_TYPES = [
    "impossible",
    "irrational", 
    "morally_hurtful",
    "contradictory",
    "contrary_to_artistic_correctness"
]

RESPONSE_METHOD:
  examine by dialectical rules:
    - same_thing_meant?
    - same_relation?
    - same_sense?
  resolve by reference to:
    - what poet says
    - what person of intelligence would assume
    
CONTEXTUAL_EVALUATION:
  "We must consider BY WHOM it is said or done, TO WHOM, 
   WHEN, BY WHAT MEANS, or FOR WHAT END;
   whether, for instance, it be to secure a greater good,
   or avert a greater evil."
```

---

## 11. The Construction Method

### 11.1 Visualization Principle

```
RULE:
  "In constructing the plot... the poet should place 
   the scene AS FAR AS POSSIBLE before his eyes."
   
RATIONALE:
  - seeing everything with utmost VIVIDNESS
  - as if SPECTATOR of the action
  - will discover what is in KEEPING
  - most unlikely to overlook INCONSISTENCIES
  
EMBODIMENT_PRINCIPLE:
  "The poet should work out his play, to the best of his power,
   with appropriate gestures; for those who feel emotion are 
   most convincing through natural sympathy with the characters."
   
  "One who is agitated storms, one who is angry rages,
   with the most lifelike reality."
```

### 11.2 The Sketch-First Method

```
def construct_tragedy(source_material):
    # STEP 1: General outline (regardless of traditional/invented)
    outline = sketch_general_plan(source_material)
    
    # STEP 2: Fill in episodes
    episodes = develop_episodes(outline)
    
    # STEP 3: Verify relevance
    for episode in episodes:
        assert episode.is_relevant_to(outline.action)
    
    # STEP 4: Assign names
    assign_characteristic_names(episodes)
    
    return complete_tragedy
```

### 11.3 The Odyssey Outline (Example)

```
GENERAL_PLAN = """
A certain man is absent from home for many years.
He is jealously watched by Poseidon and left desolate.
Meanwhile his home is in wretched plight:
  - suitors waste his substance
  - suitors plot against his son
At length, tempest-tost, he arrives.
He makes certain persons acquainted with him.
He attacks the suitors with his own hand.
He is preserved while he destroys them.
"""

NOTE: "This is the essence of the plot; the rest is episode."
```

### 11.4 The Poet's Nature

```
TWO_TYPES_OF_POETIC_GIFT:
  1. HAPPY_GIFT_OF_NATURE: can take the mould of any character
  2. STRAIN_OF_MADNESS: lifted out of proper self
  
  "Hence poetry implies either a happy gift of nature 
   or a strain of madness."
```

---

## 12. The Chorus

```
RULE:
  "The Chorus should be regarded as ONE OF THE ACTORS"
  
REQUIREMENTS:
  - integral part of whole
  - share in ACTION
  - manner of Sophocles (integrated) NOT Euripides (detached)
  
ANTI-PATTERN:
  choral songs as "mere interludes"
  songs pertaining "as little to the subject of the piece
  as to that of any other tragedy"
  
TEST:
  "What difference is there between introducing such choral interludes,
   and transferring a speech, or even a whole act, from one play to another?"
   
AGATHON'S_ERROR:
  First to introduce interlude songs unrelated to plot
```

---

## 13. Superiority of Tragedy

### 13.1 The Argument

```
PROPOSITION: Tragedy > Epic

EVIDENCE:
  1. Tragedy has ALL epic elements
     (may even use epic meter)
  2. Tragedy has music and spectacle AS IMPORTANT ACCESSORIES
     (produce most vivid pleasures)
  3. Tragedy has vividness in reading AND representation
  4. Tragedy attains end within NARROWER LIMITS
     (concentrated effect more pleasurable than diluted)
  5. Tragedy has GREATER UNITY
     (any epic furnishes subjects for SEVERAL tragedies)
  6. Tragedy fulfills specific function BETTER
     (produces proper pleasure more effectively)

CONCLUSION:
  "Tragedy is the higher art, as attaining its end more perfectly."
  
CONCENTRATION_PRINCIPLE:
  "What, for example, would be the effect of the Oedipus of Sophocles,
   if it were cast into a form as long as the Iliad?"
```

---

## 14. Diagnostic Questions

Answer the following questions to validate the dramatic structure:

1. **Does every event follow by necessity or probability?** Confirm causal binding.
2. **If a part is removed, is the whole disturbed?** Verify organic unity.
3. **Does the character's action follow from their nature?** Check character-action binding.
4. **Does the unraveling arise from the plot itself (not a machine)?** Verify resolution integrity.
5. **Is the fall caused by an error (hamartia) rather than vice?** Confirm tragic protagonist logic.
6. **Does the reversal produce the opposite of the intended effect?** Verify peripeteia.
7. **Is the recognition integrated with the incidents of the plot?** Verify anagnorisis.
8. **Is the probable impossible preferred over the improbable possible?** Test for internal logic.
9. **Are characters good, proper, true to life, and consistent?** Check characterization standards.
10. **Does the suffering occur between near or dear ones?** Verify maximum emotional impact.

---

## Appendix A: Quick Reference Card

### The Core Tests

| Test | Condition |
|------|-----------|
| Unity | Displacement/removal of any part disturbs whole |
| Probability | Every event follows by necessity or probability |
| Magnitude | Length allows fortune change while remaining perspicuous |
| Tragic Effect | Produces pity AND fear through plot structure |
| Character | Good, proper, true to life, consistent |
| Relationship | Suffering occurs between intimates |

### The Canonical Tragic Form

```
1. Protagonist: renowned, prosperous, not eminently good/evil
2. Hamartia: great error or frailty (not vice)
3. Change: good fortune â†’ bad fortune
4. Reversal: action veers to opposite
5. Recognition: ignorance â†’ knowledge
6. Catharsis: purgation of pity and fear
```

### The Questions

| Stage | Question |
|-------|----------|
| Event sequence | "Does this follow by necessity or probability?" |
| Part | "If removed, is the whole disturbed?" |
| Character action | "Does this follow from this character's nature?" |
| Resolution | "Does this arise from the plot itself?" |
| Imitation | "Is this as it was, as it's said to be, or as it ought to be?" |
| Error | "Is this essential to poetry or merely accidental?" |
| Overall | "Is the probable impossible or the improbable possible?" |

### The Hierarchy

```
PLOT > CHARACTER > THOUGHT > DICTION > SONG > SPECTACLE

Complex > Simple
Reversal + Recognition > Either alone > Neither
Probable impossibility > Improbable possibility
Structure-generated emotion > Spectacle-generated emotion
Terrible (tragic) > Monstrous (spectacular)
Essential errors > Accidental errors (in severity)
```

### The Three Defenses

```
WHEN CRITICIZED FOR INACCURACY:
  1. "This is as it OUGHT to be" (ideal defense)
  2. "This is as it is SAID to be" (traditional defense)  
  3. "This is as it WAS" (historical defense)
```

---

## Appendix B: Aristotelian Validation Checklist

```python
def validate_tragedy(tragedy):
    checks = [
        # Structural
        ("Has beginning, middle, end", has_complete_structure),
        ("Parts organically necessary", organic_parts_test),
        ("Events follow probability/necessity", causal_chain_test),
        ("Not episodic", not_episodic_test),
        ("Proper magnitude", magnitude_test),
        
        # Plot Type
        ("Complex preferred (reversal + recognition)", complexity_test),
        ("Reversal arises from structure", reversal_integration_test),
        ("Recognition arises from structure", recognition_integration_test),
        ("Surprise combined with causation", surprise_causation_test),
        
        # Tragic Effect
        ("Produces pity", pity_test),
        ("Produces fear", fear_test),
        ("Suffering between intimates", relationship_proximity_test),
        ("Terrible not merely monstrous", terrible_vs_monstrous_test),
        ("Protagonist neither saint nor villain", character_type_test),
        ("Fall from hamartia not vice", hamartia_test),
        
        # Character
        ("Characters good", character_goodness_test),
        ("Characters proper", character_propriety_test),
        ("Characters true to life", character_realism_test),
        ("Characters consistent", character_consistency_test),
        
        # Resolution
        ("No deus ex machina in action", no_deus_test),
        ("Unraveling from plot", unraveling_test),
        ("Irrational outside action", irrational_placement_test),
        
        # Chorus
        ("Chorus integral to action", chorus_integration_test),
        
        # Diction
        ("Elaborate diction in pauses only", diction_placement_test),
        ("Authorial presence minimized", authorial_restraint_test),
    ]
    
    return all(test(tragedy) for name, test in checks)
```

---

## Appendix C: Theoretical Correspondence Table

| Aristotle | McKee | South Park | Waller-Bridge |
|-----------|-------|------------|---------------|
| Probability/Necessity | Cause-effect chains | But/Therefore | Layered causation |
| Reversal (peripeteia) | Gap between expectation/result | Reversal beats | Subversion of expectation |
| Recognition (anagnorisis) | Character revelation under pressure | â€” | Emotional recognition |
| Hamartia | Character flaw driving action | Character blind spots | Fatal flaw activation |
| Unity of action | Spine/through-line | Central dramatic question | Want vs. need unity |
| Catharsis | Emotional release at climax | Lesson/insight | Emotional payoff |
| Magnitude | Proper length for value change | Episode scope | Scene economy |
| Complex > Simple | Gap-driven > linear | Active > passive causation | Multi-layered > single-track |

---

*Compiled from Aristotle. Poetics. Translated by S. H. Butcher. ~335 BCE.*
*Available at: http://classics.mit.edu/Aristotle/poetics.html*
