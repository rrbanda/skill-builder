---
name: skill-writing-guide
description: >-
  Expert guidance for writing high-quality SKILL.md files. Covers instruction
  structure, progressive disclosure design, reference file organization, and
  writing craft. Load this skill when creating or improving agent skills.
---

# Skill Writing Guide

When creating a new SKILL.md, follow this methodology to produce clear,
effective agent skills that work across any agentskills.io-compatible tool.

## Step 1: Understand the Domain

Before writing, clarify:
- What specific task does this skill enable?
- Who is the target user triggering this skill?
- What does "done well" look like for this task?
- What domain knowledge is required that the LLM might not have?

## Step 2: Design the Progressive Disclosure Layers

Decide what belongs at each level:

- **L1 (Frontmatter description)**: A single sentence that tells the LLM
  *when* to activate this skill. Be specific — "Reviews Python code for
  security vulnerabilities including injection, auth, and crypto issues"
  is better than "Reviews code."
- **L2 (Instructions body)**: Step-by-step workflow the agent follows.
  Keep under 500 lines. Should be actionable without loading references.
- **L3 (References)**: Detailed domain knowledge, checklists, specs, or
  examples that are too long for the body. Load on demand via
  `load_skill_resource`.

## Step 3: Write the Frontmatter

```yaml
---
name: kebab-case-name
description: >-
  Concise, specific description under 1024 characters. This is
  what the LLM reads at L1 to decide if this skill is relevant.
---
```

Rules:
- Name: kebab-case, max 64 characters, pattern `^[a-z0-9]+(-[a-z0-9]+)*$`
- Description: Under 1024 characters, specific enough to distinguish from
  other skills, includes key capabilities

## Step 4: Structure the Instructions

Use this template:

1. **Context section**: Brief statement of what this skill does
2. **Step-by-step workflow**: Numbered steps with H2 headings
3. **Reference loading**: Explicit `load_skill_resource` calls where needed
4. **Output format**: Specify exactly what the agent should produce

Read `references/example-skills.md` for complete examples across domains.
Read `references/anti-patterns.md` to avoid common mistakes.

## Step 5: Organize References

Create `references/` files for:
- Domain-specific checklists or rubrics
- API specifications or format definitions
- Style guides or compliance rules
- Detailed examples that would bloat the main instructions

Each reference file should be self-contained and focused on one topic.

## Step 6: Validate

Before finalizing, check:
- Can the agent follow the instructions without ambiguity?
- Are reference files loaded only when needed (not always)?
- Is the description specific enough for accurate L1 matching?
- Would this skill work in Cursor, Gemini CLI, and Claude Code?
