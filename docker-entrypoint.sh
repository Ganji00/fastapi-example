#!/bin/bash
set -Eeuo pipefail

echo Starting the application...
poetry run gunicorn -w 3 -k uvicorn.workers.UvicornWorker src.main:app --bind 0.0.0.0:5000
