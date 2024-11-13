.PHONY: all test lint

WEEKDAY ?= $(shell date '+%A')
$(info today is a $(WEEKDAY))

all: test

lint:
	ruff check . --fix
	ruff format .

test: lint
	pytest -v -m $(WEEKDAY)

