import ply.yacc as yacc
from calclex import tokens

identifiers = dict()

def p_assign_expression(p):
    'statement : IDENTIFIER ASSIGN expression'
    identifiers[p[1]] = p[3]

def p_statement(p):
    'statement : expression'
    p[0] = p[1]

def p_expression_plus(p):
    'expression : expression PLUS factor'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS factor'
    p[0] = p[1] - p[3]

def p_expression_factor(p):
    'expression : factor'
    p[0] = p[1]

def p_factor_multiplication(p):
    'factor : factor TIMES term'
    p[0] = p[1] * p[3]
    

def p_factor_divide(p):
    'factor : factor DIVIDE term'
    p[0] = p[1] / p[3]

def p_factor_term(p):
    'factor : term'
    p[0] = p[1]

def p_expression_number(p):
    'term : NUMBER'
    p[0] = p[1]

calcparser = yacc.yacc()




