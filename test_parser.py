from parser import Parser, Tokenizer

def is_app_equal(a, b):
    return round(int(a-b), 5) == 0


class TestParser:
    def test_empty():
        parsed = Parser("")
        assert parsed.exp_list == "" and parsed.commands == ""
    
    def test_no_changes():
        parsed = Parser("5")
        assert parsed.exp_tree == "5"

    def test_simple_commands():
        parsed = Parser("@printall")
        assert "printall" in parsed.commands
    
    def test_simple_commands_and_exp():
        parsed = Parser("@printall 1")
        assert "printall" in parsed.commands and parsed.exp_tree == "1"
        
    def test_multiple_commands():
        parsed = Parser("@printall @numeric")
        assert "printall" in parsed.commands and "numeric" in parsed.commands

class TestTokenizer:
    def test_empty():
        tokenized = Tokenizer("")
        assert tokenized.commands == dict()
        assert tokenized.tokens == list()

    def test_number():
        tokenized = Tokenizer("5")
        tok_types = ["NUMBER"]
        literals = ["5"]
        assert tokenized.commands == dict()
        for i in range(len(tokenized)):
            assert tokenized[i].tok_type == tok_types[i]
            assert tokenized[i].literal == literals[i]

    def test_float():
        tok_types = ["NUMBER"]
        literals = ["5.1234"]
        tokenized = Tokenizer("5.1234")
        assert tokenized.commands == dict()
        for i in range(len(tokenized)):
            assert tokenized[i].tok_type == tok_types[i]
            assert tokenized[i].literal == literals[i]
    
    def test_mutiple():
        tokenized = Tokenizer("a 5*3")
        tok_types = ["VARIABLE", "NUMBER", "MULTIPLY", "NUMBER"]
        literals = ["a", "5", "*", "3"]
        assert tokenized.commands == dict()
        for i in range(len(tokenized)):
            assert tokenized[i].tok_type == tok_types[i]
            assert tokenized[i].literal == literals[i]

    def test_complex():
        tokenized = Tokenizer("5*sin(4)/a")
        tok_types = ["NUMBER"]
        literals = ["5"]
        assert tokenized.commands == dict()
        assert tokenized.tokens == ["NUMBER", "MULTIPLY", "SIN", "LBRAC", "NUMBER", "RBRAC", "DIVIDE", "VARIABLE"]
        assert tokenized.split_input == ["5", "*", "3", "sin", "(", "4", ")", "/", "a"] 
        for i in range(len(tokenized)):
            assert tokenized[i].tok_type == tok_types[i]
            assert tokenized[i].literal == literals[i]

    def test_mix():
        tokenized = Tokenizer("@replace(1) 5.4*b+ ln(4)^3) ")
        tok_types = ["5.4", "*", "a", "+", "ln","(", "4", ")", "^","3")]
        literals = ["NUMBER", "MULTIPLY", "VARIABLE", "PLUS", "LN", "LBRAC", "NUMBER", "RBRAC", "POWER", "NUMBER"]
        assert tokenized.commands == {"replace": 1}
        for i in range(len(tokenized)):
            assert tokenized[i].tok_type == tok_types[i]
            assert tokenized[i].literal == literals[i]


