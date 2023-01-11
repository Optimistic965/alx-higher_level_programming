#!/usr/bin/python3

def element_at(my_list, idx):
    """Retrives the element at a certain position"""
    if idx < 0 | idx > len(my_list) - 1:
        return "None"
    else:
        return my_list[idx]
