# Narratological Algorithmic Lenses - Implementation Plan

## Progress Summary

### Completed
- [x] Phase 1: Core Library Foundation (Pydantic models, loader, 65 tests)
- [x] Phase 2: Algorithm Engine (92 algorithms, registry, executor, 122 tests)
- [x] Phase 3: Analysis & Reports (generators, 9-role analyst, diagnostics, 243 tests @ 77% coverage)
- [x] CLI: study commands (6/6 working), algorithm list/show/stats (3/4 working)
- [x] FastAPI/React scaffolds

### Current: Phase 4 - CLI Backend Wiring

**Goal:** Wire scaffolded CLI commands to the core library.

---

## Phase 4 Implementation Plan

### Current CLI Status

| Module | Commands | Status |
|--------|----------|--------|
| `study.py` | 6 commands | ✅ Fully working |
| `algorithm.py` | 4 commands | ⚠️ 3/4 working (run needs LLM) |
| `analyze.py` | 4 commands | ❌ Scaffolded |
| `diagnose.py` | 5 commands | ❌ Scaffolded |
| `generate.py` | 5 commands | ❌ Scaffolded |

### 4.1 Script Parser (`packages/cli/src/narratological_cli/parser.py`)

Create a simple script parser to convert text files into `Script` models:

```python
def parse_script(path: Path, title: str | None = None) -> Script:
    """Parse a text file into a Script model with basic scene detection."""

def parse_beat_map_json(path: Path) -> DiagnosticContext:
    """Parse a beat map JSON file into DiagnosticContext for diagnostics."""
```

**Scene Detection Heuristics:**
- Look for `INT.` / `EXT.` sluglines
- Fall back to paragraph breaks if no sluglines
- Extract character names from dialogue (ALL CAPS lines)

### 4.2 Wire `diagnose.py` Commands

| Command | Core Library Call |
|---------|-------------------|
| `causal` | `DiagnosticRunner().run_causal(context)` |
| `reorder` | `DiagnosticRunner().run_reorderability(context)` |
| `necessity` | `DiagnosticRunner().run_necessity(context)` |
| `framework` | `DiagnosticRunner().run_framework(context, study_ids)` |
| `all` | `DiagnosticRunner().run_all(context)` |

**Input Options:**
- `--input FILE` - Raw script text file
- `--beat-map FILE` - Pre-analyzed beat map JSON
- `--target FLOAT` - Target score threshold (default 0.80)

### 4.3 Wire `analyze.py` Commands

| Command | Core Library Call |
|---------|-------------------|
| `script` | `CoverageReportGenerator().generate(script)` |
| `scene` | `BeatMapReportGenerator().generate(script)` |
| `compare` | Compare two scripts using diagnostics |
| `batch` | Loop over multiple files |

**LLM Configuration:**
- `--provider [ollama|anthropic|openai|mock]` - Provider selection (default: ollama)
- `--model MODEL` - Model name override (default: llama3.2 for ollama)
- `--base-url URL` - Custom API endpoint for OSS/local models
- Environment variables: `OLLAMA_HOST`, `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`

**Provider Priority (OSS-first):**
1. **Ollama** (default) - Local models, no API key needed
2. **OpenAI-compatible** - Works with LiteLLM, vLLM, LocalAI
3. **Anthropic** - Claude models
4. **Mock** - Testing without any LLM

### 4.4 Wire `generate.py` Commands

| Command | Core Library Call |
|---------|-------------------|
| `outline` | `StructuralReportGenerator` + study algorithms |
| `beats` | `BeatMapReportGenerator` in generation mode |
| `character` | `CharacterAtlasReportGenerator` |
| `transformation` | Ovid study algorithms |

### 4.5 Add OllamaProvider to Core Library

Add OSS-first provider to `packages/core/src/narratological/llm/providers.py`:

```python
class OllamaProvider:
    """OpenAI-compatible provider for Ollama and other local LLMs."""
    def __init__(self, model: str = "llama3.2", base_url: str = "http://localhost:11434/v1"):
        ...
```

### 4.6 Complete `algorithm.py run`

Wire the `run` command to `AlgorithmExecutor`:

```python
executor = create_executor(provider=provider)
result = executor.run(algorithm_id, context, mode=mode)
```

---

## Implementation Sequence

1. **Script Parser** - `parser.py` with basic scene detection
2. **LLM Provider Config** - Add `--provider` flag handling
3. **Wire diagnose.py** - Connect to `DiagnosticRunner`
4. **Wire analyze.py** - Connect to report generators
5. **Wire generate.py** - Connect to LLM-based generation
6. **Complete algorithm run** - Wire to `AlgorithmExecutor`
7. **Add CLI tests** - `packages/cli/tests/test_commands.py`

---

## Files to Create/Modify

| File | Action |
|------|--------|
| `packages/core/src/narratological/llm/providers.py` | MODIFY - Add OllamaProvider |
| `packages/cli/src/narratological_cli/parser.py` | CREATE |
| `packages/cli/src/narratological_cli/llm_config.py` | CREATE |
| `packages/cli/src/narratological_cli/commands/diagnose.py` | MODIFY |
| `packages/cli/src/narratological_cli/commands/analyze.py` | MODIFY |
| `packages/cli/src/narratological_cli/commands/generate.py` | MODIFY |
| `packages/cli/src/narratological_cli/commands/algorithm.py` | MODIFY |
| `packages/cli/tests/test_commands.py` | CREATE |

---

## Verification

```bash
# Run all tests
uv run pytest packages/core/tests/ packages/cli/tests/ -v

# Test diagnose commands (with mock provider)
uv run narratological diagnose causal sample.txt --provider mock
uv run narratological diagnose all sample.txt --output report.json

# Test analyze commands
uv run narratological analyze script sample.txt --provider mock
uv run narratological analyze scene sample.txt --output beatmap.json

# Test generate commands
uv run narratological generate outline --study pixar --provider mock
uv run narratological generate character "John Doe" --arc positive

# Test algorithm execution
uv run narratological algorithm run pixar/empathy-engineering --mode analyze --input sample.txt
```

---

## Project Vision

Transform the theoretical specifications into a comprehensive software system with four integrated components:

1. **Narrative Analysis Tool** - Analyze scripts/stories using formalized algorithms
2. **AI/LLM Integration Library** - Enable AI systems to apply narratological frameworks
3. **Interactive Reference App** - Browse, search, and apply specifications
4. **Code Generation Framework** - Generate narrative structures algorithmically

---

## What We're Building (Distilled from Specifications)

### Core Data Model
- **14 studies** with ~79 axioms, ~92 algorithms, structural hierarchies, diagnostic questions
- **7 sequence pairs** linking related studies (Tarkovsky↔Bergman, Moore↔Morrison, etc.)
- **5 analysis templates**: Coverage, Structural, Beat Map, Character Atlas, Diagnostic
- **8-role analyst system**: Aesthete, Dramaturgist, Narratologist, Art Historian, Cinephile, Rhetorician, Producer, Academic, First-Reader

### Key Algorithms to Implement
- **Transformation validation** (Ovid) - Metamorphosis logic with mens_pristina preservation
- **Empathy engineering** (Pixar) - 5-step character investment system
- **Discovery pacing** (Zelda) - Gravity well distribution, exploration rewards
- **Causal binding analysis** - BUT/THEREFORE vs AND THEN connector validation
- **Diagnostic batteries** - Reorderability, necessity, information economy tests

### Analysis Workflows
- Generate coverage reports (executive summaries with recommendations)
- Create beat maps (scene-by-scene with 15 function codes)
- Build character atlases (Want vs Need, arc classification)
- Run diagnostic tests (targeting >80% causal binding)
- Map theoretical correspondences (Aristotle, McKee, Campbell, etc.)

---

## Architecture

**Hybrid: Python core + TypeScript web app** (decided)

Key directories:
- `packages/core/` - Python library (Pydantic models, algorithms, LLM)
- `packages/cli/` - CLI application (typer)
- `packages/api/` - FastAPI backend
- `packages/web/` - React/TypeScript frontend

---

## Remaining Phases (Future)

### Phase 5: API Layer
- FastAPI endpoints calling core library
- Streaming support for long analyses
- WebSocket for real-time diagnostic feedback

### Phase 6: Web Application
- React frontend consuming API
- Interactive study/algorithm explorer
- Visual beat map editor
- Diagnostic dashboard
