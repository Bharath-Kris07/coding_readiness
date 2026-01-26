n=input("Enter the binary number:")
de=0
if n=="0":
    print(0)
else:
    for j,i in enumerate(reversed(n)):
        de+=int(i)*2**j
        j+=1
    print(f"The decimal of {n} is {de}")