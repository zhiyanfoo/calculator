import sys
sys.path.append("..") 
sys.path.append("../zero_cas")
import pytest

import calcparse
from calcparse import calcparser

from math import factorial

def test_number():
    raw_formula = '7'
    expected = 7
    assert expected == calcparser.parse(raw_formula)

def test_identifier():
    raw_formula = 'b = 7'
    calcparser.parse(raw_formula)
    assert calcparse.identifiers['b'] == 7

def test_addition():
    raw_formula = "3 + 4"
    expected = 7
    assert expected == calcparser.parse(raw_formula)

def test_subtraction():
    raw_formula = "4 - 3"
    expected = 1
    assert expected == calcparser.parse(raw_formula)

def test_subtraction_subtraction():
    raw_formula = "4 - 3 - 10"
    expected = -9
    assert expected == calcparser.parse(raw_formula)

def test_multiplication():
    raw_formula = "4 * 3 * 10"
    expected = 120
    assert expected == calcparser.parse(raw_formula)


def test_division():
    raw_formula = "50 / 10 / 5"
    expected = 1
    assert expected == calcparser.parse(raw_formula)

def test_division_multiplication():
    raw_formula = "50 / 10 * 5"
    expected = 25
    assert expected == calcparser.parse(raw_formula)
    
def test_multiplication_division():
    raw_formula = "50 * 10 / 5"
    expected = 100
    assert expected == calcparser.parse(raw_formula)

def test_negative():
    raw_formula = "-10"
    expected = -10
    assert expected == calcparser.parse(raw_formula)

def test_multiplication_negative():
    raw_formula = "4 * -10"
    expected = -40
    assert expected == calcparser.parse(raw_formula)

def test_addition_negative():
    raw_formula = "40 + -10"
    expected = 30
    assert expected == calcparser.parse(raw_formula)

def test_minus_negative():
    raw_formula = "40 - - 10"
    expected = 50
    assert expected == calcparser.parse(raw_formula)
    

def test_invalid_recursive_negation(capsys):
    raw_formula = "--40"
    calcparser.parse(raw_formula)
    out, err = capsys.readouterr()
    expected = 'yacc: Syntax error at line 1, token=MINUS\n'
    print(err)
    print(expected)
    assert expected == err

def test_parenthesis():
    raw_formula = "5 * (11 - 1)"
    expected = 50
    assert expected == calcparser.parse(raw_formula)

def test_parenthesis_whole():
    raw_formula = "(11 - 1)"
    expected = 10
    assert expected == calcparser.parse(raw_formula)

def test_parenthesis_unary():
    raw_formula = "-(-1)"
    expected = 1
    assert expected == calcparser.parse(raw_formula)

def test_parenthesis_division():
    raw_formula = "1000/(90 + 10)"
    expected = 10
    assert expected == calcparser.parse(raw_formula)

def test_exponential():
    raw_formula = "2^5"
    expected = 2**5
    assert expected == calcparser.parse(raw_formula)

def test_exponential_exponential():
    raw_formula = "3^3^2"
    expected = 3**9
    assert expected == calcparser.parse(raw_formula)


def test_exponential_exponential_multiplication():
    raw_formula = "3^3^2*2"
    expected = (3**9)*2
    assert expected == calcparser.parse(raw_formula)


def test_exponential_negative_exponential():
    raw_formula = "9^-2"
    expected = 9 ** -2
    assert abs(expected - calcparser.parse(raw_formula)) < 0.00001

def test_multiplication_exponential_negative_exponential_negative_exponential():
    raw_formula = "3 * 9^-2 ^ -1 ^ -2"
    expected = 3 * 9 ** -2 ** -1 ** -2
    assert abs(expected - calcparser.parse(raw_formula)) < 0.00001

def test_factorial():
    raw_formula = "4!"
    expected = factorial(4)
    assert expected == calcparser.parse(raw_formula)

def test_factorial():
    raw_formula = "4!!"
    expected = factorial(factorial(4))
    assert expected == calcparser.parse(raw_formula)

def test_factorial_complex():
    raw_formula = "-4!^3!"
    expected = -factorial(4) ** factorial(3)
    assert expected == calcparser.parse(raw_formula)

def test_factorial_parenthesis():
    raw_formula = "(2 + 1)!"
    expected = 6
    assert expected == calcparser.parse(raw_formula)

def test_empty():
    raw_formula = ""
    expected = ""
    assert expected == calcparser.parse(raw_formula)

def test_function():
    raw_formula = "{$sin$}(0)"
    expected = 0
    assert expected == calcparser.parse(raw_formula)


def test_minus_function():
    raw_formula = "{$sin$} - {$pi$} "
    expected = 0
    assert abs(expected - calcparser.parse(raw_formula)) < 0.00001
