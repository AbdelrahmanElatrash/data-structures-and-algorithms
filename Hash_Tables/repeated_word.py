try:
    from hash_table import HashTable
except :
    from .hash_table import HashTable

def split_(str_):
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
    split_list=split_(str_)
    hash_=None
    hash_=HashTable()
    my_list=[]
    for item in split_list:
        
        value_pairs=hash_.get(item)   
        # print(value_pairs)   
        if  item in f'{value_pairs}': 
            my_list.append(item) 
                    
        hash_.set(item,item)
        
        
    return set(my_list)   
    

# str_1="It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn't know what I was doing in New York..."       
str_1 ="It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."   
# str_1="Once upon a time, there was a brave princess who..."
print(count_word(str_1)) 
# # repeated_word(str_1)
# # print(hash_.get('it'))    
            