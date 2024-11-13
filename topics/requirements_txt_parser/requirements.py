#!/usr/bin/env python3


class Requirements:
    """
    A class representing the requirements.txt. Example usage:

        with open("requirements.txt") as stream:
            contents = stream.read()
        req = Requirements(contents)
        for dependency in req:
            print(dependency)        
    """
    def __init__(self, text=None):
        self.flags = []
        self.dependencies = []

        if text is not None:
            self.parse(text)

    def __iter__(self):
        return iter(self.dependencies)

    def parse(self, text):
        """
        Parses the contents of the requirements.txt
        """
        for line in text.splitlines():
            line = line.strip()
            if line.startswith("#"):
                continue
            elif not line:
                continue
            elif line.startswith("-"):
                self.flags.append(line)
            else:
                self.dependencies.append(line)
