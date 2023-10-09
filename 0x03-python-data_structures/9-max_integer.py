#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    length = len(my_list)
    my_list = my_list.sort()
    return my_list[length - 1]
