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
	uv run main.py --data abc,1,1.5,true,verbose=false,level=5 
	@echo ""
	uv run main.py --server myhost,2200,false
	@echo ""
	uv run main.py --server myhost,port=3344,secured=True
	@echo ""
	uv run main.py --user 501,anna,false
	@echo ""
	uv run main.py --user 1,root,is_admin=true

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
