#!/usr/bin/env python3
"""Demo template."""

import os

from template import Template

DOC = """
ABOUT ME
  Username: {{env.USER}}
  Home dir: {{ env.HOME }}

ENV1
  Name: {{ alias.env1.metadata.name }}
  UUID: {{ alias.env1.metadata.uid }}
""".strip()


def main():
    """Entry"""

    print()
    print("-" * 80)
    print("TEMPLATE")
    print("-" * 80)
    print(DOC)

    print()
    print("-" * 80)
    print("OUTPUT")
    print("-" * 80)
    tem = Template(
        env=os.environ,
        alias={
            "env1": {
                "metadata": {
                    "name": "env-1",
                    "uid": "1e9bc88f-fe35-401c-84d7-1cc1600078be",
                }
            }
        },
    )
    new_doc = tem.expand(DOC)
    print(new_doc)


if __name__ == "__main__":
    main()
