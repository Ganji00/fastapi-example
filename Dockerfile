FROM python:3.12.3-alpine

LABEL maintainer="Mateusz Kiersnowski <mateusz.kiersnowski@gmail.com>"

# Install Poetry
RUN pip install poetry==1.8.3

# make poetry create virtualenvs in the project directory
ENV POETRY_VIRTUALENVS_IN_PROJECT=true

WORKDIR /app

# Copy dependencies files
COPY pyproject.toml poetry.lock ./
COPY docker-entrypoint.sh .

# Copy source code
COPY src/ src/

# Copy database migration files
COPY alembic/ alembic/
COPY alembic.ini alembic.ini

# Install dependencies
RUN poetry install --no-root --no-dev

EXPOSE 5000

ENTRYPOINT ["sh", "./docker-entrypoint.sh"]
