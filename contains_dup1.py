import numpy as np
def check(arr,count_dict):
    for num in arr:
        if num in count_dict:
            return False
        else:
            count_dict[num]=1
    return True
arr=input("Enter the numbers separated by a space:")
arr=np.fromstring(arr,dtype=int,sep=' ')
count_dict={}
check(arr,count_dict)