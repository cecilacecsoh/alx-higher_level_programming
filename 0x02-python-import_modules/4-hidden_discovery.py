#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import hidden_4

    for nme in dir(hidden_4):
        if nme[:2] != "__":
             print(nme)
