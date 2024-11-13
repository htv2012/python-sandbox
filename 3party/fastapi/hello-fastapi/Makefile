.PHONY: run all lint format

all: server

client:
	http --print=b 'http://localhost:8000/'
	http --print=b 'http://localhost:8000/items/'
	http --print=b 'http://localhost:8000/items/501'
	http --print=b 'http://localhost:8000/items/502'

server: lint
	uvicorn main:app --log-level=debug --reload --host=0.0.0.0

lint: format
	ruff check . --fix

format:
	ruff check --select I --fix .
	ruff format .

