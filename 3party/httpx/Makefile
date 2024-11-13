help:
	@awk '/^[a-z]+:/ { sub(/:/, "", $$1); print "make " $$1 }' Makefile

run: lint
	python -i httpx_tryout.py

lint: format
	ruff . --fix

format:
	ruff check--select I --fix .
	ruff format .

