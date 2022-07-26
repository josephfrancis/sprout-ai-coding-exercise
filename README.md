# Sprout.AI Coding Exercise

## Functionality

This FastAPI application:

* Accepts a blog post
* Stores it in a database
* Checks if any of its sentences contain foul language
* Updates the database with a flag `hasFoulLanguage` if it does

The database is SQLite as per [this tutorial](https://fastapi.tiangolo.com/advanced/async-sql-databases/).

## Running

```sh
# With Docker Compose (requires Docker daemon)
docker-compose up --build

# With local environment (Python v3.10.5)
python -m uvicorn app.main:app
```
