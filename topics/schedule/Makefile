try: lint
	python3 schedule_tryout.py

lint: format
	ruff . --fix

format:
	ruff check--select I --fix .
	ruff format .

