#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def main():
    ope = ['+', '-', '*', '/']
    if len(sys.argv) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif len(sys.argv) == 4:
        if sys.argv[2] not in ope:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        elif sys.argv[2] == '+':
            sum = add(int(sys.argv[1]), int(sys.argv[3]))
            print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], sum))
        elif sys.argv[2] == '-':
            res = sub(int(sys.argv[1]), int(sys.argv[3]))
            print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], res))
        elif sys.argv[2] == '*':
            mu = mul(int(sys.argv[1]), int(sys.argv[3]))
            print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], mu))
        elif sys.argv[2] == '/':
            di = div(int(sys.argv[1]), int(sys.argv[3]))
            print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], di))
        sys.exit(0)

if __name__ == "__main__":
        main()
