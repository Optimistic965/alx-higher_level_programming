#!/usr/bin/python3
from sys import *
if __name__ = "__main__":
    count = len(argv) - 1
    if count < 1:
        print("{} arguments.".format(count))
    elif count == 1:
        print("{} argument:".format(count))
        print("{}: {}".format(count, argv[count]))
    else:
        print("{} arguments:".format(count))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
