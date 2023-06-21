

def insert(sorted_,value):
    i=0

    while value > sorted_[i]:
        i +=1
        if len(sorted_)==i:
           break
        

    while i < len(sorted_):
        temp=sorted_[i]
        sorted_[i]=value
        value=temp
        i +=1
    sorted_.append(value)


def InsertionSort(list_):
    sorted_=[]
    sorted_.append(list_[0])

    for i in range(1, len(list_)):
        insert(sorted_, list_[i])
    
    return sorted_


# print(InsertionSort([8,4,23,42,16,15]))
