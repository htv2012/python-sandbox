import pathlib
import re
import subprocess
import tomllib


def edit_file(filename: str, search: str, replace: str):
    file = pathlib.Path(filename)
    content = file.read_text()
    content = re.sub(rf"\b{search}\b", replace, content)
    file.write_text(content)


def get_current_project_name() -> str:
    with open("pyproject.toml", "rb") as stream:
        info = tomllib.load(stream)
    return info["project"]["name"]


def main():
    # Get old- and new names
    old_name = get_current_project_name()
    old_dir_name = old_name.replace("-", "_")

    name = input("New name: ")
    dir_name = name.replace("-", "_")

    # Rename dir
    package_dir = pathlib.Path(f"src/{old_dir_name}")
    package_dir.rename(f"src/{dir_name}")

    # Replace text
    edit_file("pyproject.toml", f"{old_dir_name}:main", f"{dir_name}:main")
    edit_file("pyproject.toml", old_name, name)
    edit_file("Makefile", old_name, name)

    # Update uv.lock file
    subprocess.run(["uv", "sync"])


if __name__ == "__main__":
    main()
