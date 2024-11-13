help:
	# Show a list of targets
	@awk '/^[a-z]+:/ { sub(/:/, "", $$1); print "make", $$1 }' Makefile

test: lint
	pytest -s -v

keypath: lint
	python3 key_path.py 

run: lint
	python3 main.py

lint: format
	ruff . --fix

format:
	ruff check--select I --fix .
	ruff format .

