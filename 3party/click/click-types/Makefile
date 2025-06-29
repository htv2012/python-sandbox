.PHONY: all clean install lab lint py run test

### Default target(s)
all: run

### Perform static analysis
lint:
	uv tool run ruff check --select I --fix .
	uv tool run ruff format .
	uv tool run ruff check . --fix

### Run the project
run: lint
	@echo ""
	uv run ct \
		--confirm yes \
		--date 2025-05-31 \
		--root-dir . \
		--run-type manual \
		--server foo.com:2400 \
		--transport "2000,Mercedes Benz,E Class"

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
