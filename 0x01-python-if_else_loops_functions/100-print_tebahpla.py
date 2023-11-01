#!/usr/bin/python3
for i in range(122, 96, -2):
    print("{}".format(chr(i)), end="")
    k = i - 1
    print("{}".format(chr(k - 32)), end="")
