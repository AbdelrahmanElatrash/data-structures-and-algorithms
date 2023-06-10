import pytest
from tree.tree import Tree ,Node
from tree.tree_breadth import breadth_first



tree=Tree()

def test_breadth_first_empty_tree():
    assert breadth_first(tree.root) == 'tree is empty'




def test_breadth_first():
    
    tree.root=Node(2)
    tree.root.left=Node(7)
    tree.root.right=Node(5)
    tree.root.left.left=Node(2)
    tree.root.left.right=Node(6)
    tree.root.left.right.left=Node(5)
    tree.root.left.right.right=Node(11)
    tree.root.right.right=Node(9)
    tree.root.right.right.left=Node(4)

    assert breadth_first(tree.root) ==[2, 7, 5, 2, 6, 9, 5, 11, 4]



