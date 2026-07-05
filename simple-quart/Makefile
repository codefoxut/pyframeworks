PYTHON := python3
APP    := app.py

.DEFAULT_GOAL := help

.PHONY: help install run clean

help:
	@echo "make install   install quart"
	@echo "make run       run $(APP) in debug mode (add it first — see README.md)"
	@echo "make clean     remove Python cache files"

install:
	$(PYTHON) -m pip install quart

run:
	@test -f $(APP) || (echo "$(APP) not found yet — see README.md to get started" && exit 1)
	QUART_APP=$(APP) QUART_DEBUG=1 $(PYTHON) -m quart run

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
