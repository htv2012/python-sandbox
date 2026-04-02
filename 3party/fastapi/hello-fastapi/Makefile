.PHONY: run all lint format

all: server

client:
	http 'http://localhost:8000/'
	http 'http://localhost:8000/users/'
	http 'http://localhost:8000/users/501'
	http 'http://localhost:8000/users/502'
	-http 'http://localhost:8000/users/503'

server: lint
	uv run uvicorn main:app --log-level=debug --reload --host=0.0.0.0

lint: format
	uv run ruff check . --fix

format:
	uv run ruff check --select I --fix .
	uv run ruff format .

