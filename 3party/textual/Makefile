stopwatch: lint
	python3 stopwatch.py

lint: format
	ruff . --fix

format:
	ruff check--select I --fix .
	ruff format .

