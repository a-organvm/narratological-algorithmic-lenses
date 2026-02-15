# Narratological Algorithmic Lenses

A computational engine for formalizing, analyzing, and applying narrative craft. 

This system transforms abstract storytelling principles—from **Aristotle's** *Poetics* to **Phoebe Waller-Bridge's** *Fleabag*—into executable algorithms that can diagnose scripts, identify structural weaknesses, and simulate "Script Doctor" consultations.

## Core Capabilities

### 1. The Compendium
A living library of 27+ formalized narrative frameworks, including:
- **Classical**: Aristotle, Bharata Muni (Natyasastra), Ovid, Plato, Horace, African Oral Epic.
- **Film**: Tarkovsky (Time-Pressure), Bergman (Interiority), Tarantino (Discovery Writing), Lynch (Dream Logic), Kubrick (Non-Submersible Units).
- **Television**: Phoebe Waller-Bridge (Layered Obstacles), Larry David (Comedy Geometry), South Park (Therefore/But).
- **Global**: Kishōtenketsu (Conflict-Agnostic), Heroine's Journey (Internal Integration).
- **Interactive**: Zelda (Exploration), Final Fantasy (Ensemble).
- **Comics**: Alan Moore (Formalism), Grant Morrison (Hypersigil), Kirby (Mythopoeia).
- **Meta**: 8-Role Analyst System, Attention Mechanics.

### 2. Deep Diagnostics
Quantitative and qualitative analysis of script structure:
- **Causal Binding**: Measures the ratio of "THEREFORE/BUT" connections vs. "AND THEN" (Target > 60%).
- **Reorderability**: Identifies scenes that can be moved without breaking causality (lower is better).
- **Necessity**: Flags scenes that serve no structural or character function.
- **Information Economy**: Detects redundant exposition and missing setups.

### 3. The Script Doctor
Collaborative AI analysis that simulates a writers' room with master creators:
- **Pairings**: Ask **Tarkovsky** and **Bergman** to debate your script's pacing.
- **Consultations**: Get a "prescription" for your second act from **Phoebe Waller-Bridge**.
- **Dialogue**: Receive feedback formatted as a philosophical debate between conflicting narrative schools.

### 4. Fountain Integration
Native support for the **Fountain** screenplay format, allowing direct ingestion of professional scripts from Highland 2, Fade In, or VS Code.

---

## Repository Layout

```text
narratological-algorithmic-lenses/
├── specs/                    # The Knowledge Base
│   ├── 02-completed-studies/ # Markdown source of truth for all algorithms
│   ├── 03-structured-data/   # Validated JSON extracts (Compendium)
│   └── 06-open-view-drafts/  # Case study screenplays
├── packages/                 # The Software Stack
│   ├── core/                 # Python library (models, parsers, diagnostics, LLM)
│   ├── cli/                  # Command-line interface (Typer)
│   ├── api/                  # FastAPI service
│   └── web/                  # React + Vite visualization dashboard
└── docs/                     # Documentation & Roadmaps
```

## Getting Started

### Prerequisites
- Python 3.11+
- `uv` (Universal Python Package Installer)
- `npm` (for web dashboard)

### Installation

```bash
# Initialize Python workspace
uv sync

# Initialize Web workspace
npm install
```

### Key Commands

**1. Analyze a Script**
Run deep diagnostics on a Fountain or text script:
```bash
# Full battery (Causal, Reorderability, Necessity)
uv run narratological diagnose all my_script.fountain

# Targeted Causal Binding check
uv run narratological diagnose causal my_script.fountain --target 0.8
```

**2. Consult the Script Doctor**
Simulate a creative consultation between two masters:
```bash
# Consult Tarkovsky and Bergman (Sequence B)
uv run narratological analyze script-doctor my_script.fountain --sequence B

# Custom pairing: Larry David vs. Aristotle
uv run narratological analyze script-doctor my_script.fountain --primary larry-david --secondary aristotle
```

**3. Explore the Compendium**
```bash
# List all available studies
uv run narratological info

# Validate data integrity
uv run narratological validate compendium
```

## Development

### Data Synchronization
The system maintains strict synchronization between Markdown research files and JSON computational models.
If you edit a study in `specs/02-completed-studies/`, run:
```bash
uv run narratological validate sync
```

### Testing
```bash
uv run pytest                  # Run all Python tests
uv run ruff check .            # Linting
npm run web:test               # Run frontend tests
```

---

*There and Back Again.*
