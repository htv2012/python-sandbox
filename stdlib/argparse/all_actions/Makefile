run: lint
	./main.py

lint: format
	ruff --fix .

format:
	ruff check--select I --fix .
	ruff format .

run: lint
	python3 main.py

lint: format
	ruff check . --fix

format:
	ruff check --select I --fix .
	ruff format .

