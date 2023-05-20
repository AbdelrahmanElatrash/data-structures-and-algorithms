
class Node :

    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None



class Tree:

    def __init__(self):
        self.root=None 
        #self.travirsal=[]    # I dont know if this is best place for arr ? 
                             #no is not becouse all travirsal method will save inside it
                              # I sould init arr for each method ?

    def in_order(self,root , arr=[]):  # but arr in the method function can solve problem ?!
        """
        traversing tree using in order way
        return : an array of tree node values,
        """
        if root :
            
            self.in_order(root.left,arr)  # Traverse left
            arr +=[root.value] # Traverse root
            self.in_order(root.right,arr)  # Traverse right
        
        return arr 
    

    def post_order(self,root , arr=[]):
        """
        traversing tree using in post order way
        return : an array of tree node values,
        """

        if root :
            self.post_order(root.left) # Traverse left
            self.post_order(root.right) # Traverse right
            arr +=[root.value] # Traverse root

        return arr 

    def pre_order(self, root,arr=[]):
        """
        traversing tree using in pre order way
        return : an array of tree node values,
        """
        if root :
            arr +=[root.value] # Traverse root
            self.pre_order(root.left) # Traverse left
            self.pre_order(root.right) # Traverse right
        
        return arr
    
class Binary_Search_Tree(Tree):

    def __init__(self):
        super().__init__()
        

    def add(self,root=None,value=None):
        """
        Adds a new node with that value in the correct location in the binary search tree.
        args: root : a node in the root of tree that we want insert to it  
            value : int as a node value
        """
        if  root is None :
            root= Node(value)
        if value < root.value :
            root.left=self.add(root.left,value)
        if value > root.value:
            root.right=self.add(root.right,value)
        
        

    def contains(self):
        """
        find a value in a tree
        args: value :int the value want be searched
        return : boolien
        """
        pass

if __name__=="__main__":

    tree_1=Tree()
    tree_1.root=Node("a")
    tree_1.root.left=Node("b")
    tree_1.root.right=Node("c")
    tree_1.root.left.left=Node("1")
    tree_1.root.left.right=Node("2")

    tree=Binary_Search_Tree()

    tree.add(tree.root,7)
    tree.add(tree.root,3)
    # tree.add(4)
    # tree.add(8)
    # tree.add(11)
    # tree.add(6)

    print(tree.in_order(tree.root))

    print(tree_1.in_order(tree_1.root))
    print(tree_1.post_order(tree_1.root))
    print(tree_1.pre_order(tree_1.root))



