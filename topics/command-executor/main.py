from command import Exec

e = Exec()
r = e.run(["echo start; sleep 120; echo end"])
print(r)


def main():
    print("Hello from command-executor!")


if __name__ == "__main__":
    main()
