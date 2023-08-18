#!/usr/bin/python3

def uniq_add(my_list=[]):
    myNew_list = set(my_list)
    data = 0

    for i in myNew_list:
        data += i
    return (data)
