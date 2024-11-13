.PHONY: all test run lint
SCRIPT := main.py


all: test

lint:
	ruff check --select I --fix .
	ruff format .
	ruff check . --fix

run: lint
	python3 $(SCRIPT)

test: lint
	pytest -s -v $(TEST)

