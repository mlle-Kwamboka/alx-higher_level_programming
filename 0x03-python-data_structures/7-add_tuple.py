#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    for i in tuple_a:
        for j in tuple_b:
            tuple_c = (tuple_a[i] + tuple_b[j])
            if len(tuple_a[i]), len(tuple_b[j]) < 2:
                tuple_a[i + 1], tuple_b[j + 1] = 0
            elif len(tuple_a[i]), len(tuple_b[j]) > 2:
                i, j  = 1, 1
            else:
                print("{}".format(tuple_c))
