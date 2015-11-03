import ply.lex as lex

tokens = (
        "NUMBER", 
        "PLUS", 
        "MINUS",
        "TIMES",
        "DIVIDE",
        "EXPONENT",
        "FACTORIAL",
        "LPAREN",
        "RPAREN",
        "ASSIGN",
        "IDENTIFIER",
        )

t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_EXPONENT = r"\^"
t_FACTORIAL = r"\!"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_ASSIGN = r"="

def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t

def t_IDENTIFIER(t):
    r"[a-zA-Z_](_[a-zA-Z0-9_]+|[0-9]+)?"
    return t

t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

