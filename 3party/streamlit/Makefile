help:
	@echo make slider
	@echo make sidebar
	@echo make start
	@echo make csv
	@echo make format
	@echo make lint

slider: lint
	streamlit run 00_slider.py

sidebar: lint
	streamlit run 01_sidebar.py

start: lint
	streamlit run 02_getting_started.py

csv: lint
	streamlit run 03_display_csv.py

format:
	ruff check--select I --fix .
	isort *.py

lint: format
	ruff --fix .


.PHONY: help lint format slider sidebar start csv
