.PHONY: all clean install lab lint py run test

### Default target(s)
all: run

edit:
	$(EDITOR) main.py

### Perform static analysis
lint:
	@uv run ruff check --select I --fix . --quiet
	@uv run ruff format . --quiet
	@uv run ruff check . --fix --quiet

### Run the project
run: lint
	uv run main.py
	@echo ""
	uv run main.py --server '{"host": "myhost", "port": 2200, "secured": false}'
	@echo ""
	uv run main.py --user '{"uid": 501, "alias": "anna", "is_admin": true, "groups": ["sudo", "print"]}'
	@echo ""
	uv run main.py --band '{"name": "Peter, Paul, and Mary", "members": ["Peter", "Paul", "Mary"]}'
	@echo ""
	@echo "# Demo: invalid argument"
	-uv run main.py --server '{"host": "myhost", "port": "2200", "secured": false}'
	

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
