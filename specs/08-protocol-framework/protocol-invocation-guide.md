# Protocol Invocation Guide

Practical guide for invoking analysis protocols. Includes invocation syntax, worked examples, and workflow specifications.

---

## 1. Invocation Syntax

### 1.1 Explicit Protocol Request

```
SYNTAX:

  "Run [PROTOCOL] on [MATERIAL]"
  "Analyze [MATERIAL] using [PROTOCOL] protocol"
  "[PROTOCOL_NAME] analysis of [MATERIAL]"

EXAMPLES:

  "Run P3-CRAFT on my screenplay"
  "Analyze this script using the TRIAGE protocol"  
  "Scholarly analysis of Open View draft 3"
  "P6 extraction on this Fleabag episode"
```

### 1.2 Implicit Protocol Selection

When no protocol is specified, selection follows the decision tree:

| Request Phrasing | Selected Protocol |
|------------------|-------------------|
| "Quick thoughts on this script" | P1 (Triage) |
| "What's wrong with the structure?" | P2 (Structural) |
| "Give me revision notes" | P3 (Craft) |
| "Analyze this theoretically" | P4 (Scholarly) |
| "Will this sell?" | P5 (Market) |
| "How does this technique work?" | P6 (Extraction) |
| "Full analysis" / "Everything" | P7 (Comprehensive) |

### 1.3 Protocol Modifiers

```
MODIFIERS:

  "P3, but skip the character atlas"
  "P2 with emphasis on turning points"
  "P5, also include production notes"
  "P1, but if interesting escalate to P2"

COMBINATION_SYNTAX:

  "P2 + P5 combined"     â†’ Structural + Market lenses
  "P3 then P6"           â†’ Craft analysis, then extract mechanisms
  "Start P1, upgrade as needed"
```

---

## 2. Protocol Workflow Specifications

### 2.1 P1 â€” TRIAGE Workflow

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚                    P1 TRIAGE WORKFLOW                        â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚                                                              â”‚
â”‚  STEP 1: SINGLE ENGAGEMENT READ                              â”‚
â”‚  â”œâ”€â”€ Read material without stopping                          â”‚
â”‚  â”œâ”€â”€ Note engagement peaks/valleys                           â”‚
â”‚  â””â”€â”€ Capture first-reader emotional journey                  â”‚
â”‚                                                              â”‚
â”‚  STEP 2: FUNDAMENTAL ARCHITECTURE CHECK                      â”‚
â”‚  â”œâ”€â”€ Protagonist identifiable? Goal clear?                   â”‚
â”‚  â”œâ”€â”€ Opposition present? Causation working?                  â”‚
â”‚  â””â”€â”€ Red flag scan (passive protag, reorderable scenes)      â”‚
â”‚                                                              â”‚
â”‚  STEP 3: RECOMMENDATION                                      â”‚
â”‚  â”œâ”€â”€ Synthesize engagement + architecture                    â”‚
â”‚  â”œâ”€â”€ Make binary decision (RECOMMEND/CONSIDER/PASS)          â”‚
â”‚  â””â”€â”€ Note escalation potential                               â”‚
â”‚                                                              â”‚
â”‚  OUTPUT: Triage Report (1 document)                          â”‚
â”‚  TIME: 30-60 minutes                                         â”‚
â”‚                                                              â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

### 2.2 P2 â€” STRUCTURAL Workflow

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚                  P2 STRUCTURAL WORKFLOW                      â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚                                                              â”‚
â”‚  STEP 1: ENGAGEMENT READ (inherit from P1)                   â”‚
â”‚                                                              â”‚
â”‚  STEP 2: STRUCTURAL READ                                     â”‚
â”‚  â”œâ”€â”€ Identify act/movement breaks                            â”‚
â”‚  â”œâ”€â”€ Mark all turning points                                 â”‚
â”‚  â”œâ”€â”€ Note proportions (setup/confrontation/resolution)       â”‚
â”‚  â””â”€â”€ Map parallel plotlines if present                       â”‚
â”‚                                                              â”‚
â”‚  STEP 3: DIAGNOSTIC TESTS                                    â”‚
â”‚  â”œâ”€â”€ But/Therefore causal binding test                       â”‚
â”‚  â”œâ”€â”€ McKee progressive complications check                   â”‚
â”‚  â”œâ”€â”€ Turning point placement validation                      â”‚
â”‚  â””â”€â”€ Proportion assessment                                   â”‚
â”‚                                                              â”‚
â”‚  STEP 4: STRUCTURAL DIAGNOSIS                                â”‚
â”‚  â”œâ”€â”€ Identify critical structural issues                     â”‚
â”‚  â”œâ”€â”€ Reference comparable structural models                  â”‚
â”‚  â””â”€â”€ Generate ASCII structural diagrams                      â”‚
â”‚                                                              â”‚
â”‚  STEP 5: SYNTHESIS                                           â”‚
â”‚  â””â”€â”€ Coverage Report + Structural Analysis + Diagnostic      â”‚
â”‚                                                              â”‚
â”‚  OUTPUT: 3 documents                                         â”‚
â”‚  TIME: 2-3 hours                                             â”‚
â”‚                                                              â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

### 2.3 P3 â€” CRAFT Workflow

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚                    P3 CRAFT WORKFLOW                         â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚                                                              â”‚
â”‚  STEP 1-4: INHERIT FROM P2                                   â”‚
â”‚                                                              â”‚
â”‚  STEP 5: CHARACTER ANALYSIS                                  â”‚
â”‚  â”œâ”€â”€ Profile all named characters                            â”‚
â”‚  â”œâ”€â”€ Map want/need/wound triads                              â”‚
â”‚  â”œâ”€â”€ Track arcs and transformations                          â”‚
â”‚  â””â”€â”€ Assess character-driven issues                          â”‚
â”‚                                                              â”‚
â”‚  STEP 6: DIALOGUE ASSESSMENT                                 â”‚
â”‚  â”œâ”€â”€ Voice distinctiveness check                             â”‚
â”‚  â”œâ”€â”€ Exposition handling evaluation                          â”‚
â”‚  â””â”€â”€ Subtext identification                                  â”‚
â”‚                                                              â”‚
â”‚  STEP 7: REVISION ROADMAP                                    â”‚
â”‚  â”œâ”€â”€ Prioritize all identified issues                        â”‚
â”‚  â”œâ”€â”€ Sequence into revision passes                           â”‚
â”‚  â”œâ”€â”€ Estimate effort for each item                           â”‚
â”‚  â””â”€â”€ Formulate questions for the artist                      â”‚
â”‚                                                              â”‚
â”‚  OUTPUT: 5 documents                                         â”‚
â”‚  TIME: 4-5 hours                                             â”‚
â”‚                                                              â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

### 2.4 P4 â€” SCHOLARLY Workflow

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚                  P4 SCHOLARLY WORKFLOW                       â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚                                                              â”‚
â”‚  STEP 1: STRUCTURAL READ                                     â”‚
â”‚  â”œâ”€â”€ Identify formal architecture                            â”‚
â”‚  â””â”€â”€ Note unconventional structures                          â”‚
â”‚                                                              â”‚
â”‚  STEP 2: THEMATIC MAPPING                                    â”‚
â”‚  â”œâ”€â”€ Identify controlling idea                               â”‚
â”‚  â”œâ”€â”€ Map theme layers                                        â”‚
â”‚  â”œâ”€â”€ Track motifs and symbols                                â”‚
â”‚  â””â”€â”€ Note articulation points                                â”‚
â”‚                                                              â”‚
â”‚  STEP 3: THEORETICAL APPLICATION                             â”‚
â”‚  â”œâ”€â”€ Apply Aristotelian framework                            â”‚
â”‚  â”œâ”€â”€ Apply McKee value system                                â”‚
â”‚  â”œâ”€â”€ Apply attention mechanics                               â”‚
â”‚  â”œâ”€â”€ Apply genre-specific frameworks                         â”‚
â”‚  â””â”€â”€ Note where work resists/subverts frameworks             â”‚
â”‚                                                              â”‚
â”‚  STEP 4: HISTORICAL CONTEXTUALIZATION                        â”‚
â”‚  â”œâ”€â”€ Identify artistic lineage                               â”‚
â”‚  â”œâ”€â”€ Note movement affiliations                              â”‚
â”‚  â””â”€â”€ Map intertextual references                             â”‚
â”‚                                                              â”‚
â”‚  STEP 5: COMPARATIVE ANALYSIS                                â”‚
â”‚  â””â”€â”€ Extended comparison with reference works                â”‚
â”‚                                                              â”‚
â”‚  OUTPUT: 4-5 documents (scholarly-formatted)                 â”‚
â”‚  TIME: 6-8 hours                                             â”‚
â”‚                                                              â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

### 2.5 P5 â€” MARKET Workflow

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚                   P5 MARKET WORKFLOW                         â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚                                                              â”‚
â”‚  STEP 1: ENGAGEMENT READ (commercial lens)                   â”‚
â”‚  â”œâ”€â”€ Note "hook" moments                                     â”‚
â”‚  â”œâ”€â”€ Identify "trailer moments"                              â”‚
â”‚  â””â”€â”€ Assess pacing for commercial viability                  â”‚
â”‚                                                              â”‚
â”‚  STEP 2: COMPARABLE RESEARCH                                 â”‚
â”‚  â”œâ”€â”€ Identify 3-5 direct comparables                         â”‚
â”‚  â”œâ”€â”€ Research performance data                               â”‚
â”‚  â””â”€â”€ Analyze success/failure patterns                        â”‚
â”‚                                                              â”‚
â”‚  STEP 3: AUDIENCE ANALYSIS                                   â”‚
â”‚  â”œâ”€â”€ Define primary demographic                              â”‚
â”‚  â”œâ”€â”€ Identify secondary/crossover potential                  â”‚
â”‚  â””â”€â”€ Assess audience size and accessibility                  â”‚
â”‚                                                              â”‚
â”‚  STEP 4: PRODUCTION ASSESSMENT                               â”‚
â”‚  â”œâ”€â”€ Budget tier estimation                                  â”‚
â”‚  â”œâ”€â”€ Production feasibility flags                            â”‚
â”‚  â””â”€â”€ Cast requirement analysis                               â”‚
â”‚                                                              â”‚
â”‚  STEP 5: PLATFORM FIT                                        â”‚
â”‚  â””â”€â”€ Assess fit across distribution platforms                â”‚
â”‚                                                              â”‚
â”‚  OUTPUT: 4 documents (market-focused)                        â”‚
â”‚  TIME: 3-4 hours                                             â”‚
â”‚                                                              â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

### 2.6 P6 â€” EXTRACTION Workflow

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚                  P6 EXTRACTION WORKFLOW                      â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚                                                              â”‚
â”‚  STEP 1: STRUCTURAL MAPPING                                  â”‚
â”‚  â”œâ”€â”€ Map complete structure                                  â”‚
â”‚  â””â”€â”€ Identify recurring patterns                             â”‚
â”‚                                                              â”‚
â”‚  STEP 2: MECHANISM HUNTING                                   â”‚
â”‚  â”œâ”€â”€ Identify operational techniques                         â”‚
â”‚  â”œâ”€â”€ Note where effects are produced                         â”‚
â”‚  â”œâ”€â”€ Cross-reference with known mechanisms                   â”‚
â”‚  â””â”€â”€ Flag novel or unusual approaches                        â”‚
â”‚                                                              â”‚
â”‚  STEP 3: SOURCE EVIDENCE GATHERING                           â”‚
â”‚  â”œâ”€â”€ Locate creator statements (if available)                â”‚
â”‚  â”œâ”€â”€ Document specific instances                             â”‚
â”‚  â””â”€â”€ Assess evidence strength                                â”‚
â”‚                                                              â”‚
â”‚  STEP 4: FORMALIZATION ATTEMPT                               â”‚
â”‚  â”œâ”€â”€ Write pseudocode for each mechanism                     â”‚
â”‚  â”œâ”€â”€ Identify preconditions and effects                      â”‚
â”‚  â””â”€â”€ Map to existing theoretical frameworks                  â”‚
â”‚                                                              â”‚
â”‚  STEP 5: AXIOM IDENTIFICATION                                â”‚
â”‚  â””â”€â”€ Distill underlying principles                           â”‚
â”‚                                                              â”‚
â”‚  OUTPUT: 3 documents (extraction-focused)                    â”‚
â”‚  TIME: 4-6 hours                                             â”‚
â”‚                                                              â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

### 2.7 P7 â€” COMPREHENSIVE Workflow

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚                P7 COMPREHENSIVE WORKFLOW                     â”‚
â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¤
â”‚                                                              â”‚
â”‚  FULL 4-PHASE INGESTION (per SKILL.md)                       â”‚
â”‚  â”œâ”€â”€ Phase 1: Initial read (engagement)                      â”‚
â”‚  â”œâ”€â”€ Phase 2: Structural read                                â”‚
â”‚  â”œâ”€â”€ Phase 3: Analytical read (annotation)                   â”‚
â”‚  â””â”€â”€ Phase 4: Synthesis                                      â”‚
â”‚                                                              â”‚
â”‚  ALL 9 ROLES ACTIVE                                          â”‚
â”‚                                                              â”‚
â”‚  ALL 8 CORE DOCUMENTS GENERATED                              â”‚
â”‚  â”œâ”€â”€ Coverage Report                                         â”‚
â”‚  â”œâ”€â”€ Beat Map (exhaustive)                                   â”‚
â”‚  â”œâ”€â”€ Structural Analysis                                     â”‚
â”‚  â”œâ”€â”€ Character Atlas                                         â”‚
â”‚  â”œâ”€â”€ Thematic Architecture                                   â”‚
â”‚  â”œâ”€â”€ Diagnostic Report                                       â”‚
â”‚  â”œâ”€â”€ Theoretical Correspondence                              â”‚
â”‚  â””â”€â”€ Revision Roadmap                                        â”‚
â”‚                                                              â”‚
â”‚  SUPPLEMENTS AS WARRANTED                                    â”‚
â”‚  â”œâ”€â”€ Production Notes                                        â”‚
â”‚  â”œâ”€â”€ Comparative Analysis                                    â”‚
â”‚  â”œâ”€â”€ Dialogue Analysis                                       â”‚
â”‚  â”œâ”€â”€ Visual Grammar                                          â”‚
â”‚  â””â”€â”€ Market Positioning                                      â”‚
â”‚                                                              â”‚
â”‚  OUTPUT: 8+ documents                                        â”‚
â”‚  TIME: 8-12 hours                                            â”‚
â”‚                                                              â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

---

## 3. Worked Examples

### 3.1 Example: Triage Request

**Request**: "Quick thoughts on this pilot scriptâ€”worth developing?"

**Protocol Selected**: P1 (TRIAGE)

**Invocation Log**:
```
PROTOCOL: P1-TRIAGE
MATERIAL: [Pilot Script, 55 pages]
ROLES: FIRST-READER (primary), DRAMATURGIST (primary)
DOCUMENTS: Triage Report (abbreviated coverage)
```

**Sample Output Structure**:
```
# [Untitled Pilot] â€” Triage Report

## Recommendation
[X] CONSIDER

## First-Reader Response
The cold open grabbed attention immediatelyâ€”the visual of [specific image] 
creates instant intrigue. Engagement held through the first act break (p.18) 
but flagged during the extended exposition sequence (pp. 22-31). The final 
twist (p. 52) partially recovered interest but felt unearned.

## Structural Assessment  
Fundamental architecture is present: clear protagonist (JANE), identifiable 
goal (expose the conspiracy), active opposition (DIRECTOR CHEN). However, 
causal binding weakens in Act Twoâ€”several scenes feel reorderable.

RED FLAGS:
- [X] Reorderable scenes (pp. 22-31)

## Decision Rationale
Strong concept and promising pilot hook. Structural issues in Act Two are 
addressable. Worth a structural pass (P2) to diagnose specific fixes.

## Escalation Notes
Recommend P2 (STRUCTURAL) to diagnose Act Two causation issues.
```

---

### 3.2 Example: Revision Request

**Request**: "I'm doing my second draftâ€”need feedback to guide revision"

**Protocol Selected**: P3 (CRAFT)

**Invocation Log**:
```
PROTOCOL: P3-CRAFT
MATERIAL: [Feature Script, 112 pages]
ROLES: DRAMATURGIST (P), NARRATOLOGIST (P), RHETORICIAN (P), 
       FIRST-READER (S), CINEPHILE (S)
DOCUMENTS: Coverage Report, Structural Analysis, Character Atlas,
           Diagnostic Report, Revision Roadmap
```

**Sample Revision Roadmap Excerpt**:
```
## Suggested Revision Sequence

### Pass 1 â€” Structure (Est. 1 week)
Priority items:

| # | Issue | Location | Action | Effort |
|---|-------|----------|--------|--------|
| 1 | Inciting incident delayed | pp. 1-18 | Move catalyst to p.10 | Medium |
| 2 | Act Two sag | pp. 45-62 | Add midpoint reversal | High |
| 3 | Climax undramatized | pp. 98-105 | Expand confrontation | Medium |

### Pass 2 â€” Character (Est. 1 week)
[...]

### Questions for the Artist
1. Is MARCUS's betrayal intended as surprise or dramatic irony?
2. What is ELENA's ghost/woundâ€”it's currently unclear?
3. The B-story with DETECTIVE HUANGâ€”is this essential or cuttable?
```

---

### 3.3 Example: Academic Analysis Request

**Request**: "I'm writing a paper on surveillance aesthetics in contemporary cinemaâ€”can you analyze this film theoretically?"

**Protocol Selected**: P4 (SCHOLARLY)

**Invocation Log**:
```
PROTOCOL: P4-SCHOLARLY
MATERIAL: [Feature Film or Script]
ROLES: ACADEMIC (P), NARRATOLOGIST (P), ART_HIST (P),
       RHETORICIAN (S), CINEPHILE (S)
DOCUMENTS: Structural Analysis, Thematic Architecture,
           Theoretical Correspondence, Comparative Analysis
```

**Sample Theoretical Correspondence Excerpt**:
```
## Theoretical Correspondence

### Foucauldian Framework

The film's panopticon motif operates on multiple levels:

| Element | Panopticon Analogue | Textual Evidence |
|---------|---------------------|------------------|
| HQ surveillance room | Central tower | "We see everything" (p.34) |
| Family unawareness | Prisoner uncertainty | Quadrant structure |
| Viewer position | Guard position | Found-footage POV |

### McKee Framework Application

| Element | McKee Principle | Implementation | Assessment |
|---------|-----------------|----------------|------------|
| Controlling Idea | Value + Cause | "Privacy is [...]" | âœ“ Clear |
| Gap | Action â‰  Reaction | Multiple instances | âœ“ Functional |
| Progressive Compl. | Escalating obstacles | See Act Two analysis | âœ— Incomplete |

### Attention Mechanics

The film operates primarily in **prediction-failure-recalibration** mode (jazz), 
with genre expectations established then subverted at the beat level. This 
aligns with Attention Mechanics axiom ATT-A4 regarding mode consistency.
```

---

### 3.4 Example: Algorithm Extraction Request

**Request**: "I want to study how this showrunner structures episodesâ€”extract the mechanisms"

**Protocol Selected**: P6 (EXTRACTION)

**Invocation Log**:
```
PROTOCOL: P6-EXTRACT
MATERIAL: [3 episodes from series]
ROLES: NARRATOLOGIST (P), ACADEMIC (P), DRAMATURGIST (S), ART_HIST (S)
DOCUMENTS: Structural Analysis (mechanism-focused), 
           Theoretical Correspondence, Mechanism Extraction Report
```

**Sample Mechanism Extraction Excerpt**:
```
## M3: The "Echo Scene" Technique

**Location in Source**: 
- Episode 1: pp. 12, 45 (mirrored)
- Episode 2: pp. 8, 52 (mirrored)  
- Episode 3: pp. 15, 48 (mirrored)

**Operational Description**:
The showrunner creates paired scenes early and late in each episode that 
mirror each other structurally but with inverted emotional valence. The 
first scene establishes a configuration; the echo scene reveals how that 
configuration has transformed.

**Formalization Attempt**:

```
MECHANISM: echo_scene

PRECONDITION:
  Scene A exists in first quarter of episode
  Scene A establishes character configuration C
  
OPERATION:
  Create Scene B in final quarter
  Scene B mirrors Scene A in:
    - Location (same or symbolically parallel)
    - Character configuration (same participants)
    - Dialogue rhythm (similar pacing)
  Scene B inverts Scene A in:
    - Emotional valence
    - Power dynamics
    - Information state

EFFECT:
  - Structural symmetry creates satisfaction
  - Transformation becomes visible through contrast
  - Episode feels "complete"
  
VALIDATION_TEST:
  Remove Scene B â†’ Does episode feel unfinished?
  If YES â†’ Mechanism is functional
```

**Theoretical Correspondence**:

| Framework | Related Concept | Relationship |
|-----------|-----------------|--------------|
| McKee | Scene polarity reversal | Extension to episode-level |
| Aristotle | Recognition (anagnorisis) | Echo scene as recognition site |
| Attention Mechanics | Prediction-satisfaction | Setup/payoff at macro level |
```

---

## 4. Protocol Upgrade Paths

### 4.1 Standard Escalation Triggers

| Current | Trigger | Upgrade To |
|---------|---------|------------|
| P1 | "Structural issues need diagnosis" | P2 |
| P1 | "Commercial viability question" | P5 |
| P2 | "Characters need work" | P3 |
| P2 | "Interesting mechanisms here" | P6 |
| P3 | "Need theoretical framing" | P3 + P4 elements |
| P3 | "Needs full treatment" | P7 |
| Any | "Give me everything" | P7 |

### 4.2 Upgrade Syntax

```
"Based on P1 analysis, escalate to P2"
"Continue from P2 findings into P3"
"Add P4 theoretical layer to existing P3"
"Complete upgrade to P7"
```

### 4.3 Document Reuse

When upgrading, prior documents carry forward:

| From | To | Reused | Generated Fresh |
|------|-----|--------|-----------------|
| P1 | P2 | Engagement notes | Structural Analysis, Diagnostics |
| P2 | P3 | All P2 docs | Character Atlas, Revision Roadmap |
| P2 | P4 | Structural Analysis | Thematic, Theoretical, Comparative |
| P3 | P7 | All P3 docs | Beat Map, Thematic, Theoretical |

---

## 5. Quality Checklist by Protocol

### P1 Checklist
- [ ] Recommendation clearly stated
- [ ] Engagement journey captured
- [ ] Fundamental architecture checked
- [ ] Escalation noted if warranted

### P2 Checklist
- [ ] Act/movement breaks identified
- [ ] Turning points marked
- [ ] But/Therefore test applied
- [ ] Structural diagrams included
- [ ] Critical issues prioritized

### P3 Checklist
- [ ] All P2 items
- [ ] Characters fully profiled
- [ ] Dialogue assessed
- [ ] Revision roadmap sequenced
- [ ] Questions for artist formulated

### P4 Checklist
- [ ] Thematic architecture complete
- [ ] At least 3 frameworks applied
- [ ] Historical context provided
- [ ] Citation-ready observations
- [ ] Comparative works analyzed

### P5 Checklist
- [ ] Comparables researched
- [ ] Audience defined
- [ ] Budget tier estimated
- [ ] Platform fit assessed
- [ ] Commercial recommendation clear

### P6 Checklist
- [ ] Mechanisms formally described
- [ ] Pseudocode provided
- [ ] Theoretical correspondence mapped
- [ ] Axioms proposed
- [ ] Formalizability assessed

### P7 Checklist
- [ ] All 8 core documents complete
- [ ] All 9 roles contributed
- [ ] Complete beat map (no gaps)
- [ ] All named characters profiled
- [ ] Supplements as warranted

---

*Protocol Invocation Guide v1.0*
