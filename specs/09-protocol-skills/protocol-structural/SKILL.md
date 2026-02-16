---
name: protocol-structural
description: Architecture diagnosis protocol (P2) for creative work requiring structural overhaul. Triggers on "structure", "architecture", "act breakdown", "what's broken structurally", "macro-level problems", "rewrite planning". Produces Coverage Report, Structural Analysis, and Diagnostic Report. Uses DRAMATURGIST and NARRATOLOGIST as primary roles. Estimated time 2-3 hours per 100-page script.
---

# P2 â€” STRUCTURAL Protocol

Architecture diagnosis for active revision of creative work.

## Configuration

```yaml
ROLES_ACTIVE:
  PRIMARY:   [DRAMATURGIST, NARRATOLOGIST]
  SECONDARY: [FIRST-READER, CINEPHILE]
  INACTIVE:  [AESTHETE, ART_HIST, RHETORICIAN, PRODUCER, ACADEMIC]

DOCUMENTS:
  GENERATE:  [Coverage Report, Structural Analysis, Diagnostic Report]
  EXCLUDE:   [Beat Map (full), Character Atlas, Thematic Architecture,
              Theoretical Correspondence, Revision Roadmap]

DEPTH: Medium
INGESTION: Two reads (engagement + structural)
```

## Ingestion Protocol

### Read 1: Engagement
- Note where attention holds/flags
- Capture [FIRST-READER] reactions

### Read 2: Structural
- Identify act breaks (even if unconventional)
- Mark turning points and structural nodes
- Map temporal structure and time span

## Diagnostic Tests (Required)

Apply these formal tests and document results:

### Test 1: South Park But/Therefore

```
For each act transition:
  IF connection = "AND THEN" â†’ FLAG: Episodic structure
  IF connection = "BUT" or "THEREFORE" â†’ PASS: Causal binding present
```

### Test 2: McKee Progressive Complications

```
For each act:
  complications[n] > complications[n-1]? 
  IF false â†’ FLAG: Stakes not escalating
```

### Test 3: Turning Point Placement

| Node | Expected Position | Tolerance |
|------|-------------------|-----------|
| Inciting Incident | 10-15% | Â±5% |
| End Act I | 20-25% | Â±5% |
| Midpoint | 45-55% | Â±5% |
| End Act II | 75-80% | Â±5% |
| Climax | 85-95% | Â±5% |

### Test 4: Act Proportion

```
Standard: 25% / 50% / 25%
Acceptable variance: Â±10%
```

## Output: Structural Diagram

Generate ASCII architecture visualization:

```
ACT I          â”‚ ACT II                      â”‚ ACT III
               â”‚                             â”‚
    â•±â•²         â”‚         â•±â•²                  â”‚    â•±â•²
   â•±  â•²        â”‚        â•±  â•²                 â”‚   â•±  â•²
  â•±    â•²       â”‚       â•±    â•²    â•±â•²          â”‚  â•±    â•²
 â•±      â•²      â”‚      â•±      â•²  â•±  â•²         â”‚ â•±      â•²
â•±        â•²     â”‚     â•±        â•²â•±    â•²        â”‚â•±        â•²
â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â–ºâ”‚â—„â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â–ºâ”‚â”€â”€â”€â”€â”€â”€â”€â”€â”€â–º
Hook    Incitingâ”‚     Midpoint    Crisis      â”‚ Climax  Resolution
        Incidentâ”‚                             â”‚
```

## Comparable Works Section

[CINEPHILE] must provide 2-3 structural comparisons:
- Similar structural approach that succeeds
- Similar structural approach that fails
- Alternative structural model to consider

## Escalation Triggers

Upgrade to P3-CRAFT if:
- [ ] Character arcs are the primary structural issue
- [ ] Dialogue problems compound structural weakness
- [ ] Writer needs revision roadmap, not just diagnosis
