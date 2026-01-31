FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false

WORKDIR /code

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry через pip — это самый стабильный способ в Docker
RUN pip install --no-cache-dir poetry==2.1.2

# Копируем конфиги и ставим зависимости
COPY pyproject.toml poetry.lock* ./
RUN poetry install -vvv --no-root --only main --no-cache --no-interaction

# Копируем остальной код
COPY . .
