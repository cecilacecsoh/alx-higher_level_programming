#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    divisbl = []

    for d in range(len(my_list)):
        if my_list[d] % 2 == 0:
            divisbl.append(True)
        else:
            divisbl.append(False)

    return (divisbl)
