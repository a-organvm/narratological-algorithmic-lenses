# Praxis — Remediation Plan

The attack vectors for evolution.

## Immediate (This Session)

### 1. Close Type Safety Gaps
- Fix `type: ignore` in `utils.py:79` — replace `screen_times.get` with lambda
- Add missing return annotations to `fountain.py` — `__init__`, `_start_new_scene`, `_finalize_current_scene`

### 2. Protocol CLI Test Coverage
- Add `TestAnalyzeProtocolCommand` to `packages/cli/tests/test_commands.py`
- Cover: help, invalid level, missing file, mock-provider execution

### 3. Web Component Tests
- Add Vitest tests for `StudyExplorer`, `AlgorithmViewer`, `DiagnosticRunner`, `ScriptDoctorWorkbench`
- Use existing SSR pattern from `App.test.tsx`

## Short-Term (Next Sprint)

### 4. Web Test Depth
- Add interaction tests (click handlers, route navigation)
- Add loading/error state tests
- Target: 80% component coverage

### 5. Fountain Parser Hardening
- Enable `--check-untyped-defs` for `parsers.fountain` module
- Add edge case tests: empty scripts, malformed headings, dual dialogue

### 6. API Test Expansion
- Current: 5 tests. Target: cover all endpoints with integration tests
- Add OpenAPI schema validation tests

## Medium-Term (v0.2.0)

### 7. Protocol Runner Improvements
- Add streaming output support for long-running analyses
- Add progress callbacks for protocol execution
- Support parallel role analysis within protocols

### 8. Study Data Pipeline
- Automate study extraction from primary sources
- Add validation pipeline for study JSON exports
- Create study comparison and diff tools

### 9. Documentation Completeness
- Add API reference docs (auto-generated from FastAPI OpenAPI)
- Create user guide with walkthrough scenarios
- Document protocol selection decision tree

## Long-Term (v1.0.0)

### 10. Multi-Modal Analysis
- Image frame analysis (cinematic composition)
- Audio/dialogue rhythm analysis
- Interactive narrative structure analysis (games)

### 11. Collaborative Features
- Multi-user protocol sessions
- Annotation and commenting on analysis results
- Version tracking for revision protocols

### 12. Ecosystem Integration
- VS Code extension feature completion
- MCP server for external tool integration
- Plugin system for custom algorithms
