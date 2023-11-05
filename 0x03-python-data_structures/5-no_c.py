#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        str = ""
        for i in range(0, len(my_string)):
            if my_string[i] != 'c' and my_string[i] != 'C':
                str += my_string[i]
        return str
