# Plato's Narratological Algorithms

A systematic distillation of Plato's *Republic* (c. 375 BCE) into formal, implementable principles for narrative construction, evaluation, and censorship.

**Source**: *The Republic*, Books II, III, and X (Benjamin Jowett translation)

---

## Table of Contents

0. [Meta-Principles (Axioms)](#0-meta-principles-axioms)
1. [The Three Modes of Narration](#1-the-three-modes-of-narration)
2. [The Ontological Hierarchy (Three Removes from Truth)](#2-the-ontological-hierarchy-three-removes-from-truth)
3. [The Userâ€“Makerâ€“Imitator Knowledge Hierarchy](#3-the-usermakerimitator-knowledge-hierarchy)
4. [The Tripartite Soul and Mimetic Address](#4-the-tripartite-soul-and-mimetic-address)
5. [Content Regulation Algorithms](#5-content-regulation-algorithms)
6. [The Lie Typology](#6-the-lie-typology)
7. [The Specialization Principle](#7-the-specialization-principle)
8. [Harmony, Rhythm, and Style Protocol](#8-harmony-rhythm-and-style-protocol)
9. [The Psychic Contagion Mechanism](#9-the-psychic-contagion-mechanism)
10. [Admitted vs. Excluded Poetry](#10-admitted-vs-excluded-poetry)
11. [Diagnostic Questions](#11-diagnostic-questions)
12. [Theoretical Correspondence Table](#12-theoretical-correspondence-table)
13. [Quick Reference Card](#13-quick-reference-card)

---

## 0. Meta-Principles (Axioms)

| Axiom | Formulation |
|-------|-------------|
| P-A0 | **"Truth over Reverence."** A man is not to be reverenced more than the truth; evaluation must be dispassionate. |
| P-A1 | **"Mimetic Art as Inferior."** Poetical imitations are thrice removed from the truth and ruinous to the understanding. |
| P-A2 | **"Soul Formation."** Narrative form shapes the psyche; imitations grow into habits and become second nature. |
| P-A3 | **"The Master Goal."** The goal of regulation is justice in the soul, not aesthetic pleasure. |
| P-A4 | There is an "ancient quarrel between philosophy and poetry." |

### Source Quotes

> "All poetical imitations are ruinous to the understanding of the hearers, and that the knowledge of their true nature is the only antidote to them." â€”Republic X

> "The tragic poet is an imitator, and therefore, like all other imitators, he is thrice removed from the king and from the truth." â€”Republic X

> "Poetry feeds and waters the passions instead of drying them up; she lets them rule, although they ought to be controlled." â€”Republic X

> "We must remain firm in our conviction that hymns to the gods and praises of famous men are the only poetry which ought to be admitted into our State." â€”Republic X

---

## 1. Narrative Mode Identification

Plato distinguishes three fundamental modes by which poets relate events:

```
NARRATIVE_MODES:
â”œâ”€â”€ DIEGESIS (Simple Narration)
â”‚   Definition: Poet speaks in own voice throughout
â”‚   Example: Dithyramb
â”‚   Effect: Poet never conceals himself
â”‚
â”œâ”€â”€ MIMESIS (Imitation)
â”‚   Definition: Poet speaks as if he were another person
â”‚   Example: Tragedy, Comedy
â”‚   Effect: Poet "assimilates his style to that of the person"
â”‚
â””â”€â”€ MIXED MODE
    Definition: Alternation between diegesis and mimesis
    Example: Epic (Homer)
    Effect: "Double form" â€” narrative with embedded speeches
```

### 1.1 Formal Definitions

```python
class NarrativeMode:
    """Plato's taxonomy of storytelling methods."""
    
    DIEGESIS = "simple_narration"
    # "The poet is speaking in his own person;
    #  he never leads us to suppose that he is any one else."
    
    MIMESIS = "imitation"  
    # "The poet speaks in the person of another...
    #  assimilates his style to that of the person."
    
    MIXED = "combination"
    # "The combination of both is found in epic."

def identify_mode(passage):
    """
    Determine narrative mode of a passage.
    """
    if speaker == poet_voice:
        if no_character_speeches:
            return DIEGESIS
        else:
            return MIXED
    elif speaker == character_voice:
        return MIMESIS
```

### 1.2 The Homer Transformation Example

Plato demonstrates how the same content changes across modes:

```
ORIGINAL (Mixed Mode - Homer):
  "And he prayed all the Greeks... the poet is speaking in his own
   person... But in what follows he takes the person of Chryses."

TRANSFORMED TO DIEGESIS:
  "The priest came and prayed the gods on behalf of the Greeks...
   Thus he spoke, and the other Greeks revered the priest and assented.
   But Agamemnon was wroth, and bade him depart..."

TRANSFORMED TO PURE MIMESIS:
  "The intermediate passages are omitted, and the dialogue only left."
  â†’ Tragedy form
```

### 1.3 Mode Evaluation

```
PLATONIC_MODE_PREFERENCE:

  PREFERRED:    Diegesis (poet visible)
  CAUTIOUS:     Mixed (poet partially visible)
  DANGEROUS:    Pure Mimesis (poet concealed)

RATIONALE:
  Mimesis â†’ Actor "assimilates" to character
         â†’ Repeated assimilation shapes soul
         â†’ Soul becomes what it imitates
```

---

## 2. The Ontological Hierarchy (Three Removes from Truth)

The metaphysical foundation of Plato's critique: reality exists in degrees.

```
ONTOLOGICAL_HIERARCHY:

Level 1: FORMS (Ideas)
         â”œâ”€â”€ Made by: God/Nature
         â”œâ”€â”€ Quantity: One only (unique)
         â”œâ”€â”€ Status: "True existence," "the essence"
         â””â”€â”€ Example: The Idea of Bed

              â†“ (One remove)

Level 2: PARTICULARS (Things)
         â”œâ”€â”€ Made by: Craftsman/Artisan
         â”œâ”€â”€ Quantity: Many particular instances
         â”œâ”€â”€ Status: "Semblance of existence"
         â””â”€â”€ Example: A carpenter's bed

              â†“ (Two removes)

Level 3: IMAGES (Imitations)
         â”œâ”€â”€ Made by: Imitator (painter, poet)
         â”œâ”€â”€ Quantity: Infinite reproductions possible
         â”œâ”€â”€ Status: "Appearance," "thrice removed from truth"
         â””â”€â”€ Example: A painting of a bed
```

### 2.1 The Three Beds Argument

```python
def three_beds_hierarchy():
    """
    Plato's famous example demonstrating ontological levels.
    """
    
    # Level 1: The Form
    ideal_bed = Form(
        maker="God",
        quantity=1,  # "One bed in nature and one only"
        status="essentially and by nature one only",
        property="true existence"
    )
    
    # Level 2: The Particular
    physical_bed = Particular(
        maker="carpenter",
        quantity="many",
        status="indistinct expression of truth",
        relation_to_form="made in accordance with the idea"
    )
    
    # Level 3: The Image
    painted_bed = Image(
        maker="painter",
        quantity="infinite",
        status="thrice removed from the king and from the truth",
        relation_to_particular="appearance only"
    )
    
    return [ideal_bed, physical_bed, painted_bed]
```

### 2.2 Why God Made Only One Form

```
ARGUMENT:
  IF God made two beds:
    THEN "a third would still appear behind them
          which both of them would have for their idea"
    AND that third would be the true ideal bed
  
  THEREFORE:
    God "desired to be the real maker of a real bed,
        not a particular maker of a particular bed"
    
  CONCLUSION:
    Form must be unique; multiplicity = descent from truth
```

### 2.3 Imitation of Appearances

```
CRITICAL_DISTINCTION:

  QUESTION: Does the painter imitate reality or appearance?
  
  TEST: "You may look at a bed from different points of view,
         obliquely or directly or from any other point of view,
         and the bed will appear different, but there is no
         difference in reality."
  
  ANSWER: "The imitator is a long way off the truth, and can do
           all things because he lightly touches on a small part
           of them, and that part an image."
  
  THEREFORE:
    Painting/Poetry = imitation of appearance
                    â‰  imitation of reality
```

---

## 3. The Userâ€“Makerâ€“Imitator Knowledge Hierarchy

Three arts concern every object; they form a knowledge hierarchy:

```
KNOWLEDGE_HIERARCHY:

                    KNOWLEDGE
                        â”‚
    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
    â”‚                   â”‚                   â”‚
  USER              MAKER              IMITATOR
(episteme)      (correct belief)    (neither)
    â”‚                   â”‚                   â”‚
    â–¼                   â–¼                   â–¼
 KNOWS             BELIEVES             GUESSES
excellence         from user            at appearance
    â”‚                   â”‚                   â”‚
    â–¼                   â–¼                   â–¼
"speaks with      "confiding in him,    "will no more have
 authority"        will do what he       true opinion than
                   is told"              knowledge"
```

### 3.1 The Flute Example

```python
def knowledge_distribution(object_type="flute"):
    """
    Plato's three-tier knowledge hierarchy.
    """
    
    user = Agent(
        role="flute_player",
        knowledge_type="episteme",  # True knowledge
        source="direct experience of use",
        function="indicates to maker good or bad qualities"
    )
    
    maker = Agent(
        role="flute_maker", 
        knowledge_type="correct_belief",  # pistis
        source="from user, by talking to him",
        function="attain correct belief by compulsion"
    )
    
    imitator = Agent(
        role="painter_of_flutes",
        knowledge_type="neither",
        source="no use, no instruction",
        function="imitate what appears good to ignorant multitude"
    )
    
    return {
        "who_knows": user,
        "who_believes": maker,
        "who_neither": imitator
    }
```

### 3.2 The Imitator's Ignorance

```
CRITIQUE:
  
  "The imitative artist will be in a brilliant state of
   intelligence about his own creations?" â€” "Nay, very much
   the reverse."
  
  MECHANISM:
    Imitator has no use of the thing â†’ no knowledge of excellence
    Imitator has no instruction from user â†’ no correct belief
    
  RESULT:
    "Still he will go on imitating without knowing what makes
     a thing good or bad, and may be expected therefore to
     imitate only that which appears to be good to the
     ignorant multitude."
```

---

## 4. The Tripartite Soul and Mimetic Address

Plato's psychology determines which part of the soul imitation addresses.

### 4.1 The Three Parts of the Soul

```
TRIPARTITE_SOUL:

â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚  LOGISTIKON (Rational)                                      â”‚
â”‚  â”œâ”€â”€ Function: Calculates, measures, weighs                 â”‚
â”‚  â”œâ”€â”€ Tool: Reason (logos)                                   â”‚
â”‚  â”œâ”€â”€ Virtue: Wisdom/Truth                                   â”‚
â”‚  â””â”€â”€ Response to illusion: "Trusts to measure and calculation"â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚  THUMOEIDES (Spirited)                                      â”‚
â”‚  â”œâ”€â”€ Function: Honor, courage, anger                        â”‚
â”‚  â”œâ”€â”€ Aspiration: Victory, recognition                       â”‚
â”‚  â”œâ”€â”€ Virtue: Courage                                        â”‚
â”‚  â””â”€â”€ Ally of: Reason (when properly trained)                â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚  EPITHUMETIKON (Appetitive)                                 â”‚
â”‚  â”œâ”€â”€ Function: Desires, pleasures, bodily needs             â”‚
â”‚  â”œâ”€â”€ Aspiration: Satisfaction, gain                         â”‚
â”‚  â”œâ”€â”€ Vulnerability: Easily deceived by appearances          â”‚
â”‚  â””â”€â”€ Danger: "Thinks the same thing at one time great       â”‚
â”‚              and at another small"                          â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

### 4.2 Which Part Does Imitation Address?

```python
def identify_mimetic_target():
    """
    Plato's argument about which soul-part poetry addresses.
    """
    
    # The Optical Illusion Argument
    observation = """
    The body which is large when seen near, appears small
    when seen at a distance... the same object appears
    straight when looked at out of the water, and crooked
    when in the water.
    """
    
    # Two responses possible
    inferior_response = "Deceived by appearance"
    superior_response = "Corrected by measurement"
    
    # Imitation exploits the inferior
    return {
        "addresses": "inferior_principles",
        "bypasses": "calculating_and_rational_principle",
        "exploits": "weakness of human mind on which the art "
                    "of conjuring and of deceiving by light "
                    "and shadow... imposes"
    }
```

### 4.3 The Chimera Image of the Soul

```
SOUL_AS_COMPOSITE_CREATURE:

  FORM 1: "Multitudinous, many-headed monster"
          â†’ Appetitive part (desires, passions)
          
  FORM 2: "Lion"
          â†’ Spirited part (anger, honor)
          
  FORM 3: "Man" (smallest)
          â†’ Rational part
          
  EXTERIOR: "Single image, as of a man"
          â†’ How soul appears from outside

JUSTICE_DEFINITION:
  "The man within him [should have] the most complete
   mastery over the entire human creature."
  
INJUSTICE_DEFINITION:
  "Feast the multitudinous monster and strengthen the lion...
   but to starve and weaken the man"
```

---

## 5. Content Regulation Protocol

Plato's prescriptive rules for permissible narrative content.

### 5.1 Theological Content Rules

```
RULE_1: GOD_AS_AUTHOR_OF_GOOD_ONLY

  PERMITTED: God is source of good things
  FORBIDDEN: God is "author of evil to any one"
  
  IMPLEMENTATION:
    IF narrative.depicts(god.causes(evil)):
        REJECT("suicidal, ruinous, impious")
    
  RATIONALE:
    "God is not the author of all things, but of good only"


RULE_2: GOD_IS_UNCHANGING

  PERMITTED: God "remains absolutely and for ever in his own form"
  FORBIDDEN: Gods taking disguises, transforming, appearing in dreams
  
  BANNED_CONTENT:
    - "Gods, taking the disguise of strangers from other lands,
       walk up and down cities in all sorts of forms"
    - Mothers "scaring their children with a bad version of these
       myths â€” telling how certain gods 'Go about by night in the
       likeness of so many strangers'"
  
  IMPLEMENTATION:
    IF narrative.depicts(god.transforms()):
        REJECT("blasphemy against the gods")


RULE_3: GOD_DOES_NOT_DECEIVE

  PERMITTED: God is "perfectly simple and true both in word and deed"
  FORBIDDEN: God deceives "either by sign or word, by dream or waking vision"
  
  BANNED_EXAMPLE:
    - "The lying dream which Zeus sends to Agamemnon" (Homer)
    - Apollo's false prophecy to Thetis (Aeschylus)
```

### 5.2 Heroic Content Rules

```
RULE_4: NO_FEAR_OF_DEATH_IN_UNDERWORLD

  FORBIDDEN:
    - Descriptions of Hades as terrible
    - Heroes lamenting death
    - Souls "flitting about like shadows"
  
  RATIONALE:
    "If our future guardians believed this to be true, they would
     hardly be likely to face death fearlessly."
  
  IMPLEMENTATION:
    IF narrative.depicts(afterlife_as_terrible):
        REJECT("makes cowards of guardians")


RULE_5: NO_EXCESSIVE_LAMENTATION

  FORBIDDEN:
    - "Pitiful hero drawling out his sorrows in a long oration"
    - "Weeping, and smiting his breast"
    - "Inextinguishable laughter arose among the blessed gods"
  
  PERMITTED:
    - "He smote his breast, and thus reproached his heart,
       Endure, my heart; far worse hast thou endured!"
  
  IMPLEMENTATION:
    IF narrative.depicts(hero.excessive_emotion()):
        REJECT("not conducive to temperance")


RULE_6: NO_INTEMPERANCE OR DISRESPECT

  FORBIDDEN:
    - Disrespect to commanders ("O heavy with wine, who hast
       the eyes of a dog and the heart of a stag")
    - Gluttony praised ("nothing more glorious than when tables
       are full of bread and meat")
    - Gods overcome by lust (Zeus and Hera)
    - Heroes as "lovers of money" (Achilles taking bribes)
  
  PERMITTED:
    - "Friend, sit still and obey my word"
    - "The Greeks marched breathing prowess, in silent awe
       of their leaders"
```

### 5.3 The Content Evaluation Algorithm

```python
def evaluate_content(narrative):
    """
    Plato's content evaluation protocol.
    """
    
    # Theological check
    if depicts_god_causing_evil(narrative):
        return Reject("God as author of evil")
    
    if depicts_god_transforming(narrative):
        return Reject("God is unchanging")
    
    if depicts_god_deceiving(narrative):
        return Reject("God does not lie")
    
    # Heroic check
    if depicts_death_as_terrible(narrative):
        return Reject("Creates cowardice")
    
    if depicts_excessive_lamentation(narrative):
        return Reject("Weakens temperance")
    
    if depicts_disrespect_to_authority(narrative):
        return Reject("Undermines order")
    
    if depicts_intemperance_as_good(narrative):
        return Reject("Corrupts character")
    
    # Genre check
    if depicts_wicked_as_happy(narrative):
        return Reject("Until justice is defined")
    
    if depicts_just_as_miserable(narrative):
        return Reject("Until justice is defined")
    
    return Accept()
```

---

## 6. Lie Typology Filter

Plato distinguishes two kinds of lies with different moral statuses.

### 6.1 True Lie vs. Verbal Lie

```
LIE_TYPOLOGY:

â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚  TRUE LIE (pseudos alethes)                                 â”‚
â”‚  â”œâ”€â”€ Location: "In the soul"                                â”‚
â”‚  â”œâ”€â”€ Definition: "Ignorance in the soul of him who is      â”‚
â”‚  â”‚               deceived... about the highest realities    â”‚
â”‚  â”‚               in the highest part of themselves"         â”‚
â”‚  â”œâ”€â”€ Status: "Hated not only by the gods, but also by men" â”‚
â”‚  â””â”€â”€ Evaluation: ALWAYS EVIL                                â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚  VERBAL LIE (pseudos en logois)                             â”‚
â”‚  â”œâ”€â”€ Location: "In words"                                   â”‚
â”‚  â”œâ”€â”€ Definition: "A kind of imitation and shadowy image    â”‚
â”‚  â”‚               of a previous affection of the soul"       â”‚
â”‚  â”œâ”€â”€ Status: "In certain cases useful and not hateful"      â”‚
â”‚  â””â”€â”€ Evaluation: CONDITIONALLY PERMITTED                    â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

### 6.2 Permitted Uses of Verbal Lie

```python
def verbal_lie_permitted(context):
    """
    Conditions under which verbal falsehood is acceptable.
    """
    
    permitted_cases = [
        # Case 1: Against enemies
        "dealing with enemies",
        
        # Case 2: Preventing harm from friends
        "when those whom we call our friends in a fit of madness "
        "or illusion are going to do some harm, then it is useful "
        "and is a sort of medicine or preventive",
        
        # Case 3: Mythology (necessity)
        "in the tales of mythology... because we do not know "
        "the truth about ancient times, we make falsehood as "
        "much like truth as we can, and so turn it to account"
    ]
    
    # The noble lie for rulers
    ruler_privilege = """
    If any one at all is to have the privilege of lying,
    the rulers of the State should be the persons; and they,
    in their dealings either with enemies or with their own
    citizens, may be allowed to lie for the public good.
    """
    
    # Asymmetric rule
    citizen_prohibition = """
    But nobody else should meddle with anything of the kind;
    for a private man to lie to [rulers] in return is to be
    deemed a more heinous fault.
    """
    
    return context in permitted_cases
```

---

## 7. The Specialization Principle

A foundational constraint on mimetic practice.

### 7.1 The One-Art Rule

```
AXIOM:
  "One man can only do one thing well, and not many;
   and that if he attempt many, he will altogether fail
   of gaining much reputation in any."

APPLICATION_TO_IMITATION:
  "No one man can imitate many things as well as
   he would imitate a single one."

EXAMPLES:
  - Writers of tragedy â‰  writers of comedy (same persons cannot succeed)
  - Rhapsodists â‰  actors
  - Comic actors â‰  tragic actors
```

### 7.2 Implications for Guardians

```python
def guardian_imitation_protocol():
    """
    What guardians may and may not imitate.
    """
    
    # The principle
    rule = """
    Our guardians, setting aside every other business,
    are to dedicate themselves wholly to the maintenance
    of freedom in the State.
    """
    
    # What they may imitate
    permitted_imitation = [
        "brave men",
        "temperate men", 
        "holy men",
        "free men",
        "men of similar character"
    ]
    
    # What they must not imitate
    forbidden_imitation = [
        "women (young or old)",
        "slaves",
        "bad men",
        "cowards",
        "madmen",
        "craftsmen (smiths, rowers, etc.)",
        "animals (horses, bulls, rivers, sea)",
        "thunder, wind, hail, wheels, pulleys",
        "dogs, sheep"
    ]
    
    # Rationale
    rationale = """
    We would not have our guardians grow up amid images
    of moral deformity, as in some noxious pasture, and
    there browse and feed upon many a baneful herb and
    flower day by day, little by little, until they
    silently gather a festering mass of corruption in
    their own soul.
    """
    
    return {
        "permitted": permitted_imitation,
        "forbidden": forbidden_imitation,
        "rationale": rationale
    }
```

### 7.3 The Contagion of Character

```
MECHANISM:
  IF person.imitates(character_type) repeatedly:
    THEN person.becomes(character_type)
  
  "Imitations, beginning in early youth and continuing
   far into life, at length grow into habits and become
   a second nature, affecting body, voice, and mind."

THEREFORE:
  Limit imitation to excellent types only.
```

---

## 8. Harmony, Rhythm, and Style Protocol

Plato's prescriptions for musical and metrical elements.

### 8.1 The Compositional Hierarchy

```
HIERARCHY_OF_ELEMENTS:

  WORDS (logoi)
       â†“ determine
  MELODY (harmonia)
       â†“ determines  
  RHYTHM (rhythmos)

PRINCIPLE:
  "Rhythm and harmony are regulated by the words,
   and not the words by them."

IMPLICATION:
  Content (words) has priority over form (music).
  Sound must serve sense.
```

### 8.2 Permitted and Forbidden Harmonies

```
HARMONY_EVALUATION:

FORBIDDEN (to be banished):
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚  Mixed/Tenor Lydian  â”‚  "Harmonies expressive of sorrow"   â”‚
â”‚  Full-toned/Bass Lydian â”‚                                  â”‚
â”‚  Ionian              â”‚  "Soft or drinking harmonies"       â”‚
â”‚  Lydian (relaxed)    â”‚  "Termed 'relaxed'"                 â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜

PERMITTED (retained):
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚  DORIAN   â”‚  "Strain of necessity and freedom"             â”‚
â”‚           â”‚  "Strain of the unfortunate and fortunate"     â”‚
â”‚           â”‚  For: courage, stern resolve, endurance        â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚  PHRYGIAN â”‚  "Strain of courage and temperance"            â”‚
â”‚           â”‚  For: peace, freedom, persuasion, moderation   â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

### 8.3 Instrument Restrictions

```
INSTRUMENT_EVALUATION:

FORBIDDEN:
  - "Many-stringed curiously-harmonised instruments"
  - "Artificers of lyres with three corners and complex scales"
  - Flute ("in this composite use of harmony the flute is
           worse than all the stringed instruments")

PERMITTED:
  - Lyre and harp (in city)
  - Pipe (for shepherds in country)

SYMBOLIC:
  "The preferring of Apollo and his instruments to
   Marsyas and his instruments"
```

### 8.4 The Style-Soul Connection

```
PRINCIPLE:
  "Beauty of style and harmony and grace and good rhythm
   depend on simplicity â€” I mean the true simplicity of a
   rightly and nobly ordered mind and character, not that
   other simplicity which is only an euphemism for folly."

ALGORITHM:
  good_style = f(good_soul)
  good_rhythm = f(good_life)
  harmony = f(character)
  
  THEREFORE:
    To judge style â†’ judge soul that produces it
    To improve style â†’ improve soul
```

---

## 9. The Psychic Contagion Mechanism

How poetry transmits emotional states from fiction to audience.

### 9.1 The Sympathy Problem

```
OBSERVATION:
  "The best of us, as I conceive, when we listen to a passage
   of Homer, or one of the tragedians, in which he represents
   some pitiful hero who is drawling out his sorrows in a long
   oration, or weeping, and smiting his breast â€” the best of us,
   you know, delight in giving way to sympathy, and are in
   raptures at the excellence of the poet who stirs our
   feelings most."

CONTRADICTION:
  "But when any sorrow of our own happens to us, then you may
   observe that we pride ourselves on the opposite quality â€”
   we would fain be quiet and patient; this is the manly part,
   and the other which delighted us in the recitation is now
   deemed to be the part of a woman."

QUESTION:
  "Now can we be right in praising and admiring another who
   is doing that which any one of us would abominate and be
   ashamed of in his own person?"
```

### 9.2 The Infection Mechanism

```python
def psychic_contagion(audience, narrative):
    """
    How fictional emotions infect real souls.
    """
    
    # Step 1: Natural hunger for emotional release
    natural_desire = """
    When in misfortune we feel a natural hunger and desire
    to relieve our sorrow by weeping and lamentation.
    """
    
    # Step 2: Vicarious satisfaction
    vicarious_release = """
    This feeling which is kept under control in our own
    calamities is satisfied and delighted by the poets.
    """
    
    # Step 3: Guard lowered
    rationalization = """
    The better nature in each of us, not having been
    sufficiently trained by reason or habit, allows the
    sympathetic element to break loose because the sorrow
    is another's; and the spectator fancies that there can
    be no disgrace to himself in praising and pitying any
    one who comes telling him what a good man he is.
    """
    
    # Step 4: Transfer to real life
    contagion = """
    Few persons ever reflect... that from the evil of other
    men something of evil is communicated to themselves.
    And so the feeling of sorrow which has gathered strength
    at the sight of the misfortunes of others is with
    difficulty repressed in our own.
    """
    
    # Applies to all emotions
    extension = """
    The same may be said of lust and anger and all the other
    affections, of desire and pain and pleasure... poetry
    feeds and waters the passions instead of drying them up.
    """
    
    return "Soul corrupted by strengthened passions"
```

### 9.3 The Comedy Parallel

```
THE_RISIBLE_FACULTY:

  OBSERVATION:
    "There are jests which you would be ashamed to make
     yourself, and yet on the comic stage, or indeed in
     private, when you hear them, you are greatly amused
     by them, and are not at all disgusted."
  
  MECHANISM:
    "There is a principle in human nature which is disposed
     to raise a laugh, and this which you once restrained
     by reason, because you were afraid of being thought a
     buffoon, is now let out again."
  
  CONSEQUENCE:
    "Having stimulated the risible faculty at the theatre,
     you are betrayed unconsciously to yourself into playing
     the comic poet at home."
```

---

## 10. Admitted vs. Excluded Poetry

### 10.1 The Final Verdict

```
EXCLUDED_POETRY:
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚  TYPE: "The honeyed muse... either in epic or lyric verse" â”‚
â”‚                                                             â”‚
â”‚  CHARACTERISTICS:                                           â”‚
â”‚  - Addresses irrational soul parts                          â”‚
â”‚  - Imitates passionate, fitful temper                       â”‚
â”‚  - Strengthens passions at expense of reason                â”‚
â”‚  - "Pleasure and pain will be the rulers"                   â”‚
â”‚                                                             â”‚
â”‚  STATUS: "Not to be regarded seriously as attaining to      â”‚
â”‚           the truth"                                        â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜

ADMITTED_POETRY:
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚  TYPE 1: "Hymns to the gods"                                â”‚
â”‚  TYPE 2: "Praises of famous men"                            â”‚
â”‚                                                             â”‚
â”‚  CHARACTERISTICS:                                           â”‚
â”‚  - "Law and the reason of mankind... have ever been         â”‚
â”‚     deemed best"                                            â”‚
â”‚  - Supports rational order                                  â”‚
â”‚  - Strengthens "man within"                                 â”‚
â”‚                                                             â”‚
â”‚  STATUS: "The only poetry which ought to be admitted        â”‚
â”‚           into our State"                                   â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

### 10.2 The Conditional Readmission

```python
def poetry_readmission_protocol():
    """
    Conditions under which excluded poetry might return.
    """
    
    challenge = """
    Let us assure our sweet friend and the sister arts of
    imitation that if she will only prove her title to exist
    in a well-ordered State we shall be delighted to receive her.
    """
    
    condition_1 = """
    She make a defence of herself in lyrical or some other metre.
    """
    
    condition_2 = """
    Let them show not only that she is pleasant but also useful
    to States and to human life.
    """
    
    if defense_successful():
        return "We shall surely be the gainers"
    else:
        return """
        Like other persons who are enamoured of something,
        but put a restraint upon themselves when they think
        their desires are opposed to their interests, so too
        must we after the manner of lovers give her up,
        though not without a struggle.
        """
```

### 10.3 The Self-Protective Charm

```
AUDIENCE_PROTOCOL:

  "This argument of ours shall be a charm to us, which we
   will repeat to ourselves while we listen to her strains;
   that we may not fall away into the childish love of her
   which captivates the many."
  
  IMPLEMENTATION:
    WHILE consuming_poetry():
        remember("poetry is not truth")
        remember("it addresses inferior soul parts")
        remember("it strengthens passions")
        guard("the city which is within")
```

---

## 11. Diagnostic Questions

### 11.1 Narrative Mode Diagnosis

```
â–¡ Is the poet speaking in his own voice or as a character?
â–¡ If mixed, what is the ratio of narration to impersonation?
â–¡ Does the narrative conceal or reveal the poet's presence?
â–¡ What modes of imitation does it require from performers?
```

### 11.2 Ontological Status Diagnosis

```
â–¡ Is this narrative about Forms, particulars, or images?
â–¡ How many removes from truth is the depicted content?
â–¡ Does the narrative imitate reality or appearance?
â–¡ Does it "lightly touch on a small part" while claiming wholeness?
```

### 11.3 Psychological Target Diagnosis

```
â–¡ Which part of the soul does this narrative address?
â–¡ Does it strengthen reason or passion?
â–¡ Does it feed the "many-headed monster" or the "man within"?
â–¡ Would the audience be ashamed to do in life what they enjoy in fiction?
```

### 11.4 Content Diagnosis

```
â–¡ Are gods depicted as authors of good only?
â–¡ Are gods depicted as unchanging and truthful?
â–¡ Are heroes depicted as temperate and courageous?
â–¡ Does the narrative inspire courage or fear regarding death?
â–¡ Are the wicked shown as happy or the just as miserable?
```

### 11.5 Contagion Risk Diagnosis

```
â–¡ What emotions does this narrative cultivate in audiences?
â–¡ Would repeated exposure strengthen passions or reason?
â–¡ Does it release feelings that should remain controlled?
â–¡ Will the audience carry these emotions into their own lives?
```

## 11. Diagnostic Questions

1. **Does the poet speak in their own voice (Diegesis) or as a character (Mimesis)?** (DIEGESIS PREFERRED)
2. **How many removes from the 'Form' (Truth) is this representation?** (MINIMAL REMOVES)
3. **Which part of the soul (Rational, Spirited, Appetitive) does this narrative address?** (RATIONAL)
4. **Are gods depicted as anything other than the source of good things?** (NO)
5. **Does the work encourage emotional release that the audience would be ashamed of in real life?** (NO)
6. **Does this work strengthen the 'city within' (rational governance)?** (YES)

---

## 12. Theoretical Correspondence Table

| Platonic Concept | Modern Equivalent | Theoretical Analog |
|------------------|-------------------|-------------------|
| **Diegesis** | Narration | Genette's "telling" |
| **Mimesis** | Dramatic imitation | Genette's "showing" |
| **Three removes** | Remediation theory | Baudrillard's simulacra orders |
| **Tripartite soul** | Psychoanalytic topology | Freud's id/ego/superego |
| **Psychic contagion** | Identification theory | Aristotle's catharsis (inverted) |
| **Specialization** | Division of labor | McKee's archetype vs. stereotype |
| **User/Maker/Imitator** | Practitioner/Designer/Artist | Know-how vs. Know-that distinction |
| **Admitted poetry** | Didactic art | Socialist realism; morality plays |
| **True lie** | Ideological false consciousness | Marx's camera obscura |
| **Verbal lie** | Noble fiction | Plato's "myth of metals" |

### Cross-References to Other Frameworks

```
PLATO â†’ ARISTOTLE:
  Plato's critique of mimesis â†’ Aristotle's defense of catharsis
  Plato: Poetry "feeds passions" â†’ Aristotle: Poetry "purges passions"
  Plato: Imitation = corruption â†’ Aristotle: Imitation = natural learning
  
PLATO â†’ McKEE:
  Three removes from truth â‰ˆ McKee's "true character vs. characterization"
  User/Maker/Imitator â‰ˆ McKee's "master/journeyman/amateur"
  Psychic contagion â‰ˆ McKee's "emotional truth" (inverted valence)
  
PLATO â†’ KUBRICK:
  Plato: Poet should not conceal himself â†’ Kubrick: Director as visible author
  Plato: Address reason not passion â†’ Kubrick: "Subconscious impact"
  Plato: Fear mimesis â†’ Kubrick: Embrace non-submersible units
```

---

## 13. Quick Reference Card

### The Core Equations

```
ONTOLOGY:
  Truth = Forms > Particulars > Images
  Artist = Imitator of appearance (three removes)

PSYCHOLOGY:
  Soul = Reason > Spirit > Appetite
  Mimesis addresses: Appetite (inferior)

KNOWLEDGE:
  User > Maker > Imitator
  Imitator has: neither knowledge nor correct belief

EFFECT:
  Poetry â†’ feeds passions â†’ weakens reason â†’ corrupts soul
```

### Mode Classification

```
DIEGESIS:    Poet visible, no impersonation
MIMESIS:     Poet concealed, full impersonation
MIXED:       Alternation of both
```

### Content Rules (Quick Check)

```
GODS:
  âœ“ Author of good only
  âœ“ Unchanging
  âœ“ Truthful
  âœ— Causing evil
  âœ— Transforming
  âœ— Deceiving

HEROES:
  âœ“ Courageous
  âœ“ Temperate  
  âœ“ Obedient to authority
  âœ— Fearing death
  âœ— Lamenting excessively
  âœ— Disrespecting leaders
  âœ— Loving money

GENERAL:
  âœ“ Just shown as happy
  âœ“ Wicked shown as miserable
  âœ— Wicked shown as happy
  âœ— Just shown as miserable
```

### The Fundamental Test

```
"He who listens to [poetry], fearing for the safety of the
 city which is within him, should be on his guard against
 her seductions and make our words his law."

QUESTION:
  Does this narrative strengthen the "city within"
  (rational governance of the soul) or weaken it
  (letting passions rule)?
  
IF strengthens â†’ ADMIT
IF weakens â†’ EXCLUDE (or consume with protective charm)
```

---

## Appendix A: The Ancient Quarrel

Plato acknowledges the conflict between his view and poetic tradition:

```
"There is an ancient quarrel between philosophy and poetry;
 of which there are many proofs, such as the saying of
 'the yelping hound howling at her lord,' or of one
 'mighty in the vain talk of fools,' and 'the mob of sages
 circumventing Zeus,' and the 'subtle thinkers who are
 beggars after all'; and there are innumerable other signs
 of ancient enmity between them."
```

This quarrel represents the tension between:
- **Philosophy**: Seeks truth through reason
- **Poetry**: Produces appearances that move emotions

Plato's Republic sides firmly with philosophy, while acknowledging poetry's seductive power: "We are very conscious of her charms."

---

## Appendix B: Implementation Notes

### For Writers

Plato's framework, though restrictive, offers diagnostic value:

1. **Mode awareness**: Know when you're showing vs. telling
2. **Ontological honesty**: Acknowledge you deal in appearances
3. **Psychological targeting**: Consider which soul-parts you address
4. **Contagion responsibility**: Accept that fiction shapes character

### For Critics

Plato provides a systematic evaluation framework:

1. **Map the ontological level** of representation
2. **Identify the psychological target** of the work
3. **Assess the ethical content** against explicit rules
4. **Evaluate the contagion risk** for audiences

### Limitations

Plato's framework assumes:
- Fixed tripartite soul (contested by later psychology)
- Clear hierarchy of knowledge (contested by epistemology)
- Narrative as moral danger (contested by Aristotle's catharsis)
- State authority over art (contested by liberal aesthetics)

Modern applications should treat Plato's algorithms as diagnostic tools rather than prescriptive mandates.

---

## Appendix C: Glossary of Key Terms

| Greek Term | Transliteration | Translation | Definition |
|------------|-----------------|-------------|------------|
| Î¼Î¯Î¼Î·ÏƒÎ¹Ï‚ | mimesis | imitation | Speaking as if one were another |
| Î´Î¹Î®Î³Î·ÏƒÎ¹Ï‚ | diegesis | narration | Speaking in one's own voice |
| Îµá¼¶Î´Î¿Ï‚ | eidos | form/idea | The eternal, unique essence |
| Î»Î¿Î³Î¹ÏƒÏ„Î¹ÎºÏŒÎ½ | logistikon | rational | Calculating part of soul |
| Î¸Ï…Î¼Î¿ÎµÎ¹Î´Î­Ï‚ | thumoeides | spirited | Honor-seeking part of soul |
| á¼Ï€Î¹Î¸Ï…Î¼Î·Ï„Î¹ÎºÏŒÎ½ | epithumetikon | appetitive | Desire-driven part of soul |
| ÏˆÎµá¿¦Î´Î¿Ï‚ | pseudos | lie/falsehood | Either true lie or verbal lie |
| á¼ÏÎ¼Î¿Î½Î¯Î± | harmonia | harmony | Musical mode |
| á¿¥Ï…Î¸Î¼ÏŒÏ‚ | rhythmos | rhythm | Metrical pattern |
| Ï†Î±Î½Ï„Î¬ÏƒÎ¼Î±Ï„Î± | phantasmata | appearances | Images, not reality |
