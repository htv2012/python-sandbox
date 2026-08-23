.PHONY: all lint run

### Default target(s)
all: run

### Perform static analysis
lint:
	@uv tool run ruff check --select I --fix . --quiet
	@uv tool run ruff format . --quiet
	@uv tool run ruff check . --fix --quiet

### Run the project
run: lint
	./mmap_tryout.py

