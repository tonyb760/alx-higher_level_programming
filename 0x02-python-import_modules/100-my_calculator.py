#!/usr/bin/env python3

import sys
from calculator_1 import add, sub, mul, div

def calculate(a, operator, b):
    if operator == '+':
        result = add(int(a), int(b))
    elif operator == '-':
        result = sub(int(a), int(b))
    elif operator == '*':
        result = mul(int(a), int(b))
    elif operator == '/':
        result = div(int(a), int(b))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, operator, b, result))

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, operator, b = sys.argv[1:]
    calculate(a, operator, b)
