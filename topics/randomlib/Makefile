.PHONY: demo format lint

demo: lint
	@echo --------------------------------------------------------------------------------
	@echo Run Demo
	@echo --------------------------------------------------------------------------------
	python3 randomlib_demo.py
	@echo --------------------------------------------------------------------------------
	@echo Generate 5 Names from Command Line
	@echo --------------------------------------------------------------------------------
	python3 -m randomlib --count=5 names
	@echo --------------------------------------------------------------------------------
	@echo Generate 5 Emails from Command Line
	@echo --------------------------------------------------------------------------------
	python3 -m randomlib --count=5 emails
	@echo --------------------------------------------------------------------------------
	@echo Generate a Single URI from Command Line
	@echo --------------------------------------------------------------------------------
	python3 -m randomlib uri

format:
	ruff check--select I --fix .
	ruff format .

lint: format
	ruff .

