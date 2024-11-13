.PHONY: all test lint

all: test

lint:
	ruff check --select I --fix .
	ruff format .
	ruff check . --fix

test: lint
	pytest
	@printf "\n#\n# NOTE: Observe that each fixture is called only once\n#\n"

