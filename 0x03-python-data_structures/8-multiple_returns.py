#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        tup_str = 0, None
        return tup_str
    tup_str = len(sentence), sentence[0]
    return tup_str
