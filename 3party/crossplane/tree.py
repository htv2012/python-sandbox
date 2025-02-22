# tree.py
import operator

import click
import crossplane


def print_tree(nodes: list, get_value, get_children, prefix: str = ""):
    for index, node in enumerate(nodes):
        is_last = index == len(nodes) - 1
        connector = "└── " if is_last else "├── "
        click.echo(f"{prefix}{connector}", nl=False)

        children = get_children(node)
        if children:
            click.echo(click.style(get_value(node), fg="cyan"), color=True)
            print_tree(
                nodes=children,
                prefix=prefix + ("    " if is_last else "│   "),
                get_value=get_value,
                get_children=get_children,
            )
        else:
            click.echo(get_value(node))


def get_children(di: dict):
    try:
        return di["block"]
    except KeyError:
        return []


@click.command()
@click.argument("file")
def main(file):
    root = crossplane.parse(file)
    # root is a dict with 3 keys: status, errors, and config
    assert root["errors"] == []

    config = root["config"][0]
    print(config)
    # config is a dict with 4 keys: file, status, errors, parsed
    assert config["errors"] == []

    parsed = config["parsed"]
    # parsed is a list of directives
    # each directive is a dict with keys: directive, line, args, block
    print()
    print_tree(
        nodes=parsed,
        get_value=operator.itemgetter("directive"),
        get_children=get_children,
    )


if __name__ == "__main__":
    main()
