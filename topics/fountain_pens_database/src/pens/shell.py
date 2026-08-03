"""Interactive shell"""

import argparse
import cmd
import shlex

INTRODUCTION = """
Welcome to my stationery listing. Type help for a list of commands.
"""


def show(df):
    df = df.sort_values(["Brand", "Model"])
    df = df.reset_index(drop=True)
    print(df.to_string())


class Shell(cmd.Cmd):
    prompt = "\n> "
    intro = INTRODUCTION

    def __init__(self, df):
        super().__init__(self)
        self.df = df

    def do_pens(self, args_text):
        df = self.df[self.df["Category"] == "Fountain Pen"]
        show(df)

    def do_ls(self, args_text):
        parser = argparse.ArgumentParser()
        parser.add_argument("-p", "--pens", default=False, action="store_true")
        args = parser.parse_args(shlex.split(args_text))
        df = self.df
        if args.pens:
            df = self.df[self.df["Category"] == "Fountain Pen"]
        show(df)

    def emptyline(self):
        pass

    def do_EOF(self, _):
        return True

    do_q = do_EOF
    do_exit = do_EOF
    do_p = do_pens


def interactive_shell(df):
    shell = Shell(df)
    shell.cmdloop()
