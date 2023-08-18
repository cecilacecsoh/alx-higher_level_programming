#!/usr/bin/python3i

def multiply_by_2(cec_dictionary):
    new_dict = cec_dictionary.copy()
    list_keys = list(new_dict.keys())

    for i in list_keys:
        new_dict[i] *= 2

    return (new_dict)
