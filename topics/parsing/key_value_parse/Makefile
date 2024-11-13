.PHONY: help parse_os_release parse_product


help:
	@echo Try the following
	@echo make parse_os_release
	@echo make parse_product


# Parses /etc/os-release
parse_os_release:
	./kv_parse_demo.py etc_os-release.txt


# Parses /etc/PRODUCT
parse_product:
	./kv_parse_demo.py etc_product.txt
