run: lint
	python3 concurrent_tasks.py

compare: lint
	python3 synchronous.py
	python3 as_completed_example.py

lint: format
	ruff check . --fix

format:
	ruff check --select I --fix .
	ruff format .

