.PHONY: all test lint

all: test

lint:
	ruff check --select I --fix .
	ruff format .
	ruff check . --fix

test: lint
	pytest -s -v

