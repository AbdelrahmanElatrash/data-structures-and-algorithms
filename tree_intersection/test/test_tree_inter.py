import pytest 
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tree_intersection import   Node , tree_traverse , tree_intersection



tree_1=Node(5)
tree_1.left=Node(4)
tree_1.right=Node(7)
tree_1.left.left=Node(3)
tree_1.left.right=Node(6)
tree_1.right.right=Node(8)


tree_2=Node(4)
tree_2.left=Node(11)
tree_2.right=Node(7)
tree_2.left.left=Node(2)
tree_2.left.right=Node(6)
tree_2.right.right=Node(9)

tree_3=Node(8)
tree_3.left=Node(6)
tree_3.right=Node(11)
tree_3.left.left=Node(5)
tree_3.left.right=Node(8)
tree_3.right.right=Node(9)

def test_tree_traverse():
    assert tree_traverse(tree_1)==[5, 4, 3, 6, 7, 8]
    assert tree_traverse(tree_2)==[4, 11, 2, 6, 7, 9]
    assert tree_traverse(tree_3)==[8, 6, 5, 8, 11, 9]
    
    
def test_tree_intersection():
    assert tree_intersection(tree_1,tree_2)=={4, 6, 7}
    assert tree_intersection(tree_2,tree_3)=={9, 11, 6}
    assert tree_intersection(tree_1,tree_3)=={8, 5, 6}