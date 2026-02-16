# Analysis Protocols Framework

A systematic differentiation of analytical approaches for applying narratological lenses to creative work. Defines distinct protocols optimized for different purposes, stages, and outputs.

---

## Table of Contents

0. [Framework Overview](#0-framework-overview)
1. [Protocol Taxonomy](#1-protocol-taxonomy)
2. [Protocol Specifications](#2-protocol-specifications)
3. [Role Activation Matrices](#3-role-activation-matrices)
4. [Document Generation Rules](#4-document-generation-rules)
5. [Protocol Selection Logic](#5-protocol-selection-logic)
6. [Cross-Protocol Integration](#6-cross-protocol-integration)
7. [Quick Reference Cards](#7-quick-reference-cards)

---

## 0. Framework Overview

### 0.1 Problem Statement

The comprehensive 9-role, 8-document analysis system is powerful but heavyweight. Different analytical contexts require different configurations:

| Context | Need |
|---------|------|
| First-draft triage | Quick structural assessment, not exhaustive mapping |
| Academic publication | Theoretical rigor over practical revision notes |
| Revision pass | Actionable diagnostics, not historical context |
| Market evaluation | Commercial viability, not thematic depth |
| Algorithm extraction | Mechanism identification, not emotional response |

### 0.2 Solution Architecture

```
PROTOCOL_ARCHITECTURE:

                      â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                      â”‚           SELECTION LAYER                   â”‚
                      â”‚   (Protocol selection based on triggers)    â”‚
                      â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                                            â”‚
          â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
          â”‚                                 â”‚                                 â”‚
          â–¼                                 â–¼                                 â–¼
  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”               â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”               â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
  â”‚   PROTOCOL A  â”‚               â”‚   PROTOCOL B  â”‚               â”‚   PROTOCOL N  â”‚
  â”‚   (Config)    â”‚               â”‚   (Config)    â”‚               â”‚   (Config)    â”‚
  â””â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”˜               â””â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”˜               â””â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”˜
          â”‚                                 â”‚                                 â”‚
          â–¼                                 â–¼                                 â–¼
  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”               â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”               â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
  â”‚  Role Matrix  â”‚               â”‚  Role Matrix  â”‚               â”‚  Role Matrix  â”‚
  â”‚  Doc Set      â”‚               â”‚  Doc Set      â”‚               â”‚  Doc Set      â”‚
  â”‚  Depth Level  â”‚               â”‚  Depth Level  â”‚               â”‚  Depth Level  â”‚
  â””â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”˜               â””â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”˜               â””â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”˜
          â”‚                                 â”‚                                 â”‚
          â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                                            â”‚
                                            â–¼
                      â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                      â”‚           EXECUTION LAYER                   â”‚
                      â”‚   (Shared templates, algorithms, tests)     â”‚
                      â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

### 0.3 Design Principles

| Principle | Implementation |
|-----------|----------------|
| **Composability** | Protocols combine existing components, not create new ones |
| **Specificity** | Each protocol optimized for clear use case |
| **Scalability** | Light protocols can upgrade to heavier ones |
| **Traceability** | Every output maps to role + framework source |

---

## 1. Protocol Taxonomy

### 1.1 Seven Core Protocols

```
PROTOCOL_SPECTRUM:

  DEPTH â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â–º
  
  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
  â”‚   P1    â”‚   P2    â”‚   P3    â”‚   P4    â”‚   P5    â”‚   P6    â”‚   P7    â”‚
  â”‚ TRIAGE  â”‚ STRUCT  â”‚ CRAFT   â”‚ SCHOLAR â”‚ MARKET  â”‚ EXTRACT â”‚ FULL    â”‚
  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”´â”€â”€â”€â”€â”€â”€â”€â”€â”€â”´â”€â”€â”€â”€â”€â”€â”€â”€â”€â”´â”€â”€â”€â”€â”€â”€â”€â”€â”€â”´â”€â”€â”€â”€â”€â”€â”€â”€â”€â”´â”€â”€â”€â”€â”€â”€â”€â”€â”€â”´â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
      â”‚         â”‚         â”‚         â”‚         â”‚         â”‚         â”‚
      â–¼         â–¼         â–¼         â–¼         â–¼         â–¼         â–¼
    1 doc     3 docs    4 docs    5 docs    4 docs    3 docs    8 docs
    2 roles   4 roles   5 roles   5 roles   4 roles   4 roles   9 roles
    30 min    2 hrs     4 hrs     6 hrs     3 hrs     4 hrs     8+ hrs
```

| ID | Protocol Name | Primary Purpose | Typical User |
|----|---------------|-----------------|--------------|
| **P1** | TRIAGE | Quick pass/consider/recommend decision | Reader, agent, producer first-look |
| **P2** | STRUCTURAL | Architecture diagnosis without full breakdown | Writer mid-revision |
| **P3** | CRAFT | Practical revision guidance | Writer seeking feedback |
| **P4** | SCHOLARLY | Academic-grade theoretical analysis | Researcher, critic, student |
| **P5** | MARKET | Commercial viability assessment | Producer, studio executive |
| **P6** | EXTRACT | Mechanism identification for algorithm building | Narratological research |
| **P7** | COMPREHENSIVE | Full 8-document analysis package | Major revision, archival |

### 1.2 Protocol Inheritance

Protocols build on each otherâ€”heavier protocols include lighter protocol outputs:

```
INHERITANCE_CHAIN:

  P1 (TRIAGE)
    â””â”€â”€ P2 (STRUCTURAL) = P1 + structure docs
          â””â”€â”€ P3 (CRAFT) = P2 + character + revision
                â””â”€â”€ P7 (COMPREHENSIVE) = all

  P4 (SCHOLARLY) â†â”€â”€ branched from P2, adds academic rigor
  P5 (MARKET) â†â”€â”€ branched from P1, adds commercial lens  
  P6 (EXTRACT) â†â”€â”€ branched from P2, mechanism focus
```

---

## 2. Protocol Specifications

### 2.1 P1 â€” TRIAGE Protocol

**Purpose**: Rapid assessment for gatekeeping decisions.

**When to Use**:
- First exposure to material
- High volume evaluation (multiple scripts)
- Binary decision needed quickly
- Client/employer needs recommendation

**Configuration**:

```
P1_CONFIG:
  
  ROLES_ACTIVE:
    PRIMARY:   [FIRST-READER, DRAMATURGIST]
    SECONDARY: []
    INACTIVE:  [AESTHETE, NARRATOLOGIST, ART_HIST, CINEPHILE, 
                RHETORICIAN, PRODUCER, ACADEMIC]
  
  DOCUMENTS:
    GENERATE:  [Coverage Report (abbreviated)]
    EXCLUDE:   [Beat Map, Structural Analysis, Character Atlas,
                Thematic Architecture, Diagnostic Report,
                Theoretical Correspondence, Revision Roadmap]
  
  DEPTH: Shallow
  TIME_ESTIMATE: 30-60 minutes
  INGESTION: Single read (engagement-focused)
```

**Output Format**:

```markdown
# [TITLE] â€” Triage Report

**Recommendation**: [ ] RECOMMEND  [ ] CONSIDER  [ ] PASS

## Engagement Response
[FIRST-READER: 2-3 paragraphs on where attention held/flagged]

## Structural Assessment  
[DRAMATURGIST: Brief diagnosis of fundamental architecture]

## Decision Rationale
[1-2 paragraphs justifying recommendation]

## Escalation Notes
[What would deeper analysis reveal? When to upgrade protocol?]
```

---

### 2.2 P2 â€” STRUCTURAL Protocol

**Purpose**: Architecture diagnosis for active revision.

**When to Use**:
- Mid-draft structural overhaul
- Identifying macro-level problems
- Understanding act/sequence architecture
- Preparing for rewrite (not polish)

**Configuration**:

```
P2_CONFIG:
  
  ROLES_ACTIVE:
    PRIMARY:   [DRAMATURGIST, NARRATOLOGIST]
    SECONDARY: [FIRST-READER, CINEPHILE]
    INACTIVE:  [AESTHETE, ART_HIST, RHETORICIAN, PRODUCER, ACADEMIC]
  
  DOCUMENTS:
    GENERATE:  [Coverage Report, Structural Analysis, Diagnostic Report]
    EXCLUDE:   [Beat Map (full), Character Atlas, Thematic Architecture,
                Theoretical Correspondence, Revision Roadmap]
  
  DEPTH: Medium
  TIME_ESTIMATE: 2-3 hours
  INGESTION: Two reads (engagement + structural)
```

**Key Differences from P1**:
- Applies formal structural tests (But/Therefore, Gap analysis)
- Produces ASCII structural diagrams
- Identifies specific turning point issues
- References comparable works for structural models

**Diagnostic Tests Applied**:
- [ ] South Park But/Therefore causal binding
- [ ] McKee progressive complications check
- [ ] Turning point placement validation
- [ ] Act proportion assessment

---

### 2.3 P3 â€” CRAFT Protocol

**Purpose**: Practical revision guidance for working writers.

**When to Use**:
- Script is structurally sound, needs deepening
- Character and dialogue focus
- Preparing for production draft
- Seeking specific, actionable notes

**Configuration**:

```
P3_CONFIG:
  
  ROLES_ACTIVE:
    PRIMARY:   [DRAMATURGIST, NARRATOLOGIST, RHETORICIAN]
    SECONDARY: [FIRST-READER, CINEPHILE]
    INACTIVE:  [AESTHETE, ART_HIST, PRODUCER, ACADEMIC]
  
  DOCUMENTS:
    GENERATE:  [Coverage Report, Structural Analysis, Character Atlas,
                Diagnostic Report, Revision Roadmap]
    EXCLUDE:   [Beat Map (full), Thematic Architecture, 
                Theoretical Correspondence]
  
  DEPTH: Medium-High
  TIME_ESTIMATE: 4-5 hours
  INGESTION: Three reads (engagement + structural + craft)
```

**Key Differences from P2**:
- Character arcs fully mapped
- Dialogue assessment included
- Revision roadmap prioritized by pass
- Line-level polish notes included

**Revision Roadmap Structure**:
1. **Structural Pass**: Architecture fixes
2. **Character Pass**: Arc deepening
3. **Dialogue Pass**: Voice refinement
4. **Polish Pass**: Line-level craft

---

### 2.4 P4 â€” SCHOLARLY Protocol

**Purpose**: Academic-grade theoretical analysis.

**When to Use**:
- Writing about the work (paper, thesis, criticism)
- Teaching or lecture preparation
- Historical/theoretical contextualization
- Peer-reviewed publication

**Configuration**:

```
P4_CONFIG:
  
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
  TIME_ESTIMATE: 6-8 hours
  INGESTION: Multiple reads (structural + thematic + theoretical)
```

**Key Differences from Craft Protocols**:
- No revision guidance (analysis, not prescription)
- Extended theoretical correspondence section
- Citation-ready observations
- Historical lineage mapping
- Framework application demonstration

**Framework Application Depth**:

| Framework | Application Level |
|-----------|-------------------|
| Aristotle | Full Poetics mapping |
| McKee | Value charge + gap analysis |
| Bharata Muni | Rasa identification |
| Attention Mechanics | Engagement mode analysis |

---

### 2.5 P5 â€” MARKET Protocol

**Purpose**: Commercial viability assessment.

**When to Use**:
- Acquisition decision
- Greenlight evaluation
- Market positioning strategy
- Budget/scale determination

**Configuration**:

```
P5_CONFIG:
  
  ROLES_ACTIVE:
    PRIMARY:   [PRODUCER, CINEPHILE]
    SECONDARY: [FIRST-READER, DRAMATURGIST]
    INACTIVE:  [AESTHETE, NARRATOLOGIST, ART_HIST, 
                RHETORICIAN, ACADEMIC]
  
  DOCUMENTS:
    GENERATE:  [Coverage Report (market-focused), 
                Comparative Analysis, Market Positioning (supplement),
                Production Notes (supplement)]
    EXCLUDE:   [Beat Map, Structural Analysis, Character Atlas,
                Thematic Architecture, Diagnostic Report,
                Theoretical Correspondence, Revision Roadmap]
  
  DEPTH: Medium (commercial focus)
  TIME_ESTIMATE: 3-4 hours
  INGESTION: Single read + market research
```

**Market-Specific Outputs**:

```markdown
## Market Positioning Report

### Comparable Titles (Box Office/Ratings Data)
| Title | Year | Budget | Gross | Platform |
|-------|------|--------|-------|----------|

### Target Audience Profile
- Primary: [demographic]
- Secondary: [demographic]
- Crossover potential: [assessment]

### Production Considerations
- Estimated budget tier: [Low/Medium/High/Tentpole]
- Location requirements: [list]
- VFX intensity: [rating]
- Cast requirements: [star power needed?]

### Platform Fit
| Platform | Fit Score | Rationale |
|----------|-----------|-----------|
```

---

### 2.6 P6 â€” EXTRACTION Protocol

**Purpose**: Identifying narrative mechanisms for algorithm construction.

**When to Use**:
- Building narratological algorithm documents
- Studying a creator's methodology
- Reverse-engineering successful narratives
- Cross-work pattern identification

**Configuration**:

```
P6_CONFIG:
  
  ROLES_ACTIVE:
    PRIMARY:   [NARRATOLOGIST, ACADEMIC]
    SECONDARY: [DRAMATURGIST, ART_HIST]
    INACTIVE:  [FIRST-READER, AESTHETE, CINEPHILE, 
                RHETORICIAN, PRODUCER]
  
  DOCUMENTS:
    GENERATE:  [Structural Analysis (mechanism-focused),
                Theoretical Correspondence (extended),
                Mechanism Extraction Report (special)]
    EXCLUDE:   [Coverage Report, Beat Map (narrative),
                Character Atlas, Thematic Architecture,
                Diagnostic Report, Revision Roadmap]
  
  DEPTH: High (mechanism focus)
  TIME_ESTIMATE: 4-6 hours
  INGESTION: Multiple reads (structural + mechanism-hunting)
```

**Mechanism Extraction Report** (Protocol-Specific Document):

```markdown
# [TITLE] â€” Mechanism Extraction Report

## Identified Mechanisms

### M1: [Mechanism Name]
- **Location**: [scenes/beats where visible]
- **Operation**: [how it functions]
- **Source Quote** (if available): "[direct quote]"
- **Formalization**:
  ```
  IF [condition]
  THEN [action]
  YIELDS [effect]
  ```
- **Theoretical Correspondence**: [McKee gap / Aristotle recognition / etc.]
- **Generalizability**: [Universal / Genre-specific / Creator-specific]

### M2: [...]

## Candidate Axioms
| ID | Formulation | Evidence Strength |
|----|-------------|-------------------|

## Cross-Reference to Existing Algorithms
| Mechanism | Similar To | Key Difference |
|-----------|------------|----------------|
```

---

### 2.7 P7 â€” COMPREHENSIVE Protocol

**Purpose**: Full analytical treatment for major work or archival purposes.

**When to Use**:
- Major revision before production
- Archival documentation
- Teaching case study preparation
- Complete understanding required

**Configuration**:

```
P7_CONFIG:
  
  ROLES_ACTIVE:
    PRIMARY:   [ALL NINE ROLES]
    SECONDARY: []
    INACTIVE:  []
  
  DOCUMENTS:
    GENERATE:  [ALL EIGHT CORE DOCUMENTS + SUPPLEMENTS AS WARRANTED]
    EXCLUDE:   []
  
  DEPTH: Maximum
  TIME_ESTIMATE: 8-12 hours
  INGESTION: Four-phase protocol (per SKILL.md)
```

**This is the existing full protocol from SKILL.md.**

---

## 3. Role Activation Matrices

### 3.1 Protocol Ã— Role Matrix

```
ROLE_ACTIVATION_MATRIX:

                    P1      P2      P3      P4      P5      P6      P7
                  TRIAGE  STRUCT  CRAFT  SCHOLAR MARKET EXTRACT  FULL
                  â”€â”€â”€â”€â”€â”€â”€ â”€â”€â”€â”€â”€â”€â”€ â”€â”€â”€â”€â”€â”€â”€ â”€â”€â”€â”€â”€â”€â”€ â”€â”€â”€â”€â”€â”€â”€ â”€â”€â”€â”€â”€â”€â”€ â”€â”€â”€â”€â”€â”€â”€
AESTHETE            â—‹       â—‹       â—‹       â—‹       â—‹       â—‹       â—
DRAMATURGIST        â—       â—       â—       â—       â—       â—       â—
NARRATOLOGIST       â—‹       â—       â—       â—       â—‹       â—       â—
ART_HIST            â—‹       â—‹       â—‹       â—       â—‹       â—       â—
CINEPHILE           â—‹       â—       â—       â—       â—       â—‹       â—
RHETORICIAN         â—‹       â—‹       â—       â—       â—‹       â—‹       â—
PRODUCER            â—‹       â—‹       â—‹       â—‹       â—       â—‹       â—
ACADEMIC            â—‹       â—‹       â—‹       â—       â—‹       â—       â—
FIRST-READER        â—       â—       â—       â—‹       â—       â—‹       â—
                  â”€â”€â”€â”€â”€â”€â”€ â”€â”€â”€â”€â”€â”€â”€ â”€â”€â”€â”€â”€â”€â”€ â”€â”€â”€â”€â”€â”€â”€ â”€â”€â”€â”€â”€â”€â”€ â”€â”€â”€â”€â”€â”€â”€ â”€â”€â”€â”€â”€â”€â”€
TOTAL ACTIVE        2       4       5       5       4       4       9

KEY: â— = Primary  â— = Secondary  â—‹ = Inactive
```

### 3.2 Role Responsibility by Protocol

**FIRST-READER Variations**:

| Protocol | First-Reader Function |
|----------|----------------------|
| P1 (Triage) | Primary: honest engagement narrative |
| P2 (Structural) | Secondary: flag engagement failures |
| P3 (Craft) | Secondary: identify boring stretches |
| P7 (Full) | Primary: complete emotional journey map |

**NARRATOLOGIST Variations**:

| Protocol | Narratologist Function |
|----------|------------------------|
| P2 (Structural) | Primary: apply causal binding tests |
| P3 (Craft) | Primary: gap analysis, mechanism diagnosis |
| P4 (Scholarly) | Primary: full theoretical apparatus |
| P6 (Extract) | Primary: mechanism identification |

---

## 4. Document Generation Rules

### 4.1 Protocol Ã— Document Matrix

```
DOCUMENT_GENERATION_MATRIX:

                          P1    P2    P3    P4    P5    P6    P7
                        â”€â”€â”€â”€â”€ â”€â”€â”€â”€â”€ â”€â”€â”€â”€â”€ â”€â”€â”€â”€â”€ â”€â”€â”€â”€â”€ â”€â”€â”€â”€â”€ â”€â”€â”€â”€â”€
Coverage Report           â—     â—     â—     â—‹     â—     â—‹     â—
Beat Map                  â—‹     â—‹     â—‹     â—‹     â—‹     â—‹     â—
Structural Analysis       â—‹     â—     â—     â—     â—‹     â—     â—
Character Atlas           â—‹     â—‹     â—     â—‹     â—‹     â—‹     â—
Thematic Architecture     â—‹     â—‹     â—‹     â—     â—‹     â—‹     â—
Diagnostic Report         â—‹     â—     â—     â—     â—‹     â—‹     â—
Theoretical Corresp.      â—‹     â—‹     â—‹     â—     â—‹     â—     â—
Revision Roadmap          â—‹     â—‹     â—     â—‹     â—‹     â—‹     â—
â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
Market Positioning        â—‹     â—‹     â—‹     â—‹     â—     â—‹     â—‹
Production Notes          â—‹     â—‹     â—‹     â—‹     â—     â—‹     â—
Comparative Analysis      â—‹     â—‹     â—‹     â—     â—     â—‹     â—
Mechanism Extract         â—‹     â—‹     â—‹     â—‹     â—‹     â—     â—‹
â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
TOTAL DOCUMENTS           1     3     5     4+    4     3     8+

KEY: â— = Full version  â— = Abbreviated  â—‹ = Not generated
```

### 4.2 Document Depth Specifications

**Coverage Report Variants**:

| Protocol | Coverage Variant | Sections Included |
|----------|------------------|-------------------|
| P1 | Triage | Recommendation + Rationale only |
| P2 | Structural | + Synopsis + Structural summary |
| P3 | Craft | + Assessment matrix + Strengths/Areas |
| P5 | Market | + Comparables + Market positioning |
| P7 | Full | All sections |

**Diagnostic Report Variants**:

| Protocol | Diagnostic Variant | Tests Applied |
|----------|-------------------|---------------|
| P2 | Structural-only | Causal binding, turning points, proportions |
| P3 | Craft | + Character validation, attention mechanics |
| P4 | Scholarly | Abbreviated (issues not solutions) |
| P7 | Full | All tests + prioritized issues |

---

## 5. Protocol Selection Logic

### 5.1 Decision Tree

```
PROTOCOL_SELECTION:

  START
    â”‚
    â–¼
  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
  â”‚ What is the primary goal?   â”‚
  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                 â”‚
    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
    â”‚            â”‚            â”‚            â”‚            â”‚
    â–¼            â–¼            â–¼            â–¼            â–¼
  DECIDE      REVISE       STUDY       SELL      BUILD
    â”‚            â”‚            â”‚            â”‚      ALGORITHM
    â”‚            â”‚            â”‚            â”‚            â”‚
    â–¼            â–¼            â–¼            â–¼            â–¼
  â”Œâ”€â”€â”€â”€â”     â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”    â”Œâ”€â”€â”€â”€â”     â”Œâ”€â”€â”€â”€â”      â”Œâ”€â”€â”€â”€â”
  â”‚ P1 â”‚     â”‚How deep?â”‚   â”‚ P4 â”‚     â”‚ P5 â”‚      â”‚ P6 â”‚
  â””â”€â”€â”€â”€â”˜     â””â”€â”€â”€â”€â”¬â”€â”€â”€â”˜    â””â”€â”€â”€â”€â”˜     â””â”€â”€â”€â”€â”˜      â””â”€â”€â”€â”€â”˜
                  â”‚
         â”Œâ”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”
         â”‚       â”‚       â”‚
         â–¼       â–¼       â–¼
      â”Œâ”€â”€â”€â”€â” â”Œâ”€â”€â”€â”€â” â”Œâ”€â”€â”€â”€â”
      â”‚ P2 â”‚ â”‚ P3 â”‚ â”‚ P7 â”‚
      â””â”€â”€â”€â”€â”˜ â””â”€â”€â”€â”€â”˜ â””â”€â”€â”€â”€â”˜
     (struct)(craft)(full)
```

### 5.2 Trigger Phrases

| If request contains... | Select Protocol |
|------------------------|-----------------|
| "quick read", "pass or consider", "worth pursuing?" | P1 (Triage) |
| "structural issues", "act breaks", "what's wrong with the architecture?" | P2 (Structural) |
| "revision notes", "feedback for rewrite", "actionable notes" | P3 (Craft) |
| "academic analysis", "theoretical framework", "for my paper" | P4 (Scholarly) |
| "market potential", "who's the audience?", "budget considerations" | P5 (Market) |
| "extract principles", "how does this work?", "algorithm" | P6 (Extraction) |
| "full analysis", "comprehensive breakdown", "everything" | P7 (Full) |

### 5.3 Escalation Logic

When to upgrade protocols mid-analysis:

| Trigger | Action |
|---------|--------|
| P1 reveals fundamental structural issues | Escalate to P2 |
| P2 reveals character-driven problems | Escalate to P3 |
| P3 requires deeper theoretical frame | Supplement with P4 elements |
| Any protocol reveals commercial question | Add P5 supplement |
| Mechanism discovered worth formalizing | Add P6 extraction |

---

## 6. Cross-Protocol Integration

### 6.1 Protocol Stacking

Multiple protocols can be run sequentially for layered analysis:

```
STACK_PATTERNS:

  WRITER_TRACK:     P1 â†’ P2 â†’ P3 â†’ P7
  SCHOLAR_TRACK:    P2 â†’ P4
  PRODUCER_TRACK:   P1 â†’ P5
  ALGORITHM_TRACK:  P2 â†’ P6
  
  TIME_SAVING: Each subsequent protocol reuses prior outputs
```

### 6.2 Role Carryover

When escalating protocols, prior role observations carry forward:

```
CARRYOVER_RULES:

  IF escalating P1 â†’ P2:
    - FIRST-READER observations preserved
    - DRAMATURGIST notes expanded (not replaced)
  
  IF escalating P2 â†’ P3:
    - All P2 observations preserved
    - RHETORICIAN layer added
    - Character analysis added fresh
  
  IF supplementing with P4:
    - ACADEMIC lens adds theory layer
    - Prior practical observations remain
    - Theoretical correspondence generated
```

### 6.3 Document Reuse

| Source Protocol | Reusable Outputs | For Protocol |
|-----------------|------------------|--------------|
| P1 | Recommendation rationale | P2, P3, P5 |
| P2 | Structural diagrams | P3, P4, P7 |
| P3 | Character atlas | P7 |
| P4 | Theoretical correspondence | P7 |
| P6 | Mechanism extractions | Algorithm documents |

---

## 7. Quick Reference Cards

### 7.1 Protocol Selection Card

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚                     PROTOCOL QUICK SELECT                           â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚                                                                     â”‚
â”‚  "Should we buy/pursue this?"      â†’  P1 TRIAGE                    â”‚
â”‚  "What's structurally broken?"     â†’  P2 STRUCTURAL                â”‚
â”‚  "How do I fix this draft?"        â†’  P3 CRAFT                     â”‚
â”‚  "Analyze this theoretically"      â†’  P4 SCHOLARLY                 â”‚
â”‚  "Will this sell?"                 â†’  P5 MARKET                    â”‚
â”‚  "How does this technique work?"   â†’  P6 EXTRACTION                â”‚
â”‚  "Give me everything"              â†’  P7 COMPREHENSIVE             â”‚
â”‚                                                                     â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

### 7.2 Role Quick Reference

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚                        ROLE QUICK REFERENCE                         â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚                                                                     â”‚
â”‚  FIRST-READER     Emotional engagement, honest response             â”‚
â”‚  DRAMATURGIST     Structure, rhythm, dramatic tension               â”‚
â”‚  NARRATOLOGIST    Mechanisms, theory application, causal binding    â”‚
â”‚  AESTHETE         Form, beauty, style, sensory imagination          â”‚
â”‚  ART_HIST         Context, lineage, influences, movements           â”‚
â”‚  CINEPHILE        Comparables, genre conventions, audience          â”‚
â”‚  RHETORICIAN      Argument, persuasion, dialogue, language          â”‚
â”‚  PRODUCER         Feasibility, budget, casting, market              â”‚
â”‚  ACADEMIC         Rigor, citation, scholarship, frameworks          â”‚
â”‚                                                                     â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

### 7.3 Document Quick Reference

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚                      DOCUMENT QUICK REFERENCE                       â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚                                                                     â”‚
â”‚  CORE DOCUMENTS:                                                    â”‚
â”‚  â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€                                                    â”‚
â”‚  1. Coverage Report       Executive summary + recommendation        â”‚
â”‚  2. Beat Map              Exhaustive scene-by-scene mapping         â”‚
â”‚  3. Structural Analysis   Act/movement architecture                 â”‚
â”‚  4. Character Atlas       All characters + arcs                     â”‚
â”‚  5. Thematic Architecture Theme layers + motif tracking             â”‚
â”‚  6. Diagnostic Report     Structural problems + solutions           â”‚
â”‚  7. Theoretical Corresp.  Framework mapping                         â”‚
â”‚  8. Revision Roadmap      Prioritized action items                  â”‚
â”‚                                                                     â”‚
â”‚  PROTOCOL-SPECIFIC:                                                 â”‚
â”‚  â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€                                                 â”‚
â”‚  â€¢ Market Positioning (P5)                                          â”‚
â”‚  â€¢ Production Notes (P5, P7)                                        â”‚
â”‚  â€¢ Comparative Analysis (P4, P5)                                    â”‚
â”‚  â€¢ Mechanism Extraction (P6)                                        â”‚
â”‚                                                                     â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

### 7.4 Time Estimates

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚                         TIME ESTIMATES                              â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚                                                                     â”‚
â”‚  Protocol      Reads    Roles    Docs    Est. Time                 â”‚
â”‚  â”€â”€â”€â”€â”€â”€â”€â”€â”€     â”€â”€â”€â”€â”€    â”€â”€â”€â”€â”€    â”€â”€â”€â”€    â”€â”€â”€â”€â”€â”€â”€â”€â”€                 â”‚
â”‚  P1 TRIAGE       1        2        1      30-60 min                â”‚
â”‚  P2 STRUCT       2        4        3      2-3 hrs                  â”‚
â”‚  P3 CRAFT        3        5        5      4-5 hrs                  â”‚
â”‚  P4 SCHOLAR      3+       5        4+     6-8 hrs                  â”‚
â”‚  P5 MARKET       1+       4        4      3-4 hrs                  â”‚
â”‚  P6 EXTRACT      3+       4        3      4-6 hrs                  â”‚
â”‚  P7 FULL         4        9        8+     8-12 hrs                 â”‚
â”‚                                                                     â”‚
â”‚  Note: Times assume ~100-page feature script                        â”‚
â”‚                                                                     â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

---

## Appendix A: Protocol Implementation Checklist

For each analysis session:

```
â–¡ Identify primary goal
â–¡ Select protocol (P1-P7)
â–¡ Confirm with requester if ambiguous
â–¡ Activate specified roles
â–¡ Follow ingestion requirements
â–¡ Generate specified documents only
â–¡ Apply specified tests only
â–¡ Check escalation triggers
â–¡ Deliver in role-tagged format
```

---

## Appendix B: Integration with Existing Skills

This framework integrates with:

| Skill | Integration Point |
|-------|-------------------|
| `script-analysis-dramaturgical` | P7 = full skill activation |
| `narratological-algorithms` | P6 feeds algorithm extraction workflow |
| Existing algorithm documents | P4, P6 apply as framework sources |

---

## Appendix C: Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-25 | Initial framework design |

---

*Analysis Protocols Framework v1.0*
*Integrates with: SKILL.md, SKILL-preview.md, Attention Mechanics Meta-Principles*
