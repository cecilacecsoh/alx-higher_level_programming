#!/usr/bin/python3

def no_c(my_string):
    new_str = ""

    for cec in my_string:
        if (cec != 'c') and (cec != 'C'):
            new_str += cec

    return (new_str)
