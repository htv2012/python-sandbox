.PHONY: all test run lint
SCRIPT := batched_tryout.py

all: run

lint:
	ruff check --select I --fix .
	ruff format .
	ruff check . --fix

run: lint
	python3 $(SCRIPT)

test: lint
	pytest -s -v

