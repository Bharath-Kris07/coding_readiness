import numpy as np
string=input("Enter the numbers separated by spaces:")
arr=np.fromstring(string,dtype=int,sep=' ')
curr_max,curr_sum=arr[0],arr[0]
for i in arr[1:]:
    curr_sum=max(i,curr_sum+i) #to start a new subarray from i if its less than i+curr_sum
    curr_max=max(curr_max,curr_sum) 
print(f"The max number in the subarray is {curr_max}")