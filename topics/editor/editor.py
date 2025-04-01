#!/usr/bin/env python
"""
A simple tool to invoke a text editor to edit a file or a block of
text.
"""

import os
import shlex
import subprocess
import tempfile


def edit_file(filename, editor=None):
    """
    Invokes an editor to edit a file. If an editor is not specified,
    look up the environment variables EDITOR and then VISUAL. If
    none found, fall back to "nano".

    :param filename: The name of the file
    :param editor: The text editor such as "vim" or "nano"
    """
    editor = editor or os.getenv("EDITOR") or os.getenv("VISUAL") or "nano"
    editor = shlex.split(editor, posix=True)
    subprocess.check_call(editor + [filename])


def edit(text: str, editor: str = None, file_extension: str = None):
    """
    Invokes an editor (see edit_file) to edit some text

    :param text: The block of text to edit
    :param editor: The text editor such as "vim" or "nano"
    :param file_extension: The file extension such as ".txt"
    :return: The edited text
    """
    tmp = tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", suffix=file_extension, delete=False
    )

    with tmp:
        tmp.write(text)

    try:
        edit_file(tmp.name, editor=editor)
        with open(tmp.name, encoding="utf-8") as stream:
            content = stream.read()
        return content
    finally:
        os.unlink(tmp.name)
