# Narratological Algorithmic Lenses

## Project Overview

**Narratological Algorithmic Lenses** is a computational narratology system designed to formalize narrative craft into implementable algorithmic frameworks. The project extracts "narrative algorithms" from primary sources (Aristotle, McKee) and master works (Tarkovsky, Pixar, Zelda), codifying them into a queryable database and a set of analysis tools.

This repository serves as both a **research archive** (containing the studies and extracted data) and a **software monorepo** (containing the tools to parse, analyze, and visualize narrative structures).

## Technology Stack

- **Core Logic:** Python 3.11+
- **Package Management:** `uv` (Python workspace), `npm` (JavaScript)
- **Backend/API:** FastAPI
- **CLI:** Python (Typer/Click-based)
- **Frontend:** TypeScript, React, Vite
- **Testing & Quality:** `pytest`, `ruff`, `mypy`, `vitest`

## Repository Structure

### Software Packages (`packages/`)
The codebase is organized as a monorepo managed by `uv`.

- **`packages/core`**: The foundational library. Contains Pydantic models for Studies, Axioms, and Algorithms, as well as the logic for loading and searching the compendium.
- **`packages/api`**: A FastAPI backend that exposes the core logic via REST endpoints (`/studies`, `/analysis`, `/diagnostics`).
- **`packages/cli`**: The command-line interface (`narratological`) for interacting with the system directly from the terminal.
- **`packages/web`**: A React-based visualization dashboard for exploring studies and running interactive analyses.

### Research & Data (`specs/`)
The knowledge base of the system.

- **`01-primary-sources/`**: Raw texts (Aristotle's Poetics, etc.).
- **`02-completed-studies/`**: Markdown documents detailing specific analytical lenses (e.g., `pixar-narratological-algorithms.md`).
- **`03-structured-data/`**: JSON extracts of the studies, ready for computational use.
- **`04-templates/`**: Standardized templates for creating new analyses.

### Case Studies (`open-view-analysis/`)
Example applications of the system. Contains comprehensive analysis of the "Open View" screenplay using the defined protocols.

## Development & Usage

### Prerequisites
- Python 3.11+
- Node.js & npm
- `uv` (Universal Python Package Installer)

### Setup
1.  **Initialize Python Workspace:**
    ```bash
    uv sync
    ```
2.  **Initialize Web Workspace:**
    ```bash
    npm install
    ```

### Running the System

**1. Command Line Interface (CLI)**
Explore studies and search axioms directly:
```bash
# List all available studies
uv run narratological study list

# Search for specific narrative concepts
uv run narratological study search "irony"
```

**2. Backend API**
Start the API server (default: `http://localhost:8000`):
```bash
uv run uvicorn narratological_api.main:app --reload
```

**3. Web Dashboard**
Start the frontend development server:
```bash
npm run web:dev
```

### Testing & Linting

**Python (Core, API, CLI):**
```bash
# Run tests
uv run pytest

# Linting and Formatting
uv run ruff check .
uv run mypy .
```

**Web Frontend:**
```bash
npm run web:test
```

## Workflow

1.  **Extraction**: Narrative principles are researched and documented in `specs/02-completed-studies/`.
2.  **Codification**: these principles are converted into structured JSON in `specs/03-structured-data/`.
3.  **Implementation**: The `core` library loads these definitions.
4.  **Application**: Users employ the `cli`, `api`, or `web` tools to apply these algorithms to new stories (as seen in `open-view-analysis/`).

<!-- ORGANVM:AUTO:START -->
## System Context (auto-generated — do not edit)

**Organ:** ORGAN-I (Theory) | **Tier:** standard | **Status:** PUBLIC_PROCESS
**Org:** `organvm-i-theoria` | **Repo:** `narratological-algorithmic-lenses`

### Edges
- **Produces** → `organvm-ii-poiesis/art-from--narratological-algorithmic-lenses`: dependency

### Siblings in Theory
`recursive-engine--generative-entity`, `organon-noumenon--ontogenetic-morphe`, `auto-revision-epistemic-engine`, `call-function--ontological`, `sema-metra--alchemica-mundi`, `system-governance-framework`, `cognitive-archaelogy-tribunal`, `a-recursive-root`, `radix-recursiva-solve-coagula-redi`, `.github`, `nexus--babel-alexandria-`, `reverse-engine-recursive-run`, `4-ivi374-F0Rivi4`, `cog-init-1-0-`, `collective-persona-operations` ... and 4 more

### Governance
- Foundational theory layer. No upstream dependencies.

*Last synced: 2026-03-08T20:11:34Z*

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
| system | any | research-standards | METADOC: Architectural Typology & Research Standards |
| system | any | sop-ecosystem | METADOC: SOP Ecosystem — Taxonomy, Inventory & Coverage |
| system | any | autopoietic-systems-diagnostics | SOP: Autopoietic Systems Diagnostics (The Mirror of Eternity) |
| system | any | cicd-resilience-and-recovery | SOP: CI/CD Pipeline Resilience & Recovery |
| system | any | cross-agent-handoff | SOP: Cross-Agent Session Handoff |
| system | any | document-audit-feature-extraction | SOP: Document Audit & Feature Extraction |
| system | any | essay-publishing-and-distribution | SOP: Essay Publishing & Distribution |
| system | any | market-gap-analysis | SOP: Full-Breath Market-Gap Analysis & Defensive Parrying |
| system | any | pitch-deck-rollout | SOP: Pitch Deck Generation & Rollout |
| system | any | promotion-and-state-transitions | SOP: Promotion & State Transitions |
| system | any | repo-onboarding-and-habitat-creation | SOP: Repo Onboarding & Habitat Creation |
| system | any | research-to-implementation-pipeline | SOP: Research-to-Implementation Pipeline (The Gold Path) |
| system | any | security-and-accessibility-audit | SOP: Security & Accessibility Audit |
| system | any | session-self-critique | session-self-critique |
| system | any | source-evaluation-and-bibliography | SOP: Source Evaluation & Annotated Bibliography (The Refinery) |
| system | any | stranger-test-protocol | SOP: Stranger Test Protocol |
| system | any | strategic-foresight-and-futures | SOP: Strategic Foresight & Futures (The Telescope) |
| system | any | typological-hermeneutic-analysis | SOP: Typological & Hermeneutic Analysis (The Archaeology) |
| unknown | any | gpt-to-os | SOP_GPT_TO_OS.md |
| unknown | any | index | SOP_INDEX.md |
| unknown | any | obsidian-sync | SOP_OBSIDIAN_SYNC.md |

Linked skills: evaluation-to-growth


**Prompting (Google)**: context 1M tokens (Gemini 1.5 Pro), format: markdown, thinking: thinking mode (thinkingConfig)

<!-- ORGANVM:AUTO:END -->


## ⚡ Conductor OS Integration
This repository is a managed component of the ORGANVM meta-workspace.
- **Orchestration:** Use `conductor patch` for system status and work queue.
- **Lifecycle:** Follow the `FRAME -> SHAPE -> BUILD -> PROVE` workflow.
- **Governance:** Promotions are managed via `conductor wip promote`.
- **Intelligence:** Conductor MCP tools are available for routing and mission synthesis.
