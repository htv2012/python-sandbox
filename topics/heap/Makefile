run:
	uv run python heap.py
	
test: lint
	uv run pytest -s -vv

lint: format
	uv run ruff check . --fix

format:
	uv run ruff check --select I --fix .
	uv run ruff format .

