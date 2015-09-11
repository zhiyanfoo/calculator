class Parser:
    def __init__(self, inp):
        tokenized = Tokenizer(inp)
        top_left_recursive(tokenized)


    def shunting_yard(self, tokens):
        self.exp_tree = list()
        pass

class Tokenizer:
    def __init__(self, inp):
        #variable declerations modified from https://github.com/ebbes/MathParser/blob/master/Lexer.py
        self.operators = ['+', '-', '*', '/', '%', '=', '^']
        self.digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.digits_decimal_point = ['.'] + self.digits
        lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                        "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.characters = lower + upper
        self.name_elements = self.characters + self.digits
        tokenize(inp)

    def tokenize(self, inp):
        self.commands = None
        self.tokens = None 
        pass

class Token:
    def __init__(self, literal, tok_type):
        self.literal = literal 
        self.tok_type = tok_type
        
        used_func_operat = { 
            ("SIN", "LOG"): "FUNCTIONS",
            ("PLUS", "MINUS", "MULTIPLY", "DIVIDE", "EXP"): "OPERATORS" ,
            }

        # assign tokens categories to use in shunting yard algorithim
        found = False
        
        for key in used_func_operat:
            if self.tok_type in key:
                self.category = used_func_operat[key]
                found = True
                break
        if not found:
            self.category = self.tok_type

        self.assign_values
        

        

    def assign_values(tok_type):
        if tok_type == "PLUS":
            self.precedence = 500
            self.assoc = "LEFT"
        elif tok_type == "MINUS":
            self.precedence = 500
            self.assoc = "LEFT"
        elif tok_type == "MULTIPLY":
            self.precedence = "250"
            self.assoc = "LEFT"
        elif tok_type == "DIVIDE":
            self.precedence = 250 
            self.assoc = "LEFT"
        elif tok_type == "EXP":
            self.precedence = 0
            self.assoc = "RIGHT"
