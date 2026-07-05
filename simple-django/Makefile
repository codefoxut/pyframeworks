PYTHON := python3
MANAGE := $(PYTHON) manage.py

.DEFAULT_GOAL := help

.PHONY: help install migrate makemigrations run shell test clean

help:
	@echo "make install         pip install -r requirement.txt"
	@echo "make migrate         apply database migrations"
	@echo "make makemigrations  create new migrations from model changes"
	@echo "make run             runserver on :8000"
	@echo "make shell           open the Django shell"
	@echo "make test            run pytest"
	@echo "make clean           remove Python cache files"

install:
	$(PYTHON) -m pip install -r requirement.txt

migrate:
	$(MANAGE) migrate

makemigrations:
	$(MANAGE) makemigrations

run:
	$(MANAGE) runserver 0.0.0.0:8000

shell:
	$(MANAGE) shell

test:
	$(PYTHON) -m pytest

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
