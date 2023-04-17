
import pytest
from linked_list import  LinkedList 



ll=LinkedList()
# Test  empty linked list
def test_empty_ll():
    expected = "Empty LinkeList"
    actual = str(ll)
    assert expected == actual



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


# test add a node to the end of the linked list
def test_add_node_to_end_list(insert,reset_ll):
    reset_ll
    insert
    ll.append("this value")
    assert str(ll) == '{ c } -> { b } -> { a } -> { this value } -> NULL'

# add multiple nodes to the end of a linked list
def test_add_multiple_nodes_to_the_end(reset_ll,append):
    reset_ll
    append
    assert str(ll) == '{ a } -> { b } -> { c } -> NULL'

#  Can successfully insert a node before a node located i the middle of a linked list
def test_insert_node_before_node(reset_ll,append):
    reset_ll
    append
    ll.insert_before('b', 'x')
    assert str(ll) == '{ a } -> { x } -> { b } -> { c } -> NULL'

#  Can successfully insert a node before the first node of a linked list
def test_insert_node_before_first_node(reset_ll,append):
    reset_ll
    append
    ll.insert_before('a', 'x')
    assert str(ll) == '{ x } -> { a } -> { b } -> { c } -> NULL'

#  Can successfully insert after a node in the middle of the linked list
def test_insert_after_node(reset_ll,append):
    reset_ll
    append
    ll.insert_after('b', 'x')
    assert str(ll) == '{ a } -> { b } -> { x } -> { c } -> NULL'


# Can successfully insert a node after the last node of the linked list
def test_insert_after_last_node(reset_ll,append):   # use append method
    reset_ll
    append
    ll.append('x')
    assert str(ll) == '{ a } -> { b } -> { c } -> { x } -> NULL'

#  delete node 

def test_delete_node(reset_ll,append):
    reset_ll
    append
    ll.delete_node('b')
    assert str(ll) == '{ a } -> { c } -> NULL'

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
    
@pytest.fixture
def append():
    ll.append("a")
    ll.append("b")
    ll.append("c")
    return ll     












