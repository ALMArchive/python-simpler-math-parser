from utils import *
from math_token import MathToken


def handle_val(val):
    if is_num(val):
        return val, MathToken.NUM
    elif is_op(val):
        return val, MathToken.OP
    else:
        raise Exception('Invalid value')


def tokenize(code):
    stream = stream_string(code)

    def parse_gen():
        yield None, MathToken.START
        try:
            while True:
                val = next(stream)
                if is_whitespace(val):
                    continue
                yield handle_val(val)
        except StopIteration:
            yield None, MathToken.END

    return parse_gen()
