import marshal
import os
import subprocess
from collections import Sequence


class PerforceError(Exception):
    pass


class Perforce(object):
    def __init__(self, client=None, port=None):
        client = client or os.environ.get("P4CLIENT", "")
        port = port or os.environ.get("P4PORT", "")
        os.environ["P4CLIENT"] = client
        os.environ["P4PORT"] = port

    def add(self, file_names):
        cmd = ["p4", "add"]
        cmd.extend(_make_list(file_names))
        output = subprocess.check_output(cmd)

        added_files = _extract_filenames_from_output(output)
        return added_files

    def edit(self, file_names, change_list=None, preview_only=False):
        """Check out one or more files for editing
        :param file_names: A single or a list of file names to check out
        :param change_list: Optional change list number
        :param preview_only: Do not actually check out
        :return: A list of enlistment file names
        """
        cmd = ["p4", "edit"]
        if change_list is not None:
            cmd.extend(["-c", str(change_list)])
        if preview_only:
            cmd.append("-n")
        cmd.extend(_make_list(file_names))

        output = subprocess.check_output(cmd)
        opened_files = _extract_filenames_from_output(output)
        return opened_files

    def revert(self, file_names, unchanged_files_only=False, change_list=None):
        cmd = ["p4", "revert"]
        if change_list is not None:
            cmd.extend(["-c", str(change_list)])
        if unchanged_files_only:
            cmd.append("-a")
        cmd.extend(_make_list(file_names))

        subprocess.check_call(cmd)

    def revert_unchanged(self, file_names, change_list=None):
        self.revert(file_names, change_list=change_list, unchanged_files_only=True)

    def opened(self, file_names=None):
        cmd = ["p4", "opened"]
        if file_names is not None:
            cmd.extend(_make_list(file_names))

        output = subprocess.check_output(cmd)
        opened_files = _extract_filenames_from_output(output)
        return opened_files

    def fstat(self, path):
        command = ["p4", "-G", "fstat", path]
        marshal_output = subprocess.check_output(command)
        stat = marshal.loads(marshal_output)
        return stat

    def local2depot(self, path):
        stat = self.fstat(path)
        return stat["depotFile"]


# ==================================================================================================
# Helpers
# ==================================================================================================


def _extract_filenames_from_output(output):
    # sample of output:
    # //sandbox/basetest.py#5 - opened for edit
    # //sandbox/delete_tests.py#5 - opened for edit
    # //sandbox/hello.py#4 - opened for edit
    file_names = [line.split("#")[0] for line in output.splitlines() if "#" in line]
    return file_names or None


def _make_list(entity):
    """Takes in one or more string and return a list of strings
    :param entity: A single string, or list of strings
    :return: A list of strings
    """
    if isinstance(entity, str):
        return [entity]
    elif isinstance(entity, Sequence):
        return entity
    else:
        raise ValueError("Entity must a a string or list: {}".format(entity))
