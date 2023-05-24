try: 
    from tree.tree import Tree , Node 
except :
    from tree import Tree , Node 


def breadth_first(node):
    """
    travirsal tree by level travirsal method
    args : node : tree.root 
    return list of node values 
    """
    arr=[]
    if node :
        q=[node]

        while len(q)>0:
            poped=q.pop()
            arr.append(poped.value)
            if poped.left:
                q = [poped.left]+q
            if poped.right:
                q= [poped.right] + q 
        return arr 
    else :
        return "tree is empty"

    

   
    


# tree=Tree()
# tree.root=Node(2)
# tree.root.left=Node(7)
# tree.root.right=Node(5)
# tree.root.left.left=Node(2)
# tree.root.left.right=Node(6)
# tree.root.left.right.left=Node(5)
# tree.root.left.right.right=Node(11)
# tree.root.right.right=Node(9)
# tree.root.right.right.left=Node(4)


# print(breadth_first(tree.root))