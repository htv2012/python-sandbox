.PHONY: all test run lint
SCRIPT := main.py

all: run

lint:
	ruff check --select I --fix .
	ruff format .
	ruff check . --fix

run: lint
	@printf "\n#\n# Show Help\n#\n$$ "
	python3 main.py -h
	@printf "\n#\n# Without Args\n#\n$$ "
	python3 main.py
	@printf "\n#\n# Insecured\n#\n$$ "
	python3 main.py --connection=insecured

test: lint
	pytest -s -v

