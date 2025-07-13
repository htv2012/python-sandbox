.PHONY: all clean install lab lint py run test

### Default target(s)
all: test run

edit:
	$(EDITOR) class-param

### Perform static analysis
lint:
	@uv run ruff check --select I --fix . --quiet
	@uv run ruff format . --quiet
	@uv run ruff check . --fix --quiet

### Run the project
run: lint
	@echo ""
	uv run class-param --user 501,karen,1
	@echo ""
	uv run class-param --user 502,john,is_admin=0,shell=zsh
	@echo ""
	uv run class-param --server example.com
	@echo ""
	uv run class-param --server example.com,port=2233

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
