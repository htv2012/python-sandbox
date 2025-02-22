"""
tree.py

The `crossplane.parse()` function returns

    {
        "status": "ok",  # ok or error
        "errors": []     # List of errors
        "config": {
            "file":
            "status":
            "error":
            "parsed": [
                {
                    "directive": STR,  # Name, e.g. "user"
                    "line": NUM,       # Line number within the file
                    "args": [STR],     # Arguments
                    "block": [],       # Optional, a list of children directives
                },
            ]
        }
    }
"""

import click
import crossplane


def print_tree(nodes: list, prefix: str = ""):
    for index, node in enumerate(nodes):
        is_last = index == len(nodes) - 1
        connector = "└── " if is_last else "├── "
        click.echo(f"{prefix}{connector}", nl=False)

        name = node["directive"]
        children = node.get("block")
        if children:
            click.echo(click.style(name, fg="cyan"), color=True, nl=False)
            if name == "location":
                click.echo(" " + " ".join(node["args"]), nl=False)
            click.echo("")
            print_tree(
                nodes=children,
                prefix=prefix + ("    " if is_last else "│   "),
            )
        else:
            click.echo(name)


@click.command()
@click.argument("file")
def main(file):
    root = crossplane.parse(file)
    # root is a dict with 3 keys: status, errors, and config
    assert root["errors"] == []

    config = root["config"][0]
    # config is a dict with 4 keys: file, status, errors, parsed
    assert config["errors"] == []

    parsed = config["parsed"]
    # parsed is a list of directives
    # each directive is a dict with keys: directive, line, args, block
    print_tree(parsed)


if __name__ == "__main__":
    main()
