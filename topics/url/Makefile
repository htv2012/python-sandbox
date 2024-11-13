test: lint
	pytest -s -vv

lint: format
	ruff . --fix

format:
	ruff check--select I --fix .
	ruff format .

