# FastAPI Example

This is a portfolio project demonstrating the use of FastAPI, a modern, fast (high-performance),
web framework for building APIs with Python 3.12 based on standard Python type hints.

The goal of this project is to demonstrate the setup of whole environment with code, tests, pipelines, and building.

## Features
ORM is done using `SQLAlchemy` and `Alembic` for migrations. The DBMS is `PostgreSQL`.
Tests are done using `pytest` framework. Whole app us asynchronous.

# Usage
The application is dockerized, it can be run using `docker compose`:
```bash
docker compose up -d
```
# Running tests
In order to run tests, you need to install the dependencies:
```bash
poetry install
```
Start the PostgreSQL database:
```bash
docker compose up db -d
```
Then you can run the tests using the following command:
```bash
poetry run pytest
```
