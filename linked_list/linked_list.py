class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    

#  Adds a new node with that value to the head of the list with an O(1) Time  // let last node == head 
    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
    
    def includes(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    def __str__(self):
        result = ""
      
        if not self.head :
            result = "Empty LinkeList"
        else :
            current_node = self.head
            while current_node:
                result += f"{{ {current_node.value} }} -> "
                current_node = current_node.next
            result += "NULL"
        return result
    



    
    def append(self, value):
        new_node = Node(value)
        if not self.head :
            self.head = new_node
        else:
            current= self.head
            while current.next :
                current=current.next
            current.next=new_node 


    def insert_before(self, value, new_value):
        # If the linked list is empty, we can't insert before anything
        if not self.head:
            return " linked list is empty"
        
        # If the first node has the value specified, we can just insert 
        if self.head.value == value:
            self.insert(new_value)


        else :
            
            current = self.head
            while current.next:
                if current.next.value == value:
                    # Found the node with the value specified
                    new_node = Node(new_value)
                    new_node.next = current.next
                    current.next = new_node
                    return ""
                current = current.next
        
           
        # Node with the value specified not found
        return "we not found the value that you want to insert befor"
    
    
    def insert_after(self, value, new_value):
        """
        Inserts a new node with the given new_value after the first node
        that has the value specified.
        """
        current = self.head
        while current:
            if current.value == value:
                # Found the node with the value specified
                new_node = Node(new_value)
                new_node.next = current.next
                current.next = new_node
                return ""
            current = current.next
        
        #  not found
        return "we not found the value that you want to insert befor"
    
    # Stretch Goal
    #  Once you’ve achieved a working solution, write an additional method to delete a node with the given value 
    # from the linked list. 

    def delete_node(self, value):
        """
        Deletes the first node with the given value from the linked list.
        """
        if not self.head:
            
            return " linked list is empty"
        
        if self.head.value == value:
            # If the first node has the value specified, we can just update the head
            self.head = self.head.next
        
        else : 
            current = self.head
            while current.next:
                if current.next.value == value:
                    # Found the node with the value specified
                    current.next = current.next.next
                    return ""
                current = current.next
        
        # Node with the value specified not found
        return " not found"
    

    def kth_from_end(self, k):
        """
         k: refere to  the location or index  starting from the end at pozition 0
        """
        if k < 0:
           raise Exception("negative number")
        
        elif not self.head :
            raise Exception ("list is empty")
        else :
            current = self.head
            length = 1
            while current.next:

                length += 1  
                current = current.next
            if k > length:
                raise Exception("out of range")

            current = self.head
            index=length -1
            for i in range(index -(k)):
                current = current.next

            return current.value
        

    def find_middle(self):

        if not self.head:
            raise Exception("list is empty")

        current = self.head
        length = 1
        while current.next:
            length += 1  
            current = current.next
        mid=length //2
        try :
            return LinkedList.kth_from_end(self,mid)
        except Exception as e:
            raise e


def get_length(head):
    """Returns the length of a linked list."""
    current = head
    count = 0
    while current:
        count += 1
        current = current.next
    return count
    
def zip_lists(ll1, ll2):
    """
    zip 2 linked list together 
    arg : ll1 : linked list , ll2 : linked list 
    return :  one linked list generated from the prevuce 2 linked list 
    """
    if not ll1:
        return ll2
    if not ll2:
        return ll1
    
    curr1 = ll1.head
    curr2 = ll2.head
    
    while curr1 and curr2:
        next1 = curr1.next
        next2 = curr2.next
        curr1.next = curr2
        curr2.next = next1
        curr1 = next1
        curr2 = next2
    
    return ll1
    
# ---------------------------------------------------------------------------
    

if __name__ == "__main__":

    ll1=LinkedList()
    ll2=LinkedList()

   