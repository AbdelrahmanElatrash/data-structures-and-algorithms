
def revers_arr(arr):
    # return arr.revers() 
    rev_arr=[]
    for n in arr:
       rev_arr.insert(0,n)
    return rev_arr 

arr=[1,2,3,4,5]
print(revers_arr(arr))



