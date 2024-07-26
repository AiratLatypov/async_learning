FROM python:3.12
ENV POETRY_VIRTUALENVS_CREATE=false
WORKDIR /app
RUN apt-get update \
    && apt-get install -y curl lsof \
    && pip install poetry==1.8.2
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root
COPY . .
