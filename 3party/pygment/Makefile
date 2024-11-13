run: lint
	python3 pygments_tryout.py

lint: format
	ruff . --fix

format:
	ruff check--select I --fix .
	ruff format .

