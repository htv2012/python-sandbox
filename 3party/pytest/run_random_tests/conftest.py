import json
import random

import pytest


def reduce_list(original, keep_percentage: float):
    # Indices to be deleted
    reduction_count = int(len(original) * (1.0 - keep_percentage))
    tbd = random.sample(range(len(original)), reduction_count)
    tbd = sorted(tbd, reverse=True)

    # Delete
    for index in tbd:
        del original[index]


def pytest_collection_modifyitems(
    session: pytest.Session, config: pytest.Config, items: list[pytest.Item]
):
    test_options_path = config.rootpath / "test_options.json"
    if test_options_path.exists():
        with open(test_options_path) as stream:
            options = json.load(stream)
    else:
        options = {}

    reduce_list(items, options.get("reduction", 1.0))
