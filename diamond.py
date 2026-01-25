n=4
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print('*',end="")
    if i != 1:
        print(" "*(2*i-3),end='*') # for spaces between stars (1-3-5)
    print()
for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    print('*',end='')
    if i!=1:
        print(" "*(2*i-3),end="*")
    print()