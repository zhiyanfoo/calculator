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
    raw_formula = '3 + 4 * 10  + -20 *2'

    expected = [
        ['NUMBER', 3, 0],
        ['PLUS', '+', 2],
        ['NUMBER', 4, 4],
        ['TIMES', '*', 6],
        ['NUMBER', 10, 8],
        ['PLUS', '+', 12],
        ['MINUS', '-', 14],
        ['NUMBER', 20, 15],
        ['TIMES', '*', 18],
        ['NUMBER', 2, 19],
    ]

    assert expected == totoklist(raw_formula, lexer)

identifier_assignment_data = (
        ('x = 4 * 100',
        [
            ['IDENTIFIER', 'x', 0],
            ['ASSIGN', '=', 2],
            ['NUMBER', 4, 4],
            ['TIMES', '*', 6],
            ['NUMBER', 100, 8]
        ]
        ),
        ('h_l1238 = 12/3 + 2',
            [
                ['IDENTIFIER', 'h_l1238', 0],
                ['ASSIGN', '=', 8], 
                ['NUMBER', 12, 10],
                ['DIVIDE', '/', 12],
                ['NUMBER', 3, 13],
                ['PLUS', '+', 15],
                ['NUMBER', 2, 17]
            ]
        )
    )
@pytest.mark.parametrize("raw_formula,expected", identifier_assignment_data)
def test_identifier_assignment(lexer, raw_formula, expected):
    assert expected == totoklist(raw_formula, lexer)

def test_factorial(lexer):
    raw_formula = '3!'

    expected = [
        ['NUMBER', 3, 0],
        ['FACTORIAL', '!', 1],
    ]

    assert expected == totoklist(raw_formula, lexer)

def test_invalid_variable(lexer):
    raw_formula = 'he'

    expected = [
        ['IDENTIFIER', 'h', 0],
        ['IDENTIFIER', 'e', 1]
    ]

    assert expected == totoklist(raw_formula, lexer)

def test_function(lexer):
    raw_formula = '{sin$1}'

    expected = [
        ['FUNCTION_1', 'sin', 0],
    ]

    assert expected == totoklist(raw_formula, lexer)

def test_function_assignment(lexer):
    raw_formula = '{sin$1}x = {xo$0}(x - a)'

    expected = [
        ['FUNCTION_1', 'sin', 0],
        ['IDENTIFIER', 'x', 7],
        ['ASSIGN', '=', 9],
        ['FUNCTION_0', 'xo', 11],
        ['LPAREN', '(', 17],
        ['IDENTIFIER', 'x', 18],
        ['MINUS', '-', 20],
        ['IDENTIFIER', 'a', 22],
        ['RPAREN', ')', 23],
    ]
    assert expected == totoklist(raw_formula, lexer)


def tokensaslist(tokens):
    for i in tokens:
        print(i)
    print(tokens[0].lineno)
    return [ [tok.type, tok.value, tok.lexpos] for tok in tokens]


def totoklist(raw_formula, lexer):
    lexer.input(raw_formula)

    tokens_created = list()
    
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens_created.append(tok)

    return tokensaslist(tokens_created)

