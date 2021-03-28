from math_token import MathToken
from tokenizer import tokenize
from utils import op_greater
from node import Node


class Parser:
    def __init__(self, code):
        self.val_stack = []
        self.op_stack = []
        self.state = None
        self.result = self._parse(tokenize(code))

    def _parse_start(self, val):
        if self.state is not None:
            raise Exception('Start state encountered after first token')
        if val is not None:
            raise Exception('Start state parsed with a value')
        self.state = MathToken.START

    def _parse_num(self, num):
        if self.state != MathToken.OP and self.state != MathToken.START:
            raise Exception('Invalid transition, a number must follow start or operator')
        self.state = MathToken.NUM
        self.val_stack.append(Node(MathToken.NUM, num))

    def _build_node(self):
        tmp_op = self.op_stack.pop()
        r_val = self.val_stack.pop()
        l_val = self.val_stack.pop()
        tmp_node = Node(MathToken.OP, tmp_op, l_val, r_val)
        self.val_stack.append(tmp_node)

    def _parse_op(self, op):
        if self.state != MathToken.NUM:
            raise Exception('Invalid transition, an operator must follow a number')
        if len(self.op_stack) > 0 and not op_greater(op, self.op_stack[-1]):
            self._build_node()
        self.op_stack.append(op)
        self.state = MathToken.OP

    def _parse(self, tokenizer):
        val, tok_type = next(tokenizer)
        while tok_type != MathToken.END:
            if tok_type == MathToken.START:
                self._parse_start(val)
            elif tok_type == MathToken.OP:
                self._parse_op(val)
            elif tok_type == MathToken.NUM:
                self._parse_num(val)
            val, tok_type = next(tokenizer)
        while len(self.op_stack) > 0:
            self._build_node()
        return self.val_stack.pop()

    def parse(self):
        return self.result
