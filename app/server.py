"""A2A server entry point.

Converts the skill-builder ADK agent into a Starlette ASGI application
that exposes:
  - GET  /.well-known/agent-card.json  (A2A agent discovery)
  - POST /                             (A2A JSON-RPC: message/send, message/stream)

Run with:
    uvicorn app.server:app --host 0.0.0.0 --port 8000

Or directly:
    python -m app.server
"""

from __future__ import annotations

import logging

from dotenv import load_dotenv

load_dotenv()

from google.adk.a2a.utils.agent_to_a2a import to_a2a  # noqa: E402

from .agent import root_agent  # noqa: E402
from .config import load_server_config  # noqa: E402

logger = logging.getLogger(__name__)

_server_config = load_server_config()

app = to_a2a(
    root_agent,
    host=_server_config.host,
    port=_server_config.port,
    protocol=_server_config.protocol,
)


def main() -> None:
    """Run the server directly with uvicorn."""
    import uvicorn

    logger.info(
        "Starting skill-builder A2A server on %s:%d",
        _server_config.host,
        _server_config.port,
    )
    uvicorn.run(
        app,
        host=_server_config.host,
        port=_server_config.port,
    )


if __name__ == "__main__":
    main()
