import numpy as np
arr=input("Enter the stock prices separated by a space:")
prices=np.fromstring(arr,dtype='int',sep=' ')
min_price=float('inf')
max_profit=0
for price in prices:
    if price < min_price:
        min_price=price
    else:
        profit=price-min_price
        max_profit=max(max_profit,profit)
print(f"The maximum profit is {max_profit}")