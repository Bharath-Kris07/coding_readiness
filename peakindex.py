import numpy as np
arr=input("Enter the array elements separated by a space: ")
arr=np.fromstring(arr,dtype='int',sep=" ")
L,R=0,len(arr)-1
while L<R:
    mid=(L+R)//2
    if arr[mid]<arr[mid+1]:
        L=mid+1
    else:
        R=mid
print(f"The index of the peak element is: {L}")