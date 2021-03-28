from parse import Parser

if __name__ == '__main__':
    parser = Parser('1 + 2 * 4 / 2')
    tree = parser.parse()
    print(tree.eval())
