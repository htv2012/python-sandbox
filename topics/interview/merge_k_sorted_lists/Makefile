test: lint 
	PYTHONPATH=$(PYTHONPATH):../lib pytest -v

lint: format
	ruff . ../lib --fix

format:
	black  ../lib/*.py *.py 
	ruff format ../lib . 

