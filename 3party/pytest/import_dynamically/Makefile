all: lint
	pytest

lint: format
	ruff check . --fix

format:
	ruff check --select I --fix .
	ruff format .

