FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV HOST=0.0.0.0
ENV PORT=9471
ENV TRINI_RECALL_DB_PATH=/data/trini_recall_chat_memory.sqlite3
ENV TRINI_RECALL_JSONL_PATH=/data/trini_recall_chat_memory.jsonl

WORKDIR /app

COPY pyproject.toml README.md LICENSE ./
COPY src ./src
COPY scripts ./scripts
COPY static ./static
COPY docs ./docs
COPY datasets ./datasets

RUN python -m pip install --no-cache-dir --upgrade pip \
    && python -m pip install --no-cache-dir -e .

RUN mkdir -p /data

EXPOSE 9471

CMD ["python", "scripts/run_trini_recall_ui.py", "--host", "0.0.0.0", "--port", "9471"]
