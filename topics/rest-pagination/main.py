#!/usr/bin/env python3
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


def iter_users(
    base_url: str,
    per_page: int = 5,
    page: int = 1,
    per_page_label: str = "per_page",
    page_label: str = "page",
    get_data=None,
    session: requests.Session = None,
):
    def default_get_data(resp: requests.Response):
        return resp.json()["data"]

    session = session or requests.Session()
    if get_data is None:
        get_data = default_get_data

    for page in itertools.count(page):
        url = f"{base_url}?{per_page_label}={per_page}&&{page_label}={page}"
        resp = session.get(url)
        data = get_data(resp)
        if not data:
            break
        yield from data


def print_user(user):
    print(f"- [{user['id']:>2}] {user['first_name']} {user['last_name']}")


def main():
    print("\n# Handle pagination")
    users = iter_users("https://reqres.in/api/users")
    for user in users:
        print_user(user)

    print("\n# Start on page 2")
    users = iter_users(
        base_url="https://reqres.in/api/users",
        page=2,
        per_page=5,
    )
    for user in users:
        print_user(user)


if __name__ == "__main__":
    main()
