import csv
import json
import random

import pytest


def load_test_options(path):
    with open(path) as stream:
        options = json.load(stream)
    return options


def pytest_collection_modifyitems(
    session: pytest.Session, config: pytest.Config, items: list[pytest.Item]
):
    options = load_test_options(config.rootpath / "test_options.json")

    # Get a list of tests which were tested
    tested_path = config.rootpath / ".tested.csv"
    history = set()
    if tested_path.exists():
        with open(tested_path) as stream:
            history = set(tuple(row) for row in csv.reader(stream))

    # Find those tests with mark=long
    long_tests = {
        (str(item.path), item.name): item
        for item in items
        if list(item.iter_markers(name="long"))
    }
    if len(history) >= len(long_tests):
        history = set()

    for key in list(history):
        try:
            long_tests[key].add_marker(pytest.mark.skip(reason="tested"))
            del long_tests[key]
        except KeyError:
            history.discard(key)

    # Select some tests to run
    batch_size = min(options["batch_size"], len(long_tests))
    for key in random.sample(sorted(long_tests), batch_size):
        history.add(key)
        del long_tests[key]

    # Update the tested file
    with open(tested_path, "w") as stream:
        writer = csv.writer(stream)
        writer.writerows(history)

    # Mark the rest as skipped
    for item in long_tests.values():
        item.add_marker(pytest.mark.skip(reason="time constrain"))
