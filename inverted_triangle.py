num,rows=1,4
for i in range(rows,0,-1):
    print("  "*(rows-i),end="")
    for j in range(1,i+1):
        print(num,end=" ")
    num=num+1
    print()