.PHONY: help test clean format lint watch

test: lint
	python -m doctest numericlib.py
	pytest -v

watch: lint
	ptw -v --onfail 'say tests failed'

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

format:
	ruff check--select I --fix .
	isort *.py

lint: format
	ruff *.py
