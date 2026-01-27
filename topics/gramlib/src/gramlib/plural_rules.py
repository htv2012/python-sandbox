"""Pluralize words"""

import re


def plural(count: int, word: str) -> str:
    """Form the count + word, taking care of correct singular and plural forms.

    Examples:

        >>> plural(1, "bulb")
        '1 bulb'

        >>> plural(2, 'bulb')
        '2 bulbs'

        >>> plural(1, "child|children")
        '1 child'

        >>> plural(2, "child|children")
        '2 children'

        >>> plural(1, "batch(es)")
        '1 batch'

        >>> plural(2, "batch(es)")
        '2 batches'
    """
    if "|" in word:
        singular_form, plural_form = word.split("|")
    elif (matched := re.match(r"(\w+)\((\w+)\)", word)) is not None:
        singular_form = matched[1]
        plural_form = matched[1] + matched[2]
    else:
        singular_form, plural_form = word, word + "s"

    return f"{count} {plural_form if count > 1 else singular_form}"
