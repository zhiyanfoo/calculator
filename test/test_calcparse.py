import sys
sys.path.append("..") 
sys.path.append("../zero_cas")
import pytest

import calcparse
from calcparse import calcparser

from math import factorial
from data_io import DataInputMethod, DataOutputMethod
from main import App


def test_number(capsys):
    raw_formula = '7'
    expected = 7
    assert expected == calcparser.parse(raw_formula)
    out, err = capsys.readouterr()
    assert err == ""

def test_identifier(capsys):
    raw_formula = 'b = 7'
    calcparser.parse(raw_formula)
    assert calcparse.identifiers['b'] == 7

def test_addition(capsys):
    raw_formula = "3 + 4"
    expected = 7
    assert expected == calcparser.parse(raw_formula)
    out, err = capsys.readouterr()
    assert err == ""

def test_subtraction(capsys):
    raw_formula = "4 - 3"
    expected = 1
    assert expected == calcparser.parse(raw_formula)
    out, err = capsys.readouterr()
    assert err == ""

def test_subtraction_subtraction(capsys):
    raw_formula = "4 - 3 - 10"
    expected = -9
    assert expected == calcparser.parse(raw_formula)
    out, err = capsys.readouterr()
    assert err == ""

def test_multiplication(capsys):
    raw_formula = "4 * 3 * 10"
    expected = 120
    assert expected == calcparser.parse(raw_formula)
    out, err = capsys.readouterr()
    assert err == ""


def test_division(capsys):
    raw_formula = "50 / 10 / 5"
    expected = 1
    assert expected == calcparser.parse(raw_formula)
    out, err = capsys.readouterr()
    assert err == ""

def test_division_multiplication(capsys):
    raw_formula = "50 / 10 * 5"
    expected = 25
    assert expected == calcparser.parse(raw_formula)
    out, err = capsys.readouterr()
    assert err == ""
    
def test_multiplication_division(capsys):
    raw_formula = "50 * 10 / 5"
    expected = 100
    assert expected == calcparser.parse(raw_formula)
    out, err = capsys.readouterr()
    assert err == ""

def test_negative(capsys):
    raw_formula = "-10"
    expected = -10
    assert expected == calcparser.parse(raw_formula)
    out, err = capsys.readouterr()
    assert err == ""

def test_multiplication_negative(capsys):
    raw_formula = "4 * -10"
    expected = -40
    assert expected == calcparser.parse(raw_formula)
    out, err = capsys.readouterr()
    assert err == ""

def test_addition_negative(capsys):
    raw_formula = "40 + -10"
    expected = 30
    assert expected == calcparser.parse(raw_formula)
    out, err = capsys.readouterr()
    assert err == ""

def test_minus_negative(capsys):
    raw_formula = "40 - - 10"
    expected = 50
    assert expected == calcparser.parse(raw_formula)
    out, err = capsys.readouterr()
    assert err == ""
    

def test_invalid_recursive_negation(capsys):
    raw_formula = "--40"
    calcparser.parse(raw_formula)
    out, err = capsys.readouterr()
    expected = 'yacc: Syntax error at line 1, token=MINUS\n'
    print(err)
    print(expected)
    assert expected == err

def test_parenthesis(capsys):
    raw_formula = "5 * (11 - 1)"
    expected = 50
    assert expected == calcparser.parse(raw_formula)
    out, err = capsys.readouterr()
    assert err == ""

def test_parenthesis_whole(capsys):
    raw_formula = "(11 - 1)"
    expected = 10
    assert expected == calcparser.parse(raw_formula)
    out, err = capsys.readouterr()
    assert err == ""

def test_parenthesis_unary(capsys):
    raw_formula = "-(-1)"
    expected = 1
    assert expected == calcparser.parse(raw_formula)
    out, err = capsys.readouterr()
    assert err == ""

def test_parenthesis_division(capsys):
    raw_formula = "1000/(90 + 10)"
    expected = 10
    assert expected == calcparser.parse(raw_formula)
    out, err = capsys.readouterr()
    assert err == ""

def test_exponential(capsys):
    raw_formula = "2^5"
    expected = 2**5
    assert expected == calcparser.parse(raw_formula)
    out, err = capsys.readouterr()
    assert err == ""

def test_exponential_exponential(capsys):
    raw_formula = "3^3^2"
    expected = 3**9
    assert expected == calcparser.parse(raw_formula)
    out, err = capsys.readouterr()
    assert err == ""


def test_exponential_exponential_multiplication(capsys):
    raw_formula = "3^3^2*2"
    expected = (3**9)*2
    assert expected == calcparser.parse(raw_formula)
    out, err = capsys.readouterr()
    assert err == ""


def test_exponential_negative_exponential(capsys):
    raw_formula = "9^-2"
    expected = 9 ** -2
    assert abs(expected - calcparser.parse(raw_formula)) < 0.00001

def test_multiplication_exponential_negative_exponential_negative_exponential(capsys):
    raw_formula = "3 * 9^-2 ^ -1 ^ -2"
    expected = 3 * 9 ** -2 ** -1 ** -2
    assert abs(expected - calcparser.parse(raw_formula)) < 0.00001

def test_factorial(capsys):
    raw_formula = "4!"
    expected = factorial(4)
    assert expected == calcparser.parse(raw_formula)
    out, err = capsys.readouterr()
    assert err == ""

def test_factorial(capsys):
    raw_formula = "4!!"
    expected = factorial(factorial(4))
    assert expected == calcparser.parse(raw_formula)
    out, err = capsys.readouterr()
    assert err == ""

def test_factorial_complex(capsys):
    raw_formula = "-4!^3!"
    expected = -factorial(4) ** factorial(3)
    assert expected == calcparser.parse(raw_formula)
    out, err = capsys.readouterr()
    assert err == ""

def test_factorial_parenthesis(capsys):
    raw_formula = "(2 + 1)!"
    expected = 6
    assert expected == calcparser.parse(raw_formula)
    out, err = capsys.readouterr()
    assert err == ""

def test_empty(capsys):
    raw_formula = ""
    expected = ""
    assert expected == calcparser.parse(raw_formula)
    out, err = capsys.readouterr()
    assert err == ""

def test_function(capsys):
    raw_formula = "{sin$1}(0)"
    expected = 0
    assert abs(expected - calcparser.parse(raw_formula)) < 0.00001
    out, err = capsys.readouterr()
    assert err == ""


def test_minus_function(capsys):
    raw_formula = "{sin$1} - {pi$0} "
    expected = 0
    assert abs(expected - calcparser.parse(raw_formula)) < 0.00001
    out, err = capsys.readouterr()
    assert err == ""

def test_function_function(capsys):
    raw_formula = "{cos$1} {sin$1} 0"
    expected = 1
    assert abs(expected - calcparser.parse(raw_formula)) < 0.00001
    out, err = capsys.readouterr()
    assert err == ""

def test_function_parenthesis(capsys):
    raw_formula = "{cos$1} (({cos$1} - {pi$0})*{pi$0})"
    expected = -1
    assert abs(expected - calcparser.parse(raw_formula)) < 0.00001
    out, err = capsys.readouterr()
    assert err == ''
    

def test_define_function(capsys):
    raw_formula = "{hello$0} = 5"
    expected = 5
    assert abs(expected - calcparser.parse(raw_formula)) < 0.00001
    out, err = capsys.readouterr()
    assert err == ''


def test_use_defined_function(capsys):
    data = [
        "{boy$0} = 3 + 7",
        "{boy$0} - 3",
        "@printall",
        "  @exit"
        ]
    output = DataOutputMethod()
    app = App(DataInputMethod(data), output)
    app.run()
    assert output.output == [10, 7]
    out, err = capsys.readouterr()
    assert err == ''

