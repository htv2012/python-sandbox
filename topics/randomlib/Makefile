.PHONY: demo format lint

demo: lint
	@echo ""
	uv run python randomlib_demo.py
	@echo ""
	uv run python -m randomlib --count=5 names
	@echo ""
	uv run python -m randomlib --count=5 emails
	@echo ""
	uv run python -m randomlib uri

format:
	uv run ruff check --select I --fix .
	uv run ruff format .

lint: format
	uv run ruff check .

