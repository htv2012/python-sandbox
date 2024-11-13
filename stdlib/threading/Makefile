.PHONY: help lint format max wait barrier 

help:
	@echo Targets are:
	@awk -F ':' '/^[a-z]/ { print "make", $$1 }' Makefile | sort

barrier: lint
	python3 synchronize_using_barrier.py

wait: lint
	python wait_using_event.py

max: lint
	python max_threads_at_once.py

obj: lint
	python thread_object.py
	
format:
	ruff format .
	ruff check--select I --fix .

lint: format
	ruff *.py