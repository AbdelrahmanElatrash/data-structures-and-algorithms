class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if not self.head :
            self.head = new_node
        else:
            current= self.head
            while current.next :
                current=current.next
            current.next=new_node 

#  Adds a new node with that value to the head of the list with an O(1) Time  // let last node == head 
    # def insert(self, value):
    #     new_node = Node(value)
    #     if not self.head:
    #         self.head = new_node
    #     else:
    #         new_node.next = self.head
    #         self.head = new_node
        
    
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
    

if __name__ == "__main__":

    link1=LinkedList()

    link1.insert('a')
    link1.insert('b')
    link1.insert('c')
    link1.insert('d')


    print(link1)