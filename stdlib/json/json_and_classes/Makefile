.PHONY: demo lint format

demo: lint
	python3 main.py

format:
	ruff check--select I --fix .
	isort *.py

lint: format
	ruff *.py
