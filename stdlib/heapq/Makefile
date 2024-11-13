run: lint
	python3 priority_tasks.py

lint: format
	ruff . --fix

format:
	ruff check--select I --fix .
	ruff format .

