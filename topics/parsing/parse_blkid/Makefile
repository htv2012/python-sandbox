.PHONY: all test run lint edit clean

### Default target(s)
all: run

### Perform static analysis
lint:
	uv run ruff check --select I --fix .
	uv run ruff format .
	uv run ruff check . --fix

### Run the project
run: lint
	uv run blkid-tool

### Run unit tests
test: lint
	uv run pytest -s -v

### Clean up generated files
clean:
	uv clean
	rm -fr .ruff_cache .venv

### Edit project and run
dev: edit run

### Edit project
edit:
	nvim src/blkid_tool/tool.py

