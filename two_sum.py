import numpy as np
arr=input("Enter the numbers separated by a space:")
target=int(input("Enter the target sum:"))
arr=np.fromstring(arr,dtype='int',sep=' ')
seen={}
for i,num in enumerate(arr):
    needed=target-num
    if needed in seen:
        ans=[seen[needed],i]
    else:
        seen[num]=i
print(f"The index array is {ans}")