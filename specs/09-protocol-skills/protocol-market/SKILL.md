---
name: protocol-market
description: Commercial viability assessment protocol (P5) for creative work. Triggers on "will this sell", "commercial potential", "market assessment", "audience", "budget", "castability", "production feasibility", "pitch deck", "packaging". Produces Coverage Report (market-focused), Market Positioning Analysis, Comparable Titles Analysis, and Production Feasibility Assessment. Uses PRODUCER as primary role. Estimated time 3-4 hours per 100-page script.
---

# P5 â€” MARKET Protocol

Commercial viability assessment for creative work.

## Configuration

```yaml
ROLES_ACTIVE:
  PRIMARY:   [PRODUCER]
  SECONDARY: [FIRST-READER, CINEPHILE, DRAMATURGIST]
  INACTIVE:  [AESTHETE, NARRATOLOGIST, ART_HIST, RHETORICIAN, ACADEMIC]

DOCUMENTS:
  GENERATE:  [Coverage Report (market-focused), Market Positioning,
              Comparable Titles Analysis, Production Feasibility]
  EXCLUDE:   [Beat Map, Structural Analysis, Character Atlas,
              Thematic Architecture, Diagnostic Report,
              Theoretical Correspondence, Revision Roadmap]

DEPTH: Medium (commercial focus)
INGESTION: Two reads (engagement + commercial lens)
```

## Ingestion Protocol

### Read 1: Audience Response
- [FIRST-READER]: General audience appeal
- Where does engagement hold for mainstream viewer?

### Read 2: Commercial Lens
- [PRODUCER]: Production considerations
- [CINEPHILE]: Market positioning

## Core Deliverables

### 1. Market Positioning Analysis (Required)

```markdown
## Market Positioning

### Genre Classification
**Primary**: [Genre]
**Secondary**: [Subgenre/hybrid elements]
**Tone**: [Descriptor]

### Target Audience

| Quadrant | Fit | Notes |
|----------|-----|-------|
| Male <25 | â—‹â—‹â—‹â—‹â—‹ | |
| Male 25+ | â—‹â—‹â—‹â—‹â—‹ | |
| Female <25 | â—‹â—‹â—‹â—‹â—‹ | |
| Female 25+ | â—‹â—‹â—‹â—‹â—‹ | |

### Platform Fit

| Platform | Fit | Rationale |
|----------|-----|-----------|
| Theatrical (Major) | â—‹â—‹â—‹â—‹â—‹ | |
| Theatrical (Limited) | â—‹â—‹â—‹â—‹â—‹ | |
| Streaming (Premium) | â—‹â—‹â—‹â—‹â—‹ | |
| Streaming (General) | â—‹â—‹â—‹â—‹â—‹ | |
| Cable/Network | â—‹â—‹â—‹â—‹â—‹ | |

### Unique Selling Proposition
[1-2 sentences: What makes this marketable?]

### Commercial Challenges
[1-2 sentences: What makes this a tough sell?]
```

### 2. Comparable Titles Analysis (Required)

```markdown
## Comparable Titles

| Title | Year | Box Office/Viewership | Relevance |
|-------|------|----------------------|-----------|
| [X] | [Y] | [Z] | [Why comparable] |

### Lessons from Comparables

**[Title 1]** succeeded because: [X]
- This project shares: [Y]
- This project differs: [Z]

**[Title 2]** underperformed because: [X]
- Risk for this project: [Y]
- Mitigation: [Z]
```

### 3. Production Feasibility (Required)

```markdown
## Production Feasibility

### Budget Tier Estimate

| Tier | Range | Fit | Notes |
|------|-------|-----|-------|
| Micro (<$1M) | | â—‹â—‹â—‹â—‹â—‹ | |
| Low ($1-10M) | | â—‹â—‹â—‹â—‹â—‹ | |
| Mid ($10-50M) | | â—‹â—‹â—‹â—‹â—‹ | |
| High ($50-100M) | | â—‹â—‹â—‹â—‹â—‹ | |
| Tentpole (>$100M) | | â—‹â—‹â—‹â—‹â—‹ | |

### Production Considerations

| Element | Assessment | Impact |
|---------|------------|--------|
| Location requirements | [X] | $/Schedule |
| VFX/SFX needs | [X] | $/Quality |
| Period/futuristic elements | [X] | $/Quality |
| Stunt/action complexity | [X] | $/Safety |
| Cast size | [X] | $/Scheduling |

### Castability Assessment

**Lead Roles**:
| Role | Type | Castability | Notes |
|------|------|-------------|-------|
| [X] | [Archetype] | â—‹â—‹â—‹â—‹â—‹ | [Star vehicle? Character role?] |

**Attachable Elements**:
- [ ] Star-vehicle lead role
- [ ] Ensemble with multiple hooks
- [ ] Director-driven material
- [ ] High-concept premise (sells itself)
```

### 4. Go/No-Go Recommendation

```markdown
## Commercial Recommendation

**Verdict**: [ ] GREEN LIGHT  [ ] DEVELOP FURTHER  [ ] PASS

### Strengths (Commercial)
1. [X]
2. [X]

### Weaknesses (Commercial)
1. [X]
2. [X]

### Recommended Path
[Specific next steps for commercial development]
```

## Commercial Assessment Criteria

| Factor | Weight | Assessment Questions |
|--------|--------|----------------------|
| Concept clarity | High | Can it be pitched in one sentence? |
| Genre viability | High | Is this genre performing currently? |
| Budget/scope alignment | High | Can it be made for appropriate budget? |
| Castability | Medium | Roles actors want to play? |
| Timeliness | Medium | Cultural moment alignment? |
| Franchise potential | Low-Medium | Sequel/universe possibilities? |
