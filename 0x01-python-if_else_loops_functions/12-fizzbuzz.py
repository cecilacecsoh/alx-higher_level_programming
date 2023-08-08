#!/usr/bin/python3
def fizzbuzz():
    for no in range(1, 101):
        if (no % 15 == 0):
            print("FizzBuzz ", end="")

        elif (no % 3 == 0):
            print("Fizz ", end="")

        elif (no % 5 == 0):
            print("Buzz ", end="")

        else:
            print("{:d} ".format(no), end="")
