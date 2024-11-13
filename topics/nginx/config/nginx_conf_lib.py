#!/usr/bin/env python3
"""
nginx_conf_lib.py - A collection of NGINX configuration tools.
"""

import collections
import dataclasses
import shlex
from typing import List


@dataclasses.dataclass()
class Directive:
    """A nginx.conf directive, which could contain nested directives."""

    name: str
    args: List[str] = dataclasses.field(default_factory=list)
    children: List = dataclasses.field(default_factory=list, repr=False)

    @classmethod
    def from_list(cls, lst):
        """
        Given a list, construct a directive.

        >>> Directive.from_list(["location", "/hello"])
        Directive(name='location', args=['/hello'])
        """
        lst = lst.copy()
        name = lst.pop(0)
        return cls(name, lst)

    def __iter__(self):
        return iter(self.children)


def parse(text):
    """Parse text into a list of Directive objects."""
    tokens = shlex.shlex(text, posix=True, punctuation_chars=";")
    tokens.whitespace_split = True
    directives = []
    stack = [directives]
    lst = []

    for token in tokens:
        if token == ";":
            directive = Directive.from_list(lst)
            stack[-1].append(directive)
            lst = []
        elif token == "{":
            directive = Directive.from_list(lst)
            stack[-1].append(directive)
            stack.append(directive.children)
            lst = []
        elif token == "}":
            stack.pop()
        else:
            lst.append(token)
    return directives


def depth_first_traversal(directive: Directive, visit, parents: tuple = None):
    """Depth-first traverse."""
    parents = parents or tuple()
    visit(directive, parents)
    for node in directive:
        depth_first_traversal(node, visit, parents=parents + (directive,))


def breadth_first_traversal(directive: Directive, visit, parents: tuple = None):
    """Breadth-first traverse."""
    parents = parents or tuple()
    stack = collections.deque([(directive, parents)])
    while stack:
        directive, parents = stack.popleft()
        visit(directive, parents)
        # stack.extend(directive)
        for sub_directive in directive:
            stack.append((sub_directive, parents + (directive,)))


def find_all(directive, predicate):
    """Search a directive using a predicate."""
    found = (node for node in directive if predicate(node))
    return found


def find_next(directive, predicate):
    found = next(find_all(directive, predicate))
    return found


# A few predicates
def by_name(name):
    """Search by name."""

    def match(directive):
        """Return True if a directive name matched."""
        return directive.name == name

    return match


def by_any_args(args):
    def match(directive):
        return set(args).issubset(directive.args)

    return match


def all_of(*predicates):
    def match(directive):
        return all(predicate(directive) for predicate in predicates)

    return match


def any_of(*predicates):
    def match(directive):
        return any(predicate(directive) for predicate in predicates)

    return match


def negative(predicate):
    def match(directive):
        return not predicate(directive)

    return match
