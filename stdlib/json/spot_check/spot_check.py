def json_bfs(obj, key_path: tuple = None):
    key_path = key_path or tuple()
    if isinstance(obj, dict):
        for key, value in obj.items():
            yield from json_bfs(value, key_path + (key,))
    elif isinstance(obj, list):
        for index, value in enumerate(obj):
            yield from json_bfs(value, key_path + (index,))
    else:
        yield obj, key_path


def get_value(obj, key_path: tuple):
    for key in key_path:
        obj = obj[key]
    return obj


def spot_check(actual, expected):
    errors = []
    for expected_value, path in json_bfs(expected):
        try:
            actual_value = get_value(actual, path)
        except (KeyError, IndexError) as error:
            actual_value = error
        if actual_value != expected_value:
            errors.append(
                AssertionError(
                    f"{path=}, expected={expected_value!r}, actual={actual_value!r}"
                )
            )

    if errors:
        raise ExceptionGroup("Spot check failed", errors)
