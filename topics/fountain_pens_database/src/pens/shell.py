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
        self.categories = self.df["Category"].dropna().str.lower().unique().tolist()
        self.columns = self.df.columns.str.lower().tolist()

    def do_pen(self, args_text):
        """Show my pens. Short hand for ls --category pen"""
        self.do_ls(f"--category 'fountain pen' {args_text}")

    def do_ink(self, args_text):
        self.do_ls(f"--category ink {args_text}")

    def do_notebook(self, args_text):
        self.do_ls(f"--category notebook {args_text}")

    def do_case(self, args_text):
        self.do_ls(f"--category case {args_text}")

    def do_ls(self, args_text):
        parser = argparse.ArgumentParser(exit_on_error=False, add_help=False)
        parser.add_argument("-c", "--category", choices=self.categories)
        parser.add_argument(
            "-s", "--sort", default=[], action="append", choices=self.columns
        )
        try:
            args = parser.parse_args(shlex.split(args_text))
        except argparse.ArgumentError:
            parser.print_help()
            return

        df = self.df
        if args.category:
            df = df[self.df["Category"] == args.category.title()]

        if not args.sort:
            args.sort = ["Category", "Brand", "Model"]
        args.sort = [col.title() for col in args.sort]
        df = df.sort_values(args.sort)
        show(df)

    def emptyline(self):
        pass

    def do_EOF(self, _):
        print()
        return True

    do_q = do_EOF
    do_exit = do_EOF
    do_p = do_pen
    do_n = do_notebook
    do_i = do_ink
    do_c = do_case


def interactive_shell(df):
    shell = Shell(df)
    shell.cmdloop()
