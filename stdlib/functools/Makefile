.PHONY: help run lint format

run: lint
	python3 partialmethod_tryout.py
	python3 lru_cache_method.py

lint: format
	ruff . --fix

format:
	ruff check--select I --fix .
	ruff format .

