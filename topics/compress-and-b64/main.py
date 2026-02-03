import base64
import gzip


def main():
    with open("data.txt") as stream:
        data = stream.read()

    compressed = gzip.compress(data.encode())
    encoded = base64.b64encode(compressed)

    with open("out.b64", "wb") as stream:
        stream.write(encoded)


if __name__ == "__main__":
    main()
