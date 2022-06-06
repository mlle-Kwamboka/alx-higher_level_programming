#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    for i in idx[i]:
        idx[i] = range(0, len(my_list))
        del my_list[idx]
        new_list = my_list[idx - 1]
        if idx < 0:
            return my_list
        else:
            print("{]".format(new_list))
