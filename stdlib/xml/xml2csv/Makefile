run: lint
	@echo =============================================================
	python3 xml2csv.py
	@echo =============================================================
	python3 xml2csv_etree.py

lint: format
	ruff check . --fix

format:
	ruff check --select I --fix .
	ruff format .

