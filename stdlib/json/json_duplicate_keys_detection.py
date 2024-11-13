import json
import pprint


def consolidate_duplicate_keys(list_of_pairs):
    # Add all values to a list
    result = dict()
    for k, v in list_of_pairs:
        result.setdefault(k, []).append(v)

    # Convert values from lists to strings
    result = {k: ";".join(v) for k, v in result.items()}
    return result


def main():
    json_text = """
    {
        "1061": "GROCERY",
        "1073": "GM-HBC",
        "4220": "PRODUCE",
        "958": "MEAT",
        "958": "DAIRY",
        "958": "FROZEN"
    }
    """
    obj = json.loads(json_text, object_pairs_hook=consolidate_duplicate_keys)
    pprint.pprint(obj)


if __name__ == "__main__":
    main()
