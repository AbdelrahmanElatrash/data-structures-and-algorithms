
def binarySearch(arr, k):  
    low= 0
    high=len(arr)-1
    try:
        while low <= high:
            mid = low + (high - low)//2
            if arr[mid] == k:
                return mid
            elif arr[mid] < k:
                low = mid + 1
            else:
                high = mid - 1
        return -1
        
    except Exception as e:
        raise (print(e))
        
    finally:
        print( 'nice to see you')



#print(binarySearch([-131, -82, 0, 27, 42, 68, 179],42))

# Stretch Goal
# What would you need to change if the array contained objects (sorted on a given property),
# and you were searching for certain property value? Write out the pseudocode.



def binarySearchDict(dict, k):  
    arr = list(dict.keys())
    low= 0
    high=len(arr)-1
    try:
        while low <= high:  
            mid = low + (high - low)//2
            
            if dict[arr[mid]] == k:
                return mid
            elif dict[arr[mid]] < k:
                low = mid + 1
            else:
                high = mid - 1
        return -1
        
    except Exception as e:
        raise (print(e))
        
    finally:
        print( 'nice to see you')


print(binarySearchDict({1:1, 2:2, 3:3,4:4}, 3))

