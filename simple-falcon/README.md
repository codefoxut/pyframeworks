# simple-falcon

[Falcon](https://falconframework.org/) is a minimalist WSGI/ASGI framework aimed squarely at REST APIs, with no templating or ORM baked in — good for learning what's left when a framework strips everything down to routing + request/response.

## Start here

- [Falcon docs — User Guide](https://falcon.readthedocs.io/en/stable/user/index.html)
- [Falcon docs — Quickstart](https://falcon.readthedocs.io/en/stable/user/quickstart.html)

## Key concepts to learn

- Resource classes with `on_get`/`on_post`/... methods instead of decorated functions
- `falcon.App()` (WSGI) vs `falcon.asgi.App()` (ASGI) — same resource API, different runtime
- Request/response objects (`req`, `resp`) passed explicitly to every method
- Falcon's deliberate lack of built-in ORM/templating — you wire in what you need

## Suggested first project

A minimal REST API (e.g. a notes or todo API) using resource classes, then compare the amount of boilerplate against the same API in Flask or FastAPI.

## Running

```bash
make install   # pip install falcon gunicorn
make run       # runs app.py once you've added one
```
