import jsonpath

import data


def main():
    matches = jsonpath.findall("$.users.*.name", data.users)
    print(f"{matches=}")
    for match in matches:
        print(f"{match=}")


if __name__ == "__main__":
    main()
