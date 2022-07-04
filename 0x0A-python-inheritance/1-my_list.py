#!/usr/bin/python3
"""
module 1-my_list.
A class that inherits from list
"""

class MyList(list):
    """Class MyList inherits from list"""
    
    def print_sorted(self):
        """prints list sorted in ascending order"""
        new_list = [:]
        new_list.sort()
        print("{}".format(new_list))
