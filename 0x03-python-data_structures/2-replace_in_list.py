#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    idx = range(0, len(my_list))
    for i in idx[i]:
        if idx[i] < 0:
            return my_list
        elif idx[i] > len(my_list) - 1:
            return my_list
        else:
            my_list[idx] = element
