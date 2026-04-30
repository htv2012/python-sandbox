run: lint
	uv run main.py

lint: format
	uv run ruff check . --fix

format:
	uv run ruff check --select I --fix .
	uv run ruff format .

