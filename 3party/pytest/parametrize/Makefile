FILE ?= *.py

run: lint
	pytest -s -vv $(FILE)

lint: format
	ruff . --fix

format:
	ruff check--select I --fix .
	ruff format .

