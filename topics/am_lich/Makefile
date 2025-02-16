.PHONY: all test run lint clean

### Default target(s)
all: run

### Perform static analysis
lint:
	uv tool run ruff check --select I --fix .
	uv tool run ruff format .
	uv tool run ruff check . --fix

### Run the project
run: lint
	uv run amlich tuoi "ty"
	uv run amlich nam 2025
	uv run amlich gio
	uv run amlich ten-tuoi \
		-t Ba 1941 \
		-t Má 1943 \
		-t x x \
		-t Cường 1963 \
		-t Huyền 1966 \
		-t Kenny 2006 \
		-t x x \
		-t Hải 1965 \
		-t Trang 1969 \
		-t Lynn 1998 \
		-t Erica 2000 \
		-t x x \
		-t Long 1969- \
		-t Lừng 1971 \
		-t Hân 2000 \
		-t x x \
		-t Ly 1970 \
		-t văn 1965- \
		-t Brandon 2003 \
		-t x x \
		-t Dương 1971 \
		-t Thanh 1976 \
		-t Cody 2005 \
		-t x x \
		-t "Bích Ngọc" 1973 \
		-t Dylan 2004 \
		-t Tiona 2006 \
		-t x x \
		-t Châu 1974 \
		-t "Kim Ngọc" 1977 \
		-t Nathan 2005 \
		-t Landon 2007

### Run unit tests
test: lint
	uv run pytest -s -v

### Clean up generated files
clean:
	uv clean
	rm -fr .ruff_cache .venv

### Install this tool for local use
install:
	uv tool install --upgrade .
