import ast
import collections
import os

try:
    5 / 0
except ZeroDivisionError:
    pass

try:
    "2" + 3
except TypeError:
    pass

try:
    os.unlink("/foobar")
except (OverflowError, ReferenceError, OSError):
    pass

try:
    x = 1
except:
    pass

try:
    x = 1
except Exception:
    pass

try:
    print("Exceptions:")
except IndentationError:
    print("ERROR")


def do_something():
    """
    Even exceptions handlers that are nested in functions, classes
    """
    try:
        x = 1
    except UnboundLocalError:
        pass


def find_ignored_exceptions(filename):
    with open(filename) as f:
        code = f.read()
        tree = ast.parse(code)

    ignore_counter = collections.Counter()
    for node in ast.walk(tree):
        if not isinstance(node, ast.ExceptHandler):
            continue

        ehandler = node
        nodes = list(ast.walk(ehandler))
        if isinstance(nodes[1], ast.Pass):
            # "except:"
            ignore_counter.update(["Exception"])
        elif isinstance(nodes[1], ast.Name) and isinstance(nodes[2], ast.Pass):
            # "except ErrorName:"
            print("Ignore:", nodes[1].id)
            ignore_counter.update([nodes[1].id])
        elif isinstance(nodes[1], ast.Tuple) and isinstance(nodes[2], ast.Pass):
            # "except (A, B, C):"
            for node in ast.walk(nodes[1]):
                if isinstance(node, ast.Name):
                    print("Ignore multi:", node.id)
                    ignore_counter.update([node.id])
        elif (
            isinstance(nodes[1], ast.Name)
            and isinstance(nodes[2], ast.Name)
            and isinstance(nodes[3], ast.Pass)
        ):
            # "except ValueError as e"
            print("Ignore named:", nodes[1].id)
            ignore_counter.update([nodes[1].id])

    return ignore_counter


print(find_ignored_exceptions(__file__))
