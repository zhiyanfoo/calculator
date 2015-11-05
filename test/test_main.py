import sys
sys.path.append(".") 
sys.path.append("..") 
sys.path.append("../zero_cas")
import pytest
from main import App
from helper import DataInputMethod, DataOutputMethod, multiline_calc

# class DataInputMethod:
#     def __init__(self, data):
#         self.data = data
#         self.count = -1

#     def __call__(self):
#         self.count += 1
#         return(self.data[self.count])

# class DataOutputMethod:
#     def __init__(self):
#         self.output = list()

#     def __call__(self, calc_output, lines):
#         for i in lines:
#             self.output.append(calc_output[i])

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
