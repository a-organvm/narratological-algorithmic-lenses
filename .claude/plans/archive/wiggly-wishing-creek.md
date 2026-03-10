# Plan: Create `there+back-again.md` Roadmap & Update README

## Context

The narratological-algorithmic-lenses repository has completed its full build cycle (Phases 1–6), its "Omega Synthesis" release (v0.1.0), and a comprehensive Claude Desktop intake (52 files, 27 threads). The project is at PRODUCTION/CANDIDATE status within the organvm ecosystem.

The user wants three things in this session:
1. **Create `there+back-again.md`** — an exhaustive macro↔micro↔macro roadmap documenting the full journey from origin to true omega, with milestones
2. **Update README.md** — fix stale elements (counts, directory layout, missing new sections)
3. **Stage, commit, push**

---

## Part 1: Create `docs/plans/there+back-again.md`

### Location
`docs/plans/there+back-again.md` (the `docs/plans/` directory already exists)

### Structure: MACRO → MICRO → MACRO

The document follows a three-act structure mirroring the narrative theory it formalizes:

#### ACT I — MACRO: The Journey There (Origin → Current State)
A chronicle of how the project got here, phase by phase, with what each produced.

**Section 1.1: Genesis** — The Claude Desktop "open-view" project
- 52 project files, 27 conversation threads (Jan–Feb 2026)
- Core thesis: attention as ur-currency of narrative
- 5 primary sources, 10 algorithm docs, research reports, skills, creative work

**Section 1.2: Phase Map** — Each build phase with concrete deliverables

| Phase | Name | Commit | Key Deliverables |
|-------|------|--------|------------------|
| 0 | Platinum Sprint | `7bc9982`–`4c2df46` | CI, CHANGELOG, ADR-001/002, badge row |
| 1 | Foundation | `ed5a5a8` | Pydantic models, JSON loader, 14 studies, 65 tests |
| 2 | Promotion | `ff93834`–`a4820e9` | Fountain parser, Causal Binding, study promotions, Script Doctor layer |
| 3 | Engine | `acbc172`–`69a7dd4` | Generators (4), 8-role analyst, diagnostic runners (5), algorithm engine, 243 tests |
| 4 | Debate | `3ecfee0`–`9dd2e3f` | CLI wiring, LLM providers, parser module, 290 tests |
| 5 | Interface | `0c3a781` | FastAPI routes, React dashboard, MCP server, VS Code extension |
| 6 | Omega Synthesis | `115fbdc`–`5aacbb7` | Documentation, v0.1.0 release, organvm integration |
| 7 | Intake | `2e1029f` | 119 files: 19 text docs, 27 threads, 9 PDFs, 45 EL bonus files |

**Section 1.3: Current State Inventory**

| Layer | Count | Status |
|-------|-------|--------|
| Completed studies | 28 (+ 1 research report) | `specs/02-completed-studies/` |
| JSON extracts | 28 | `specs/03-structured-data/json-extracts/` |
| Unified compendium | 1 (295 KB) | `specs/03-structured-data/` |
| Core Python modules | 34 .py files | `packages/core/` |
| CLI commands | 4 groups (diagnose, analyze, generate, algorithm) | `packages/cli/` |
| API routes | Studies, analysis, diagnostics | `packages/api/` |
| Web components | 4 (StudyExplorer, AlgorithmViewer, DiagnosticRunner, ScriptDoctorWorkbench) | `packages/web/` |
| MCP server | FastMCP wrapper | `packages/mcp/` |
| VS Code extension | 2 snippet files | `packages/vscode/` |
| Spec directories | 13 | `specs/00–12` |
| Tests | 248+ passing | `packages/core/tests/` |

#### ACT II — MICRO: The Milestones Ahead (Current → True Omega)

Concrete, actionable milestones with specific files and tasks.

**Milestone 1: The Scouring (Housekeeping)** — THIS SESSION
- [x] README.md: fix stale study count (27+ → 28), update repo layout, add new sections
- [x] CHANGELOG.md: add intake commit, add this session
- [x] Create this roadmap document

**Milestone 2: Data Integrity Hardening**
- Validate all 28 JSON extracts load cleanly via `uv run narratological validate compendium`
- Ensure `ovid-study-research-report.md` is correctly classified (research report, not a study — currently in `02-completed-studies/`)
- Verify Bharata Muni supplement/extended in `05-secondary-sources/` are properly cross-referenced
- Confirm unified compendium JSON matches all 28 individual extracts
- Run `uv run narratological validate sync` — fix any drift

**Milestone 3: Package Hardening**
- **CLI**: Verify all 4 command groups work end-to-end with a real `.fountain` file
- **API**: Smoke-test all routes with `uvicorn` + curl
- **Web**: `npm run build` succeeds; basic component rendering verified
- **MCP**: Server starts, tool discovery works, at least one tool invocation succeeds
- **VS Code**: Snippets load in VS Code, fountain syntax triggers

**Milestone 4: CI/CD Pipeline**
- Verify `.github/workflows/ci-python.yml` runs: lint, type-check, test
- Add web build step to CI
- Add MCP server test step
- Badge in README reflects real CI status

**Milestone 5: Protocol Framework Integration**
- Wire `specs/08-protocol-framework/` docs into the software layer
- P1–P7 protocol skills (`specs/09-protocol-skills/`) available via CLI/API
- Protocol invocation via `uv run narratological analyze protocol --level P3 my_script.fountain`

**Milestone 6: New Study Pipeline**
- Document the end-to-end flow: markdown study → JSON extract → compendium → algorithm registry
- Automate JSON extraction from markdown studies
- Target list from PF-029/030: next candidates for formalization

**Milestone 7: Deployment**
- Web dashboard deployed (Vercel or similar)
- MCP server registered in Claude Desktop
- PyPI package published (`pip install narratological`)
- npm package published (web components)

**Milestone 8: True Omega**
- Self-sustaining pipeline: new study auto-flows through entire system
- Community contribution pathway documented
- Academic paper readiness (formal methodology description)
- Complete test coverage across all packages
- Performance benchmarks for diagnostic analysis

#### ACT III — MACRO: The Journey Back (System → Theory → System)

**Section 3.1: The Feedback Loop**
How the software system enriches the theoretical foundation:
- Diagnostic results reveal gaps in theoretical frameworks
- Cross-study analysis discovers emergent patterns not visible in individual studies
- Script Doctor debates generate novel theoretical synthesis

**Section 3.2: The Organvm Integration**
- Organ I (Theoria) → consumed by Organ II (Poiesis)
- Governance subscriptions from Organ IV
- Health audit compliance
- The project as a living node in a larger system

**Section 3.3: The Omega State**
Definition of "done" — not a fixed endpoint but a self-sustaining state where:
- New narrative knowledge flows in automatically
- Analysis capabilities expand without architectural changes
- The system validates and enriches its own theoretical foundations
- *There and Back Again* — the Bilbo principle: the system returns enriched

---

## Part 2: Update README.md

### Stale elements identified

| Line | Current | Fix |
|------|---------|-----|
| 10 | "27+ formalized narrative frameworks" | → "28 formalized narrative frameworks" |
| 40–53 | Repository Layout missing 9 spec dirs, `docs/` present but incomplete | → Full accurate tree with all 13 spec dirs |
| 52 | Shows `docs/` as "Documentation & Roadmaps" | → Accurate: `docs/adr/` and `docs/plans/` |
| 44 | Only shows `06-open-view-drafts/` under specs | → Show key dirs: `00-chat-transcripts/`, `01-primary-sources/`, `02-completed-studies/`, `03-structured-data/`, `04-templates/`, `05-secondary-sources/`, `06-open-view-drafts/`, `07-skill-documentation/`, `08-protocol-framework/`, `09-protocol-skills/`, `10-project-manifests/`, `11-el-series/`, `12-mythological-sources/` |
| 121 | Closing line "There and Back Again." | → Link to roadmap: "There and Back Again — [the roadmap](docs/plans/there+back-again.md)." |

### Content additions
- Add a "Project History" or "Phases" section summarizing the build arc
- Add "Protocol Framework" to Core Capabilities (P1–P7)
- Add "Claude Desktop Archive" mention (27 conversation threads, full provenance)

---

## Part 3: Stage, Commit, Push

```bash
git add -A
git commit -m "docs: add there+back-again roadmap and refresh README

- Create docs/plans/there+back-again.md: exhaustive macro↔micro↔macro
  roadmap from genesis through current state to true omega
- Update README.md: fix study count (28), expand repo layout to show
  all 13 spec directories, add protocol framework capabilities,
  link roadmap from closing line
- Update CHANGELOG.md: document intake and roadmap sessions"
git push origin main
```

---

## Files to create/modify

| File | Action | Size |
|------|--------|------|
| `docs/plans/there+back-again.md` | **CREATE** | ~8–12 KB |
| `README.md` | **MODIFY** | Update stale counts, expand layout, add sections |
| `CHANGELOG.md` | **MODIFY** | Add entries for intake + this session |

## Verification

1. `docs/plans/there+back-again.md` exists with all three acts
2. README.md study count reads "28" not "27+"
3. README.md repo layout shows all 13 `specs/` subdirs
4. CHANGELOG.md has entries for both intake and roadmap
5. `uv run pytest` still passes (no code changes)
6. `git status` clean after commit
7. Push to origin succeeds
