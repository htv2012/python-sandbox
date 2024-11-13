#!/usr/bin/env python

import random
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    li = [random.randint(0, 9) for i in range(5)]
    output = ', '.join(str(i) for i in li)
    return output

if __name__ == '__main__':
    app.run()

