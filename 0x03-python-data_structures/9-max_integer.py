#!/usr/bin/python3

def max_integer(my_list=[]):
    length = len(my_list)

    if length == 0:
        return (None)

    bg_int = my_list[0]

    for i in range(1, length):
        if my_list[i] > bg_int:
            bg_int = my_list[i]

    return (bg_int)
