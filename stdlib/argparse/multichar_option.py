import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-password", default="i4got")
options = parser.parse_args(["-password=me2you"])
print(options)
