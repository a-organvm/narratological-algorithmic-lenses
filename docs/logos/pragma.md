# Pragma — Concrete State

The honest account of what exists.

## Repository

- **Monorepo** with 4 Python packages (`core`, `cli`, `api`, `mcp`) + 1 React web app + 1 VS Code extension
- **Version:** 0.1.0 (initial release, 2026-02-11)
- **Python:** 3.11+, managed via `uv`
- **Web:** React 18 + Vite + TypeScript, Vitest for testing

## Data Layer

| Asset | Count | Location |
|-------|-------|----------|
| Primary sources | 5 | `specs/01-primary-sources/` |
| Completed studies | 28 | `specs/02-completed-studies/` |
| Structured data exports | — | `specs/03-structured-data/` |
| Templates | — | `specs/04-templates/` |
| Protocol specifications | 6 docs | `specs/08-protocol-framework/` |

## Core Library (`packages/core`)

**Models:** `Study`, `Algorithm`, `Axiom`, `DiagnosticQuestion`, `StructuralHierarchy`, `TheoreticalCorrespondences`, `QuickReference`, `Script`, `Scene`, `Character`, `ProtocolSpec`, `ProtocolLevel`, `AnalystRole`

**Modules:**
- `parsers/` — Fountain script parser (197 lines, well-annotated)
- `algorithms/` — Registry, executor, base classes
- `protocols/` — P1-P7 protocol specs, runner, prompts
- `generators/` — Report generators with 16 utility functions
- `llm/` — Provider abstraction (OpenAI, Anthropic, mock)

**Quality:**
- 304 Python tests passing, 1 skipped
- mypy clean (77 files, no errors)
- ruff clean

## CLI (`packages/cli`)

Typer-based CLI with subcommands: `study`, `algorithm`, `diagnose`, `analyze`, `generate`, `info`, `version`, `protocol`

- 48 CLI tests passing, 1 skipped

## API (`packages/api`)

FastAPI service, 5 tests passing.

## Web (`packages/web`)

React + Vite dashboard with 4 route components:
- `StudyExplorer` — Browse and select studies
- `AlgorithmViewer` — View algorithm details
- `DiagnosticRunner` — Run diagnostic analyses
- `ScriptDoctorWorkbench` — Interactive script analysis

**Test coverage:** Minimal — 1 smoke test (App.test.tsx). No component-level tests.

## Protocol Framework

Seven protocol levels from triage to full craft analysis:

| Level | Name | Roles | Purpose |
|-------|------|-------|---------|
| P1 | Triage | 2 | Quick coverage assessment |
| P2 | Diagnostic | 3 | Identify structural issues |
| P3 | Craft | 5 | Deep craft analysis |
| P4 | Character | 4 | Character atlas and dynamics |
| P5 | Thematic | 4 | Thematic architecture |
| P6 | Revision | 6 | Actionable revision roadmap |
| P7 | Full | 9 | Complete multi-role analysis |

## Known Gaps

1. **Logos docs** — This layer was missing until this session
2. **Web test coverage** — Only 1 smoke test; no component tests
3. **Fountain parser** — Missing 3 return type annotations (`__init__`, `_start_new_scene`, `_finalize_current_scene`)
4. **One `type: ignore`** — `utils.py:79` suppresses a valid type error
5. **Protocol CLI test** — No CLI-level test for `analyze protocol` subcommand
