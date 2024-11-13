#!/usr/bin/env python3
import yaml


class Monster(yaml.YAMLObject):
    yaml_tag = "!Monster"

    def __init__(self, name, hp, ac, attacks):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.attacks = attacks

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"name={self.name!r}"
            f", "
            f"hp={self.hp!r}"
            f", "
            f"ac={self.ac!r}"
            f", "
            f"attacks={self.attacks!r}"
            f")"
        )


YAML_TEXT = """!Monster
    name: Cave spider
    hp: [2, 6]
    ac: 16
    attacks: [BITE, HURT]
"""

YAML_LIST = """
- !Monster
    name: Cave spider
    hp: [2, 6]
    ac: 16
    attacks: [BITE, HURT]
- !Monster
    name: Angry Cow
    hp: [1, 2]
    ac: 11
    attacks: [SQUIRT MILK, RAM, WAG TAIL]
"""


def main():
    """Entry"""
    print("\n# Raw YAML text")
    print(YAML_TEXT)

    print("\n# Deserialize")
    monster = yaml.load(YAML_TEXT, Loader=yaml.Loader)
    print(monster)

    print()
    print("\n# Raw YAML text")
    print(YAML_LIST)

    print("\n# Deserialize")
    monsters = yaml.load(YAML_LIST, Loader=yaml.Loader)
    for monster in monsters:
        print(monster)


if __name__ == "__main__":
    main()
