# simple-sanic

[Sanic](https://sanic.dev/) is an async (ASGI/asyncio-native) framework with a Flask-like API but built for speed from day one — worth practicing to see "Flask idioms, async execution."

## Start here

- [Sanic docs — Getting Started](https://sanic.dev/en/guide/getting-started.html)
- [Sanic docs — Routing](https://sanic.dev/en/guide/basics/routing.html)

## Key concepts to learn

- `Sanic(__name__)` app instance + `@app.route(...)` / `@app.get`, `@app.post`
- `async def handler(request)` — every handler is a coroutine, unlike Flask
- Blueprints for splitting a larger app into modules
- Built-in dev server with auto-reload (`app.run(..., debug=True, auto_reload=True)`)

## Suggested first project

Rebuild the Flask blog/todo idea from `simple-flask` in Sanic and compare how much of the Flask-style API carries over once everything is `async`.

## Running

```bash
make install   # pip install sanic
make run       # runs app.py once you've added one
```
