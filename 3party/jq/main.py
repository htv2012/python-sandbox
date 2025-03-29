import json
import pathlib

import jq
import rich


def main():
    with open(pathlib.Path(__file__).with_name("data.json")) as stream:
        data = json.load(stream)

    print("\n# Show Authors")
    out = (
        jq.compile(".[] | {author: .commit.author.name, email: .commit.author.email}")
        .input_value(data)
        .all()
    )
    rich.print_json(data=out)


if __name__ == "__main__":
    main()
