.PHONY: all test run lint clean

### Default target(s)
all: run

### Perform static analysis
lint:
	uv tool run ruff check --select I --fix .
	uv tool run ruff format .
	uv tool run ruff check . --fix
	uv tool run ty check .

### Run the project
run: lint
	uv run ptree src
	uv run ptree samples/kens_books.json
	uv run ptree samples/kens_books.xml

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
