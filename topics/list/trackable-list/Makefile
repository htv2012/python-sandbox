.PHONY: all clean install lab lint py run test

### Default target(s)
all: test run

edit:
	$(EDITOR) trackable-list

### Perform static analysis
lint:
	uv run ruff check --select I --fix . --quiet
	uv run ruff format . --quiet
	uv run ruff check . --fix --quiet
	uv run ty check .

### Run the project
run: lint
	uv run trackable-list

### Run unit tests
test: lint
	uv run pytest -s -vv

### Clean up generated files
clean:
	uv clean
	rm -fr .ruff_cache .venv

### Start a Python interpreter
py:
	uv run ipython

### Start a Jupyter Lab
lab:
	uv run jupyter lab

### Install this tool locally
install:
	uv tool install --upgrade .
