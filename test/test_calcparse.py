import sys
sys.path.append(".") 
sys.path.append("..") 
sys.path.append("../calculator")
import pytest

import calcparse
from calcparse import calcparser

from math import factorial
from helper import DataInputMethod, DataOutputMethod, check_parser, check_multiline_calc
from simplify import simplify


@pytest.mark.ast
def test_ast_number(capsys):
    raw_formula = '7'
    expected = 7
    check_parser(raw_formula, expected, capsys)

# @pytest.mark.simplify
# def test_number(capsys):
#     abstract_syntax_tree = 7
#     expected = 7
#     assert expected == simplify(abstract_syntax_tree)


@pytest.mark.ast
def test_ast_addition(capsys):
    raw_formula = "3 + 4"
    expected = ('PLUS', 3, 4)
    check_parser(raw_formula, expected, capsys)

# @pytest.mark.simplify
# def test_addition(capsys):
#     abstract_syntax_tree = ('PLUS', 3, 4)
#     expected = 7
#     assert simplify(abstract_syntax_tree) = expected

@pytest.mark.ast
def test_ast_subtraction(capsys):
    raw_formula = "4 - 3"
    expected = ("MINUS", 4, 3)
    check_parser(raw_formula, expected, capsys)

# @pytest.mark.simplify
# def test_subtraction(capsys):
#     abstract_syntax_tree = ("MINUS", 4, 3)
#     expected = 1
#     assert simplify(abstract_syntax_tree) = expected

@pytest.mark.ast
def test_ast_subtraction_subtraction(capsys):
    raw_formula = "4 - 3 - 10"
    expected = ("MINUS",  ("MINUS", 4, 3), 10)
    check_parser(raw_formula, expected, capsys)

# @pytest.mark.simplify
# def test_subtraction_subtraction(capsys):
#     abstract_syntax_tree = ("MINUS",  ("MINUS", 4, 3), 10)
#     expected = -11
#     assert simplify(abstract_syntax_tree) = expected

@pytest.mark.ast
def test_ast_multiplication(capsys):
    raw_formula = "4 * 3 * 10"
    expected = ("TIMES", ("TIMES", 4.0, 3), 10)
    check_parser(raw_formula, expected, capsys)


# @pytest.mark.simplify
# def test_multiplication(capsys):
#     abstract_syntax_tree = ("TIMES", 4, 3, 10)
#     expected = 120
#     assert simplify(abstract_syntax_tree) = expected

@pytest.mark.ast
def test_ast_division(capsys):
    raw_formula = "50 / 10 / 5"
    expected = ("DIVIDE", ("DIVIDE", 50, 10), 5)
    check_parser(raw_formula, expected, capsys)


# @pytest.mark.simplify
# def test_division(capsys):
#     abstract_syntax_tree = ("DIVIDE", ("DIVIDE", 50, 10), 5)
#     expected = 1
#     assert simplify(abstract_syntax_tree) = expected

@pytest.mark.ast
def test_ast_division_multiplication(capsys):
    raw_formula = "50 / 10 * 5"
    expected = ("TIMES", ("DIVIDE", 50, 10), 5)
    check_parser(raw_formula, expected, capsys)
    
# @pytest.mark.simplify
# def test_division_multiplication(capsys):
#     abstract_syntax_tree = ("TIMES", ("DIVIDE", 50, 10), 5)
#     expected = 25
#     assert simplify(abstract_syntax_tree) = expected

@pytest.mark.ast
def test_ast_multiplication_division(capsys):
    raw_formula = "50 * 10 / 5"
    expected = ("DIVIDE", ("TIMES", 50, 10), 5)
    check_parser(raw_formula, expected, capsys)

# @pytest.mark.simplify
# def test_multiplication_division(capsys):
#     abstract_syntax_tree = ("DIVIDE", ("TIMES", 50, 10), 5)
#     expected = 100
#     assert simplify(abstract_syntax_tree) = expected

@pytest.mark.ast
def test_ast_negative(capsys):
    raw_formula = "-10"
    expected = ("NEGATIVE",  10)
    check_parser(raw_formula, expected, capsys)

# @pytest.mark.simplify
# def test_negative(capsys):
#     abstract_syntax_tree = ("NEGATIVE",  10)
#     expected = -10
#     assert simplify(abstract_syntax_tree) = expected

@pytest.mark.ast
def test_ast_multiplication_negative(capsys):
    raw_formula = "4 * -10"
    expected = ("TIMES", 4, ("NEGATIVE", 10))
    check_parser(raw_formula, expected, capsys)

# @pytest.mark.simplify
# def test_multiplication_negative(capsys):
#     abstract_syntax_tree = ("TIMES", 4, ("NEGATIVE", 10))
#     expected = -40
#     assert simplify(abstract_syntax_tree) = expected

@pytest.mark.ast
def test_ast_addition_negative(capsys):
    raw_formula = "40 + -10"
    expected = ("PLUS", 40 , ("NEGATIVE", 10))
    check_parser(raw_formula, expected, capsys)
    
# @pytest.mark.simplify
# def test_addition_negative(capsys):
#     abstract_syntax_tree = ("PLUS", 40 , ("NEGATIVE", 10))
#     expected = 30
#     assert simplify(abstract_syntax_tree) = expected

@pytest.mark.ast
def test_ast_minus_negative(capsys):
    raw_formula = "40 - - 10"
    expected = ("MINUS", 40, ("NEGATIVE", 10))
    check_parser(raw_formula, expected, capsys)

# @pytest.mark.simplify
# def test_minus_negative(capsys):
#     abstact_syntax_tree = ("MINUS", 40, ("NEGATIVE", 10))
#     expected = 50
#     assert simplify(abstract_syntax_tree) = expected

# #check old commit

@pytest.mark.ast
def test_invalid_recursive_negation(capsys):
    raw_formula = "--40"
    expected = ('NEGATIVE', ('NEGATIVE', 40))
    check_parser(raw_formula, expected, capsys)

@pytest.mark.ast
def test_ast_parenthesis(capsys):
    raw_formula = "5 * (11 - 1)"
    expected = ("TIMES", 5, ("MINUS", 11, 1))
    check_parser(raw_formula, expected, capsys)

# @pytest.mark.simplify
# def test_parenthesis(capsys):
#     raw_formula = ("TIMES", 5, ("MINUS", 11, 1))
#     expected = 50
#     assert simplify(abstract_syntax_tree) = expected
    
@pytest.mark.ast
def test_ast_parenthesis_whole(capsys):
    raw_formula = "(11 - 1)"
    expected = ("MINUS", 11, 1)
    check_parser(raw_formula, expected, capsys)
    
# @pytest.mark.simplify
# def test_parenthesis_whole(capsys):
#     abstract_syntax_tree = ("MINUS", 11 1)
#     expected = 10
#     assert simplify(abstract_syntax_tree) = expected

@pytest.mark.ast
def test_ast_parenthesis_unary(capsys):
    raw_formula = "-(-1)"
    expected = ('NEGATIVE', ('NEGATIVE', 1))
    check_parser(raw_formula, expected, capsys)
    
# @pytest.mark.simplify
# def test_parenthesis_unary(capsys):
#     abstract_syntax_tree = "-(-1)"
#     expected = 1
#     assert simplify(abstract_syntax_tree) = expected

@pytest.mark.ast
def test_ast_parenthesis_division(capsys):
    raw_formula = "1000/(90 + 10)"
    expected = ("DIVIDE", 1000, ("PLUS", 90, 10))
    check_parser(raw_formula, expected, capsys)
    
# @pytest.mark.simplify
# def test_parenthesis_division(capsys):
#     abstract_syntax_tree = "1000/(90 + 10)"
#     expected = 10
#     assert simplify(abstract_syntax_tree) = expected

@pytest.mark.ast
def test_ast_exponential(capsys):
    raw_formula = "2^5"
    expected = ("POWER", 2, 5)
    check_parser(raw_formula, expected, capsys)
    
# @pytest.mark.simplify
# def test_exponential(capsys):
#     abstract_syntax_tree = "2^5"
#     expected = 2**5
#     assert simplify(abstract_syntax_tree) = expected

@pytest.mark.ast
def test_ast_exponential_exponential(capsys):
    raw_formula = "3^3^2"
    expected = ("POWER", 3, ("POWER", 3, 2))
    check_parser(raw_formula, expected, capsys)
    
# @pytest.mark.simplify
# def test_exponential_exponential(capsys):
#     abstract_syntax_tree = "3^3^2"
#     expected = 3**9
#     assert simplify(abstract_syntax_tree) = expected

@pytest.mark.ast
def test_ast_exponential_exponential_multiplication(capsys):
    raw_formula = "3^2*2"
    expected = ("TIMES", ("POWER", 3, 2), 2)
    check_parser(raw_formula, expected, capsys)
    
# @pytest.mark.simplify
# def test_exponential_exponential_multiplication(capsys):
#     abstract_syntax_tree = "3^3^2*2"
#     expected = (3**9)*2
#     assert simplify(abstract_syntax_tree) = expected

@pytest.mark.ast
def test_ast_exponential_negative_exponential(capsys):
    raw_formula = "9^-2"
    expected = ("POWER", 9, ("NEGATIVE", 2))
    check_parser(raw_formula, expected, capsys)

# @pytest.mark.simplify
# def test_exponential_negative_exponential(capsys):
#     abstract_syntax_tree = "9^-2"
#     expected = 3
#     assert simplify(abstract_syntax_tree) = expected

@pytest.mark.ast
def test_exponential_negative_exponential(capsys):
    raw_formula = "-9^12"
    expected = ("NEGATIVE", ("POWER", 9, 12))
    check_parser(raw_formula, expected, capsys)


@pytest.mark.ast
def test_ast_factorial(capsys):
    raw_formula = "4!"
    expected = ('FACTORIAL', 4)
    check_parser(raw_formula, expected, capsys)
    
# @pytest.mark.simplify
# def test_factorial(capsys):
#     abstract_syntax_tree = "4!"
#     expected = factorial(4)
#     assert simplify(abstract_syntax_tree) = expected

@pytest.mark.ast
def test_ast_factorial_factorial(capsys):
    raw_formula = "4!!"
    expected = ("FACTORIAL", ("FACTORIAL", 4))
    check_parser(raw_formula, expected, capsys)
    
# @pytest.mark.simplify
# def test_factorial_factorial(capsys):
#     abstract_syntax_tree = "4!!"
#     expected = factorial(factorial(4))
#     assert simplify(abstract_syntax_tree) = expected

@pytest.mark.ast
def test_ast_factorial_complex(capsys):
    raw_formula = "-4!^3!"
    expected = ("NEGATIVE", ("FACTORIAL", ("POWER", ("FACTORIAL", 4), 3)))
    check_parser(raw_formula, expected, capsys)
    
# @pytest.mark.simplify
# def test_factorial_complex(capsys):
#     abstract_syntax_tree = "-4!^3!"
#     expected = -factorial(4) ** factorial(3)
#     assert simplify(abstract_syntax_tree) = expected

@pytest.mark.ast
def test_ast_empty(capsys):
    raw_formula = ""
    expected = ""
    check_parser(raw_formula, expected, capsys)
    
# @pytest.mark.simplify
# def test_empty(capsys):
#     abstract_syntax_tree = ""
#     expected = ""
#     assert simplify(abstract_syntax_tree) = expected

@pytest.mark.ast
def test_ast_function(capsys):
    raw_formula = "{sin$1}(0)"
    expected = ("FUNCTION", 'sin', 0)
    check_parser(raw_formula, expected, capsys)

# @pytest.mark.simplify
# def test_function(capsys):
#     abstract_syntax_tree = "{sin$1}(0)"
#     expected = ("FUNCTION", 'sin', 0)
#     assert simplify(abstract_syntax_tree) = expected
    
@pytest.mark.ast
def test_ast_minus_function(capsys):
    raw_formula = "{sin$1} - {#gravitational_constant}"
    expected = ("FUNCTION", 'sin', ("NEGATIVE", 9.81))
    check_parser(raw_formula, expected, capsys)

    
# @pytest.mark.simplify
# def test_minus_function(capsys):
#     abstact_syntax_tree = ("FUNCTION", 'sin', ("NEGATIVE",  'pi'))
#     expected = 0
#     assert simplify(abstract_syntax_tree) = expected

# @pytest.mark.ast
# def test_ast_function_1_function_1(capsys):
#     raw_formula = "{cos$1} {sin$1} 0"
#     expected = ("FUNCTION", 'cos', ("FUNCTION", 'sin', 0))
#     check_parser(raw_formula, expected, capsys)

# @pytest.mark.simplify
# def test_function_1_function_1(capsys):
#     abstact_syntax_tree = ("FUNCTION", 'cos', ("FUNCTION", 'sin', 0))
#     expected = 1
#     assert simplify(abstract_syntax_tree) = expected

# @pytest.mark.ast
# def test_ast_functions_parenthesis(capsys):
#     raw_formula = "{cos$1} (({cos$1} - {pi$0})*{pi$0})"
#     expected = ("FUNCTION", 'cos', ("TIMES", ("FUNCTION", 'cos', ("NEGATIVE", 'pi')), pi))
#     check_parser(raw_formula, expected, capsys)

# @pytest.mark.simplify
# def test_functions_parenthesis(capsys):
#     abstact_syntax_tree = ("FUNCTION", 'cos', ("TIMES", ("FUNCTION", 'cos', ("NEGATIVE", 'pi')), pi))
#     expected = -1
#     assert simplify(abstract_syntax_tree) = expected
    

# @pytest.mark.ast
# def test_ast_ast_define_function_0(capsys):
#     raw_formula = "{#hello} = 5"
#     expected = ("ASSIGN", 'hello', 5)
#     check_parser(raw_formula, expected, capsys)
    
# @pytest.mark.simplify
# def test_ast_define_function_0(capsys):
#     abstact_syntax_tree = "{#hello} = 5"
#     expected = ("ASSIGN", 'hello', 5)
#     assert simplify(abstract_syntax_tree) = expected

# @pytest.mark.simplify
# def test_define_function_0(capsys):
#     abstact_syntax_tree = ("ASSIGN", 'hello', 5)
#     expected = 5
#     assert simplify(abstract_syntax_tree) = expected

# # def test__identifier(capsys):
# #     raw_formula = 'b = 7'
# #     calcparser.parse(raw_formula)
# #     assert calcparse.identifiers['b'] == 7

# def test_use_defined_function_0(capsys):
#     data = [
#         "{boy$0} = 3 + 7",
#         "{boy$0} - 3",
#         "@printall",
#         "  @exit"
#         ]
#     expected = [10, 7]
#     check_multiline_calc(data, expected, capsys)
