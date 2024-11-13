HOSTS ?= primary

info: lint
	fab --hosts=$(HOSTS) info

primary:
	$(MAKE) HOSTS=primary

mercury:
	$(MAKE) HOSTS=mercury

nuc:
	$(MAKE) HOSTS=nuc

all:
	$(MAKE) HOSTS=nuc,mercury,primary


lint: format
	ruff check . --fix

format:
	ruff check --select I --fix .
	ruff format .

