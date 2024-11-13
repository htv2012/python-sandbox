def ep(root: str):
    root = root.removesuffix("/")

    def make(path: str):
        nonlocal root
        return f"{root}/{path}"

    return make
