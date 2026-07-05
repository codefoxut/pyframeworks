# simple-aiohttp

[aiohttp](https://docs.aiohttp.org/) is an asyncio-native framework that is also a full HTTP *client* library — the same package gives you `web.Application` for servers and `ClientSession` for concurrent HTTP clients.

## Start here

- [aiohttp docs — Web Server Quickstart](https://docs.aiohttp.org/en/stable/web_quickstart.html)
- [aiohttp docs — Client Quickstart](https://docs.aiohttp.org/en/stable/client_quickstart.html)
- [aiohttp docs — Websockets](https://docs.aiohttp.org/en/stable/web_quickstart.html#websockets)

## Key concepts to learn

- `web.Application` + `web.RouteTableDef` / `app.router.add_get(...)` for routing
- Handlers as `async def handler(request) -> web.Response`
- `aiohttp.ClientSession` for concurrent outgoing requests (`asyncio.gather` fan-out)
- Middlewares (`@web.middleware`) for cross-cutting concerns (auth, logging)
- Websocket handling via `web.WebSocketResponse`

## Suggested first project

A client+server pair: a scraper that fans out concurrent `aiohttp.ClientSession` requests, fronted by a tiny aiohttp server that reports scrape status.

## Running

```bash
make install   # pip install aiohttp
make run       # runs app.py once you've added one
```
