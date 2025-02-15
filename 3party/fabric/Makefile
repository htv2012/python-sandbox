HOST ?= primary

run: lint
	uv run write_remote_with_progress_using_paramiko.py

lint: format
	uv tool run ruff check . --fix

format:
	uv tool run ruff check --select I --fix .
	uv tool run ruff format .
