import pytest
from ..hash_table import HashTable


hash_=HashTable()


def test_set_key_value():
    assert hash_.set('d','this d value')==None 

def test_get_value():
    assert hash_.get('d')==['d', 'this d value']

def test_if_key_exist():
    assert hash_.has('d')==True
    assert hash_.has('as')==False

def test_return_keys():
    assert hash_.hash("a")==7

def test_handel_collision():
    assert hash_.set('d','this d value')==None 

def test_hash_key_in_range():
    value=hash_.hash("a")
    assert value== value in range(10)