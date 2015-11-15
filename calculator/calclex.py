import ply.lex as lex

literals = (
        '+',
        '-',
        "*",
        "/",
        "^",
        "!",
        "(",
        ")",
        "=",
        )

tokens = (
        "NUMBER", 
        "IDENTIFIER",
        "FUNCTION_0",
        "FUNCTION_1",
        )

def t_FUNCTION_0(t):
    r"\{[a-zA-Z_][a-zA-Z0-9_]*\$0\}"
    t.value = t.value[1:len(t.value)-3]
    return t

def t_FUNCTION_1(t):
    r"\{[a-zA-Z_][a-zA-Z0-9_]*\$1\}"
    t.value = t.value[1:len(t.value)-3]
    return t

def t_NUMBER(t):
    r"(\d*\.\d+|\d+)"
    t.value = float(t.value)
    return t

def t_IDENTIFIER(t):
    r"[a-zA-Z_](_[a-zA-Z0-9_]+|[0-9]+)?"
    return t

t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

