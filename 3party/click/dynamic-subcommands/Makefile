.PHONY: all test run lint clean

### Default target(s)
all: lint test run

### Perform static analysis
lint:
	uv run ruff check --select I --fix .
	uv run ruff format .
	uv run ruff check . --fix

### Run the project
run: lint
	uv run dynamic-subcommands
	uv run dynamic-subcommands put
	uv run dynamic-subcommands get

### Run unit tests
test: lint
	PYTHONPATH=./src uv run pytest -s -v

### Clean up generated files
clean:
	uv clean
	rm -fr .ruff_cache .venv

