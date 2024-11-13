def find_all_paths(g, start):
    if start not in g:
        return []

    seen = set()

    def bfs(src, path=None):
        path = path or []
        if src in seen:
            yield path
        seen.add(src)
        path.append(src)
        for intermediate in g[src]:
            yield from bfs(intermediate)

    yield from bfs(start)


g = {"a": {("b", 2)}, "b": {("c", 3)}}
for path in find_all_paths(g, "a"):
    print(path)
