help:
	@awk '/^[a-z]+:/ { sub(/:/, "", $$1); print "make " $$1 }' Makefile

run: lint
	python3 forwardable_tryout.py

lint: format
	ruff . --fix

format:
	ruff format .
	

