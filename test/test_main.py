import sys
sys.path.append("..") 
sys.path.append("../zero_cas")
import pytest
import main

def test_remove_ini_whitespace():
    assert main.remove_ini_whitespace("   hello  ") == "hello  "

