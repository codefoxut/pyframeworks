PYTHON := python3
APP    := firstapp/helllo_world.py

.DEFAULT_GOAL := help

.PHONY: help install run clean

help:
	@echo "make install   pdm install (falls back to pip install -r tornado_req.txt)"
	@echo "make run       run $(APP) on :8888"
	@echo "make clean     remove Python cache files"

install:
	@command -v pdm >/dev/null 2>&1 && pdm install || $(PYTHON) -m pip install -r tornado_req.txt

run:
	$(PYTHON) $(APP)

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
