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
    
    assert tree.in_order(tree.root)  == ['5', '13', '14', '9', '7']
    assert tree.post_order(tree.root) == ['5', '14', '13', '7', '9']
    assert tree.pre_order(tree.root) == ['9', '13', '5', '14', '7']



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


def test_find_max(insert):
    insert
    assert tree.find_maximum_value()==14

def test_find_max_empty_tree(reset_ll):
    reset_ll
    assert tree.find_maximum_value()== "tree is empty"





#################################################################################################


@pytest.fixture
def insert():
    tree.root=Node("9")
    tree.root.left=Node("13")
    tree.root.right=Node("7")
    tree.root.left.left=Node("5")
    tree.root.left.right=Node("14")

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
    # bst = None
    tree.root =None