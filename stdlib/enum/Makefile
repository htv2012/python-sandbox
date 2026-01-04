.PHONY: test, lint

test: lint
	uv run pytest -s -v

lint:
	uv run ruff check --select I --fix .
	uv run ruff format .
	uv run ruff check .
