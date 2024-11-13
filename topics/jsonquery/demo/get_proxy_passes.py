#!/usr/bin/env python3
import pprint

import jsonquery

data = {
    "uriSnippets": [
        {
            "directives": [
                { "other": 1 },
                { "directive": "no" },
                { "directive": "proxy_pass1" },
                { "directive": "no again" }
            ]
        },
        { "directives": [] },
        {
            "directives": [
                { "directive": "proxy_pass2" },
                { "directive": "definitely no" }
            ]
        }
    ]
}

print("\n# Find all `directive`")
result = list(jsonquery.query(
    data,
    ("uriSnippets", "*", "directives", "*", "directive")
))

pprint.pprint(list(result))

print("\n# Find all `directive` with starts with `proxy_pass`")
result = list(jsonquery.query(
    data,
    ("uriSnippets", "*", "directives", "*", "directive"),
    predicate=lambda d: d.startswith("proxy_pass")
))
pprint.pprint(list(result))
