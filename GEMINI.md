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
**Org:** `unknown` | **Repo:** `narratological-algorithmic-lenses`

### Edges
- **Produces** → `unknown`: unknown

### Siblings in Theory
`recursive-engine--generative-entity`, `organon-noumenon--ontogenetic-morphe`, `auto-revision-epistemic-engine`, `call-function--ontological`, `sema-metra--alchemica-mundi`, `system-governance-framework`, `cognitive-archaelogy-tribunal`, `a-recursive-root`, `radix-recursiva-solve-coagula-redi`, `.github`, `nexus--babel-alexandria-`, `reverse-engine-recursive-run`, `4-ivi374-F0Rivi4`, `cog-init-1-0-`, `collective-persona-operations` ... and 4 more

### Governance
- Foundational theory layer. No upstream dependencies.

*Last synced: 2026-02-24T12:41:28Z*
<!-- ORGANVM:AUTO:END -->
