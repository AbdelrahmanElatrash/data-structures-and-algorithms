try:
    from linked_list import LinkedList 
except :
    from .linked_list import LinkedList 


class HashTable():

    def __init__(self,size=10) -> None:
        self.size=size                  # cardinality
        self.hash_table= [None]*size     # we used linked list  #[[] for _ in range(self.size)]  each element is a list of pairs



    # deterministic
    # fast to compute
    # desturbutes keys well
    # few collisions
    def hash(self, key):
        """
        generate hash index 
        args : key > int , str
        return : index number > int 
        """
        h=0
        if isinstance(key,(int,float)):
            key=int(key)
        for ch in key :
            h += ord(ch)

        index= h % self.size
        return index


    def set(self ,key ,value):  
        """
        set the key and value pair in the table,
        args key : <int , str> , value :<any>
        return None
        """      
        hashed_key= self.hash(key)
        if not self.hash_table[hashed_key]:
            self.hash_table[hashed_key]=[key,value]

        else :   #  check if the index is linkedlist ornot 
            if isinstance(self.hash_table[hashed_key],LinkedList):
                self.hash_table[hashed_key].add([key,value])

            else :
                # create new linked list chine
                
                chine = LinkedList()   # create linked list instance

                new_value =[key , value]   # the new value pair
                exist_value=self.hash_table[hashed_key]    # sve existing value pair its only one value 
                self.hash_table[hashed_key]=chine        # let hashed_key  as instanse for linked list
                chine.add(exist_value)                  # add the oldest value as a head of linked list
                chine.add(new_value)                            
                


    def get(self , key):
        hashed_key=self.hash(key)

        if not self.hash_table[hashed_key] :
            return "no value "
        else :
            value_pairs=self.hash_table[hashed_key]

            if isinstance(value_pairs, LinkedList):
                return  value_pairs.__str__() 
            else :
                return value_pairs


    def has(self , key):
        hashed_key=self.hash(key)

        if self.hash_table[hashed_key]:
            return True
        return False

    def keys(self):
        key_collection=[]

        for key in self.hash_table:
            if key :
                if isinstance(key , LinkedList):
                    head=key.head.value[0]
                    key_collection.append(head)
                else :
                    key_collection.append(key[0])
            


        return key_collection 



    

if __name__=="__main__":

    hash_=HashTable()

    hash_.set('d','this d value')
#     hash_.set('5','this 5 value')
#     hash_.set('R','this R value')
#     hash_.set('Z','this Z value')
    print(hash_.get('d'))

#     for i in range(10):
#         print(hash_.hash_table[i])


#     print(hash_.keys())

#     print(hash_.has('cs'))