# simple-apidaora

[apidaora](https://github.com/dutradda/apidaora) is a minimal ASGI framework where plain Python **dataclasses** (not a validation library like Pydantic) define request and response shapes — a useful contrast to FastAPI's Pydantic-first style.

## Start here

- [apidaora GitHub — README & usage examples](https://github.com/dutradda/apidaora)

## Key concepts to learn

- `@dataclass` request/response models instead of a schema library
- `route(...)` decorators mapping dataclasses to HTTP methods/paths
- Running the resulting ASGI `app` with an ASGI server (`uvicorn`)
- How little apidaora does compared to FastAPI/Starlette — no built-in DI, no OpenAPI UI by default

## Suggested first project

A tiny dataclass-in / dataclass-out API (e.g. a calculator or a todo list), then compare its serialization style side-by-side with the FastAPI todo API in `simple-fastapi`.

## Running

```bash
make install   # pip install apidaora uvicorn
make run       # runs app.py once you've added one
```
