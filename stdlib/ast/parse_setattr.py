#!/usr/bin/env python
import ast
import contextlib

code = """
class Foo(TestCase, something.ElseClass):
    def __getattr__(self):
        return {
            'abcd': 1,
            'efgh': 2,
            'ijkl': 3,
        }
        
class Bar(testcase.TestCase):
    pass
    
class Moo:
    pass
"""

class Visitor(ast.NodeVisitor):
    def __init__(self, path):
        self.path = path

    @contextlib.contextmanager
    def path_descend(self, name):
        old_path = self.path
        self.path = '{}.{}'.format(self.path, name).lstrip('.')
        yield self.path
        self.path = old_path

    def _is_testcase(self, node):
        for base_class in node.bases:
            name = getattr(base_class, 'id', None) or getattr(base_class, 'attr', None)
            if name == 'TestCase':
                return True
        return False

    def visit_ClassDef(self, node):
        if not self._is_testcase(node):
            return

        print('class,{},{}.{}'.format(node.name,self.path, node.name))

        with self.path_descend(node.name):
            self.generic_visit(node)

    def visit_FunctionDef(self, node):
        for decor in node.decorator_list:
            if 'property' == decor.id:
                print('property,{},{}.{}'.format(node.name, self.path,node.name))
                break
        else:
            print('function,{},{}.{}'.format(node.name, self.path,node.name))
        with self.path_descend(node.name):
            self.generic_visit(node)

    def visit_Dict(self, node):
        print('Dict keys:', node.keys)


if __name__ == '__main__':
    filename = 'simple.py'
    module_str = 'a.b.c.simple'
    module = ast.parse(code, filename)
    visitor = Visitor(module_str)
    visitor.visit(module)