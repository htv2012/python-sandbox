#!/usr/bin/env python3
import os
import re

# Pattern for place holders, e.g. {{ENV:HOME}} for bash $HOME
# We use re.VERBOSE to enable in-string comments
SUBSTITUTION_PATTERN = re.compile(
    r"""
    {{         # Literal
    ([^:]*)    # Group 1: The namespace, e.g. ENV, ALIAS
    :?         # Namespace and colon are optional
    (.*?)      # Group 2: The variable name
    }}         # Literal
    """,
    re.VERBOSE,
)


class Template:
    def __init__(self):
        self.namespaces = {
            "ENV": os.environ,
            "ALIAS": {
                "env1": {
                    "metadata": {
                        "name": "env-1",
                        "uid": "38d5a185-3a62-4010-aef9-0a1ae37db2e4",
                    }
                }
            },
        }

    def sub(self, text):
        """Substitude the placeholders within the text."""
        result = SUBSTITUTION_PATTERN.sub(self._lookup, text)
        return result

    def _dot_key_lookup(self, ns, dot_key):
        """Look up a dot key such as env1.metadata.name."""
        for key in dot_key.split("."):
            ns = ns[key]
        return ns

    def _lookup(self, match: re.Match):
        """Given a match object, substitude.

        The `re.sub()` function will call this method for each of
        the regular expression pattern matched.  The match object's
        groups will return the namespace (e.g. "ENV") and the dot
        key (e.g. "env1.metadata.name").  This method will then
        perform the look up in the correct namespace and travese
        the dictionary using the dot key to find the final value
        and return it.
        """
        namespace_selector, dot_key = [text.strip() for text in match.groups()]

        # Handle default namespace
        if dot_key == "":
            dot_key = namespace_selector
            namespace_selector = "ALIAS"

        namespace = self.namespaces[namespace_selector]
        result = self._dot_key_lookup(namespace, dot_key)
        return result


def main():
    """Entry"""
    template_text = (
        "My username is {{ ENV:USER }}.\n"
        "My home directory is {{ENV: HOME}}.\n"
        "My first environment is '{{ ALIAS : env1.metadata.name }}'.\n"
        "Its UID is {{ env1.metadata.uid }}."  # If no namespace, assume ALIAS
    )
    print("\nTEMPLATE:")
    print("---------")
    print(template_text)

    template = Template()
    out = template.sub(template_text)
    print("\nOUTPUT:")
    print("-------")
    print(out)
    print()


if __name__ == "__main__":
    main()
