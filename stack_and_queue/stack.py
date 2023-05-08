from node import Node
class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        value = self.top.value
        self.top = self.top.next
        return value
    
    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.top.value
    
    def is_empty(self):
        return self.top is None