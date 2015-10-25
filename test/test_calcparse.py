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
