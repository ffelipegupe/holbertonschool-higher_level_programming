#!/usr/bin/python3
import sys


def main():
    a = len(sys.argv) - 1
    if a == 0:
        print("{} arguments.".format(a))
    elif a == 1:
        print("{} argument:".format(a))
    else:
        print("{} arguments:".format(a))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))

if __name__ == "__main__":
    main()
