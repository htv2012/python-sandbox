import marshal
import os
import subprocess


def depot2local(depot_file):
    """Convert a file name from depot format to local format
    :param depot_file: a file name in depot format
    :return: The file name in the file system's local format
    >>> depot2file('//mydepot/file1.txt')
    '/Users/account/src/file1.txt'
    """
    stdout = subprocess.check_output(["p4", "-G", "fstat", depot_file])
    output = marshal.loads(stdout)
    return output["clientFile"]


def get_changed_files(change_list):
    """Get a list of files from a change list
    :param change_list: The change list number (could be a string or a number)
    :return: A list of tuples (filename, action) where as action can be 'add', 'edit', or 'delete'
    """
    stdout = subprocess.check_output(["p4", "-G", "describe", "-s", str(change_list)])
    output = marshal.loads(stdout)

    for n in range(len(output)):
        file_name = output.get("depotFile{}".format(n))
        if file_name is None:
            break
        action = output["action{}".format(n)]
        yield depot2local(file_name), action


def flake8(file_name):
    command = ["flake8", file_name]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    print(out)
    return process.returncode


def get_python_changed_files(change_list):
    """Generate a list of Python files that are added or edited in a change list
    :param change_list: The change list number (in str or int format)
    :return: A list of Python files that are added or edited
    """
    for file_name, action in get_changed_files(change_list):
        if action in ["add", "edit"] and file_name.endswith(".py"):
            yield file_name


if __name__ == "__main__":
    os.chdir("/Volumes/dev/native-dev")
    if any(map(flake8, get_python_changed_files(431619))):
        print("Error found")
