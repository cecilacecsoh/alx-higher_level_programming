#!/usr/bin/python3
def uppercase(str):
    case = 0
    for letter in str:
        if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
            case = 32

        else:
            case = 0
        print('{:c}'.format(ord(letter) - case), end="")
    print()
