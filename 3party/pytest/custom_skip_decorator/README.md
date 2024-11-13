# How to Create a Custom Skip Decorator

First, decide on the name of the decorator. In this example, we use
`skip_if_env_var_undefined`.

Next, we create a conftest.py and create the `pytest_runtest_setup`
hook. In this hook, we look for a marker with the name we picked.
If found, we will perform some work to decide if we should skip the
current test or not.  See the `skip_if_env_var_undefined` for more
details.
