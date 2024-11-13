.PHONY: all deserialize run lint
SCRIPT = serialize.py

run:
	python3 $(SCRIPT)

lint:
	ruff check --select I --fix .
	ruff format .
	ruff check . --fix

run: lint
	python3 $(SCRIPT)

