# Example SKILL.md Files

These examples demonstrate well-structured skills across different domains.
Use them as templates when generating new skills.

---

## Example 1: Code Review Skill

```markdown
---
name: code-review
description: >-
  Reviews Python code for correctness, style, and performance. Checks for
  common bugs, PEP 8 compliance, type hint coverage, and suggests
  optimizations with severity-based reporting.
---

# Code Review Instructions

When asked to review code, follow this process:

## Step 1: Load Guidelines
Use `load_skill_resource` to read `references/review-checklist.md`.

## Step 2: Analyze the Code
Check the code against each category:
- **Correctness**: Logic errors, edge cases, error handling
- **Style**: PEP 8, naming conventions, docstrings
- **Performance**: Unnecessary loops, N+1 patterns, memory usage
- **Security**: Input validation, injection risks, secret handling
- **Types**: Type hint coverage, correct usage of Optional/Union

## Step 3: Report Findings
Organize findings by severity:
- **Critical**: Bugs or security issues that must be fixed
- **Warning**: Style violations or performance concerns
- **Info**: Suggestions for improvement

For each finding, include:
1. File and line reference
2. What the issue is
3. Why it matters
4. Suggested fix with code
```

---

## Example 2: API Design Skill

```markdown
---
name: api-design-reviewer
description: >-
  Reviews REST API designs for consistency, usability, and adherence to
  best practices. Covers URL structure, HTTP methods, status codes,
  pagination, error responses, and versioning.
---

# API Design Review Instructions

## Step 1: Load Standards
Use `load_skill_resource` to read `references/api-standards.md`.

## Step 2: Review URL Structure
- Resources are nouns, not verbs (`/users` not `/getUsers`)
- Consistent pluralization
- Nesting max 2 levels (`/users/{id}/orders`)
- Query params for filtering, sorting, pagination

## Step 3: Review HTTP Methods
- GET: Read (no side effects)
- POST: Create
- PUT: Full replace
- PATCH: Partial update
- DELETE: Remove

## Step 4: Review Response Format
- Consistent envelope or direct response (pick one)
- Proper status codes (201 for create, 204 for delete)
- Error responses include: code, message, details array
- Pagination: cursor-based preferred over offset

## Step 5: Produce Report
For each endpoint reviewed, provide:
1. Current design
2. Issues found (if any)
3. Recommended design with rationale
```

---

## Example 3: Data Pipeline Skill

```markdown
---
name: data-pipeline-validator
description: >-
  Validates data pipeline configurations for correctness, performance,
  and reliability. Checks schema definitions, transformation logic,
  error handling, idempotency, and monitoring setup.
---

# Data Pipeline Validation

## Step 1: Schema Validation
- All fields have explicit types
- Nullable fields are marked
- Default values are sensible
- Schema evolution strategy exists (backward/forward compatible)

## Step 2: Transformation Logic
- Transformations are idempotent (rerunning produces same result)
- NULL handling is explicit for every field
- Date/time zones are handled consistently
- String encoding is specified (UTF-8)

## Step 3: Error Handling
- Dead letter queue configured for failed records
- Retry policy with exponential backoff
- Circuit breaker for downstream dependencies
- Alerting thresholds defined

## Step 4: Performance
- Partitioning strategy matches query patterns
- Batch sizes are configurable
- Parallelism is bounded
- Backpressure handling exists

## Step 5: Report
Produce a validation report with:
- PASS/WARN/FAIL per category
- Specific issues with line references
- Recommended fixes
```

---

## Example 4: Technical Writing Skill

```markdown
---
name: technical-writer
description: >-
  Writes clear technical documentation including API docs, architecture
  decision records, runbooks, and how-to guides. Follows docs-as-code
  principles with consistent structure and terminology.
---

# Technical Writing Instructions

## Step 1: Identify Document Type
- **API Reference**: Endpoint-by-endpoint with examples
- **ADR**: Context, decision, consequences format
- **Runbook**: Step-by-step with troubleshooting branches
- **How-To**: Task-oriented, single goal, prerequisites listed

## Step 2: Load Style Guide
Use `load_skill_resource` to read `references/style-guide.md`.

## Step 3: Structure the Document
Every document needs:
1. **Title**: Clear, includes the technology or system name
2. **Overview**: One paragraph explaining what and why
3. **Prerequisites**: What the reader needs before starting
4. **Body**: Structured by document type (see Step 1)
5. **Next Steps**: Where to go from here

## Step 4: Write with Clarity
- Use active voice ("Run the command" not "The command should be run")
- One idea per sentence
- Define acronyms on first use
- Code examples must be complete and runnable
- Use consistent terminology (pick one term and stick with it)
```
