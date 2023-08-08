#!/usr/bin/python3

for no in range(122, 96, -1):
    if no % 2 != 0:
        no = no - 32
    print("{}".format(chr(no)), end="")
