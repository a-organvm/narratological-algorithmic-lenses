# Analysis Protocols Skills Integration Guide

How the protocol skills integrate with the existing narratological algorithms project.

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                      USER REQUEST                                    │
│  "Analyze this script" / "Give me notes" / "How does this work?"    │
└────────────────────────────────┬────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────────┐
│                   creative-analysis (Router)                         │
│                                                                      │
│  Parses intent → Selects protocol → Confirms with user              │
└────────────────────────────────┬────────────────────────────────────┘
                                 │
         ┌───────────────────────┼───────────────────────┐
         ▼                       ▼                       ▼
┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐
│  Protocol Skill │   │  Protocol Skill │   │  Protocol Skill │
│   (P1-P7)       │   │   (P1-P7)       │   │   (P1-P7)       │
└────────┬────────┘   └────────┬────────┘   └────────┬────────┘
         │                     │                     │
         └─────────────────────┼─────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    PROJECT KNOWLEDGE BASE                            │
│                                                                      │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐  │
│  │ Algorithm Docs   │  │ Templates        │  │ Meta-Framework   │  │
│  │                  │  │                  │  │                  │  │
│  │ • McKee          │  │ • coverage.md    │  │ • attention_     │  │
│  │ • Aristotle      │  │ • beat-map.md    │  │   mechanics.md   │  │
│  │ • South Park     │  │ • structural.md  │  │                  │  │
│  │ • PWB            │  │ • character.md   │  │ • analysis_      │  │
│  │ • Larry David    │  │ • diagnostic.md  │  │   protocols_     │  │
│  │ • Bharata Muni   │  │                  │  │   framework.md   │  │
│  │ • Horace         │  │                  │  │                  │  │
│  │ • Plato          │  │                  │  │                  │  │
│  └──────────────────┘  └──────────────────┘  └──────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
```

## Integration Points

### 1. Algorithm Application

Protocols reference these project files for framework tests:

| Protocol | Applies |
|----------|---------|
| P2, P3, P7 | McKee gap analysis, progressive complications |
| P2, P3, P7 | South Park but/therefore test |
| P3, P7 | Phoebe Waller-Bridge three-obstacle check |
| P3, P7 | Larry David cascading consequences |
| P4, P7 | Aristotle unity/catharsis/reversal |
| P4, P7 | Bharata Muni rasa identification |
| All | Attention Mechanics engagement modes |

### 2. Template Usage

Protocols pull templates from:

```
/mnt/project/coverage-template.md    → P1, P2, P3, P5, P7
/mnt/project/beat-map-template.md    → P7
/mnt/project/structural-template.md  → P2, P3, P4, P7
/mnt/project/character-template.md   → P3, P7
/mnt/project/diagnostic-template.md  → P2, P3, P4, P7
```

### 3. Extraction → Algorithm Pipeline

P6-EXTRACTION feeds the narratological-algorithms workflow:

```
P6 Analysis
    │
    ▼
Mechanism Extraction Report
    │
    ▼
Candidate Axioms + Formalizations
    │
    ▼
narratological-algorithms skill
    │
    ▼
New Algorithm Document
    │
    ▼
Project Knowledge Base
```

## Skill File Locations

After installation:

```
/mnt/skills/user/
├── creative-analysis/
│   ├── SKILL.md (master router)
│   └── references/
│       └── quick-reference.md
├── protocol-triage/
│   └── SKILL.md (P1)
├── protocol-structural/
│   └── SKILL.md (P2)
├── protocol-craft/
│   └── SKILL.md (P3)
├── protocol-scholarly/
│   └── SKILL.md (P4)
├── protocol-market/
│   └── SKILL.md (P5)
├── protocol-extraction/
│   └── SKILL.md (P6)
└── protocol-comprehensive/
    └── SKILL.md (P7)
```

## Invocation Patterns

### Via Router (Recommended)

```
User: "Analyze this script—I need revision notes"
Claude: [Reads creative-analysis/SKILL.md]
Claude: "Selected: P3-CRAFT. This will produce..."
Claude: [Reads protocol-craft/SKILL.md]
Claude: [Executes protocol]
```

### Direct Protocol

```
User: "Apply P6 extraction protocol to this episode"
Claude: [Reads protocol-extraction/SKILL.md directly]
Claude: [Executes protocol]
```

### Natural Language

```
User: "How does Tarantino structure this scene?"
Claude: [Router identifies P6 intent]
Claude: [Executes extraction protocol]
```

## Project Manifest Integration

Add to `/mnt/project/narratological_project_manifest.md`:

```markdown
### Skills & Templates (Update)

#### SF-001: Creative Analysis Router

| Field | Value |
|-------|-------|
| **ID** | `SF-001` |
| **Filename** | `creative-analysis/SKILL.md` |
| **Tags** | `SKILL`, `ROUTER`, `ANALYSIS` |

**Annotation**: Master routing skill for protocol selection.

#### SF-002 through SF-008: Protocol Skills

[P1-P7 skill entries]
```

## Version Compatibility

| Skill Version | Compatible With |
|---------------|-----------------|
| creative-analysis v1.0 | analysis_protocols_framework v1.0 |
| protocol-* v1.0 | SKILL.md (dramaturgical) v1.0 |
| All | attention_mechanics_meta_principles current |
