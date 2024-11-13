We know that we cannot call a fixture directly, a get-around to
this restriction is to create a free function so that we can call
it directly. Next, we pass this function to `pytest.fixture()` to
create a fixture.

The free function is `generate_odd_number()` which resides in
numericlib.py and the fixture is `odd_number` which is in conftest.py
