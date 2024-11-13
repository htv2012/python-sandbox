#!/usr/bin/env python3
"""
Demo: Get an item from 1Password
"""
import getpass

import onepassword


def main():
    """ Entry """
    url = "https://my.1password.com"
    email = "haivu2004@gmail.com"
    secret_key = getpass.getpass("Enter secret key: ")
    item = onepassword.get_item(url, email, secret_key, "FictionAccount")

    print()
    print(f"UUID: {item.uuid}")
    print(f"Title: {item.overview.title}")
    print(f"User name: {item.username}")
    print(f"Password: {item.password}")
    print(f"URL: {item.overview.url}")
    print(f"Tags: {', '.join(item.overview.tags)}")
    print(f"Notes: {item.details.notesPlain}")


if __name__ == "__main__":
    main()
