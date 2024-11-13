sandbox: lint
	python3 -i pastebin.py

run: lint
	python3 main.py

lint: format
	ruff check . --fix

format:
	ruff check --select I --fix .
	ruff format .
