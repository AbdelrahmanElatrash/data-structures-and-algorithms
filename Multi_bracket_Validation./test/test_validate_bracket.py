
import pytest
from stack_queue_brackets import validate_brackets

def test_valid_cases():
    assert validate_brackets("{}") == True
    assert validate_brackets("{}(){}") == True
    assert validate_brackets("()[[Extra Characters]]") == True
    assert validate_brackets("(){}[[]]") == True
    assert validate_brackets("{}{Code}[Fellows](())") == True

def test_invalid_cases():
    assert validate_brackets("[({}]") ==False
    assert validate_brackets("(](") ==False
    assert validate_brackets("{(})") ==False
