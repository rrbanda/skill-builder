---
name: skill-quality-checklist
description: >-
  Validates and scores SKILL.md files against the agentskills.io specification.
  Checks frontmatter validity, instruction clarity, progressive disclosure
  design, reference organization, and cross-tool portability. Load this skill
  to review or improve a generated or user-provided skill.
---

# Skill Quality Checklist

Use this checklist to validate a SKILL.md file before it is delivered to
the user. This can be applied to skills you generate or to skills the user
asks you to review.

## Step 1: Frontmatter Validation

Check the YAML frontmatter block:

- [ ] `name` field exists and is kebab-case
- [ ] `name` matches pattern `^[a-z0-9]+(-[a-z0-9]+)*$`
- [ ] `name` is max 64 characters
- [ ] `description` field exists
- [ ] `description` is under 1024 characters
- [ ] `description` is specific enough to distinguish from similar skills
- [ ] `description` mentions key capabilities (not just the domain)
- [ ] Frontmatter uses `---` delimiters

## Step 2: Instruction Quality

Evaluate the markdown body:

- [ ] Instructions are step-by-step (numbered or with H2 headings)
- [ ] Each step is actionable (tells the agent *what* to do)
- [ ] No ambiguous instructions ("review carefully" without criteria)
- [ ] Output format is specified (what should the agent produce?)
- [ ] Total body is under 500 lines
- [ ] No tool-specific assumptions (works in Cursor, Gemini CLI, etc.)

## Step 3: Progressive Disclosure

Check L2/L3 separation:

- [ ] Core workflow is in the SKILL.md body (L2)
- [ ] Detailed domain knowledge is in `references/` files (L3)
- [ ] `load_skill_resource` calls are explicit where references are needed
- [ ] References are loaded conditionally, not unconditionally
- [ ] Each reference file is focused on one topic

## Step 4: Directory Structure

If the skill has companion files:

- [ ] Directory name matches the `name` field exactly
- [ ] `references/` contains only `.md` files with clear names
- [ ] No binary files or executables in the skill directory
- [ ] Reference files are self-contained (don't require other references)

## Step 5: Scoring

Use `load_skill_resource` to read `references/scoring-rubric.md` for the
detailed point-based scoring system.

Apply the rubric and report:
1. Total score (out of 100)
2. Category breakdown
3. Specific issues found
4. Suggested improvements with examples
