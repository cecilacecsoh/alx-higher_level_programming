#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    z = len(sys.argv) - 1

    if z == 0:
        print("{} arguments.".format(z))

    elif z == 1:
        print("{} argument:".format(z))

    else:
        print("{} arguments:".format(z))

    if z >= 1:
        z = 0

        for arg in sys.argv:
            if z != 0:
                print("{}: {}".format(z, arg))
                    z += 1
