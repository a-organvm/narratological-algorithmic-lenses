# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Narratological Algorithmic Lenses is a **comprehensive software system** that transforms theoretical narrative craft methodologies into implementable tools. The system provides:

- **Narrative Analysis Tool** - Analyze scripts/stories using formalized algorithms
- **AI/LLM Integration Library** - Enable AI systems to apply narratological frameworks
- **Interactive Reference App** - Browse, search, and apply specifications
- **Code Generation Framework** - Generate narrative structures algorithmically

## Architecture

**Hybrid: Python core + TypeScript web app**

```
narratological-algorithmic-lenses/
├── specs/                    # Theoretical specifications (14 studies, templates, sources)
│   ├── 01-primary-sources/
│   ├── 02-completed-studies/
│   ├── 03-structured-data/   # JSON exports + unified compendium
│   ├── 04-templates/
│   ├── 05-secondary-sources/
│   └── 07-skill-documentation/
│
├── packages/
│   ├── core/                 # Python core library (Pydantic models, algorithms)
│   ├── cli/                  # Python CLI application (typer)
│   ├── api/                  # FastAPI backend
│   └── web/                  # TypeScript/React web app (Vite)
│
├── pyproject.toml            # Python workspace root (uv)
└── package.json              # Node.js workspace root
```

## Build Commands

### Python Packages (using uv)

```bash
# Install all Python dependencies
uv sync

# Install specific package in development mode
uv pip install -e packages/core
uv pip install -e packages/cli
uv pip install -e packages/api

# Run CLI
uv run narratological --help

# Run API server
uv run uvicorn narratological_api.main:app --reload
```

### TypeScript Web App

```bash
# Install dependencies
cd packages/web && npm install

# Development server
npm run dev

# Build for production
npm run build

# Type checking
npm run typecheck
```

## Test Commands

### Python Tests (pytest)

```bash
# Run all Python tests
uv run pytest

# Run specific package tests
uv run pytest packages/core/tests/
uv run pytest packages/cli/tests/
uv run pytest packages/api/tests/

# Run with coverage
uv run pytest --cov=narratological --cov-report=html

# Run specific test file
uv run pytest packages/core/tests/test_models.py -v
```

### TypeScript Tests (vitest)

```bash
cd packages/web

# Run tests
npm test

# Run with coverage
npm run test:coverage

# Watch mode
npm run test:watch
```

## Key Files

### Specifications
- **`specs/03-structured-data/narratological-algorithms-unified.json`** - All 14 studies in machine-readable format (~209 KB)
- **`specs/03-structured-data/CROSS-REFERENCE-TABLE.md`** - Study inventory with axiom counts
- **`specs/07-skill-documentation/SKILL.md`** - Complete 8-role analyst methodology

### Core Library
- **`packages/core/src/narratological/models/`** - Pydantic data models
- **`packages/core/src/narratological/algorithms/`** - Algorithm implementations
- **`packages/core/src/narratological/diagnostics/`** - Diagnostic test runners
- **`packages/core/src/narratological/generators/`** - Report generators

## Data Model

**14 studies** containing:
- ~79 axioms (foundational principles)
- ~92 algorithms (formalized processes with pseudo-code)
- Structural hierarchies (nested organizational levels)
- Diagnostic questions (self-assessment prompts)
- Theoretical correspondences (mappings to Aristotle, McKee, Campbell, etc.)

**7 sequence pairs** linking related studies:
- A: Ovid ↔ Gaiman (anthology, myth-remix)
- B: Tarkovsky ↔ Bergman (cinematic interiority)
- C: Moore ↔ Morrison (formalism vs hypersigil)
- D: Kirby ↔ Tolkien (mythopoeia, cosmic dualism)
- E: Zelda ↔ Final Fantasy (interactive narrative)
- F: Tarantino ↔ Ovid (non-linear structure)
- G: Pixar ↔ Final Fantasy (emotional engineering)

## Development Workflow

### Working with Core Library

1. Models are defined in `packages/core/src/narratological/models/`
2. Algorithms implement the pseudo-code from studies
3. Tests validate against the unified JSON data

### Adding New Algorithms

1. Reference the algorithm spec in `specs/02-completed-studies/`
2. Implement in `packages/core/src/narratological/algorithms/`
3. Add tests that validate inputs/outputs match spec

### Working with Web App

1. API endpoints defined in `packages/api/src/narratological_api/routes/`
2. React components consume API in `packages/web/src/`
3. Shared types can be generated from Pydantic models

## Study JSON Schema

Studies in `specs/03-structured-data/json-extracts/` use this schema:

```json
{
  "id": "creator-work",
  "creator": "Name",
  "work": "Work Title",
  "category": "Category",
  "axioms": [
    {
      "id": "XX-A0",
      "name": "Axiom Name",
      "statement": "The principle statement",
      "derivations": ["Implication 1", "Implication 2"]
    }
  ],
  "structural_hierarchy": {
    "levels": [
      {
        "level": 1,
        "name": "Level Name",
        "description": "Level description",
        "elements": ["Element 1", "Element 2"]
      }
    ]
  },
  "core_algorithms": [
    {
      "name": "Algorithm Name",
      "purpose": "What it does",
      "pseudocode": "The implementation logic",
      "inputs": ["input1", "input2"],
      "outputs": ["output1", "output2"]
    }
  ],
  "diagnostic_questions": [
    {
      "id": "Q1",
      "question": "The diagnostic question",
      "valid_if": "Criteria for validity"
    }
  ],
  "theoretical_correspondences": {
    "maps_to": ["Theory 1", "Theory 2"],
    "sequence_pairs": ["paired-study-id"]
  },
  "quick_reference": {
    "core_operations": ["Operation 1", "Operation 2"],
    "key_constraints": ["Constraint 1", "Constraint 2"]
  }
}
```

## 8-Role Analyst System

Script analysis uses eight distinct analytical perspectives:

| Role | Focus |
|------|-------|
| AESTHETE | Form, beauty, style, sensory patterns |
| DRAMATURGIST | Structure, rhythm, dramatic tension |
| NARRATOLOGIST | Narrative mechanisms, causal binding |
| ART HISTORIAN | Historical context, influences, lineages |
| CINEPHILE | Comparable works, genre conventions |
| RHETORICIAN | Argument structure, dialogue craft |
| PRODUCER | Practical feasibility, budget implications |
| ACADEMIC | Theoretical frameworks, rigor |
| FIRST-READER | Emotional response, engagement |

See `specs/07-skill-documentation/SKILL.md` for complete methodology.

<!-- ORGANVM:AUTO:START -->
## System Context (auto-generated — do not edit)

**Organ:** ORGAN-I (Theory) | **Tier:** standard | **Status:** GRADUATED
**Org:** `organvm-i-theoria` | **Repo:** `narratological-algorithmic-lenses`

### Edges
- **Produces** → `organvm-ii-poiesis/art-from--narratological-algorithmic-lenses`: dependency

### Siblings in Theory
`recursive-engine--generative-entity`, `organon-noumenon--ontogenetic-morphe`, `auto-revision-epistemic-engine`, `call-function--ontological`, `sema-metra--alchemica-mundi`, `cognitive-archaelogy-tribunal`, `a-recursive-root`, `radix-recursiva-solve-coagula-redi`, `.github`, `nexus--babel-alexandria`, `4-ivi374-F0Rivi4`, `cog-init-1-0-`, `linguistic-atomization-framework`, `my-knowledge-base`, `scalable-lore-expert` ... and 5 more

### Governance
- Foundational theory layer. No upstream dependencies.

*Last synced: 2026-03-21T13:20:55Z*

## Session Review Protocol

At the end of each session that produces or modifies files:
1. Run `organvm session review --latest` to get a session summary
2. Check for unimplemented plans: `organvm session plans --project .`
3. Export significant sessions: `organvm session export <id> --slug <slug>`
4. Run `organvm prompts distill --dry-run` to detect uncovered operational patterns

Transcripts are on-demand (never committed):
- `organvm session transcript <id>` — conversation summary
- `organvm session transcript <id> --unabridged` — full audit trail
- `organvm session prompts <id>` — human prompts only


## Active Directives

| Scope | Phase | Name | Description |
|-------|-------|------|-------------|
| system | any | prompting-standards | Prompting Standards |
| system | any | research-standards-bibliography | APPENDIX: Research Standards Bibliography |
| system | any | phase-closing-and-forward-plan | METADOC: Phase-Closing Commemoration & Forward Attack Plan |
| system | any | research-standards | METADOC: Architectural Typology & Research Standards |
| system | any | sop-ecosystem | METADOC: SOP Ecosystem — Taxonomy, Inventory & Coverage |
| system | any | autonomous-content-syndication | SOP: Autonomous Content Syndication (The Broadcast Protocol) |
| system | any | autopoietic-systems-diagnostics | SOP: Autopoietic Systems Diagnostics (The Mirror of Eternity) |
| system | any | background-task-resilience | background-task-resilience |
| system | any | cicd-resilience-and-recovery | SOP: CI/CD Pipeline Resilience & Recovery |
| system | any | community-event-facilitation | SOP: Community Event Facilitation (The Dialectic Crucible) |
| system | any | context-window-conservation | context-window-conservation |
| system | any | conversation-to-content-pipeline | SOP — Conversation-to-Content Pipeline |
| system | any | cross-agent-handoff | SOP: Cross-Agent Session Handoff |
| system | any | cross-channel-publishing-metrics | SOP: Cross-Channel Publishing Metrics (The Echo Protocol) |
| system | any | data-migration-and-backup | SOP: Data Migration and Backup Protocol (The Memory Vault) |
| system | any | document-audit-feature-extraction | SOP: Document Audit & Feature Extraction |
| system | any | dynamic-lens-assembly | SOP: Dynamic Lens Assembly |
| system | any | essay-publishing-and-distribution | SOP: Essay Publishing & Distribution |
| system | any | formal-methods-applied-protocols | SOP: Formal Methods Applied Protocols |
| system | any | formal-methods-master-taxonomy | SOP: Formal Methods Master Taxonomy (The Blueprint of Proof) |
| system | any | formal-methods-tla-pluscal | SOP: Formal Methods — TLA+ and PlusCal Verification (The Blueprint Verifier) |
| system | any | generative-art-deployment | SOP: Generative Art Deployment (The Gallery Protocol) |
| system | any | market-gap-analysis | SOP: Full-Breath Market-Gap Analysis & Defensive Parrying |
| system | any | mcp-server-fleet-management | SOP: MCP Server Fleet Management (The Server Protocol) |
| system | any | multi-agent-swarm-orchestration | SOP: Multi-Agent Swarm Orchestration (The Polymorphic Swarm) |
| system | any | network-testament-protocol | SOP: Network Testament Protocol (The Mirror Protocol) |
| system | any | open-source-licensing-and-ip | SOP: Open Source Licensing and IP (The Commons Protocol) |
| system | any | performance-interface-design | SOP: Performance Interface Design (The Stage Protocol) |
| system | any | pitch-deck-rollout | SOP: Pitch Deck Generation & Rollout |
| system | any | polymorphic-agent-testing | SOP: Polymorphic Agent Testing (The Adversarial Protocol) |
| system | any | promotion-and-state-transitions | SOP: Promotion & State Transitions |
| system | any | recursive-study-feedback | SOP: Recursive Study & Feedback Loop (The Ouroboros) |
| system | any | repo-onboarding-and-habitat-creation | SOP: Repo Onboarding & Habitat Creation |
| system | any | research-to-implementation-pipeline | SOP: Research-to-Implementation Pipeline (The Gold Path) |
| system | any | security-and-accessibility-audit | SOP: Security & Accessibility Audit |
| system | any | session-self-critique | session-self-critique |
| system | any | smart-contract-audit-and-legal-wrap | SOP: Smart Contract Audit and Legal Wrap (The Ledger Protocol) |
| system | any | source-evaluation-and-bibliography | SOP: Source Evaluation & Annotated Bibliography (The Refinery) |
| system | any | stranger-test-protocol | SOP: Stranger Test Protocol |
| system | any | strategic-foresight-and-futures | SOP: Strategic Foresight & Futures (The Telescope) |
| system | any | styx-pipeline-traversal | SOP: Styx Pipeline Traversal (The 7-Organ Transmutation) |
| system | any | system-dashboard-telemetry | SOP: System Dashboard Telemetry (The Panopticon Protocol) |
| system | any | the-descent-protocol | the-descent-protocol |
| system | any | the-membrane-protocol | the-membrane-protocol |
| system | any | theoretical-concept-versioning | SOP: Theoretical Concept Versioning (The Epistemic Protocol) |
| system | any | theory-to-concrete-gate | theory-to-concrete-gate |
| system | any | typological-hermeneutic-analysis | SOP: Typological & Hermeneutic Analysis (The Archaeology) |
| unknown | any | gpt-to-os | SOP_GPT_TO_OS.md |
| unknown | any | index | SOP_INDEX.md |
| unknown | any | obsidian-sync | SOP_OBSIDIAN_SYNC.md |

Linked skills: cicd-resilience-and-recovery, continuous-learning-agent, evaluation-to-growth, genesis-dna, multi-agent-workforce-planner, promotion-and-state-transitions, quality-gate-baseline-calibration, repo-onboarding-and-habitat-creation, structural-integrity-audit


**Prompting (Anthropic)**: context 200K tokens, format: XML tags, thinking: extended thinking (budget_tokens)


## Ecosystem Status

- **delivery**: 2/4 live, 0 planned
- **content**: 0/2 live, 1 planned

Run: `organvm ecosystem show narratological-algorithmic-lenses` | `organvm ecosystem validate --organ I`


## Entity Identity (Ontologia)

**UID:** `ent_repo_01KKKX3RVH9V0QZTE41HWYQCF2` | **Matched by:** primary_name

Resolve: `organvm ontologia resolve narratological-algorithmic-lenses` | History: `organvm ontologia history ent_repo_01KKKX3RVH9V0QZTE41HWYQCF2`


## Live System Variables (Ontologia)

| Variable | Value | Scope | Updated |
|----------|-------|-------|---------|
| `active_repos` | 62 | global | 2026-03-21 |
| `archived_repos` | 53 | global | 2026-03-21 |
| `ci_workflows` | 104 | global | 2026-03-21 |
| `code_files` | 23121 | global | 2026-03-21 |
| `dependency_edges` | 55 | global | 2026-03-21 |
| `operational_organs` | 8 | global | 2026-03-21 |
| `published_essays` | 0 | global | 2026-03-21 |
| `repos_with_tests` | 47 | global | 2026-03-21 |
| `sprints_completed` | 0 | global | 2026-03-21 |
| `test_files` | 4337 | global | 2026-03-21 |
| `total_organs` | 8 | global | 2026-03-21 |
| `total_repos` | 116 | global | 2026-03-21 |
| `total_words_formatted` | 740,907 | global | 2026-03-21 |
| `total_words_numeric` | 740907 | global | 2026-03-21 |
| `total_words_short` | 741K+ | global | 2026-03-21 |

Metrics: 9 registered | Observations: 8632 recorded
Resolve: `organvm ontologia status` | Refresh: `organvm refresh`


## System Density (auto-generated)

AMMOI: 54% | Edges: 28 | Tensions: 33 | Clusters: 5 | Adv: 3 | Events(24h): 14977
Structure: 8 organs / 117 repos / 1654 components (depth 17) | Inference: 98% | Organs: META-ORGANVM:66%, ORGAN-I:55%, ORGAN-II:47%, ORGAN-III:56% +4 more
Last pulse: 2026-03-21T13:20:54 | Δ24h: n/a | Δ7d: n/a


## Dialect Identity (Trivium)

**Dialect:** FORMAL_LOGIC | **Classical Parallel:** Logic | **Translation Role:** The Grammar — defines well-formedness in any dialect

Strongest translations: III (formal), IV (formal), META (formal)

Scan: `organvm trivium scan I <OTHER>` | Matrix: `organvm trivium matrix` | Synthesize: `organvm trivium synthesize`

<!-- ORGANVM:AUTO:END -->


## ⚡ Conductor OS Integration
This repository is a managed component of the ORGANVM meta-workspace.
- **Orchestration:** Use `conductor patch` for system status and work queue.
- **Lifecycle:** Follow the `FRAME -> SHAPE -> BUILD -> PROVE` workflow.
- **Governance:** Promotions are managed via `conductor wip promote`.
- **Intelligence:** Conductor MCP tools are available for routing and mission synthesis.
