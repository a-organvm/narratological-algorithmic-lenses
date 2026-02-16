---
ct_id: CT-021
uuid: beff0b1b-606f-4aa2-a85d-5ac1ddce5435
title: "Designing multi-lens protocols for project review"
created_at: 2026-01-25T10:03:33.216422Z
updated_at: 2026-01-25T10:21:38.789956Z
message_count: 4
tags: [PROTOCOL_DESIGN, METHODOLOGY, FRAMEWORK]
source: claude-desktop-export
---

# Designing multi-lens protocols for project review

**CT-021** | 4 messages | Source: Claude Desktop

---

## Human *(2026-01-25 10:03 UTC)*

review the entire project (chats & files) & design a series of differing protocols in which to apply the different lenses & the documents they produce;

---

## Assistant *(2026-01-25 10:10 UTC)*

I'll conduct a comprehensive review of your project files and chat history to understand the full scope of your narratological algorithms work, then design differentiated protocols for applying the various analytical lenses.

Now I have a comprehensive view of the project's scope. Let me synthesize this into a differentiated protocol system.

Based on my review, I'll design a series of distinct analysis protocols that apply different combinations of the nine analytical roles and produce different document sets, each optimized for specific use cases. I'll create this as a comprehensive framework document.

Now let me create the protocol-specific document templates that don't exist in the current system:

## Summary: Analysis Protocols Framework

I've designed a differentiated protocol system based on comprehensive review of your project files (31 documents) and 18 conversation threads. The system defines **seven distinct protocols** that apply different configurations of your nine analytical roles and produce different document sets.

---

### Protocol Taxonomy

| Protocol | Name | Purpose | Roles | Documents | Time |
|----------|------|---------|-------|-----------|------|
| **P1** | TRIAGE | Rapid pass/consider/recommend | 2 | 1 | 30-60 min |
| **P2** | STRUCTURAL | Architecture diagnosis | 4 | 3 | 2-3 hrs |
| **P3** | CRAFT | Practical revision guidance | 5 | 5 | 4-5 hrs |
| **P4** | SCHOLARLY | Academic/theoretical analysis | 5 | 4+ | 6-8 hrs |
| **P5** | MARKET | Commercial viability | 4 | 4 | 3-4 hrs |
| **P6** | EXTRACTION | Mechanism identification (algorithm building) | 4 | 3 | 4-6 hrs |
| **P7** | COMPREHENSIVE | Full 8-document treatment (existing SKILL.md) | 9 | 8+ | 8-12 hrs |

---

### Key Design Decisions

1. **Composability**: Protocols build on each other—P7 encompasses all others; lighter protocols can escalate to heavier ones without repeating work.

2. **Role Selectivity**: Each protocol activates only relevant roles (e.g., P5-Market activates PRODUCER and CINEPHILE but not ACADEMIC or ART_HIST).

3. **Document Specificity**: New protocol-specific templates created for:
   - Triage Report (P1)
   - Market Positioning Report (P5)
   - Mechanism Extraction Report (P6)

4. **Integration**: P6-EXTRACTION feeds directly into your `narratological-algorithms` skill workflow for building new algorithm documents.

---

### Documents Delivered

| Document | Contents |
|----------|----------|
| **analysis_protocols_framework.md** | Full protocol taxonomy, role activation matrices, document generation rules, selection logic, cross-protocol integration |
| **protocol_specific_templates.md** | Templates for Triage Report, Market Positioning, Mechanism Extraction, and abbreviated Coverage variants |
| **protocol_invocation_guide.md** | Practical invocation syntax, full workflow specifications for each protocol, worked examples, escalation paths, quality checklists |

---

### Relationship to Existing Project

```
INTEGRATION_MAP:

  SKILL.md (existing)           →  P7 = Full activation of existing skill
  SKILL-preview.md (existing)   →  P6 outputs feed algorithm extraction workflow
  Attention Mechanics           →  Applied in P2-P7 diagnostics
  Individual algorithms         →  Applied as framework sources in P2-P7
  Templates (existing)          →  Reused with protocol-specific variants
```

These protocols provide structured differentiation while maintaining compatibility with your existing infrastructure.

---

## Human *(2026-01-25 10:20 UTC)*

now provide me a simple ai-prompt to signify the want for these processes to be applied to a creative work

---

## Assistant *(2026-01-25 10:21 UTC)*

## Invocation Prompts

**Minimal (single line):**
```
Protocol P[#] on [attached work]
```

**Standard:**
```
Apply narratological analysis framework.
Protocol: P3 (Craft)
```

**Natural language triggers:**

| Phrase | Protocol |
|--------|----------|
| "Worth pursuing?" | P1 |
| "What's broken?" | P2 |
| "Revision notes" | P3 |
| "Theoretical analysis" | P4 |
| "Will this sell?" | P5 |
| "How does this work?" | P6 |
| "Full analysis" | P7 |

The document includes an embeddable system instruction block if you want to bake this into project instructions permanently.

---
