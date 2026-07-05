# Learning Plan — 5 hours/week

A pacing plan to work through every framework in `README.md`'s Block 2 table, at 5 hours/week. Frameworks are grouped by category so you compare similar ones back-to-back (the contrast is where most of the learning happens). Each "week" is a unit of effort, not a calendar week with a fixed date — start Week 1 whenever you begin and move to the next week once that framework's checklist is done, even if it takes a few extra days.

**Total: 27 weeks (~6 months) at 5 hrs/week ≈ 135 hours** to touch all 22 frameworks currently listed. If a week runs long, let it — don't compress the project just to stay on schedule.

## Weekly template (5 hours)

Repeat this structure for every 1-week framework:

| Day | Time | Task |
|---|---|---|
| Day 1 | 1h | Read that framework's "Start here" links + "Key concepts to learn" in its `simple-<framework>/README.md` |
| Day 2 | 2h | Build the "Suggested first project" from that same README |
| Day 3 | 1h | Finish the project so it actually runs end-to-end; commit it |
| Day 4 | 1h | Write 3–5 bullet notes: what felt different vs. a framework you already know. Flip the status column in the main `README.md` table (⬜ → 🚧 → ✅) |

For 2-week frameworks, keep Day 1 and Day 4 as-is and stretch Day 2–3 (build) across the extra week — the point is more hands-on time, not more reading.

## Phase 0 — Consolidate what's already started (3 weeks)

These already have code in the repo; the goal is to finish them properly before moving on, so the comparisons in later phases have a solid baseline.

| Week | Framework | Focus |
|---|---|---|
| 1 | Django | Review polls/blog/DRF apps, run migrations + admin + tests end-to-end |
| 2 | FastAPI | Build the suggested todo API (Pydantic models, `Depends` auth, background tasks) |
| 3 | Tornado | Build the suggested websocket chat room |

## Phase 1 — Sync WSGI micro cluster (8 weeks)

Flask anchors this cluster since the rest get compared against it.

| Week | Framework | Focus |
|---|---|---|
| 4–5 | Flask | Blog with Jinja + Flask-SQLAlchemy + Flask-Login (2 weeks — extensions add real scope) |
| 6 | Bottle | Single-file URL shortener |
| 7 | CherryPy | Guestbook app (object-dispatch routing) |
| 8 | Pyramid | Traversal-vs-URL-dispatch demo |
| 9 | Falcon | Minimal REST API with resource classes |
| 10 | web2py | Quick tour — its own admin/IDE workflow is the main thing to learn |
| 11 | web.py | Quick tour — minimal, mostly historical interest |

## Phase 2 — Async/ASGI cluster (10 weeks)

| Week | Framework | Focus |
|---|---|---|
| 12 | Starlette | Minimal ASGI app: WebSocket + SSE endpoint |
| 13 | aiohttp | Scraper client fan-out + status server |
| 14 | Sanic | Port the Flask app from Week 4–5 — fast, since the API rhymes with Flask |
| 15 | Quart | Same port exercise as Sanic — note exactly what had to change to go async |
| 16–17 | Litestar | Port the FastAPI todo API (2 weeks — layered DI takes longer to click) |
| 18 | BlackSheep | Benchmark-style JSON API, compare req/sec against FastAPI |
| 19 | apidaora | Tiny dataclass-in/out API, contrast with Pydantic-first FastAPI |
| 20–21 | Robyn | Rust-core async framework (2 weeks buffer — newer, thinner docs) |

## Phase 3 — Full-stack (2 weeks)

| Week | Framework | Focus |
|---|---|---|
| 22–23 | Masonite | Laravel-style IoC container + ORM + controllers (2 weeks — most ceremony of the micro-frameworks) |

## Phase 4 — API-first / RPC (4 weeks)

| Week | Framework | Focus |
|---|---|---|
| 24 | Django Ninja | Type-hinted API layer on top of the Django app from Week 1 |
| 25 | Connexion | OpenAPI-spec-first: write the spec, wire handlers to it |
| 26–27 | gRPC (grpcio) | Protobuf codegen + a typed RPC service (2 weeks — different paradigm from everything above) |

## Keeping score

- Update the Status column in `README.md`'s Block 2 table as you go (⬜ → 🚧 → ✅).
- If a framework's suggested project turns out too small to fill its week, use the spare time to write a short comparison note instead of starting the next framework early — the contrast notes are what make this plan worth more than reading 22 sets of docs back to back.
