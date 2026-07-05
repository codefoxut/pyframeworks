# simple-litestar

[Litestar](https://litestar.dev/) is a modern, strongly-typed ASGI framework (spiritual successor to Starlite) with dependency injection, OpenAPI docs, and layered architecture built in — worth practicing as FastAPI's most credible modern alternative.

## Start here

- [Litestar docs — Introduction](https://docs.litestar.dev/latest/)
- [Litestar docs — Tutorial](https://docs.litestar.dev/latest/tutorials/)

## Key concepts to learn

- `Litestar(route_handlers=[...])` with `@get`/`@post`/... decorators
- Layered dependency injection (app/router/controller/handler level)
- Controllers (class-based handler grouping) as an alternative to plain functions
- Built-in data validation via type hints (msgspec/attrs/Pydantic-compatible) and automatic OpenAPI

## Suggested first project

The same todo API built for FastAPI, ported to Litestar — compare how DI and OpenAPI generation differ between the two.

## Running

```bash
make install   # pip install litestar uvicorn
make run       # runs app.py once you've added one
```
