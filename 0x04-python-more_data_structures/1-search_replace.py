#!/usr/bin/python3

def search_replace(my_list, search, replace):
    return [replace if data == search else data for data in my_list]
