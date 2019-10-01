import sys
import operator

def checkPositiveValue(value):
    if value <= 0:
        raise ArithmeticError("Value " + str(value) + " must be larger than 0")

def checkNoneValue(value, valueName):
    if not value:
        raise AssertionError(valueName, " cannot be None!")

def checkValidation(value, valueName, validValues):
    if value not in validValues:
        raise AssertionError(valueName, " is ", value, ", which is not valid." \
            " The valid list is: ", validValues)

def comparisonCheck(first, relate, second):
    operators = {
        '>': operator.gt,
        '<': operator.lt,
        '>=': operator.ge,
        '<=': operator.le,
        '==': operator.eq
    }
    checkValidation(relate, "relate", tuple(operators.keys()))
    return operators[relate](first, second)

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
