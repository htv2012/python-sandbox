import pathlib
import sys

import pytest

# Get a list of libraries to import
LIB_DIR = pathlib.Path(__file__).with_name("lib")
LIBS = [path.stem for path in LIB_DIR.glob("lib*.py")] + ["lib_ghost"]
sys.path.append(str(LIB_DIR))


@pytest.fixture(params=LIBS)
def get_home(request):
    library_name = request.param
    library = pytest.importorskip(library_name, reason=f"Cannot import {library_name}")

    try:
        return getattr(library, "get_home")
    except AttributeError:
        pytest.skip(f"{library_name} does not implement or export get_home()")
