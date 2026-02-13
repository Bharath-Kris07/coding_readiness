import numpy as np
arr=input("Enter the numbers separated by a space:")
arr=np.fromstring(arr,dtype='int',sep=' ')
count=0
candidate=None
for num in arr:
    if count==0:
        candidate=num
    if candidate==num:
        count+=1
    else:
        count-=1
print(f"The majority element is {candidate}")