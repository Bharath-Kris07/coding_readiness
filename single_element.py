import numpy as np
def singleNonDuplicate(nums):
    L,R=0,len(nums)-1
    while L<R:
        mid=(L+R)//2
        if mid%2==1:
            mid-=1
        if nums[mid]==nums[mid+1]:
            L=mid+2
        else:
            R=mid
        return nums[L]
arr=input("Enter the array elements separated by a space: ")
arr=np.fromstring(arr,dtype='int',sep=" ")
result=singleNonDuplicate(arr)
print(f"The single non-duplicate element is: {result}")