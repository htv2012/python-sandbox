import shellingham


def main():
    shell_name, shell_path = shellingham.detect_shell()
    print("\n# Shellingham detects")
    print(f"Shell name: {shell_name}")
    print(f"Shell path: {shell_path}")


if __name__ == "__main__":
    main()
