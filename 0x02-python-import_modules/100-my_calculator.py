#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def main():
    import sys
    if len(sys.argv) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif len(sys.argv) == 4:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        ope = ['+', '-', '*', '/']
        if sys.argv[2] not in ope:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        elif sys.argv[2] == '+':
            sum = add(a,b)
            print("{} {} {} = {}".format(a, sys.argv[2], b, sum))
        elif sys.argv[2] == '-':
            res = sub(a, b)
            print("{} {} {} = {}".format(a, sys.argv[2], b, res))
        elif sys.argv[2] == '*':
            mu = mul(int(sys.argv[1]), int(sys.argv[3]))
            print("{} {} {} = {}".format(a, sys.argv[2], b, mu))
        elif sys.argv[2] == '/':
            di = div(int(sys.argv[1]), int(sys.argv[3]))
            print("{} {} {} = {}".format(a, sys.argv[2], b, di))
if __name__ == "__main__":
        main()
