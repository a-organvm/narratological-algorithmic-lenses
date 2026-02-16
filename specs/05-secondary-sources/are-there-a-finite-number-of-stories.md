# Are there a finite number of stories? The enduring quest to enumerate narrative

**Stories may cluster into a small number of emotional shapes, but the claim that all narratives reduce to a fixed set of “basic plots” rests on shaky epistemological ground.** Computational analysis confirms that sentiment trajectories converge toward roughly six patterns—  validating Kurt Vonnegut’s rejected 1947 thesis—yet these emotional arcs are distinct from plot, character, or meaning. The major theoretical taxonomies (Polti’s 36 situations, Booker’s 7 plots, Propp’s 31 functions, Campbell’s 17-stage monomyth) each operate at different levels of abstraction and conflate fundamentally different aspects of narrative. While Propp’s morphology offers genuine computational tractability—enabling procedural story generation since the 1970s—the Jungian foundations underlying Campbell and Booker have been challenged as empirically unverifiable and culturally biased. Non-Western and Indigenous narrative traditions that follow circular, non-linear structures rather than Aristotelian beginnings, middles, and ends present serious counterexamples to claims of universality. 

-----

## Aristotle’s foundational categories established Western dramatic theory

The enumeration project begins with **Aristotle’s *Poetics* (c. 335 BCE)**, which established plot (*mythos*) as the “soul of tragedy”—more important than character, thought, diction, melody, or spectacle. Aristotle distinguished **simple plots** (change of fortune without reversal or recognition) from **complex plots** containing *peripeteia* (reversal of fortune) and *anagnorisis* (recognition/discovery). His touchstone was *Oedipus Rex*, where reversal and recognition occur simultaneously.

Aristotle’s emphasis on **organic unity**—that plots should have beginning, middle, and end, with parts connected “like a living organism”—became the dominant Western assumption. His concept of *catharsis* (emotional purging through pity and fear) and *hamartia* (tragic flaw) shaped two millennia of dramatic theory and provided the conceptual vocabulary later theorists inherited.

-----

## Polti’s 36 dramatic situations: a systematic catalog

**Georges Polti’s *The Thirty-Six Dramatic Situations* (1895)** represents the first comprehensive attempt at enumeration. Polti claimed to validate an assertion attributed to the Italian playwright **Carlo Gozzi (1720–1806)**, author of *Turandot*, who allegedly maintained there could only be 36 tragic situations.  As Polti quoted Goethe: “Gozzi maintained that there can be but thirty-six tragic situations. Schiller took great pains to find more, but he was unable to find even so many as Gozzi.”  Gozzi never published his list; Polti supplied the systematic cataloging.

The **complete 36 situations** are:

|# |Situation                               |Example                  |
|--|----------------------------------------|-------------------------|
|1 |Supplication                            |                         |
|2 |Deliverance                             |                         |
|3 |Crime Pursued by Vengeance              |                         |
|4 |Vengeance Taken for Kin upon Kin        |*Hamlet*                 |
|5 |Pursuit                                 |*Les Misérables*         |
|6 |Disaster                                |                         |
|7 |Falling Prey to Cruelty/Misfortune      |*Job*                    |
|8 |Revolt                                  |*Julius Caesar*          |
|9 |Daring Enterprise                       |*Raiders of the Lost Ark*|
|10|Abduction                               |Helen of Troy            |
|11|The Enigma                              |                         |
|12|Obtaining                               |                         |
|13|Enmity of Kin                           |                         |
|14|Rivalry of Kin                          |                         |
|15|Murderous Adultery                      |                         |
|16|Madness                                 |*The Shining*            |
|17|Fatal Imprudence                        |                         |
|18|Involuntary Crimes of Love              |                         |
|19|Slaying of Kin Unrecognized             |*Oedipus*                |
|20|Self-Sacrifice for an Ideal             |                         |
|21|Self-Sacrifice for Kin                  |                         |
|22|All Sacrificed for Passion              |                         |
|23|Necessity of Sacrificing Loved Ones     |Binding of Isaac         |
|24|Rivalry of Superior vs. Inferior        |                         |
|25|Adultery                                |                         |
|26|Crimes of Love                          |                         |
|27|Discovery of the Dishonor of a Loved One|                         |
|28|Obstacles to Love                       |*Romeo and Juliet*       |
|29|An Enemy Loved                          |                         |
|30|Ambition                                |                         |
|31|Conflict with a God                     |                         |
|32|Mistaken Jealousy                       |                         |
|33|Erroneous Judgment                      |                         |
|34|Remorse                                 |                         |
|35|Recovery of a Lost One                  |*Finding Nemo*           |
|36|Loss of Loved Ones                      |                         |

Polti analyzed classical Greek tragedies, French dramatic literature, and select non-French authors.  Crucially, these are **dramatic situations, not plots**—how characters respond to the situation creates the plot.  Each situation includes essential character roles (persecutor, suppliant, victim) and contains multiple sub-variations.

-----

## Propp’s 31 functions: the structuralist revolution

**Vladimir Propp’s *Morphology of the Folktale* (1928)** introduced scientific rigor to narrative analysis.  By analyzing **100 Russian fairy tales** from the Afanasyev collection, Propp identified **31 narrative functions**  that occur in **fixed sequential order**:

**Preparatory Section (Functions 0–7):**

- Initial Situation → Absentation → Interdiction → Violation → Reconnaissance → Delivery → Trickery → Complicity

**Complication (Functions 8–11):**

- Villainy/Lack → Mediation → Counteraction → Departure

**Donor Sequence (Functions 12–19):**

- Testing → Reaction → Acquisition → Guidance → Struggle → Branding → Victory → Resolution

**Hero’s Return (Functions 20–31):**

- Return → Pursuit → Rescue → Arrival → Claim → Task → Solution → Recognition → Exposure → Transfiguration → Punishment → Wedding

Propp also identified **7 character archetypes**: the Villain, Dispatcher, Helper, Princess (and her Father), Donor, Hero, and False Hero.  Functions are defined by their **role in narrative**, not specific content—whether a hero receives a magic sword or a ring, the function “Acquisition of Magical Agent” remains the same.

Propp’s syntagmatic (sequential) analysis influenced Lévi-Strauss, Barthes, and modern narratology,  though Lévi-Strauss critiqued Propp’s approach as differing from his own paradigmatic structural analysis. Propp’s formalism proved **uniquely amenable to computational implementation**, powering story generation systems from the 1970s onward.

-----

## Campbell’s monomyth: the hero with a thousand faces

**Joseph Campbell’s *The Hero with a Thousand Faces* (1949)** synthesized comparative mythology with Jungian psychology into the concept of the **monomyth**—a term borrowed from James Joyce.  Campbell argued that hero myths across cultures share a common structure:

> “A hero ventures forth from the world of common day into a region of supernatural wonder: fabulous forces are there encountered and a decisive victory is won: the hero comes back from this mysterious adventure with the power to bestow boons on his fellow man.”  

Campbell’s **17 stages** divide into three phases: 

**Departure (Separation):** The Call to Adventure → Refusal of the Call → Supernatural Aid → Crossing the First Threshold → Belly of the Whale

**Initiation:** The Road of Trials → Meeting with the Goddess → Woman as Temptress → Atonement with the Father → Apotheosis → The Ultimate Boon

**Return:** Refusal of the Return → The Magic Flight → Rescue from Without → Crossing the Return Threshold → Master of Two Worlds → Freedom to Live

Campbell drew on Greek, Hindu, Buddhist, Native American, Egyptian, and Christian mythologies, arguing myths serve “to carry the individual through the stages of one’s life.”  His work achieved massive cultural influence after **George Lucas** explicitly modeled *Star Wars* on it, and screenwriter **Christopher Vogler** condensed the 17 stages to 12 in *The Writer’s Journey* (1992), which became a Hollywood touchstone.

-----

## Booker’s seven basic plots and the Jungian synthesis

**Christopher Booker’s *The Seven Basic Plots: Why We Tell Stories* (2004)** represents the most ambitious modern attempt at enumeration—**34 years** of research   condensed into **728 pages**.  Booker identified:

1. **Overcoming the Monster** – Hero defeats evil threatening homeland (*Beowulf*, *Star Wars*, *Jaws*) 
1. **Rags to Riches** – Poor protagonist gains wealth/power, loses it, regains it with personal growth (*Cinderella*, *Jane Eyre*) 
1. **The Quest** – Hero and companions seek an object or destination (*Lord of the Rings*, *Raiders of the Lost Ark*) 
1. **Voyage and Return** – Journey to strange world, adventures, return transformed (*Alice in Wonderland*, *Wizard of Oz*) 
1. **Comedy** – Increasing confusion resolves in clarifying event; happy ending (*A Midsummer Night’s Dream*) 
1. **Tragedy** – Protagonist’s character flaw leads to destruction (*Macbeth*, *Anna Karenina*, *Breaking Bad*) 
1. **Rebirth** – Hero under dark spell experiences redemption through love (*A Christmas Carol*, *Sleeping Beauty*)

Booker argued for a common **five-stage structure**: Anticipation → Dream → Frustration → Nightmare → Destruction or Rebirth.  Drawing explicitly on **Carl Jung’s analytical psychology**, he treated these plots as archetypal patterns embedded in the collective unconscious, representing psychological journeys toward individuation. 

-----

## Tobias’s 20 master plots and the practitioner’s perspective

**Ronald Tobias’s *20 Master Plots* (1993)** occupies middle ground between Polti’s granularity and Booker’s abstraction, offering a practical writer’s manual:

Quest, Adventure, Pursuit, Rescue, Escape, Revenge, The Riddle, Rivalry, Underdog, Temptation, Metamorphosis, Transformation, Maturation, Love, Forbidden Love, Sacrifice, Discovery, Wretched Excess, Ascension, and Descension. 

Tobias built on Aristotle’s three-part structure, providing checklists for each plot’s beginning, middle, and end.  Unlike Booker’s Jungian framing, Tobias’s approach is pragmatic—he acknowledges stories often combine multiple plots and that these aren’t exhaustive but rather useful templates.

-----

## Computational research validates Vonnegut’s story shapes

The most rigorous empirical test came from **Andrew Reagan and colleagues at the University of Vermont’s Computational Story Lab**, published in *EPJ Data Science* (2016) as “The emotional arcs of stories are dominated by six basic shapes.”  

The study analyzed **1,327 stories** from Project Gutenberg using **sentiment analysis** with the Hedonometer (labMT dataset) and **10,000-word sliding windows**.  Three independent analytical methods—**singular value decomposition**, **hierarchical clustering**, and **self-organizing maps**—converged on **six core emotional arcs**:

1. **Rags to riches** (rise) 
1. **Tragedy/Riches to rags** (fall) 
1. **Man in a hole** (fall-rise) 
1. **Icarus** (rise-fall) 
1. **Cinderella** (rise-fall-rise) 
1. **Oedipus** (fall-rise-fall) 

The first six SVD modes explained **80% of variance** from mean-centered time series. The researchers noted this validates **Kurt Vonnegut’s rejected 1947 master’s thesis**, which proposed graphing stories on axes of good fortune/ill fortune versus beginning/end. Vonnegut called this “his greatest contribution” and asserted: “There is no reason why the simple shapes of stories can’t be fed into computers, they are beautiful shapes.” 

However, critical limitations must be noted. Literary scholar **Katherine Elkins** (Cambridge, 2022) observed: “With enough smoothing, virtually any story can be made to fit a small number of shapes.”  More fundamentally, **emotional arcs are not plots**: “The emotional arc of a story does not give us direct information about the plot or the intended meaning of the story.” Sentiment trajectory captures audience emotional experience, not narrative structure.

-----

## Academic critics challenge the foundations of enumeration

### The Campbell critique

Folklorist **Barre Toelken** noted that “Jung-influenced psychologists and authors have tended to build complex theories around single versions of a tale that supports a theory.”  Scholar **C.P. Nield** (2022) described Campbell’s framework as a “Hollywood McMyth” that “rather than promoting cross-cultural plurality, has become a monocultural construct.” 

The core methodological problems are **vagueness** (stages defined so loosely anything can fit), **source-selection bias** (Campbell chose supporting examples while ignoring counterexamples), and **unfalsifiability** (stories can “skip, condense, or reorder” stages, making disconfirmation impossible). As one critic put it: “The ‘hero’s journey’ is essentially just a list of tropes that sometimes appear in some stories from some cultures.” 

### The Booker critique

Novelist **Adam Mars-Jones** observed that Booker “sets up criteria for art, and ends up condemning Rigoletto, The Cherry Orchard, Wagner, Proust, Joyce, Kafka and Lawrence—the list goes on—while praising Crocodile Dundee, E.T. and Terminator 2.”  Critic **Roz Kaveney** noted Booker’s “cultural blindness”—“almost every text or film Booker cites is European or North American”—and pointed to Lady Murasaki’s *Tale of Genji*, which has a “remarkably tenuous” relationship with any of the seven plots: “But of course Lady Murasaki was a woman, and not a European.” 

### The Jungian problem

The Jungian foundation underlying both Campbell and Booker has been challenged on empirical grounds. Psychologist **Andrew Neher** (1996) argued that Jung’s collective unconscious and archetypes “have been difficult to empirically verify” and are “seriously flawed.” Literary critic **Terence Dawson** noted “endless reiteration about the collective unconscious or the shadow… Jungian criticism has become reductive and distressingly predictable.”

Notably, **Northrop Frye**—whose *Anatomy of Criticism* (1957) established archetypal criticism with his four *mythoi* (Comedy, Romance, Tragedy, Satire/Irony mapped to seasons)—explicitly distanced himself from Jung, arguing literary critics “should be concerned only with the ritual or dream patterns and need not concern themselves with how the symbols actually got there.”

-----

## The fabula/syuzhet distinction undermines simple enumeration

The Russian Formalists (**Viktor Shklovsky**, **Vladimir Propp**) distinguished **fabula** (the chronological sequence of events) from **syuzhet** (the artistic arrangement and presentation of those events). This distinction, later refined by **Tzvetan Todorov** (histoire vs. discours) and **Gérard Genette** (histoire vs. récit), reveals a fundamental problem: different taxonomies operate at different levels.

Propp analyzes fabula-level functions; Booker analyzes syuzhet-level macro-patterns; Campbell conflates both; Reagan’s emotional arcs capture reader experience, not either. The question “how many basic plots exist?” cannot be answered without specifying **which level of narrative analysis** one means. As critics note, for most fabula there are “many possible syuzhets—many different ways to tell the story.” 

-----

## Non-Western narratives challenge universality claims

The taxonomies surveyed derive almost exclusively from Western, particularly European, sources. **Indigenous narrative structures** present fundamental challenges.

**American Indian storytelling**, according to the School Library Journal, “didn’t necessarily have a beginning or an ending. We didn’t use the Western narrative or develop the Western mindset for telling and enjoying stories—a process first developed by Aristotle in which all plots have a beginning, middle, and end.” **Métis stories** “have non-linear narratives and, unlike European stories, many of them have no real beginning, middle or end.”

**Kishotenketsu**, the four-act structure common in Korean, Chinese, and Japanese narrative, emphasizes **contrast without conflict**—directly contradicting the Western assumption that drama requires conflict.  Story consultant **Steve Seager** observed: “Indian narrative forms are radically different from Western forms. Watch a Bollywood movie.” 

Christopher Vogler himself acknowledged that Australians “pointed out to me hidden cultural assumptions in my understanding of the Hero’s Journey”—yet still claimed universality.

### Feminist and postcolonial critiques

When **Maureen Murdock** asked Campbell about women’s role in the monomyth, he reportedly replied: “Women don’t need to make the journey… In the whole mythological tradition, the woman is there. All she has to do is realize that she’s the place that people are trying to get to.”  Feminist scholars like **Mary Sharratt** noted that Campbell “drew his monomyth primarily from classical Greek mythology, which evolved in one of the most misogynist eras of history.” 

Campbell’s model also assumes heteronormativity—“male heroes are always sexually attracted to women and female heroes are always attracted to men”—making “sexual union with the opposite sex an important part of his outline.”

-----

## Propp enables generation; Booker enables classification

In computational applications, **Propp’s morphology** proves most tractable due to its discrete, enumerable functions and sequential grammar.  Systems like **PropperWryter** (Gervás, 2013), **TALE-SPIN** (Meehan, 1977), **MINSTREL** (Turner, 1993), and **MEXICA** (Pérez y Pérez, 1999) all drew on Proppian structures.

Campbell’s higher abstraction makes it useful for guidance but harder to implement procedurally. Booker’s seven plots function best for **classification and tagging** rather than generation.

|Framework|Granularity        |Generation Utility|Analysis Utility|
|---------|-------------------|------------------|----------------|
|Propp    |Fine (31 functions)|Excellent         |Good            |
|Campbell |Medium (17 stages) |Moderate          |Good            |
|Tobias   |Medium (20 plots)  |Good              |Good            |
|Booker   |Coarse (7 plots)   |Poor              |Good            |

Modern **large language model** approaches combine symbolic planning with neural generation. **Dramatron** (DeepMind, 2022) uses hierarchical generation (logline → title → characters → outline → script). Hybrid systems using **Answer Set Programming** to guide LLMs produce more diverse stories than unguided generation. However, LLM-generated narratives show persistent bias toward “tightly-knit positive relationships” and “less conflict-driven social dynamics.”

The proprietary **Dramatica** system (Phillips \u0026 Huntley, 1993) offers perhaps the most sophisticated formal implementation, modeling story as “a model of a single human mind trying to resolve a problem” with **32,000+ unique storyforms** possible within its constraint system.

-----

## Conclusion: useful heuristics, not universal laws

The evidence suggests a nuanced verdict. **Emotional trajectories** do cluster into a small number of shapes—roughly six—as demonstrated by computational analysis of large corpora.  This validates Vonnegut’s intuition about “beautiful shapes” that can be graphed and computed.

However, emotional arcs are not plots, plots are not stories, and stories are not meaning. The theoretical taxonomies—from Aristotle through Polti, Propp, Campbell, Booker, and Tobias—each capture genuine patterns while operating at incompatible levels of abstraction and embedding unexamined cultural assumptions. The question “how many basic plots exist?” has no single answer because it depends on:

- **Level of abstraction**: At extreme abstraction, perhaps one plot (desire → fulfillment); at ground level, infinite unique stories
- **Aspect analyzed**: Fabula events, syuzhet arrangement, emotional trajectory, or thematic meaning
- **Cultural frame**: Western Aristotelian assumptions versus circular, non-linear, non-conflict-driven Indigenous and Eastern forms

For **practical purposes**, these frameworks offer genuine utility. Screenwriters use Save the Cat beat sheets; game designers implement Proppian quest structures; story analysts apply Booker’s categories. The taxonomies work as **heuristics**—useful simplifications enabling creative work and analysis—not as **universal laws** of narrative structure.

The deeper insight may be Katherine Elkins’s observation that “emotional structure may be more fundamental than plot structure and can exist independently of the latter. A powerful narrative can retain its power through an emotional arc even when plot is minimal.”  What feels universal may be the rhythm of tension and release, hope and despair—not the specific dramatis personae or sequence of situations, but the emotional music that stories play upon human consciousness.