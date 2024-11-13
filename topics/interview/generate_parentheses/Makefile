test: lint
	pytest -vv

lint: format
	ruff . --fix

format:
	ruff check--select I --fix .
	ruff format .

