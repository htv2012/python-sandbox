.PHONY: all test run lint clean

### Default target(s)
all: run

### Perform static analysis
lint:
	uv tool run ruff check --select I --fix .
	uv tool run ruff format .
	uv tool run ruff check . --fix

### Run the project
run: lint
	#uv run amlich -d 1911
	#uv run amlich -d 2025
	uv run amlich a2d
	uv run amlich d2a 2025

### Run unit tests
test: lint
	uv run pytest -s -v

### Clean up generated files
clean:
	uv clean
	rm -fr .ruff_cache .venv

