import sys
sys.path.append("..") 
sys.path.append("../zero_cas")
import pytest
import main

def test_remove_ini_whitespace():
    assert( main.remove_ini_whitespace("   hello  ") == "hello  ")

# class TestCommands:
#     def test_get_commands()
#         assert main.tokenize_command("@ printall print 5 remove 1-5 insert 3") == [("printall, 

