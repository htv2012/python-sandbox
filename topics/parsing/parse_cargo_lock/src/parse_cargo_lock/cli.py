import argparse
import collections
import pathlib

import tomllib


def parse_command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument("project_dir")
    options = parser.parse_args()
    return options


def print_package(name: str, dependencies: dict, indent=0):
    indent_str = "│    " * indent
    print(f"{indent_str}├── {name}")

    for sub_name in sorted(dependencies.get(name, [])):
        print_package(sub_name, dependencies, indent + 1)


def get_direct_dependencies(meta_path: pathlib.Path):
    with open(meta_path, "rb") as stream:
        meta = tomllib.load(stream)
    return sorted(meta["dependencies"])


def get_project_name(meta_path: pathlib.Path):
    with open(meta_path, "rb") as stream:
        meta = tomllib.load(stream)
    return meta["package"]["name"]


def main() -> None:
    options = parse_command_line()
    project_dir = pathlib.Path(options.project_dir)

    with open(project_dir / "Cargo.lock", "rb") as stream:
        content = tomllib.load(stream)

    dep = collections.defaultdict(set)
    for package in content["package"]:
        name = package["name"]
        dependencies = set(package.get("dependencies", []))
        dep[name] = dependencies

    meta_path = project_dir / "Cargo.toml"
    project_name = get_project_name(meta_path)
    print()
    print(f"Project {project_name}")
    for name in get_direct_dependencies(project_dir / "Cargo.toml"):
        print_package(name, dep)
