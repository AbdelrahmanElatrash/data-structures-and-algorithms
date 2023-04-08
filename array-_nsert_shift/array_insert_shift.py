

def insertShiftArray(list ,value):
    if value :
        if not(len(list)==0 or len(list)==1):
           mid=len(list)//2+1
           list = list[0:mid] + [value] + list[mid:]  
    return list


def remove_mid(list):
    if not(len(list)==0 or len(list)==1):
        mid=len(list)//2+1
        list = list[0:mid-1] + list[mid:]  
    return list

list =[1,2,3,4,5]

print(insertShiftArray(list,8))
# print(list)
# print(remove_mid(insertShiftArray(list,8)))



    