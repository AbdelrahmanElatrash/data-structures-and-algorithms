import pytest
from pseudo_queue import Stack , PseudoQueue


pq = PseudoQueue()

def test_empty():
    try:
        pq.dequeue()
    except Exception as e:
        assert str(e)=="Can't dequeue from empty queue"
    

def test_pseudo_queue(append):
    append
    assert pq.dequeue() == 10
    pq.enqueue(40)
    assert pq.dequeue() == 20
    assert pq.dequeue() == 30
    assert pq.dequeue() == 40



#################################################################

@pytest.fixture
def append():
    pq.enqueue(10)
    pq.enqueue(20)
    pq.enqueue(30)
    return pq     