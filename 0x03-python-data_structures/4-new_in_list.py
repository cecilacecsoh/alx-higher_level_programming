#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    length = len(my_list)

    origi_list = my_list[:]

    if 0 <= idx < length:
        origi_list[idx] = element

    return (origi_list)
