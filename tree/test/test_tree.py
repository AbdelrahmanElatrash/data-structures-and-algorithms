import pytest
from tree.tree import   Node ,Tree


tree=Tree()


def test_tree(insert):
    insert
    
    assert tree.in_order(tree.root)  == ['1', 'b', '2', 'a', 'c']
    assert tree.post_order(tree.root) == ['1', '2', 'b', 'c', 'a']
    assert tree.pre_order(tree.root) == ['a', 'b', '1', '2', 'c']



#################################################################################################


@pytest.fixture
def insert():
    tree.root=Node("a")
    tree.root.left=Node("b")
    tree.root.right=Node("c")
    tree.root.left.left=Node("1")
    tree.root.left.right=Node("2")

    return tree