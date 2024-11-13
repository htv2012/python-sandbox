run: lint
	python3 dict2csv.py

lint: format
	ruff . --fix

format:
	ruff check--select I --fix .
	ruff format .

