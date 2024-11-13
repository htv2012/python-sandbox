SCRIPT ?= unpack_using_shutil_custom_format.py
all: my.zip my.tar.lz
	ruff format -q .
	ruff check -q --select I --fix .
	ruff check -q --fix .

	@-rm -fr out
	python3 $(SCRIPT)
	tree

clean:
	-rm -fr out my.zip my.tar.lz

my.zip:
	zip my.zip *.py

my.tar.lz:
	tar --lzma -cf my.tar.lz *.py

