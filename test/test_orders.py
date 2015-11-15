import sys
sys.path.append("..") 
sys.path.append("../calculator")
import pytest
import orders
import main

keywords = main.App(None,None).keywords


def test_valid_value():
    tok = orders.OrderToken(["printall"], keywords)
    assert tok.value == "printall"

@pytest.mark.parametrize("word", [word for word in keywords if 0 in keywords[word][0]] )
def test_all_valid_values_no_arg(word):
    assert orders.OrderToken([word], keywords).value == word


def test_invalid_value():
    with pytest.raises(ValueError) as err:
        tok = orders.OrderToken(["prin"], keywords)
    assert err.value.args[0] == "Invalid order: prin"

def test_invalid_argument():
    with pytest.raises(ValueError) as err:
        tok = orders.OrderToken(["print", 2, 3], keywords)
    assert err.value.args[0] == "Order \"print\" given invalid number of arguments (2), args: \"[2, 3]\""

    
def test_valid_arguement_list():
    tok = orders.OrderToken(["remove", "1,11,3"], keywords)
    assert tok.value == "remove" \
            and tok.args == [(1,11,3)]

def test_valid_arguement_range():
    tok = orders.OrderToken(["print", "1..5"], keywords)
    assert tok.value == "print" \
            and tok.args == [(1,2,3,4,5)]


def test_invalid_arguement_range():
    with pytest.raises(ValueError) as err:
        tok = orders.OrderToken(["replace", "6..2"], keywords)
    assert err.value.args[0] == "\"replace\" given invalid range \"6..2\", 6 more than 2"


class DataInputMethod:
    def __init__(self, data):
        self.data = data
        self.count = -1

    def __call__(self):
        self.count += 1
        return(data[self.count])

# def test_perform_order():
#     data = [
#         "3 + 7",
#         " 3 ^ 2",
#         "  @exit"
#         ]





