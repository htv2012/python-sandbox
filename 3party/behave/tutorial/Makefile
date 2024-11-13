run: lint
	behave

lint: format
	ruff check . --fix

format:
	ruff check --select I --fix .
	ruff format .

