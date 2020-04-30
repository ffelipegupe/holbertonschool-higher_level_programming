#!/usr/bin/python3
import sys


def main():
    if len(sys.argv) == 1:
        print(0)
    else:
        total = 0
        for i in range(1, len(sys.argv)):
            total = total + int(sys.argv[i])
        print(total)

if __name__ == "__main__":
    main()
