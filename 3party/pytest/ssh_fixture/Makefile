run: lint
	pytest -s -v

lint: format
	ruff check . --fix

sandbox:
	python3 -i sandbox.py

format:
	ruff check --select I --fix .
	ruff format .

