import re
from consts import operators


def op_greater(op1, op2):
    if operators.index(op1) > operators.index(op2):
        return True
    else:
        return False


def stream_string(code):
    num = 0
    while num < len(code):
        yield code[num]
        num += 1


def is_num(val):
    if re.search('\d+', val):
        return True
    else:
        return False


def is_whitespace(val):
    if re.search('\s+', val):
        return True
    else:
        return False


def is_op(val):
    return val in operators
