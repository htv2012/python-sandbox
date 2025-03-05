import tomli_w


def main():
    obj = {
        # This will result in quotes
        "tool.pytest.ini_options": {
            "log_cli": True,
        },
        # This will not
        "tool": {
            "pytest": {
                "ini_options": {
                    "log_cli": False,
                }
            }
        },
    }
    text = tomli_w.dumps(obj)
    print(text)


if __name__ == "__main__":
    main()
