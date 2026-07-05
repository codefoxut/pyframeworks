PYTHON := python3
APP    := app
PORT   := 8000

.DEFAULT_GOAL := help

.PHONY: help install run clean

help:
	@echo "make install   install starlette + uvicorn"
	@echo "make run       serve $(APP):app on port $(PORT) (add it first — see README.md)"
	@echo "make clean     remove Python cache files"

install:
	$(PYTHON) -m pip install starlette uvicorn

run:
	@test -f $(APP).py || (echo "$(APP).py not found yet — see README.md to get started" && exit 1)
	$(PYTHON) -m uvicorn $(APP):app --reload --port $(PORT)

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
