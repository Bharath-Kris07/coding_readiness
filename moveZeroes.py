import numpy as np
nums=input("Enter the numbers separated by a space:")
nums=np.fromstring(nums,dtype='int',sep=' ')
L=0
for R in range(len(nums)):
    if nums[R]!=0:
        nums[L],nums[R]=nums[R],nums[L]
        L+=1
print(f"The new array is {nums}")