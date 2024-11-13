run: lint
	PYTHONPATH=.. pytest -s -v

lint: format
	ruff check . --fix

format:
	ruff check --select I --fix .
	ruff format .

