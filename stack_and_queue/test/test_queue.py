import pytest
from queue import Queue

def test_queue():
    q = Queue()
    assert q.is_empty() == True
    q.enqueue(1)
    assert q.peek() == 1
    q.enqueue(2)
    assert q.peek() == 1
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.is_empty() == True
    try:
        q.dequeue()
    except Exception as e:
        assert str(e) == "Queue is empty"
    try:
        q.peek()
    except Exception as e:
        assert str(e) == "Queue is empty"