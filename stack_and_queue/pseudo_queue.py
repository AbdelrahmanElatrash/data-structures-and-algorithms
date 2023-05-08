class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """ add value to the stack 
        arg : item : value -> any
        """
        self.items.append(item)

    def pop(self):
        """ remove the last value added to stack 
        return the value
        """
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        """ return the last value added to the stack """
        if not self.is_empty():
            return self.items[-1]
        
    def is_empty(self):
        return len(self.items) == 0   

class PseudoQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        """   pushes the new value onto stack1."""
        self.stack1.push(value)

    def dequeue(self):
        """   it pops all the elements from stack1 and pushes them onto stack2 in reverse order 
        if the stack2 is empty"""
        
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        if self.stack2.is_empty():
            raise IndexError("Can't dequeue from empty queue")
        return self.stack2.pop()