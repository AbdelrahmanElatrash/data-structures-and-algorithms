
import pytest
from linked_list import  LinkedList 



ll=LinkedList()
# Test  empty linked list
def test_empty_ll():
    expected = "Empty LinkeList"
    actual = str(ll)
    assert expected == actual


# # Test inserting a single node into the linked list
# def test_insert_1_node():
    
#     ll.insert('a')
#     expected = '{ a } -> NULL'
#     actual = str(ll)
#     assert expected == actual


#  The head property will properly point to the first node in the linked list 
def test_head_is_first_node():
    ll.insert('a')
    assert ll.head.value == 'a'

#  Test inserting multiple nodes into the linked list
def test_inserting_multiple_nodes(reset_ll,insert):
    reset_ll
    insert
    expected = '{ c } -> { b } -> { a } -> NULL'
    actual = str(ll)
    assert expected == actual

#   Test includes method with a value that exists in the list  
def test_if_value_exists(insert):
    insert
    assert ll.includes('b') == True 

#  value that doesn't exist in the list   
def test_if_value_doesnt_exist(insert):
    insert
    assert ll.includes('e') == False


# Test to_string method
def test_to_string(insert,reset_ll):
    reset_ll
    insert
    assert str(ll) == '{ c } -> { b } -> { a } -> NULL'

#################################################################################################
@pytest.fixture
def insert():
    ll.insert('a')
    ll.insert('b')
    ll.insert('c')
    return ll
@pytest.fixture(autouse=True)
def reset_ll():
    
    ll.head = None
    yield ll
    ll.head = None
    
     












