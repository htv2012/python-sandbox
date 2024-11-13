#!/usr/bin/env python3
import pytest


@pytest.fixture
def app(request):
    app_kind = request.node.get_closest_marker("app_kind")

    # There is no mark
    if app_kind is None:
        return "app"

    return f"{app_kind.args[0]}-app"


@pytest.mark.app_kind("web")
def test_web_app(app):
    assert app == "web-app"


@pytest.mark.app_kind("cli")
def test_cli_app(app):
    assert app == "cli-app"


def test_app(app):
    assert app == "app"
