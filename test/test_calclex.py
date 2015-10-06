import sys
sys.path.append("..") 
sys.path.append("../zero_cas")
import pytest
import calclex
import ply.lex as lex

@pytest.fixture(scope='module')
def lexer():
    return lex.lex(module=calclex)


def test_add_sub_mul_unminus(lexer):
    data = '3 + 4 * 10  + -20 *2'

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

    assert expected == totoklist(data, lexer)

def test_variable_assignment(lexer):
    data = 'x = 4 * 100'

    expected = [
        ['VARIABLE', 'x', 1, 0],
        ['ASSIGNMENT', '=', 1, 2],
        ['NUMBER', 4, 1, 4],
        ['TIMES', '*', 1, 6],
        ['NUMBER', 100, 1, 8],
        ]

    assert expected == totoklist(data, lexer)



def tokensaslist(tokens):
    for i in tokens:
        print(i)
    return [ [tok.type, tok.value, tok.lineno, tok.lexpos] for tok in tokens]


def totoklist(data, lexer):
    lexer.input(data)

    tokens_created = list()
    
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens_created.append(tok)

    return tokensaslist(tokens_created)

