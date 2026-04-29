import jsonpath

import banner
import data


def main():
    banner.banner("finditer")
    matches = jsonpath.finditer("$.users[*].name", data.users)
    for match in matches:
        print(f"- {match.obj}")

    banner.banner("finditer with filter")
    matches = jsonpath.finditer(
        "$.users[?@.score < _.threshold]",
        data.users,
        filter_context={"threshold": 90},
    )

    print("score  name")
    for match in matches:
        print(f"{match.obj['score']:>5}  {match.obj['name']}")


if __name__ == "__main__":
    main()
