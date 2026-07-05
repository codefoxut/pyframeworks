PYTHON := python3

.DEFAULT_GOAL := help

.PHONY: help install run-first run-second clean

help:
	@echo "make install     pip install -r fastapi_req.txt -c fastapi_constraints.txt"
	@echo "make run-first   serve firstapp on :8000"
	@echo "make run-second  serve secondapp on :8001"
	@echo "make clean       remove Python cache files"

install:
	$(PYTHON) -m pip install -r fastapi_req.txt -c fastapi_constraints.txt

run-first:
	cd firstapp && $(PYTHON) -m uvicorn firstapp:app --reload --port 8000

run-second:
	$(PYTHON) -m uvicorn secondapp.main:app --reload --port 8001

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
