import numpy as np
def minSubArrayLen(self, target, nums):
    L = 0
    current_sum = 0
    min_length = float('inf') 
    for R in range(len(nums)):
        current_sum += nums[R]
        while current_sum >= target:
            min_length = min(min_length, R - L + 1)
            current_sum -= nums[L]
            L += 1
    if min_length == float('inf'):
        return 0
    else:
        return min_length
arr = input("Enter the array elements separated by a space: ")
arr = np.fromstring(arr, dtype='int', sep=" ")
target = int(input("Enter the target sum: "))
result = minSubArrayLen(target, arr)
print(f"The length of the smallest subarray with sum at least {target} is: {result}")