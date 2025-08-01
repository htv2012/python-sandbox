.PHONY: all clean install lab lint py run test

### Default target(s)
all: run

edit:
	$(EDITOR) -p src/config_choice/__init__.py src/config_choice/config/*.py

### Perform static analysis
lint:
	@uv run ruff check --select I --fix . --quiet
	@uv run ruff format . --quiet
	@uv run ruff check . --fix --quiet
	@uv run ty check .

### Run the project
run: lint
	#
	# Demo: choices
	#
	uv run config-choice --config=config1
	uv run config-choice --config=config2

	#
	# Demo: Aliases
	#
	uv run config-choice --config=normal

	#
	# Demo: test config
	#
	uv run config-choice --config=config1 --test-config=smoke

	#
	# Demo: Invalid choice
	#
	-uv run config-choice --config=foobar

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
