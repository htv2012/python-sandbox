.PHONY: all test run lint
SCRIPT := skip_comments_in_csv.py

all: run

lint:
	ruff check --select I --fix .
	ruff format .
	ruff check . --fix

run: lint
	python3 $(SCRIPT)

test: lint
	pytest -s -v

