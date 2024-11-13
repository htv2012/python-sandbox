.PHONY: help search traversal

help:
	@echo make traversal
	@echo make search
	@echo make tree
	
search: lint
	python3 search.py

traversal: lint
	python3 traversal.py

tree: lint
	python3 summary_tree.py nginx.conf

lint:
	ruff check --fix .
	ruff check --select I --fix .
	ruff format .

