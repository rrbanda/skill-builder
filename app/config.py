"""Centralized configuration loaded from environment variables.

All settings have sensible defaults and can be overridden via env vars
or a .env file (loaded by python-dotenv in server.py).
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

_SKILLS_DIR = Path(__file__).parent / "skills"


@dataclass(frozen=True, slots=True)
class AgentConfig:
    """Immutable agent configuration."""

    model: str = field(
        default_factory=lambda: os.getenv("SKILL_BUILDER_MODEL", "gemini-2.5-pro")
    )
    agent_name: str = field(
        default_factory=lambda: os.getenv("SKILL_BUILDER_AGENT_NAME", "skill_builder_agent")
    )
    agent_description: str = field(
        default_factory=lambda: os.getenv(
            "SKILL_BUILDER_AGENT_DESCRIPTION",
            (
                "Builds agentskills.io-compatible SKILL.md files for any domain."
                " Uses its own skills to craft high-quality, spec-compliant"
                " agent skills with progressive disclosure."
            ),
        )
    )
    skills_dir: Path = field(
        default_factory=lambda: Path(os.getenv("SKILL_BUILDER_SKILLS_DIR", str(_SKILLS_DIR)))
    )


@dataclass(frozen=True, slots=True)
class ServerConfig:
    """Immutable A2A server configuration."""

    host: str = field(
        default_factory=lambda: os.getenv("SKILL_BUILDER_HOST", "0.0.0.0")
    )
    port: int = field(
        default_factory=lambda: int(os.getenv("SKILL_BUILDER_PORT", "8000"))
    )
    protocol: str = field(
        default_factory=lambda: os.getenv("SKILL_BUILDER_PROTOCOL", "http")
    )


def load_agent_config() -> AgentConfig:
    return AgentConfig()


def load_server_config() -> ServerConfig:
    return ServerConfig()
