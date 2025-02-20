def print_tree(nodes: list, get_value, get_children, prefix: str = ""):
    for index, node in enumerate(nodes):
        is_last = index == len(nodes) - 1
        connector = "└── " if is_last else "├── "
        print(f"{prefix}{connector}{get_value(node)}")

        print_tree(
            get_children(node),
            prefix=prefix + ("    " if is_last else "│   "),
            get_value=get_value,
            get_children=get_children,
        )
