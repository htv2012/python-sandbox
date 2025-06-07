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
	@echo ""
	uv run dysub put
	@echo ""
	uv run dysub get
	@echo ""
	uv run dysub get-status
	@echo ""
	uv run dysub show root

### Run unit tests
test: lint
	PYTHONPATH=./src uv run pytest -s -v

### Clean up generated files
clean:
	uv clean
	rm -fr .ruff_cache .venv

