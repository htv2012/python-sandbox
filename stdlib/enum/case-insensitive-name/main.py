from data import Environment


def main():
    for name in ["TEST", "test", "Test", "pilot", "PILOT"]:
        print(f"{name} -> {Environment[name]}")


if __name__ == "__main__":
    main()
