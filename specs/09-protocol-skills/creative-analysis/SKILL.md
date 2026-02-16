---
name: creative-analysis
description: Route creative work (scripts, narratives, stories, films, games) to appropriate analysis protocols. Triggers on requests involving script analysis, narrative breakdown, story feedback, creative work evaluation, structural diagnosis, algorithm extraction, or any variation of "analyze this [creative work]". Selects protocol based on user intent: triage (P1), structural diagnosis (P2), craft revision (P3), scholarly analysis (P4), market assessment (P5), mechanism extraction (P6), or comprehensive analysis (P7). Default to P3 (Craft) for revision-oriented requests.
---

# Creative Analysis Protocol Router

Systematic selection and invocation of narratological analysis protocols for creative work.

## Protocol Selection Logic

### Quick Selection

| User Intent | Protocol | Time |
|-------------|----------|------|
| "Worth pursuing?" / "Should I read this?" | P1-TRIAGE | 30-60 min |
| "What's structurally broken?" | P2-STRUCTURAL | 2-3 hrs |
| "How do I fix this?" / "Give me notes" | P3-CRAFT | 4-5 hrs |
| "Analyze this theoretically" / "For a paper" | P4-SCHOLARLY | 6-8 hrs |
| "Will this sell?" / "Commercial potential?" | P5-MARKET | 3-4 hrs |
| "How does this technique work?" | P6-EXTRACTION | 4-6 hrs |
| "Full analysis" / "Everything" | P7-COMPREHENSIVE | 8-12 hrs |

### Decision Tree

```
START
  â”‚
  â”œâ”€ Is this a gatekeeping decision? â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â–º P1-TRIAGE
  â”‚
  â”œâ”€ Is the focus commercial viability? â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â–º P5-MARKET
  â”‚
  â”œâ”€ Is this for academic/scholarly output? â”€â”€â”€â”€â”€â”€â”€â–º P4-SCHOLARLY
  â”‚
  â”œâ”€ Is the goal to extract technique/mechanism? â”€â”€â–º P6-EXTRACTION
  â”‚
  â”œâ”€ Is comprehensive documentation needed? â”€â”€â”€â”€â”€â”€â”€â–º P7-COMPREHENSIVE
  â”‚
  â”œâ”€ Is this a structural overhaul (pre-polish)? â”€â”€â–º P2-STRUCTURAL
  â”‚
  â””â”€ Is this revision guidance for a working draft?â–º P3-CRAFT (DEFAULT)
```

### Trigger Patterns

| Pattern | Maps To |
|---------|---------|
| "quick read", "first look", "recommend or pass" | P1 |
| "structure", "architecture", "act breakdown" | P2 |
| "revision", "notes", "feedback", "fix" | P3 |
| "academic", "paper", "theory", "framework" | P4 |
| "market", "sell", "commercial", "audience" | P5 |
| "technique", "mechanism", "algorithm", "how does X work" | P6 |
| "full", "comprehensive", "everything" | P7 |

## Protocol Invocation

After selecting protocol, invoke corresponding skill:

- **P1**: Load `protocol-triage/SKILL.md`
- **P2**: Load `protocol-structural/SKILL.md`
- **P3**: Load `protocol-craft/SKILL.md`
- **P4**: Load `protocol-scholarly/SKILL.md`
- **P5**: Load `protocol-market/SKILL.md`
- **P6**: Load `protocol-extraction/SKILL.md`
- **P7**: Load `protocol-comprehensive/SKILL.md`

## Escalation Rules

Monitor for triggers requiring protocol upgrade:

| During | If You Find | Escalate To |
|--------|-------------|-------------|
| P1 | Fundamental structural issues | P2 |
| P2 | Character-driven problems | P3 |
| P3 | Needs theoretical framing | Add P4 elements |
| Any | Commercial questions arise | Add P5 supplement |
| Any | Mechanism worth formalizing | Add P6 extraction |

## Output Confirmation

Always confirm protocol selection with user before proceeding:

```
Selected: P[#] â€” [PROTOCOL NAME]

This will produce:
- [Document 1]
- [Document 2]
- ...

Estimated time: [X] hours
Proceed? [Y/n]
```

## Cross-References

- Templates: `/mnt/project/coverage-template.md`, `/mnt/project/beat-map-template.md`, etc.
- Algorithms: `/mnt/project/mckee_narratological_algorithms_complete.md`, etc.
- Meta-framework: `/mnt/project/attention_mechanics_meta_principles.md`
