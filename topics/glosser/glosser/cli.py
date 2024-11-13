import argparse
import cmd
import dataclasses
import pathlib
import shlex
import sqlite3


@dataclasses.dataclass
class Glossary:
    term: str
    summary: str
    defails: str = None

    @classmethod
    def factory(cls, _, row):
        return cls(*row)

    def __format__(self, spec):
        if not spec:
            spec = "c"
        if spec == "c":
            # Columns format
            return f"| {self.term:<8} | {self.summary:<60} |"
        elif spec == "csv":
            return f"{self.term},{self.summary},{self.defails}"



SQL_TABLE = "glossary"
SQL_CREATE_TABLE = f"CREATE TABLE {SQL_TABLE} (term TEXT, summary TEXT, details TEXT)"


def parse_command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--db", required=True)
    options = parser.parse_args()
    return options


def create_db(path):
    with sqlite3.connect(path) as conn:
        conn.execute(SQL_CREATE_TABLE)
        conn.commit()


def connect_to_db(path):
    if not path.exists():
        create_db(path)
    conn = sqlite3.connect(path)
    conn.row_factory = Glossary.factory
    return conn


def add_term(db: sqlite3.Connection, cmdline: str):
    args = shlex.split(cmdline)
    parser = argparse.ArgumentParser(prog="add")
    parser.add_argument("term")
    parser.add_argument("summary")
    parser.add_argument("details", nargs="*", default="")

    try:
        options = parser.parse_args(args)
        print(options)
    except SystemExit as error:
        print(error)
        return

    db.execute(
        f"INSERT INTO {SQL_TABLE} (term, summary, details) VALUES (?, ?, ?)",
        (options.term, options.summary, options.details),
    )
    db.commit()


def lookup_term(db: sqlite3.Connection, term: str):
    term = f"%{term}%"
    sql = f"SELECT * from {SQL_TABLE} WHERE term LIKE ?"
    for row in db.execute(sql, (term,)):
        print(f"{row}")


class GlossaryCLI(cmd.Cmd):
    prompt = "G> "
    intro = "type help for a list of valid commands, Ctrl+D to exit"

    def __init__(self, db):
        super().__init__()
        self.db = db

    def do_EOF(self, s):
        """quit - quit the program"""
        return True

    do_q = do_EOF

    def emptyline(self):
        pass

    def do_add(self, arg):
        add_term(self.db, arg)

    do_a = do_add

    def do_lookup(self, arg):
        lookup_term(self.db, arg)

    do_l = do_lookup
    do_f = do_lookup
    do_s = do_lookup
    do_look = do_lookup


def main():
    options = parse_command_line()
    db_path = pathlib.Path(options.db)
    db = connect_to_db(db_path)
    cli = GlossaryCLI(db)
    cli.cmdloop()
