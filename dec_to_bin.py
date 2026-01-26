n=int(input("enter the decimal number:"))
m=n
bi="" # empty string to store the binary number
if n == 0 :
    print("0")
else:
    while n!=0:
        bi=str(n%2)+bi # remainder of n/2 is added to the left of binary string
        n//=2
    print(f"The binary of {m} is {bi}")