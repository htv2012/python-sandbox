# main.py

import subfile

import globals

globals.init()  # Call only once
subfile.stuff()  # Do stuff with global var
print(globals.myList[0])  # Check the result
