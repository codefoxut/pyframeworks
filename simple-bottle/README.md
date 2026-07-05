# simple-bottle

[Bottle](https://bottlepy.org/) is a single-file, zero-dependency WSGI micro-framework — a good place to see how little code a working web app actually needs.

## Start here

- [Bottle docs — Tutorial](https://bottlepy.org/docs/dev/tutorial.html)
- [Bottle docs — API reference](https://bottlepy.org/docs/dev/api.html)

## Key concepts to learn

- `@route(...)` decorator-based routing on a single default `Bottle()` app
- `request` / `response` globals instead of a per-handler parameter
- Bottle's built-in `SimpleTemplate` engine
- Running with the built-in dev server (`bottle.run(...)`) vs. a production WSGI server

## Suggested first project

A single-file URL shortener using Bottle's built-in dev server and SQLite.

## Running

```bash
make install   # pip install bottle
make run       # runs app.py once you've added one
```
