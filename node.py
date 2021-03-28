from math_token import MathToken


class Node:
    def __init__(self, node_type, val, l_child=None, r_child=None):
        self.node_type = node_type
        self.val = val
        self.l_child = l_child
        self.r_child = r_child

    def eval(self):
        if self.node_type == MathToken.NUM:
            return int(self.val)
        elif self.node_type == MathToken.OP:
            op = self.val
            l_val = self.l_child.eval()
            r_val = self.r_child.eval()
            if op == '+':
                return l_val + r_val
            if op == '-':
                return l_val - r_val
            if op == '*':
                return l_val * r_val
            if op == '/':
                return l_val // r_val
