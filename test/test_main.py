import sys
sys.path.append(".") 
sys.path.append("..") 
sys.path.append("../zero_cas")
import pytest
from main import App
from helper import DataInputMethod, DataOutputMethod, multiline_calc

def test_basic_calculations(capsys):
    data = [
        "3 + 7",
        " 3 ^ 2",
        "@printall",
        "  @exit"
        ]
    expected = [10, 9]
    multiline_calc(data, expected, capsys)

def test_variable_assignement(capsys):
    data = [
        "a = 3 + 7",
        " a ^ 2",
        "@printall",
        "  @exit"
        ]
    expected = [10, 100]
    multiline_calc(data, expected, capsys)
