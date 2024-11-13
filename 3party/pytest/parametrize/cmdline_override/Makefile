.PHONY: all us international lint format

all: lint us international

us:
	pytest -s -v

international:
	pytest -s -v --test-data-files asia.yaml europe.yaml

lint: format
	ruff check . --fix
	
format:
	ruff check --select I --fix .
	ruff format .