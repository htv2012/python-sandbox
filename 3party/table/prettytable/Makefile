script = prettytable_tryout.py

run: lint
	@uv run $(script)

lint: format
	@uv run ruff check --quiet --fix .

format:
	@uv run ruff check --select I --fix --quiet .
	@uv run ruff format . --quiet

