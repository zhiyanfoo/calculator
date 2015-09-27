import sys
sys.path.append("..") 
sys.path.append("../zero_cas")
import pytest
import calclex
import ply.lex as lex


def test_add_sub_mul_unminus():
    lexer = lex.lex(module=calclex)
    data = '''3 + 4 * 10  + -20 *2'''
    lexer.input(data)

    tokens_created = list()
    
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens_created.append(tok)

    tokaslist = toktolist(tokens_created)

    expected = [
    ['NUMBER', 3, 1, 0],
    ['PLUS', '+', 1, 2],
    ['NUMBER', 4, 1, 4],
    ['TIMES', '*', 1, 6],
    ['NUMBER', 10, 1, 8],
    ['PLUS', '+', 1, 12],
    ['MINUS', '-', 1, 14],
    ['NUMBER', 20, 1, 15],
    ['TIMES', '*', 1, 18],
    ['NUMBER', 2, 1, 19],
    ]

    assert tokaslist == expected

def toktolist(output):
    for i in output:
        print(i)
    return [ [tok.type, tok.value, tok.lineno, tok.lexpos] for tok in output]


def test_valid_variable
