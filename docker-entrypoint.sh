#!/bin/bash
set -Eeuo pipefail

echo Running database migrations...
poetry run alembic upgrade head

echo Starting the application...
poetry run gunicorn -w 3 -k uvicorn.workers.UvicornWorker src.main:app --bind 0.0.0.0:5000
