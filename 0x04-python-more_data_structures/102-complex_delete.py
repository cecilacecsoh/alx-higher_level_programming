#!/usr/bin/python3

def complex_delete(cec_dictionary, value):
    tmp = cec_dictionary.copy()
    for i, v in tmp.items():
        if value == v:
            cec_dictionary.pop(i)

    return cec_dictionary
