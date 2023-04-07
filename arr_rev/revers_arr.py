
def revers_arr(arr):
    rev_arr=[]
    i= len(arr)-1
    if not(len(arr)==0 or len(arr)==1):
       while i >=0 :
        rev_arr=rev_arr + [arr[i]]
        i -=1
       return rev_arr 
    else :   return "the arr can't reversed"

def revArr(arr):
    rev_arr=[]
    i=-1
    if not(len(arr)==0 or len(arr)==1):
        while i >= -(len(arr)):
            rev_arr = rev_arr + [arr[i]]
            i -=1

    return rev_arr


arr=[1,2,3,4,5]
print(revArr(arr))



