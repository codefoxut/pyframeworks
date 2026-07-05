# simple-quart

[Quart](https://quart.palletsprojects.com/) is an async fork of Flask with (almost) the same API. Practicing it side-by-side with Flask is the clearest way to feel the sync-vs-async difference without changing frameworks.

## Start here

- [Quart docs — Quickstart](https://quart.palletsprojects.com/en/latest/tutorials/quickstart.html)
- [Quart docs — Flask compatibility notes](https://quart.palletsprojects.com/en/latest/how_to_guides/flask_migration.html)

## Key concepts to learn

- `Quart(__name__)` app + `@app.route(...)` — near-identical surface to Flask
- `async def` view functions, `await` for anything I/O-bound
- Background tasks (`app.add_background_task`) and websockets (`@app.websocket(...)`)
- Where Quart genuinely diverges from Flask (ASGI-only extensions, async test client)

## Suggested first project

Port the Flask blog/todo app from `simple-flask` to Quart, changing as little as possible, then note exactly what had to change to make it async.

## Running

```bash
make install   # pip install quart
make run       # runs app.py once you've added one
```
