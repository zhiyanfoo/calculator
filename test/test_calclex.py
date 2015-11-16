import sys
sys.path.append("..") 
sys.path.append("../calculator")
import pytest
import calclex
import ply.lex as lex

@pytest.fixture(scope='module')
def lexer():
    return lex.lex(module=calclex)

def test_numbers(lexer):
    raw_formula = '12.123 * .1234'

    expected = [
        ['NUMBER', 12.123, 0],
        ['*', '*', 7],
        ['NUMBER', 0.1234, 9],
    ]

    assert expected == totoklist(raw_formula, lexer)

def test_add_sub_mul_unminus(lexer):
    raw_formula = '3 + 4 * 10  + -20 *2'

    expected = [
        ['NUMBER', 3, 0],
        ['+', '+', 2],
        ['NUMBER', 4, 4],
        ['*', '*', 6],
        ['NUMBER', 10, 8],
        ['+', '+', 12],
        ['-', '-', 14],
        ['NUMBER', 20, 15],
        ['*', '*', 18],
        ['NUMBER', 2, 19],
    ]

    assert expected == totoklist(raw_formula, lexer)

identifier_assignment_data = (
        ('x = 4 * 100',
        [
            ['IDENTIFIER', 'x', 0],
            ['=', '=', 2],
            ['NUMBER', 4, 4],
            ['*', '*', 6],
            ['NUMBER', 100, 8]
        ]
        ),
        ('h_l1238 = 12/3 + 2',
            [
                ['IDENTIFIER', 'h_l1238', 0],
                ['=', '=', 8], 
                ['NUMBER', 12, 10],
                ['/', '/', 12],
                ['NUMBER', 3, 13],
                ['+', '+', 15],
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
        ['!', '!', 1],
    ]

    assert expected == totoklist(raw_formula, lexer)

def test_multivariable(lexer):
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
        ['=', '=', 9],
        ['FUNCTION_0', 'xo', 11],
        ['(', '(', 17],
        ['IDENTIFIER', 'x', 18],
        ['-', '-', 20],
        ['IDENTIFIER', 'a', 22],
        [')', ')', 23],
    ]
    assert expected == totoklist(raw_formula, lexer)

def test_function_assignment(lexer):
    raw_formula = '{ant$+}(x,y) = (12.51, 1)'

    expected = [
        ['FUNCTION_MULTI', 'ant', 0],
        ['(', '(', 7],
        ['IDENTIFIER', 'x', 8],
        [',', ',', 9],
        ['IDENTIFIER', 'y', 10],
        [')', ')', 11],
        ['=', '=', 13],
        ['(', '(', 15],
        ['NUMBER', 12.51, 16],
        [',', ',', 21],
        ['NUMBER', 1.0, 23],
        [')', ')', 24],
    ]
    assert expected == totoklist(raw_formula, lexer)

def test_defined_constant_assignment(lexer):
    raw_formula = '{#ant} = 1'

    expected = [
        ['DEFINED_CONSTANT', 'ant', 0],
        ['=', '=', 7],
        ['NUMBER', 1, 9],
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

