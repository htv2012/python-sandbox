
test: lint
	pytest -v 

lint: format
	ruff . --fix

format:
	ruff check--select I --fix .
	ruff format .

