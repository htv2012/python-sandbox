.PHONY: test lint depend

test: lint
	pytest -vv

lint:
	ruff check--select I --fix .
	ruff format .
	ruff . --fix

simple: lint
	python3 simple_dependency_resolver.py
