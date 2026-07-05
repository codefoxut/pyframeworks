# simple-starlette

[Starlette](https://www.starlette.io/) is the lightweight ASGI toolkit that FastAPI is built on top of. Learning it directly shows which parts of "FastAPI" are actually Starlette (routing, middleware, websockets, SSE) and which are FastAPI/Pydantic on top.

## Start here

- [Starlette docs](https://www.starlette.io/)
- [Starlette docs — Routing](https://www.starlette.io/routing/)
- [Starlette docs — WebSockets](https://www.starlette.io/websockets/)
- [Starlette docs — Responses (incl. Server-Sent Events via streaming)](https://www.starlette.io/responses/)

## Key concepts to learn

- `Starlette(routes=[...])` and `Route`/`WebSocketRoute`
- ASGI request/response cycle (`Request`, `Response`, `JSONResponse`, `StreamingResponse`)
- Middleware stack (`Middleware(...)`)
- Plain `async def` websocket handlers (no FastAPI abstractions)

## Suggested first project

A minimal ASGI app with a WebSocket endpoint and a Server-Sent Events endpoint, showing exactly what FastAPI is built on top of.

## Running

```bash
make install   # pip install starlette uvicorn
make run       # runs app.py once you've added one
```
