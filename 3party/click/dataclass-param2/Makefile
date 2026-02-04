.PHONY: all clean install lab lint py run test

### Default target(s)
all: run

### Perform static analysis
lint:
	@uv run ruff check --select I --fix . --quiet
	@uv run ruff format . --quiet
	@uv run ruff check . --fix --quiet

### Run the project
run: lint
	uv run main.py --help
	@echo "================================================================================"
	uv run main.py --user-alias=anna --user-uid=501 --user-keys=1 --user-keys=7 --user-groups sudo --user-groups print --user-admin --user-department engineer

### Run unit tests
test: lint
	uv run pytest -s -v

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
