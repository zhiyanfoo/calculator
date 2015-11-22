import ply.lex as lex
import sys

literals = (
        "+",
        "-",
        "*",
        "/",
        "^",
        "!",
        "(",
        ")",
        "=",
        ",",
        )

tokens = (
        "NUMBER", 
        "IDENTIFIER",
        "FUNCTION_1",
        "FUNCTION_MULTI",
        )

def t_IDENTIFIER(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*"
    return t

def t_FUNCTION_1(t):
    r"\{[a-zA-Z_][a-zA-Z0-9_]*\$1\}"
    t.value = t.value[1:len(t.value)-3]
    return t

def t_FUNCTION_MULTI(t):
    r"\{[a-zA-Z_][a-zA-Z0-9_]*\$\+\}"
    t.value = t.value[1:len(t.value)-3]
    return t


def t_NUMBER(t):
    r"(\d*\.\d+|\d+)"
    t.value = float(t.value)
    return t


t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0], file=sys.stderr)
    t.lexer.skip(1)

