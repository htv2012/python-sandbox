import json
from functools import wraps
from atom.test_utilities.test_case_info import TestCaseInfo


def tci_file(json_filename):
    with open(json_filename) as f:
        json_data = json.load(f)
        test_cases = [TestCaseInfo(str(k), **v) for k, v in json_data.items()]
        return test_cases


if __name__ == '__main__':
    print tci_file('data.json')