import numpy as np
nums = input("Enter the numbers separated by a space: ")
nums = np.fromstring(nums, dtype='int', sep=' ')
target = int(input("Enter the target sum: "))
L, R = 0, len(nums) - 1
ans = None  
while L < R:
    curr_sum = nums[L] + nums[R]
    if curr_sum == target:
        ans = [L + 1, R + 1]
        break  
    elif curr_sum > target:
        R -= 1 
    else:
        L += 1
if ans:
    print(f"The numbers are at indices {ans}")
else:
    print("No two numbers add up to that target.")