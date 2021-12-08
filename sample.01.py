import sys
from lark import Lark
from lark import Transformer
from functools import reduce

class CalcTransformer(Transformer):
    def expr(self, tree):
        return reduce(lambda x, y: x+y, tree)
    def term(self, tree):
        return reduce(lambda x, y: x*y, tree)
    def factor(self, tree):
        return tree[0]
    def number(self, tree):
        return int(tree[0])

if __name__ == "__main__":
    args = sys.argv
    text = args[1]
    # print(text)

    with open("./calc_grammar.lark", encoding="utf-8") as grammar:
        parser = Lark(grammar.read(), start="expr")
        tree = parser.parse(text)
        print(tree)

        result = CalcTransformer().transform(tree)
        print(result)
