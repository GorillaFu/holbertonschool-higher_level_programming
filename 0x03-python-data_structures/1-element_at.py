#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return (None)
    if idx == 0:
        return (my_list[0])
    else:
        if idx > len(my_list) - 1:
            return (None)
        for i in my_list:
            if i == idx:
                return (my_list[i])
        return (None)
