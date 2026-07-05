# simple-django

[Django](https://www.djangoproject.com/) is a batteries-included, synchronous (WSGI) full-stack framework: ORM, admin site, auth, templating, and forms out of the box.

## Start here

- [Django docs — Writing your first app](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- [Django Girls Tutorial](https://tutorial.djangogirls.org/en/django_start_project/)
- [Django REST Framework — Tutorial](https://www.django-rest-framework.org/tutorial/1-serialization/)

## Key concepts to learn

- Project vs. app structure (`django_proj/` project, `polls`/`blog`/`snippets`/`rest_api` apps)
- Models + migrations (`makemigrations`/`migrate`) and the ORM query API
- The admin site (`admin.py`) for free CRUD over your models
- Class-based vs. function-based views, and DRF serializers/viewsets for APIs

**Sample apps already in this folder:**
- Sample Poll App ([Django Project Tutorial](https://docs.djangoproject.com/en/1.11/intro/tutorial01/))
- Sample Blog App ([Django Girls Tutorial](https://tutorial.djangogirls.org/en/django_start_project/))
- Sample DjangoRestFramework App ([Django Rest Framework Tutorial](http://www.django-rest-framework.org/tutorial/1-serialization/))

## Running

```bash
make install    # pip install -r requirement.txt
make migrate    # apply migrations (sqlite db.sqlite3)
make run        # runserver on :8000
make test       # pytest (see pytest.ini)
```