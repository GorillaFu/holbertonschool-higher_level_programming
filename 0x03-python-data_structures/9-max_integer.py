#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    i = 0
    j = 0
    while i < len(my_list):
        if i > j:
            j = i
        i += 1
    return j
