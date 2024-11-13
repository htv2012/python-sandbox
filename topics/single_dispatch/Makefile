run: lint
	python3 get_ref_using_single_dispatch.py

lint: format
	ruff . --fix

format:
	ruff check--select I --fix .
	ruff format .

