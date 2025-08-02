.PHONY: help run lint format

run: lint
	uv run partialmethod_tryout.py
	uv run lru_cache_method.py
	uv run cached_property.py

lint:
	uv run ruff check --select I --fix .
	uv run ruff format .
	uv run ruff check . --fix

