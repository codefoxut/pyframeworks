# simple-tornado

[Tornado](https://www.tornadoweb.org/) is one of the original async Python frameworks, with its own event loop predating `asyncio`. It's strong at long-lived connections: websockets, long-polling, streaming.

## Start here

- [Tornado docs — Overview & Quickstart](https://www.tornadoweb.org/en/stable/guide.html)
- [Tornado docs — Coroutines](https://www.tornadoweb.org/en/stable/guide/coroutines.html)
- [Tornado docs — WebSockets](https://www.tornadoweb.org/en/stable/websocket.html)

## Key concepts to learn

- `tornado.web.RequestHandler` subclasses with `get`/`post`/... methods
- `tornado.web.Application` route table + `.listen(port)` + `IOLoop.current().start()`
- `AsyncHTTPClient` for making async outbound requests from a handler
- `tornado.websocket.WebSocketHandler` for websocket endpoints

## What's already here

- **`firstapp/`** — a minimal "Hello, world" handler plus an `AsyncHTTPClient` example.

## Suggested next project

A websocket chat room — or revisit a pictionary-style real-time drawing game (canvas state synced over websockets), which was sketched out earlier and later dropped from this repo.

## Running

```bash
make install   # pdm install (falls back to pip install -r tornado_req.txt)
make run       # runs firstapp/helllo_world.py on :8888
```
