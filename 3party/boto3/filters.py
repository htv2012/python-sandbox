import pathlib


def is_file(obj):
    return not obj.key.endswith("/")


def is_python(obj):
    path = pathlib.Path(obj.key)
    return path.suffix == ".py"
