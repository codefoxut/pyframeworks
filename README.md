# pyframeworks

A hands-on tour of Python web frameworks — one small project per framework, built to learn how each one actually feels to work with.

Reference: [TechEmpower Framework Benchmarks (Python)](https://github.com/TechEmpower/FrameworkBenchmarks/tree/master/frameworks/Python)

Working through this at 5 hours/week? See [`LEARNING_PLAN.md`](LEARNING_PLAN.md) for a week-by-week pacing plan across all frameworks below.

## Block 1 — Definitions

- **[Django](https://www.djangoproject.com/)** — Batteries-included, synchronous (WSGI) full-stack framework: ORM, admin site, auth, templating, and forms out of the box. The default choice when you want a lot of things decided for you.
- **[FastAPI](https://fastapi.tiangolo.com/)** — Async (ASGI) API framework built on Starlette + Pydantic. Type hints double as request/response validation and generate an interactive OpenAPI/Swagger UI for free.
- **[Tornado](https://www.tornadoweb.org/)** — One of the original async Python frameworks, with its own event loop predating `asyncio`. Strong at long-lived connections: websockets, long-polling, streaming.
- **[aiohttp](https://docs.aiohttp.org/)** — Async (ASGI-adjacent, asyncio-native) framework that is also a full HTTP *client* library. Good for learning how a server and a concurrent client-fan-out talk to each other in the same ecosystem.
- **[Bottle](https://bottlepy.org/)** — A single-file, zero-dependency WSGI micro-framework. Useful for seeing how little code a working web app actually needs.
- **[Flask](https://flask.palletsprojects.com/)** — The archetypal WSGI micro-framework: a small core (routing + Jinja2 templating) extended via a large plugin ecosystem (SQLAlchemy, Login, RESTful, etc.).
- **[Pyramid](https://trypyramid.com/)** — WSGI framework that supports both URL-dispatch routing (Flask-style) and traversal-based routing (object-graph based), making it a good place to learn what traversal even is.
- **[Starlette](https://www.starlette.io/)** — The lightweight ASGI toolkit FastAPI is built on top of. Learning it directly shows which parts of "FastAPI" are actually Starlette (routing, middleware, websockets, SSE).
- **[BlackSheep](https://www.neoteroi.dev/blacksheep/)** — An ASGI framework built for raw throughput, with built-in dependency injection and OpenAPI docs. A good benchmark comparison point against FastAPI.
- **[apidaora](https://github.com/dutradda/apidaora)** — A minimal ASGI framework where plain dataclasses (not a validation library) define request/response shapes — a useful contrast to FastAPI's Pydantic-first style.
- **[Sanic](https://sanic.dev/)** *(Async/ASGI, recommended)* — Async (ASGI/asyncio-native) framework with a Flask-like API but built for speed from day one. Worth practicing to see "Flask idioms, async execution."
- **[Quart](https://quart.palletsprojects.com/)** *(Async/ASGI, recommended)* — An async fork of Flask with (almost) the same API. Practicing it side-by-side with Flask is the clearest way to feel the sync-vs-async difference without changing frameworks.
- **[Litestar](https://litestar.dev/)** *(Async/ASGI, recommended)* — A modern, strongly-typed ASGI framework (spiritual successor to Starlite) with DI, OpenAPI, and layered architecture built in. Worth practicing as FastAPI's most credible modern alternative.
- **[Robyn](https://robyn.tech/)** *(Async/ASGI)* — A Rust-powered async Python web framework focused on raw performance, with a Flask-like decorator API. The "extreme performance" end of the async spectrum.
- **[Falcon](https://falconframework.org/)** *(WSGI micro, recommended)* — A minimalist WSGI/ASGI framework aimed squarely at REST APIs, with no templating or ORM baked in. Good for learning what's left when a framework strips everything down to routing + request/response.
- **[CherryPy](https://cherrypy.dev/)** *(WSGI micro, recommended)* — An older, minimal, object-oriented WSGI framework where URLs map directly to methods on a Python object. Good historical/foundational contrast to today's decorator-routed frameworks.
- **[web2py](http://www.web2py.com/)** *(WSGI micro)* — An older, no-install-needed full-stack-ish framework with a built-in admin/IDE and its own ORM (DAL). A historical contrast to today's app-factory conventions.
- **[Masonite](https://docs.masoniteproject.com/)** *(Full-stack)* — A modern full-stack framework explicitly modeled on Laravel: an IoC container, its own ORM, and Rails/Laravel-style conventions applied to Python.
- **[web.py](https://webpy.org/)** *(Full-stack)* — A famously tiny, "zero-config" full-stack framework. Mostly of historical interest today, but a good example of extreme minimalism.
- **[Django Ninja](https://django-ninja.dev/)** *(API-first/RPC)* — A FastAPI-style (type-hint validation, automatic OpenAPI) API layer built on top of Django, so you keep Django's ORM/admin while getting FastAPI-like ergonomics.
- **[Connexion](https://connexion.readthedocs.io/)** *(API-first/RPC)* — An OpenAPI/Swagger-spec-first framework (built on Flask or Starlette) where you write the spec first and Connexion wires it to your handler functions.
- **[gRPC (grpcio)](https://grpc.io/docs/languages/python/)** *(API-first/RPC)* — Not a REST/HTTP web framework — an RPC framework using Protocol Buffers over HTTP/2. Worth practicing to contrast typed RPC contracts against the REST APIs the rest of this list builds.

## Block 2 — Table

| Framework | Type | Folder | Status |
|---|---|---|---|
| Django | WSGI, sync | [`simple-django`](simple-django) | ✅ Implemented |
| FastAPI | ASGI, async | [`simple-fastapi`](simple-fastapi) | ✅ Implemented |
| Tornado | async (own loop) | [`simple-tornado`](simple-tornado) | 🚧 Started |
| aiohttp | asyncio-native | [`simple-aiohttp`](simple-aiohttp) | ⬜ Not started |
| Bottle | WSGI, sync | [`simple-bottle`](simple-bottle) | ⬜ Not started |
| Flask | WSGI, sync | [`simple-flask`](simple-flask) | ⬜ Not started |
| Pyramid | WSGI, sync | [`simple-pyramid`](simple-pyramid) | ⬜ Not started |
| Starlette | ASGI, async | [`simple-starlette`](simple-starlette) | ⬜ Not started |
| BlackSheep | ASGI, async | [`simple-blacksheep`](simple-blacksheep) | ⬜ Not started |
| apidaora | ASGI, async | [`simple-apidaora`](simple-apidaora) | ⬜ Not started |
| Sanic | ASGI, async | [`simple-sanic`](simple-sanic) | ⬜ Not started |
| Quart | ASGI, async | [`simple-quart`](simple-quart) | ⬜ Not started |
| Litestar | ASGI, async | [`simple-litestar`](simple-litestar) | ⬜ Not started |
| Robyn | ASGI, async (Rust core) | *(no folder yet)* | ⬜ Not started |
| Falcon | WSGI/ASGI | [`simple-falcon`](simple-falcon) | ⬜ Not started |
| CherryPy | WSGI, sync | [`simple-cherrypy`](simple-cherrypy) | ⬜ Not started |
| web2py | WSGI, sync | *(no folder yet)* | ⬜ Not started |
| Masonite | WSGI, sync | *(no folder yet)* | ⬜ Not started |
| web.py | WSGI, sync | *(no folder yet)* | ⬜ Not started |
| Django Ninja | WSGI/ASGI (Django) | *(no folder yet)* | ⬜ Not started |
| Connexion | WSGI/ASGI (spec-first) | *(no folder yet)* | ⬜ Not started |
| gRPC (grpcio) | RPC over HTTP/2 | *(no folder yet)* | ⬜ Not started |

Each folder that exists has its own `Makefile` (install/run/clean) and `README.md` (framework docs, key concepts, suggested first project) to get started with that framework specifically.

## Repo conventions

- Each framework lives in its own `simple-<framework>/` folder with its own `requirements.txt`/`pyproject.toml` so environments don't collide.
- Prefer the framework's own project-generator/quickstart for the initial skeleton, then extend it with the project idea suggested in that folder's `README.md`.
- Keep each project small — the goal is breadth across frameworks, not a polished app per framework.
