from behave import given, then, when


@given("we have behave installed")
def step_impl(context):  # noqa: F811
    pass


@when("we implement a test")
def step_impl(context):  # noqa: F811
    assert True


@then("behave will test it for us!")
def step_impl(context):  # noqa: F811
    assert context.failed is False
