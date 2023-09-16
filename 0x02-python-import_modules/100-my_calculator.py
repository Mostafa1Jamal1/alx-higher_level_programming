#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    op = {'+': add, '-': sub, '*': mul, '/': div}

    if argv[2] not in op:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    num1 = int(argv[1])
    num2 = int(argv[3])
    res = op[argv[2]](num1, num2)
    print("{:d} {} {:d} = {}".format(num1, argv[2], num2, res))
