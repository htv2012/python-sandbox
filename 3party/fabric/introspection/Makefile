all: lint
	fab -H lab introspection

lint: format
	ruff check . --fix

format:
	ruff check --select I --fix .
	ruff format .

