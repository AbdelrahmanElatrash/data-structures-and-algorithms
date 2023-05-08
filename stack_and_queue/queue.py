from node import Node 

class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = new_node
            self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node
            
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.back = None
        return value
    
    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.front.value
    
    def is_empty(self):
        return self.front is None