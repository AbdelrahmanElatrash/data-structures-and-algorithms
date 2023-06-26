
from .linked_list import LinkedList


class HashTable():

    def __init__(self,size=10) -> None:
        self.size=size                  # cardinality
        self.table= [[] for _ in range(self.size)]        # each element is a list of pairs



    # deterministic
    # fast to compute
    # desturbutes keys well
    # few collisions
    def hash(self, key):
        index=''
        return index


    def set_(self ,key ,vlaue):        
        pass

    def get(self , key):
        pass


    def has(self , key):
        pass

    def keys(self):
        pass