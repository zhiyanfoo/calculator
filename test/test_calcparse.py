import sys
sys.path.append("..") 
sys.path.append("../zero_cas")
import pytest
import ply.yacc as yacc

import calcparse
from calcparse import calcparser

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

