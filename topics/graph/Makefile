run: lint
	python3 sandbox.py

lint: format
	ruff check . --fix

format:
	ruff check --select I --fix .
	ruff format .
