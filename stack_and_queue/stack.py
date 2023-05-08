from node import Node
class Stack:
    """ stack class"""
    def __init__(self):
        self.top = None
    
    def push(self, value):
        """
        add a value to the top of stack
        arg: value --> any to create node value
        """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        """
        remove the top value from the stack
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        value = self.top.value
        self.top = self.top.next
        return value
    
    def peek(self):
        """ return peek value in the top of stack"""
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.top.value
    
    def is_empty(self):
        """
        return true if the stack is empty else return false
        """
        return self.top is None