.PHONY: all clean install lab lint py run test

### Default target(s)
all: run

edit:
	$(EDITOR) co

### Perform static analysis
lint:
	uv tool run ruff check --select I --fix .
	uv tool run ruff format .
	uv tool run ruff check . --fix

### Run the project
run: lint
	@echo ""
	uv run co up --server=foo --port=8888
	@echo ""
	uv run co down --server=bar --port=9999
	@echo ""
	uv run co

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
