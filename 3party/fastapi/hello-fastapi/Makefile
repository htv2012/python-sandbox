.PHONY: run all lint format

all: server

client:
	http --print=b 'http://localhost:8000/'
	http --print=b 'http://localhost:8000/users/'
	http --print=b 'http://localhost:8000/users/501'
	http --print=b 'http://localhost:8000/users/502'
	-http --print=b 'http://localhost:8000/users/503'

server: lint
	uv run uvicorn main:app --log-level=debug --reload --host=0.0.0.0

lint: format
	uv run ruff check . --fix

format:
	uv run ruff check --select I --fix .
	uv run ruff format .

