
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

    def in_order(self,root , arr=None):  # but arr in the method function can solve problem ?!
        """
        traversing tree using in order way
        return : an array of tree node values,
        """
        if arr is None:
            arr=[]
        if root :
            
            self.in_order(root.left,arr)  # Traverse left
            arr +=[root.value] # Traverse root
            self.in_order(root.right,arr)  # Traverse right
        
        return arr 
    

    def post_order(self,root , arr=None):
        """
        traversing tree using in post order way
        return : an array of tree node values,
        """
        if arr is None:
            arr=[]
        if root :
            self.post_order(root.left,arr) # Traverse left
            self.post_order(root.right,arr) # Traverse right
            arr +=[root.value] # Traverse root

        return arr 

    def pre_order(self, root,arr=None):  # if arr=[] give err in test AssertionError: assert ['a', 'b', '1... 'c', 50, ...] == [50, 30, 20, 40, 70, 60, ...]
        """
        traversing tree using in pre order way
        return : an array of tree node values,
        """
        if arr is None:
            arr=[]
        if root :
            arr +=[root.value] # Traverse root
            self.pre_order(root.left,arr) # Traverse left
            self.pre_order(root.right,arr) # Traverse right
        
        return arr
    
class Binary_Search_Tree(Tree):

    def __init__(self):
        super().__init__()  
        # super().__init__(value)    # here the value is inhert the int function in base clase it's Node 
        

    def add(self, value):
        """
        Adds a new node with that value in the correct location in the binary search tree.
        args:  value : int as a node value
        """
        if self.root is None:
            self.root = Node(value)
        else:
            self.root = self._insert_recursive(self.root, value)

        # if  self.root is None :
        #     self.root= Node(value)
        # else : 
        #     node=self.root
        #     if node is None:
        #         return Node(value)
        #     if value < node.value :
        #         node.left=self.add(node.left,value)
        #     elif value > node.value:
        #         node.right=self.add(node.right,value)

        # if value < root.value :
        #     root.left=self.add(root.left,value)
        # elif value > root.value:
        #     root.right=self.add(root.right,value)


    def _insert_recursive(self, node, value):
        """
        static method
        Adds a new node with that value in the correct location in the binary search tree.
        args: node : a node in the root of tree that we want insert to it 
        return : node value in the tree  
        """
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        return node
        
        
    # def add(self, value):
    #     if self.value is None:
    #         self.value = value
    #     elif value < self.value:
    #         if self.left is None:
    #             self.left = Binary_Search_Tree(value)
    #         else:
    #             self.left.add(value)
    #     else:
    #         if self.right is None:
    #             self.right = Binary_Search_Tree(value)
    #         else:
    #             self.right.add(value)   

    def contains(self,value):
        """
        find a value in a tree
        args: value :int the value want be searched
        return : boolien
        """
        
        if  self.root is None: 
            return False
        else :
            return self._search_b(self.root,value)


    def _search_b(self,node,value):
        
        if node is None :
            return False
        
        if node.value == value:
            return True
        
        if value < node.value:
            return self._search_b(node.left,value)
        elif value > node.value:
            return self._search_b(node.right,value)
        
        
if __name__=="__main__":

    # tree_1=Tree()
    # tree_1.root=Node("a")
    # tree_1.root.left=Node("b")
    # tree_1.root.right=Node("c")
    # tree_1.root.left.left=Node("1")
    # tree_1.root.left.right=Node("2")

    bst=Binary_Search_Tree()

    bst.add(50)
    bst.add(30)
    bst.add(70)
    bst.add(20)
    bst.add(40)
    bst.add(60)
    bst.add(80)
    

    # print(bst.in_order(bst.root)) 
    # # print(tree_1.in_order(tree_1.root))
    # print(bst.post_order(bst.root))
    print(bst.contains(70))
    print(bst.contains(15))



