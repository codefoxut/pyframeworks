# simple-blacksheep

[BlackSheep](https://www.neoteroi.dev/blacksheep/) is an ASGI framework built for raw throughput, with built-in dependency injection and automatic OpenAPI docs — a good benchmark comparison point against FastAPI.

## Start here

- [BlackSheep docs — Getting Started](https://www.neoteroi.dev/blacksheep/getting-started/)
- [BlackSheep docs — OpenAPI docs generation](https://www.neoteroi.dev/blacksheep/openapi/)

## Key concepts to learn

- `Application()` instance + `@app.route(...)` / `@get`, `@post` decorators
- Built-in dependency injection (services registered on the app, resolved by type hints)
- Controllers (class-based views) as an alternative to function handlers
- Automatic OpenAPI/Swagger generation

## Suggested first project

A benchmark-style JSON API (BlackSheep is built for raw throughput) — build the same todo API you wrote for FastAPI and compare requests/sec.

## Running

```bash
make install   # pip install blacksheep uvicorn
make run       # runs app.py once you've added one
```
