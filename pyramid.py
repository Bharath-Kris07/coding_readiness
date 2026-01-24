rows=4
for i in range(1,rows+1):
    print("  "*(rows-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    for k in range(j-1,0,-1):
        print(k,end=" ")
    print()