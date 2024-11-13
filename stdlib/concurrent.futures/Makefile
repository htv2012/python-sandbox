.PHONY: help depend lint format
tryout: lint
	python3 concurrent_tryout.py

help:
	@echo make depend
	@echo make lint
	@echo make format

depend: lint
	python3 thread_dependencies.py

lint: format
	ruff . --fix

format:
	ruff check--select I --fix .
	ruff format .

