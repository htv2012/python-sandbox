.PHONY: clean, all

all: mylib.zip
	PYTHONPATH=mylib.zip python3 example.py

mylib.zip:
	python3 create_zip_library.py

clean:
	rm -f mylib.zip
	rm -fr lib/__pycache__

