
import pytest
import search_in_array_binary

binarySearch=search_in_array_binary.binarySearch


def test_1_binarySearch():
    actual=binarySearch([1,2,3,4,5],8)
    expected=-1
    assert actual == expected

def test_2_binarySearch():
    actual= binarySearch([1, 2, 3, 4, 5,8],8)
    expected= 5
    assert actual == expected

def test_3_binarySearch():
    actual= binarySearch([0],8)
    expected= -1
    assert actual == expected

@pytest.mark.xfail()
def test_4_binarySearch():
    actual= binarySearch([1, 2, 3,8, 4, 5,],8)
    expected= -3
    assert actual == expected