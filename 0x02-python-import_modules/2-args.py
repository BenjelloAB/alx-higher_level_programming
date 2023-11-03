#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    size = len(argv) - 1
    if size == 0:
        print("{} arguments.".format(size))
    elif size > 0:
        print("{} argument{}:".format(size, "s" if size > 1 else ""))
        for i in range(1, size + 1):
            print("{}: {}".format(i, argv[i]))
