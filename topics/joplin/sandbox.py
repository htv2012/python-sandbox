#!/usr/bin/env python3
import pathlib

class Data:
    def __init__(self, title, content, metadata):
        self.title = title
        self.content = content
        self.metadata = metadata

    @classmethod
    def from_text(cls, text):
        id_index = text.index("id: ")
        meat = text[:id_index].strip()
        title, content = meat.split("\n", 1)

        meta_text = text[id_index:]
        metadata = dict(line.split(": ") for line in meta_text.strip().splitlines())
        return cls(title, content, metadata)

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r", encoding="utf-8") as stream:
            text = stream.read()
        return cls.from_text(text)


root = pathlib.Path("~/workspaces/joplin/raw").expanduser()
assert root.is_dir()
filename = next(root.glob("*"))
data = Data.from_file(filename)
print(data.title)

