"""
Scenario: load a JSON string, but use OrderedDict to ensure keys order
"""

import json
from collections import OrderedDict

json_str = """
[
    {"uid": 501, "alias": "bob", "shell": "bash"},
    {"uid": 502, "alias": "alice", "shell": "tcsh"}
]
"""

rows = json.loads(json_str, object_pairs_hook=OrderedDict)
headers = list(rows[0].keys())
assert headers == ["uid", "alias", "shell"]
