x=int(input("Enter the base: "))
n=int(input("Enter the exponent: "))
res=1.0
if n<0:
    x=1/x
    n=-n
while n:
    if n%2:
        res*=x
    x*=x
    n//=2
print(f"The result is {res}")