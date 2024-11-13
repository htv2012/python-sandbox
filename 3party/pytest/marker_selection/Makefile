.PHONY: test

test_license:
	ruff format .
	ruff check --select I --fix .
	ruff check --fix .

	@echo -e "\n#"
	@echo "# Test all licenses"
	@echo "#"
	pytest --no-header -v

	@echo -e "\n#"
	@echo "# Skip trial license"
	@echo "#"
	pytest --no-header -v -m "not license(license_kind='trial')" 

	@echo -e "\n#"
	@echo "# Only trial license"
	@echo "#"
	pytest --no-header -v -m "license(license_kind='trial')" 

