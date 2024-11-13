HOST ?= primary

run: lint
	python3 fabric_tryout.py $(HOST)

hosts: lint
	python3 get_hosts_from_ssh_cfg.py

lint: format
	ruff . --fix

format:
	ruff check--select I --fix .
	ruff format .
