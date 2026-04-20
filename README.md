# Skill Builder Agent

An ADK agent that **uses skills to build skills**. It generates [agentskills.io](https://agentskills.io)-compatible `SKILL.md` files for any domain, exposed via the [A2A protocol](https://google.github.io/A2A) for deployment on [Kagenti](https://github.com/kagenti/kagenti).

Built using all four skill patterns from [Developer's Guide to Building ADK Agents with Skills](https://developers.googleblog.com/developers-guide-to-building-adk-agents-with-skills/).

## How It Works

The agent composes multiple skills together when building a new skill:

1. **skill-creator** (Pattern 4 — Meta Skill): The factory. Embeds the agentskills.io spec as L3 resources and orchestrates the full generation workflow.
2. **skill-reviewer** (Pattern 1 — Inline): Validates existing SKILL.md files against the spec.
3. **skill-writing-guide** (Pattern 2 — File-based): Writing craft guidance with diverse example skills as L3 references.
4. **skill-quality-checklist** (Pattern 2 — File-based): Quality rubric with point-based scoring as L3 references.

When asked to create a skill, the agent loads the creator, reads the spec, loads the writing guide for craft, generates the output, then loads the quality checklist to self-review — all through progressive disclosure (L1/L2/L3).

## Prerequisites

- Python 3.11+
- [Google ADK](https://adk.dev) (`pip install google-adk`)
- A [Google API key](https://aistudio.google.com/apikey)

## Quick Start

```bash
# Set up environment
python3 -m venv .venv && source .venv/bin/activate
pip install -e .

# Configure API key
cp .env.example .env
# Edit .env with your GOOGLE_API_KEY

# Run with ADK Web UI (for development)
adk web

# Or run as A2A server
uvicorn app.server:app --host 0.0.0.0 --port 8000
```

## Try It

| Query | What It Demonstrates |
|-------|---------------------|
| "Create a skill for reviewing Kubernetes manifests for security" | Full workflow: creator + writing guide + quality checklist composed together |
| "I have a SKILL.md, can you review it?" (paste content) | Reviewer skill with quality scoring |
| "Create a simple skill for git commit message formatting" | Lighter workflow: creator loads minimal supporting skills |
| "What skills do you have available?" | Progressive disclosure: agent lists L1 metadata for all 4 skills |

## Configuration

All settings are configurable via environment variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `GOOGLE_API_KEY` | (required) | Google API key for Gemini |
| `SKILL_BUILDER_MODEL` | `gemini-2.5-pro` | LLM model to use |
| `SKILL_BUILDER_HOST` | `0.0.0.0` | A2A server host |
| `SKILL_BUILDER_PORT` | `8000` | A2A server port |
| `SKILL_BUILDER_PROTOCOL` | `http` | A2A server protocol |
| `SKILL_BUILDER_AGENT_NAME` | `skill_builder_agent` | Agent name in A2A card |
| `SKILL_BUILDER_AGENT_DESCRIPTION` | (see .env.example) | Agent description in A2A card |
| `SKILL_BUILDER_SKILLS_DIR` | `app/skills` | Path to file-based skills directory |

## Project Structure

```
skill-builder/
├── app/
│   ├── __init__.py
│   ├── agent.py                          # Root agent assembly
│   ├── config.py                         # Environment-based configuration
│   ├── server.py                         # A2A server (to_a2a + uvicorn)
│   ├── skills_registry.py               # Skill definitions (all 4 patterns)
│   └── skills/
│       ├── skill-writing-guide/          # Pattern 2: File-based
│       │   ├── SKILL.md
│       │   └── references/
│       │       ├── example-skills.md
│       │       └── anti-patterns.md
│       └── skill-quality-checklist/      # Pattern 2: File-based
│           ├── SKILL.md
│           └── references/
│               └── scoring-rubric.md
├── Dockerfile
├── pyproject.toml
├── .env.example
└── README.md
```

## A2A Endpoints

When running as an A2A server:

- `GET /.well-known/agent-card.json` — Agent discovery
- `POST /` — A2A JSON-RPC (`message/send`, `message/stream`)

## Kagenti Deployment

Deploy via the Kagenti UI:

1. Push code to a GitHub repository
2. Log in to Kagenti UI
3. Navigate to "Import New Agent"
4. Select "Build from source", provide the GitHub URL
5. Set `GOOGLE_API_KEY` via Kubernetes secret reference
6. The agent exposes `/.well-known/agent-card.json` for auto-discovery
