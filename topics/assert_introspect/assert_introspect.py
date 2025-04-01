import argparse
import ast
import os


def flag_assert_that_never_fail(node, filename, line):
    if isinstance(node.test, ast.Tuple) and node.msg is None:
        error_template = "\n{}({}): The following assert will never fail:"
        print(error_template.format(filename, node.lineno))
        print(line)


def find_bad_assert(filename):
    with open(filename) as f:
        try:
            lines = f.read()
            code = ast.parse(lines, filename=filename)
            lines = lines.splitlines()
            for node in ast.walk(code):
                if isinstance(node, ast.Assert):
                    flag_assert_that_never_fail(node, filename, lines[node.lineno - 1])
        except IndentationError as e:
            error_template = "\n{}: file has indentation error"
            print(error_template.format(e.filename))
            print(e.text)
            print("{}^".format(" " * e.offset))
        except SyntaxError as e:
            error_template = "\n{}({}): file contains syntax error:"
            print(error_template.format(filename, e.lineno))
            print(e.text.strip())
            print("{}^".format(" " * e.offset))
        except TypeError:
            error_template = "\n{}: file contains type error:"
            print(error_template.format(filename))


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("root")
    options = argument_parser.parse_args()

    for cwd, subdirs, filenames in os.walk(options.root):
        for filename in filenames:
            if os.path.splitext(filename)[-1] == ".py":
                filename = os.path.join(cwd, filename)
                find_bad_assert(filename)
