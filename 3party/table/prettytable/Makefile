script = prettytable_tryout.py

run: lint
	uv run $(script)

lint: format
	uv run ruff check . --fix

format:
	uv run ruff check --select I --fix .
	uv run ruff format .

