---
name: protocol-extraction
description: Mechanism identification and algorithm extraction protocol (P6) for studying how narrative techniques work. Triggers on "how does this technique work", "extract the mechanism", "algorithm extraction", "formalize the approach", "what's the pattern", "study this showrunner's method". Produces Structural Analysis (mechanism-focused), Theoretical Correspondence, and Mechanism Extraction Report. Designed to feed the narratological-algorithms workflow. Estimated time 4-6 hours per work.
---

# P6 â€” EXTRACTION Protocol

Mechanism identification for algorithm development.

## Configuration

```yaml
ROLES_ACTIVE:
  PRIMARY:   [NARRATOLOGIST, ACADEMIC]
  SECONDARY: [DRAMATURGIST, ART_HIST]
  INACTIVE:  [FIRST-READER, AESTHETE, CINEPHILE, RHETORICIAN, PRODUCER]

DOCUMENTS:
  GENERATE:  [Structural Analysis (mechanism-focused), 
              Theoretical Correspondence, Mechanism Extraction Report]
  EXCLUDE:   [Coverage Report, Beat Map, Character Atlas,
              Thematic Architecture, Revision Roadmap]

DEPTH: High (theoretical + operational)
INGESTION: Multiple targeted reads (per mechanism)
```

## Purpose

Extract replicable narrative mechanisms from creative work for formalization into algorithmic frameworks. This protocol feeds the `narratological-algorithms` skill workflow.

## Ingestion Protocol

### Read 1: Pattern Identification
- Note recurring structural patterns
- Flag unusual or innovative techniques
- Mark moments of particular effectiveness

### Read 2: Mechanism Isolation
- For each identified pattern:
  - Define operational boundaries
  - Identify components
  - Document trigger conditions

### Read 3: Cross-Reference
- Compare to existing algorithms
- Note similarities and differences
- Identify novel elements

## Core Deliverable: Mechanism Extraction Report

```markdown
# Mechanism Extraction Report: [WORK TITLE]

## Executive Summary
[1-2 paragraphs: What mechanisms were identified? What's novel?]

---

## M1: [MECHANISM NAME]

### Location in Source
- [Specific instances with page/timestamp references]

### Operational Description
[2-3 paragraphs: How does this mechanism work?]

### Components

| Component | Function | Required? |
|-----------|----------|-----------|
| [X] | [What it does] | Yes/No |

### Trigger Conditions
- When does the creator deploy this technique?
- What narrative problem does it solve?

### Formalization Attempt

```
MECHANISM_[NAME]:
  
  INPUTS:
    - [Input 1]
    - [Input 2]
  
  PROCESS:
    1. [Step 1]
    2. [Step 2]
    IF [condition]:
      [Action A]
    ELSE:
      [Action B]
  
  OUTPUTS:
    - [Output 1]
  
  VALIDATION:
    [How to verify mechanism is working]
```

### Scope Assessment
- **Generalizability**: [Universal / Genre-specific / Creator-specific / Work-specific]
- **Medium constraints**: [Any / Film only / TV only / etc.]
- **Combinability**: [Works with X, conflicts with Y]

---

## M2: [...]
[Same format]

---

## Candidate Axioms

| ID | Formulation | Evidence Strength | Source Mechanism |
|----|-------------|-------------------|------------------|
| [A1] | [Axiom statement] | High/Med/Low | M1 |

---

## Cross-Reference to Existing Algorithms

| Mechanism | Similar To | Key Difference |
|-----------|------------|----------------|
| M1 | [Existing algorithm] | [What's different] |

---

## Recommended Next Steps

1. [ ] Validate mechanism across additional works by same creator
2. [ ] Test generalizability with works by other creators
3. [ ] Integrate into narratological-algorithms corpus
4. [ ] Develop diagnostic questions
```

## Extraction Quality Criteria

A well-extracted mechanism must be:

| Criterion | Test |
|-----------|------|
| **Observable** | Can you point to specific instances? |
| **Repeatable** | Does creator use it consistently? |
| **Describable** | Can you explain it without jargon? |
| **Formalizable** | Can you write pseudocode for it? |
| **Testable** | Can you verify presence/absence? |

## Integration with Existing Algorithms

Cross-reference extracted mechanisms against:

- `/mnt/project/mckee_narratological_algorithms_complete.md`
- `/mnt/project/south_park_narratological_algorithms.md`
- `/mnt/project/larry_david_narratological_algorithms.md`
- `/mnt/project/phoebe_waller_bridge_narratological_algorithms.md`
- `/mnt/project/aristotle_narratological_algorithms.md`
- `/mnt/project/bharata_muni_narratological_algorithms.md`
- `/mnt/project/attention_mechanics_meta_principles.md`

## Output Handoff

Completed extraction reports feed into:
1. Algorithm document creation (via `narratological-algorithms` skill)
2. Study prompts for future creator analyses
3. Cross-reference tables in project manifest
