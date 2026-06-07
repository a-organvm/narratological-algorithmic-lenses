# Alchemical I/O — Source & Transmutation

Narrative of inputs, process, and returns.

## Inputs (Prima Materia)

### Primary Sources
Five foundational texts providing the theoretical axioms:

| Source | Tradition | Key Contribution |
|--------|-----------|-----------------|
| Aristotle — *Poetics* | Greek tragedy | Structure, mimesis, catharsis |
| Bharata Muni — *Natyasastra* | Sanskrit drama | Rasa, dosas, holistic performance |
| Horace — *Ars Poetica* | Roman criticism | Decorum, didactic function |
| Plato — *Republic* | Greek philosophy | Mimetic hierarchy, moral weight |
| McKee — *Story* | Screenwriting | Controlling ideas, value change |

### Practitioner Studies
28 completed studies extracting algorithms from:

- **Film:** Bergman, Kubrick, Lynch, Tarkovsky, Tarantino, Pixar, South Park
- **Comics:** Gaiman (Sandman), Kirby (New Gods), Morrison, Ellis, Moore
- **Literature:** Tolkien, Larry David, Phoebe Waller-Bridge
- **Games:** Final Fantasy, Zelda
- **Oral traditions:** African epic, Kishōtenketsu, Heroine's Journey
- **Theory:** McKee, 8-Role Analyst framework

### User Input
- Script files (`.txt`, `.fountain`, `.pdf`, `.fdx`)
- Protocol selection (P1-P7)
- Provider configuration (OpenAI, Anthropic, Ollama)

## Transmutation Pipeline

```
┌─────────────────────────────────────────────────────────┐
│                    INPUT LAYER                          │
│  Scripts (Fountain parser) → Script model               │
│  Study data (JSON/Markdown) → Study/Algorithm models    │
│  Protocol selection → ProtocolSpec                      │
└──────────────────────┬──────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────┐
│                  PROCESS LAYER                          │
│  Algorithm Executor: runs selected algorithms           │
│  Protocol Runner: orchestrates multi-role analysis      │
│  LLM Provider: generates narrative analysis             │
│  Diagnostic Engine: identifies structural issues        │
└──────────────────────┬──────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────┐
│                   OUTPUT LAYER                          │
│  Structured reports (JSON models)                       │
│  Markdown narratives (human-readable)                   │
│  Diagnostic results (actionable feedback)               │
│  Generated content (outlines, characters, beats)        │
└─────────────────────────────────────────────────────────┘
```

## Returns (Gold)

### For Practitioners
- Protocol-gounded analysis reports
- Diagnostic questions specific to their script's issues
- Revision roadmaps with prioritized action items
- Character and structure breakdowns

### For Scholars
- Formalized algorithmic representations of craft principles
- Cross-tradition comparison frameworks
- Structured data for computational analysis
- Traceable axioms from primary sources

### For Students
- Multi-perspective explanations through 9 analyst roles
- Concrete examples from 28 diverse practitioner traditions
- Progressive depth from triage (P1) to full analysis (P7)
- Interactive exploration via web dashboard

## Transmutation Log

| Version | Input | Process | Output |
|---------|-------|---------|--------|
| v0.1.0 | 5 sources, 28 studies | Core lib + CLI + API | 304 tests, protocol framework |
| v0.2.0 | +10 studies, +scripts | +Web tests, +API depth | +Streaming, +Multi-modal |
| v1.0.0 | +50 studies, +plugins | +Collaborative, +Ecosystem | +Full documentation |
