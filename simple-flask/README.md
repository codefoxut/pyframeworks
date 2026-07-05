# simple-flask

[Flask](https://flask.palletsprojects.com/) is the archetypal WSGI micro-framework: a small core (routing + Jinja2 templating) extended via a large plugin ecosystem.

## Start here

- [Flask docs — Quickstart](https://flask.palletsprojects.com/en/latest/quickstart/)
- [Flask docs — Application Factories](https://flask.palletsprojects.com/en/latest/patterns/appfactories/)
- [Flask-SQLAlchemy docs](https://flask-sqlalchemy.palletsprojects.com/)
- [Flask-Login docs](https://flask-login.readthedocs.io/)

## Key concepts to learn

- `@app.route(...)` and the application factory pattern (`create_app()`)
- Jinja2 templating and Flask's `render_template`
- Blueprints for splitting a larger app into modules
- Extensions: Flask-SQLAlchemy (ORM), Flask-Login (auth), Flask-RESTful/Flask-Smorest (APIs)

## Suggested first project

A blog with Jinja templates, Flask-SQLAlchemy, and Flask-Login — or a REST API with Flask-RESTful/Flask-Smorest.

## Running

```bash
make install   # pip install flask
make run       # runs app.py once you've added one
```
