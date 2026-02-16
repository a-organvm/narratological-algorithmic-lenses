---
name: protocol-scholarly
description: Academic-grade theoretical analysis protocol (P4) for scholarly output. Triggers on "academic analysis", "for a paper", "theoretical framework", "teaching material", "lecture prep", "peer review", "thesis chapter", "historical context". Produces Structural Analysis, Thematic Architecture, Theoretical Correspondence, and Diagnostic Report. Uses ACADEMIC, NARRATOLOGIST, ART_HIST as primary roles. Estimated time 6-8 hours per 100-page script.
---

# P4 â€” SCHOLARLY Protocol

Academic-grade theoretical analysis for scholarly purposes.

## Configuration

```yaml
ROLES_ACTIVE:
  PRIMARY:   [ACADEMIC, NARRATOLOGIST, ART_HIST]
  SECONDARY: [RHETORICIAN, CINEPHILE]
  INACTIVE:  [FIRST-READER, DRAMATURGIST, PRODUCER, AESTHETE]

DOCUMENTS:
  GENERATE:  [Structural Analysis, Thematic Architecture,
              Theoretical Correspondence, Diagnostic Report,
              Comparative Analysis (supplement)]
  EXCLUDE:   [Coverage Report, Beat Map, Character Atlas,
              Revision Roadmap]

DEPTH: High (theoretical)
INGESTION: Multiple reads (structural + thematic + theoretical)
```

## Key Differences from Craft Protocols

- **No revision guidance** â€” analysis, not prescription
- Extended theoretical correspondence section
- Citation-ready observations
- Historical lineage mapping
- Framework application demonstration

## Ingestion Protocol

### Read 1: Structural
- Map architecture without judgment
- Note unconventional structures

### Read 2: Thematic
- Identify controlling idea
- Track motif patterns
- Map symbolic systems

### Read 3: Theoretical
- Apply frameworks systematically
- Document correspondences
- Note departures from theory

## Framework Application Depth

Apply all relevant frameworks with full documentation:

| Framework | Application Level |
|-----------|-------------------|
| Aristotle | Full Poetics mapping (unity, reversal, recognition) |
| McKee | Value charge + gap analysis |
| Bharata Muni | Rasa identification + bhava mapping |
| Attention Mechanics | Engagement mode analysis |
| Medium-specific | As warranted by work type |

## Core Deliverables

### 1. Theoretical Correspondence Table (Required)

```markdown
## Theoretical Correspondence

### [FRAMEWORK 1] Application

| Element | Framework Principle | Implementation | Assessment |
|---------|---------------------|----------------|------------|
| [X] | [Principle] | [How work does/doesn't] | âœ“/âœ— |

### [FRAMEWORK 2] Application
[Same format]

### Cross-Framework Synthesis
[How multiple frameworks illuminate different aspects]
```

### 2. Thematic Architecture (Required)

```markdown
## Thematic Architecture

### Controlling Idea
**Thesis**: [1-sentence argument]
**Antithesis**: [Counter-argument represented in work]
**Synthesis**: [Resolution, if any]

### Thematic Layers
| Layer | Theme | Evidence | Prominence |
|-------|-------|----------|------------|
| Primary | [X] | pp. X, Y, Z | Central |
| Secondary | [X] | pp. X, Y | Supporting |

### Motif Tracking
| Motif | First Appearance | Recurrences | Transformation |
|-------|------------------|-------------|----------------|
| [X] | p. X | pp. Y, Z | [How it evolves] |
```

### 3. Historical Lineage (Required)

[ART_HIST] provides:

```markdown
## Historical Lineage

### Antecedents
- [Work/Movement] (Year) â€” [Specific influence]

### Contemporaneous Context
- [How work relates to current moment]

### Descendant Influence (if applicable)
- [How work has influenced subsequent works]
```

### 4. Citation-Ready Observations

Format observations for direct quotation in academic writing:

```markdown
## Key Observations (Citation-Ready)

> "[Direct observation with page reference]" (p. X)

**Analysis**: [Interpretive commentary suitable for academic prose]
```

## Academic Standards

- All claims supported by textual evidence
- Page/line references for every observation
- Theoretical terminology used precisely
- Counter-arguments acknowledged
- Scope of claims appropriately limited
