# Skill Authoring Anti-Patterns

Avoid these common mistakes when writing SKILL.md files.

---

## 1. Vague Descriptions

**Bad**: "A helpful skill for reviewing things."
**Good**: "Reviews Python code for security vulnerabilities including SQL
injection, authentication bypass, insecure deserialization, and weak
cryptography. Reports findings by OWASP severity."

The description is the L1 metadata the LLM uses to decide whether to load
a skill. Vague descriptions cause false positives (skill loaded when not
needed) or false negatives (skill not loaded when it should be).

## 2. Monolithic Instructions

**Bad**: Cramming 2000 lines of checklists, examples, and rules into the
SKILL.md body.

**Good**: Keep instructions under 500 lines. Move detailed checklists,
examples, and domain knowledge into `references/` files. The agent loads
them via `load_skill_resource` only when needed.

## 3. Missing Actionable Steps

**Bad**: "Review the code and provide feedback."

**Good**:
```
## Step 1: Check Input Validation
For every user-facing input, verify:
- Input is validated before use
- Validation rejects unexpected types
- Length limits are enforced
```

Always tell the agent *what* to check and *how* to report it.

## 4. Hardcoded Tool Assumptions

**Bad**: "Open the file in VS Code and run the linter."

**Good**: Write instructions that are tool-agnostic. The agentskills.io
spec is used by 40+ tools. Your skill should work in Cursor, Gemini CLI,
Claude Code, and any ADK agent.

## 5. No Output Format

**Bad**: Instructions that never specify what the agent should produce.

**Good**: Always include an output format section:
```
## Output Format
Produce a markdown report with:
- Summary (2-3 sentences)
- Findings table (severity, location, description, fix)
- Recommended next steps
```

## 6. Overly Broad Scope

**Bad**: A single skill that handles "all DevOps tasks."

**Good**: One skill per focused capability. Break large domains into
multiple skills:
- `k8s-manifest-reviewer` (not "devops-helper")
- `dockerfile-optimizer` (not "container-skill")
- `ci-pipeline-validator` (not "automation-skill")

## 7. Ignoring Progressive Disclosure

**Bad**: Loading all references unconditionally in every step.

**Good**: Load references only when the current step requires them:
```
## Step 3: Check Security (if applicable)
If the code handles user input, authentication, or sensitive data,
use `load_skill_resource` to read `references/security-checklist.md`.
```

## 8. Missing Directory Name Match

**Bad**: Directory named `my_skill/` with frontmatter `name: my-skill`.

**Good**: Directory name MUST exactly match the `name` field:
`my-skill/SKILL.md` with `name: my-skill`.
