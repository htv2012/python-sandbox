from __future__ import print_function

import json
import textwrap
from collections import namedtuple
from itertools import dropwhile, takewhile

FileAction = namedtuple("FileAction", "depot_path action")
ChangeListInfo = namedtuple(
    "ChangeListInfo", "changelist,date,time,user,status,description,files"
)


def parse_file_action(text):
    depot_path, _, action = text.split()
    file_action = FileAction(depot_path, action)
    return file_action


def parse_change_output(lines):
    # Skip the comment--lines which starts with a hash sign
    lines = dropwhile(lambda line: line.startswith("#"), lines)

    for line in lines:
        if "Change:" in line:
            _, changelist = line.split()
        elif "Date:" in line:
            _, datestr, timestr = line.split()
        elif "User:" in line:
            _, user = line.split()
        elif "Status:" in line:
            _, status = line.split()
        elif "Description:" in line:
            description = "".join(
                takewhile(lambda a: a.startswith(" ") or a.startswith("\t"), lines)
            )
            description = textwrap.dedent(description)
        elif "Files:" in line:
            files = [parse_file_action(a) for a in lines if a.strip()]

    change_list_info = ChangeListInfo(
        changelist, datestr, timestr, user, status, description, files
    )
    return change_list_info


def main():
    with open("p4_change_output.txt") as ifile:
        change_list_info = parse_change_output(ifile)
        print("Change:", change_list_info.changelist)
        print("Date time:", change_list_info.date, change_list_info.time)
        print("User:", change_list_info.user)
        print("Status:", change_list_info.status)
        print("Description:")
        print(change_list_info.description)
        print("Files:")
        for fa in change_list_info.files:
            print(fa.depot_path, ">>>", fa.action)

        print("\n\n")
        as_dict = change_list_info._asdict()
        print(json.dumps(as_dict, indent=4))


if __name__ == "__main__":
    main()
