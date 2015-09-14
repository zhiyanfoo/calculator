import sys
sys.path.append("..") 
sys.path.append("../zero_cas")
import pytest
import orders

def test_valid_value():
    tok = orders.OrderToken(["printall"])
    assert tok.value == "printall"

@pytest.fixture 
def keywords_no_arg():
    return [word for word in orders.OrderToken.keywords if 0 in orders.OrderToken.keywords[word]]

@pytest.fixture(params=keywords_no_arg())
def identity(request):
    return request.param

def test_all_valid_values_no_arg(identity):
    # for word in orders.OrderToken.keywords:
    #     if 0 in orders.OrderToken.keywords[word]:
    #         tok = orders.OrderToken([word])
    #         assert tok.value == word
    word = identity
    assert orders.OrderToken([word]).value == word


def test_invalid_token_value():
    with pytest.raises(ValueError) as err:
        tok = orders.OrderToken(["prin"])
    assert err.value.args[0] == "Invalid order: prin"

def test_invalid_token_argument():
    with pytest.raises(ValueError) as err:
        tok = orders.OrderToken(["print", 2, 3])
    assert err.value.args[0] == "Order \"print\" given invalid number of arguments (2), args: \"[2, 3]\""

    
def test_valid_token_arguement1():
    tok = orders.OrderToken(["remove", "1,11,3"])
    assert tok.value == "remove" \
            and tok.arg_type == ("list") \
            and tok.args[0] == (1,11,3)

# def test_valid_token_arguement():
#     tok = orders.OrderToken(["print", "1-5"])
#     assert tok.value == "print"
#     assert tok.arg_type == ("range")
#     assert tok.args == ((1,5))

