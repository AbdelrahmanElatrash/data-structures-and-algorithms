import pytest
from array_insert_shift import insertShiftArray , remove_mid




def test_1():
    actual=insertShiftArray([1,2,3,4,5],8)
    expected=[1, 2, 3, 8, 4, 5]
    assert actual == expected

def test_2():
    actual= remove_mid([1, 2, 3, 8, 4, 5])
    expected=[1,2,3,4,5]
    assert actual == expected