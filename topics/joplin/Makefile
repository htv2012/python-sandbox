.PHONY: all test run lint

### Default target(s)
all: run

### Perform static analysis
lint:
	uv run ruff check --select I --fix .
	uv run ruff format .
	uv run ruff check . --fix

### Run the project
run: lint
	uv run jopcli cat 'jopcli test'

### Run unit tests
test: lint
	uv run pytest -s -v

