import numpy as np
def conquer(arr,start,mid,end):
    lmax=rmax=float('-inf')
    curr_lsum=curr_rsum=0
    for i in range(mid,start-1,-1):
        curr_lsum+=arr[i]
        lmax=max(curr_lsum,lmax) # find the max sum in the left subarray
    for i in range(mid+1,end+1):
        curr_rsum+=arr[i]
        rmax=max(curr_rsum,rmax) # find the max sum in the right subarray
    cross_max=lmax+rmax # find the max sum of the subarray crossing the mid element
    return max(cross_max,lmax,rmax) # return the max of the three values
def divide(arr,start,end):
    if start==end:
        return arr[start] # only one element in arr
    mid=(start+end)//2
    left_max=divide(arr,start,mid)
    right_max=divide(arr,mid+1,end)
# divide until single element,that element will be the max in that subarray
    cross_max=conquer(arr,start,mid,end)
    return max(left_max, right_max, cross_max)
arr=input("enter the numbers separated by a space :")
arr=np.fromstring(arr,dtype=int,sep=' ')
max_sum=divide(arr,0,len(arr)-1)
print(f"Maximum Subarray Sum is: {max_sum}")