from camel import camel2snake


def main():
    for text in ["helloWorld", "IBMPcJr", "PostIDCheck", "PostAM"]:
        print(f"{text} -> {camel2snake(text)}")


if __name__ == "__main__":
    main()
