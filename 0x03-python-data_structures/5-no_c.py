#!/usr/bin/python3

def no_c(my_string):
    if my_string:
        str = ""
        for m in my_string:
            if m != 'c' and m != 'C':
                str += m
        return (str)
