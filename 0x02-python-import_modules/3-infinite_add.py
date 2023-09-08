#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    total = 0
    if len(argv) == 1:
        print("0")
    else:
        for i in range(len(argv) - 1):
            number = int(argv[i + 1])
            total += number
        print("{:d}".format(total))
