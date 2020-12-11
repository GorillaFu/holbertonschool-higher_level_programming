#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = 1
    num = 0
    while i != len(argv):
        a = argv[i]
        num += int(a)
        i += 1
    print("{:d}".format(num))
