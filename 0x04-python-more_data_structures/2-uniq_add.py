#!/usr/bin/python3
def uniq_add(my_list=[]):
    copy_list = set(my_list)
    sum_int = 0
    for i in copy_list:
        sum_int += i
        return sum_int
