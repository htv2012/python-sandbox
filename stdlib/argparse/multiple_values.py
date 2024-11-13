"""
csv arguments parsing
"""
import argparse


def parser_test(parser):
    def do_test(argv):
        options = parser.parse_args(argv)
        print("{!r} ==> {!r}".format(argv, options))

    do_test(["-b1,2,3,4"])
    do_test(["-b1,2,3,4", "--bug=5,6", "-b", "7,8,9"])


class CsvSplitter(argparse.Action):
    def __call__(self, parser, namespace, values, option_string):
        list_object = getattr(namespace, self.dest) or []
        setattr(namespace, self.dest, list_object)

        for value in values:
            sublist = [int(x) for x in value.split(",")]
            list_object.extend(sublist)


if __name__ == "__main__":
    print("\n# Using type")
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--bug", type=lambda arg: [int(x) for x in arg.split(",")])
    parser_test(parser)

    print("\n# Using action class")
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--bug", action=CsvSplitter, nargs="*")
    parser_test(parser)
