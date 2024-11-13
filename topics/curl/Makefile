test: lint
	pytest

lint: format
	ruff . --fix

format:
	ruff check--select I --fix .
	ruff format .

