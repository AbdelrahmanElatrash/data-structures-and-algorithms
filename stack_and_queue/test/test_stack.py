import pytest
from stack import Stack

def test_stack():
    s = Stack()
    assert s.is_empty() == True
    s.push(1)
    assert s.peek() == 1
    s.push(2)
    assert s.peek() == 2
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.is_empty() == True
    try:
        s.pop()
    except Exception as e:
        assert str(e) == "Stack is empty"
    try:
        s.peek()
    except Exception as e:
        assert str(e) == "Stack is empty"
