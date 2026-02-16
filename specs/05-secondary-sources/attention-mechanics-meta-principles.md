# Attention Mechanics: A Cross-Media Meta-Principles Framework

A foundational theoretical document establishing attention as the ur-currency of narrative and formalizing the mechanisms by which different media sustain engagement across time.

**Status**: Meta-theoretical foundation (sits above individual artist/theorist algorithms)

**Dependencies**: Integrates with all narratological algorithm documents; provides unifying theoretical substrate.

---

## Table of Contents

0. [Foundational Axioms](#0-foundational-axioms)
1. [The Attention-Sustenance Problem](#1-the-attention-sustenance-problem)
2. [Medium-Specific Attention Mechanisms](#2-medium-specific-attention-mechanisms)
3. [The Involuntary Response Hierarchy](#3-the-involuntary-response-hierarchy)
4. [Prediction Dynamics: Two Modes](#4-prediction-dynamics-two-modes)
5. [Density and Simultaneity](#5-density-and-simultaneity)
6. [Causal Binding as Attention Glue](#6-causal-binding-as-attention-glue)
7. [Cross-Media Correspondence Tables](#7-cross-media-correspondence-tables)
8. [Diagnostic Protocols](#8-diagnostic-protocols)
9. [Genre as Attention Contract](#9-genre-as-attention-contract)
10. [Theoretical Lineage](#10-theoretical-lineage)
11. [Quick Reference Card](#11-quick-reference-card)

---

## 0. Foundational Axioms

| Axiom | Formulation |
|-------|-------------|
| **ATT-A0** | Attention is the ur-currency of all narrative; it precedes and transcends any specific medium. |
| **ATT-A1** | Every narrative medium evolves mechanisms to solve the same fundamental problem: sustaining engagement through time. |
| **ATT-A2** | Temporal arts must fill time to make time vanish; silence in music = "and then" in narrative = attention collapse. |
| **ATT-A3** | The purest attention mechanisms are those producing involuntary physiological responses. |
| **ATT-A4** | Sustained attention requires either *anticipation-satisfaction cycles* or *prediction-failure-recalibration cycles*; mixing modes requires mastery. |
| **ATT-A5** | As media become more simultaneous, they can pack more attention-sustaining mechanisms per unit time, but each mechanism must remain causally operative. |
| **ATT-A6** | Medium-specific techniques are surface implementations of universal attention constraints. |

### Source Synthesis

The axioms derive from convergent observations across traditions:

> "Conflict is to storytelling what sound is to music. Both story and music are temporal arts, and the single most difficult task of the temporal artist is to hook our interest, hold our uninterrupted concentration, then carry us through time without an awareness of the passage of time."
> â€”Robert McKee, *Story*

> "The very nature of the visual experience in 2001 is to give the viewer an instantaneous, visceral reaction that does notâ€”and should notâ€”require further amplification."
> â€”Stanley Kubrick, *Playboy* interview (1968)

> "If the words 'and then' belong between those beats, you're fucked."
> â€”Trey Parker, NYU lecture (2011)

---

## 1. The Attention-Sustenance Problem

### 1.1 The Universal Constraint

All narrative confronts the same problem: a temporal gap exists between engagement initiation and completion. The audience can disengage at any moment. The author must provide continuous justification for continued attention.

```
ATTENTION_PROBLEM:
  
  INPUT:  Audience with finite attention, competing demands
  OUTPUT: Sustained engagement from OPEN to CLOSE
  
  CONSTRAINT: At every micro-moment t, the audience implicitly asks:
              "Why should I continue rather than disengage?"
  
  SOLUTION:   Provide continuous answer through MECHANISM
```

### 1.2 Historical Universality

The attention economy is not a modern phenomenon:

| Era | Medium | Attention Mechanism |
|-----|--------|---------------------|
| Oral tradition | Spoken narrative | Rhythm, repetition, vocal variation, audience participation |
| Classical theater | Live performance | Spectacle, recognition, catharsis anticipation |
| Print | Prose | Sentence rhythm, semantic gaps, chapter hooks |
| Comics | Sequential art | Panel curiosity, page-turn reveals, closure |
| Cinema | Film | Shot composition, editing rhythm, audio-visual synthesis |
| Television | Serialized video | Episode hooks, season arcs, commercial break structure |
| Interactive | Games/hypertext | Agency, exploration reward, challenge calibration |

### 1.3 The Temporal Binding Problem

```python
def attention_binding(narrative_unit: Unit, duration: Time) -> AttentionState:
    """
    Every narrative must bind attention across temporal gaps.
    The mechanism varies by medium; the problem is invariant.
    """
    
    while not narrative_unit.complete:
        current_moment = get_current_moment()
        
        # The implicit audience question at every moment
        justification = provide_continuation_reason(current_moment)
        
        if justification.strength < DISENGAGEMENT_THRESHOLD:
            return AttentionState.LOST
        
        advance_to_next_moment()
    
    return AttentionState.SUSTAINED
```

---

## 2. Medium-Specific Attention Mechanisms

### 2.1 Mechanism Taxonomy

Each medium has evolved characteristic techniques for attention sustenance:

| Medium | Primary Unit | Micro-Mechanism | Meso-Mechanism | Macro-Mechanism |
|--------|--------------|-----------------|----------------|-----------------|
| **Prose** | Word | Sentence rhythm, word choice | Paragraph tension, scene hook | Chapter cliffhanger, narrative arc |
| **Poetry** | Syllable | Meter, rhyme, enjambment | Stanza structure, volta | Poem arc, sequence structure |
| **Comics** | Panel | Panel composition, gutter | Tier rhythm, page layout | Issue arc, series continuity |
| **Theater** | Moment | Gesture, vocal delivery | Scene tension, act curtain | Play arc, catharsis |
| **Film** | Frame | Shot composition, cut | Sequence tension, scene | Act structure, resolution |
| **Television** | Scene | Scene tension, act-out | Episode arc, cliffhanger | Season arc, series mythology |
| **Animation** | Frame | Frame density, timing | Sequence, musical sync | Episode/film arc |
| **Games** | Input | Feedback loop, reward | Level/quest structure | Campaign/story arc |

### 2.2 The Author's Demand

Different media make different implicit demands on audience participation:

```
MEDIUM_DEMAND_TAXONOMY:

  PROSE:
    demand = "Turn the phrase"
    unit = sentence â†’ paragraph â†’ chapter
    effort = mental construction of image/scene
    reward = semantic completion, imagery, meaning
  
  COMICS:
    demand = "Turn the page"
    unit = panel â†’ tier â†’ page
    effort = closure (filling gutters mentally)
    reward = visual revelation, narrative progression
  
  THEATER:
    demand = "Remain seated"
    unit = moment â†’ scene â†’ act
    effort = sustained imaginative projection
    reward = catharsis, communal experience
  
  FILM:
    demand = "Keep watching"
    unit = frame â†’ shot â†’ sequence
    effort = audio-visual-narrative synthesis
    reward = immersion, emotional transport
  
  ANIMATION:
    demand = "Process parallel streams"
    unit = frame (dense with parallel information)
    effort = simultaneous audio/visual/narrative integration
    reward = aesthetic pleasure, narrative meaning
  
  GAMES:
    demand = "Take action"
    unit = input â†’ feedback â†’ state change
    effort = decision, skill execution
    reward = agency confirmation, mastery feeling
```

### 2.3 The Prose Attention Engine

```
PROSE_MECHANISM:

  SENTENCE_LEVEL:
    - Syntactic tension (delay of main verb/object)
    - Semantic gap (implication, subtext)
    - Rhythm variation (long/short sentence alternation)
    - Sonic texture (consonance, assonance, rhythm)
  
  PARAGRAPH_LEVEL:
    - Opening hook (first sentence carries weight)
    - Development with micro-tension
    - Closing propulsion (drives to next paragraph)
  
  SCENE_LEVEL:
    - Entry at latest possible moment
    - Sustained uncertainty about outcome
    - Exit with question or momentum
  
  CHAPTER_LEVEL:
    - Chapter-end hook (explicit or implicit)
    - Delayed revelation across chapter break
    - Reader's predictive investment
```

### 2.4 The Comics Attention Engine

```
COMICS_MECHANISM:

  PANEL_LEVEL:
    - Composition directs eye
    - Incompleteness demands closure
    - Text/image interplay
  
  TIER_LEVEL:
    - Left-to-right progression with variation
    - Temporal manipulation (moment-to-moment, action-to-action)
    - Panel size/shape as pacing control
  
  PAGE_LEVEL:
    - Page as compositional unit
    - Verso/recto rhythm (odd pages = reveals)
    - Page-turn as dramatic mechanism
  
  ISSUE/CHAPTER_LEVEL:
    - Final page as cliffhanger position
    - Serialization gaps exploited for tension
  
  CLOSURE_TYPES (McCloud):
    - Moment-to-moment: minimal closure, slow time
    - Action-to-action: single subject, moderate closure
    - Subject-to-subject: scene-internal, reader connects
    - Scene-to-scene: deductive leap required
    - Aspect-to-aspect: mood, place, wandering eye
    - Non-sequitur: maximum reader construction
```

### 2.5 The Film/Animation Attention Engine

```
FILM_MECHANISM:

  FRAME_LEVEL:
    - Composition (where eye goes)
    - Information density (empty vs. full frame)
    - Duration (held shot = accumulating attention)
  
  SHOT_LEVEL:
    - Internal movement (choreography)
    - Camera movement (energy transfer)
    - Focal manipulation (attention direction)
  
  CUT_LEVEL:
    - Match cut (smooth attention transfer)
    - Jump cut (attention disruption as signal)
    - Rhythm (cutting pace as emotional control)
  
  SEQUENCE_LEVEL:
    - Scene-level tension (want/obstacle)
    - Sequence question (will X achieve Y?)
  
  AUDIO_LAYER (parallel channel):
    - Dialogue (semantic information)
    - Music (emotional instruction)
    - Sound design (spatial/textural immersion)
    - Silence (attention heightening)

ANIMATION_EXTENSION:
  
  FRAME_DENSITY:
    Animation can load each frame with multiple parallel streams:
    - Visual narrative (action)
    - Visual comedy (background gags)
    - Audio narrative (dialogue)
    - Audio texture (music, effects)
    - Timing itself as expressive element
  
  SIMULTANEITY_ADVANTAGE:
    Unlike live action, every element is authored
    â†’ Maximum information density possible
    â†’ Attention sustained through parallel reward streams
```

---

## 3. The Involuntary Response Hierarchy

### 3.1 The Epistemological Privilege of Comedy and Horror

**Core claim**: Comedy and horror are epistemologically privileged genres because they possess **binary physiological verification**â€”the body cannot lie about fear or laughter.

```
INVOLUNTARY_RESPONSE_HIERARCHY:

  TIER 1 - PHYSIOLOGICAL BINARY (Body confirms/denies in real-time):
    
    COMEDY:
      marker = laughter
      verification = audible, visible, uncontrollable
      failure_mode = silence
      test = "Did the audience laugh? Y/N"
    
    HORROR:
      marker = fear response (startle, tension, dread, unease)
      verification = physiological (heart rate, skin conductance, posture)
      failure_mode = boredom, disengagement
      test = "Did the audience experience fear? Y/N"
  
  TIER 2 - PHYSIOLOGICAL BUT AMBIGUOUS:
    
    TRAGEDY:
      marker = tears, grief
      verification = visible but fakeable, can be intellectual
      failure_mode = admiration without feeling
      test = "Did the audience weep?" (but weeping can be performed)
    
    ROMANCE:
      marker = longing, satisfaction
      verification = subjective report
      failure_mode = indifference
  
  TIER 3 - SUBJECTIVE REPORT ONLY:
    
    DRAMA:
      marker = "emotional engagement"
      verification = subjective, post-hoc report
      failure_mode = intellectual appreciation only
      test = "Was the audience moved?" (self-report unreliable)
```

### 3.2 Classical Support

**Aristotle** (Poetics): Tragedy aims at catharsis of pity and fearâ€”specific physiological/emotional states, not intellectual appreciation.

**Bharata Muni** (Natyasastra): The rasa (aesthetic emotional essence) manifests through involuntary physical responses:

> "Laughter arises from a mimicry of other people's actions. It is to be represented on the stage with Smile, Laughter, and Excessive Laughter."

> "Fear is to be represented with tremor of hands and feet, palpitation of the heart, paralysis, licking the lips, drying up of the mouth, loosened limbs and sinking body."

**Plato** (Republic, Book X): Acknowledges the dangerous power of poetry to bypass reason:

> "There is a principle in human nature which is disposed to raise a laugh, and this which you once restrained by reason, because you were afraid of being thought a buffoon, is now let out again."

### 3.3 The Husband Test / The Brave Test

```python
def involuntary_response_test(content: Narrative, audience: Person) -> bool:
    """
    Comedy and horror are "pure" when they compel involuntary response
    even from audiences with reason to resist.
    """
    
    # THE HUSBAND TEST (Comedy)
    if content.genre == COMEDY:
        joke_target = content.get_target()
        if audience.has_personal_investment_against(joke_target):
            response = observe_response(audience)
            if response == LAUGHTER:
                return True  # Pure comedy: overcame resistance
            else:
                return False  # Failed: resistance won
    
    # THE BRAVE TEST (Horror)
    if content.genre == HORROR:
        if audience.self_identifies_as("brave", "unflinching"):
            response = observe_response(audience)
            if response in [FEAR, DREAD, UNEASE, STARTLE]:
                return True  # Pure horror: overcame self-image
            else:
                return False  # Failed: bravado maintained
    
    return None  # Not applicable to other genres
```

### 3.4 Implications for Craft

```
INVOLUNTARY_RESPONSE_CRAFT_IMPLICATIONS:

  1. COMEDY and HORROR have no hiding place
     - Audience reaction is immediate and public
     - "Bombing" in comedy is visible; failing in horror = boredom
     - No critical apparatus can rescue failed execution
  
  2. Involuntary response requires NON-CONTRIVED triggers
     - Setup must not telegraph punchline
     - Horror must not announce its scares
     - The response must be SURPRISED out of the audience
  
  3. Repetition degrades involuntary response (McKee's Law of Diminishing Returns)
     - First scare: full effect
     - Second scare: half effect
     - Third scare: laugher (or boredom)
     
     - First joke: laugh
     - Second similar joke: smile
     - Third similar joke: groan
  
  4. VARIATION and SUBVERSION required to sustain involuntary response
     - Pattern establishment â†’ pattern violation
     - Prediction â†’ prediction failure â†’ recalibration
```

---

## 4. Prediction Dynamics: Two Modes

### 4.1 The Two Attention Modes

Sustained attention operates through one of two cognitive-emotional dynamics:

```
MODE_1: ANTICIPATION-SATISFACTION (Genre Fulfillment)

  MECHANISM:
    1. Establish pattern/promise (genre contract)
    2. Create anticipation of fulfillment
    3. Delay fulfillment through complications
    4. Deliver satisfaction (pattern completed)
  
  ATTENTION_DRIVER: "I know what's coming; I want to see it happen"
  
  EXAMPLES:
    - Romantic comedy: Will they get together? (Yes, eventually)
    - Heist film: Will they pull it off?
    - Sports movie: Will underdog win?
    - Slasher film: How will final girl survive?
  
  RISK: Boredom if delay feels arbitrary
  
  TECHNIQUE: Complications must feel NECESSARY, not arbitrary
             (See: But/Therefore causation)

MODE_2: PREDICTION-FAILURE-RECALIBRATION (Jazz Mode)

  MECHANISM:
    1. Establish apparent pattern
    2. Violate pattern at beat level
    3. Force cognitive recalibration
    4. Repeat before new pattern stabilizes
  
  ATTENTION_DRIVER: "I can't predict what's next; I must keep watching"
  
  EXAMPLES:
    - Barbarian (2022): Genre shifts at sequence level
    - Atlanta: Surreal intrusions per scene
    - Coen Brothers: Tonal whiplash
    - Lynch: Logic violation as sustained mode
  
  RISK: Incoherence if no underlying structure
  
  TECHNIQUE: Coherence at one level, subversion at another
             (Genre coherence + beat-level jazz)
```

### 4.2 The Jazz Analogy

```
JAZZ_MODE_ANALOGY:

  JAZZ_MUSIC:
    coherence_level = key, time signature, harmonic language
    subversion_level = phrase, individual note choices
    
    RESULT: Listener knows "where we are" (key/rhythm)
            but cannot predict "what's next" (specific phrase)
  
  JAZZ_NARRATIVE (e.g., Barbarian):
    coherence_level = genre (horror), consistent tone
    subversion_level = beat-to-beat progression
    
    RESULT: Viewer knows "what kind of experience" (horror film)
            but cannot predict "what happens next" (specific beat)
    
  MECHANISM:
    - Prediction model never stabilizes at beat level
    - Nervous system remains in ACQUISITION mode
    - Attention sustained through uncertainty, not anticipation
```

### 4.3 Subversion Density Spectrum

```
SUBVERSION_DENSITY:

  LOW (Traditional structure):
    Subvert at ACT level
    Most beats predictable; major surprises at act breaks
    Example: Classical Hollywood narrative
  
  MEDIUM (Elevated genre):
    Subvert at SEQUENCE level
    Tonal/genre shifts every 15-20 minutes
    Example: Get Out, Parasite
  
  HIGH (Jazz mode):
    Subvert at BEAT level
    No stable prediction between scenes
    Example: Barbarian, Mulholland Drive
  
  MAXIMUM (Avant-garde):
    Subvert at MOMENT level
    Constant violation; coherence abandoned or deeply hidden
    Example: Godard, experimental film
```

### 4.4 Mode Mixing

```python
def assess_mode_mixing(narrative: Narrative) -> MixAssessment:
    """
    Mixing anticipation-satisfaction and jazz modes requires skill.
    The modes can coexist at different structural levels.
    """
    
    levels = ['moment', 'beat', 'scene', 'sequence', 'act', 'whole']
    
    mode_map = {}
    for level in levels:
        mode_map[level] = detect_dominant_mode(narrative, level)
    
    # VALID MIX: Different modes at different levels
    # Example: Jazz at beat level, anticipation at act level
    if is_consistent_within_levels(mode_map):
        return MixAssessment.VALID
    
    # INVALID MIX: Modes collide at same level
    # Example: Promising genre fulfillment then violating it arbitrarily
    if has_same_level_collision(mode_map):
        return MixAssessment.INCOHERENT
    
    return MixAssessment.AMBIGUOUS
```

---

## 5. Density and Simultaneity

### 5.1 The Density Gradient

As media become more simultaneous (capable of presenting parallel information streams), they can achieve higher attention-sustaining density:

```
SIMULTANEITY_SPECTRUM:

  LOW SIMULTANEITY:
    Medium: Prose
    Channels: 1 (text)
    Mechanism: Sequential processing only
    Density: Must achieve attention through sequence quality
  
  MEDIUM SIMULTANEITY:
    Medium: Comics
    Channels: 2 (text + image, but spatially separated)
    Mechanism: Eye movement between channels
    Density: Can reward attention with visual + textual
  
  HIGH SIMULTANEITY:
    Medium: Film
    Channels: 3+ (image + dialogue + music + sound design)
    Mechanism: Parallel processing of streams
    Density: Multiple reward streams per moment
  
  VERY HIGH SIMULTANEITY:
    Medium: Animation, Games
    Channels: 4+ (all film channels + interactivity/authored timing)
    Mechanism: Every element authored for maximum density
    Density: Can sustain attention through sheer richness
```

### 5.2 Density as Compensation

```
DENSITY_COMPENSATION_PRINCIPLE:

  IF narrative_quality.causal_binding is WEAK:
    THEN require HIGH attention_density to compensate
  
  IF narrative_quality.causal_binding is STRONG:
    THEN can operate with LOWER attention_density
  
  EXAMPLES:
    - Music video: Weak narrative causation, but high audio-visual density sustains attention
    - Tarkovsky: Slow pacing, low density, but strong thematic/causal binding
    - Michael Bay: Weak causation, compensated by relentless visual density
    - Pixar: Strong causation AND high density = maximum sustained attention
```

### 5.3 The Parallel Stream Architecture

```
PARALLEL_STREAM_MODEL:

  For any moment t in a high-simultaneity medium:
  
  STREAM_1: Visual narrative (what is happening)
  STREAM_2: Visual texture (how it looks, composition, color)
  STREAM_3: Auditory semantic (dialogue, what is said)
  STREAM_4: Auditory emotional (music, how to feel)
  STREAM_5: Auditory textural (sound design, immersion)
  STREAM_6: Kinetic (editing rhythm, camera movement)
  
  ATTENTION_SUSTAINABILITY:
    If any stream falters, others can carry attention
    Maximum resilience when all streams are operative
    Failure requires multiple streams to fail simultaneously
  
  ANIMATION_ADVANTAGE:
    In animation, ALL streams are fully authored
    No "found" footage, no improvisation, no accident
    Therefore maximum potential density achievable
```

---

## 6. Causal Binding as Attention Glue

### 6.1 The But/Therefore Substrate

Regardless of medium or attention mechanism, **causal binding** is the underlying adhesive:

```
CAUSAL_BINDING_PRINCIPLE:

  DEFINITION:
    Causal binding = each narrative unit exists BECAUSE OF the previous
                     and creates CONDITIONS for the next
  
  EQUIVALENCES:
    Parker/Stone: "but / therefore" (not "and then")
    Aristotle: propter hoc (not post hoc)
    Forster: plot (not story)
    McKee: gap between expectation and result
  
  FUNCTION:
    Causal binding creates MOMENTUM
    Momentum creates INEVITABILITY feeling
    Inevitability feeling sustains ATTENTION
    
    "I must keep watching to see what this CAUSES"
```

### 6.2 Causation Across Media

```
CAUSAL_BINDING_BY_MEDIUM:

  PROSE:
    Unit: Sentence â†’ Paragraph â†’ Scene â†’ Chapter
    Binding: Each sentence should make next sentence feel necessary
    Test: "Would removing this sentence break the chain?"
  
  COMICS:
    Unit: Panel â†’ Tier â†’ Page â†’ Issue
    Binding: Panel N should make Panel N+1 feel inevitable
    Test: McCloud's closure types; higher closure = weaker binding
  
  FILM:
    Unit: Shot â†’ Scene â†’ Sequence â†’ Act
    Binding: Cut should feel motivated; scenes causally linked
    Test: "Can I reorder these scenes without breaking logic?"
  
  TELEVISION:
    Unit: Scene â†’ Episode â†’ Season â†’ Series
    Binding: Episode cliffhangers; season arcs
    Test: "Would skipping this episode break understanding?"
  
  GAMES:
    Unit: Action â†’ Quest â†’ Chapter â†’ Campaign
    Binding: Player actions cause state changes that matter
    Test: "Do my choices have consequences I can trace?"
```

### 6.3 When Causation Can Be Weakened

```
CAUSATION_RELAXATION_CONDITIONS:

  1. HIGH SIMULTANEITY compensation
     If visual/audio streams are sufficiently rewarding,
     narrative causation can be looser
     Example: Music video, tone poem, visual spectacle
  
  2. JAZZ MODE operation
     If prediction-failure is the attention driver,
     strict causation may be deliberately violated
     Example: Surrealist narrative, David Lynch
     
     BUT: Some meta-level coherence still required
          (thematic, tonal, or symbolic binding replaces causal)
  
  3. MEDITATIVE/AMBIENT goals
     If attention goal is not "sustained engagement" but "dwelling,"
     causation requirements relax
     Example: Slow cinema, ambient music, contemplative games
     
  4. GENRE CONTRACT allows it
     Some genres promise episodic rather than causal structure
     Example: Sketch comedy, anthology, picaresque
```

---

## 7. Cross-Media Correspondence Tables

### 7.1 Attention Mechanisms by Medium

| Mechanism | Prose | Comics | Film | Animation | Games |
|-----------|-------|--------|------|-----------|-------|
| Primary hook | Sentence rhythm | Panel curiosity | Shot composition | Frame density | Agency |
| Micro-unit | Word/phrase | Panel/gutter | Frame/cut | Frame | Input/feedback |
| Progression driver | Semantic gap | Closure demand | Edit momentum | Timing | Challenge/reward |
| Page/screen turn | Chapter end | Page turn | Scene end | Episode end | Level transition |
| Simultaneity | Low | Medium | High | Very high | Very high |
| Author control | Total | Total | Partial | Total | Systemic |

### 7.2 Involuntary Response Markers

| Genre | Aristotle | Bharata Muni | McKee | Physiological Marker | Verification |
|-------|-----------|--------------|-------|---------------------|--------------|
| Tragedy | Pity + Fear | Karuna (pathos) | Emotional climax | Tears, grief | Visible but fakeable |
| Comedy | The Ludicrous | Hasya | Release of tension | Laughter | Audible, binary |
| Horror | Fear (phobos) | Bhayanaka | Dread | Startle, tension | Physiological |
| Wonder | Thaumaston | Adbhuta | Awe | Widened eyes, stillness | Observable |
| Anger | â€” | Raudra | Indignation | Tension, flushing | Observable |
| Disgust | â€” | Bibhatsa | Revulsion | Aversion behavior | Observable |
| Erotic | â€” | Sringara | Longing | Varies | Subjective |
| Heroic | â€” | Vira | Admiration | Elevated posture | Partially observable |

### 7.3 Prediction Mode Mapping

| Mode | Cognitive State | Attention Driver | Genre Examples | Structural Level |
|------|-----------------|------------------|----------------|------------------|
| Anticipation-Satisfaction | Prediction confident | "I want to see X happen" | Romance, Heist, Sports | Act-level subversion |
| Mild Jazz | Prediction cautious | "I think X, but unsure" | Thriller, Mystery | Sequence-level subversion |
| Full Jazz | Prediction destabilized | "I cannot predict" | Barbarian, Mulholland Drive | Beat-level subversion |
| Ambient | Prediction suspended | "I am dwelling, not predicting" | Slow cinema, Meditation games | Causation relaxed |

### 7.4 Density Compensation Matrix

| Causal Strength | Low Density | Medium Density | High Density |
|-----------------|-------------|----------------|--------------|
| **Strong** | Tarkovsky, Slow cinema | Classical Hollywood | Pixar, Peak TV |
| **Medium** | Literary fiction | Standard genre film | Marvel, Blockbuster |
| **Weak** | Experimental, Avant-garde | Music video, Tone poem | Michael Bay, Spectacle |

---

## 8. Diagnostic Protocols

### 8.1 Universal Attention Diagnostic

Apply to any narrative in any medium:

```
ATTENTION_DIAGNOSTIC:

  STEP 1: IDENTIFY MEDIUM
    What is the primary medium?
    What simultaneity level does it afford?
  
  STEP 2: MAP MECHANISM LAYERS
    â–¡ What is the micro-unit of attention? (word, panel, frame, input)
    â–¡ What is the meso-unit? (scene, page, sequence, level)
    â–¡ What is the macro-unit? (chapter, issue, act, campaign)
  
  STEP 3: TEST CAUSAL BINDING
    â–¡ Can units be reordered without breaking logic?
    â–¡ Does each unit create conditions for the next?
    â–¡ If "and then" fits between units, why?
  
  STEP 4: IDENTIFY PREDICTION MODE
    â–¡ Anticipation-satisfaction (genre fulfillment)?
    â–¡ Jazz mode (prediction destabilization)?
    â–¡ Mixed? At what levels?
  
  STEP 5: ASSESS DENSITY COMPENSATION
    â–¡ If causation is weak, is density sufficient?
    â–¡ If density is low, is causation sufficient?
  
  STEP 6: CHECK INVOLUNTARY RESPONSE TARGETS
    â–¡ What physiological response is targeted?
    â–¡ Is the mechanism appropriate to that response?
    â–¡ Is repetition degrading the response?
```

### 8.2 Genre-Specific Diagnostics

```
COMEDY_DIAGNOSTIC:
  â–¡ Does the audience laugh? (Binary test)
  â–¡ Does laughter occur against audience's interests? (Purity test)
  â–¡ Is setup/punchline rhythm varied? (Diminishing returns check)
  â–¡ Is timing precise? (Involuntary response requires precision)

HORROR_DIAGNOSTIC:
  â–¡ Does the audience experience fear/dread/unease?
  â–¡ Does fear persist in self-identified "brave" viewers?
  â–¡ Are scares unpredictable at beat level?
  â–¡ Is tension maintained between scares?

TRAGEDY_DIAGNOSTIC:
  â–¡ Does the audience experience genuine grief/catharsis?
  â–¡ Or only intellectual appreciation of craft?
  â–¡ Is pity earned through character investment?
  â–¡ Is fear generated through identification with stakes?
```

### 8.3 The Barbarian Test (Jazz Mode Verification)

```
JAZZ_MODE_VERIFICATION:

  For a narrative suspected of operating in jazz mode:
  
  1. COHERENCE CHECK
     â–¡ Is there underlying coherence (genre, tone, theme)?
     â–¡ Can you name what KIND of experience this is?
     â–¡ If no coherence at any level â†’ not jazz, just incoherent
  
  2. SUBVERSION FREQUENCY
     â–¡ At what level does subversion occur?
     â–¡ Beat level (high jazz): Every scene defies expectation
     â–¡ Sequence level (moderate): Every 15-20 min
     â–¡ Act level (low): Major twists at act breaks only
  
  3. PREDICTION MODEL
     â–¡ Does viewer's prediction model stabilize?
     â–¡ Jazz mode = model never stabilizes
     â–¡ If model stabilizes â†’ not jazz mode
  
  4. ACQUISITION STATE
     â–¡ Is viewer's nervous system in acquisition mode?
     â–¡ Characterized by: alertness, forward lean, uncertainty
     â–¡ Versus: relaxation, backward lean, confirmation-seeking
```

---

## 9. Genre as Attention Contract

### 9.1 The Genre Contract Framework

Genre is an attention contract between creator and audience:

```
GENRE_CONTRACT:

  CREATOR_PROMISE:
    "If you invest attention, you will receive [GENRE_FULFILLMENT]"
  
  AUDIENCE_EXPECTATION:
    "I am investing attention because I anticipate [GENRE_FULFILLMENT]"
  
  FULFILLMENT_TYPES:
    Comedy â†’ Laughter
    Horror â†’ Fear (safely experienced)
    Romance â†’ Romantic satisfaction
    Action â†’ Kinetic excitement
    Mystery â†’ Solution revelation
    Tragedy â†’ Cathartic grief
  
  CONTRACT_VIOLATION:
    If promise not fulfilled â†’ audience feels cheated
    Attention investment not rewarded â†’ trust broken
```

### 9.2 Genre and Prediction Mode

```
GENRE_PREDICTION_RELATIONSHIP:

  STRONG_CONTRACT_GENRES (Anticipation-Satisfaction dominant):
    Romance, Sports, Heist, Courtroom
    Audience knows outcome type; wants to see journey
    Subversion at beat level acceptable
    Subversion at outcome level = contract violation
  
  WEAK_CONTRACT_GENRES (Jazz mode acceptable):
    Arthouse, Experimental, Some horror, Thriller
    Audience accepts uncertainty as part of contract
    Subversion at outcome level acceptable
    Incoherence still not acceptable
  
  HYBRID:
    Elevated genre (Get Out, Parasite)
    Honors genre contract at macro level
    Subverts at sequence/beat level
    Maximum engagement: fulfillment + surprise
```

### 9.3 Comedy and Horror as Pure Genres

```
PURE_GENRE_THEORY:

  COMEDY and HORROR are "pure" because:
  
  1. Contract is PHYSIOLOGICAL, not intellectual
     - Other genres: "I promise you will feel engaged"
     - Comedy/Horror: "I promise your body will react"
  
  2. Verification is IMMEDIATE and BINARY
     - Did you laugh? Did you feel fear?
     - No post-hoc rationalization possible
  
  3. FAILURE is PUBLIC and UNDENIABLE
     - Silent comedy audience = failed comedy
     - Bored horror audience = failed horror
  
  4. CRAFT is NON-NEGOTIABLE
     - Cannot rely on thematic importance
     - Cannot rely on critical apparatus
     - Must deliver involuntary response or fail
```

---

## 10. Theoretical Lineage

### 10.1 Classical Foundations

| Source | Contribution | Modern Echo |
|--------|--------------|-------------|
| Aristotle, *Poetics* | Catharsis, unity, propter hoc vs. post hoc | Involuntary response, causal binding |
| Plato, *Republic* | Mimesis danger, emotional contagion | Physiological engagement theory |
| Horace, *Ars Poetica* | Docere et delectare (teach and delight) | Dual-channel attention (meaning + pleasure) |
| Bharata Muni, *Natyasastra* | Rasa theory, 8-9 emotional essences | Genre as emotional contract |

### 10.2 Modern Craft Theory

| Source | Contribution | Integration |
|--------|--------------|-------------|
| E.M. Forster | Story vs. plot (causation distinction) | Causal binding formalization |
| Robert McKee | Gap, progressive complications, Law of Diminishing Returns | Attention mechanics, repetition degradation |
| Parker/Stone | But/Therefore rule | Causal binding diagnostic |
| Scott McCloud | Closure, panel transitions | Comics-specific attention mechanisms |
| Kubrick | Subconscious engagement, productive ambiguity | Jazz mode, non-verbal attention |

### 10.3 Novel Contributions

This framework introduces:

1. **Attention as ur-currency** â€” Explicit framing of attention as the trans-historical, trans-media constraint
2. **Involuntary response hierarchy** â€” Comedy and horror as epistemologically privileged
3. **Two prediction modes** â€” Anticipation-satisfaction vs. prediction-failure-recalibration (jazz)
4. **Density-causation compensation** â€” Formal relationship between parallel streams and narrative causation
5. **Simultaneity spectrum** â€” Gradient from prose to games based on parallel channel capacity
6. **The husband test / brave test** â€” Operational definitions of "pure" comedy and horror

---

## 11. Quick Reference Card

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚           ATTENTION MECHANICS - QUICK REFERENCE                 â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚                                                                 â”‚
â”‚  FOUNDATIONAL AXIOM:                                            â”‚
â”‚  Attention is the ur-currency; all media solve the same        â”‚
â”‚  problem: sustaining engagement through time.                   â”‚
â”‚                                                                 â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚                                                                 â”‚
â”‚  INVOLUNTARY RESPONSE HIERARCHY:                                â”‚
â”‚  TIER 1 (Binary physiological): Comedy (laughter), Horror      â”‚
â”‚  TIER 2 (Physiological but fakeable): Tragedy (tears)          â”‚
â”‚  TIER 3 (Subjective only): Drama ("engagement")                â”‚
â”‚                                                                 â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚                                                                 â”‚
â”‚  TWO PREDICTION MODES:                                          â”‚
â”‚  MODE 1: Anticipation-Satisfaction (genre fulfillment)         â”‚
â”‚    â†’ "I know what's coming; I want to see it happen"           â”‚
â”‚  MODE 2: Prediction-Failure-Recalibration (jazz)               â”‚
â”‚    â†’ "I can't predict; I must keep watching"                   â”‚
â”‚                                                                 â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚                                                                 â”‚
â”‚  CAUSAL BINDING TEST:                                           â”‚
â”‚  â–¡ "And then" between units? â†’ WEAK (rewrite)                  â”‚
â”‚  â–¡ "But/Therefore" between units? â†’ STRONG (pass)              â”‚
â”‚  â–¡ Can units be reordered? â†’ WEAK if yes                       â”‚
â”‚                                                                 â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚                                                                 â”‚
â”‚  DENSITY COMPENSATION:                                          â”‚
â”‚  IF causation weak, THEN density must be high                  â”‚
â”‚  IF density low, THEN causation must be strong                 â”‚
â”‚  BOTH strong = maximum sustained attention                      â”‚
â”‚                                                                 â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚                                                                 â”‚
â”‚  SIMULTANEITY SPECTRUM:                                         â”‚
â”‚  Prose (1 channel) â†’ Comics (2) â†’ Film (3+) â†’                  â”‚
â”‚  Animation (4+) â†’ Games (4+ with agency)                       â”‚
â”‚                                                                 â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚                                                                 â”‚
â”‚  PURITY TESTS:                                                  â”‚
â”‚  COMEDY: Does the husband laugh at jokes about husbands?       â”‚
â”‚  HORROR: Does the brave person feel fear anyway?               â”‚
â”‚  If YES â†’ mechanism working at somatic level                   â”‚
â”‚                                                                 â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

---

## Appendix: Integration with Existing Algorithms

This meta-principles document provides theoretical foundation for:

| Existing Algorithm | Integration Point |
|--------------------|-------------------|
| **Aristotle** | Catharsis as involuntary response target; propter hoc as causal binding |
| **Bharata Muni** | Rasa as genre-emotional contract; involuntary physical manifestations |
| **McKee** | Gap as micro-attention mechanism; Law of Diminishing Returns |
| **South Park** | But/Therefore as causal binding diagnostic |
| **Larry David** | Cascading consequences as strong causal binding |
| **Phoebe Waller-Bridge** | Three-layer obstacles as density mechanism |
| **Kubrick** | Subconscious engagement as jazz mode; non-verbal as simultaneity exploitation |
| **Tarantino** | Genre as attention contract; sub-genre specificity |
| **Plato** | Mimesis danger as evidence of involuntary response power |
| **Horace** | Docere et delectare as dual-channel attention theory |

---

*Document version: 1.0*
*Framework status: Foundational meta-theory*
*Integration: Sits above all individual artist/theorist algorithms*
