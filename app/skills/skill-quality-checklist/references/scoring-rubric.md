# Skill Quality Scoring Rubric

Score each category and sum for a total out of 100.

---

## Category 1: Frontmatter (20 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| Name format | 5 | Valid kebab-case, under 64 chars |
| Description quality | 10 | Specific, actionable, under 1024 chars |
| Description differentiation | 5 | Clearly distinguishable from similar skills |

**Deductions**:
- Missing name or description: -20 (automatic fail)
- Name not kebab-case: -5
- Description over 1024 chars: -3
- Vague description ("A helpful skill"): -8

---

## Category 2: Instructions (35 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| Step-by-step structure | 10 | Clear numbered steps or H2 sections |
| Actionability | 10 | Each step tells the agent exactly what to do |
| Output specification | 10 | Defines what the agent should produce |
| Brevity | 5 | Under 500 lines, no redundancy |

**Deductions**:
- No clear steps: -10
- Ambiguous instructions: -5 per instance
- No output format: -10
- Over 500 lines without references: -5

---

## Category 3: Progressive Disclosure (25 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| L2/L3 separation | 10 | Core workflow in body, details in references |
| Conditional loading | 8 | References loaded only when needed |
| Reference focus | 7 | Each reference covers one topic |

**Deductions**:
- All content in body with no references for complex skills: -10
- Unconditional reference loading: -5
- References that depend on other references: -3

---

## Category 4: Portability (20 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| Tool-agnostic | 10 | No assumptions about specific IDE or tool |
| Spec compliance | 5 | Follows agentskills.io spec exactly |
| Directory structure | 5 | Correct naming, clean layout |

**Deductions**:
- Tool-specific instructions: -5 per instance
- Directory name mismatch: -5
- Non-markdown files in references: -3

---

## Score Interpretation

| Score | Rating | Meaning |
|-------|--------|---------|
| 90-100 | Excellent | Production-ready, no changes needed |
| 75-89 | Good | Minor improvements suggested |
| 60-74 | Acceptable | Several issues to address |
| 40-59 | Needs Work | Significant improvements required |
| 0-39 | Poor | Major restructuring needed |
