#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_1 = ()
    if len(sentence) == 0:
        tuple_1 = 0, "None"
    else:
        tuple_1 = len(sentence), sentence[0]
    return tuple_1
