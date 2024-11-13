#!/usr/bin/env python
import ast
import contextlib


class Visitor(ast.NodeVisitor):
    def __init__(self, path):
        self.path = path

    # @contextlib.contextmanager
    # def path_descend(self, name):
    #     old_path = self.path
    #     self.path = '{}.{}'.format(self.path, name).lstrip('.')
    #     yield self.path
    #     self.path = old_path
    #
    # def _is_testcase(self, node):
    #     for base_class in node.bases:
    #         name = getattr(base_class, 'id', None) or getattr(base_class, 'attr', None)
    #         if name == 'TestCase':
    #             return True
    #     return False
    #
    # def visit_ClassDef(self, node):
    #     if not self._is_testcase(node):
    #         return
    #
    #     print('class,{},{}.{}'.format(node.name, self.path, node.name))
    #
    #     with self.path_descend(node.name):
    #         self.generic_visit(node)

    def visit_FunctionDef(self, node):
        if node.name != '__setstate__':
            return
        print(node.name)


    def visit_Dict(self, node):
        print('Dict keys:', node.keys)


def main():
    filename = 'sample.py'
    module_str = filename.replace('.py', '')
    with open(filename) as stream:
        code = stream.read()
    module = ast.parse(code, filename)
    visitor = Visitor(filename)
    visitor.visit(module)


if __name__ == '__main__':
    main()
