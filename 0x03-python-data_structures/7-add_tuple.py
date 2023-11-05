#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        n = 2 - len(tuple_a)
        new_els_ta = (0,) * n
        tuple_a = tuple_a + new_els_ta
    if len(tuple_b) < 2:
        n = 2 - len(tuple_b)
        new_els_b = (0,) * n
        tuple_b = tuple_b + new_els_b
    tuple_s = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return (tuple_s)
