#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    try:
        c = 0;
        for i in my_list:
            if c == x:
                break
            print("{}".format(i), end="")
            c += 1
        print()
        return (c)
    except Exception:
        pass
