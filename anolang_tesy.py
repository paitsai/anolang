import sys
from antlr4 import *
from antlrgen.AnolangLexer import AnolangLexer
from antlrgen.AnolangParser import AnolangParser
from antlrgen.AnolangVisitor import AnolangVisitor


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = AnolangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = AnolangParser(stream)
    tree = parser.ano_program()
    # print(tree.accept(AnolangVisitor())) 
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)