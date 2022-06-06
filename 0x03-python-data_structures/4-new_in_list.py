#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list1 = my_list.copy()
    my_list[idx] = element
    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    else:
        print("{}".format(my_list1))
