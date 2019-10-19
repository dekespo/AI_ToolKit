import sys

def check_positive_value(value):
    if value <= 0:
        raise ArithmeticError("Value " + str(value) + " must be larger than 0")

def error_print(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
