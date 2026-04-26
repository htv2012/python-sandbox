import jsonpath

import data


def main():
    names = jsonpath.findall("$..name", data.users)
    print(names)


if __name__ == "__main__":
    main()
