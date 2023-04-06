

def insertShiftArray(list ,value):
    mid=len(list)//2+1
    list = list[0:mid] + [value] + list[mid:]  
    return list


def remove_mid(list):
    mid=len(list)//2+1
    list = list[0:mid-1] + list[mid:]  
    return list

list =[1,2,3,4,5]

# print(insertShiftArray(list,8))
# print(list)
# print(remove_mid(insertShiftArray(list,8)))



    