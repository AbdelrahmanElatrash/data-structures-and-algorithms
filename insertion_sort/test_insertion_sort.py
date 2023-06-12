import pytest
from insertion_sort import insert_sort, selection_sort , reversed


def test_insert_sort():
    assert insert_sort([2,4,8,9,11],7) == [2,4,7,8,9,11]

def test_sort():

    assert selection_sort([5,4,2,1,3]) == [1,2,3,4,5]


def test_reversed():

    assert reversed([1,2,3,4,5]) == [5,4,3,2,1]