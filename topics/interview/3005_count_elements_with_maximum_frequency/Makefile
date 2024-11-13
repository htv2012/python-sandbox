LOGLEVEL ?= WARN

test: lint
	pytest -s -vv --log-cli-level $(LOGLEVEL)

log: lint
	$(MAKE) LOGLEVEL=DEBUG

lint: format
	ruff . --fix

format:
	ruff check--select I --fix .
	ruff format .

