test: lint
	pytest -s -v

lint: format
	ruff . --fix

format:
	ruff check--select I --fix .
	ruff format .

