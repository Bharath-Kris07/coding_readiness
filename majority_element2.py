import numpy as np
arr=input("Enter the numbers separated by a space:")
arr=np.fromstring(arr,dtype='int',sep=' ')
counts={}
win_condition=len(arr)//2
for num in arr:
    counts[num]=counts.get(num,0)+1
    if counts[num] > win_condition:
        print(f"The majority element is {num}")
        break