from print_tree import print_tree

obj = {
    "metadata": {
        "name": "env1",
        "description": "My first environment",
    }
}

print_tree(
    nodes=list(obj.items()),
    get_value=lambda item: item[0],
    get_children=lambda item: item[1],
)