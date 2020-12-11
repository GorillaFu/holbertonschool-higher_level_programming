#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = 1
    if len(argv) == 1:
        print("{:d} arguments.".format(len(argv) - 1))
    elif len(argv) == 2:
        print("{:d} argument:".format(len(argv) - 1))
    else:
        print("{:d} arguments:".format(len(argv) - 1))
    while i != len(argv):
        j = argv[i]
        print("{:d}: {:s}".format(i, str(j)))
        i += 1
