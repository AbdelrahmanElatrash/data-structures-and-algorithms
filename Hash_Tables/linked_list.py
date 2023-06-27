
class Node():

    def __init__(self,value) -> None:
        self.value=value 
        self.next=None


class LinkedList():

    def __init__(self):
        self.head=None


    def __str__(self):
            values=[]
            current=self.head

            while current :
                values.append(current.value)
                current=current.next

            return f"{values}"
        

    def add(self,value):
            node=Node(value)

            if not self.head :
                self.head=node
            
            else :
                current=self.head

                while current.next :
                    current=current.next

                current.next=node
