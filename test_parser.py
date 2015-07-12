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
        
    def test_mutiple_commands():
        parsed = Parser("@printall @numeric")
        assert "printall" in parsed.commands and "numeric" in parsed.commands

class TestTokenizer:
    def test_empty():
        tokenized = Tokenizer("")
        assert tokenized.commands == dict()
        assert tokenized.tokens == list()
        assert tokenized.split_input == list()

    def test_number():
        Tokenizer("5")
        assert tokenized.commands == dict()
        assert tokenized.tokens == ["INTEGER"]
        assert tokenized.split_input == ["5"]

    def test_float():
        Tokenizer("5.1234")
        assert tokenized.commands == dict()
        assert tokenized.tokens == ["FLOAT"]
        assert tokenized.split_input == ["INTEGER"]
    
    def test_mutiple():
        Tokenizer("\\alpha 5*3")
        assert tokenized.commands == dict()
        assert tokenized.tokens == ["VARIABLE", "INTEGER", "MULTIPLY", "INTEGER"]
        assert tokenized.split_input == ["\\alpha", "5", "*", "3"] 

    def test_complex():
        Tokenizer("5*sin(4)/a")
        assert tokenized.commands == dict()
        assert tokenized.tokens == ["INTEGER", "MULTIPLY", "SIN", "LBRAC", "INTEGER", "RBRAC", "DIVIDE", "VARIABLE"]
        assert tokenized.split_input == ["5", "*", "3", "sin", "(", "4", ")", "/", "a"] 

    def test_mix():
        Tokenizer("@replace(1) 5.4*\\beta+ ln(4)^3) ")
        assert tokenized.commands == {"replace": 1}
        assert tokenized.tokens == ["FLOAT", "VARIABLE", "PLUS", "LN", "LBRAC", "INTEGER", "RBRAC", "POWER", "INTEGER"]
        assert tokenized.split_input == ["5.4", "*", "\\beta", "+", "ln","(", "4", ")", "^","3") ] 


