unflatten: lint
	python3 unflatten_tryout.py

lint: format
	ruff check . --fix

format:
	ruff check --select I --fix .
	ruff format .

