import ply.yacc as yacc
from calclex import tokens
import math 

identifiers = dict()

defined_constants = { 'pi': math.pi , 'gravitational_constant' : 9.81}
functions_1 =  { 'sin' : math.sin, 'cos' : math.cos }

precedence = (
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('right', 'NEGATIVE'),
    ('left', '!'),
    ('left', 'FUNCTION_1'),
    ('right', '^'),
    ('left', "FUNCTION_PAREN"),
    )
# def p_assign_expression(p):
#     'statement : IDENTIFIER ASSIGN expression'
#     identifiers[p[1]] = p[3]
#     p[0] = p[3]

# def p_define_function(p):
#     'statement : FUNCTION_0 ASSIGN expression'
#     functions[0][p[1]] = p[3]
#     p[0] = p[3]

def p_statement_expression(p):
    'statement : expression'
    p[0] = p[1]

def p_expression_binop(p):
    """expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression
                  | expression '^' expression"""
    if   p[2] == '+'   : p[0] = ('PLUS', p[1], p[3])
    elif p[2] == '-' : p[0] = ('MINUS', p[1], p[3])
    elif p[2] == '*' : p[0] = ('TIMES', p[1], p[3])
    elif p[2] == '/' : p[0] = ('DIVIDE', p[1], p[3])
    elif p[2] == '^' : p[0] = ('POWER', p[1], p[3])



def p_expression_negative(p):
    "expression : '-' expression %prec NEGATIVE" 
    p[0] = ('NEGATIVE', p[2])

def p_expression_postfix(p):
    "expression : expression '!'" 
    p[0] = ('FACTORIAL', p[1])

def p_statement_empty(p):
    'statement : empty'
    p[0] = p[1]

def p_expression_function_1_paren(p):
    "expression : FUNCTION_1 '(' expression ')' %prec FUNCTION_PAREN"
    p[0] = ("FUNCTION", p[1], p[3])

def p_expression_function_1(p):
    "expression : FUNCTION_1  expression"
    p[0] = ("FUNCTION", p[1], p[2])

def p_expression_parenthesis(p):
    "expression : '(' expression ')'"
    p[0] = p[2]

def p_expression_defined_constant(p):
    "expression : DEFINED_CONSTANT"
    p[0] = defined_constants[p[1]]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

# def p_term_function_unary(p):
#     'term : FUNCTION_1 term'
#     p[0] = functions[1][p[1]](p[2])
    

# def p_term_negative_unary(p):
#     'term : MINUS unary'
#     p[0] = -p[2]

# def p_term_unary(p):
#     'term : unary'
#     p[0] = p[1]

# def p_unary_parenthesis(p):
#     'unary : LPAREN expression RPAREN'
#     p[0] = p[2]

# def p_unary_exponential(p):
#     'unary : exponential'
#     p[0] = p[1]

# def p_exponential_parenthesis(p):
#     'exponential : LPAREN expression RPAREN'
#     p[0] = p[2]

# def p_exponential_exponential(p):
#     'exponential : factorial EXPONENT term'
#     p[0] = p[1] ** p[3]

# def p_real_factorial(p):
#     'exponential : factorial FACTORIAL'
#     p[0] = math.factorial(p[1])

# def p_exponential_factorial(p):
#     'exponential : factorial'
#     p[0] = p[1]

# def p_repeat_factorial(p):
#     'factorial : factorial FACTORIAL'
#     p[0] = math.factorial(p[1])

# def p_factorial_parenthesis(p):
#     'factorial : LPAREN expression RPAREN'
#     p[0] = p[2]

# def p_to_number(p):
#     'factorial : NUMBER'
#     p[0] = p[1]

# def p_to_variable(p):
#     'factorial : IDENTIFIER'
#     p[0] = identifiers[p[1]]

# def p_to_function_0(p):
#     'factorial : FUNCTION_0'
#     p[0] = functions[0][p[1]]

# def p_to_function_1(p):
#     'factorial : FUNCTION_1'
#     p[0] = functions[1][p[1]]()

def p_empty(p):
    'empty :'
    p[0] = ""

calcparser = yacc.yacc()
