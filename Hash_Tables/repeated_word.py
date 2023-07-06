try:
    from hash_table import HashTable
except :
    from .hash_table import HashTable

def split_(str_):
    """
    split string to list remove any samol
    args : str_ string
    return list of splited str_
    """
    str_=str_.lower().replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace(":", "")   # or regex
    split_str=''
    split_list=[]
    for ch in str_:
        if ch !=' ':
           split_str +=ch
        else :
           split_list +=[split_str]
           split_str=''
           
    return split_list
    
   
# def repeated_word(str_):
#     split_list=split_(str_)
#     my_set=set()
#     for i in range(len(split_list)):
#           my_set.add(split_list[i])
#           if len(my_set) != i+1 :
#                return split_list[i]

def repeated_word(str_):
    """
    repeated word that finds the first word to occur more than once in a string
    args : str_ string
    return string <word occur more than once in a str_>
    """
    split_list=split_(str_)
    hash_=None
    hash_=HashTable()
    for item in split_list:
        
        value_pairs=hash_.get(item)   
          
        if  item in f'{value_pairs}': 
            return item  
                    
        hash_.set(item,item)
        
        
    return None

def count_word(str_):
    """
    return a count of each of the words in the provided string
    args : str_ string
    return : dict of word and countof it
    """
    split_list=split_(str_)
    hash_=None
    hash_=HashTable()
    
    word_counts = {}
    
    for item in split_list:
        
        value_pairs=hash_.get(item)
        
        if  item in f'{value_pairs}': 
            try:
                word_counts[item] += 1 
            except KeyError as e:
                  e
        else :
            word_counts[item] = 1 
            hash_.set(item,item)          
        
    return   word_counts   
        
def list_word(str_):
    """
    function to return a list of the words most frequently used in the provided string
    args : str_ string
    return list of most frequently used in the str_"""
    split_list=split_(str_)
    hash_=None
    hash_=HashTable()
    my_list=[]
    for item in split_list:
        
        value_pairs=hash_.get(item)     
        if  item in f'{value_pairs}': 
            my_list.append(item) 
                    
        hash_.set(item,item)
        
        
    return set(my_list)   
    

 
            