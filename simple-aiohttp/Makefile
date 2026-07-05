PYTHON := python3
APP    := app.py

.DEFAULT_GOAL := help

.PHONY: help install run clean

help:
	@echo "make install   install aiohttp"
	@echo "make run       run $(APP) (add it first — see README.md)"
	@echo "make clean     remove Python cache files"

install:
	$(PYTHON) -m pip install aiohttp

run:
	@test -f $(APP) || (echo "$(APP) not found yet — see README.md to get started" && exit 1)
	$(PYTHON) $(APP)

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
