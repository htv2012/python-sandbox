#!/usr/bin/env python3

import ast
import os
import contextlib
from ast import *


class Visitor(ast.NodeVisitor):
    def __init__(self, filename):
        path, _ = os.path.splitext(filename)
        with open(filename) as f:
            module = ast.parse(f.read(), path)
            self.path = path
            self.visit(module)

    @contextlib.contextmanager
    def path_descend(self, name):
        old_path = self.path
        self.path = '{}.{}'.format(self.path, name).lstrip('.')
        yield self.path
        self.path = old_path

    def visit_Module(self, node):
        print('{},{},{}'.format('module', self.path, self.path))
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        print('class,{},{}.{}'.format(node.name,self.path, node.name))
        with self.path_descend(node.name):
            self.generic_visit(node)

    def visit_Assign(self, node):
        for target in node.targets:
            print('value,{},{}.{}'.format(target.id, self.path, target.id))

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
    visitor = Visitor('simple.py')
