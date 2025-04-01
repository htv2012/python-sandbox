#!/usr/bin/env python
import collections
import os
import re
import sys


def parse_serial_filename(filename):
    """
    Parses a file name (a base name without paths, but with extension)
    and returns a dictionary with the following parts:

    - serial: the serial number
    - suffix: the alpha+dash part that follows a suffix
    - extension: the file extension
    - event: the rest of the file name

    E.g. for filename = 'john_wedding_2012_0087a.jpg', the parts are as
    followed:

    - serial    = 0087
    - suffix    = 'a'
    - extension = '.jpg'
    - event     = 'john_wedding_2012'

    E.g. for filename = '089_San_Diego_Zoo_2012.jpg', the parts are as
    followed:

    - serial    = 089
    - suffix    = ''
    - extension = '.jpg'
    - event     = 'San_Diego_Zoo_2012'

    """
    patterns = [
        # Match example: 0089a_San_Diego_Zoo_2012.jpg
        """
            (?P<serial>\d+)                # Serial number
            (?P<suffix>[a-zA-Z-]*)         # Suffix
            _                              # Separator
            (?P<event>.+)                  # Event's name
            (?P<extension>\.[a-zA-Z0-9]+)  # File extension, with dot
        """,
        # Match example: john_wedding_2012_0087End.jpg
        """
            (?P<event>.+)                  # Event's name
            _
            (?P<serial>\d+)                # Serial number
            (?P<suffix>[a-zA-Z]*)          # Suffix (_0087End ==> 'End')
            (?P<extension>\.[a-zA-Z0-9]+)  # File extension, with dot
        """,
    ]

    for pattern in patterns:
        matched = re.match(pattern, filename, re.VERBOSE)
        if matched:
            parts = matched.groupdict()
            parts["iserial"] = int(parts["serial"].lstrip("0"))
            return parts
    return {}


def unify_filename(filename, serial_width=4):
    print("DBG: filename: {}".format(filename))
    parts = parse_serial_filename(filename)
    if parts:
        if serial_width == 0:
            serial_width = len(parts["serial"])
        parts["serial"] = int(parts["serial"].lstrip("0"))
        new_filename = "{event}_".format(**parts)
        new_filename += "{serial:0{w}}".format(w=serial_width, **parts)
        new_filename += "{suffix}{extension}".format(**parts)
        print("DBG:      new: {}".format(new_filename))


fmt_string = """\n{0}
- Event:     {event}
- Serial:    {serial}
- Suffix:    {suffix}
- Extension: {extension}"""

if __name__ == "__main__":
    if len(sys.argv) < 2:
        root_dir = "/Volumes/haibo/do_not_back_up/Videos/PhimBo"
    else:
        root_dir = sys.argv[1]

    os.chdir(root_dir)
    files = collections.defaultdict(set)
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            parts = parse_serial_filename(filename)
            if parts:
                files[parts["event"]].add(parts["iserial"])

    for filename, episodes in files.items():
        first_episode = 1
        last_episode = max(episodes)
        all_episodes = set(range(first_episode, last_episode + 1))
        missing_episodes = all_episodes - episodes
        print("{1:3} {0}".format(filename, last_episode), end=" ")
        if missing_episodes:
            print("- missing:", end=" ")
            print(", ".join(str(e) for e in missing_episodes), end=" ")
        print()
