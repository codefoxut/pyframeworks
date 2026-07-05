# simple-cherrypy

[CherryPy](https://cherrypy.dev/) is an older, minimal, object-oriented WSGI framework where URLs map directly to methods on a Python object — a good historical/foundational contrast to today's decorator-routed frameworks.

## Start here

- [CherryPy docs — Tutorials](https://docs.cherrypy.dev/en/latest/tutorials.html)
- [CherryPy docs — Basics](https://docs.cherrypy.dev/en/latest/basics.html)

## Key concepts to learn

- Exposing methods on a plain class via `@cherrypy.expose`, dispatched by URL path segments
- `cherrypy.quickstart(RootObject(), '/', config)` — no separate route table
- CherryPy's built-in production-ready WSGI server (no separate `gunicorn`/`uvicorn` needed)
- Config dicts for per-path settings (static file serving, sessions, tools)

## Suggested first project

A small multi-page app (e.g. a guestbook or a file browser) that shows how object-attribute traversal replaces an explicit route table.

## Running

```bash
make install   # pip install cherrypy
make run       # runs app.py once you've added one
```
