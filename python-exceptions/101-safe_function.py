#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as inst:
        print("Exception: {}".format(inst), file=sys.stderr)
        return None
