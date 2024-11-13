from spot_check import spot_check


def test_json_diff():
    ref = {
        "metadata": {
            "name": "My stuff",
            "description": "My things which I use most often",
            "tags": ["things", "stuff", "my"],
        },
        "food": {
            "meat": ["lamb", "pork", "chicken"],
            "veggie": ["On choy", "potato"],
        },
    }

    actual_obj = {
        "metadata": {
            "name": "Your stuff",
            "tags": ["things", "stuff", "his"],
        },
        "food": {
            "meat": ["lamb", "pork", "duck"],
            "veggie": ["On choy", "potato"],
        },
    }
    spot_check(actual=actual_obj, expected=ref)
