import os

try:
    os.mkdir("mydir")
except OSError:
    print("the directory exists already.")
