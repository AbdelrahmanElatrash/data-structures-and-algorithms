import pytest
from insertion_sort import InsertionSort ,insert


def test_insert_sort():
    assert InsertionSort([20,18,12,8,5,-2]) == [-2,5,8,12,18,20]
    assert InsertionSort([8,4,23,42,16,15])==[4,8,15,16,23,42]
    assert InsertionSort([5,12,7,5,5,7])==[5,5,5,7,7,12]
    assert InsertionSort([2,3,5,7,13,11])==[2,3,5,7,11,13]

