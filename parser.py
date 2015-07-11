class Parser:
    def __init__(self, inp):
        tokenized = Tokenizer(inp)
        top_left_recursive(tokenized.tokens, tokenized.split_input)


    def top_left_recursive(self, tokens, split_input):
        self.exp_tree = list()
        pass

class Tokenizer:
    def __init__(self, inp):
        tokenize(inp)

    def tokenize(self, inp):
        self.commands = None
        self.tokens = None 
        self.split_input = None
        pass

