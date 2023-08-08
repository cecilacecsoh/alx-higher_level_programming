#!/usr/bin/python3
for prnum in range(00, 100):
    print("{:02d}".format(prnum), end='\n' if prnum == 99 else ", ")
