#!/usr/bin/python3

def roman_to_int(roman_string):
    value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    reslt = 0
    i = 0

    if type(roman_string) is str and roman_string:
        for c in range(len(roman_string) - 1, -1, -1):
            if value[roman_string[c]] >= i:
                reslt += value[roman_string[c]]
            else:
                reslt -= value[roman_string[c]]
            i = value[roman_string[c]]
    return reslt
