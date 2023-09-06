#!/usr/bin/python3

"""
N Queens Backtracking program that prints coordinates of N queens
on an NxN grid such that they are all to be in non-attacking positions
"""


from sys import argv

if __name__ == "__main__":
    a = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    iv = int(argv[1])
    if iv < 4:
        print("N must be at least 4")
        exit(1)

    # initializing the answer list
    for z in range(iv):
        a.append([z, None])

    def already_exists(y):
        """check that a queen has not already existed in the y value"""
        for x in range(iv):
            if y == a[x][1]:
                return True
        return False

    def reject(x, y):
        """determines whether to accept/reject the solution"""
        if (already_exists(y)):
            return False
        z = 0
        while(z < x):
            if abs(a[z][1] - y) == abs(z - x):
                return False
            z += 1
        return True

    def clear_a(x):
        """clears the answers from point of failure on"""
        for z in range(x, iv):
            a[z][1] = None

    def nqueens(x):
        """recursive backtracking function helps find the solution"""
        for y in range(iv):
            clear_a(x)
            if reject(x, y):
                a[x][1] = y
                if (x == iv - 1):  # accepts the solution
                    print(a)
                else:
                    nqueens(x + 1)  # moves on to next x value to continue

    # start the recursive process at x = 0
    nqueens(0)
