1: lint
	python 01_simple_connect.py primary

2: lint
	python 02_ssh_config.py

lint: format
	ruff . --fix

format:
	ruff check--select I --fix .
	ruff format .