#!/usr/bin/python3
for i in range(100):
    if i >= 0 and i <= 9:
        i = '0' + str(i)
    if i == 99:
        print("{}".format(i))
        break
    print("{}, ".format(i), end="")

