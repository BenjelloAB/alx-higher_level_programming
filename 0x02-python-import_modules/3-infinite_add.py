#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    s = 0
    for i in range(1, len(argv)):
        s += int(argv[i])
    print("{:d}".format(s))
