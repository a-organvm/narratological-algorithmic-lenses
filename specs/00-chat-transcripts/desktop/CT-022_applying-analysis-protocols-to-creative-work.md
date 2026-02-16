---
ct_id: CT-022
uuid: 0afc882c-22e5-4c9d-abb9-e3c1731ea49f
title: "Applying analysis protocols to creative work"
created_at: 2026-01-25T21:32:29.597912Z
updated_at: 2026-01-25T21:43:10.751197Z
message_count: 4
tags: [SKILL_CREATION, PROTOCOL_IMPLEMENTATION, ARCHITECTURE]
source: claude-desktop-export
---

# Applying analysis protocols to creative work

**CT-022** | 4 messages | Source: Claude Desktop

---

## Human *(2026-01-25 21:32 UTC)*

design skills to apply the analysis protocols framework to a creative work;

---

## Assistant *(2026-01-25 21:37 UTC)*

Let me also check the skill-creator example to ensure proper skill structure:

Now I have a comprehensive view of your existing framework. Let me design a skill architecture that operationalizes the analysis protocols for creative work.

---

## Skill Architecture Design

### Overview

I recommend a **hub-and-spoke architecture**: one master routing skill plus protocol-specific skills that can be invoked directly or via the router.

```
SKILL_ARCHITECTURE:

┌─────────────────────────────────────────────────────────────────┐
│                    ROUTING LAYER                                │
│                                                                 │
│    creative-analysis/                                           │
│    └── SKILL.md (master router + protocol selection)            │
│                                                                 │
└───────────────────────────────┬─────────────────────────────────┘
                                │
    ┌───────────┬───────────┬───┴───┬───────────┬───────────┬─────┐
    ▼           ▼           ▼       ▼           ▼           ▼     ▼
┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐
│P1-TRIAGE│P2-STRUCT│P3-CRAFT │P4-SCHOLAR│P5-MARKET│P6-EXTRACT│P7-FULL  │
│ skill   │ skill   │ skill   │  skill   │ skill   │  skill   │ skill   │
└────────┘ └────────┘ └────────┘ └────────┘ └────────┘ └────────┘ └────────┘
```

### Rationale

| Approach | Pros | Cons |
|----------|------|------|
| Single monolithic skill | Simpler maintenance | Large context load; poor triggering |
| Separate protocol skills | Precise triggering; minimal context per protocol | More files; coordination needed |
| **Hub + spoke (recommended)** | Best triggering; progressive disclosure; reusable templates | Slightly more complex setup |

---

## Skill Specifications

### 1. Master Router Skill: `creative-analysis`

Now let me create reference materials for the skill package:

## Skill Package Summary

Created an 8-skill architecture implementing your analysis protocols framework:

### Structure

| Skill | Purpose | Triggering |
|-------|---------|------------|
| **creative-analysis** | Master router | Any "analyze creative work" request |
| **protocol-triage** | P1: Gatekeeping decisions | "Worth pursuing?", "Quick read" |
| **protocol-structural** | P2: Architecture diagnosis | "What's broken structurally?" |
| **protocol-craft** | P3: Revision guidance (DEFAULT) | "Give me notes", "How to fix?" |
| **protocol-scholarly** | P4: Academic analysis | "For a paper", "Theoretically" |
| **protocol-market** | P5: Commercial assessment | "Will it sell?" |
| **protocol-extraction** | P6: Mechanism identification | "How does this technique work?" |
| **protocol-comprehensive** | P7: Full analysis | "Everything", "Complete coverage" |

### Key Design Decisions

1. **Hub-and-spoke architecture**: Router skill handles intent parsing; protocol skills are invocable directly or via router
2. **Progressive disclosure**: Each skill loads only what's needed for that protocol depth
3. **Existing project integration**: All skills reference your algorithm documents, templates, and meta-framework
4. **P6 → Algorithm pipeline**: Extraction protocol explicitly feeds the `narratological-algorithms` workflow

### Installation

Move the skill folders to `/mnt/skills/user/` (or your equivalent skill directory). The skills will then trigger on natural language patterns as specified in each `description` field.

---

## Human *(2026-01-25 21:42 UTC)*

Move the skill folders to `/mnt/skills/user/` (or your equivalent skill directory). The skills will then trigger on natural language patterns as specified in each `description` field.

---

## Assistant *(2026-01-25 21:43 UTC)*

Done. All 8 skills are now installed in `/mnt/skills/user/`:

```
/mnt/skills/user/
├── creative-analysis/          (router)
├── protocol-triage/            (P1)
├── protocol-structural/        (P2)
├── protocol-craft/             (P3)
├── protocol-scholarly/         (P4)
├── protocol-market/            (P5)
├── protocol-extraction/        (P6)
└── protocol-comprehensive/     (P7)
```

The skills will now trigger on natural language patterns. Test with requests like:
- "Analyze this script" → router activates, selects protocol
- "Quick read—worth pursuing?" → P1 directly
- "Give me revision notes" → P3 directly
- "How does this showrunner structure episodes?" → P6 directly

---
