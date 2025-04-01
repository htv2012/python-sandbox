#!/usr/bin/env python3
"""
In a markdown doc, move all the links to the bottom.
"""

import re

LINK_PATTERN = re.compile(
    """
        # Group 1: The [text] part
        (
            \[
            [^]]+
            \]
        )

        # Group 2: The (...) part
        \(
        (
            .+?
        )
        \)
        """,
    re.VERBOSE,
)


class LinksOrganizer:
    """Organize the links by moving them to the end of the document."""

    def __init__(self):
        self.links = {}

    def _collect_links(self, match: re.Match) -> str:
        """
        Given a re.Match object, return just the name part and store
        the URL part.
        """
        name, url = match.groups()
        self.links[name] = (name, url)
        return name

    @property
    def epilogue(self):
        """Return the epilog: A list links."""
        return "\n".join("%s: %s" % (value) for value in self.links.values())

    def organize(self, markdown_document):
        """Given a mardown text document, move the links to the end."""
        self.links = {}
        out = LINK_PATTERN.sub(self._collect_links, markdown_document)
        out = f"{out}\n\n{self.epilogue}"
        return out


DOCUMENT = """
This is [my search](https://google.com), which I use daily.
For mail, I'm using [Gmail](https://mail.google.com).
""".strip()


def main():
    """Entry"""
    print(DOCUMENT)
    print("---")
    link_organizer = LinksOrganizer()
    new_document = link_organizer.organize(DOCUMENT)
    print(new_document)


if __name__ == "__main__":
    main()
