# Bharata Muni's Narratological Algorithms

A systematic distillation of Bharata Muni's *Natyasastra* (~200 BCE â€“ 200 CE) into formal, implementable principles for dramatic composition and narrative affect generation. Based on the Manomohan Ghosh translation.

---

## 0. Meta-Principles (Axioms)

The *Natyasastra* operates from foundational assumptions about the nature of dramatic representation, emotional experience, and aesthetic pleasure.

| Axiom | Formulation |
|-------|-------------|
| B0 | Drama (Natya) is **mimicry** (anukarana) of the exploits of gods, Asuras, kings, and householders |
| B1 | Drama exists to provide **satisfaction** to people of differing tastes in one place |
| B2 | The **Sentiment** (rasa) is the soul of dramaâ€”no meaning proceeds without it |
| B3 | Sentiments arise from **States** (bhava), not States from Sentiments |
| B4 | Aesthetic experience is **tasted** (asvadayanti)â€”like culinary flavor from combined ingredients |
| B5 | Successful representation requires **both** realistic (lokadharmi) and conventional (natyadharmi) practices |
| B6 | The ultimate court of appeal concerning dramatic practice is **the people** |

### 0.1 The Cooking Analogy (Central Metaphor)

```
GIVEN:
  - culinary taste (rasa) results from combining spices, vegetables, and other articles
  - six distinct tastes emerge from specific ingredient combinations
  
WHEN:
  - Dominant States (sthayibhava) combine with:
    - Determinants (vibhava)
    - Consequents (anubhava)
    - Transitory States (vyabhicaribhava)
    
THEN:
  - Dominant States "attain the quality of Sentiment"
  - Spectators "taste" these Sentiments through representation
  
THEREFORE:
  rasa_production = combine(sthayibhava, vibhava, anubhava, vyabhicari)
  aesthetic_pleasure = spectator.taste(rasa)
```

### 0.2 The Universality Principle

```
CONDITION_FOR_RASA:
  States become Sentiments WHEN:
    imbued_with(quality_of_universality = True)  # samanya/siddhartha
    
RATIONALE:
  - Personal emotion (bhava) = particular, individual
  - Aesthetic emotion (rasa) = universal, shared
  
TRANSFORMATION:
  def bhava_to_rasa(state, representation):
      if representation.achieves_universality():
          return Sentiment(state)
      else:
          return state  # remains particular, not aesthetic
```

---

## 1. Rasa Theory: The Eight Sentiments

### 1.1 The Canonical Eight

| # | Rasa | English | Dominant State | Color | Presiding Deity |
|---|------|---------|----------------|-------|-----------------|
| 1 | Åšá¹›á¹…gÄra | Erotic | Love (rati) | Bright/Green | Viá¹£á¹‡u |
| 2 | HÄsya | Comic | Mirth (hÄsa) | White | Pramathas |
| 3 | Karuá¹‡a | Pathetic | Sorrow (Å›oka) | Ash-colored | Rudra |
| 4 | Raudra | Furious | Anger (krodha) | Red | Yama |
| 5 | VÄ«ra | Heroic | Energy (utsÄha) | Light orange | Indra |
| 6 | BhayÄnaka | Terrible | Fear (bhaya) | Black | KÄla |
| 7 | BÄ«bhatsa | Odious | Disgust (jugupsÄ) | Blue | Åšiva |
| 8 | Adbhuta | Marvellous | Astonishment (vismaya) | Yellow | Brahman |

### 1.2 The Four Primary â†’ Eight Derived

```
PRIMARY_SENTIMENTS = {Raudra, VÄ«ra, BÄ«bhatsa, Åšá¹›á¹…gÄra}

DERIVATION_MAP:
  Åšá¹›á¹…gÄra â†’ HÄsya     # Comic derives from Erotic (mimicry of love)
  Raudra  â†’ Karuá¹‡a    # Pathetic derives from Furious (result of anger)
  VÄ«ra    â†’ Adbhuta   # Marvellous derives from Heroic (result of heroism)
  BÄ«bhatsa â†’ BhayÄnaka # Terrible derives from Odious

MECHANISM:
  derived_rasa = transform(primary_rasa, mode)
  WHERE mode IN {mimicry, result, consequence}
```

### 1.3 Rasa Evocation Formula

```python
def evoke_rasa(target_sentiment):
    """
    The canonical formula for producing aesthetic experience.
    """
    # Step 1: Identify the Dominant State
    sthayibhava = DOMINANT_STATE_MAP[target_sentiment]
    
    # Step 2: Establish Determinants (causes/stimuli)
    vibhavas = select_determinants(target_sentiment)
    
    # Step 3: Express through Consequents (reactions/expressions)
    anubhavas = select_consequents(target_sentiment)
    
    # Step 4: Color with Transitory States
    vyabhicaris = select_compatible_transitory_states(target_sentiment)
    
    # Step 5: Combine through representation
    return combine_through_abhinaya(
        sthayibhava,
        vibhavas,
        anubhavas,
        vyabhicaris
    )
```

---

## 2. Bhava Theory: The Forty-Nine States

### 2.1 Taxonomy of States

```
STATES (Bhava) = 49 total

â”œâ”€â”€ DOMINANT STATES (SthÄyibhÄva): 8
â”‚   â””â”€â”€ Love, Mirth, Sorrow, Anger, Energy, Fear, Disgust, Astonishment
â”‚
â”œâ”€â”€ TRANSITORY STATES (VyabhicÄribhÄva): 33
â”‚   â””â”€â”€ Discouragement, Weakness, Apprehension, Envy, Intoxication,
â”‚       Weariness, Indolence, Depression, Anxiety, Distraction,
â”‚       Recollection, Contentment, Shame, Inconstancy, Joy, Agitation,
â”‚       Stupor, Arrogance, Despair, Impatience, Sleep, Epilepsy,
â”‚       Dreaming, Awakening, Indignation, Dissimulation, Cruelty,
â”‚       Assurance, Sickness, Insanity, Death, Fright, Deliberation
â”‚
â””â”€â”€ TEMPERAMENTAL STATES (SÄttvikabhÄva): 8
    â””â”€â”€ Paralysis (stambha), Perspiration (sveda), Horripilation (romÄÃ±ca),
        Change of Voice (svarabheda), Trembling (vepathu),
        Change of Colour (vaivará¹‡ya), Weeping (aÅ›ru), Fainting (pralaya)
```

### 2.2 The Hierarchy of States

```
ANALOGY: King and Attendants

JUST_AS:
  - Among persons of similar characteristics
  - Some attain KINGSHIP (due to birth, manners, learning, skill)
  - Others become ATTENDANTS (due to inferior intellect)

SO_TOO:
  DOMINANT_STATES = "kings"
    - All other states DEPEND on them
    - They alone become SENTIMENTS
    
  DETERMINANTS_AND_CONSEQUENTS = "local officers"
    - Support the Dominant States
    
  TRANSITORY_STATES = "attendants"
    - Serve the Dominant States
    - "Carry" the Sentiment through representation

RULE:
  "Just as only a king surrounded by numerous attendants 
   receives this epithet [of king] and not any other man,
   so the Dominant States only followed by Determinants,
   Consequents and Transitory States receive the name of Sentiment."
```

### 2.3 VibhÄva (Determinants) â€” Causes

```python
DETERMINANT_PATTERNS = {
    'erotic': [
        'pleasures_of_season', 'garlands', 'unguents', 'ornaments',
        'beloved_persons', 'splendid_mansions', 'gardens',
        'seeing_beloved', 'hearing_beloved_words', 'playing', 'dallying'
    ],
    'comic': [
        'unseemly_dress', 'impudence', 'greediness', 'quarrel',
        'defective_limb', 'irrelevant_words', 'mentioning_faults'
    ],
    'pathetic': [
        'affliction_under_curse', 'separation_from_dear_ones',
        'loss_of_wealth', 'death_of_beloved', 'captivity'
    ],
    'furious': [
        'anger', 'rape', 'abuse', 'insult', 'untrue_allegation',
        'threatening', 'revengefulness', 'jealousy'
    ],
    'heroic': [
        'presence_of_mind', 'perseverance', 'diplomacy', 'discipline',
        'military_strength', 'aggressiveness', 'reputation_of_might'
    ],
    'terrible': [
        'hideous_noise', 'sight_of_ghosts', 'panic', 'empty_house',
        'forest', 'death_of_dear_ones', 'owl_cry', 'jackal_cry'
    ],
    'odious': [
        'hearing_unpleasant_things', 'seeing_unpleasant_things',
        'offensive_objects', 'impure_objects', 'harmful_things'
    ],
    'marvellous': [
        'illusion', 'magic', 'extraordinary_feats',
        'great_excellence_in_painting', 'art_works'
    ]
}
```

### 2.4 AnubhÄva (Consequents) â€” Expressions

```python
CONSEQUENT_PATTERNS = {
    'erotic': [
        'clever_eye_movements', 'eyebrow_movements', 'glances',
        'soft_limb_movements', 'sweet_words'
    ],
    'comic': [
        'throbbing_lips', 'throbbing_nose', 'throbbing_cheek',
        'wide_eyes', 'contracted_eyes', 'perspiration',
        'face_colour_change', 'holding_sides'
    ],
    'pathetic': [
        'shedding_tears', 'lamentation', 'bewailing', 'change_of_colour',
        'loss_of_voice', 'loose_limbs', 'falling_on_ground',
        'crying', 'deep_breathing', 'paralysis'
    ],
    'furious': [
        'red_eyes', 'knitting_eyebrows', 'defiance', 'biting_lips',
        'cheek_movement', 'pressing_hands_together'
    ],
    'heroic': [
        'firmness', 'patience', 'heroism', 'charity', 'diplomacy'
    ],
    'terrible': [
        'trembling_hands_feet', 'horripilation', 'change_of_colour',
        'loss_of_voice', 'palpitation', 'dry_mouth'
    ],
    'odious': [
        'contracting_limbs', 'narrowing_mouth', 'vomiting',
        'spitting', 'shaking_limbs'
    ],
    'marvellous': [
        'wide_opening_eyes', 'looking_without_winking',
        'eyebrow_movement', 'horripilation', 'head_moving',
        'cry_of_well_done'
    ]
}
```

### 2.5 Compatible Transitory States

```python
TRANSITORY_COMPATIBILITY = {
    'erotic_union': EXCLUDE(['fear', 'indolence', 'cruelty', 'disgust']),
    'erotic_separation': [
        'indifference', 'langour', 'fear', 'jealousy', 'fatigue',
        'anxiety', 'yearning', 'drowsiness', 'sleep', 'dreaming',
        'awakening', 'illness', 'insanity', 'epilepsy', 'inactivity',
        'fainting', 'death'
    ],
    'comic': [
        'indolence', 'dissimulation', 'drowsiness', 'sleep',
        'dreaming', 'insomnia', 'envy'
    ],
    'furious': [
        'presence_of_mind', 'determination', 'energy', 'indignation',
        'restlessness', 'fury', 'perspiration', 'trembling',
        'horripilation', 'choking_voice'
    ],
    'heroic': [
        'contentment', 'judgement', 'pride', 'agitation', 'energy',
        'ferocity', 'indignation', 'remembrance', 'horripilation'
    ],
    'terrible': [
        'paralysis', 'perspiration', 'choking_voice', 'horripilation',
        'trembling', 'loss_of_voice', 'change_of_colour', 'fear',
        'stupefaction', 'dejection', 'agitation', 'restlessness',
        'inactivity', 'epilepsy', 'death'
    ],
    'odious': [
        'epilepsy', 'delusion', 'agitation', 'fainting',
        'sickness', 'death'
    ]
}
```

---

## 3. Abhinaya: The Four Modes of Representation

### 3.1 The Quadripartite System

```
ABHINAYA (Histrionic Representation) = {
    Ä€á¹„GIKA:   Gestures â€” physical expression through body movements
    VÄ€CIKA:   Words â€” verbal expression through speech
    Ä€HÄ€RYA:   Costumes & Make-up â€” visual expression through appearance
    SÄ€TTVIKA: Temperament â€” psychological expression through inner states
}

DISTRIBUTION:
  Each mode contributes to total dramatic effect
  All four must work in HARMONY
  Different situations emphasize different modes
```

### 3.2 Ä€á¹…gika (Gestural Representation)

```python
class AngikAbhinaya:
    """
    Physical representation through major and minor limbs.
    """
    MAJOR_LIMBS = ['head', 'hands', 'chest', 'sides', 'waist', 'feet']
    MINOR_LIMBS = ['eyes', 'eyebrows', 'nose', 'lips', 'cheeks', 'chin']
    
    def select_gesture(self, sentiment, character_type, situation):
        """
        Gestures must match sentiment, character status, and context.
        """
        base_gesture = GESTURE_LIBRARY[sentiment]
        
        # Adjust for character type
        if character_type == 'superior':
            return refine(base_gesture, subtlety='high')
        elif character_type == 'middling':
            return refine(base_gesture, subtlety='medium')
        else:
            return refine(base_gesture, subtlety='low')
```

### 3.3 VÄcika (Verbal Representation)

```python
class VacikaAbhinaya:
    """
    Verbal expression including speech, intonation, and metre.
    """
    
    def configure_speech(self, sentiment):
        """
        Speech parameters vary by sentiment.
        """
        config = {
            'erotic': {'intonation': 'madhyama', 'tempo': 'medium', 'note': 'gandhara_nisada'},
            'comic': {'intonation': 'madhyama', 'tempo': 'medium', 'note': 'gandhara_nisada'},
            'pathetic': {'intonation': 'normal', 'tempo': 'slow', 'note': 'gandhara_nisada'},
            'heroic': {'intonation': 'udatta', 'tempo': 'quick', 'note': 'sadja_rsabha'},
            'furious': {'intonation': 'udatta', 'tempo': 'quick', 'note': 'sadja_rsabha'},
            'marvellous': {'intonation': 'udatta', 'tempo': 'quick', 'note': 'sadja_rsabha'},
            'terrible': {'intonation': 'normal', 'tempo': 'quick', 'note': 'sadja_rsabha'},
            'odious': {'intonation': 'normal', 'tempo': 'quick', 'note': 'sadja_rsabha'}
        }
        return config[sentiment]
```

### 3.4 Ä€hÄrya (Visual Representation)

```
COSTUME_PRINCIPLES:
  1. APPROPRIATENESS: Match costume to character's status, region, occupation
  2. CONSISTENCY: Maintain character identity throughout
  3. SIGNIFICATION: Use conventional colors for character types
  
COLOR_CODING:
  Gods         â†’ golden/yellow
  Kings        â†’ variegated, rich
  Ascetics     â†’ matted hair, bark garments
  Raksasas     â†’ black, unkempt
  Women        â†’ appropriate to status (wife, courtesan, etc.)
  
MAKE-UP:
  Apply to enhance recognition of character type
  Use conventional features for divine vs. human vs. demonic
```

### 3.5 SÄttvika (Temperamental Representation)

```python
class SattvikaAbhinaya:
    """
    The eight involuntary psychophysical responses.
    These arise from the actor's internal state (sattva/mind).
    """
    
    SATTVIKA_BHAVAS = [
        'stambha',      # Paralysis â€” immobility from emotion
        'sveda',        # Perspiration â€” spontaneous sweating
        'romanca',      # Horripilation â€” goosebumps
        'svarabheda',   # Voice change â€” breaking/trembling voice
        'vepathu',      # Trembling â€” involuntary shaking
        'vaivarnya',    # Color change â€” pallor/flushing
        'asru',         # Tears â€” weeping
        'pralaya'       # Fainting â€” loss of consciousness
    ]
    
    def represent(self, state, intensity='natural'):
        """
        Sattvika bhavas must arise from genuine internal engagement.
        Cannot be mechanically producedâ€”require actor's psychological investment.
        """
        if intensity == 'natural':
            return full_expression(state)
        elif intensity == 'feigned':
            return milder_expression(state)
```

---

## 4. DharmÄ«: The Two Practices

### 4.1 Lokadharmi (Realistic Practice)

```
DEFINITION:
  "Reproduction of natural behaviour of men and women on the stage"
  
CHARACTERISTICS:
  - Mimics everyday life actions
  - Natural speech patterns
  - Ordinary movements and gestures
  - Familiar emotional expressions
  
APPLICATION:
  - Domestic scenes
  - Conversational exchanges
  - Common activities
  - Character establishment
```

### 4.2 NÄtyadharmÄ« (Conventional Practice)

```
DEFINITION:
  "Theatrical conventions not found in ordinary life"
  
CHARACTERISTICS:
  - Stylized movement vocabulary
  - Codified gesture system
  - Dance-like quality
  - Musical accompaniment
  - Exaggerated expression
  
EXAMPLES:
  - Characters speak in verse
  - Movements timed to rhythm
  - Conventional exits/entrances
  - Symbolic space representation
  
RATIONALE:
  "The Hindu theatre recognized very clearly that drama or the Natya 
   was different from the real life and followed its own conventions."
```

### 4.3 Practice Selection Algorithm

```python
def select_dharmi(scene_type, sentiment, characters):
    """
    Determine appropriate practice for scene.
    """
    # Emotional intensity determines base practice
    if sentiment in ['erotic', 'heroic', 'furious', 'marvellous']:
        base = 'natyadharmi'  # heightened states need stylization
    else:
        base = 'lokadharmi'  # grounded states use realism
    
    # Scene type modifies
    if scene_type == 'combat' or scene_type == 'love_making':
        return 'natyadharmi'  # always stylized
    elif scene_type == 'domestic':
        return 'lokadharmi'  # always realistic
    else:
        return blend(base, scene_requirements)
```

---

## 5. Vá¹›tti: The Four Styles

### 5.1 Style Classification

| Style | Sanskrit | Characteristics | Primary Sentiments |
|-------|----------|-----------------|-------------------|
| Verbal | BhÄratÄ« | Dialogue-dominant, Sanskrit emphasis | All (universal base) |
| Grand | SÄttvatÄ« | Noble characters, exalted speech, gestures | Heroic, Marvellous, Furious |
| Graceful | KaiÅ›ikÄ« | Charming costumes, dance, female characters | Erotic, Comic |
| Energetic | Ä€rabhaá¹­Ä« | Bold presentation, battles, conflicts | Terrible, Furious |

### 5.2 Style-Sentiment Mapping

```python
STYLE_SENTIMENT_MAP = {
    'bharati': {
        'description': 'Speech-centered, intellectual engagement',
        'sentiments': ['all'],
        'features': ['elaborate_dialogue', 'sanskrit_predominant', 'minimal_dance']
    },
    'sattvati': {
        'description': 'Grand manner for noble themes',
        'sentiments': ['heroic', 'marvellous', 'furious'],
        'features': ['exalted_characters', 'dignified_gestures', 'elevated_diction']
    },
    'kaisiki': {
        'description': 'Graceful manner for love and humor',
        'sentiments': ['erotic', 'comic'],
        'features': ['charming_costumes', 'dance_emphasis', 'female_centered', 'love_themes']
    },
    'arabhati': {
        'description': 'Energetic manner for conflict',
        'sentiments': ['terrible', 'furious'],
        'features': ['bold_presentation', 'battle_scenes', 'physical_intensity']
    }
}

def select_style(dominant_sentiment, play_type, act_number):
    """
    Styles are not mutually exclusiveâ€”blend according to scene needs.
    """
    primary_style = STYLE_SENTIMENT_MAP.get_primary(dominant_sentiment)
    
    # Different acts may emphasize different styles
    # A single play often uses multiple styles across its acts
    return blend_styles(primary_style, scene_requirements)
```

---

## 6. Vastu: Plot Structure

The primary unit of dramatic plot is the **VASTU**. The most complete form of this structure is the **NATAKA**.

### 6.1 The Five Stages of Action

```
HERO'S_EXERTION = [
    1. Ä€RAMBHA (Beginning)      â€” Initial impulse toward the goal
    2. PRAYATNA (Effort)        â€” Active pursuit of the objective
    3. PRÄ€PTI-SAMBHAVA          â€” Possibility of attainment appears
       (Possibility of Attainment)
    4. NIYATÄ€PTI                â€” Certainty of attainment emerges
       (Certainty of Attainment)
    5. PHALÄ€GAMA                â€” Actual attainment of the result
       (Attainment of Result)
]
```

### 6.2 The Five Elements of Plot

```python
PLOT_ELEMENTS = {
    'bija': {
        'name': 'Germ/Seed',
        'function': 'Initial cause that generates entire action',
        'placement': 'Opening'
    },
    'bindu': {
        'name': 'Point/Drop',
        'function': 'Maintains continuity when action seems interrupted',
        'placement': 'Throughout (as needed)'
    },
    'pataka': {
        'name': 'Episode/Banner',
        'function': 'Subsidiary narrative supporting main action',
        'placement': 'Development'
    },
    'prakari': {
        'name': 'Episodical Incident',
        'function': 'Minor incident within episode',
        'placement': 'Development'
    },
    'karya': {
        'name': 'Denouement',
        'function': 'Final resolution of action',
        'placement': 'Conclusion'
    }
}
```

### 6.3 The Five Junctures (Sandhi)

```python
SANDHIS = {
    'mukha': {
        'name': 'Opening',
        'function': 'Introduces germ (bija) of the plot',
        'stage_correspondence': 'Ärambha',
        'contains': ['bija_introduction', 'hero_establishment']
    },
    'pratimukha': {
        'name': 'Progression',
        'function': 'Germ begins to sprout, action advances',
        'stage_correspondence': 'prayatna',
        'contains': ['complication_introduction', 'bindu_development']
    },
    'garbha': {
        'name': 'Development',
        'function': 'Main body of action, episodes unfold',
        'stage_correspondence': 'prapti_sambhava',
        'contains': ['pataka_episodes', 'primary_conflicts']
    },
    'vimarsa': {
        'name': 'Pause',
        'function': 'Crisis point, action seems in doubt',
        'stage_correspondence': 'niyatapti',
        'contains': ['suspense_peak', 'reversal_possibility']
    },
    'nirvahana': {
        'name': 'Conclusion',
        'function': 'Resolution, result achieved',
        'stage_correspondence': 'phalagama',
        'contains': ['denouement', 'karya_completion']
    }
}
```

### 6.4 Principal vs. Incidental Plots

The atomic unit of performance within this structure is the **SCENE**.

```python
class PlotStructure:
    """
    Dual plot architecture in dramatic composition.
    """
    
    def __init__(self):
        self.adhikarika = None  # Principal/Primary plot
        self.prasangika = []     # Incidental/Subsidiary plots
    
    def set_principal_plot(self, hero, objective, obstacles):
        """
        The adhikarika (principal) plot is obvious from its nameâ€”
        it concerns the Hero's main action.
        """
        self.adhikarika = {
            'hero': hero,
            'objective': objective,
            'obstacles': obstacles,
            'sandhis': generate_five_junctures(hero, objective)
        }
    
    def add_incidental_plot(self, characters, their_interest, hero_benefit):
        """
        Incidental plots: characters acting in their own interest
        INCIDENTALLY further the purpose of the Hero.
        """
        self.prasangika.append({
            'characters': characters,
            'their_interest': their_interest,
            'how_it_helps_hero': hero_benefit
        })
```

---

## 7. NÄá¹­aka Typology: The Ten Dramatic Forms

### 7.1 Classification Table

| Form | Acts | Hero Type | Plot Source | Dominant Elements |
|------|------|-----------|-------------|-------------------|
| NÄá¹­aka | 5-10 | Royal/divine | Celebrated legend | All sentiments (heroic dominant) |
| Prakaraá¹‡a | 5-10 | Brahmin/merchant | Original/invented | Love (bourgeois comedy) |
| SamavakÄra | 3 | God/Asura | Mythological | Deception, excitement, love |
| ÄªhÄmá¹›ga | 4 | Divine males | Divine conflict | Love, discord, intrigue |
| á¸Œima | 4 | Exalted, well-known | Well-constructed | All except Comic & Erotic |
| VyÄyoga | 1 | Well-known | Single day events | Battle, combat, conflict |
| Utsá¹›á¹£á¹­ikÄá¹…ka | 1 | Human | Well-known | Pathetic (women's lament) |
| Prahasana | 1 | Varied | Original | Comic (farce, satire) |
| BhÄá¹‡a | 1 | Single actor | Adventure | Monologue (rogue/parasite) |
| VÄ«thÄ« | 1 | 1-2 actors | Varied | Short dramatic sketch |

### 7.2 NÄá¹­aka Construction Algorithm

```python
def construct_nataka(legendary_source, hero):
    """
    The NÄá¹­aka is the most complete dramatic form.
    """
    # Validation
    assert hero.type in ['royal', 'divine_descended', 'sage_descended']
    assert legendary_source.is_celebrated == True
    
    # Structure
    nataka = {
        'acts': range(5, 11),  # 5-10 acts
        'hero': {
            'type': 'exalted',
            'character': hero,
            'death_prohibition': True  # Hero cannot die on stage
        },
        'plot': {
            'source': legendary_source,
            'junctures': generate_five_sandhis()
        },
        'constraints': {
            'location': 'India',  # Human characters placed in India
            'time_per_act': 'one_day_maximum',
            'on_stage_prohibitions': [
                'hero_death', 'battle', 'loss_of_kingdom',
                'siege', 'eating', 'bathing', 'sexual_union',
                'natural_calamity', 'degradation'
            ]
        },
        'outcome': 'hero_triumph_or_prosperity'
    }
    return nataka
```

### 7.3 On-Stage Prohibitions

```python
PROHIBITED_REPRESENTATIONS = [
    'death_of_hero',
    'actual_battle',
    'loss_of_kingdom',
    'siege_of_town',
    'eating',
    'bathing',
    'sexual_union',
    'anointing',
    'application_of_unguents',
    'natural_calamity',
    'degradation_of_hero'
]

# These may be REPORTED in Introductory Scenes (praveÅ›aka)
# but never SHOWN directly on stage

def can_show_on_stage(event):
    return event not in PROHIBITED_REPRESENTATIONS
```

---

## 8. Character Typology

### 8.1 The Three Character Types

```python
CHARACTER_TYPES = {
    'superior': {
        'qualities': ['noble_birth', 'learning', 'skill', 'dignity'],
        'emotional_expression': 'restrained',
        'laughter_style': ['slight_smile', 'smile'],
        'sorrow_style': 'patience',
        'examples': ['kings', 'gods', 'sages']
    },
    'middling': {
        'qualities': ['moderate_status', 'education', 'refinement'],
        'emotional_expression': 'moderate',
        'laughter_style': ['gentle_laughter', 'laughter_of_ridicule'],
        'sorrow_style': 'controlled_grief',
        'examples': ['merchants', 'ministers', 'officers']
    },
    'inferior': {
        'qualities': ['common_status', 'unrefined'],
        'emotional_expression': 'unrestrained',
        'laughter_style': ['vulgar_laughter', 'excessive_laughter'],
        'sorrow_style': 'open_weeping',
        'examples': ['servants', 'rogues', 'parasites']
    }
}
```

### 8.2 The Eight Types of Heroines (NÄyikÄ)

```python
NAYIKA_TYPES = {
    'vÄsaka-sajjÄ': {
        'name': 'Dressed for Union',
        'state': 'Expectantly awaiting lover',
        'emotional_dominant': 'anticipation'
    },
    'virahotkÄá¹‡á¹­hitÄ': {
        'name': 'Distressed by Separation',
        'state': 'Pining for absent lover',
        'emotional_dominant': 'yearning'
    },
    'svÄdhÄ«na-patikÄ': {
        'name': 'Having Husband in Subjection',
        'state': 'Confident in lover\'s devotion',
        'emotional_dominant': 'contentment'
    },
    'kalahÄntaritÄ': {
        'name': 'Separated by Quarrel',
        'state': 'Estranged after argument',
        'emotional_dominant': 'regret'
    },
    'khaá¹‡á¸itÄ': {
        'name': 'Enraged',
        'state': 'Angry at lover\'s infidelity',
        'emotional_dominant': 'jealous_anger'
    },
    'vipralabdhÄ': {
        'name': 'Deceived',
        'state': 'Betrayed by lover',
        'emotional_dominant': 'disappointment'
    },
    'proá¹£ita-bhartá¹›kÄ': {
        'name': 'With Sojourning Husband',
        'state': 'Husband away on journey',
        'emotional_dominant': 'loneliness'
    },
    'abhisÄrikÄ': {
        'name': 'Moving to Lover',
        'state': 'Going to meet lover',
        'emotional_dominant': 'adventurous_love'
    }
}
```

### 8.3 Anger Expression by Relationship

```python
def express_anger(character, target_relationship):
    """
    Anger manifestation varies by social relationship.
    """
    ANGER_EXPRESSIONS = {
        'towards_enemy': [
            'knitting_eyebrows', 'fierce_look', 'bitten_lips',
            'hands_clasping', 'touching_head_and_breast'
        ],
        'towards_superior': [
            'slightly_downcast_eyes', 'wiping_slight_perspiration',
            'NO_violent_movement'  # Constrained expression
        ],
        'towards_beloved': [
            'very_slight_body_movement', 'shedding_tears',
            'knitting_eyebrows', 'sidelong_glances', 'throbbing_lips'
        ],
        'towards_servant': [
            'threat', 'rebuke', 'dilating_eyes',
            'contemptuous_looks_various_kinds'
        ],
        'feigned': [
            'mild_versions_of_above',
            'ulterior_motive_present'
        ]
    }
    return ANGER_EXPRESSIONS[target_relationship]
```

---

## 9. Siddhi: The Theory of Success

### 9.1 Dual Success Model

```python
SUCCESS_TYPES = {
    'daiviki': {
        'name': 'Divine Success',
        'source': 'Superior spectators (cultured, educated)',
        'recognition_of': 'Deeper aspects of play',
        'expression': 'Refined appreciation',
        'measure': 'quality_of_understanding'
    },
    'mÄnuá¹£Ä«': {
        'name': 'Human Success',
        'source': 'Average spectators (ordinary people)',
        'recognition_of': 'Superficial/obvious aspects',
        'expression': 'Tumultuous applause, energetic response',
        'measure': 'intensity_of_reaction'
    }
}

# Both are valid and necessary
# "The ultimate court of appeal concerning dramatic practice is THE PEOPLE"
```

### 9.2 Audience Taste Differentiation

```python
AUDIENCE_PREFERENCES = {
    'lovers': 'erotic_sentiment_presentation',
    'learned': 'religious_philosophical_doctrine',
    'wealth_seekers': 'acquisition_themes',
    'passionless': 'liberation_topics',
    'fierce_persons': 'odious_terrible_sentiments',
    'warriors': 'personal_combats_battles',
    'elderly': 'puranic_tales_virtue',
    'common_women_children_uncultured': 'comic_sentiment_remarkable_costumes'
}

# A drama must satisfy DIVERSE tastes in ONE PLACE
# This is the essence of dramatic art's social function
```

---

## 10. Compositional Methodology

### 10.1 The Integration Principle

```python
def compose_drama(source, intended_sentiment):
    """
    Systematic approach to dramatic composition.
    """
    # Step 1: Establish core rasa
    dominant_rasa = select_primary_sentiment(intended_sentiment)
    
    # Step 2: Identify sthayibhava
    dominant_state = RASA_TO_BHAVA[dominant_rasa]
    
    # Step 3: Design vibhavas (determinants/causes)
    vibhavas = create_circumstances_that_trigger(dominant_state)
    
    # Step 4: Design anubhavas (consequents/expressions)
    anubhavas = design_expression_vocabulary(dominant_state)
    
    # Step 5: Select compatible vyabhicaris
    transitory_states = filter_compatible(dominant_rasa)
    
    # Step 6: Choose appropriate style (vrtti)
    style = STYLE_SENTIMENT_MAP[dominant_rasa]
    
    # Step 7: Structure plot (vastu)
    plot = construct_five_sandhis(source, hero)
    
    # Step 8: Distribute across acts
    acts = distribute_elements(plot, dominant_rasa, style)
    
    # Step 9: Design abhinaya for each scene
    for act in acts:
        for scene in act.scenes:
            scene.angika = design_gestures(scene.sentiment)
            scene.vacika = design_dialogue(scene.sentiment)
            scene.aharya = design_costumes(scene.characters)
            scene.sattvika = design_internal_states(scene.sentiment)
    
    return Drama(acts)
```

### 10.2 Diction Guidelines

```python
DICTION_PRINCIPLES = {
    'metre_selection': {
        'heroic_furious': 'arya_metre',
        'erotic': ['malini', 'mandakranta'],  # Gentle metres
        'pathetic': ['sakkari', 'atidhriti']
    },
    'euphony': {
        'requirement': 'agreeable_and_soft_sounds',
        'accessibility': 'intelligible_to_country_people',
        'feminine_speech': 'words_recitable_by_women'
    },
    'verse_prose_balance': {
        'warning': 'Long prose passages prove tiresome to spectators',
        'recommendation': 'Emphasize verse in dialogue'
    },
    'character_names': {
        'method': 'suggestive_significant_names',
        'function': 'Names indicate character qualities'
    }
}
```

---

## 11. Diagnostic Questions

Answer the following questions to validate the dramatic structure:

### 11.1 Rasa Verification

1. **Which Dominant State (sthayibhava) is being evoked?** Confirm clear sthayibhava identification.
2. **Are the Determinants (causes) specific and appropriate?** Verify vibhava specificity.
3. **Are the Consequents (expressions) appropriate to the sentiment?** Check anubhava selection.
4. **Are the Transitory States compatible with the dominant rasa?** Validate vyabhicari choices.
5. **Does the representation achieve universality (rasa) over personal emotion?** Test for aesthetic vs. personal emotion.

### 11.2 Structural Verification

6. **Is the Germ (bija) planted in the Opening?** Verify plot foundation.
7. **Do the Five Junctures appear in logical sequence?** Check structural completeness.
8. **Does the Incidental Plot INCIDENTALLY serve the Principal Plot?** Test subplot integration.
9. **Is the Hero's progression through the Five Stages clear?** Verify dramatic arc.
10. **Does the Conclusion arise from the Development?** Check organic resolution.

### 11.3 Performance Verification

11. **Do the four Abhinaya modes (body, word, appearance, mind) work in harmony?** Verify integrated representation.
12. **Is the practice (dharmi) appropriate to the emotional intensity?** Check realistic/conventional balance.
13. **Is the style (vrtti) matched to the sentiment?** Validate style-sentiment correspondence.
14. **Are character expressions appropriate to their type?** Verify character consistency.
15. **Are prohibited on-stage actions (death, eating, battle) reported rather than shown?** Verify staging boundaries.

---

## Appendix A: Quick Reference Card

### The Core Formula

```
RASA = STHAYIBHAVA + VIBHAVA + ANUBHAVA + VYABHICARI
      (Sentiment)   (Dominant)  (Determinants) (Consequents) (Transitory)
                    (State)     (Causes)       (Expressions) (States)
```

### The Eight Rasas

```
Åšá¹›á¹…gÄra (Erotic)    â† Love      â†’ Comic
HÄsya (Comic)       â† Mirth
Karuá¹‡a (Pathetic)   â† Sorrow    â† Furious
Raudra (Furious)    â† Anger     â†’ Pathetic
VÄ«ra (Heroic)       â† Energy    â†’ Marvellous
BhayÄnaka (Terrible)â† Fear      â† Odious
BÄ«bhatsa (Odious)   â† Disgust   â†’ Terrible
Adbhuta (Marvellous)â† Astonishment
```

### The Four Representations

```
Ä€á¹…gika   â†’ BODY (gestures, movement)
VÄcika   â†’ WORDS (speech, intonation)
Ä€hÄrya   â†’ APPEARANCE (costume, make-up)
SÄttvika â†’ TEMPERAMENT (psychophysical states)
```

### The Five Junctures

```
1. Mukha (Opening)      â†’ Germ planted
2. Pratimukha (Progress)â†’ Germ sprouts
3. Garbha (Development) â†’ Action unfolds
4. VimarÅ›a (Pause)      â†’ Crisis point
5. Nirvahana (Conclusion)â†’ Resolution
```

---

## Appendix B: Validation Checklist

```python
def validate_drama(drama):
    checks = [
        # Rasa
        ("Clear dominant sentiment identified", rasa_clarity_test),
        ("Sthayibhava consistently evoked", dominant_state_test),
        ("Vibhavas specific and appropriate", determinant_test),
        ("Anubhavas match sentiment", consequent_test),
        ("Vyabhicaris compatible", transitory_state_test),
        ("Universal quality achieved", universality_test),
        
        # Structure
        ("Germ (bija) in Opening", germ_placement_test),
        ("Five Junctures present", sandhi_completeness_test),
        ("Principal plot clear", adhikarika_test),
        ("Incidental plots serve main", prasangika_test),
        ("Hero's Five Stages visible", hero_progression_test),
        
        # Representation
        ("Four Abhinaya modes integrated", abhinaya_integration_test),
        ("Practice (dharmi) appropriate", practice_selection_test),
        ("Style (vrtti) matches sentiment", style_sentiment_test),
        ("Character types consistent", character_consistency_test),
        ("Prohibited actions excluded", prohibition_test),
        
        # Success
        ("Appeals to diverse tastes", diversity_test),
        ("Both divine and human success possible", dual_success_test),
    ]
    
    return all(test(drama) for name, test in checks)
```

---

## Appendix C: Theoretical Correspondence Table

| Bharata Muni | Aristotle | McKee | South Park |
|--------------|-----------|-------|------------|
| Rasa (Sentiment) | Catharsis | Emotional experience | Episode impact |
| Sthayibhava (Dominant State) | Pathos | Core emotion | Emotional throughline |
| Vibhava (Determinant) | Probable cause | Inciting incident/setup | Setup |
| Anubhava (Consequent) | Recognition/expression | Payoff | Payoff |
| Vyabhicari (Transitory) | Complication | Gap complications | Complications |
| Sandhi (Juncture) | Plot structure | Act structure | Story beats |
| Natyadharmi | Poetic truth | â€” | â€” |
| Lokadharmi | Historical truth | â€” | â€” |
| Abhinaya | Spectacle/manner | â€” | â€” |

---

## Appendix D: Key Terms Glossary

| Sanskrit | Translation | Function |
|----------|-------------|----------|
| Rasa | Sentiment/Aesthetic flavor | Goal of dramatic representation |
| BhÄva | State/Emotion | Building blocks of rasa |
| SthÄyibhÄva | Dominant State | Core emotion underlying rasa |
| VibhÄva | Determinant | Causes that trigger emotional response |
| AnubhÄva | Consequent | Expressions that follow emotion |
| VyabhicÄribhÄva | Transitory State | Accompanying/coloring emotions |
| SÄttvikabhÄva | Temperamental State | Psychophysical involuntary responses |
| Abhinaya | Representation | Acting/expression technique |
| Ä€á¹…gika | Gestural | Body-based representation |
| VÄcika | Verbal | Speech-based representation |
| Ä€hÄrya | Costume/Visual | Appearance-based representation |
| SÄttvika | Temperamental | Psychology-based representation |
| DharmÄ« | Practice | Mode of representation |
| Lokadharmi | Realistic | Everyday-life imitation |
| NÄá¹­yadharmi | Conventional | Theatrical stylization |
| Vá¹›tti | Style | Manner of presentation |
| Sandhi | Juncture | Plot structural unit |
| Vastu | Plot | Subject-matter/action |
| NÄá¹­aka | Drama | Complete dramatic form |
| Siddhi | Success | Achievement of dramatic effect |

---

*Compiled from Bharata Muni. Natyasastra: A Treatise on Hindu Dramaturgy and Histrionics. Translated by Manomohan Ghosh. Calcutta: Asiatic Society of Bengal, 1950.*
# Bharata Muni's Narratological Algorithms: Supplement

Extended algorithms for advanced dramatic construction, covering topics not addressed in the primary document. Based on the Manomohan Ghosh translation of the *Natyasastra*.

---

## 12. GhÄá¹­a: The Theory of Blemishes (Failure Modes)

### 12.1 Core Principle

Dramatic success (siddhi) has an inverse: ghÄá¹­a (blemish/failure). Understanding failure modes enables proactive prevention. Bharata categorizes failures by source, severity, and remediability.

### 12.2 Taxonomy of Blemishes

```
GHÄ€á¹¬A (Blemishes) = 4 categories

â”œâ”€â”€ DAIVIKA (From Gods/Fate)
â”‚   â””â”€â”€ External accidents beyond human control
â”‚
â”œâ”€â”€ Ä€TMA-SAMUTTHA (Self-Made)
â”‚   â””â”€â”€ Errors by performers themselves
â”‚
â”œâ”€â”€ PARA (From Enemies)
â”‚   â””â”€â”€ Sabotage by rival groups
â”‚
â””â”€â”€ AUTPÄ€TIKA (From Portents)
    â””â”€â”€ Natural calamities during performance
```

### 12.3 Daivika GhÄá¹­a (Divine/Accidental Blemishes)

```python
DIVINE_BLEMISHES = [
    'strong_wind',           # Disrupts sound, movement
    'fire',                  # Emergency evacuation
    'rain',                  # Open-air performance ruined
    'elephant_fear',         # Animal intrusion
    'serpent_appearance',    # Panic in audience
    'lightning_strike',      # Dangerous interruption
    'ant_invasion',          # Distraction on stage
    'insect_swarm',          # Disrupts actors
    'wild_animal_entry'      # Ferocious beast intrusion
]

# These are UNPREVENTABLE but some are IGNORABLE
def assess_divine_blemish(blemish_type):
    """
    Not all divine blemishes require stopping performance.
    """
    IGNORABLE = ['ant_invasion', 'minor_animal_appearance']
    CATASTROPHIC = ['fire', 'lightning', 'earthquake']
    
    if blemish_type in CATASTROPHIC:
        return 'halt_immediately'
    elif blemish_type in IGNORABLE:
        return 'continue_with_adaptation'
    else:
        return 'director_discretion'
```

### 12.4 Ä€tma-Samuttha GhÄá¹­a (Self-Made Blemishes)

The most preventable categoryâ€”errors arising from the performers themselves.

```python
SELF_MADE_BLEMISHES = {
    # Acting errors
    'unnaturalness': {
        'description': 'Acting that breaks believability',
        'severity': 'high',
        'remedy': 'rehearsal, directorial correction'
    },
    'wrong_movement': {
        'description': 'Gestures inappropriate to sentiment/character',
        'severity': 'medium',
        'remedy': 'practice, memorization of abhinaya'
    },
    'role_unsuitability': {
        'description': 'Actor miscast for the part (vibhÅ«mikatva)',
        'severity': 'high',
        'remedy': 'proper casting, role reassignment'
    },
    'memory_loss': {
        'description': 'Forgetting lines or blocking',
        'severity': 'high',
        'remedy': 'prompting system, over-rehearsal'
    },
    'wrong_words': {
        'description': 'Speaking words not in the script (anyavacana)',
        'severity': 'medium',
        'remedy': 'strict memorization'
    },
    'distress_cry': {
        'description': 'Actor breaking character in pain/discomfort',
        'severity': 'high',
        'remedy': 'physical preparation, safety measures'
    },
    'poor_hand_work': {
        'description': 'Incorrect hand gestures (vihastatva)',
        'severity': 'medium',
        'remedy': 'hasta practice'
    },
    'crown_falling': {
        'description': 'Ornaments/costume pieces dropping',
        'severity': 'low-medium',
        'remedy': 'secure costume design'
    },
    'drum_defects': {
        'description': 'Poor percussion (puá¹£karadoá¹£a)',
        'severity': 'medium',
        'remedy': 'musician rehearsal, instrument maintenance'
    },
    'speech_shyness': {
        'description': 'Timid or unclear speech (vÄgbhÄ«ti)',
        'severity': 'high',
        'remedy': 'voice training, confidence building'
    },
    'excessive_laughing': {
        'description': 'Breaking character with inappropriate laughter',
        'severity': 'medium',
        'remedy': 'emotional discipline'
    },
    'excessive_crying': {
        'description': 'Overacting emotional states',
        'severity': 'medium',
        'remedy': 'emotional calibration'
    }
}

def diagnose_self_made_blemish(performance):
    """
    Identify self-made blemishes in a performance.
    """
    detected = []
    for blemish, config in SELF_MADE_BLEMISHES.items():
        if performance.exhibits(blemish):
            detected.append({
                'type': blemish,
                'severity': config['severity'],
                'remedy': config['remedy']
            })
    return sorted(detected, key=lambda x: 
        {'high': 0, 'medium': 1, 'low': 2}[x['severity']])
```

### 12.5 Para GhÄá¹­a (Enemy-Created Blemishes)

Sabotage by rival theatrical groups or hostile audience members.

```python
ENEMY_BLEMISHES = {
    'screaming': 'Deliberate noise to drown performance',
    'buzzing': 'Coordinated distracting sounds (visphoá¹­ita)',
    'noisy_clapping': 'Disruptive applause at wrong moments',
    'throwing_cowdung': 'Physical disruption with projectiles',
    'throwing_clods': 'Earth/mud thrown at performers',
    'throwing_grass': 'Debris thrown onto stage',
    'throwing_stones': 'Dangerous projectile attacks'
}

ENEMY_MOTIVATIONS = [
    'jealousy',           # Rival troupe's envy
    'hostility',          # Personal grudge
    'partisanship',       # Loyalty to rival group
    'bribery'             # Paid sabotage (arthabheda)
]

# NOTE: The Natyasastra observes that such tactics
# "sometimes occur also now-a-days in meetings supporting
# candidates from rival political parties. Human psychology
# has not much changed..."
```

### 12.6 Blemish Severity Grades

```python
SEVERITY_GRADES = {
    'minor': {
        'examples': ['crown_falling', 'minor_animal_appearance'],
        'action': 'ignore_and_continue',
        'impact_on_siddhi': 'reduces_applause'
    },
    'moderate': {
        'examples': ['speech_shyness', 'drum_defects'],
        'action': 'adapt_and_continue',
        'impact_on_siddhi': 'spoils_success_wholly'
    },
    'severe': {
        'examples': ['fire', 'earthquake', 'actor_injury'],
        'action': 'halt_performance',
        'impact_on_siddhi': 'complete_failure'
    }
}

def grade_blemish(blemish):
    """
    Determine appropriate response to a blemish.
    """
    if blemish in ['fire', 'earthquake', 'lightning']:
        return 'severe'
    elif blemish in ['speech_shyness', 'drum_defects', 'memory_loss']:
        return 'moderate'
    else:
        return 'minor'
```

---

## 13. Temporal Constraints: Time Rules for Dramatic Composition

### 13.1 The Single-Day Rule for Acts

```
AXIOM: Each Act must contain only incidents that could occur
       within the course of a SINGLE DAY.

COROLLARY: Nothing in an Act may interrupt routine duties
           such as prayers or meals (these imply day-passage).
```

### 13.2 Inter-Act Duration Limits

```python
INTER_ACT_TIME_RULES = {
    'minimum': 'immediate_continuation',  # Same day possible
    'maximum': 'one_year',                # Never more than a year
    'indication_method': 'praveÅ›aka',     # Introductory Scene
    
    'RULE': """
        The lapse of time between two Acts, which might be
        a month or a year (but never more than a year) is
        to be indicated by an Introductory Scene (praveÅ›aka)
        preceding the last one.
    """
}

def validate_temporal_structure(drama):
    """
    Check temporal constraints across all acts.
    """
    for i, act in enumerate(drama.acts):
        # Check single-day rule
        if act.implied_duration > ONE_DAY:
            raise TemporalViolation(
                f"Act {i+1} exceeds single-day limit"
            )
        
        # Check inter-act gap
        if i > 0:
            gap = drama.time_between(act, drama.acts[i-1])
            if gap > ONE_YEAR:
                raise TemporalViolation(
                    f"Gap between Acts {i} and {i+1} exceeds one year"
                )
            if gap > ONE_DAY and not act.has_pravesaka:
                raise TemporalViolation(
                    f"Act {i+1} needs Introductory Scene for time gap"
                )
    
    return True
```

### 13.3 Single-Act Drama Types

Some dramatic forms are constrained to one act:

```python
SINGLE_ACT_FORMS = {
    'VyÄyoga': {
        'duration': 'events_of_single_day',
        'content': ['battle', 'personal_combat', 'challenge', 'angry_conflict'],
        'hero': 'well_known_character'
    },
    'Utsá¹›á¹£á¹­ikÄá¹…ka': {
        'duration': 'single_day',
        'content': ['pathetic_sentiment', 'women_lament'],
        'hero': 'human'
    },
    'Prahasana': {
        'duration': 'single_day',
        'content': ['comic_sentiment', 'farce', 'satire'],
        'hero': 'varied'
    },
    'BhÄá¹‡a': {
        'duration': 'single_day',
        'content': ['monologue', 'rogue_adventure'],
        'hero': 'single_actor'
    },
    'VÄ«thÄ«': {
        'duration': 'single_day',
        'content': ['short_dramatic_sketch'],
        'hero': 'one_or_two_actors'
    }
}
```

---

## 14. PÅ«rvaraá¹…ga: The Preliminaries Protocol

### 14.1 Core Principle

Every performance begins with PÅ«rvaraá¹…ga (Preliminaries)â€”a structured ritual sequence that consecrates the performance space, invokes divine blessing, and prepares the audience for aesthetic experience.

### 14.2 The Nineteen Components

```python
PURVARANGA_SEQUENCE = [
    # Phase 1: Musical Preparation
    ('pratyÄhÄra', 'Musical tuning and preparation'),
    ('avatÄraá¹‡a', 'Descent/entry of performers'),
    ('Ärambha', 'Beginning of instrumental music'),
    ('ÄÅ›ravaá¹‡a', 'Making audience attentive through sound'),
    ('vaktrapÄá¹‡i', 'Hand gestures indicating time-beat'),
    ('parighaá¹­á¹­ana', 'Striking drums in specific pattern'),
    ('saá¹ƒghoá¹­ana', 'Rehearsing hand poses for time-beat'),
    ('mÄrgÄsÄrita', 'Harmonious playing of drums and strings'),
    ('ÄsÄrita', 'Practicing time-fraction beats'),
    
    # Phase 2: Vocal/Ritual
    ('gÄ«tavidhi', 'Application of songs praising gods'),
    ('utthÄpana', 'Raising ceremonyâ€”starts performance proper'),
    ('parivartana', 'Walking-round praising guardian deities'),
    ('nandÄ«', 'Benediction invoking gods, Brahmins, kings'),
    ('Å›uá¹£kÄvaká¹›á¹£á¹­a', 'Dhruva with meaningless sounds for Jarjara'),
    
    # Phase 3: Dramatic Introduction
    ('raá¹…gadvÄra', 'Gateway to performanceâ€”words and gestures begin'),
    ('cÄrÄ«', 'Movements depicting Erotic Sentiment'),
    ('mahÄcÄrÄ«', 'Movements depicting Furious Sentiment'),
    ('trigata', 'Three Men\'s Talkâ€”Director, Assistant, Jester'),
    ('prarocanÄ', 'Laudationâ€”suggesting the play\'s denouement')
]

def execute_purvaranga(performance):
    """
    Execute the Preliminaries in proper sequence.
    """
    for component, description in PURVARANGA_SEQUENCE:
        perform_component(component)
        # Each component must complete before next begins
    
    # After Preliminaries, main play may commence
    return 'ready_for_main_performance'
```

### 14.3 The Benediction (NandÄ«) Algorithm

```python
def compose_nandi():
    """
    The Benediction must include blessings for three entities.
    """
    REQUIRED_BLESSINGS = ['gods', 'brahmins', 'kings']
    
    nandi = Benediction()
    
    for entity in REQUIRED_BLESSINGS:
        nandi.add_blessing(
            target=entity,
            words='holy_auspicious_terms',
            metre='appropriate_to_sentiment'
        )
    
    # The Nandi sets the tone for the entire performance
    # Wrong Benediction is classified as a Blemish
    return nandi
```

### 14.4 The Three Men's Talk (Trigata)

```python
class Trigata:
    """
    Conversational introduction involving three characters.
    """
    
    PARTICIPANTS = {
        'sÅ«tradhÄra': 'Directorâ€”leads the conversation',
        'pÄripÄrÅ›vika': 'Assistantâ€”responds and queries',
        'vidÅ«á¹£aka': 'Jesterâ€”provides comic relief and transitions'
    }
    
    def execute(self, play):
        """
        The Trigata introduces the play through dialogue.
        """
        # Director enters and establishes context
        self.sutradhara.establish_setting()
        
        # Assistant queries about the play
        self.pariparsvika.ask_about_play()
        
        # Director reveals playwright, plot summary
        self.sutradhara.reveal_play_details(
            playwright=play.author,
            title=play.name,
            subject=play.subject_summary
        )
        
        # Jester provides transition to action
        self.vidusaka.comic_transition()
        
        # Exit Preliminaries, enter main play
        return 'commence_main_action'
```

### 14.5 Preliminaries Types

```python
PRELIMINARIES_TYPES = {
    'Å›uddha': {
        'name': 'Pure Preliminaries',
        'characteristics': 'Full 19-component sequence',
        'use': 'Major dramatic productions'
    },
    'tryasra': {
        'name': 'Triangular Preliminaries',
        'characteristics': 'Abbreviated sequence',
        'use': 'Shorter dramatic forms'
    },
    'miÅ›ra': {
        'name': 'Mixed Preliminaries',
        'characteristics': 'Combined elements from both',
        'use': 'Context-dependent adaptation'
    }
}
```

---

## 15. Rasa Combination Rules

### 15.1 Primary-Derivative Relationships

```python
RASA_DERIVATION = {
    # PRIMARY â†’ DERIVATIVE (with mechanism)
    'Åšá¹›á¹…gÄra': ('HÄsya', 'mimicry'),      # Erotic â†’ Comic
    'Raudra': ('Karuá¹‡a', 'result'),        # Furious â†’ Pathetic
    'VÄ«ra': ('Adbhuta', 'result'),         # Heroic â†’ Marvellous
    'BÄ«bhatsa': ('BhayÄnaka', 'consequence')  # Odious â†’ Terrible
}

# The four PRIMARY rasas generate the four DERIVATIVE rasas
PRIMARY_RASAS = {'Åšá¹›á¹…gÄra', 'Raudra', 'VÄ«ra', 'BÄ«bhatsa'}
DERIVATIVE_RASAS = {'HÄsya', 'Karuá¹‡a', 'Adbhuta', 'BhayÄnaka'}
```

### 15.2 Dominant Rasa Principle

```python
def establish_dominant_rasa(drama):
    """
    Every drama must have ONE dominant sentiment that
    governs the work, though others may appear.
    """
    # The dominant rasa determines:
    # - Overall tone and style (vá¹›tti)
    # - Hero's primary emotional journey
    # - Resolution type
    
    dominant = drama.select_primary_sentiment()
    
    # All other rasas must SERVE the dominant
    for scene in drama.scenes:
        if scene.rasa != dominant:
            assert serves_dominant(scene.rasa, dominant), \
                f"{scene.rasa} must support {dominant}"
    
    return dominant
```

### 15.3 Transitory State Compatibility

```python
# Not all vyabhicÄris work with all rasas
VYABHICARI_EXCLUSIONS = {
    'erotic_union': {
        'exclude': ['fear', 'indolence', 'cruelty', 'disgust'],
        'reason': 'These destroy the mood of love-in-union'
    },
    'comic': {
        'compatible': ['indolence', 'dissimulation', 'drowsiness', 
                      'sleep', 'dreaming', 'insomnia', 'envy'],
        'reason': 'Comic requires specific coloring states'
    }
}

def validate_vyabhicari_selection(rasa, vyabhicaris):
    """
    Check that transitory states are compatible with sentiment.
    """
    if rasa in VYABHICARI_EXCLUSIONS:
        exclusions = VYABHICARI_EXCLUSIONS[rasa].get('exclude', [])
        for v in vyabhicaris:
            if v in exclusions:
                raise IncompatibilityError(
                    f"{v} incompatible with {rasa}"
                )
    return True
```

### 15.4 Scene-Level Rasa Shifts

```python
def manage_rasa_transitions(drama):
    """
    Rasas may shift between scenes but must transition smoothly.
    """
    for i, scene in enumerate(drama.scenes[1:], 1):
        prev_rasa = drama.scenes[i-1].rasa
        curr_rasa = scene.rasa
        
        if prev_rasa != curr_rasa:
            # Transition must be motivated
            assert scene.has_transition_trigger(), \
                "Rasa shift requires narrative motivation"
            
            # Some transitions are more natural than others
            if is_related_rasa(prev_rasa, curr_rasa):
                # Primary â†’ Derivative is smooth
                continue
            else:
                # Unrelated rasas need stronger bridging
                assert scene.has_strong_bridge(), \
                    f"Transition from {prev_rasa} to {curr_rasa} needs bridging"
```

---

## 16. Unity Principles: Structural Coherence Mechanisms

### 16.1 The BÄ«ja (Germ) Continuity Rule

```python
BIJA_RULE = """
The Germ (bÄ«ja) of the play as well as its Prominent Point (bindu)
must relate to EVERY Act of the play. The Hero must either appear
in every Act or be mentioned there.
"""

def validate_bija_continuity(drama):
    """
    The seed planted in Act 1 must connect to all subsequent acts.
    """
    bija = drama.acts[0].germ  # Planted in Opening (Mukha)
    
    for act in drama.acts:
        # Bija must be referenced or advanced
        assert act.references_or_advances(bija), \
            f"Act {act.number} loses connection to the Germ"
        
        # Hero must appear or be mentioned
        assert act.hero_present or act.hero_mentioned, \
            f"Act {act.number} must include Hero presence/reference"
    
    return True
```

### 16.2 The Bindu (Point) Maintenance Rule

```python
class Bindu:
    """
    The Bindu maintains continuity when action seems interrupted.
    It's a narrative device that keeps the thread alive during
    apparent diversions.
    """
    
    def apply(self, scene_sequence):
        """
        Insert bindu elements where continuity might break.
        """
        for i, scene in enumerate(scene_sequence):
            if scene.diverges_from_main_plot():
                # Insert a binduâ€”a reference back to main action
                scene.add_bindu(
                    reference=self.main_plot_element,
                    method='dialogue_mention' or 'visual_callback'
                )
        return scene_sequence
```

### 16.3 Incident Density Control

```python
INCIDENT_DENSITY_RULE = """
An Act must not present TOO MANY incidents.
Subsidiary events that might affect unity of impression
should be REPORTED (in Introductory Scenes) rather than
directly presented.
"""

def control_incident_density(act):
    """
    Ensure act doesn't overload with incidents.
    """
    MAX_MAIN_INCIDENTS = 3  # Guideline, not strict rule
    
    main_incidents = [i for i in act.incidents if i.is_main]
    subsidiary = [i for i in act.incidents if not i.is_main]
    
    if len(main_incidents) > MAX_MAIN_INCIDENTS:
        # Too manyâ€”consider redistribution
        return 'redistribute_to_other_acts'
    
    for sub in subsidiary:
        if sub.would_break_unity():
            # Move to Introductory Scene as report
            sub.convert_to_pravesaka_report()
    
    return act
```

### 16.4 The Pravesaka (Introductory Scene) Device

```python
class Pravesaka:
    """
    Introductory Scene placed before an Act to:
    1. Indicate time passage between acts
    2. Report subsidiary events that can't be shown
    3. Clarify complex plot points
    4. Maintain unity by summarizing rather than showing
    """
    
    FUNCTIONS = [
        'time_passage_indication',   # "A year has passed..."
        'off_stage_event_report',    # "Meanwhile, the battle occurred..."
        'clarification',             # "What the hero meant was..."
        'subsidiary_plot_summary'    # "While we follow X, Y has been..."
    ]
    
    def compose(self, preceding_act, following_act, events_to_report):
        """
        Create an Introductory Scene bridging two acts.
        """
        pravesaka = Scene(type='introductory')
        
        # Indicate time gap if any
        time_gap = following_act.time - preceding_act.time
        if time_gap > ONE_DAY:
            pravesaka.add_time_indication(time_gap)
        
        # Report events that shouldn't be staged
        for event in events_to_report:
            if event in PROHIBITED_REPRESENTATIONS:
                pravesaka.add_report(event)
        
        return pravesaka
```

---

## 17. Language and Dialect Rules

### 17.1 Character-Language Mapping

```python
LANGUAGE_RULES = {
    'sanskrit': {
        'speakers': ['kings', 'brahmins', 'sages', 'gods', 'ministers'],
        'register': 'elevated',
        'context': 'formal_discourse, philosophical_discussion'
    },
    'prakrit': {
        'speakers': ['women', 'children', 'common_people'],
        'variants': {
            'Å›aurasenÄ«': 'women_of_rank',
            'mÄgadhÄ«': 'servants',
            'ardhamÄgadhÄ«': 'merchants',
            'avantÄ«': 'rogues_and_gamblers'
        },
        'register': 'colloquial'
    }
}

def assign_language(character):
    """
    Determine appropriate language for a character.
    """
    if character.type in ['king', 'brahmin', 'sage', 'god', 'minister']:
        return 'sanskrit'
    elif character.type == 'woman':
        if character.rank == 'high':
            return ('prakrit', 'Å›aurasenÄ«')
        else:
            return ('prakrit', 'general')
    elif character.type == 'servant':
        return ('prakrit', 'mÄgadhÄ«')
    # ... and so on
```

### 17.2 Diction Quality Marks

```python
DICTION_QUALITIES = {
    # Positive marks (guá¹‡a)
    'clarity': 'Words must be intelligible',
    'euphony': 'Sounds must be agreeable and soft',
    'appropriateness': 'Language matches character status',
    'accessibility': 'Intelligible to country people',
    'recitability': 'Feminine speech uses words women can recite',
    
    # Negative marks (doá¹£a)
    'circumlocution': 'Unnecessary wordiness',
    'superfluous_expression': 'Redundant phrasing',
    'want_of_significance': 'Empty words',
    'logical_defect': 'Internal contradiction',
    'metrical_defect': 'Verse that doesn\'t scan',
    'hiatus': 'Unpleasant vowel collision',
    'slang': 'Inappropriate colloquialism for context'
}
```

---

## 18. Supplementary Diagnostic Questions

### 18.1 Blemish Prevention Checklist

| Question | Purpose |
|----------|---------|
| "Are all actors properly cast for their roles?" | Prevent vibhÅ«mikatva |
| "Have actors memorized completely?" | Prevent memory loss errors |
| "Are costumes/props secured?" | Prevent physical blemishes |
| "Have musicians rehearsed adequately?" | Prevent puá¹£karadoá¹£a |
| "Is the performance space protected from intrusion?" | Prevent divine/enemy blemishes |

### 18.2 Temporal Structure Checklist

| Question | Purpose |
|----------|---------|
| "Does each act stay within single-day bounds?" | Validate act duration |
| "Are inter-act gaps under one year?" | Validate structural limits |
| "Are time gaps indicated by PraveÅ›aka?" | Verify continuity devices |
| "Does the hero appear or get mentioned in every act?" | Check bÄ«ja continuity |

### 18.3 Unity Verification Checklist

| Question | Purpose |
|----------|---------|
| "Does the Germ (bÄ«ja) connect all acts?" | Verify plot coherence |
| "Are subsidiary events reported rather than shown when appropriate?" | Check incident density |
| "Do all rasas serve the dominant sentiment?" | Validate emotional unity |
| "Are transitions between rasas motivated?" | Check emotional flow |

---

## Appendix E: Extended Numerical Reference

| Category | Count | Components |
|----------|-------|------------|
| Blemish Types | 4 | Divine, Self-made, Enemy, Portent |
| Self-Made Blemishes | 12+ | See Section 12.4 |
| PÅ«rvaraá¹…ga Components | 19 | See Section 14.2 |
| Preliminary Types | 3 | Pure, Triangular, Mixed |
| Primary Rasas | 4 | Åšá¹›á¹…gÄra, Raudra, VÄ«ra, BÄ«bhatsa |
| Derivative Rasas | 4 | HÄsya, Karuá¹‡a, Adbhuta, BhayÄnaka |
| Diction Qualities | 10+ | Positive and negative marks |
| Single-Act Forms | 5 | VyÄyoga, Utsá¹›á¹£á¹­ikÄá¹…ka, Prahasana, BhÄá¹‡a, VÄ«thÄ« |

---

## Appendix F: Extended Glossary

| Term | Sanskrit | Meaning |
|------|----------|---------|
| GhÄá¹­a | à¤˜à¤¾à¤Ÿ | Blemish, failure, defect in production |
| Daivika | à¤¦à¥ˆà¤µà¤¿à¤• | Divine, relating to fate/gods |
| Ä€tma-samuttha | à¤†à¤¤à¥à¤®à¤¸à¤®à¥à¤¤à¥à¤¥ | Self-arising, self-made |
| Para | à¤ªà¤° | Enemy, other, rival |
| AutpÄtika | à¤”à¤¤à¥à¤ªà¤¾à¤¤à¤¿à¤• | Relating to portents/omens |
| PÅ«rvaraá¹…ga | à¤ªà¥‚à¤°à¥à¤µà¤°à¤™à¥à¤— | Preliminaries, pre-performance ritual |
| NandÄ« | à¤¨à¤¨à¥à¤¦à¥€ | Benediction, auspicious opening |
| Trigata | à¤¤à¥à¤°à¤¿à¤—à¤¤ | Three Men's Talk |
| PrarocanÄ | à¤ªà¥à¤°à¤°à¥‹à¤šà¤¨à¤¾ | Laudation, introduction of play |
| PraveÅ›aka | à¤ªà¥à¤°à¤µà¥‡à¤¶à¤• | Introductory Scene |
| BÄ«ja | à¤¬à¥€à¤œ | Germ, seed of plot |
| Bindu | à¤¬à¤¿à¤¨à¥à¤¦à¥ | Point, continuity device |
| VibhÅ«mikatva | à¤µà¤¿à¤­à¥‚à¤®à¤¿à¤•à¤¤à¥à¤µ | Role unsuitability, miscasting |
| Puá¹£karadoá¹£a | à¤ªà¥à¤·à¥à¤•à¤°à¤¦à¥‹à¤· | Defect in drumming |
| VÄgbhÄ«ti | à¤µà¤¾à¤—à¥à¤­à¥€à¤¤à¤¿ | Speech shyness, timidity |

---

*This supplement extends the primary Bharata Muni Narratological Algorithms document. Together they provide a comprehensive algorithmic framework for classical Indian dramatic theory.*

*Compiled from Bharata Muni. Natyasastra: A Treatise on Hindu Dramaturgy and Histrionics. Translated by Manomohan Ghosh. Calcutta: Asiatic Society of Bengal, 1950.*
# Bharata Muni's Narratological Algorithms: Extended Protocols

Tertiary document completing the algorithmic distillation of the *Natyasastra*. Covers performance-integrated narrative systems: musical cues, spatial grammar, movement algorithms, special representations, and structural prohibitions.

---

## 19. Dhruva: Musical-Narrative Cue System

### 19.1 Core Principle

Dhruvas are songs that function as structural punctuation in dramatic narrative. They signal entrances, exits, emotional transitions, and scene changesâ€”serving as the audio architecture of plot progression.

```
AXIOM: Music is not decorative but STRUCTURAL.
       Dhruvas mark narrative beats as reliably as
       chapter breaks mark textual divisions.
```

### 19.2 The Five Dhruva Types

```python
DHRUVA_TYPES = {
    'prÄveÅ›ikÄ«': {
        'function': 'ENTRANCE',
        'trigger': 'Character entering stage',
        'narrative_signal': 'New agent enters the action',
        'placement': 'Begins as curtain draws, continues until character established'
    },
    'Äká¹£epikÄ«': {
        'function': 'CASUAL/INCIDENTAL',
        'trigger': 'Transitional moments, minor actions',
        'narrative_signal': 'Subordinate action or emotional coloring',
        'placement': 'During transitional business'
    },
    'niá¹£krÄmikÄ«': {
        'function': 'EXIT',
        'trigger': 'Character leaving stage',
        'narrative_signal': 'Agent withdraws from current action',
        'placement': 'Accompanies departure movement'
    },
    'prÄsÄdikÄ«': {
        'function': 'PLEASING/PACIFYING',
        'trigger': 'Resolution moments, reconciliation',
        'narrative_signal': 'Tension release, harmony restored',
        'placement': 'During emotional resolution sequences'
    },
    'ÄntarÄ': {
        'function': 'INTERMEDIATE/INTERVAL',
        'trigger': 'Between major segments',
        'narrative_signal': 'Structural pause, scene division',
        'placement': 'Bridging distinct dramatic units'
    }
}
```

### 19.3 Dhruva-Narrative Synchronization Algorithm

```python
def select_dhruva(narrative_event):
    """
    Match the appropriate dhruva type to narrative moment.
    """
    if narrative_event.type == 'character_entrance':
        return DhruvaType.PRAVESIKI
    elif narrative_event.type == 'character_exit':
        return DhruvaType.NISKRAMIKI
    elif narrative_event.type == 'emotional_resolution':
        return DhruvaType.PRASADIKI
    elif narrative_event.type == 'scene_transition':
        return DhruvaType.ANTARA
    else:
        return DhruvaType.AKSEPIKI  # Default for incidental moments

def synchronize_dhruva_to_action(dhruva, stage_action):
    """
    Dhruva must align precisely with stage movement.
    """
    # Entrance dhruva begins with curtain movement
    if dhruva.type == 'pravesiki':
        dhruva.start_on('curtain_draw')
        dhruva.end_on('character_established_in_space')
    
    # Exit dhruva accompanies departure
    elif dhruva.type == 'niskramiki':
        dhruva.start_on('departure_intention_shown')
        dhruva.end_on('character_exits_view')
    
    return dhruva
```

### 19.4 Dhruva-Rasa Correspondence

```python
DHRUVA_RASA_MAPPING = {
    # Each rasa has characteristic musical qualities for its dhruvas
    'Åšá¹›á¹…gÄra': {
        'tempo': 'medium',
        'quality': 'sweet, graceful',
        'entrance_style': 'languid, anticipatory'
    },
    'VÄ«ra': {
        'tempo': 'quick',
        'quality': 'bold, energetic',
        'entrance_style': 'martial, decisive'
    },
    'Karuá¹‡a': {
        'tempo': 'slow',
        'quality': 'plaintive, heavy',
        'entrance_style': 'weighted, sorrowful'
    },
    'Raudra': {
        'tempo': 'quick',
        'quality': 'harsh, intense',
        'entrance_style': 'aggressive, turbulent'
    },
    'HÄsya': {
        'tempo': 'varied',
        'quality': 'light, playful',
        'entrance_style': 'bouncing, comic'
    },
    'BhayÄnaka': {
        'tempo': 'irregular',
        'quality': 'ominous, tense',
        'entrance_style': 'creeping, unsettling'
    },
    'BÄ«bhatsa': {
        'tempo': 'slow',
        'quality': 'discordant, heavy',
        'entrance_style': 'reluctant, repulsed'
    },
    'Adbhuta': {
        'tempo': 'building',
        'quality': 'expansive, surprising',
        'entrance_style': 'revelatory, ascending'
    }
}
```

---

## 20. Kaká¹£yÄvibhÄga: Stage Zone Grammar

### 20.1 Core Principle

The stage is not neutral space but a semantic field. Location on stage signifies narrative location in the story world. Movement across the stage represents travel through dramatic geography.

```
AXIOM: Space is symbolic. A few steps on stage can
       represent miles in the story world. The actor's
       position MEANS something.
```

### 20.2 Zone Signification System

```python
STAGE_ZONES = {
    'front_center': {
        'signifies': 'immediate_presence',
        'narrative_proximity': 'closest_to_audience',
        'typical_use': 'direct_address, key_revelations'
    },
    'rear': {
        'signifies': 'distance, elsewhere',
        'narrative_proximity': 'removed_from_main_action',
        'typical_use': 'arrivals_from_afar, watching'
    },
    'stage_right': {
        'signifies': 'auspicious_direction',
        'traditional_association': 'entrance_of_noble_characters',
        'typical_use': 'heroes, divine_figures'
    },
    'stage_left': {
        'signifies': 'varied_by_context',
        'traditional_association': 'entrance_of_others',
        'typical_use': 'supporting_characters, servants'
    }
}
```

### 20.3 The Walking-Distance Convention

```python
class DistanceRepresentation:
    """
    Physical walking distance on stage maps to narrative distance.
    """
    
    DISTANCE_MAPPING = {
        'short_walk': {
            'steps': 'few',
            'signifies': 'nearby_location',
            'example': 'moving_to_adjacent_room'
        },
        'medium_walk': {
            'steps': 'moderate',
            'signifies': 'medium_distance',
            'example': 'going_to_another_part_of_city'
        },
        'long_walk': {
            'steps': 'extended_circuit',
            'signifies': 'great_distance',
            'example': 'journey_to_another_kingdom'
        }
    }
    
    def represent_travel(self, narrative_distance):
        """
        A few steps can represent any distanceâ€”
        the QUALITY of movement signals the scale.
        """
        if narrative_distance == 'nearby':
            return self.short_walk()
        elif narrative_distance == 'medium':
            return self.medium_walk_with_scene_indication()
        elif narrative_distance == 'far':
            return self.extended_walk_with_travel_markers()
```

### 20.4 Zone Change Protocol

```python
def change_zone(actor, from_location, to_location, narrative_distance):
    """
    Zone change = location change in story world.
    The walk itself represents the journey.
    """
    # Start from current position
    actor.mark_departure(from_location)
    
    # Walk represents travel
    if narrative_distance == 'nearby':
        actor.walk(steps='few', tempo='normal')
    elif narrative_distance == 'medium':
        actor.walk(steps='moderate', tempo='measured')
        # May include travel indicators (wiping brow, adjusting garments)
    elif narrative_distance == 'far':
        actor.walk(steps='extended')
        actor.show_fatigue_markers()
        # Walking around stage represents long journey
    
    # Arrival at new location
    actor.establish_in_new_zone(to_location)
    
    return actor.current_zone
```

### 20.5 Symbolic Token Convention

```python
CONVEYANCE_TOKENS = {
    # Physical objects that signify vehicles without requiring them
    'elephant': 'goad (aá¹…kuÅ›a)',
    'horse': 'bit or bridle',
    'chariot': 'whip',
    'boat': 'oar gesture',
    'celestial_vehicle': 'upward gaze + floating movement'
}

# The Natyasastra asks rhetorically:
# "Will the actors have to die when the character
#  is said to be dead?" â€” signification replaces literalism
```

---

## 21. Gati: The Gait Algorithm System

### 21.1 Core Principle

Gait (gati) is not merely walking but characterization through movement. Character type, emotional state, and narrative situation all manifest in how a figure moves across the stage.

```
AXIOM: Movement reveals character. Before a word is spoken,
       the audience should know who approaches by HOW
       they approach.
```

### 21.2 Character-Type Gait Parameters

```python
GAIT_BY_CHARACTER_TYPE = {
    'superior': {
        'step_width': '4 tÄlas',
        'step_duration': '4 kalÄs',
        'posture': 'Vaiá¹£á¹‡ava sthÄna',
        'qualities': ['dignified', 'measured', 'unhurried'],
        'includes': ['gods', 'kings', 'sages']
    },
    'middling': {
        'step_width': '2 tÄlas',
        'step_duration': '2 kalÄs',
        'posture': 'natural',
        'qualities': ['balanced', 'purposeful'],
        'includes': ['ministers', 'merchants', 'citizens']
    },
    'inferior': {
        'step_width': '1 tÄla',
        'step_duration': '1 kalÄ',
        'posture': 'varied',
        'qualities': ['quick', 'practical'],
        'includes': ['servants', 'common people']
    },
    'women': {
        'step_width': '1 tÄla',
        'step_duration': 'graceful timing',
        'posture': 'Ä€yata or Avahittha',
        'qualities': ['delicate', 'graceful', 'lalita'],
        'movement': 'hands follow feet gently'
    }
}

def calculate_gait(character):
    """
    Determine base gait parameters from character type.
    """
    type_params = GAIT_BY_CHARACTER_TYPE[character.type]
    
    return Gait(
        step_width=type_params['step_width'],
        step_duration=type_params['step_duration'],
        posture=type_params['posture'],
        qualities=type_params['qualities']
    )
```

### 21.3 Emotional State Gait Modifiers

```python
GAIT_BY_EMOTIONAL_STATE = {
    # States that SLOW the gait (more than 4 kalÄs)
    'slow_states': {
        'fever': {'tempo': 'very_slow', 'qualities': ['weak', 'unsteady']},
        'hunger': {'tempo': 'slow', 'qualities': ['depleted', 'trembling']},
        'fatigue': {'tempo': 'slow', 'qualities': ['heavy', 'dragging']},
        'sorrow': {'tempo': 'slow', 'qualities': ['drooping', 'weighted']},
        'dissimulation': {'tempo': 'slow', 'qualities': ['cautious', 'measured']},
        'love_in_separation': {'tempo': 'slow', 'qualities': ['languid', 'distracted']}
    },
    
    # States that QUICKEN the gait (2 kalÄs or less)
    'quick_states': {
        'anxiety': {'tempo': 'quick', 'qualities': ['nervous', 'darting']},
        'panic': {'tempo': 'very_quick', 'qualities': ['frantic', 'uncontrolled']},
        'joy': {'tempo': 'quick', 'qualities': ['bouncing', 'energetic']},
        'anger': {'tempo': 'quick', 'qualities': ['forceful', 'aggressive']},
        'pursuit': {'tempo': 'very_quick', 'qualities': ['focused', 'relentless']},
        'concealed_love': {'tempo': 'quick', 'qualities': ['furtive', 'eager']}
    }
}

def modify_gait_for_state(base_gait, emotional_state):
    """
    Emotional state modifies the base character gait.
    """
    if emotional_state in GAIT_BY_EMOTIONAL_STATE['slow_states']:
        modifier = GAIT_BY_EMOTIONAL_STATE['slow_states'][emotional_state]
        base_gait.tempo = modifier['tempo']
        base_gait.add_qualities(modifier['qualities'])
        base_gait.duration *= 1.5  # Extend step duration
        
    elif emotional_state in GAIT_BY_EMOTIONAL_STATE['quick_states']:
        modifier = GAIT_BY_EMOTIONAL_STATE['quick_states'][emotional_state]
        base_gait.tempo = modifier['tempo']
        base_gait.add_qualities(modifier['qualities'])
        base_gait.duration *= 0.5  # Shorten step duration
    
    return base_gait
```

### 21.4 Sentiment-Specific Gait Algorithms

```python
GAIT_BY_RASA = {
    'Åšá¹›á¹…gÄra': {
        'ordinary_love': {
            'cÄrÄ«': 'AtikrÄnta',
            'qualities': ['graceful', 'adorned', 'measured'],
            'hands': 'follow feet smoothly'
        },
        'concealed_love': {
            'movement': 'dismisses servants, walks alone',
            'qualities': ['cautious', 'eager', 'looking around']
        }
    },
    'VÄ«ra': {
        'gait': 'bold, martial',
        'qualities': ['forceful steps', 'chest raised', 'arms active'],
        'cÄrÄ«': 'varies with weapon'
    },
    'Raudra': {
        'gait': 'aggressive',
        'qualities': ['stamping', 'quick', 'threatening'],
        'tempo': 'quick to very quick'
    },
    'Karuá¹‡a': {
        'gait': 'slow tempo',
        'qualities': ['eyes tearful', 'limbs drooping', 'arms thrown up and down'],
        'special': 'feet not raised high, body bent in dejection'
    },
    'BhayÄnaka': {
        'gait': 'Eá¸akakrÄ«á¸ita CÄrÄ«',
        'qualities': ['trembling', 'eyes wide and moving', 'quick steps'],
        'special': 'feet sometimes close, sometimes distant, hands follow'
    },
    'HÄsya': {
        'gait': 'swift short steps',
        'qualities': ['bouncing', 'varied direction'],
        'character_types': 'middling and inferior primarily'
    },
    'Adbhuta': {
        'gait': 'swift short steps in all directions',
        'qualities': ['sudden changes', 'expansive gestures']
    }
}
```

### 21.5 Special Condition Gaits

```python
SPECIAL_GAITS = {
    'darkness_or_blindness': {
        'feet': 'drawn over ground (not lifted)',
        'hands': 'groping for the way',
        'quality': 'tentative, searching'
    },
    'riding_chariot': {
        'posture': 'SamapÄda SthÄna',
        'hands': 'one holds bow, other holds pole',
        'quality': 'mimicry of being carried',
        'entry': 'quick simple steps'
    },
    'riding_horse': {
        'posture': 'VaiÅ›Äkha SthÄna',
        'steps': 'simple, various kinds',
        'token': 'holding bit/bridle'
    },
    'swimming': {
        'shallow_water': 'tucking up clothes',
        'deep_water': 'throwing out hands, body bent forward',
        'carried_by_current': 'arms stretch alternately, mouth fills'
    },
    'intoxication_light': {
        'quality': 'reeling',
        'feet': 'sometimes going backwards'
    },
    'intoxication_heavy': {
        'quality': 'staggering',
        'feet': 'unsteady',
        'body': 'reeling'
    },
    'lunacy': {
        'steps': 'irregular',
        'quality': 'imitates various types of men',
        'behavior': 'talks without reason, sings, laughs, dances randomly'
    },
    'old_age': {
        'body': 'trembling',
        'feet': 'raised slowly',
        'breathing': 'takes breath with each step'
    },
    'corpulence': {
        'feet': 'raised slowly',
        'quality': 'drags body with effort'
    }
}
```

---

## 22. ViÅ›eá¹£Äbhinaya: Special Representation Protocols

### 22.1 Core Principle

Certain narrative elements cannot be shown literally and require conventional representation. These protocols allow the staging of weather, time, death, dreams, and other phenomena through codified physical and vocal techniques.

### 22.2 Season Representation Algorithm

```python
SEASON_REPRESENTATION = {
    'Å›arad_autumn': {
        'behavioral': 'composure of all senses, tranquility',
        'visual': 'view of different flowers',
        'quality': 'serene, balanced'
    },
    'hemanta_early_winter': {
        'superior_middling': 'narrowing limbs, seeking sun/fire/warm clothing',
        'inferior': 'groaning, clicking, trembling head/lips, chattering teeth'
    },
    'Å›iÅ›ira_winter': {
        'behavioral': 'smelling flowers, drinking wine',
        'environmental': 'pleasant wind indicated'
    },
    'vasanta_spring': {
        'behavioral': 'acts of rejoicing, enjoyments, festivities',
        'visual': 'display of various flowers'
    },
    'grÄ«á¹£ma_summer': {
        'behavioral': 'fans, wiping sweat',
        'environmental': 'heat of earth, hot wind indicated'
    },
    'vará¹£Ä_rainy_season': {
        'visual': 'Kadamba, Nimba, Kutaja flowers; green grass; Indragopa insects',
        'grouping': 'peacocks gathering'
    },
    'rainy_night': {
        'auditory': 'loud sound of clouds',
        'visual': 'falling showers, lightning',
        'environmental': 'thunder indicated'
    }
}

def represent_season(season, character_type):
    """
    Season representation varies by character status.
    """
    season_protocol = SEASON_REPRESENTATION[season]
    
    # Superior characters may indicate discomfort more subtly
    if character_type == 'superior' and 'superior_middling' in season_protocol:
        return season_protocol['superior_middling']
    elif character_type == 'inferior' and 'inferior' in season_protocol:
        return season_protocol['inferior']
    else:
        return season_protocol.get('behavioral', season_protocol)
```

### 22.3 Death Representation Algorithm

```python
DEATH_REPRESENTATION = {
    'general_principle': """
        Death from different conditions requires different representation.
        Sometimes throwing out all hands and feet,
        sometimes paralysis of all limbs.
    """,
    
    'death_from_disease': {
        'vocal': 'hiccough, hard breathing',
        'physical': 'imperceptible movement, relaxed limbs'
    },
    
    'death_from_poison': {
        'physical': 'throwing out hands, feet, limbs',
        'progression': 'quivering action through body parts',
        'eight_stages': [
            ('glÄni', 'general weaknessâ€”sunken eyes, depressed cheeks/lips/belly/shoulder, feeble arms'),
            ('vepathu', 'tremorâ€”shaking head, hands, feet simultaneously or separately'),
            ('dÄha', 'burning sensation'),
            ('hikkÄ', 'hiccough'),
            ('phena', 'froth in mouth'),
            ('grÄ«vÄbhaá¹…ga', 'breaking/bending of neck'),
            ('stambha', 'paralysis/rigidity'),
            ('maraá¹‡a', 'death')
        ]
    },
    
    'dying_speech': {
        'voice': 'indistinct (kala)',
        'speech_organs': 'relaxed and heavy',
        'quality': 'faltering, like sound of small bells',
        'accompaniments': 'hiccough, hard breathing, phlegm action'
    },
    
    'swoon_resembling_death': {
        'indicators': 'hiccough and hard breathing',
        'speech': 'contains repetition'
    }
}

def represent_death(cause, character):
    """
    Select appropriate death representation protocol.
    """
    if cause == 'disease':
        return execute_disease_death(character)
    elif cause == 'poison':
        return execute_poison_death_stages(character)
    elif cause == 'weapon':
        return execute_violent_death(character)
    elif cause == 'grief':
        return execute_grief_death(character)
```

### 22.4 Speech Mode Protocols

```python
SPEECH_MODES = {
    'ÄkÄÅ›abhÄá¹£ita': {
        'name': 'Speaking to the Sky',
        'function': 'Address to invisible/absent person',
        'technique': 'Eyes directed upward/outward, no physical addressee',
        'narrative_use': 'Prayers, appeals to fate, addressing departed'
    },
    'janÄntika': {
        'name': 'Private Personal Address',
        'function': 'Confidential speech heard only by intended recipient',
        'technique': 'Words spoken in ear, preceded by "so, so"',
        'narrative_use': 'Secrets, conspiracies, intimate communication'
    },
    'Ätmagata': {
        'name': 'Speaking Aside',
        'function': 'Thoughts spoken aloud, unheard by other characters',
        'technique': 'Relates to something within oneself, deliberation and feeling',
        'narrative_use': 'Interior monologue, audience-directed commentary'
    },
    'apavÄritaka': {
        'name': 'Concealed Speaking',
        'function': 'Speech deliberately hidden from some characters',
        'technique': 'TripatÄka hand covering the speaker',
        'narrative_use': 'Plotting, private reactions, dramatic irony'
    }
}

def execute_speech_mode(mode, content, visible_to, hidden_from):
    """
    Apply appropriate speech convention.
    """
    protocol = SPEECH_MODES[mode]
    
    speech = Speech(content=content)
    speech.apply_technique(protocol['technique'])
    speech.visible_to = visible_to
    speech.hidden_from = hidden_from
    
    return speech
```

### 22.5 Sleep and Dream Representation

```python
SLEEP_REPRESENTATION = {
    'somnolent_state': {
        'gesture_rule': 'States NOT represented by hand movement',
        'method': 'Through speech (meaning of words) only',
        'rationale': 'Sleeping body does not gesture'
    },
    
    'speech_in_sleep': {
        'voice': 'slow',
        'words': 'sometimes distinct, sometimes indistinct',
        'content': 'senses repeated twice',
        'quality': 'depends on recollection of past events'
    },
    
    'dream_content': {
        'representation': 'Through sleep-speech describing visions',
        'narrative_function': 'Prophecy, memory, desire revelation'
    }
}
```

### 22.6 Word Repetition Protocol

```python
WORD_REPETITION_RULES = {
    'triggers': ['fright', 'calamity', 'anger', 'intense_sorrow'],
    
    'words_to_repeat': [
        'tell', 'well done', 'ah', 'alas', 
        'go away', 'what', 'let me go', 'no', 'speak'
    ],
    
    'repetition_count': 'twice or thrice',
    
    'function': 'Indicates emotional intensity beyond normal speech'
}
```

---

## 23. Niá¹£edha: On-Stage Prohibitions (Expanded)

### 23.1 Core Principle

Certain events must NEVER be directly shown on stage. They are reported, implied, or represented through conventional signs. This is not prudishness but dramatic wisdomâ€”some things gain power by remaining unseen.

### 23.2 Comprehensive Prohibition List

```python
STAGE_PROHIBITIONS = {
    'absolute_prohibitions': {
        # These must NEVER be shown directly
        'death_of_hero': {
            'reason': 'Hero must survive for narrative completion',
            'alternative': 'Report in PraveÅ›aka or show recovery'
        },
        'killing_on_stage': {
            'reason': 'Violence distances audience from rasa',
            'alternative': 'Sounds off-stage, character reports'
        },
        'battle': {
            'reason': 'Cannot be adequately represented',
            'alternative': 'Messengers report, sounds indicate'
        },
        'eating_on_stage': {
            'reason': 'Interrupts dramatic time',
            'alternative': 'Character exits, time passes'
        },
        'bathing': {
            'reason': 'Practical and decorum concerns',
            'alternative': 'Character enters freshly bathed'
        },
        'sexual_union': {
            'reason': 'Inappropriate for public performance',
            'alternative': 'Suggestion, time-skip, poetic description'
        },
        'sleeping': {
            'reason': 'Stops dramatic action',
            'alternative': 'Brief doze shown, full sleep off-stage'
        }
    },
    
    'contextual_prohibitions': {
        # These depend on dramatic form and context
        'siege_operations': {
            'forms': 'most nÄá¹­akas',
            'exception': 'Some single-act forms (VyÄyoga)'
        },
        'loss_of_kingdom': {
            'reason': 'Major event requires fuller treatment',
            'alternative': 'Report or show aftermath'
        },
        'journey': {
            'reason': 'Cannot show actual travel',
            'alternative': 'Walking convention represents distance'
        }
    }
}
```

### 23.3 The Report-vs-Show Decision Algorithm

```python
def should_show_or_report(event):
    """
    Determine whether an event should be staged or reported.
    """
    # Check absolute prohibitions first
    if event.type in STAGE_PROHIBITIONS['absolute_prohibitions']:
        return 'REPORT'
    
    # Check if event is too complex for staging
    if event.complexity > STAGING_THRESHOLD:
        return 'REPORT_IN_PRAVESAKA'
    
    # Check if event would break unity of impression
    if event.would_fragment_audience_attention():
        return 'REPORT'
    
    # Check if event can be adequately represented
    if not event.has_adequate_convention():
        return 'REPORT'
    
    # Default: show if possible
    return 'SHOW_WITH_CONVENTION'
```

---

## 24. Integration: The Complete Performance Algorithm

### 24.1 Scene Construction with All Systems

```python
def construct_scene(scene_data):
    """
    Integrate all systems into coherent scene construction.
    """
    scene = Scene()
    
    # 1. Establish dominant rasa
    scene.rasa = scene_data.primary_sentiment
    
    # 2. Select appropriate dhruva for entrance
    for character in scene_data.entering_characters:
        entrance_dhruva = select_dhruva_for_entrance(
            character=character,
            rasa=scene.rasa
        )
        scene.add_musical_cue(entrance_dhruva)
        
        # 3. Calculate character gait
        gait = calculate_gait(character)
        gait = modify_gait_for_state(gait, character.emotional_state)
        gait = adjust_gait_for_rasa(gait, scene.rasa)
        character.set_gait(gait)
        
        # 4. Establish zone position
        character.enter_from_zone(
            determine_entrance_zone(character.type)
        )
    
    # 5. Handle special representations
    for element in scene_data.special_elements:
        if element.type == 'season':
            apply_season_representation(element, scene)
        elif element.type == 'time_of_day':
            apply_time_representation(element, scene)
        elif element.type == 'aside':
            apply_speech_mode(element, 'Ätmagata')
    
    # 6. Validate against prohibitions
    for event in scene_data.events:
        if event.type in STAGE_PROHIBITIONS:
            event.convert_to_report()
    
    # 7. Add exit dhruvas
    for character in scene_data.exiting_characters:
        exit_dhruva = select_dhruva_for_exit(character, scene.rasa)
        scene.add_musical_cue(exit_dhruva)
    
    return scene
```

---

## 25. Extended Diagnostic Questions

### 25.1 Dhruva Integration Checklist

| Question | Purpose |
|----------|---------|
| "Does every entrance have an accompanying dhruva?" | Verify musical-narrative integration |
| "Does the dhruva tempo match the rasa?" | Check music-sentiment alignment |
| "Are exits musically marked?" | Verify structural punctuation |

### 25.2 Spatial Grammar Checklist

| Question | Purpose |
|----------|---------|
| "Is character position meaningful?" | Verify zone significance |
| "Do walking patterns indicate distance appropriately?" | Check distance convention |
| "Are conveyances represented by tokens?" | Verify symbolic staging |

### 25.3 Gait Consistency Checklist

| Question | Purpose |
|----------|---------|
| "Does gait match character type?" | Verify base parameters |
| "Does emotional state modify gait appropriately?" | Check state modifiers |
| "Is gait consistent with dominant rasa?" | Verify sentiment alignment |

### 25.4 Special Representation Checklist

| Question | Purpose |
|----------|---------|
| "Are seasons indicated through behavioral/visual signs?" | Verify environmental representation |
| "Are speech modes correctly applied (aside, sky-speech, etc.)?" | Check vocal conventions |
| "Are prohibited events reported rather than shown?" | Verify staging boundaries |

---

## Appendix G: Complete Numerical Reference (All Documents)

| Category | Count | Location |
|----------|-------|----------|
| Meta-Principles | 7 | Primary Â§0 |
| Rasas | 8 | Primary Â§1 |
| Bhavas | 49 (8+33+8) | Primary Â§2 |
| Abhinaya Modes | 4 | Primary Â§3 |
| DharmÄ«s | 2 | Primary Â§4 |
| Vá¹›ttis | 4 | Primary Â§5 |
| Plot Stages | 5 | Primary Â§6 |
| Plot Elements | 5 | Primary Â§6 |
| Sandhis | 5 | Primary Â§6 |
| Dramatic Forms | 10 | Primary Â§7 |
| Hero Types | 4 | Primary Â§8 |
| Heroine Types | 8 | Primary Â§8 |
| Siddhi Types | 2 | Primary Â§9 |
| Blemish Categories | 4 | Supplement Â§12 |
| Self-Made Blemishes | 12+ | Supplement Â§12 |
| PÅ«rvaraá¹…ga Components | 19 | Supplement Â§14 |
| Dhruva Types | 5 | Extended Â§19 |
| Stage Zones | 4+ | Extended Â§20 |
| Gait Parameters | 3 types | Extended Â§21 |
| Season Representations | 7 | Extended Â§22 |
| Speech Modes | 4 | Extended Â§22 |
| Poison Death Stages | 8 | Extended Â§22 |
| Absolute Prohibitions | 7 | Extended Â§23 |

---

## Appendix H: Extended Glossary (All Documents)

| Term | Sanskrit | Meaning |
|------|----------|---------|
| Dhruva | à¤§à¥à¤°à¥à¤µ | Fixed song; musical cue marking narrative beat |
| PrÄveÅ›ikÄ« | à¤ªà¥à¤°à¤¾à¤µà¥‡à¤¶à¤¿à¤•à¥€ | Entrance dhruva |
| Niá¹£krÄmikÄ« | à¤¨à¤¿à¤·à¥à¤•à¥à¤°à¤¾à¤®à¤¿à¤•à¥€ | Exit dhruva |
| Ä€ká¹£epikÄ« | à¤†à¤•à¥à¤·à¥‡à¤ªà¤¿à¤•à¥€ | Incidental/casual dhruva |
| PrÄsÄdikÄ« | à¤ªà¥à¤°à¤¾à¤¸à¤¾à¤¦à¤¿à¤•à¥€ | Pleasing/resolution dhruva |
| Ä€ntarÄ | à¤†à¤¨à¥à¤¤à¤°à¤¾ | Intermediate/interval dhruva |
| Kaká¹£yÄ | à¤•à¤•à¥à¤·à¥à¤¯à¤¾ | Stage zone, spatial division |
| Gati | à¤—à¤¤à¤¿ | Gait, manner of walking |
| TÄla | à¤¤à¤¾à¤² | Unit of spatial measure (for steps) |
| KalÄ | à¤•à¤²à¤¾ | Unit of temporal measure (for step duration) |
| ViÅ›eá¹£Äbhinaya | à¤µà¤¿à¤¶à¥‡à¤·à¤¾à¤­à¤¿à¤¨à¤¯ | Special representation |
| Ä€kÄÅ›abhÄá¹£ita | à¤†à¤•à¤¾à¤¶à¤­à¤¾à¤·à¤¿à¤¤ | Speaking to the sky (addressing invisible) |
| JanÄntika | à¤œà¤¨à¤¾à¤¨à¥à¤¤à¤¿à¤• | Private personal address |
| Ä€tmagata | à¤†à¤¤à¥à¤®à¤—à¤¤ | Speaking aside |
| ApavÄritaka | à¤…à¤ªà¤µà¤¾à¤°à¤¿à¤¤à¤• | Concealed speaking |
| Niá¹£edha | à¤¨à¤¿à¤·à¥‡à¤§ | Prohibition, what must not be shown |

---

*This extended document completes the algorithmic distillation of Bharata Muni's Natyasastra. Together with the primary document (Â§0-11) and supplement (Â§12-18), it provides comprehensive coverage of narratologically significant principles.*

*Compiled from Bharata Muni. Natyasastra: A Treatise on Hindu Dramaturgy and Histrionics. Translated by Manomohan Ghosh. Calcutta: Asiatic Society of Bengal, 1950.*
