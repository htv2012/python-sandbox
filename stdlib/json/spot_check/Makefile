run: lint
	pytest -s -vv

lint: format
	ruff check . --fix

format:
	ruff check --select I --fix .
	ruff format .

