#!/usr/bin/python3
def complex_delete(my_dict, value):
    tmp = my_dict.copy()
    for k, v in tmp.items():
        if value == v:
            my_dict.pop(k)
    return my_dict
