#!/usr/bin/python3
for a in range(122, 96, -1):
    if a % 2 != 0:
        con = a - 32
        print("{}".format(chr(con)), end="")
    else:
        print("{}".format(chr(a)), end="")
