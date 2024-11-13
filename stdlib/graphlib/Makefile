cleanup: lint
	python3 cleanup_objects_concurrently.py

lint: format
	ruff . --fix

format:
	ruff check--select I --fix .
	ruff format .

