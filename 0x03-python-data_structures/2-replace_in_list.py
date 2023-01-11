#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Replacing the value of a list in a specific idx with element"""
    if idx < 0 | idx > len(my_list) - 1:
        return my_list
    else:
        my_list[idx] = element
        return my_list
