.PHONY: all clean install lab lint py run test

### Default target(s)
all: test run

edit:
	$(EDITOR) main.py

### Perform static analysis
lint:
	@uv run ruff check --select I --fix . --quiet
	@uv run ruff format . --quiet
	@uv run ruff check . --fix --quiet
	@uv run ty check .

### Run the project
run: lint
	@echo ""
	@echo "#"
	@echo "# Demo: Using JSON string to create objects"
	@echo "#"
	uv run main.py --server '{"host": "myhost", "port": 2200, "secured": false}'
	@echo ""
	uv run main.py --user '{"uid": 501, "alias": "anna", "is_admin": true, "groups": ["sudo", "print"]}'

	@echo ""
	@echo "#"
	@echo "# Demo: create more complex objects"
	@echo "#"
	uv run main.py --testbed @testbeds.yaml:testbed1
	@echo ""
	uv run main.py --testbed @testbeds.yaml:testbed2
	@echo ""
	uv run main.py --testbed @testbed3.yml
	@echo ""
	uv run main.py --testbed '{"server": {"host": "host4", "port": 4444, "secured": true}, "user": {"uid": 4004, "alias": "user4"}}'

	@echo ""
	@echo "#"
	@echo "# Demo: invalid argument"
	@echo "#"
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
