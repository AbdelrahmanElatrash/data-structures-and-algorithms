import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Hash_Tables.hash_table import HashTable

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
 



def tree_traverse(root,arr=None): 
        """
        traversing tree using in pre order way
        return : an array of tree node values,
        """
        if arr is None:
            arr=[]
        if root :
            arr +=[root.value] # Traverse root
            tree_traverse(root.left , arr) # Traverse left
            tree_traverse(root.right , arr) # Traverse right
        
        return arr
    

def tree_intersection(tree1, tree2):
    """
    Find common values in 2 binary trees.
    arrgs :
          tree1 and tree2 :  the node root for tree1 and tree2 
          return set of common values in the 2 2 binary trees """
    hash_table = HashTable()  # Create an instance of the HashTable      
    common_values = set()  # Set to store common values found in both trees
    
    if not tree1 or not tree2:
        return common_values
    
    traverse_list=  tree_traverse(tree1)
    
    for value in traverse_list:
        hash_table.set(value, True)    

    

    traverse_list_2=tree_traverse(tree2)
    
    for value in traverse_list_2:
        if hash_table.has(value):
            common_values.add(value)
        

    return common_values


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

# print(tree_traverse(tree_1))
# print(tree_traverse(tree_2))
# print(tree_traverse(tree_3))
print(tree_intersection(tree_1, tree_2))
print(tree_intersection(tree_2, tree_3))
print(tree_intersection(tree_1, tree_3))