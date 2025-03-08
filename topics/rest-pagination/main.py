"""
Rest API pagination concept


Normally, with pagination, we have to get the first page, process
the data, then get the next and next. The `iter_users` function
demonstrate a different approach: it hides the paging details and
provide a generator which yields users data, thus simplify caller's
code.
"""

import itertools

import requests


def iter_users():
    url = "https://reqres.in/api/users?per_page=3"
    session = requests.Session()

    for page in itertools.count(1):
        resp = session.get(f"{url}&page={page}")
        data = resp.json()["data"]
        if not data:
            break
        yield from data


def print_user(user):
    print(f"- [{user['id']}] {user['first_name']} {user['last_name']}")


def main():
    print("\n# Pagination Demo")
    for user in iter_users():
        print_user(user)

    print("\n# Get the First 5 Users")
    for user, _ in zip(iter_users(), range(5)):
        print_user(user)

    print("\n# Find Those Whose Last Name Starts with Letter 'F'")
    found = filter(lambda user: user["last_name"].startswith("F"), iter_users())
    for user in found:
        print_user(user)


if __name__ == "__main__":
    main()
