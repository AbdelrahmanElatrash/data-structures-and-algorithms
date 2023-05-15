class Node:
    """
    node class
    """
    def __init__(self, value=None, next=None):
        """
        initiation a node wit value and next point"""
        self.value = value
        self.next = next

        
class Queue:
    """
    queue class
    """
    def __init__(self):
        """
        initation a queue front and back"""
        self.front = None
        self.back = None
        
    def enqueue(self, value):
        """
        add value to the queue
        arg : value --> any node value
        """
        new_node = Node(value)
        if self.is_empty():
            self.front = new_node
            self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node
            
    def dequeue(self):
        """
        delete a value from queue
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.back = None
        return value
    
    def peek(self):
        """
        return a peek value from queue
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.front.value
    
    def is_empty(self):
        """
        return true if the queue is empty else return false
        """
        return self.front is None