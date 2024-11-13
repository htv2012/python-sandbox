import logging


def test_tmp_path_factory_getbasetemp(tmp_path_factory):
    base = tmp_path_factory.getbasetemp()
    logging.debug("base=%r", base)
    assert base is not None


def test_tmp_path_factory_mktemp(tmp_path_factory):
    temp_dir = tmp_path_factory.mktemp("foo")
    logging.debug("temp_dir=%r", temp_dir)
    assert "foo" in temp_dir.name


def test_tmp_path_factory_create_file(tmp_path_factory):
    temp_file = tmp_path_factory.getbasetemp() / "newfile.txt"
    temp_file.write_text("hello")
    assert temp_file.read_text() == "hello"


def test_tmp_path(tmp_path):
    temp_filename = tmp_path / "newfile.txt"
    logging.debug("temp_filename=%r", temp_filename)
    assert not temp_filename.exists()
