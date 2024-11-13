"""
Runs with
    python -m randomlib
"""

import argparse

from . import generate_emails, generate_names, generate_uris

parser = argparse.ArgumentParser()
parser.add_argument("kind", choices=["name", "names", "email", "emails", "uri", "uris"])
parser.add_argument("-c", "--count", type=int, default=1)
options = parser.parse_args()

generate = {
    "name": generate_names,
    "names": generate_names,
    "email": generate_emails,
    "emails": generate_emails,
    "uri": generate_uris,
    "uris": generate_uris,
}

print("\n".join(generate[options.kind](count=options.count)))
