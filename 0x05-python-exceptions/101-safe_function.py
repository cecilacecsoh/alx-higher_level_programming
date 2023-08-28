#!/usr/bin/python3

def safe_function(fct, *args):
    from sys import stderr
    try:
        fun_result = fct(*args)
        return (fun_result)

    except Exception as eras:
        print("Exception: {}".format(eras), file=stderr)
        return None
