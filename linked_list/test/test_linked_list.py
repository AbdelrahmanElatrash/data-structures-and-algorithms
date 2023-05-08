
import pytest
from linked_list import  LinkedList , zip_lists



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

    #  Where k is greater than the length of the linked list
def test_k_greater_than_length(reset_ll,append):
    reset_ll
    append  # add 3 element  length =3
    try :
        ll.kth_from_end(4)
    except Exception as e :
        assert str(e)=="out of range"
    

#  Where k and the length of the list are the same
def test_k_same_length(reset_ll,append):
    reset_ll
    append  # add 3 element  length =3
    expected = "a"  # equal the head
    actual = ll.kth_from_end(3)
    assert expected == actual 

#  Where k is not a positive integer
def test_k_negative_number():
   try:
        ll.kth_from_end(-2)
   except Exception as e :
       assert str(e)=="negative number"
     

#  Where the linked list is of a size 1
def test_length_is_1(reset_ll):
    reset_ll
    ll.insert('a')
    assert ll.kth_from_end(0) == 'a'
    assert ll.kth_from_end(1) == 'a'
    try:
        ll.kth_from_end(2)
    except Exception as e:
        assert str(e)=="out of range"
    
    
# “Happy Path” where k is not at the end, but somewhere in the middle of the linked list
def test_k_in_mid(reset_ll,insert):
    reset_ll
    insert
    ll.insert('d')
    assert ll.kth_from_end(2) == "c"

# find mid list is empty
def test_find_mid(reset_ll):
    reset_ll
    try :
        ll.find_middle()
    except Exception as e :
        assert str(e)=="list is empty"

# test find the mid of linked list
def test_find_mid(reset_ll,insert):
    reset_ll
    insert
    assert ll.find_middle()=='b'
def test_zip_lists(reset_ll):
    # Test case 1: zipping two empty lists
    reset_ll
    ll1 = ll
    ll2 = ll
    assert str(zip_lists(ll1, ll2)) == 'Empty LinkeList'

# Test case 2: zipping a non-empty list with an empty list

    ll1 = LinkedList()
    ll2 = LinkedList()
    ll1.append(1)
    ll1.append(3)
    ll1.append(5)
    assert str(zip_lists(ll1, ll2)) == '{ 1 } -> { 3 } -> { 5 } -> NULL'

    # Test case 3: zipping two non-empty lists with equal length
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll1.append(1)
    ll1.append(3)
    ll1.append(5)
    ll2.append(2)
    ll2.append(4)
    ll2.append(6)
    assert str(zip_lists(ll1, ll2)) == "{ 1 } -> { 2 } -> { 3 } -> { 4 } -> { 5 } -> { 6 } -> NULL"

    # Test case 4: zipping two non-empty lists with different length
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll1.append(1)
    ll1.append(3)
    ll1.append(6)
    ll2.append(2)
    ll2.append(4)
    
    assert str(zip_lists(ll1, ll2)) == "{ 1 } -> { 2 } -> { 3 } -> { 4 } -> { 6 } -> NULL"

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












