run: lint
	python3 const_demo.py

lint: format
	ruff . --fix

format:
	ruff check--select I --fix .
	ruff format .

