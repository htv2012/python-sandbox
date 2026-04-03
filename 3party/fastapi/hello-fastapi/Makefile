.PHONY: run all lint format

all: serve

run:
	http 'http://localhost:8000/'
	http 'http://localhost:8000/users/'
	http 'http://localhost:8000/users/?format=alias'
	http 'http://localhost:8000/users/501'
	http 'http://localhost:8000/users/501?format=alias'
	http 'http://localhost:8000/users/502'
	-http 'http://localhost:8000/users/503'

serve: lint
	uv run uvicorn main:app --log-level=debug --reload --host=0.0.0.0

doc:
	open "http://localhost:8000/docs"

lint: format
	uv run ruff check . --fix

format:
	uv run ruff check --select I --fix .
	uv run ruff format .

