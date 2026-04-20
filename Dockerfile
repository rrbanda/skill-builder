FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

ARG RELEASE_VERSION="main"

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --no-cache --locked --link-mode copy --no-install-project

COPY . .
RUN uv sync --no-cache --locked --link-mode copy

ENV PRODUCTION_MODE=True \
    RELEASE_VERSION=${RELEASE_VERSION} \
    SKILL_BUILDER_HOST=0.0.0.0 \
    SKILL_BUILDER_PORT=8000 \
    SKILL_BUILDER_PROTOCOL=http

RUN chown -R 1001:1001 /app
USER 1001

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/.well-known/agent-card.json')" || exit 1

CMD ["uv", "run", "--no-sync", "uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8000"]
