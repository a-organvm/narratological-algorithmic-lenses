# Horace's Narratological Algorithms

A systematic distillation of Horace's *Ars Poetica* (~19 BCE) into formal, implementable principles for narrative construction. Based on the George Colman translation.

---

## 0. Meta-Principles (Axioms)

Horace's *Ars Poetica* (Epistle to the Pisos) operates as practical craft instruction, emphasizing labor, judgment, and the balance of natural gift with disciplined study.

| Axiom | Formulation |
|-------|-------------|
| H-A0 | **"Genius AND Art."** Poetry requires both natural gift and disciplined study. |
| H-A1 | **"Instruct and Delight."** The goal is to benefit (prodesse) and please (delectare). |
| H-A2 | **"Unity as Supreme Virtue."** Every part must be essential to one simple whole. |
| H-A3 | **"Decorum governs All."** Appropriateness to subject, character, genre, and audience. |
| H-A4 | **"No Middle Ground."** Poetry admits no mediocrity; excellence or nothing. |
| H-A5 | **Labor and revision** distinguish the artist from the amateur. |
| H-A6 | The **probable impossible** is preferable to the **improbable possible**. |

### 0.1 The Dual Requirement: Genius + Labor

```
PROPOSITION:
  "Whether good verse of Nature is the fruit,
   Or form'd by Art, has long been in dispute."
   
HORACE'S_RESOLUTION:
  NEITHER alone suffices
  
  IF genius.present AND labor.absent:
    output = raw_potential_wasted
    
  IF labor.present AND genius.absent:
    output = barren_toil
    
  ONLY IF genius.present AND labor.present:
    output = true_poetry
    
PROOF_BY_ANALOGY:
  "Much has the Youth, who pressing in the race
   Pants for the promis'd goal and foremost place,
   Suffer'd and done; borne heat, and cold's extremes,
   And Wine and Women scorn'd, as empty dreams."
   
THEREFORE:
  Nature + Study = "Each finds in each a friend and firm ally"
```

### 0.2 The Dual Purpose: Instruct + Delight

```
PURPOSE_OPTIONS:
  1. prodesse (to instruct/benefit)
  2. delectare (to delight/please)
  3. BOTH (optimal)

OPTIMAL_FORMULA:
  "Omne tulit punctum, qui miscuit utile dulci,
   Lectorem delectando, pariterque monendo"
   
TRANSLATION:
  "He wins every vote who blends the useful with the pleasant,
   Delighting and instructing the reader at once."

APPLICATION_BY_AUDIENCE:
  IF audience = elders:
    REQUIRE: moral instruction (frugis)
    "The Old, if Moral's wanting, damn the Play"
    
  IF audience = youth:
    REQUIRE: entertainment (sentiment)
    "Sentiment disgusts the Young and Gay"
    
  IF audience = mixed:
    REQUIRE: both instruction AND delight
```

### 0.3 No Mediocrity in Poetry

```
RULE: Poetry admits NO middle ground

CONTRAST_WITH_OTHER_ARTS:
  lawyer.mediocre = still useful
  consultant.mediocre = still valued
  
  poet.mediocre = worthless
  
REASONING:
  "Poetry, so exquisite of kind,
   Of Pleasure born, to charm the soul design'd,
   If it fall short but little of the first,
   Is counted last, and rank'd among the worst."
   
ANALOGY:
  discordant_music at feast = offensive
  rank_ointment at festival = offensive
  
  BECAUSE: these are NOT essential
           UNLESS the very best, better omitted
           
THEREFORE:
  excellence_threshold = absolute
  "Not men, nor Gods, nor niblick-polls admit" middling poets
```

---

## 1. The Unity Principle (First Law)

### 1.1 The Chimera Test

```
OPENING_IMAGE:
  "Suppose a painter to a human head
   Should join a horse's neck, and wildly spread
   The various plumage of the feather'd kind..."
   
THIS_PRODUCES:
  - woman's face
  - horse's neck  
  - fish's tail
  - feathers of varied birds
  
RESULT:
  "viewing such a sight, would you not smile?"
  
APPLICATION_TO_POETRY:
  "Trust me, my Pisos! not unlike this piece,
   Would be a book, such monstrous shapes to join,
   As have no likeness, and no one design..."
   
CHIMERA_TEST:
  FOR each element E in work:
    IF E.origin_domain != work.primary_domain:
      IF connection NOT justified:
        flag_as_chimeric
```

### 1.2 The Organic Unity Formula

```
DEFINITION:
  "One simple whole must through the piece run,
   True from the first, and finish'd when 'tis done"
   
REQUIREMENTS:
  1. Single central design (simplex_dumtaxat_et_unum)
  2. All parts derive from and serve that design
  3. No part transposable without damage
  4. No part deletable without loss
  
CONGRUITY_TEST:
  "True to one point, persu'd from end to end"
  
  IF beginning.style != middle.style:
    FAIL
  IF middle.tone != end.tone:
    FAIL
    
  "Primo ne medium, medio ne discrepet imum"
  "That beginning agrees with middle, middle with end"
```

### 1.3 The Purple Patch Warning

```
ANTI-PATTERN: "Purple patches" (purpureus pannus)

DEFINITION:
  Brilliant passages that don't serve the whole
  
SYMPTOMS:
  - grove + altar descriptions for their own sake
  - digressions on landscape beauty
  - Rhine River passages unconnected to plot
  - rainbow descriptions without function
  
WARNING:
  "Oft works of promise large, and high attempt,
   Begin in purple; glitt'ring shreds are hempt,
   And stitch'd to catch the eye..."
   
RULE:
  IF passage.brilliance > passage.function:
    DELETE or SUBORDINATE
    
  "These out of time and place, how fair soe'er,
   Like rich embroidery on a ragged ground, appear"
```

---

## 2. Decorum: The Fitness Algorithm

### 2.1 Genre-Style Matching

```
GENRE_STYLE_TABLE:
  | Genre | Style Level | Examples |
  |-------|-------------|----------|
  | Epic | High/Grand | Homer, War of Troy |
  | Tragedy | Elevated | Thyestes, Medea |
  | Comedy | Low/Familiar | Chremes, domestic affairs |
  | Satire | Middle/Varied | Moral instruction |
  | Elegy | Mournful | Lament, then praise |
  | Lyric/Ode | Elevated | Gods, victors, love, wine |

VIOLATION_EXAMPLES:
  "A comick incident loaths tragick strains"
  "Thy feast, Thyestes, lowly verse disdains"
  
FLEXIBILITY_CLAUSE:
  "Yet Comedy at times exalts her strain,
   And angry Chremes storms in swelling vein"
   
  "The tragick hero, plung'd in deep distress,
   Sinks with his fate, and makes his language less"
   
RULE:
  style = f(genre, situation, character_state)
  
  IF character.distressed AND genre = tragedy:
    ALLOW: reduced_elevation
    "Peleus and Telephus, poor, banish'd! each
     Drop their big six-foot words, and sounding speech"
```

### 2.2 Character-Speech Congruity

```
SPEAKER_PROFILE_TABLE:
  | Speaker Type | Speech Characteristics |
  |--------------|------------------------|
  | God | Elevated, authoritative |
  | Hero | Noble, grand but not pompous |
  | Grave old man | Serious, measured |
  | Hot young spark | Impetuous, passionate |
  | Matron | Dignified, proper |
  | Busy nurse | Practical, bustling |
  | Traveling merchant | Worldly, commercial |
  | Farmer | Simple, rustic |
  | Colchian | Exotic, foreign register |
  | Assyrian | Eastern, distinctive |
  | Theban | Greek, educated |
  | Argian | Greek, variant tradition |

RULE:
  "Much boots the speaker's character to mark:
   God, heroe; grave old man, or hot young spark"
   
TEST:
  IF speaker.words != speaker.type_profile:
    "Romans shall crack their sides, and all the town
     Join, horse and foot, to laugh th' impostor down"
```

### 2.3 Emotional State-Expression Matching

```
EMOTION_EXPRESSION_TABLE:
  | Emotional State | Required Expression |
  |-----------------|---------------------|
  | Sorrow | Mournful countenance + sad words |
  | Anger | Menacing aspect + threatening words |
  | Playful/Frolicking | Light manner + lascivious strain |
  | Severe/Serious | Grave demeanor + serious diction |

NATURE'S_MECHANISM:
  "For Nature first, to every varying wind
   Of changeful fortune, shapes the pliant mind;
   Sooths it with pleasure, or to rage provokes,
   Or brings it to the ground by sorrow's heavy strokes;
   Then of the joys that charm'd, or woes that wrung,
   Forces expression from the faithful tongue"
   
FAILURE_CONDITION:
  "if the actor's words belie his state,
   And speak a language foreign to his fate"
   
RESULT: ridicule and rejection
```

### 2.4 The Ages of Man Algorithm

```
LIFECYCLE_CHARACTER_PROFILES:

BOY (puer):
  - can speak and walk steadily
  - chief delight: playfellows
  - behavior: quarrels, shakes hands immediately
  - temporal_scope: "all humours ev'ry hour"
  - traits: inconstant, easily swayed
  
BEARDLESS_YOUTH (imberbus juvenis):
  - freed from tutor
  - loves: horses, hounds, liberty
  - moral_state: "Pliant as wax, to vice"
  - response_to_counsel: "Marble to wholesome counsel"
  - financial: improvident, profuse
  - emotional: high, fond, fickle, generous, loose
  
MATURE_MAN (aetas virilis):
  - pursuits: riches, friends, honor
  - knows: "all the meanness of ambition"
  - behavior: prudent, wary
  - temporal: fearful to act, then repent
  
OLD_MAN (senex):
  - relationship_to_wealth: gained much, fears to use
  - action_style: "Timid and cold in all he undertakes"
  - temporal: fond of delay, "Dup'd by to-morrow"
  - disposition: "Ill-humour'd, querulous"
  - orientation: loud praise of former days
  
RULE:
  "Confound not youth with age, nor age with youth,
   But mark their several characters with truth!"
   
IMPLEMENTATION:
  def assign_character_traits(character):
    age_bracket = determine_age_bracket(character.age)
    return LIFECYCLE_PROFILES[age_bracket]
```

---

## 3. The Established Character System

### 3.1 Traditional vs. Novel Characters

```
TWO_PATHS:
  1. FOLLOW_FAME: Use established characters
  2. CREATE_NEW: Invent original characters

TRADITIONAL_CHARACTERS (Examples):
  | Character | Required Traits |
  |-----------|-----------------|
  | Achilles | Active, wrathful, inexorable, fierce |
  | Medea | Fierce, invincible |
  | Ino | Tearful, sad |
  | Ixion | Perfidious |
  | Io | Wandering |
  | Orestes | Mad, melancholy |

RULE_FOR_TRADITIONAL:
  "Follow the Voice of Fame"
  
  IF character = Achilles:
    MUST_BE: "Impiger, iracundus, inexorabilis, acer"
             "Eager, impetuous, brave, and high of soul,
              Always for arms, and brooking no controul"
```

### 3.2 The Consistency Principle

```
RULE: "Preserve it well; continu'd as begun;
       True to itself in ev'ry scene, and one!"
       
FORMAL_STATEMENT:
  "servetur ad imum / Qualis ab incepto processerit, et sibi constet"
  "Let it be preserved to the end as it proceeded from the beginning,
   and be consistent with itself"
   
TEST:
  character_profile_t0 = establish_character(scene_1)
  
  FOR scene in scenes[1:]:
    character_profile_tn = observe_character(scene)
    IF character_profile_tn != character_profile_t0:
      UNLESS change_is_motivated:
        FLAG_INCONSISTENCY
```

### 3.3 The Common Material Paradox

```
PARADOX:
  "Difficile est propriÃ¨ communia dicere"
  "It is difficult to treat common themes distinctively"
  
RESOLUTION_PATH_1 (Safer):
  "Safer the Iliad to reduce to acts,
   Than be the first new regions to explore"
   
RESOLUTION_PATH_2 (Transform familiar):
  "Quit but the vulgar, broad, and beaten round,
   The publick field becomes your private ground"
   
METHOD:
  IF using_common_material:
    DO NOT: "word for word too faithfully translate"
    DO NOT: "leap at once into a narrow strait"
    DO: transform through personal vision
    
  "Let me on subjects known my verse so frame,
   So follow it, that each may hope the same;
   Daring the same, and toiling to prevail,
   May vainly toil, and only dare to fail!"
   
KEY_INSIGHT:
  "Such virtues order and connection bring,
   From common arguments such honours spring"
```

---

## 4. Narrative Structure

### 4.1 In Medias Res (The Epic Opening)

```
ANTI-PATTERN: The Cyclic Poet's Error

BAD_OPENING:
  "The fall of Priam, the great Trojan King!
   Of the right noble Trojan War, I sing!"
   
RESULT:
  "The mountains labour! hush'd are all the spheres!
   And, oh ridiculous! a mouse appears."
   
GOOD_OPENING (Homer's Method):
  "Say, Muse, the Man, who, after Troy's disgrace,
   In various cities mark'd the human race!"
   
PRINCIPLES:
  1. Do NOT begin with Meleager's death (prehistory)
  2. Do NOT trace from "the Double Egg" (Leda, absolute origin)
  3. DO: "Still hurrying to th' event, at once he brings
         His hearer to the heart and soul of things"
         
LATIN_FORMULA:
  "Semper ad eventum festinat; et in medias res,
   Non secus ac notas, auditorem rapit"
   
  "Always hastens to the event; and into the midst of things,
   as if already known, carries the listener"
```

### 4.2 The Light-from-Smoke Principle

```
METAPHOR:
  BAD: flame to smoke (promise to disappointment)
  GOOD: smoke to light (modest opening to brilliant development)
  
HOMER'S_METHOD:
  "Not flame to smoke he turns, but smoke to light,
   Kindling from thence a stream of glories bright:
   Antiphates, the Cyclops, raise the theme;
   Scylla, Charibdis, fill the pleasing dream."
   
IMPLEMENTATION:
  def structure_narrative():
    opening = modest_but_intriguing()
    development = escalating_wonders()
    
    # What won't bear the light: hide
    weak_material = identify_weak_passages()
    shadow_flings(weak_material)
    
    # Blend fiction and truth
    blend(fiction, truth, consistency=True)
    
    return "True to one point, persu'd from end to end"
```

### 4.3 Show vs Tell Decision Tree

```
PRINCIPLE:
  "Events are on the stage in act display'd,
   Or by narration, if unseen, convey'd."
   
IMPACT_COMPARISON:
  visual_display.impact > narration.impact
  
  "Cold is the tale distilling thro' the ear,
   Filling the soul with less dismay and fear,
   Than where spectators view, like standers-by,
   The deed submitted to the faithful eye."
   
EXCEPTION_RULE (Must NOT Show):
  | Event | Reason |
  |-------|--------|
  | Medea killing children | Too horrible |
  | Atreus cooking human flesh | Too revolting |
  | Progne becoming bird | Incredible transformation |
  | Cadmus becoming snake | Incredible transformation |
  
  "Who on Medea's parricide can look?
   View horrid Atreus human garbage cook?"
   
RESULT_OF_VIOLATION:
  "My faith revolts; and I condemn outright
   The fool that shews me such a silly sight."
   
DECISION_TREE:
  IF event.type = transformation OR event.type = atrocity:
    method = NARRATION ("touching Eloquence in time unfold")
  ELSE IF event.impact_on_audience = positive:
    method = SHOW
  ELSE:
    method = evaluate_on_case_basis
```

---

## 5. Dramatic Structure Rules

### 5.1 The Five-Act Law

```
RULE:
  "Let not your play have fewer acts than five,
   Nor more, if you would wish it run and thrive!"
   
CONSTRAINT:
  acts.count >= 5
  acts.count <= 5
  
THEREFORE:
  acts.count == 5
```

### 5.2 The Deus Ex Machina Prohibition

```
RULE:
  "Draw down no God, unworthily betray'd,
   To lend his minist'ring and mischievous aid"
   
CONDITION:
  "Nec Deus intersit, nisi dignus vindice nodus"
  "Let no god intervene, unless a knot worthy of such a deliverer"
  
IMPLEMENTATION:
  IF plot_problem.solvable_by_human_means:
    solution = human_agency
  ELIF plot_problem.magnitude = cosmic:
    solution = divine_intervention (PERMITTED)
  ELSE:
    RESTRUCTURE_PLOT
```

### 5.3 The Fourth Actor Limit

```
RULE:
  "nec quarta loqui persona laboret"
  "nor let a fourth actor struggle to speak"
  
PRACTICAL_LIMIT:
  speaking_actors_simultaneous <= 3
```

### 5.4 The Chorus Function

```
CHORUS_REQUIREMENTS:
  1. Integral to action (not mere interlude)
  2. Supports virtuous characters
  3. Maintains proper moral stance
  4. Fills time between acts appropriately
  
CHORUS_CONTENT:
  - Praise temperance
  - Sing of justice and law
  - Celebrate peace
  - Invoke heaven for the unhappy
  - Call vengeance on the proud
  
ANTI-PATTERN (Agathon's Error):
  Songs unrelated to plot
  "Interlude songs" transferable between plays
```

---

## 6. Emotional Truth

### 6.1 The Sympathy Principle

```
RULE:
  "'Tis not enough that Plays are polish'd, chaste,
   Or trickt in all the harlotry of taste,
   They must have passion too"
   
MECHANISM:
  "With those that smile, our face in smiles appears;
   With those that weep, our cheeks are bath'd in tears"
   
IMPLEMENTATION:
  audience.emotion = mirror(character.emotion)
  
REQUIREMENT_FOR_WRITER:
  "To make me grieve, be first your anguish shown,
   And I shall feel your sorrows like my own."
   
  "si vis me flere, dolendum est / Primum ipsi tibi"
  "If you wish me to weep, you yourself must first feel grief"
```

### 6.2 The Authenticity Test

```
FAILURE_CONDITION:
  "Peleus, and Telephus! unless your stile
   Suit with your circumstance, I'll sleep, or smile."
   
WHEN_WORDS_BELIE_STATE:
  audience_response = ridicule OR boredom
  
TEST:
  def authenticate_emotion(character, speech):
    if speech.emotional_register != character.situation:
      return FAILURE
    if speech.words != speech.facial_expression:
      return FAILURE
    return PASS
```

---

## 7. Diction and Style

### 7.1 The Word Selection Algorithm

```
RULE: Words must be appropriate to purpose

NEOLOGISM_PERMISSION:
  "New words may, Pisos, oft by leave be fram'd"
  
CONDITION:
  1. Derived from Greek sources
  2. "With modesty and judgment be 'applied"
  
CURRENCY_OF_LANGUAGE:
  "The works of mortal man shall all decay;
   And words are grac'd and honour'd but a day"
   
  "Many shall rise again, that now are dead;
   Many shall fall, that now hold high the head"
   
ARBITER:
  "Custom alone their rank and date can teach,
   Custom, the sov'reign, law, and rule of speech"
```

### 7.2 Genre-Meter Matching

```
METER_TABLE:
  | Genre | Meter | Purpose |
  |-------|-------|---------|
  | Epic | Hexameter | "For deeds of kings and chiefs" |
  | Elegy | Elegiac couplets | Mourning, then celebration |
  | Satire | Iambic | Attack, dialogue, action |
  | Ode/Lyric | Various | "Gods, sons of Gods, victors, love, wine" |
  | Drama | Iambic trimeter | "apt for business or discourse" |

IAMBIC_SPECIFICS:
  - Quick, tripping measure
  - Suitable for dialogue
  - Admits spondees for gravity
  - "Shap'd dialogue; and still'd the noisy croud"
```

### 7.3 The Satyr Play Balance

```
CONTEXT: Satyr drama (tragicomedy)

CHALLENGE:
  Mix gravity with jest without:
  1. Debasing noble characters
  2. Becoming vulgar
  
ANTI-PATTERNS:
  | Error | Description |
  |-------|-------------|
  | Too low | God/hero speaks like tavern dweller |
  | Too high | "Grasping clouds and empty air" |
  | Vulgar | Breaking "dull jests to make the vulgar smile" |
  | Too tender | "Verses that run upon too tender feet" |

CORRECT_BALANCE:
  "Stern Tragedy rejects too light a vein:
   Like a grave Matron, destin'd to advance
   On solemn festivals to join the dance,
   Mixt with the shaggy tribe of Satyrs rude,
   She'll hold a sober mien, and act the prude."
```

---

## 8. The Labor Principle

### 8.1 The Nine-Year Rule

```
RULE:
  "Weigh the work well; and keep it back nine years!"
  "nonumque prematur in annum"
  
RATIONALE:
  "Papers unpublish'd you may blot or burn:
   A word, once utter'd, never can return."
   
IMPLEMENTATION:
  def publication_readiness(work):
    drafts = 0
    revisions = 0
    time_elapsed = 0
    
    while time_elapsed < NINE_YEARS:
      work = revise(work)
      work = seek_feedback(work, critics=[Metius, Father, Horace])
      revisions += 1
      
    if work.quality >= THRESHOLD:
      return READY
    else:
      return DELETE
```

### 8.2 The File and Polish Metaphor

```
LATIN:
  "limae labor et mora"
  "the labor and delay of the file"
  
APPLICATION:
  "Had they not, scorning the laborious file,
   Grudg'd time, to mellow and refine their stile"
   
STANDARD:
  "Never the verse approve and hold as good,
   'Till many a day, and many a blot has wrought
   The polish'd work, and chasten'd ev'ry thought,
   By tenfold labour to perfection brought!"
   
CONTRAST_WITH_CARELESSNESS:
  "scenes o'erloaded with a verse of lead,
   A mass of heavy numbers on their head,
   Speak careless haste, neglect in ev'ry part,
   Or shameful ignorance of the Poet's art."
```

### 8.3 The Greek Model Directive

```
COMMAND:
  "Pisos! be Graecian models your delight!
   Night and day read them, read them day and night!"
   
  "Vos exemplaria Graeca
   NocturnÃ¢ versate manu, versate diurnÃ¢"
   
CONTRAST_WITH_ROMAN_TENDENCY:
  Romans praised Plautus "with a too partial eye"
  "Fond e'en to folly sure"
```

---

## 9. The Critic Function

### 9.1 The True Critic Algorithm

```
QUINTILIUS_METHOD:
  INPUT: poet recites work
  
  PROCESS:
    FOR passage in work:
      IF passage.flawed:
        SAY: "Prithee, alter this! and make that right!"
        
    IF poet.claims_unable_to_improve:
      IF attempts >= 2-3:
        SAY: "Then blot it out! Back to the anvil!"
        
    IF poet.defends_error RATHER THAN mend:
      RESPONSE: silence
      "left you to admire yourself and book"
      
TRUE_CRITIC_QUALITIES:
  "The Man, in whom Good Sense and Honour join"
  
ACTIONS:
  1. "Will blame the harsh"
  2. "Reprove the idle line"
  3. "Erase the rude" (lacking grace)
  4. "Lop away ambitious ornaments"
  5. "Make you let in day" on obscure passages
  6. "Not admit loose and ambiguous terms"
  7. "Take due note of ev'ry change that's fit"
  8. Become "A very ARISTARCHUS"
  
ANTI-PATTERN (False Kindness):
  "Why give my friend offence? These are but trifles!"
  
CONSEQUENCE_OF_FALSE_KINDNESS:
  "these trifles lead
   To serious mischiefs, if he don't succeed;
   While the poor friend in dark disgrace sits down,
   The butt and laughing-stock of all the town"
```

### 9.2 The Flatterer Warning

```
DANGER: Poets with wealth attract sycophants

"As the sly Hawker, who a sale prepares,
 Collects a croud of bidders for his Wares,
 The Poet, warm in land, and rich in cash,
 Assembles flatterers, brib'd to praise his trash."

DETECTION_METHOD (Kings' Wine Test):
  "Kings have been said to ply repeated bowls,
   Urge deep carousals, to unlock the souls
   Of those, whose loyalty they wish'd to prove"
   
APPLICATION:
  "Beware the Spaniel with the Fox's mind!"
  
SIGNS_OF_FLATTERY:
  - Excessive enthusiasm: "Good! rare! divine!"
  - Physical performance: leaping, bounding, tears
  - "More mov'd appears the laugher in his sleeve,
    Than those who truly praise, or smile, or grieve"
```

---

## 10. The Wisdom Foundation

### 10.1 Knowledge Before Expression

```
FOUNDATIONAL_PRINCIPLE:
  "Scribendi rectÃ¨, sapere est et principium et fons"
  "To write well, wisdom is both beginning and source"
  
  "In Wisdom, Moral Wisdom, to excell,
   Is the chief cause and spring of writing well."
   
METHOD:
  "Draw elements from the Socratick source,
   And, full of matter, words will rise of course."
   
REQUIRED_KNOWLEDGE:
  | Domain | Content |
  |--------|---------|
  | Patriotism | "a patriot's glorious flame" |
  | Friendship | "what friendship asks" |
  | Family | "what filial duties claim" |
  | Kinship | "ties of blood" |
  | Humanity | "links that bind / The heart to strangers" |
  | Politics | "Senator's, the Judge's peaceful care" |
  | War | "sterner duties of the Chief in war" |
  
APPLICATION:
  "These who hath studied well, will all engage
   In functions suited to their rank and age."
```

### 10.2 Nature as Model

```
DIRECTIVE:
  "On Nature's pattern too I'll bid him look,
   And copy manners from her living book."
   
  "Respicere exemplar vitae morumque jubebo
   Doctum imitatorem, et veras hinc ducere voces"
   
OBSERVATION:
  "Sometimes 'twill chance, a poor and barren tale,
   Where neither excellence nor art prevail,
   With now and then a passage of some merit,
   And Characters sustain'd, and drawn with spirit,
   Pleases the people more, and more obtains,
   Than tuneful nothings, mere poetick strains."
   
HIERARCHY:
  truthful_character_drawing > mere_metrical_virtuosity
```

---

## 11. The Social Function of Poetry

### 11.1 The Civilizing Power

```
HISTORICAL_FUNCTION:
  Orpheus: "The barb'rous natives of the shaggy wood
           From horrible repasts, and acts of blood...
           a priest, and heav'nly teacher, brought,
           And all the charities of nature taught"
           
  RESULT: "said fierce tigers to allay"
  
  Amphion: "Within the hollow of AMPHION'S shell
           Such pow'rs of sound were lodg'd, so sweet a spell!
           That stones were said to move, and at his call,
           Charm'd to his purpose, form'd the Theban Wall."
           
CIVILIZING_TASKS:
  1. "mark the limits" between public and private good
  2. "raise a pale" between sacred and profane
  3. "shew the ills Promiscuous Love should dread"
  4. "teach the laws of the Connubial Bed"
  5. "Mankind dispers'd, to Social Towns to draw"
  6. "on the Sacred Tablet grave the Law"
  
CONSEQUENCE:
  "Thus fame and honour crown'd the Poet's line;
   His work immortal, and himself divine!"
```

---

## 12. The Mad Poet (Anti-Pattern)

### 12.1 Portrait of the Afflicted Poet

```
SYMPTOMS:
  1. Neglects grooming: "nails who will not pare, / Or trim their beards"
  2. Avoids society: "secreta petit loca, balnea vitat"
  3. Believes madness = genius (Democritus fallacy)
  
PUBLIC_RESPONSE:
  "A Frantick Bard puts men of sense to flight;
   His slaver they detest, and dread his bite:
   All shun his touch; except the giddy boys,
   Close at his heels, who hunt him down with noise"
   
BEHAVIOR:
  "with his head erect he threats the skies,
   Spouts verse, and walks without the help of eyes"
   
FATE:
  "Lost as a blackbird-catcher, should he pitch
   Into some open well, or gaping ditch"
   
HORACE'S_ADVICE:
  Let him fall. "By sheer design he jump'd into the well."
  
EMPEDOCLES_EXAMPLE:
  "ambitious to be thought A God"
  "Lead'p coldly into Aetna's burning mount"
```

### 12.2 The Leech Metaphor

```
FINAL_IMAGE:
  "Quem vero arripuit, tenet, occiditque legendo,
   Non missura cutem, nisi plena cruoris, hirudo"
   
  "When he catches someone, he holds on and kills by reading,
   A leech that won't release the skin until full of blood"
   
WARNING: The bad poet destroys both self and audience
```

---

## Appendix A: Quick Reference Card

### Core Tests

| Test | Question |
|------|----------|
| Unity | "Is every part essential to one simple whole?" |
| Chimera | "Do all elements share a coherent design domain?" |
| Purple Patch | "Does this brilliance serve the whole?" |
| Decorum | "Does style fit genre, character, and situation?" |
| Consistency | "Does character remain true from start to finish?" |
| Sympathy | "Does the writer feel what they ask audience to feel?" |
| Labor | "Has this been polished to tenfold perfection?" |

### The Canonical Horatian Process

```
1. FOUNDATION
   - Master wisdom first (Socratic sources)
   - Study Greek models (night and day)
   
2. CONCEPTION
   - Choose subject within your powers
   - Plan unity from the start
   
3. COMPOSITION
   - Begin in medias res
   - Blend fiction with truth
   - Maintain decorum throughout
   
4. REVISION
   - Seek honest critics (not flatterers)
   - Apply the file and polish
   - Delete purple patches
   
5. JUDGMENT
   - Wait (up to nine years)
   - Test against standards
   - If mediocre: destroy
```

### The Hierarchies

```
DUAL_REQUIREMENT:
  Genius + Labor = Poetry
  (Neither alone suffices)
  
DUAL_PURPOSE:
  Instruct + Delight = Optimal
  (Either alone acceptable, both preferred)
  
PRIORITY_ORDER:
  Moral_truth > Metrical_virtuosity
  Character_consistency > Isolated_brilliance
  Unity > Diversity
  Greek_standards > Roman_indulgence
  
QUALITY_THRESHOLD:
  Excellence = acceptable
  Mediocrity = unacceptable
  (No middle ground)
```

### The Warnings

| Anti-Pattern | Description |
|--------------|-------------|
| Chimera | Incongruous elements joined |
| Purple Patch | Brilliance unserved by whole |
| Mountains â†’ Mouse | Grand opening, trivial delivery |
| Flame â†’ Smoke | Promise decaying to disappointment |
| Mad Poet | Genius without discipline |
| Flatterer | Praise without judgment |
| False Friend | Kindness enabling failure |

---

## Appendix B: Horatian Validation Checklist

```python
def validate_work(work):
    checks = [
        # Unity
        ("Single unified design", unity_test),
        ("No chimeric elements", chimera_test),
        ("No purple patches", purple_patch_test),
        ("Congruent beginning/middle/end", congruity_test),
        
        # Decorum
        ("Style matches genre", genre_style_test),
        ("Speech matches character type", character_speech_test),
        ("Expression matches emotion", emotion_expression_test),
        ("Age-appropriate traits", lifecycle_test),
        
        # Character
        ("Traditional characters follow fame", tradition_test),
        ("Consistent throughout", consistency_test),
        
        # Structure  
        ("In medias res opening", opening_test),
        ("Smoke to light progression", progression_test),
        ("Show/tell appropriateness", presentation_test),
        ("Five acts (if drama)", act_count_test),
        ("No unworthy deus ex machina", deus_test),
        
        # Emotional Truth
        ("Writer felt first", sympathy_test),
        ("Authentic expression", authenticity_test),
        
        # Craft
        ("Appropriate diction", diction_test),
        ("Proper meter for genre", meter_test),
        ("Labor applied", revision_test),
        
        # Quality
        ("Exceeds mediocrity threshold", excellence_test),
    ]
    
    return all(test(work) for name, test in checks)
```

---

## Appendix C: Theoretical Correspondence Table

| Horace | Aristotle | McKee | South Park | Waller-Bridge |
|--------|-----------|-------|------------|---------------|
| Unity (simplex et unum) | Unity of action | Spine/through-line | Central question | Want vs. need |
| Decorum | Propriety | Character logic | Character consistency | Voice authenticity |
| In medias res | â€” | Inciting incident | Hook/cold open | Scene launch |
| Labor/file | â€” | Revision/drafts | Rewrite room | Edit discipline |
| Instruct + Delight | Catharsis | Entertainment + meaning | Message + funny | Emotional + insight |
| Greek models | â€” | Master storytellers | Classic episodes | Theatrical tradition |
| No mediocrity | Excellence threshold | Quality standard | "Good enough" rejection | Craft obsession |
| Sympathy principle | Emotional identification | Empathy for protagonist | Emotional grounding | Audience connection |
| Character consistency | Character consistency | Arc integrity | Character bible | Character logic |
| Nine-year rule | â€” | Patience/timing | Development cycles | Gestation period |

## Structural Hierarchy

The work must function as **ONE_SIMPLE_WHOLE**, a unified design. Within this whole, dramatic works are divided into five **ACT** segments. Each part of the action is a **SCENE** (displayed or narrated), and the atomic level is **DICTION** (word choice and meter).

---

## Diagnostic Questions

1. **Is every part of the work essential to one simple whole?** (YES)
2. **Do the style and speech match the character's age, rank, and situation (Decorum)?** (YES)
3. **Does the work enter 'in medias res' (into the heart of things)?** (YES)
4. **Are 'purple patches' (isolated brilliant but non-functional passages) removed?** (YES)
5. **Does the work aim to both instruct and delight?** (YES)
6. **Has the 'labor of the file' been applied to achieve tenfold perfection?** (YES)

---

## Appendix D: Key Latin Phrases

| Latin | Translation | Application |
|-------|-------------|-------------|
| *Aut prodesse aut delectare* | "Either to benefit or to delight" | Dual purpose of poetry |
| *Omne tulit punctum qui miscuit utile dulci* | "He wins every vote who blends useful with pleasant" | Optimal combination |
| *Simplex dumtaxat et unum* | "One simple whole" | Unity principle |
| *In medias res* | "Into the middle of things" | Narrative entry point |
| *Ut pictura poesis* | "As is painting, so is poetry" | Art correspondence |
| *Limae labor et mora* | "Labor and delay of the file" | Revision discipline |
| *Nonum prematur in annum* | "Let it be suppressed until the ninth year" | Patience rule |
| *Si vis me flere, dolendum est primum ipsi tibi* | "If you wish me to weep, you must first feel grief yourself" | Sympathy principle |
| *Purpureus pannus* | "Purple patch" | Warning against unintegrated brilliance |

---

*Compiled from Horace. Ars Poetica (Epistula ad Pisones). ~19 BCE. George Colman translation (1783).*
*Project Gutenberg eBook #9175*
