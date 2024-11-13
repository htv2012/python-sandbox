.PHONY: test, lint

test: lint
	pytest -s -v

lint:
	ruff check --select I --fix .
	ruff format .
	ruff check .
