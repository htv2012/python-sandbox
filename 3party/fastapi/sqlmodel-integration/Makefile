API_ROOT := http://localhost:8000/heroes/

.PHONY: \
	all \
	clean \
	install \
	lab \
	lint \
	py \
	rename \
	serve \
	run \
	test \

### Default target(s)
all: serve

### Start the server
serve:
	-rm db.sqlite
	uv run fastapi dev src/sqlmodel_integration

### Clean up generated files
clean:
	uv clean
	rm -fr .ruff_cache .venv

### Install this tool locally
install:
	uv tool install --upgrade .

### Run Jupyter lab
lab:
	JUPYTER_CONFIG_DIR=etc uv run jupyter lab --notebook-dir=etc/notebooks

### Perform static analysis
lint:
	uv tool run ruff check --select I --fix .
	uv tool run ruff format .
	uv tool run ruff check . --fix

### Open a Python shell
py:
	PYTHONSTARTUP= uv run ipython --profile-dir=./etc/ipython

### Rename the project
rename:
	uv run etc/set_project_name.py

### Run the project
run: lint
	uv run http POST $(API_ROOT) name="Johnny B. Goode" age:=25 secret_name="Stingray"
	uv run http POST $(API_ROOT) name="Dianna Le" age:=22 secret_name="Black Scorpion"
	uv run http POST $(API_ROOT) name="Thomas Tran" age:=27 secret_name="The Crusher"
	uv run http GET $(API_ROOT)


### Run unit tests
test: lint
	PYTHONBREAKPOINT="pudb.set_trace" uv run pytest -vv

