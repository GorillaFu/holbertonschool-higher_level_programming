#!/usr/bin/python3
def search_replace(my_list, search, replace):
    i = 0
    new = my_list.copy()
    while i < len(my_list):
        if my_list[i] == search:
            new[i] = replace
        i+=1
    return new
