import urllib.error
import urllib.parse
import urllib.request


def make_url(server, port, path, scheme="http"):
    netloc = "{}:{}".format(server, port)
    url = urllib.parse.urlunsplit((scheme, netloc, path, "", ""))
    return url


#
# Main
#
server = "haimac.local"
port = 9000

# 1 - Request directory listing
url = make_url(server, port, "/")
file_list = urllib.request.urlopen(url).read()
print("Files from server:")
for filename in file_list.splitlines():
    print("- {}".format(filename))

# 2 - Request contents of a file
filename = input("Type a file name: ")
url = make_url(server, port, filename)
contents = urllib.request.urlopen(url).read()
print("Contents:")
print(contents)

# 3 - Upload a file to the server
contents = "hello, world.\nThe End"
filename = "foo.txt"
url = make_url(server, port, filename)
f = urllib.request.urlopen(url, data=contents)

# 4 - Do some calculation
n1 = 19
n2 = 5
path = "/calculation/{}/{}".format(n1, n2)
url = make_url(server, port, path)
result = int(urllib.request.urlopen(url).read())
print("{} + {} = {}".format(n1, n2, result))

# Send quit signal

url = make_url(server, port, "/quit")
urllib.request.urlopen(url).read()
