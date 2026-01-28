import numpy as np
def find_single(nums):
    return np.bitwise_xor.reduce(nums)
nums=input("Enter the numbers")
nums=np.fromstring(nums,dtype=int,sep=' ')
print(f"The single number is {find_single(nums)}")