.PHONY: all clean install lab lint py run test

### Default target(s)
all: run

edit:
	$(EDITOR) config-choice

### Perform static analysis
lint:
	@uv run ruff check --select I --fix . --quiet
	@uv run ruff format . --quiet
	@uv run ruff check . --fix --quiet

### Run the project
run: lint
	uv run config-choice --venue devpit1
	uv run config-choice --venue devpit
	uv run config-choice --venue treasureIsland
	uv run config-choice --venue devpit1
	uv run config-choice --venue fs1
	-uv run config-choice --venue foobar

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
