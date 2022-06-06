#!/usr/bin/python3
def element_at(my_list, idx):
    for i in my_list:
        idx = my_list.index(i)
        if idx < 0:
            return 'None'
        elif idx > len(my_list[i] - 1):
            return 'None'
        else:
            return my_list[idx]
