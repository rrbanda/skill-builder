FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

LABEL org.opencontainers.image.source="https://github.com/rrbanda/skill-builder"

ARG RELEASE_VERSION="main"

RUN useradd -m -u 1001 appuser

WORKDIR /app

COPY --chown=1001:1001 pyproject.toml uv.lock ./
RUN uv sync --no-cache --locked --link-mode copy --no-install-project

COPY --chown=1001:1001 . .
RUN uv sync --no-cache --locked --link-mode copy

ENV PRODUCTION_MODE=True \
    RELEASE_VERSION=${RELEASE_VERSION} \
    SKILL_BUILDER_HOST=0.0.0.0 \
    SKILL_BUILDER_PORT=8000 \
    SKILL_BUILDER_PROTOCOL=http \
    SKILL_BUILDER_MODEL=openai/gemini/models/gemini-2.5-pro \
    OPENAI_API_BASE=https://llamastack-llamastack.apps.ocp.v7hjl.sandbox2288.opentlc.com/v1 \
    OPENAI_API_KEY=no-key-needed

USER 1001

EXPOSE 8000

CMD ["uv", "run", "--no-sync", "uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8000"]
