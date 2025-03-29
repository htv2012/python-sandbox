import argparse
from tasks import user

parser = argparse.ArgumentParser()
parser.add_argument('uid', type=int)
options = parser.parse_args()

result = user.delay(options.uid)
try:
    payload = result.get()
    print(payload)
except ValueError as error:
    print(error)


