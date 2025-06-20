.PHONY: all clean install lab lint py run test

### Default target(s)
all: run

edit:
	$(EDITOR) ec

### Perform static analysis
lint:
	uv tool run ruff check --select I --fix .
	uv tool run ruff format .
	uv tool run ruff check . --fix

### Run the project
run: lint
	@echo ""
	#
	# Use default value
	#
	uv run ec

	@echo ""
	#
	# Case insenstive
	#
	uv run ec --star Marilyn

	@echo ""
	#
	# Same config as Marilyn
	#
	uv run ec --star monroe

	@echo ""
	#
	# Dash will be converted to underscore
	#
	uv run ec --star Mary-Lou

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
