.PHONY: all test run lint
script := list_titles.py

all: run

lint:
	ruff check --select I --fix .
	ruff format .
	ruff check . --fix

run: lint
	python3 $(script)

test: lint
	pytest -s -v

