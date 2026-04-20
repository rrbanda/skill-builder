"""Skill definitions and registry.

Separates skill definitions from agent wiring so they can be tested,
extended, and configured independently.

Patterns used (from the Developer's Guide to Building ADK Agents with Skills):
  - Pattern 1 (Inline): skill-creator, skill-reviewer
  - Pattern 2 (File-based): skill-writing-guide, skill-quality-checklist
  - Pattern 4 (Meta / Factory): skill-creator generates new SKILL.md files
"""

from __future__ import annotations

from pathlib import Path

from google.adk.skills import load_skill_from_dir, models

# ---------------------------------------------------------------------------
# Embedded L3 resources for the meta skill (Pattern 4)
# These are the agentskills.io spec and a minimal example that the
# skill-creator reads via load_skill_resource at runtime.
# ---------------------------------------------------------------------------

_AGENTSKILLS_SPEC = """\
# Agent Skills Specification (agentskills.io)

## SKILL.md Format

Every skill directory must contain a `SKILL.md` file with YAML frontmatter
followed by Markdown instructions.

### Frontmatter (YAML)

```yaml
---
name: my-skill-name          # kebab-case, max 64 chars, required
description: >-              # max 1024 chars, required
  What this skill does. Be specific — this is the L1 metadata
  the LLM uses to decide whether to load the skill.
---
```

### Body (Markdown)

The body contains step-by-step instructions the agent follows when the
skill is activated. Write clear, actionable steps. Use H2 headings for
major steps and H3 for sub-steps.

### Directory Structure

```
my-skill-name/
  SKILL.md           # Required: frontmatter + instructions (L2)
  references/        # Optional: detailed reference docs (L3)
  assets/            # Optional: templates, data files
  scripts/           # Optional: executable scripts
```

### Key Rules

1. Directory name MUST match the `name` field in frontmatter
2. Name must be kebab-case: `^[a-z0-9]+(-[a-z0-9]+)*$`
3. Name max 64 characters
4. Description max 1024 characters
5. Description is what the LLM uses to decide when to load the skill
6. Keep instructions actionable — tell the agent WHAT to do
7. Use `load_skill_resource` to reference files in `references/`
8. Keep SKILL.md body under 500 lines — put details in references/
9. The spec is used by 40+ tools: Cursor, Gemini CLI, Claude Code, ADK, etc.
"""

_EXAMPLE_SKILL = """\
# Example: Dockerfile Optimizer Skill

This is a complete, valid SKILL.md with companion reference file.

## SKILL.md

```markdown
---
name: dockerfile-optimizer
description: >-
  Reviews Dockerfiles for image size, build speed, security, and
  layer caching. Suggests multi-stage builds, pinned versions,
  non-root users, and .dockerignore improvements.
---

# Dockerfile Optimization

When asked to optimize a Dockerfile, follow these steps:

## Step 1: Load Best Practices
Use `load_skill_resource` to read `references/docker-best-practices.md`.

## Step 2: Analyze Image Size
- Check base image choice (alpine vs slim vs full)
- Identify unnecessary packages or files in final image
- Check for multi-stage build opportunities
- Verify .dockerignore exists and covers build artifacts

## Step 3: Analyze Build Speed
- Check layer ordering (least-changing layers first)
- Identify cache-busting operations
- Check for combined RUN statements
- Verify COPY granularity (specific files before directories)

## Step 4: Check Security
- Base image pinned to digest or specific version (not :latest)
- Non-root USER directive present
- No secrets in build args or ENV
- HEALTHCHECK defined

## Step 5: Produce Report
For each finding:
1. Current line or pattern
2. Issue description
3. Suggested fix with corrected Dockerfile snippet
4. Impact: size / speed / security
```

## references/docker-best-practices.md

A separate file with detailed Docker best practices, layer caching
rules, and base image comparison tables. This file would be loaded
only when Step 1 is reached — not on every invocation.
"""


def build_skill_creator() -> models.Skill:
    """Pattern 4: Meta skill that generates new SKILL.md files.

    Embeds the agentskills.io spec and a working example as L3 resources.
    At runtime, the agent reads these via load_skill_resource to understand
    the format before generating a new skill.
    """
    return models.Skill(
        frontmatter=models.Frontmatter(
            name="skill-creator",
            description=(
                "Creates new agentskills.io-compatible skill definitions from"
                " user requirements. Generates complete SKILL.md files with"
                " YAML frontmatter, step-by-step instructions, and optional"
                " reference files. Uses the writing guide and quality checklist"
                " skills to ensure high-quality output."
            ),
        ),
        instructions=(
            "When asked to create a new skill, follow this workflow:\n\n"
            "## Step 1: Understand Requirements\n"
            "Ask clarifying questions if the domain or use case is unclear.\n"
            "Identify: task scope, target user, success criteria, domain knowledge needed.\n\n"
            "## Step 2: Load the Specification\n"
            "Read `references/skill-spec.md` for the agentskills.io format rules.\n"
            "Read `references/example-skill.md` for a working example.\n\n"
            "## Step 3: Load Supporting Skills\n"
            "Load the `skill-writing-guide` skill for writing craft guidance.\n"
            "Use `load_skill_resource` on the writing guide's `references/example-skills.md`"
            " to see diverse skill examples across domains.\n\n"
            "## Step 4: Generate the SKILL.md\n"
            "Follow these rules:\n"
            "1. Name must be kebab-case, max 64 characters\n"
            "2. Description must be under 1024 characters and highly specific\n"
            "3. Instructions must be clear, step-by-step with H2 headings\n"
            "4. Include explicit `load_skill_resource` calls for reference files\n"
            "5. Specify an output format section\n"
            "6. Keep body under 500 lines — put details in references/\n\n"
            "## Step 5: Self-Review\n"
            "Load the `skill-quality-checklist` skill and apply it to your output.\n"
            "Fix any issues before presenting to the user.\n\n"
            "## Step 6: Deliver\n"
            "Present the complete output as fenced markdown code blocks:\n"
            "1. The SKILL.md file content\n"
            "2. Any `references/*.md` file contents (each in its own block)\n"
            "3. A suggested directory structure\n"
            "4. The quality score from the checklist\n"
        ),
        resources=models.Resources(
            references={
                "skill-spec.md": _AGENTSKILLS_SPEC,
                "example-skill.md": _EXAMPLE_SKILL,
            }
        ),
    )


def build_skill_reviewer() -> models.Skill:
    """Pattern 1: Inline skill for validating existing SKILL.md files.

    Standalone validation — users can bring their own SKILL.md for feedback.
    """
    return models.Skill(
        frontmatter=models.Frontmatter(
            name="skill-reviewer",
            description=(
                "Reviews and validates existing SKILL.md files against the"
                " agentskills.io specification. Checks frontmatter format,"
                " instruction quality, progressive disclosure design, and"
                " cross-tool portability. Provides a quality score and"
                " specific improvement suggestions."
            ),
        ),
        instructions=(
            "When asked to review a SKILL.md file, follow this process:\n\n"
            "## Step 1: Parse the Input\n"
            "Extract the YAML frontmatter and markdown body from the provided content.\n"
            "If the input is not a valid SKILL.md, explain the expected format.\n\n"
            "## Step 2: Load Quality Standards\n"
            "Load the `skill-quality-checklist` skill for the validation rubric.\n"
            "Use `load_skill_resource` to read the scoring rubric reference.\n\n"
            "## Step 3: Validate Frontmatter\n"
            "Check:\n"
            "- `name` exists, is kebab-case, max 64 chars\n"
            "- `description` exists, under 1024 chars, is specific\n"
            "- Frontmatter uses `---` delimiters\n\n"
            "## Step 4: Evaluate Instructions\n"
            "Check:\n"
            "- Step-by-step structure with headings\n"
            "- Each step is actionable (not vague)\n"
            "- Output format is specified\n"
            "- Appropriate use of `load_skill_resource` for references\n"
            "- Body under 500 lines\n\n"
            "## Step 5: Score and Report\n"
            "Apply the scoring rubric and produce:\n"
            "1. Overall score (out of 100)\n"
            "2. Category breakdown (Frontmatter, Instructions, Progressive Disclosure, Portability)\n"
            "3. Specific issues with severity (Critical / Warning / Info)\n"
            "4. Suggested improvements with corrected examples\n"
            "5. An improved version of the SKILL.md if score is below 75\n"
        ),
    )


def load_file_based_skills(skills_dir: Path) -> list[models.Skill]:
    """Pattern 2: Load file-based skills from disk.

    Scans the skills directory for subdirectories containing SKILL.md.
    Each directory becomes a skill with L2 instructions and L3 references.
    """
    skills = []
    if not skills_dir.is_dir():
        return skills

    for skill_path in sorted(skills_dir.iterdir()):
        if skill_path.is_dir() and (skill_path / "SKILL.md").exists():
            skills.append(load_skill_from_dir(skill_path))

    return skills


def build_all_skills(skills_dir: Path) -> list[models.Skill]:
    """Assemble all skills from all patterns into a single list.

    Order matters for L1 display: most commonly used skills first.
    """
    return [
        build_skill_creator(),
        build_skill_reviewer(),
        *load_file_based_skills(skills_dir),
    ]
