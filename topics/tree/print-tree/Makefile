.PHONY: all test run lint clean

### Default target(s)
all: run

### Perform static analysis
lint:
	uv run ruff check --select I --fix .
	uv run ruff format .
	uv run ruff check . --fix
	uv run ty check .

### Run the project
run: lint
	uv run ptree src
	@echo ""
	@echo "--------------------------------------"
	@echo ""
	uv run ptree samples/kens_books.json
	@echo ""
	@echo "--------------------------------------"
	@echo ""
	uv run ptree samples/kens_books.yaml
	@echo ""
	@echo "--------------------------------------"
	@echo ""
	uv run ptree samples/kens_books.xml
	@echo ""
	@echo "--------------------------------------"
	@echo ""
	uv run ptree pyproject.toml

### Run unit tests
test: lint
	uv run pytest -s -v

### Clean up generated files
clean:
	uv clean
	rm -fr .ruff_cache .venv

### Install this tool locally
install:
	uv tool install --upgrade .
