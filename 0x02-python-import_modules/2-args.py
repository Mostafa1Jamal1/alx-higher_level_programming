#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    print("{:d} ".format(argc - 1), end="")

    if argc == 2:
        print("argument", end="")
    else:
        print("arguments", end="")

    if argc == 1:
        print(".")
    else:
        print(":")
    for i in range(argc - 1):
        print("{:d}: {:s}".format((i + 1), argv[i + 1]))
