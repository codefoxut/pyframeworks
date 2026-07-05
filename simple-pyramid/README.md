# simple-pyramid

[Pyramid](https://trypyramid.com/) supports both URL-dispatch routing (Flask-style) and traversal-based routing (object-graph based) — a good place to learn what traversal actually is.

## Start here

- [Pyramid docs — Quick Tutorial](https://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/index.html)
- [Pyramid docs — URL Dispatch](https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/urldispatch.html)
- [Pyramid docs — Traversal](https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/traversal.html)

## Key concepts to learn

- The `Configurator` object used to wire up routes/views at startup
- URL dispatch (`config.add_route` + `config.add_view`) vs. traversal (resource trees, `__getitem__`)
- Renderers (JSON, templates) declared per-view
- Pyramid's scaffolds (`pcreate`) for generating a starter project

## Suggested first project

A "traversal vs. URL dispatch" demo app that implements the same two routes both ways, since that contrast is Pyramid's signature feature.

## Running

```bash
make install   # pip install pyramid
make run       # runs app.py once you've added one
```
