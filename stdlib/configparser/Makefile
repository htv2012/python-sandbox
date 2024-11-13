SCRIPT:=simple.py
run: lint
	python3 $(SCRIPT)

lint: format
	ruff check . --fix

format:
	ruff check --select I --fix .
	ruff format .

