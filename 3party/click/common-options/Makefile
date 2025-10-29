.PHONY: all clean install lab lint py run test

### Default target(s)
all: run

edit:
	$(EDITOR) main.py

### Perform static analysis
lint:
	@uv tool run ruff check --select I --fix . --quiet
	@uv tool run ruff format . --quiet
	@uv tool run ruff check . --fix --quiet

### Run the project
run: lint
	@echo "================================================================================"
	@echo "# Demo: Common options"
	@echo "================================================================================"
	uv run main.py common --help
	@echo "================================================================================"
	@echo "# Demo: Common with customization"
	@echo "================================================================================"
	uv run main.py customize --help

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
