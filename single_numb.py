# Input: nums = [4,1,1]
# Output: 4
# 4^1 = 100^001 = 101 which is 5 (101 contains both bits of 4 and 1) 101^001 = 100 which is 4 (001 (1 in bits) is removed from result) 
def find_singlenumber(nums):
    res=0
    for i in nums:
        res^=i # xor function finds the single number.1^1 and 0^0 = 0 so same bits get deleted and returns the single value only   
    return res
nums=input("Enter the numbers:")
nums=list(map(int,nums.split())) # map converts each number entered as string separated by space to int
# same as writing nums=[int(x) for x in nums.split()] 
res=find_singlenumber(nums)
print(f"The single element is {res}")