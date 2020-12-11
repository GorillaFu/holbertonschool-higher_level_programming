#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    j = len(sys.argv) - 1
    if j == 0:
        print("{} arguments.".format(j))
    elif j == 1:
        print("{0} argument:\n{0}: {1}".format(j, sys.argv[j]))
    else:
        print("{} arguments:".format(j))
        for i, str in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, str))
