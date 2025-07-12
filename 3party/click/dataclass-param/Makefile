.PHONY: all clean install lab lint py run test

### Default target(s)
all: run

edit:
	$(EDITOR) dataclass-param

### Perform static analysis
lint:
	@uv run ruff check --select I --fix . --quiet
	@uv run ruff format . --quiet
	@uv run ruff check . --fix --quiet

### Run the project
run: lint
	@echo ""
	uv run dataclass-param --user uid=501,alias=karenc,shell=bash --admin alias=root,uid=0,shell=sh,serial=1 --raw foo=1,bar=1.5

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
