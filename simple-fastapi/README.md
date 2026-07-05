# simple-fastapi

[FastAPI](https://fastapi.tiangolo.com/) is an async (ASGI) API framework built on Starlette + Pydantic. Type hints double as request/response validation and generate an interactive OpenAPI/Swagger UI for free.

## Start here

- [FastAPI docs — Tutorial, User Guide](https://fastapi.tiangolo.com/tutorial/)
- [FastAPI docs — Bigger Applications, Multiple Files](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
- [FastAPI docs — Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)

## Key concepts to learn

- Path/query/body parameters validated via type hints and Pydantic models
- Automatic docs at `/docs` (Swagger UI) and `/redoc`
- `Depends(...)` for dependency injection (auth, shared query params, DB sessions)
- `APIRouter` for splitting a bigger app into modules (see `secondapp/routers/`)
- Background tasks, response models, status codes, tags

## What's already here

- **`firstapp/`** — follows the official FastAPI tutorial: path/query/body params, headers/cookies, response models. Run from inside the folder since it uses bare imports (`from firstapp_data import ...`).
- **`secondapp/`** — follows the ["Bigger Applications"](https://fastapi.tiangolo.com/tutorial/bigger-applications/) tutorial: routers, dependencies, an internal admin router. Uses relative imports, so it must run as a package from the `simple-fastapi/` root.

## Suggested next project

A JSON todo API with Pydantic models, dependency-injected auth, and background tasks for notifications.

## Running

```bash
make install     # pip install -r fastapi_req.txt -c fastapi_constraints.txt
make run-first   # serves firstapp on :8000
make run-second  # serves secondapp on :8001
```
