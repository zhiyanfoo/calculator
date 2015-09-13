import sys
sys.path.append("..") 
sys.path.append("../zero_cas")
import pytest
import orders

def test_valid_value():
    tok = orders.OrderToken(["printall"])
    assert tok.value == "printall"

def test_all_valid_values_no_arg():
    for word in orders.OrderToken.keywords:
        if 0 in orders.OrderToken.keywords[word]:
            tok = orders.OrderToken([word])
            assert tok.value == word


def test_invalid_token_value():
    with pytest.raises(ValueError) as err:
        tok = orders.OrderToken(["prin"])
        assert err.args == "Invalid order: prin"

def test_invalid_token_argument():
    with pytest.raises(ValueError) as err:
        tok = orders.OrderToken(["print", 2, 3])
        assert err.args[0] == "Order \"print\" given invalid number of arguments (2), args: \"(2,3)\""

def test_valid_token_arguement():
    tok = orders.OrderToken(["remove", "1,11"])
    assert tok.value == "remove"
    assert tok.arg_type == ("list")
    assert tok.args[0] == (1,11)

def test_valid_token_arguement():
    tok = orders.OrderToken(["print", "1-5"])
    assert tok.value == "print"
    assert tok.arg_type == ("range")
    assert tok.args == ((1,5))

