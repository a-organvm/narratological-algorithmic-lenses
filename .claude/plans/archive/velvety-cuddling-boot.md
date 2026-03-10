# Phase 4: From Library to Instrument

## Context

Phase 3 is complete. The repo contains 40 files — a mature theory corpus, 19 research reports (~10K lines, ~1.5MB), and complete creative scaffolding — but **zero creative output, zero code, and zero cross-cutting synthesis**. The 19 research reports are siloed: each is useful individually but there's no way to look up "which mechanisms activate at Rimbaud 70 / Wilde 20 / Burroughs 10" without reading through multiple reports manually. The encoding schema exists as theory; it needs to become an instrument.

Phase 4 transforms the project from a static markdown library into an operational creative toolkit. Three moves:
1. **Synthesize** the research into cross-cutting instruments a writer can reach for mid-draft
2. **Extend** the author corpus to fill the representational gaps the comparative report flags (no women except Bishop, no intersectional lens, no punk-feminist)
3. **Build tools** — actual Python code that scaffolds fragments, validates schemas, and looks up mechanisms

### What's NOT in Phase 4
- Creative fragments (human writes these — AI builds the tools)
- Neon DB bridge (Phase 5, when fragments exist to sync)
- Platform presence / publication (Phase 5+)
- CHTHON-ONEIROS companion sync (Phase 5+)
- Remaining 4 second-wave authors: Barnes, Woolf, Mishima, Arenas (Phase 5)

---

## Workstreams

| # | Workstream | Deliverables | Method |
|---|-----------|-------------|--------|
| A | Research Synthesis | 4 cross-cutting instruments | 3 parallel agents (Batch 1-2) |
| B | Second-Wave Author Research | 2 reports (Acker, Lorde) | 1 agent per batch |
| C | Encoding Engine | 3 Python CLI tools + docs | Direct file creation |
| D | Targeted World Research | 3 briefs (Language Codes, Music, Eco-Queer) | 3 parallel agents |
| E | Infrastructure Sync | CATALOG v3.0, seed.yaml, KG, Neon | Direct + MCP tools |

---

## Step 1: Research Synthesis + Priority Authors (Batch 1)

Three parallel agents. Each reads ALL 9 author reports + comparative report and produces a synthesis document.

### 1a. Master Mechanism Atlas
**Output**: `research/synthesis/MECHANISM-ATLAS.md`

Extract every mechanism from all 9 author reports (sections D: Mechanics Atlas), deduplicate overlapping names (e.g., "Negative Space as Primary Content" in Bishop vs "Negative Space as Content" in the core schema), cross-reference by author. Expected: ~60-80 unique mechanisms after dedup from ~120+ scattered instances.

Structure:
- **Part I**: Alphabetical mechanism inventory. Per entry: name, definition, which authors use it (with specific examples from their reports), which dial settings activate it, writer-facing craft rule (imperative: "Do X when Y")
- **Part II**: Mechanism-to-dial matrix. Rows = mechanisms. Columns = Rimbaud Drift / Wilde Mask / Burroughs Control. Cells = activation level (primary / moderate / rare). Source: the cross-reference table already in ENCODING-WORKSHEET.md lines 209-219, expanded with all mechanisms
- **Part III**: Mechanism-by-cluster distribution. Which clusters favor which mechanisms

**Source files**: `research/rimbaud-deep-research.md`, `research/wilde-deep-research.md`, `research/burroughs-deep-research.md`, `research/forster-deep-research.md`, `research/cavafy-deep-research.md`, `research/baldwin-deep-research.md`, `research/genet-deep-research.md`, `research/delany-deep-research.md`, `research/bishop-deep-research.md`, `research/comparative-report.md`

### 1b. Universal Claims Ledger
**Output**: `research/synthesis/CLAIMS-LEDGER.md`

Consolidate ALL claims from all 9 author reports + comparative report (each has a Claims Ledger section, typically 15-25 entries per report, 20 in the comparative). Merge, deduplicate, tag each:
- **unique**: only one author report makes this claim
- **corroborated**: 2+ reports provide independent evidence
- **contested**: reports provide conflicting evidence

Expected: ~150-200 entries after dedup.

Structure:
- Claims table with columns: #, Claim, Source Author(s), Cross-Validation Status, Confidence (0-100), Craft Implication
- Summary section: key themes, strongest claims (confidence 90+), weakest claims, contradictions

### 1c. Kathy Acker Deep Research
**Output**: `research/acker-deep-research.md`

Standard template (sections A-I matching anchor reports). Cluster C (Burroughs-adjacent) with feminist inflection. Focus:
- Literary piracy as encoding: appropriating/rewriting canonical texts makes authorial confession structurally impossible
- Identity fragmentation as $PLAUSIBLE_DENIABILITY: "I can't get sexual genders straight" as formal principle
- Cut-up extended through feminist/queer lens: Burroughsian discontinuity + refusal of patriarchal coherent subjectivity
- Key question: does "refusing coherent subjecthood" function as $PLAUSIBLE_DENIABILITY?

Entry texts: *Blood and Guts in High School* (1984), *Great Expectations* (1982), *Empire of the Senseless* (1988), *Don Quixote* (1986). Comparative report profile at lines 420-425.

---

## Step 2: Research Synthesis continued + Lorde (Batch 2)

Three parallel agents. A3 and A4 depend on A1 (Mechanism Atlas) completing in Batch 1.

### 2a. Dial Calibration Matrix
**Output**: `research/synthesis/DIAL-CALIBRATION.md`

For each of the 6 preset configurations from `drafts/ENCODING-WORKSHEET.md` (lines 157-196):
1. **Confessional Whisper** (R70/W20/B10)
2. **Defensive Wit** (R10/W80/B30)
3. **Systems Dread** (R20/W15/B85)
4. **Bright Surface, Dark Water** (R40/W60/B20)
5. **Surveillance Fugue** (R50/W10/B60)
6. **Archive Grief** (R60/W30/B30)

Per preset:
- Dial values (already defined)
- Primary mechanisms activated (from Mechanism Atlas Part II, with author attribution)
- 2-3 example passages from the research demonstrating the texture at these settings
- Recommended mask types and signal types
- What to avoid (mechanism conflicts at these settings)
- Sample encoding schema walkthrough: fill in all 7 variables for a hypothetical fragment

### 2b. Author Encoding Crosswalk
**Output**: `research/synthesis/AUTHOR-CROSSWALK.md`

A 9-author (expandable to 15) comparison grid:
- Rows = 7 encoding variables ($SURFACE_STORY through $AFFECT_COST)
- Columns = 9 authors (Rimbaud, Wilde, Burroughs, Forster, Cavafy, Baldwin, Genet, Delany, Bishop)
- Per cell: specific technique description (2-3 sentences) + key example text
- 3 empty columns labeled "Wave 2" for Acker, Lorde, + future authors

Enables lookups like: "How does Bishop handle $PLAUSIBLE_DENIABILITY vs Genet?"

Source: Section C (Encoding Schema) from each author's deep research report.

### 2c. Audre Lorde Deep Research
**Output**: `research/lorde-deep-research.md`

Standard template (sections A-I). Cluster E (Schema Expansion) — the most important gap in the current corpus.

Focus:
- Biomythography (*Zami*) as dual-channel form: surface = memoir, substrate = mythological transformation
- Intersectional identity as mutual camouflage: multiple identities provide strategic cover for each other
- The erotic as power (from "Uses of the Erotic" essay): what happens when the writer *refuses* concealment?
- Key question for the schema: does the 7-variable encoding model still describe the formal operations when the writer operates under visibility politics rather than closet politics?

Entry texts: *Zami: A New Spelling of My Name* (1982), *Sister Outsider* (essays, 1984), *The Black Unicorn* (poetry, 1978). Comparative report profile at lines 481-486.

If Lorde's refusal of concealment breaks the schema, that break is the most important finding of Phase 4 — the report should characterize it explicitly.

---

## Step 3: World Research + Encoding Engine (Batch 3)

Three parallel agents for world research. Encoding engine built directly (no agents needed).

### 3a. World Research: Language Codes (Topic 11)
**Output**: `research/world-11-language-codes.md`

Standard world research structure (sections A-G from QV33R World Research Operator):
- Polari in the UK (1930s-1970s), ballroom slang (shade, reading, vogue, legendary), hanky codes, Swardspeak (Philippines), online queer coded language
- World A (Reality): material conditions of police surveillance that made coded language necessary
- World B (Artifice): semiotic architecture of the codes themselves
- Direct connection to the project's core double-channel model: these codes operate on the same principle as the literary texts — a surface meaning for outsiders, a substrate meaning for the initiated

### 3b. World Research: Music and Sonic Environments (Topic 12)
**Output**: `research/world-12-music-sonic.md`

- Disco (1970s, Fire Island, Studio 54), house (Chicago 1980s, Frankie Knuckles), ballroom/vogue (NYC 1980s-90s), Hi-NRG, queer punk, contemporary PC Music/hyperpop
- The concealment/revelation dynamic in each genre: how disco's hedonism was simultaneously visibility and deniability ("just dancing")
- Double-channel in lyrics: surface pop, substrate desire

### 3c. World Research: Eco-Queer Futures (Topic 23)
**Output**: `research/world-23-eco-queer.md`

- Eco-queer theory (Nicole Seymour's *Strange Natures*, queer ecology)
- Queer kinship structures as analogs for non-human relations
- Climate grief as queer-coded affect
- At least 3 case studies

### 3d. Encoding Engine (direct, no agents)

Create `tools/` directory with three Python CLI scripts. All use only stdlib + PyYAML (confirmed available: v6.0.3 via Anaconda).

**`tools/scaffold.py`** (~120-150 lines)
```
Usage: python tools/scaffold.py --slug "city-after-rain" [--preset confessional-whisper]
```
- Reads `drafts/TEMPLATE.md` as source template
- If `--preset` provided: pre-fills dial values from the 6 presets (hardcoded from ENCODING-WORKSHEET.md)
- If no preset: interactive prompts for each dial (0-100) and schema fields
- Writes to `drafts/YYYY-MM-DD-{slug}.md`
- `--help` flag prints usage

**`tools/validate.py`** (~100-120 lines)
```
Usage: python tools/validate.py drafts/2026-02-17-city-after-rain.md
```
- Parses YAML frontmatter
- Checks: all required fields present, dials 0-100, mask_type and signal_type are recognized values, fragment section non-empty, plausible_deniability 1-5
- Outputs: checklist with pass/fail per item + summary
- `--help` flag

**`tools/lookup.py`** (~100-120 lines)
```
Usage: python tools/lookup.py --dials rimbaud=70,wilde=20,burroughs=10
   or: python tools/lookup.py --mechanism "negative_space"
   or: python tools/lookup.py --author bishop
```
- Reads `research/synthesis/MECHANISM-ATLAS.md` (flat-file parse)
- For dial query: returns mechanisms that activate at those settings
- For mechanism query: returns full Atlas entry
- For author query: returns all mechanisms attributed to that author
- `--help` flag

**`tools/README.md`** — documents all three tools with usage examples

**`tools/requirements.txt`** — `PyYAML>=6.0`

---

## Step 4: Synthesis Wave 2 Integration

After Acker and Lorde reports are complete (from Steps 1-2), update the synthesis documents:

### 4a. Update Author Crosswalk
Add Acker and Lorde columns to the crosswalk grid (filling the first 2 of 3 "Wave 2" columns).

### 4b. Update Mechanism Atlas
Add any new mechanisms discovered in Acker and Lorde reports to the Atlas (particularly: literary piracy as encoding, identity fragmentation as deniability, biomythography as dual-channel, intersectional mutual camouflage).

### 4c. Update Claims Ledger
Add claims from Acker and Lorde reports. Particularly important: any claims that **contradict** or **qualify** existing claims (e.g., Lorde may challenge Claim #1's universality claim about concealment-as-composition).

---

## Step 5: Infrastructure Sync

### 5a. CATALOG.md v3.0
Update to reflect:
- New `research/synthesis/` subdirectory (4 documents)
- 2 new author reports (Acker, Lorde)
- 3 new world research briefs (Topics 11, 12, 23)
- `tools/` directory (3 Python scripts + README + requirements.txt)
- Updated corpus statistics (estimated: ~50 files total)
- New section: "Synthesis Documents"
- New section: "Tools"

### 5b. seed.yaml update
Add new agent definitions reflecting new capabilities:
- `synthesis-updater`: watches `research/*.md`, flags when synthesis documents may need updating
- `fragment-validator`: wraps `tools/validate.py`
- `encoding-engine`: documents the three tools

### 5c. Knowledge Graph sync
Add entities: 4 synthesis documents, 2 new authors (Acker, Lorde), new mechanisms from synthesis

### 5d. Neon DB sync
Insert rows for all new documents

### 5e. Commit and push

---

## Execution Order & Agent Batching (max 3 concurrent)

```
Batch 1: [3 agents in parallel]
├── Agent 1: Mechanism Atlas (A1) ──────→ research/synthesis/MECHANISM-ATLAS.md
├── Agent 2: Claims Ledger (A2) ────────→ research/synthesis/CLAIMS-LEDGER.md
└── Agent 3: Acker deep research (B1) ──→ research/acker-deep-research.md

Batch 2: [3 agents in parallel] (A3, A4 depend on A1)
├── Agent 1: Dial Calibration (A3) ─────→ research/synthesis/DIAL-CALIBRATION.md
├── Agent 2: Author Crosswalk (A4) ─────→ research/synthesis/AUTHOR-CROSSWALK.md
└── Agent 3: Lorde deep research (B2) ──→ research/lorde-deep-research.md

Batch 3: [3 agents + direct work in parallel]
├── Agent 1: World-11 Language Codes ───→ research/world-11-language-codes.md
├── Agent 2: World-12 Music/Sonic ──────→ research/world-12-music-sonic.md
├── Agent 3: World-23 Eco-Queer ────────→ research/world-23-eco-queer.md
└── Direct:  Encoding Engine (C) ───────→ tools/{scaffold,validate,lookup}.py

Step 4: Synthesis Wave 2 Integration [direct edits]
├── Update MECHANISM-ATLAS.md with Acker/Lorde mechanisms
├── Update AUTHOR-CROSSWALK.md with Acker/Lorde columns
└── Update CLAIMS-LEDGER.md with Acker/Lorde claims

Step 5: Infrastructure Sync [direct + MCP]
├── CATALOG.md v3.0
├── seed.yaml update
├── KG sync
├── Neon DB sync
└── Commit and push
```

---

## Files to Create

| File | Step | Lines (est.) |
|------|------|-------------|
| `research/synthesis/MECHANISM-ATLAS.md` | 1a | 350-450 |
| `research/synthesis/CLAIMS-LEDGER.md` | 1b | 400-500 |
| `research/acker-deep-research.md` | 1c | ~500 |
| `research/synthesis/DIAL-CALIBRATION.md` | 2a | 250-300 |
| `research/synthesis/AUTHOR-CROSSWALK.md` | 2b | 250-300 |
| `research/lorde-deep-research.md` | 2c | ~500 |
| `research/world-11-language-codes.md` | 3a | 400-450 |
| `research/world-12-music-sonic.md` | 3b | 400-450 |
| `research/world-23-eco-queer.md` | 3c | 350-400 |
| `tools/scaffold.py` | 3d | 120-150 |
| `tools/validate.py` | 3d | 100-120 |
| `tools/lookup.py` | 3d | 100-120 |
| `tools/README.md` | 3d | 60-80 |
| `tools/requirements.txt` | 3d | 1-3 |

**Total: 14 new files + 2 new directories**

## Files to Modify

| File | Step |
|------|------|
| `research/synthesis/MECHANISM-ATLAS.md` | 4b |
| `research/synthesis/AUTHOR-CROSSWALK.md` | 4a |
| `research/synthesis/CLAIMS-LEDGER.md` | 4c |
| `CATALOG.md` | 5a |
| `seed.yaml` | 5b |

---

## Verification

### Synthesis
- [ ] MECHANISM-ATLAS.md has entries sourced from all 9 authors (verify: grep for each author name)
- [ ] No mechanism listed twice under different names without cross-reference
- [ ] Every mechanism has a craft rule in imperative voice
- [ ] CLAIMS-LEDGER.md has 150+ entries
- [ ] Every claim tagged: unique / corroborated / contested
- [ ] DIAL-CALIBRATION.md has complete sections for all 6 presets
- [ ] AUTHOR-CROSSWALK.md: 9 columns x 7 rows, no empty cells

### Author Research
- [ ] acker-deep-research.md follows template (sections A-I), 12+ mechanisms, 15+ claims
- [ ] lorde-deep-research.md addresses visibility/concealment dialectic explicitly
- [ ] lorde-deep-research.md covers *Zami*, *The Black Unicorn*, *Sister Outsider*

### World Research
- [ ] world-11-language-codes.md has World A / World B decomposition
- [ ] world-12-music-sonic.md covers: disco, house, ballroom/vogue, + 1 contemporary genre
- [ ] world-23-eco-queer.md has 3+ case studies

### Encoding Engine
- [ ] `python tools/scaffold.py --slug test --preset confessional-whisper` runs without error
- [ ] Output file has valid YAML frontmatter (parseable by PyYAML)
- [ ] Output file has all sections from TEMPLATE.md
- [ ] `python tools/validate.py` correctly rejects: missing field, dial > 100, empty fragment
- [ ] `python tools/lookup.py --dials rimbaud=70,wilde=20,burroughs=10` returns 3+ mechanisms
- [ ] All 3 tools respond to `--help`

### Infrastructure
- [ ] CATALOG.md v3.0 has Synthesis Documents and Tools sections
- [ ] seed.yaml parses as valid YAML
- [ ] All new files committed and pushed
