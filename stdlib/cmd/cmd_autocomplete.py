#!/usr/bin/env python
"""
Demo: autocompletion via function complete_*
"""
import cmd
import readline
import shlex


def remove_delimiters(to_be_removed):
    existing = readline.get_completer_delims()
    new_delimiters = set(existing) - set(to_be_removed)
    new_delimiters = ''.join(new_delimiters)
    readline.set_completer_delims(new_delimiters)

class MyCmd(cmd.Cmd):
    prompt = "> "

    def do_show(self, arguments):
        """ Shows the system settings """
        print(f"information for {arguments!r} to be implemented")

    def complete_show(self, text, line, begidx, endidx):
        valid = sorted([
            "network:cluster",
            "network:dns",
            "network:gateway",
            "openconfig:system-config",
            "openconfig:system-config:config",
            "openconfig:system-config:clock",
            "openconfig:system-config:alarms",
            "openconfig:system-bak:peers",
            "openconfig:system-bak:schedules",
            "openconfig:logging",
            "openconfig:printing",
        ])
        chosen = [x for x in valid if x.startswith(text)]
        return chosen

    def do_EOF(self, s):
        """quit - quit the program"""
        return True
    do_q = do_EOF


if __name__ == "__main__":
    # Tells readline that colon is not a word delimiter
    remove_delimiters("-:")
    cmd = MyCmd()
    cmd.cmdloop()
