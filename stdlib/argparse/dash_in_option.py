import argparse

parser = argparse.ArgumentParser(description="get all versions")
parser.add_argument("test-version")
version = parser.parse_args()

print(version)
print((getattr(version, "test-version")))
