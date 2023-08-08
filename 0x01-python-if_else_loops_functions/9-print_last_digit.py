#!/usr/bin/python3

def print_last_digit(number):
    last_digt = abs(number) % 10
    print(last_digt, end="")
    return last_digt
