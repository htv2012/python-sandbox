import json

from jsontools.json_object import JsonObject


def main():
    with open("raw.json") as file:
        raw = json.load(file)
        obj = JsonObject(raw)

    print("Raw:", json.dumps(raw, indent=4))

    print("-" * 80)

    print(f"Color Scheme: {obj.color_scheme!r}")
    print(f"Drop lines flag: {obj.flags.drop_lines}")
    print(f"No Save flag: {obj.flags.no_save}")
    print(f"Font size: {obj.font_size}")
    print(f"Rulers: {obj.rulers}")

    print("Ignored packages:")
    for package in obj.ignored_packages:
        print(f"- {package}")


if __name__ == "__main__":
    main()
