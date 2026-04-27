import jsonpath

import data


def main():
    matches = jsonpath.finditer("$.users[*].name", data.users)
    for match in matches:
        print(f"{match}")


if __name__ == "__main__":
    main()
