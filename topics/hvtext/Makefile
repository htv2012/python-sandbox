.PHONY: all py test run lint clean

### Default target(s)
all: test run

### Perform static analysis
lint:
	uv tool run ruff check --select I --fix .
	uv tool run ruff format .
	uv tool run ruff check . --fix

### Start an iPython interpreter
py:
	uv run ipython

### Run the project
run: lint
	uv run python -m hvtext.serial "edit 25"

### Run unit tests
test: lint
	uv run pytest -vv --doctest-modules

### Clean up generated files
clean:
	uv clean
	rm -fr .ruff_cache .venv

### Install this tool locally
install:
	uv tool install --upgrade .
