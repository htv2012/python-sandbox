#!/usr/bin/env python3
"""Demo: Round trip: json -> box -> json."""

import box


def main():
    data = {
        "metadata": {
            "name": "myenv",
            "description": "My First environment",
            "tags": ["sandbox", "experimental"],
        }
    }
    print("\n#Original data:")
    print(data)

    print("\n# Roundtrip data:")
    bx = box.Box(data)
    round = bx.to_dict()
    print(round)

    assert round == data


if __name__ == "__main__":
    main()
