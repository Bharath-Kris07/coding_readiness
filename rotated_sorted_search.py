import numpy as np
def search(nums, target):
        L,R=0,len(nums)-1
        while L<=R:
            mid=(L+R)//2
            if nums[mid]==target:
                return mid
            if nums[L]<=nums[mid]:
                if nums[L]<=target and target<nums[mid]:
                    R=mid-1
                else:
                    L=mid+1
            else:
                if nums[mid]<target and target<=nums[R]:
                    L=mid+1
                else:
                    R=mid-1
        return -1
arr=input("Enter the rotated sorted array elements separated by a space: ")
arr=np.fromstring(arr,dtype='int',sep=" ")
target=int(input("Enter the target element: "))
result=search(arr,target)
print(f"The index of the target element is: {result}")