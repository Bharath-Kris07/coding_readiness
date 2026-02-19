import numpy as np
def check(arr):
    return len(arr) == len(set(arr))
arr=input("Enter the numbers separated by a space:")
arr=np.fromstring(arr,dtype='int',sep=' ')
if check(arr): 
    print("There are no duplicates in the array.")
else:  
    print("There are duplicates in the array.")