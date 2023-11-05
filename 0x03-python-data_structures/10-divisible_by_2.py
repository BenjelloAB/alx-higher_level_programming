#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    list_bool = []
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            list_bool.append(True)
        else:
            list_bool.append(False)
    return list_bool
