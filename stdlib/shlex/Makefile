run: lint
	python3 shlex_tryout.py

lint: format
	ruff . --fix

format:
	ruff check--select I --fix .
	ruff format .

