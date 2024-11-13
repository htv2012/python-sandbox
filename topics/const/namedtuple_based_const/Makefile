run: test
	python3 1_simple_usage.py
	python3 2_redefine.py
	python3 3_characteristics.py
	python3 4_add_values.py

test: lint
	PYTHONPATH=. pytest -s -v

lint: format
	ruff . --fix

format:
	ruff check--select I --fix .
	ruff format .

