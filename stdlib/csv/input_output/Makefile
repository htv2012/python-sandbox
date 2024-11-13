.PHONY: from_stdin help from_stdin2 from_file from_string

help:
	@echo make targets
	@echo make help
	@echo make from_file
	@echo make from_stdin
	@echo make from_stdin2
	@echo make from_string

from_string:
	python3 from_string.py

from_stdin:
	python3 from_stdin.py < data.csv

from_stdin2:
	python3 from_file_or_stdin.py < data.csv

from_file:
	python3 from_file_or_stdin.py data.csv

