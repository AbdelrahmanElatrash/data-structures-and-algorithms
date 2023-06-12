def insert_sort( sorted,value):
    """ 
    insert a new value in sorted list
    args : sorted list containes int
           value : int
    return : sorted list contain the new value
    """
    i=0
    
    while value > sorted[i]:
        i +=1
    while i < len(sorted):
        temp=sorted[i]
        sorted[i]=value
        value=temp
        i +=1
    sorted.append(value)
    return sorted

# print(insert_sort([2,4,8,9,11],7))

def selection_sort(arr):
    
    for j in range(len(arr)):
        minimum=arr[j]

        for i in range(j+1 ,len(arr)):
            x=arr[j]
            if arr[i] < minimum:
                minimum =arr[i]
                arr[j]=minimum 
                arr[i]=x
        

    return arr


def reversed(arr):
    reversd_list=[]
    i=-1
    while i >= -len(arr):
        reversd_list +=  [arr[i]]
        i -=1
    return reversd_list

