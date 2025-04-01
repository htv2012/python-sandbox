#!/usr/bin/env python3
"""Generate random names and other objects such as URIs, emails, or locations."""

import itertools
import pathlib
import random


class _Randomized:
    """Provide random names and other random objects."""

    def __init__(self):
        data_dir = pathlib.Path(__file__).parent

        with open(data_dir / "adjectives.txt", encoding="utf-8") as stream:
            adjectives = set(stream.read().split())

        with open(data_dir / "nouns.txt", encoding="utf-8") as stream:
            nouns = set(stream.read().split())

        self.adjective_noun_pairs = list(itertools.product(adjectives, nouns))
        random.shuffle(self.adjective_noun_pairs)
        self.adjective_noun_pairs = iter(self.adjective_noun_pairs)

    def generate_name(
        self,
        separator: str = "-",
        prefix: str = "",
        suffix: str = "",
        max_length: int = 64,
    ) -> str:
        """Generate a single random name such as 'lazy-dog'.

        :param separator: The separator between the words
        :param: prefix: The result will always starts with this text
        :param suffix: The result will always ends with this text
        :param max_length: The maximum length, including the prefix and suffix
        :return: A random name.
        """
        root = separator.join(next(self.adjective_noun_pairs))
        if max_length > 0:
            adjusted_length = max_length - len(prefix) - len(suffix)
            root = root[:adjusted_length]
        name = f"{prefix}{root}{suffix}"
        return name

    def generate_names(
        self,
        count: int = 1,
        separator: str = "-",
        prefix: str = "",
        suffix: str = "",
        max_length: int = 64,
    ) -> list[str]:
        """Generate random names.

        Note that even when this function always return a list,
        even for one name. The caller can call `next_name` if they
        want a single string instead.

        :param count: The number of names
        :param separator: The separator between the words
        :param: prefix: The result strings will always start with this text
        :param suffix: The result strings will always end with this text
        :param max_length: The maximum length, including the prefix and suffix
        :return: A list of random names.
        """
        assert count >= 0
        names = [
            self.generate_name(separator, prefix, suffix, max_length)
            for _ in range(count)
        ]
        return names

    def generate_email(self, domain: str = ".com") -> str:
        """Generate a random email such as 'funny@hamster.com'.

        :param: domain: The top-level domain, which includes the dot
        :return: A random email
        """
        email = self.generate_name(separator="@", suffix=domain)
        return email

    def generate_emails(self, count: int = 1, domain: str = ".com") -> list[str]:
        """Generate a list of random emails.

        :param count: The number of emails
        :param: domain: The top-level domain, which includes the dot
        :return: A list of emails
        """
        assert count >= 0
        emails = [self.generate_email(domain) for _ in range(count)]
        return emails

    def generate_uri(self, protocol: str = "http", domain: str = ".com") -> str:
        """Generate a random URI such as 'http://eliptical-bamboo.com'.

        :param protocol: 'http', 'https', 'tcp', or 'udp'
        :param: domain: The top-level domain, which includes the dot
        :return: A random URI.
        """
        uri = self.generate_name(prefix=f"{protocol}://", suffix=domain)
        return uri

    def generate_uris(
        self, count: int = 1, protocol: str = "http", domain: str = ".com"
    ) -> list[str]:
        """Generate random URIs.

        :param count: The number of URIs
        :param protocol: 'http', 'https', 'tcp', or 'udp'
        :param: domain: The top-level domain, which includes the dot
        :return: A list of random URIs.
        """
        assert count >= 0
        uris = [self.generate_uri(protocol, domain) for _ in range(count)]
        return uris
