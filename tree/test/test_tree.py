import pytest
from tree.tree import   Node ,Tree , Binary_Search_Tree


tree=Tree()
bst=Binary_Search_Tree()

def test_instantiate_empty_tree():
    empty_tree=Tree()
    empty_bst=Binary_Search_Tree()

    assert empty_tree.in_order(empty_tree.root) == []
    assert empty_bst.in_order(empty_bst.root) == []


def test_tree_traversal(insert):
    insert
    
    assert tree.in_order(tree.root)  == ['1', 'b', '2', 'a', 'c']
    assert tree.post_order(tree.root) == ['1', '2', 'b', 'c', 'a']
    assert tree.pre_order(tree.root) == ['a', 'b', '1', '2', 'c']



def test_add_to_bst(insert_bst,reset_ll): 
    reset_ll
    insert_bst
    assert bst.in_order(bst.root)  == [20, 30, 40, 50, 60, 70, 80]
    assert bst.post_order(bst.root) == [20, 40, 30, 60, 80, 70, 50]
    assert bst.pre_order(bst.root) == [50, 30, 20, 40, 70, 60, 80]

def test_contains(insert_bst):
    insert_bst

    assert bst.contains(70)==True
    assert bst.contains(15)==False

#################################################################################################


@pytest.fixture
def insert():
    tree.root=Node("a")
    tree.root.left=Node("b")
    tree.root.right=Node("c")
    tree.root.left.left=Node("1")
    tree.root.left.right=Node("2")

    return tree

@pytest.fixture
def insert_bst():

    bst.add(50)
    bst.add(30)
    bst.add(70)
    bst.add(20)
    bst.add(40)
    bst.add(60)
    bst.add(80)

    return bst

@pytest.fixture(autouse=True)
def reset_ll():
    
    bst = None
    # tree.root=None
    yield bst 
    bst = None
    # tree.root =None