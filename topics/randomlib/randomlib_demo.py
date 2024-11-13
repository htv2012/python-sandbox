#!/usr/bin/env python3
import randomlib


def main():
    """Entry"""
    print("\n# Random names")
    for name in randomlib.generate_names(count=2):
        print(name)
    print(randomlib.generate_name())  # Single name

    print("\n# Random emails")
    for email in randomlib.generate_emails(count=2):
        print(email)
    print(randomlib.generate_email())  # Single email

    print("\n# Random URIs")
    for uri in randomlib.generate_uris(count=2):
        print(uri)
    print(randomlib.generate_uri())  # Single uri


if __name__ == "__main__":
    main()
