---
name: protocol-triage
description: Rapid assessment protocol (P1) for creative work gatekeeping decisions. Triggers on "quick read", "worth pursuing", "should I read this", "pass or recommend", "first look", or high-volume evaluation contexts. Produces abbreviated coverage report with RECOMMEND/CONSIDER/PASS decision. Uses FIRST-READER and DRAMATURGIST roles only. Estimated time 30-60 minutes per 100-page script.
---

# P1 â€” TRIAGE Protocol

Rapid assessment for gatekeeping decisions on creative work.

## Configuration

```yaml
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
INGESTION: Single read (engagement-focused)
```

## Ingestion Protocol

1. Read work completely without annotation
2. Note immediate emotional/engagement responses
3. Capture [FIRST-READER] reactions throughout
4. Assess fundamental architecture viability

## Output Template

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

## Decision Criteria

| Recommendation | Criteria |
|----------------|----------|
| RECOMMEND | Compelling premise + functional structure + distinct voice |
| CONSIDER | Strong elements present + addressable weaknesses |
| PASS | Fundamental structural issues OR concept viability problems |

## Escalation Triggers

Upgrade to P2-STRUCTURAL if:
- [ ] Act structure is unclear or unconventional
- [ ] Turning points are missing or misplaced
- [ ] Causal logic fails "but/therefore" test at macro level

## Role-Tag Requirements

- [FIRST-READER]: Minimum 2 engagement observations
- [DRAMATURGIST]: Minimum 2 structural observations
