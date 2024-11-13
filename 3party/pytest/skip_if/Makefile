.PHONY: test test_license lint

test_license: lint
	pytest -s -vv -m 'not unlicensed'

test: lint
	pytest -s -vv

lint:
	ruff format .
	ruff check --select I --fix .
	ruff check --fix .
