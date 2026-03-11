import numpy as np
height=input("Enter the heights separated by a space: ")
height=np.fromstring(height,dtype='int',sep=' ')
L,R=0,len(height)-1
max_water=0
while L<R:
    width=R-L
    current_water=min(height[L],height[R])*width
    max_water=max(max_water,current_water)
    if height[L]<height[R]: # If the left height is less than the right height, we can move the left pointer to try to find a taller line that might increase the water capacity.
        L+=1
    else:
        R-=1
print(f"The maximum amount of water that can be contained is: {max_water}")