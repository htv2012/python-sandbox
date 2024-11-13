#
# Partial Method
#
from functools import partialmethod


def print_if_not_none(obj, label):
    if obj is not None:
        print(f"{label}: {obj}")


class Curl:
    def send(
        self,
        method,
        url,
        headers=None,
        data=None,
        params=None,
        resolve=None,
        follow_redirects=False,
        max_wait=None,
    ):
        print_if_not_none(method, "method")
        print_if_not_none(url, "url")
        print_if_not_none(headers, "headers")
        print_if_not_none(data, "data")
        print_if_not_none(params, "params")
        print_if_not_none(resolve, "resolve")
        print_if_not_none(follow_redirects, "follow_redirects")
        print_if_not_none(max_wait, "max_wait")

    delete = partialmethod(send, "DELETE")
    post = partialmethod(send, "POST")


def main():
    """Entry"""
    print("\n#\n# partialmethod demo\n#")
    url = "http://nginx.test"
    curl = Curl()

    print("\n# Send")
    curl.send(method="GET", url=url)

    print("\n# Delete")
    curl.delete(url)

    print("\n# Post")
    curl.post(url, data={"data": 1})


if __name__ == "__main__":
    main()
