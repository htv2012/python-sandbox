#!/usr/bin/env python
import os


def get_doc_dir():
    for doc_dir in ("~/Documents", "~/My Documents"):
        doc_dir = os.path.expanduser(doc_dir)
        if os.path.isdir(doc_dir):
            return doc_dir

    return None


if __name__ == "__main__":
    doc_dir = get_doc_dir()
    print(("Doc dir: {}".format(doc_dir)))
